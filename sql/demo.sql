# 显示所有数据库
SHOW DATABASES;

# 新建数据库
CREATE DATABASE school;

# 选择数据库
USE school;

# 查看数据的所有表
SHOW TABLES;

# 创建新表
CREATE TABLE students(
    stu_id      INT         NOT NULL AUTO_INCREMENT,    # 学生ID
    stu_name    CHAR(10)    NOT NULL,                   # 学生姓名
    stu_math    INT         NULL DEFAULT 60,            # 数学成绩
    stu_eng     INT         NULL DEFAULT 60,            # 英语成绩
    stu_art     INT         NULL DEFAULT 60,            # 美术成绩
    PRIMARY KEY (stu_id)
)ENGINE=INNODB;

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
VALUES(1, "Jack", 55, 88, 66);

# 插入单行数据（安全）
INSERT INTO students(stu_id, stu_name, stu_math, stu_eng, stu_art)
VALUES(1, "Jack", 55, 88, 66);

# 插入单行数据（省略部分字段）
INSERT INTO students(stu_name, stu_math)
VALUES("Jack", 55);

# 插入多行数据
INSERT INTO students(stu_name, stu_math, stu_eng, stu_art)
VALUES
("Jack", 55, 88, 66),
("John", 88, 86, 90), 
("Marry", 88, 95, 96), 
("Andy", 88, 95, 80),
("Coco", 86, 89, 75);

# 选择插入数据数据
INSERT INTO students2(stu_id, stu_name, stu_math, stu_eng, stu_art)
SELECT stu_id, stu_name, stu_math, stu_eng, stu_art FROM students;

# 修改表数据
UPDATE IGNORE students
SET stu_math = 88
WHERE stu_id = 2;

# 查看最后一个自增值
SELECT LAST_INSERT_ID();

/***********************************************************/

# 复制表结构
CREATE TABLE students2 LIKE students;

# 导入表数据
INSERT INTO students2 SELECT * FROM students;

# 创建并复制表数据
CREATE TABLE students2 SELECT * FROM students;

# 删除一行数据
DELETE FROM students
WHERE stu_id = 1;

# 删除全部数据
DELETE FROM students2;

# 更快的数据删除
TRUNCATE TABLE students2;

/***********************************************************/

# 检索单个列
SELECT stu_name FROM students;

# 检索多列
SELECT stu_id, stu_name, stu_math FROM students;

# 检索结果值唯一
SELECT DISTINCT stu_id, stu_math, stu_eng FROM students;

# 检索表所有数据
SELECT * FROM students;

# 限制检索返回个数
SELECT stu_id, stu_name FROM students
LIMIT 3;

# 限制开始检索的行数
SELECT stu_id, stu_name FROM students
LIMIT 2,3;

# 限制开始检索的行数(更清晰)
SELECT stu_id, stu_name FROM students
LIMIT 3 OFFSET 2;

# 完全限定名
SELECT students.stu_name FROM school.students;
