import pymysql
import datetime
from settings import Settings

CONST_TB_NAME = "TB_CALC_ELEVEN"
CONST_TB_SELECT = "select * from " + CONST_TB_NAME
CONST_TB_COUNT = "select count(*) from " + CONST_TB_NAME
CONST_TB_CREATE = """create table %s(
    ID INT(6) not null primary key auto_increment,
    WORK_DATE DATE not null,
    QUESTION VARCHAR(64) not null,
    ANSWER VARCHAR(32) not null,
    RESULT TINYINT(1)not null,
    USAGE_TIME DOUBLE(8,2) not null
);""" % (CONST_TB_NAME)
CONST_TB_DROP = "DROP TABLE IF EXISTS " + CONST_TB_NAME


class c_db():
    def __init__(self):
        settings = Settings()
        # 连接配置信息
        self.conn = pymysql.connect(host=settings.db_ip,
                                    port=3306,
                                    user='root',
                                    password='chenc',
                                    db='db_eleven',
                                    charset='utf8mb4',
                                    cursorclass=pymysql.cursors.DictCursor)
        # 创建连接
        self.cur = self.conn.cursor()

    def __del__(self):
        self.cur.close()
        self.conn.close()

    def tb_drop(self):
        self.cur.execute(CONST_TB_DROP)

    def tb_create(self):
        self.cur.execute(CONST_TB_CREATE)

    def tb_insert(self, str_question, str_answer, n_result, f_usage_time):
        dt = datetime.datetime.now().strftime('%Y-%m-%d')
        sql = """INSERT INTO %s(
            WORK_DATE, QUESTION, ANSWER, RESULT, USAGE_TIME)
            VALUES ('%s', '%s', '%s', '%d', '%f');""" % (CONST_TB_NAME, dt,
                                                         str_question, str_answer, n_result, f_usage_time)
        # print(sql)

        try:
            self.cur.execute(sql)
            self.conn.commit()
        except Exception as e:
            print("Error to insert table:", e)
            self.conn.rollback()

    def tb_select(self, str_filter='', str_select=CONST_TB_SELECT):
        if len(str_filter) == 0:
            str_sql = str_select
        else:
            str_sql = str_select + ' WHERE ' + str_filter

        # print(str_sql)
        self.cur.execute(str_sql)
        # for r in self.cur:
        # print(r)

        return self.cur.fetchall()

    def tb_count_today(self):
        dt = datetime.datetime.now().strftime('%Y-%m-%d')
        str = "WORK_DATE='%s'" % dt
        data = self.tb_select(str, CONST_TB_COUNT)
        count = data[0]['count(*)']

        str = "WORK_DATE='%s' AND RESULT=0" % dt
        data = self.tb_select(str, CONST_TB_COUNT)
        fault = data[0]['count(*)']

        return count, fault


if __name__ == '__main__':
    db = c_db()
    db.tb_select('RESULT = 0')
    print('\n')
    db.tb_select('USAGE_TIME > 15')
    print('\n')

    print(db.tb_count_today())
