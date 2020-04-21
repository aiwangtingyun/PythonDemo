# 显示所有数据库
SHOW DATABASES;

# 新建数据库
CREATE DATABASE school;

# 选择数据库
USE school;

# 查看数据的所有表
SHOW TABLES;

# 创建新表
CREATE TABLE students (
    stu_id      INT         NOT NULL AUTO_INCREMENT,    # 学生ID
    stu_name    CHAR(10)    NOT NULL,                   # 姓名
    stu_sex     CHAR(5)     NOT NULL DEFAULT "女",      # 性别
    stu_class   CHAR(10)    NOT NULL,                   # 班级
    stu_phone   CHAR(20)    NULL,                       # 电话号码
    PRIMARY KEY (stu_id)
) ENGINE=INNODB;

# 查看表的内部结构
DESCRIBE students;

/***********************************************************/

# 删除表
DROP TABLE IF EXISTS students;

# 给表添加新字段
ALTER TABLE students
ADD stu_math FLOAT NULL; 

# 删除字段
ALTER TABLE students
DROP COLUMN stu_math;

# 插入单行数据（不安全）
INSERT INTO students
VALUES(1, "小明", "男", "3年级", "123456");

# 插入单行数据（安全）
INSERT INTO students(stu_id, stu_name, stu_sex, stu_class, stu_phone)
VALUES(2, "小英", "女", "2年级", "456789");

# 插入单行数据（省略部分字段）
INSERT INTO students(stu_name, stu_class)
VALUES("小花", "2年级");

# 插入多行数据
INSERT INTO students(stu_name, stu_sex, stu_class)
VALUES("小张", "男", "2年级"),("小云", "女", "2年级");

# 查看最后一个自增值
SELECT LAST_INSERT_ID();

/***********************************************************/

# 复制表结构
CREATE TABLE students2 LIKE students;

# 导入表数据
INSERT INTO students2 SELECT * FROM students;

# 选择插入数据数据
INSERT INTO students2(stu_id, stu_name, stu_sex, stu_class, stu_phone)
SELECT stu_id, stu_name, stu_sex, stu_class, stu_phone FROM students;

# 创建并复制表数据
CREATE TABLE students3 SELECT * FROM students2;

# 删除一行数据
DELETE FROM students2
WHERE stu_id = 1;

# 删除全部数据
DELETE FROM students2;

# 更快的数据删除
TRUNCATE TABLE students2;

/***********************************************************/

# 修改表数据
UPDATE IGNORE students
SET stu_sex = "女", stu_phone = "123456"
WHERE stu_id = 5;

# 检索单个列


# 查看表所有行数据
SELECT * FROM students;

