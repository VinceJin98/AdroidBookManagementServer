import sys
sys.path.append('..')
from Model.UserModel import UserModel
from View.UserView import UserView

class UserController(object):
    #初始化，有model 和 view作为属性
    def __init__(self):
        self.model = UserModel()
        self.view = UserView()

    #登录控制器
    #传入的参数为登录提供的表单 例子为 {userName: passWord: }
    def UserLoginController(self,request):
        userName = request['userName']
        passWord = request['passWord']

        userId = self.model.login(userName,passWord)
        res = self.view.UserLoginView(userId)
        return res 

    #登录控制器
    #传入的参数为注册提供的表单 例子为 {userName: passWord: }
    def UserRigisterController(self,request):
        userName = request['userName']
        passWord = request['passWord']

        userId = self.model.rigister(userName,passWord)
        res = self.view.UserRegisterView(userId)
        return res 

    #登出控制器
    #传入的参数为登出提供的表单 ，userId
    def UserLogOutController(self,request):
        userId = int(request['userId'])

        result = self.model.logout(userId)
        res = self.view.UserLogOutView(result)
        return res 
    
    #删除控制器
    #传入的参数为删除提供的表单 ，userId
    def UserCloseAccountController(self,request):
        userId = int(request['userId'])
        
        result = self.model.CloseAccount(userId)
        res = self.view.UserCloseView(result)
        return res 
    
    #修改用户信息
    def UserChangeInfoController(self,request):

        userId = request.get('userId',default=0)
        userName = request.get('userName',default=None)
        passWord = request.get('passWord',default=None)
        userIcon = request.get('userIcon',default=None)

        result = self.model.ChangeUserInfo(userId,userName=userName,passWord=passWord,userIcon=userIcon)
        res = self.view.UserChangeInfoView(result)      
        return res 

    #查询用户信息
    def UserQueryInfoController(self,request):
        userId = request.get('userId',default=0)
        userName = request.get('userName',default=None)        
        
        result = self.model.QueryUserInfo(userId=userId,userName=userName)
        res = self.view.UserQueryView(userDict=result)

        return res