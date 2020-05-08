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
SHOW COLUMNS FROM students;
SHOW STATUS;

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

# 排序
SELECT stu_id, stu_math, stu_name FROM students 
ORDER BY stu_math, stu_name;

# 指定排序方向
SELECT stu_id, stu_math, stu_name FROM students 
ORDER BY stu_math DESC, stu_name ASC;

# ORDER BY 与 LIMIT 结合
SELECT stu_math FROM students 
ORDER BY stu_math DESC
LIMIT 1;

# where语句
SELECT * FROM students
WHERE stu_id = 2;

SELECT * FROM students
WHERE stu_id <> 2;

SELECT * FROM students
WHERE stu_id BETWEEN 2 AND 4;

# IS NULL语句
UPDATE students SET stu_eng = NULL 
WHERE stu_id BETWEEN 2 AND 3;

SELECT * FROM students
WHERE stu_eng IS NULL;

/***********************************************************/
# upper() 函数
select stu_name, upper(stu_name) as upper_name
from students;

# lower() 函数
select stu_name, lower(stu_name) as lower_name
from students;

# left() 函数
select stu_name, left(stu_name, 3) as left_name
from students;

# right() 函数
select stu_name, right(stu_name, 3) as right_name
from students;

# locate() 函数
select stu_name, locate("o", stu_name) as locate_name
from students;

# substring() 函数
SELECT stu_name, substring(stu_name, 2) AS substring_name
FROM students;

# ltrim() 函数
SELECT stu_name, ltrim(stu_name) AS ltrim_name
FROM students;

# rtrim() 函数
SELECT stu_name, rtrim(stu_name) AS rtrim_name
FROM students;

# length() 函数
SELECT stu_name, length(stu_name) AS name_len
FROM students;

# soundex() 函数
select stu_name from students
where soundex(stu_name) = soundex("jac");

/***********************************************************/

# avg() 函数
select avg(distinct stu_math) as avg_math
from students;

# max() 函数
SELECT max(stu_name) as max_math
FROM students;

# min() 函数
SELECT min(stu_math) AS min_math
FROM students;

# count() 函数
SELECT count(stu_id) AS stu_count
FROM students;

# sum() 函数
SELECT sum(stu_math * stu_eng) AS sum_math_eng
FROM students;

# 组合
SELECT avg(stu_math) AS avg_math,
       max(stu_math) as max_math,
       min(stu_eng) as min_eng,
       count(*) as all_count
FROM students;

/***********************************************************/

# 分组
select stu_math, count(*) as num_count
from students
group by stu_math;

# 分组级别
SELECT stu_math, COUNT(*) AS num_count
FROM students
GROUP BY stu_math WITH ROLLUP;

# 过滤分组
SELECT stu_math, COUNT(*) AS num_count
FROM students
GROUP BY stu_math
having COUNT(*) >= 2;

# HAVING 和 WHERE 组合使用
SELECT stu_math, COUNT(*) AS num_count
FROM students
where stu_math >= 60
GROUP BY stu_math
HAVING COUNT(*) >= 1;

# 排序分组
SELECT stu_math, COUNT(*) AS num_count
FROM students
GROUP BY stu_math
HAVING COUNT(*) >= 1
ORDER BY stu_math;

/***********************************************************/

# 子查询
select stu_id, stu_name, stu_eng from students
where stu_math in (select stu_math from students where stu_eng >= 90);

# 子查询作为字段
select stu_id, stu_name, (select count(*) from students) as stu_count
from students;

# 组合查询
select stu_id, stu_name from students
where stu_math >= 88
union
SELECT stu_id, stu_name FROM students
WHERE stu_eng <= 90;

# 包含重复行
SELECT stu_id, stu_name FROM students
WHERE stu_math >= 88
UNION ALL
SELECT stu_id, stu_name FROM students
WHERE stu_eng <= 90;

# 排序组合查询
SELECT stu_id, stu_name FROM students
WHERE stu_math >= 88
UNION
SELECT stu_id, stu_name FROM students
WHERE stu_eng <= 90
order by stu_name;

# 创建全文本字段
drop table if exists product;
create table if not exists product (
    pro_id      int     not null auto_increment,
    pro_info    text    null,
    primary key(pro_id),
    fulltext(pro_info)
)engine=myisam;

describe product;

insert into product(pro_id, pro_info)
values(1, "Hello MySql, My name is Andy, I'm learning MySql.");

select * from product
where match(pro_info) against('is');






