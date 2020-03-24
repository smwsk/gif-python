from collections import Iterable
from sqlalchemy import func
from utils.db_utils import *

class BaseModel(object):
    """基础模型."""

    _db_name = 'research'

    @class_dbsession(True)
    def add(self, session):
        u"""增.

        eg: a = MerchantBillDetail(id=1)
            a.add()
        """
        session.add(self)

    @classmethod
    @class_dbsession(True)
    def batch_add(cls, session, objs):
        """批量增加.

        eg: a = [MerchantBillDetail(id=1), MerchantBillDetail(id=2)]
            MerchantBillDetail.batch_add(a)
        """
        return session.add_all(objs)

    @classmethod
    @class_dbsession(True)
    def delete(cls, session, where_conds=[]):
        u"""删.

        eg: BaseModel.delete([BaseModel.a>1, BaseModel.b==2])
        """
        session.query(cls).filter(*where_conds).delete(
            synchronize_session='fetch')

    @classmethod
    @class_dbsession(True)
    def update(cls, session, update_dict, where_conds=[]):
        u"""更新.

        eg: BaseModel.update({'name': 'jack'}, [BaseModel.id>=1])
        """
        return session.query(cls).filter(*where_conds).update(
            update_dict,
            synchronize_session='fetch')

    @classmethod
    @class_dbsession(True)
    def join(cls, session, other_model, join_condition):
        u"""

        """
        return session.query(cls, other_model).join(
            other_model, *join_condition)

    @classmethod
    @class_dbsession(False)
    def query(cls, session, params, **where_conds):
        u"""查询.

        eg: BaseModel.query([BaseModel.id, BaseModel.name],
                filter=[BaseModel.id>=1],
                group_by=[BaseModel.id, BaseModel.name]
                order_by=BaseModel.id.desc(), limit=10, offset=0)
        """
        if not where_conds:
            if not set(where_conds.keys()).issubset(
                    {'filter', 'group_by', 'order_by', 'limit', 'offset'}):
                raise Exception('input para error!')
        cfilter = where_conds.pop('filter', None)
        group_para = where_conds.pop('group_by', None)
        order_para = where_conds.pop('order_by', None)
        limit = where_conds.pop('limit', None)
        offset = where_conds.pop('offset', None)
        query_first = where_conds.get('query_first', False)

        if not isinstance(params, Iterable):
            params = [params]
        squery = session.query(*params)
        if cfilter is not None:
            squery = squery.filter(*cfilter)
        if group_para is not None:
            squery = squery.group_by(*group_para)
        if order_para is not None:
            squery = squery.order_by(order_para)
        if limit is not None:
            squery = squery.limit(limit)
        if offset is not None:
            squery = squery.offset(offset)
        if query_first:
            return squery.first()
        return squery.all()

    @classmethod
    @class_dbsession(False)
    def __aggregate(cls, session, aggr_fun, params, where_conds=[]):
        u"""对参数进行聚合函数(sum, avg, max, min)计算.

        BaseModel.__aggregate(func.sum,
                            [BaseModel.id, BaseModel.num], [BaseModel.id==1])
        """
        if not isinstance(params, Iterable):
            params = [params]
        aggr_list = [aggr_fun(param) for param in params]
        re = session.query(*aggr_list).filter(*where_conds).one()
        if len(re) == 1:
            return re[0] or 0
        return [i or 0 for i in re]

    @classmethod
    def sum(cls, params, where_conds=[]):
        u"""求和.

        eg: BaseModel.sum([BaseModel.id], [BaseModel.id==1])
        """
        return cls.__aggregate(func.sum, params, where_conds)

    @classmethod
    def max(cls, params, where_conds=[]):
        u"""求最大值.

        eg: BaseModel.max([BaseModel.num], [BaseModel.id==2])
        """
        return cls.__aggregate(func.max, params, where_conds)

    @classmethod
    @class_dbsession(False)
    def count(cls, session, params, where_conds=[], distinct=False):
        u"""计数.

        eg: BaseModel.count([BaseModel.id, BaseModel.XXX], [BaseModel.id==2])
            BaseModel.count(BaseModel.id, [BaseModel.id==2], True)
        """
        if distinct:
            if isinstance(params, Iterable) and len(params) >= 2:
                re = session.query(func.count(
                    func.distinct(func.concat(*params))))\
                    .filter(*where_conds).one()[0]
            elif isinstance(params, Iterable):
                qp = params[0]
                re = session.query(func.count(func.distinct(qp))).filter(
                    *where_conds).one()[0]
            else:
                re = session.query(func.count(func.distinct(
                    params))).filter(*where_conds).one()[0]
        else:
            if not isinstance(params, Iterable):
                params = [params]
            re = session.query(*params).filter(*where_conds).count()
        return re

    @classmethod
    @class_dbsession(False)
    def simple_paging_query(cls, session, params, where_conds, page_size=100):
        """简单分页查询
        """
        total_count = cls.count([cls.id], where_conds)
        rv = []
        for offset in range(0, total_count, page_size):
            rv.extend(cls.query(
                params, filter=where_conds, offset=offset, limit=page_size
            ))
        return rv

    @classmethod
    def execute(cls, sql_str):
        with db_session(cls._db_name, commit=True) as session:
            return session.execute(sql_str)


    def model_serialize(model):
        from sqlalchemy.orm import class_mapper
        columns = [c.key for c in class_mapper(model.__class__).columns]
        return dict((c, getattr(model, c)) for c in columns)

    def list_model_serialize(list):
        result = []
        for model in list:
            result.append(model.model_serialize())
        return result