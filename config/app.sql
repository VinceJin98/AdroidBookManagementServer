
-- 创建app数据库
DROP DATABASE IF EXISTS db_app;
CREATE DATABASE db_app;
-- 切换到该app数据库 
USE db_app;
-- 创建表
-- 用户信息表
DROP TABLE IF EXISTS t_userinfo;
CREATE TABLE t_userinfo(
    userId   INTEGER        NOT NULL PRIMARY KEY AUTO_INCREMENT,
    userName VARCHAR(16)    NOT NULL UNIQUE,
    passWord VARCHAR(16)    NOT NULL,
    nickName VARCHAR(16),
    userIcon VARCHAR(100)  -- 用户头像的URL 
)AUTO_INCREMENT = 1;

-- 根据ISBN查询到的图书信息
DROP TABLE IF EXISTS t_bookinfo_isbn;
CREATE TABLE t_bookinfo_isbn(
    levelNum        VARCHAR(10)    NOT NULL,
    subTitle        VARCHAR(100),   
    author          VARCHAR(100)   NOT NULL,
    date            VARCHAR(20)    NOT NULL,
    imagesMedium    VARCHAR(100)   NOT NULL,
    imagesLarge     VARCHAR(100)   NOT NULL,    
    publisher       VARCHAR(50)    NOT NULL,
    isbn            VARCHAR(13)    PRIMARY KEY,
    title           VARCHAR(100)   NOT NULL,
    summary         VARCHAR(400)   
);
-- 根据用户设置的图书信息,包括标签，借出状态
DROP TABLE IF EXISTS t_bookinfo_user;
CREATE TABLE t_bookinfo_user(
    bookId          INTEGER         NOT NULL PRIMARY KEY AUTO_INCREMENT,
    userId          INTEGER         NOT NULL,
    isbn            VARCHAR(13)     NOT NULL,
    tag1            VARCHAR(100)    NOT NULL,
    tag2            VARCHAR(100)    NOT NULL,
    place           VARCHAR(100)    NOT NULL,
    isGroupVisible  INTEGER         NOT NULL,  
    lend            INTEGER         NOT NULL
)AUTO_INCREMENT = 1;
--修改中文编码格式
alter table t_bookinfo_user convert to character set utf8mb4 collate utf8mb4_bin; 
alter table t_bookinfo_isbn convert to character set utf8mb4 collate utf8mb4_bin; 
alter table t_userinfo convert to character set utf8mb4 collate utf8mb4_bin; 
--添加外键
alter table t_bookinfo_user add foreign key(isbn) references t_bookinfo_isbn(isbn);
alter table t_bookinfo_user add foreign key(userId) references t_userinfo(userId);

-- 以上三个表都有主键不需要索引
