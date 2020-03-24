import functools

from sqlalchemy import create_engine
from contextlib import contextmanager
from sqlalchemy.orm import scoped_session, sessionmaker

# 数据库连接配置
MYSQLINFO = {
    'gif': {
        'user': 'root',
        'passwd': 'root',
        'host': '127.0.0.1',
        'port': 3306,
        'db': 'gif',
    },
    'comic': {
        'user': 'root',
        'passwd': 'root',
        'host': '127.0.0.1',
        'port': 3306,
        'db': 'comic',
    }
}

engines = {}

def init_engines():
    """初始化数据库连接"""
    for k, v in MYSQLINFO.items():
        mysql_url = ("mysql+pymysql://{user}:{passwd}@{host}:{port}/{db}"
                     "?charset=utf8".format(**v))
        engines[k] = create_engine(mysql_url,
                                   pool_size=10,
                                   max_overflow=-1,
                                   pool_recycle=1000,
                                   echo=True)

# 初始化所有数据库的连接，后续如果新增数据库访问，在MYSQL里面直接加入数据库配置即可
init_engines()


def get_session(db):
    """获取session"""
    return scoped_session(sessionmaker(
        bind=engines[db],
        expire_on_commit=False))()


@contextmanager
def db_session(db='research', commit=True):
    """db session封装.

    :params db:数据库名称
    :params commit:进行数据库操作后是否进行commit操作的标志
                   True：commit, False:不commit
    """
    session = get_session(db)
    try:
        yield session
        if commit:
            session.commit()
    except Exception as e:
        session.rollback()
        raise e
    finally:
        if session:
            session.close()

def class_dbsession(commit=True):
    """用于BaseModel中进行数据库操作前获取dbsession操作.

    :param commit:进行数据库操作后是否进行commit操作的标志，True：commit, False:不commit
    """
    def wrapper(func):
        @functools.wraps(func)
        def inner(*args, **kwargs):
            # cls为对象或类
            cls = args[0]
            # 实际传入的参数
            new_args = args[1:]
            with db_session(cls._db_name, commit) as session:
                return func(cls, session, *new_args, **kwargs)
        return inner
    return wrapper

