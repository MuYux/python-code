from flask import Flask
from flask import render_template
from flask import request
import sqlite3
import datetime

def databaseIsHaving():
    conn = sqlite3.connect('msg.db')
    cursor = conn.cursor()
    cursor.execute('drop table if exists message ')
    cursor.execute('create table message (id varchar(50) primary key, name varchar(50),time varchar(50),msg varchar(200))')
    # 关闭Cursor:
    cursor.close()
    # 提交事务:
    conn.commit()
    # 关闭Connection:
    conn.close()
def select():
    conn = sqlite3.connect('msg.db')
    cursor = conn.cursor()
    sql = "select * from message"
    cursor.execute(sql)
    values = cursor.fetchall()
    # 关闭Cursor:
    cursor.close()
    # 提交事务:
    conn.commit()
    # 关闭Connection:
    conn.close()
    return values
def insert(id,name,time,msg):
    conn = sqlite3.connect('msg.db')
    cursor = conn.cursor()
    sql = "insert into message (id,name ,time ,msg) values ('{}' ,'{}' ,'{}' ,'{}')".format(str(id),str(name),str(time),str(msg))
    cursor.execute(sql)
    # 关闭Cursor:
    cursor.close()
    # 提交事务:
    conn.commit()
    # 关闭Connection:
    conn.close()
app = Flask(__name__)
@app.route('/',methods=['GET'])
def index():
    lists =[]
    value=select()
    print(value)
    for i in value:
        tmp={}
        tmp['id']=i[0]
        tmp['name']=i[1]
        tmp['time']=i[2]
        tmp['msg']=i[3]
        lists.append(tmp)
    return render_template('index.html',list=lists)
@app.route('/',methods=['POST'])
def tj():
    username = str(request.form['user_name'])
    usermsg = str(request.form['user_msg'])
    time=str(datetime.datetime.now())
    value = select()
    id = str(len(value)+1)
    insert(id,username,time,usermsg)
    value = select()
    lists =[]
    for i in value:
        tmp={}
        tmp['id']=i[0]
        tmp['name']=i[1]
        tmp['time']=i[2]
        tmp['msg']=i[3]
        lists.append(tmp)
    return render_template('index.html', list=lists)
if __name__ == '__main__':
    app.run()
