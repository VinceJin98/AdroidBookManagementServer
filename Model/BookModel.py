# -*- coding:utf-8 -*-  

import sys
sys.path.append('..')
from function.DataBaseIneraction import insert_t_bookinfo_user,delete_t_bookinfo_user,update_t_bookinfo_user,query_t_bookinfo_user
from Model.ISBNBookModel import IsbnBookModel

class BookModel(object):

    def __init__(self,bookId=0,userId=0,isbn='',tag1='',tag2='',place='',isGroupVisible=0,lend=0):
        self.bookId = bookId
        self.userId = userId
        self.isbn = isbn
        self.tag1 = tag1
        self.tag2 = tag2
        self.place = place
        self.isGroupVisible = isGroupVisible
        self.lend = lend

    @staticmethod
    def BookUpLoadUser(userId,isbn,tag1,tag2,place,isGroupVisible,lend):
        insert_t_bookinfo_user(userId,isbn,tag1,tag2,place,isGroupVisible,lend)
        #查询该书的bookId
        bookId = BookModel.QueryBook(userId,isbn)[0]
        print(bookId)
        return bookId

    @staticmethod
    def BookDelete(bookId):
        return delete_t_bookinfo_user(bookId)

    #分享图书 ,正向分享反向关闭
    @staticmethod
    def ShareBook(bookId,isGroupVisible):
        update_t_bookinfo_user(bookId=bookId,isGroupVisible=isGroupVisible)
    
    #借出图书，lend对应的值为借书人的Id,默认为0没有借出
    @staticmethod
    def LendBook(bookId,userId):
        update_t_bookinfo_user(bookId=bookId,lend=userId)

    #修改标签1
    @staticmethod
    def EditTag1(bookId,tag1):
        update_t_bookinfo_user(bookId=bookId,tag1=tag1)

    #修改标签2
    @staticmethod
    def EditTag2(bookId,tag2):
        update_t_bookinfo_user(bookId=bookId,tag2=tag2)    

    #修改地址
    @staticmethod
    def EditPlace(bookId,place):
        update_t_bookinfo_user(bookId=bookId,place=place)    

    #返回符合条件的UserBook列表 
    #如果是bookId则一次只支持一本
    @staticmethod
    def QueryBook(bookId=None,userId='',isbn='',tag1='',tag2='',place='',isGroupVisible=2,lend=2):
        if bookId: 
            result = query_t_bookinfo_user(bookId=bookId)
            print('QueryBookResult:')
            print(result)
            return BookModel(result[0][0],result[0][1],result[0][2],result[0][3],result[0][4],result[0][5],result[0][6],result[0][7]).__dict__
        else: #求列表 
            BookLists = [] #列表的列表
            if userId :
                BookLists.append(query_t_bookinfo_user(userId=userId))
            if isbn :
                BookLists.append(query_t_bookinfo_user(isbn=isbn))
            if tag1 :
                BookLists.append(query_t_bookinfo_user(tag1=tag1))
            if tag2 :
                BookLists.append(query_t_bookinfo_user(tag2=tag2))
            if place :
                BookLists.append(query_t_bookinfo_user(place=place))
            if isGroupVisible != 2 :
                BookLists.append(query_t_bookinfo_user(isGroupVisible=isGroupVisible))
            if lend != 2 :
                BookLists.append(query_t_bookinfo_user(lend=lend))
            
            #求交集 
            BookList = BookLists[0]
            for i in BookLists:
                BookList = BookList & i            

            #求实例的列表
            UserBooks = []
            for i in BookList:
                UserBooks.append(BookModel.QueryBook(bookId=i))     

            return UserBooks
        