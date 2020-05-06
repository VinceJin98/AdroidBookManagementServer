import sys
sys.path.append('..')
from function.DataBaseIneraction import insert_t_userinfo,delete_t_userinfo,update_t_userinfo,query_t_userinfo

class UserModel(object):

    #初始化对象
    #给用户类进行赋值
    #数据库返回的是[(userId,userName,passWord,nickName,userIcon)]
    def __init__(self,UserId=0):
        if UserId:
            result = query_t_userinfo(userId=UserId)
            if result:
                self.UserId = result[0][0]
                self.UserName = result[0][1]
                self.PassWord = result[0][2]
                self.NickName = result[0][3]
                self.userIcon = result[0][4]


    #登录之后返回userId,失败返回0
    #数据库返回的是[(userId,passWord)]
    @staticmethod
    def login(userName,passWord):
        result = query_t_userinfo(userName=userName)
        print(result[0][0],result[0][1])
        try:
            if result[0][2] == passWord:
                return result[0][0]
            else: #密码不匹配
                return 0
        except: #查询不到返回空
                return 0

    #注册，成功返回userId，失败返回0
    #失败可能原因：1.数据库连接断了 2. userName已经注册过
    @staticmethod
    def rigister(userName,passWord):
        #检查userName是否已经使用过
        result = query_t_userinfo(userName=userName)
        if not result: #未使用过 
            #注册时不支持取昵称和上传头像
            insert_t_userinfo(userName,passWord)
            result = query_t_userinfo(userName=userName)
            return result[0][0]
        else:
            return 0

    #登出
    @staticmethod
    def logout(userId):
        return True

    #注销账号
    #失败可能原因 1.注销了别人的id（基本不可能的场景）2.数据库连接断掉
    def CloseAccount(self,userId):
        result = delete_t_userinfo(userId)
        if result != 1: #被删除的不止自己
            return False
        else:
            return True

    #修改用户信息
    @staticmethod
    def ChangeUserInfo(userId=0,userName=None,passWord=None,userIcon=None):
        result = update_t_userinfo(userId=userId,userName=userName,passWord=passWord,userIcon=userIcon)
        return result
    
    @staticmethod
    def QueryUserInfo(userId=0,userName=None):
        if userId:
            return UserModel(userId).__dict__
        else: 
            userId = query_t_userinfo(userName=userName)
            return UserModel(userId).__dict__

    


