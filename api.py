from flask import Flask, make_response, jsonify
import mysql.connector
import os
from mysql_config import HOST
from mysql_config import USER
from mysql_config import PASSWORD
from mysql_config import DATABASE

conexao = mysql.connector.connect(

    host=HOST,
    user=USER,
    password=PASSWORD,
    database=DATABASE
)

cursor = conexao.cursor()

##USERS LIST
getusers = f'SELECT users FROM manage_system'
cursor.execute(getusers)
users = cursor.fetchall()

listuser = list()
for usrs in users:
    listuser.append(
        {
            'b14361404c078ffd549c03db443c3fede2f3e534d73f78f77301ed97d4a436a9fd9db05ee8b325c0ad36438b43fec8510c204fc1c1edb21d0941c00e9e2c1ce2': usrs[0]
        }
    )


##PASSWORDS LIST
getpasswords = f'SELECT passwords FROM manage_system'
cursor.execute(getpasswords)
passwords = cursor.fetchall()

listpassword = list()
for pws in passwords:
    listpassword.append(
        {
            'b109f3bbbc244eb82441917ed06d618b9008dd09b3befd1b5e07394c706a8bb980b1d7785e5976ec049b46df5f1326af5a2ea6d103fd07c95385ffab0cacbc86': pws[0]
        }
    )

##STATUS LIST
statususer = f'SELECT status FROM manage_system'
cursor.execute(statususer)
status = cursor.fetchall()

liststatus = list()
for st in status:
    liststatus.append(
        {
            'status': st[0]
        }
    )


app = Flask (__name__)

# User Route
@app.route('/d3d92938c54d99e82a6e0509a517b80e02dcdb3851b96956cb50ce29ef22bc3178176d53f43584212ed7dcfed9136efa6c1ffe8081bec8c51a02566a105d32ef')
def page1():
    return make_response(
        jsonify(
        listuser
        )
    )

# Password Route
@app.route('/673a564541af31570f20969078a7c925711bf5f70c9ead75900d133f851bdedb604596579a10d5a7934bd8f01ee84a192022d974a0087daacdb1fdd1bf21e5ee')
def page2():
    return make_response(
        jsonify(
        dados=listpassword
        )
    )

#Status Users
@app.route('/d544de60d14b2c82e81028a3cebdc08a3c8012b2cbaaf0aa505e50e2d2931c36143e9a5ee79d35e9c5be342ec0cda0c73248a12eaece875463dcdf25014dd9e9')
def page3():
    return make_response(
        jsonify(
        dados=liststatus
        )
    )

app.run(host='0.0.0.0', port='80',debug=True)
