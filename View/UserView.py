class UserView(object):
    #登录视图
    def UserLoginView(self,userId):
        if userId > 0:
            res = {'code':200,'msg':'login succeeded','user':str(userId)}
        else:
            res = {'code':400,'msg':'login failed'}
        return res    
    #注册视图
    def UserRegisterView(self,userId):
        if userId > 0:
            res = {'code':200,'msg':'register secceeded','user':str(userId)}
        else:
            res = {'code':400,'msg':'register failed,userName already used'}
        return res
    
    #注销用户视图
    def UserLogOutView(self,Result):
        if Result: 
            res = {'code':200,'msg':'logout succeeded'}
        else:
            res = {'code':400,'msg':'logout failed'}
        return res 

    #删除用户视图
    def UserCloseView(self,Result):
        if Result: 
            res = {'code':200,'msg':'CloseAccount succeeded'}
        else:
            res = {'code':400,'msg':'CloseAccount failed'}
        return res 

    #修改用户信息视图
    def UserChangeInfoView(self,Result):
        if not Result: #不存在错误信息
            res = {'code':200,'msg':'change userInfo succeed'}
        else:
            res = {'code':400,'msg': Result}
        return res 

    #查询视图
    """
        Args:
            UserDict 被查询到的用户信息字典,示例为：
            {userId :  , userName : , userIcon :  }

        Returns:
            一个字典（也可能是字典列表），用户信息，之后封装为JSON发出
    """
    def UserQueryView(self,userDict):
        if userDict:
            res = {'code':200,'msg':'query succecced','user':userDict}
        else:
            res = {'code':400,'msg':'query failed'}
        return res