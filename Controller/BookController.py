# -*- coding:utf-8 -*-  

import sys
sys.path.append('..')
from Model.BookModel import BookModel
from Model.ISBNBookModel import IsbnBookModel
from View.BookView import BookView

class BookController(object):

    def __init__(self):
        self.Model = BookModel()
        self.View = BookView()

    #上传图书ISBN信息
    '''
        levelNum        VARCHAR(10)    NOT NULL,
        subTitle        VARCHAR(100),   
        author          VARCHAR(100)   NOT NULL,
        date            VARCHAR(20)    NOT NULL,
        imagesMedium    VARCHAR(100)   NOT NULL,
        imagesLarge     VARCHAR(100)   NOT NULL,    
        publisher       VARCHAR(50)    NOT NULL,
        isbn            VARCHAR(13)    NOT NULL PRIMARY KEY,
        title           VARCHAR(100)   NOT NULL,
        summary         VARCHAR(400)   NOT NULL
    '''
    def BookUpLoadISBNcontroller(self,request):
        if request.get('title',default=None):
            isbn = request['isbn']            
            levelNum = request['levelNum']      
            subTitle = request.get('subTitle',default=None)       
            author = request['author']         
            date = request['date']          
            imagesMedium = request['imagesMedium']   
            imagesLarge = request['imagesLarge']        
            publisher = request['publisher']      
            isbn = request['isbn']           
            title = request['title']         
            summary = request['summary']

            result = IsbnBookModel.BookUpLoadIsbn(isbn=isbn,levelNum=levelNum,subTitle=subTitle,author=author,date=date,imagesLarge=imagesLarge,imagesMedium=imagesMedium,publisher=publisher,title=title,summary=summary)
        else:
            isbn = request['isbn']  
            result = IsbnBookModel.BookUpLoadIsbn(isbn=isbn)

        res = self.View.BookUpLoadISBNView(result)
        return res

    #传入的参数是一个字典，表示UserBook 属性
    '''
        bookId          INTEGER         NOT NULL PRIMARY KEY AUTO_INCREMENT,
        userId          INTEGER         NOT NULL,
        isbn            VARCHAR(13)         NOT NULL,
        tag1            VARCHAR(100)    NOT NULL,
        tag2            VARCHAR(100)    NOT NULL,
        place           VARCHAR(100)    NOT NULL,
        isGroupVisible  INTEGER         NOT NULL,  
        lend          INTEGER         NOT NULL,
    '''

    def BookUpLoadController(self,request):
        #取出字典里的字典
        userId = request['userId']
        isbn = request['isbn']            
        tag1 = request['tag1']          
        tag2 = request['tag2']          
        place = request['place']         
        isGroupVisible = request['isGroupVisible'] 
        lend = request['lend']                

        bookId = self.Model.BookUpLoadUser(userId=userId,isbn=isbn,tag1=tag1,tag2=tag2,place=place,isGroupVisible=isGroupVisible,lend=lend)
        res = self.View.BookUpLoadView(bookId)

        return res   

    #删除图书视图
    def BookDeleteController(self,request):
        #取出字典里的字典
        bookId = request['bookId']

        result = self.Model.BookDelete(bookId)
        res = self.View.BookDeleteView(result)
        return res   

    #管理图书视图
    '''
        bookId          INTEGER         NOT NULL PRIMARY KEY AUTO_INCREMENT,
        userId          INTEGER         NOT NULL,
        isbn            VARCHAR(13)         NOT NULL,
        tag1            VARCHAR(100)    NOT NULL,
        tag2            VARCHAR(100)    NOT NULL,
        place           VARCHAR(100)    NOT NULL,
        isGroupVisible  INTEGER         NOT NULL,  
        lend          INTEGER         NOT NULL,
    '''
    def BookChangeBookInfoController(self,request):
        #取出不同的参数请求调动不同的model函数
        bookId = request.get('bookId',default=0)
        tag1 = request.get('tag1',default=None)
        tag2 = request.get('tag2',default=None)
        place = request.get('place',default=None)
        isGroupVisible = request.get('isGroupVisible',default=None)
        lend = request.get('lend',default=None)
        
        #修改结果 0表示正确 1表示失败 2表示没有修改需求
        results = [2,2,2,2,2]
        if tag1:
            result = self.Model.EditTag1(bookId,tag1)
            if not result:
                results[0] = 1
            else:
                results[0] = 0
        if tag2:
            result = self.Model.EditTag2(bookId,tag2)
            if not result:
                results[1] = 1
            else:
                results[1] = 0
        if place:
            result = self.Model.EditPlace(bookId,place)
            if not result:
                results[2] = 1
            else:
                results[2] = 0
        if isGroupVisible:
            result = self.Model.ShareBook(bookId,isGroupVisible)
            if not result:
                results[3] = 1
            else:
                results[3] = 0
        if lend:
            result = self.Model.LendBook(bookId,lend)
            if not result:
                results[4] = 1
            else:
                results[4] = 0

        res = self.View.BookChangeBookInfoView(results)
        return res

    #查询图书视图
    """
        Args:
            可能的查询参数
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
    def BookQueryController(self,request):
        print(request['bookId'])
        #提取出所有可能的查询参数
        bookId = request.get('bookId',default=0)
        userId = request.get('userId',default=0)
        isbn = request.get('isbn',default=None)
        tag1 = request.get('tag1',default=None)
        tag2 = request.get('tag2',default=None)
        place = request.get('place',default=None)
        isGroupVisible = request.get('isGroupVisible',default=2)
        lend = request.get('lend',default=0)
        #返回的是一个字典列表
        result = self.Model.QueryBook(bookId=bookId,userId=userId,isbn=isbn,tag1=tag1,tag2=tag2,place=place,isGroupVisible=isGroupVisible,lend=lend)
        res = self.View.BookQueryView(result)
        
        return res