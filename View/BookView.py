class BookView(object):
    #上传ISBN信息视图
    def BookUpLoadISBNView(self,Result):
        if Result:
            res = {'code':200,'msg':'上传ISBN成功'}
        else:
            res = {'code':400,'msg':'上传ISBN失败'}
        return res   

    #上传图书视图
    def BookUpLoadView(self,bookId):
        if bookId > 0:
            res = {'code':200,'msg':'上传图书成功','bookId':str(bookId)}
        else:
            res = {'code':400,'msg':'上传图书失败'}
        return res   

    #删除图书视图
    def BookDeleteView(self,bookId):
        if bookId > 0: 
            res = {'code':200,'msg':'删除图书成功','bookId':str(bookId)}
        else:
            res = {'code':400,'msg':'删除图书失败'}
        return res 

    #管理图书视图
    def BookChangeBookInfoView(self,Result):
       
        msg = ''
        if Result[0] == 1:
            msg += '修改图书tag1失败'
        if Result[1] == 1:
            msg += '修改图书tag2失败'
        if Result[2] == 1:
            msg += '修改图书place失败'
        if Result[3] == 1:
            msg += '共享图书失败'
        if Result[4] == 1:
            msg += '借出图书失败'

        if not msg: 
            res = {'code':200,'msg':'修改图书成功'}
        else:
            res = {'code':400,'msg':msg}
        
        return res 

    #查询图书视图
    """
        Args:
            bookDictList(List): 一个字典列表，里面包括了查询到的书籍的信息
                bookId          INTEGER         NOT NULL PRIMARY KEY AUTO_INCREMENT,
                userId          INTEGER         NOT NULL,
                isbn            VARCHAR(13)     NOT NULL,
                tag1            VARCHAR(100)    NOT NULL,
                tag2            VARCHAR(100)    NOT NULL,
                place           VARCHAR(100)    NOT NULL,
                isGroupVisible  INTEGER         NOT NULL,  
                lend            INTEGER         NOT NULL,
        Returns:
            一个字典（也可能是字典列表），用户信息，之后封装为JSON发出
    """
    def BookQueryView(self,BookDictList):
        if BookDictList:
            res = {'code':200,'msg':'查询成功','BookDictList':BookDictList}
        else:
            res = {'code':400,'msg':'查询失败'}
        return res