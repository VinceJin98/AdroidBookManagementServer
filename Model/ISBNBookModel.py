# -*- coding:utf-8 -*-  

import sys
sys.path.append('..')
from function.ISBNQuery import ISBNQuery
from function.DataBaseIneraction import insert_t_bookinfo_isbn,query_t_bookinfo_isbn,delete_t_bookinfo_isbn

class IsbnBookModel(object):

    #通过ISBN码进行赋值
    #返回True成功 False失败
    @staticmethod
    def DBIsbnInsertByISBNCode(ISBNCode):
        #先查库中是否有该isbn号码
        if not ISBNCode:
            return False
        result = query_t_bookinfo_isbn(ISBNCode)
        if not result:#该码不在库中
            #返回的是一个字典
            result = ISBNQuery(ISBNCode)
            if not result:#没有查到
                return False
            #给类进行赋值
            levelNum = result['levelNum']      
            subTitle = result['subtitle']        
            author   = result['author']       
            date     = result['pubdate']       
            imagesMedium = result['images_medium']   
            imagesLarge  = result['images_large']      
            publisher = result['publisher']     
            isbn      = result['isbn13']      
            title     = result['title']      
            summary   = result['summary'] 
            #对ISBN表进行插入记录
            result = insert_t_bookinfo_isbn(levelNum,subTitle,author,date,imagesMedium,imagesLarge,publisher,isbn,title,summary)
            if result == 1:
                return True
            else:
                return False
        else: #库中已有记录,
            return True

    #根据用户输入添加ISBN库
    #返回值0： 正常 1：不接受手动输入结果 2： 其他错误
    @staticmethod
    def DBIsbnInsertByInput(levelNum,subTitle,author,date,imagesMedium,imagesLarge,publisher,isbn,title,summary):
        #先查库中是否有该isbn号码
        if isbn:
            result = query_t_bookinfo_isbn(isbn)
            if not result:#该码不在库中
                if ISBNQuery(ISBNCode=isbn):#该码可以查询到不接受用户手动输入的结果
                   return 1
                #给类进行赋值
                result = insert_t_bookinfo_isbn(levelNum,subTitle,author,date,imagesMedium,imagesLarge,publisher,isbn,title,summary)
                #对ISBN表进行插入记录
                if result == 1:
                    return True
                else:
                    return False
            else: #库中已有记录,
                levelNum = result[0][0]      
                subTitle = result[0][1]     
                author   = result[0][2]       
                date     = result[0][3]       
                imagesMedium = result[0][4]   
                imagesLarge  = result[0][5]      
                publisher = result[0][6]     
                isbn      = result[0][7]      
                title     = result[0][8]      
                summary   = result[0][9] 
                return 1

    #这里用不到删除，因为一旦入库，就没法删掉该信息
    @staticmethod
    def delete_by_isbn(isbn):
        delete_t_bookinfo_isbn(isbn)

    @staticmethod
    def query_by_isbn(isbn):
        return query_t_bookinfo_isbn(isbn)

    @staticmethod
    def BookUpLoadIsbn(levelNum=None,subTitle=None,author=None,date=None,imagesMedium=None,imagesLarge=None,publisher=None,isbn=None,title=None,summary=None):
        if title: #手动模式
            IsbnBookModel.DBIsbnInsertByInput(levelNum,subTitle,author,date,imagesMedium,imagesLarge,publisher,isbn,title,summary)
        else: #自动模式
            IsbnBookModel.DBIsbnInsertByISBNCode(isbn)

        if not query_t_bookinfo_isbn(isbn):
            return False
        else:
            return True

   
