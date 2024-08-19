from common import commonUtils
from common import sqlBase


@sqlBase.connect_sql
def init_sql(conn):
    cuVersion = 0
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE name='user_list'")
    passwd = None
    if cursor.fetchone() is None:
        passwd = commonUtils.generatePasswd()
        cursor.execute("create table user_list("
                       "id integer primary key autoincrement,"
                       "userName text,"                             # 用户名
                       "passwd text,"                               # 密码
                       f"sqlVersion integer DEFAULT {cuVersion},"   # 数据库版本
                       "createTime integer DEFAULT (strftime('%s', 'now'))"
                       ")")
        cursor.execute("insert into user_list(userName, passwd) values ('admin', ?)",
                       (commonUtils.passwd2md5(passwd), ))
        conn.commit()
    else:
        cursor.execute("SELECT sqlVersion FROM user_list limit 1")
        sqlVersion = cursor.fetchone()[0]
        if sqlVersion < cuVersion:
            # do sth
            conn.commit()
    cursor.close()
    return passwd
