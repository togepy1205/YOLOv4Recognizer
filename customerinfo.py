import pymysql
import sys
import datetime
import time


host = '3.113.29.214'
user = 'eric'
passwd = '123456'
port = 3306
conninfo = {'host':host ,'port':port,'user':user , 'passwd': passwd, 'db':'store_db','charset':'utf8mb4'}

def check_register(register_id): #register_id 要指定的收銀櫃檯
    data = None
    try:
        conn = pymysql.connect(**conninfo)
        cursor = conn.cursor()
        select_register = f"select id , user from cash_register where id = '{register_id}'"
        cursor.execute(select_register)
        data = cursor.fetchall()
        print('ok')
    except:
        print('異常')
        print(sys.exc_info()[0])
        print(sys.exc_info()[1])
    finally:
        cursor.close()
        conn.close()
    return data[0][1]

def add_barsket(values): #register_id 要指定的收銀櫃檯
    try:
        conn = pymysql.connect(**conninfo)
        cursor = conn.cursor()
        add_sql = "insert into barsket(member_id ,product_id , quantity ,date) values( %s , %s , %s ,%s)"
        cursor.executemany(add_sql, values)
        conn.commit()
        print('傳送完成')
    except:
        print('異常')
        print(sys.exc_info()[0])
        print(sys.exc_info()[1])
    finally:
        cursor.close()
        conn.close()


 # for func. test
if __name__ == '__main__':
    time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    print(time)
    data = [('U23b61386d407b31635052bf2ee6da6df', 26081, 1, time )]
    add_barsket(data)
    # print(data)
