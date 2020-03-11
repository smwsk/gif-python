import pymysql
import config
class DbConnection(object):

    # 初始化
    def __init__(self):
        self.conn = None
        self.cursor = None
        self.connect()

    # 连接数据库
    def connect(self):
        self.conn = pymysql.connect(
            host=config.db_host,
            port=config.db_port,
            user=config.db_user,
            passwd=config.db_password,
            db=config.db_database,
            charset=config.db_charset
        )
        self.cursor = self.conn.cursor(cursor=pymysql.cursors.DictCursor)

    # 查询列表
    def query_table_info(self, sql, args=None):
        try:
            self.cursor.execute(sql,args)
            data = self.cursor.fetchall()  # 返回所有记录列表
            return data
        except Exception as e:
            print(e)
        finally:
            self.cursor.close()

    # 保存数据
    def save_table_info(self, sql, args=None):
        try:
            count = self.cursor.execute(sql, args)
            self.db.commit()
            return count
        except Exception as e:
            print(e)
            self.db.rollback()
        finally:
            self.cursor.close()
        return 0

    # 获取单条数据
    def get_one_row(self, sql, args= None):
        self.cursor.execute(sql, args)
        result = self.cursor.fetchone()
        return result

    # 更新数据
    def update_table_info(self, sql, args= None):
        count = self.cursor.execute(sql, args)
        self.conn.commit()
        return count

    def multi_update(self, sql, args=None):
        count = self.cursor.executemany(sql, args)
        self.conn.commit()
        return count

    # 删除数据
    def delete_table_row(self, sql, args=None):
        count = self.cursor.executemany(sql, args)
        self.conn.commit()
        return count

    # 进入with语句自动执行
    def __enter__(self):
        return self

    # 关闭数据库连接
    def close(self):
        self.cursor.close()
        self.conn.close()

    # 退出with语句块自动执行
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()