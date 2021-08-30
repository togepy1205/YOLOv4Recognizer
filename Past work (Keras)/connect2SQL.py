import pymysql
import sys
import datetime


host = '3.113.29.214'
user = 'eric'
passwd = '123456'
port = 3306
conninfo = {'host':host ,'port':port,'user':user , 'passwd': passwd, 'db':'store_db','charset':'utf8mb4'}

def con2SQL(result):
# 建立Connection物件
    try:
        conn = pymysql.connect(**db_settings)
        # 建立Cursor物件
        with conn.cursor() as cursor:
            # 新增資料SQL語法
            command = "INSERT INTO barsket(member_id, product_id, quantity, date)VALUES(%s, %s, %s, %s)"
            # 取 cart data
            barsket = CamRec.cam_recognizer(register_id)
            for i in barsket:
                cursor.execute(command, (i["member_id"], i["product_id"], i["quantity"], i["date"]))
            # 儲存變更, 關閉操作
            conn.commit()
            cursor.close()
            conn.close()

if __name__ == '__main()__':
    con2SQL(result)