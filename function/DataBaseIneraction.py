import pymysql,traceback

def get_connect():
    return pymysql.connect(host="49.233.69.46",
                           user="jzh",
                           password="54879w",
                           db='db_app',
                           charset='utf8mb4')

#执行sql语句
def execute_sql(sql,args=()):
    print(sql,args)

    conn = get_connect()
    cur = conn.cursor()
    try:
        if 'SELECT' in sql: #方法为查询
            if args: #键值查询
                cur.execute(sql,args)
            else:    #不带where条件
                cur.execute(sql)
            result = cur.fetchall()
            print(type(result))
        else: #增删改
            result = cur.execute(sql,args) #返回值为受影响的行数
            print(result)
            if not result:
                traceback.print_stack()
        conn.commit()
    except Exception as e:
        #rollback in case there is any error
        print(e.args)
        conn.rollback()
        traceback.print_stack()
        raise Exception('excepion in sql_execute')
    cur.close()
    conn.close()
    return result

'''
数据库                  意义
t_userinfo              用户信息
t_bookinfo_isbn         ISBN查询到的书籍信息
t_bookinfo_user         用户设置的书籍信息
'''

'''
    t_userinfo
    增  不对空选项进行处理 
    删  根据userId删除
    改  根据userId或userName进行更新
    查  根据userId或userName或全部进行查找
'''
#新增用户
#先不支持取昵称和注册时上传头像这样的功能
def insert_t_userinfo(userName,passWord,nickName=None,userIcon=None):
    sql = 'INSERT INTO t_userinfo VALUES(NULL,%s,%s,%s,%s);'
    try:
        execute_sql(sql,(userName,passWord,nickName,userIcon))
    except:
        raise Exception('insert_t_userinfo数据库连接出错')

#根据用户Id去注销用户
def delete_t_userinfo(usrId):
    sql = 'DELETE FROM t_userinfo WHERE userId = %s;'
    try:
        result = execute_sql(sql,(usrId,))
        return result
    except:
        raise Exception('delete_t_userinfo数据库连接出错')

#根据用户的Id来更新用户
#返回的是错误结果
def update_t_userinfo(userId=None,userName=None,passWord=None,nickName=None,userIcon=None):
    #为空的不需要更新
    msg = ''
    if userName :#判断重名
        if userName == query_t_userinfo(userId=userId,userName=userName):
            msg += 'update userName failed'
        else:
            sql = 'UPDATE t_userinfo SET userName = %s WHERE userId=%s;'
            if execute_sql(sql,(userName,userId)) != 1:
                msg += 'update userName failed'
    if passWord :
        sql = 'UPDATE t_userinfo SET passWord = %s WHERE userId=%s;'
        if execute_sql(sql,(passWord,userId)) != 1:
            msg += 'update passWord failed'
    if nickName :
        sql = 'UPDATE t_userinfo SET nickName = %s WHERE userId=%s;'
        if execute_sql(sql,(nickName,userId)) != 1:
            msg += 'update nickName failed'
    if userIcon :
        sql = 'UPDATE t_userinfo SET userIcon = %s WHERE userId=%s;'
        if execute_sql(sql,(userIcon,userId)) != 1:
            msg += 'update userIcon failed'
    return msg
#根据用户的Id或者用户的名称来搜索用户
#不传入参数则是搜索所有用户
def query_t_userinfo(userId=0,userName=None):
    if userId != 0:
        sql = 'SELECT * FROM t_userinfo WHERE userId=%s'
        return execute_sql(sql,(userId,))
    elif userName:
        sql = 'SELECT * FROM t_userinfo WHERE userName=%s'
        return execute_sql(sql,(userName,))    

'''
    t_bookinfo_isbn
    增  不对空选项进行处理 
    删  根据ISBN号进行删除
    改  不支持修改
    查  根据ISBN号进行查找或全部进行查找
'''
#新增isbn记录
def insert_t_bookinfo_isbn(levelNum,subTitle,author,date,imagesMedium,imagesLarge,publisher,isbn,title,summary):
    sql = 'INSERT INTO t_bookinfo_isbn VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);'
    return execute_sql(sql,(levelNum,subTitle,author,date,imagesMedium,imagesLarge,publisher,isbn,title,summary))

#删除
def delete_t_bookinfo_isbn(isbn):
    sql = 'DELETE FROM t_bookinfo_isbn WHERE isbn = %s;'
    execute_sql(sql,(isbn,)) 

def query_t_bookinfo_isbn(isbn):
    if isbn:
        sql = 'SELECT * FROM t_bookinfo_isbn WHERE isbn=%s;'
        return execute_sql(sql,(isbn,))
    else:
        sql = 'SELECT * FROM t_bookinfo_isbn;'
        return execute_sql(sql) 

'''
    t_bookinfo_user
    增  
    删  根据主键删除
    改  根据bookId修改tag1,tag2,place,isGroupVisible,lend
    查  根据bookId，isGroupVisible,tag1,tag2,place,userId,lend
'''
#新增书籍（实体）
#mysql没有布尔类型实质输入的是1或者0
#bookId 插入为null 交由自增完成
def insert_t_bookinfo_user(userId,isbn,tag1,tag2,place,isGroupVisible,lend):
    sql = 'INSERT INTO t_bookinfo_user VALUES(NULL,%s,%s,%s,%s,%s,%s,%s);'
    return execute_sql(sql,(userId,isbn,tag1,tag2,place,isGroupVisible,lend))

#根据书籍Id来删除实体书
def delete_t_bookinfo_user(bookId):
    sql = 'DELETE FROM t_bookinfo_user WHERE booKId = %d;'
    execute_sql(sql,(bookId,))

#根据书籍Id来更新实体书
def update_t_bookinfo_user(bookId,tag1='',tag2='',place='',isGroupVisible='',lend=''):
    #为空的不需要更新
    if tag1 :
        sql = 'UPDATE t_bookinfo_user SET tag1 = %s WHERE bookId=%d;'
        execute_sql(sql,(tag1,bookId))
    if tag2 :
        sql = 'UPDATE t_bookinfo_user SET tag2 = %s WHERE bookId=%d;'
        execute_sql(sql,(tag2,bookId))
    if place :
        sql = 'UPDATE t_bookinfo_user SET place = %s WHERE bookId=%d;'
        execute_sql(sql,(place,bookId))
    if isGroupVisible :
        sql = 'UPDATE t_bookinfo_user SET isGroupVisible = %d WHERE bookId=%d;'
        execute_sql(sql,(isGroupVisible,bookId))
    if lend :
        sql = 'UPDATE t_bookinfo_user SET lend = %d WHERE bookId=%d;'
        execute_sql(sql,(lend,bookId))    

#根据bookId，isGroupVisible,tag1,tag2,place,userId，lend
#bookId 返回全部信息，其他则只返回对应的bookId列表
def query_t_bookinfo_user(bookId=None,isGroupVisible=2,isbn='',tag1='',tag2='',place='',userId='',lend=2):
    if bookId:
        sql = 'SELECT * FROM t_bookinfo_user WHERE bookId=%s;'
        return execute_sql(sql,(bookId,))
    if isbn:
        sql = 'SELECT bookId FROM t_bookinfo_user WHERE isbn=%s;'
        return execute_sql(sql,(isbn,))         
    if isGroupVisible != 2:
        sql = 'SELECT bookId FROM t_bookinfo_user WHERE isGroupVisible=%s;'
        return execute_sql(sql,(isGroupVisible,))
    if tag1:
        sql = 'SELECT bookId FROM t_bookinfo_user WHERE tag1=%s;'
        return execute_sql(sql,(tag1,))  
    if tag2:
        sql = 'SELECT bookId FROM t_bookinfo_user WHERE tag2=%s;'
        return execute_sql(sql,(tag2,))  
    if place:
        sql = 'SELECT bookId FROM t_bookinfo_user WHERE place=%s;'
        return execute_sql(sql,(place,))  
    if userId:
        sql = 'SELECT bookId FROM t_bookinfo_user WHERE userId=%s'
        return execute_sql(sql,(userId,))  
    if lend != 2:
        sql = 'SELECT bookId FROM t_bookinfo_user WHERE lend=%s'
        return execute_sql(sql,(lend,))
    else:
        sql = 'SELECT * FROM t_bookinfo_user;'
        return execute_sql(sql)          








