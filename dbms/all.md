

Table 1: client_master table

| columnname | datatype | size |
| --- | --- | --- |
| client_no | varchar | 6 |
| name | varchar | 20 |
| city | varchar | 15 |
| state | varchar | 15 |
| pincode | int | 6 |
| bal_due | decimal | 10,2 |

Table 2: product_master table

| columnname | datatype | size |
| --- | --- | --- |
| product_no | varchar | 6 |
| description | varchar | 20 |
| profit_percent | decimal | 10,2 |
| unit_measure | varchar | 15 |
| qty_on_hand | int | 6 |
| reorder_lvl | int | 6 |
| sell_price | decimal | 10,2 |
| cost_price | decimal | 10,2 |

Table 1: sales_master schema

| Columnname | Datatype | Size | Attributes |
|------------|----------|------|------------|
| salesman_no | varchar | 6 | Primary key/first letter must start with ‘s’ |
| sal_name | varchar | 20 | Not null |
| address | varchar | 20 | Not null |
| city | varchar | 20 | |
| state | varchar | 20 | |
| pincode | int | 6 | |
| sal_amt | decimal | 8,2 | Not null, cannot be 0 |
| tgt_to_get | decimal | 6,2 | Not null, cannot be 0 |
| ytd_sales | decimal | 6,2 | Not null, cannot be 0 |
| remarks | varchar | 30 | |

Table 2: sales_order Schema

| Columnname | Datatype | Size | Attributes |
|------------|----------|------|------------|
| s_order_no | varchar | 6 | Primary/first letter must be 0 |
| s_order_date | date | 6 | Primary key reference clientno of client_master table |
| client_no | varchar | 25 |
| dely_add | varchar | 6 |
| salesman_no | varchar | 6 | Foreign key references salesman_no of salesman_master table |
| dely_type | char | 1 | Delivery part(p)/full(f),default f |
| billed_yn | char | 1 |
| dely_date | date | Can not be lessthan s_order_date |
| order_status | varchar | 10 | Values (‘in process’;’fulfilled’;back order’;’canceled |

Table 3: sales_order_details Schema

| Column | Datatype | Size | Attributes |
|--------|----------|------|------------|
| s_order_no | varchar | 6 | Primary key/foreign key references s_order_no of sales_order |
| product_no | varchar | 6 | Primary key/foreign key references product_no of product_master |
| qty_order | int | 8 |
| qty_disp | int | 8 |
| product_rate | decimal | 10,2 |

Table 4: sales_master table data

| salesman_no | salesman name | address | city | pin code | state | salamt | tgt\_to\_g et | ytd sales | remark |
|-------------|---------------|---------|------|----------|-------|--------|--------------|-----------|--------|
| 500001 | Kiran | A/14 worli | Bomba y | 400002 | Mah | 3000 | 100 | 50 | Good |
| 500002 | Manish | 65,nariman | Bomba y | 400001 | Mah | 3000 | 200 | 100 | Good |
| 500003 | Ravi | P-7 Bandra | Bomba y | 400032 | Mah | 3000 | 200 | 100 | Good |
| 500004 | Ashish | A/5 Juhu | Bomba y | 400044 | Mah | 3500 | 200 | 150 | Good |

Table 5: sales_order table data

| s_order_no | s_order_date | client_no | dely_type | billed_yn | salesman_no | dely_date | order_status |
|------------|--------------|-----------|-----------|-----------|-------------|-----------|--------------|
| 019001 | 12-jan-96 | 0001 | F | N | 50001 | 20-jan-96 | Ip |
| 019002 | 25-jan-96 | 0002 | P | N | 50002 | 27-jan-96 | C |
| 016865 | 18-feb-96 | 0003 | F | Y | 500003 | 20-feb-96 | F |
| 019003 | 03-apr-96 | 0001 | F | Y | 500001 | 07-apr-96 | F |
| 046866 | 20-may-96 | 0004 | P | N | 500002 | 22-may-96 | C |
| 010008 | 24-may-96 | 0005 | F | N | 500004 | 26-may-96 | Ip |

Table 6: sales_order_details table data

| s_order_no | product_no | qty_order | qty_disp | product_rate |
|------------|------------|-----------|----------|--------------|
| 019001 | P00001 | 4 | 4 | 525 |
| 019001 | P07965 | 2 | 1 | 8400 |
| 019001 | P07885 | 2 | 1 | 5250 |
| 019002 | P00001 | 10 | 0 | 525 |
| 046865 | P07868 | 3 | 3 | 3150 |
| 046865 | P07885 | 10 | 10 | 5250 |
| 019003 | P00001 | 4 | 4 | 1050 |
| 019003 | P03453 | 2 | 2 | 1050 |
| 046866 | P06734 | 1 | 1 | 12000 |
| 046866 | P07965 | 1 | 0 | 8400 |
| 010008 | P07975 | 1 | 0 | 1050 |
| 010008 | P00001 | 10 | 5 | 525 |

<div style="page-break-after: always;"></div>

Table 1: Challan_Header table

| Column name | Data type | Size | Attributes |
|-------------|-----------|------|------------|
| challan_no | varchar | 6 | Primary key |
| s_order_no | varchar | 6 | Foreign key references s_order_no of sales_order table |
| challan_date | date | not null | |
| billed_yn | char | 1 | values (‘Y’,’N’). Default ‘N’ |

Table 2: Challan_Details table

| Column name | Data type | Size | Attributes |
|-------------|-----------|------|------------|
| challan_no | varchar | 6 | Primary key/Foreign key references Product_no of product_master |
| qty_disp | number | 4,2 | not null |

Table 3: Challan_Header table data

| challan_no | s_order_no | challan_date | billed_yn |
|------------|------------|--------------|-----------|
| CH9001 | 019001 | 12-DEC-95 | Y |
| CH865 | 046865 | 12-NOV-95 | Y |
| CH3965 | 010008 | 12-OCT-95 | Y |

Table 4: Challan_Details table data

| challan_no | qty_disp |
|------------|----------|
| CH9001 | 4 |
| CH9001 | 1 |
| CH9001 | 1 |
| CH6865 | 3 |
| CH6865 | 4 |
| CH6865 | 10 |
| CH3965 | 5 |
| CH3965 | 2 |

<div style="page-break-after: always;"></div>

Table 5: BOOK tables

| Tables | Columns |
|--------|---------|
| BOOK | (Book_id, Title, Publisher_Name, Pub_Year) |
| BOOK_AUTHORS | (Book_id, Author_Name) |
| PUBLISHER | (Name, Address, Phone) |
| BOOK_COPIES | (Book_id, Branch_id, No-of_Copies) |
| BOOK_LENDING | (Book_id, Branch_id, Card_No, Date_Out, Due_Date) |
| LIBRARY_BRANCH | (Branch_id, Branch_Name, Address) |

Objective – Answer the following Queries


Q1. Make the primary key to client_no in client_master.

Ans:

alter table client_master add primary key(client_no);

Q2. Add a new column phone_no in the client_master table.

Ans:

alter table client_master add phone_no varchar(10);

Q3. Add the not null constraint in the product_master table with the columns description, profit
percent , sell price and cost price.

Ans:






Q4. Change the size of client_no field in the client_master table.

Ans:

alter table client_master modify client_no varchar(4);

Q5. Select product_no, description where profit percent is between 20 and 30 both inclusive.

Ans:

select product_no, description from product_master where profit_percent between 20 and 30;

// answer the above questions in mysql syntax
alter table client_master add primary key(client_no);
alter table client_master add phone_no varchar(10);
alter table product_master modify(description varchar(20) not null, profit_percent number(5,2) not null, sell_price number(10,2) not null, cost_price number(10,2) not null);
alter table client_master modify client_no varchar(4);
select product_no, description from product_master where profit_percent between 20 and 30;



Experiment No.5
Theory & Concept
Objective:- To implement the concept of Joins
Joint Multiple Table (Equi Join): Some times we require to treat more than one table as though
manipulate data from all the tables as though the tables were not separate object but one single entity.
To achieve this we have to join tables.Tables are joined on column that have dame data type and
data with in tables.
 The tables that have to be joined are specified in the FROM clause and the joining
attributes in the WHERE clause.
Algorithm for JOIN in SQL:

1. Cartesian product of tables (specified in the FROM clause)
2. Selection of rows that match (predicate in the WHERE clause)
3. Project column specified in the SELECT clause.

Consider two table student and course
Select B.*,P.*
FROM student B, course P;
2. INNER JOIN:
Cartesian product followed by selection
Select B.*,P.*
FROM student B, Course P
WHERE B.course # P.course # ;
3. LEFT OUTER JOIN:
LEFT OUTER JOIN = Cartesian product + selection but include rows from the left table
which are unmatched pat nulls in the values of attributes belonging to th e second table
Exam:
Select B.*,P*
FROM student B left join course p
ON B.course # P.course #;
4. RIGHT OUTER JOIN:
RIGHT OUTER JOIN = Cartesian product + selection but include rows from right table
which are unmatched
Exam:
Select B.*,P.*
From student B RIGHT JOIN course P
B.course# = P course # ;
5. FULL OUTER JOIN
 Exam
Select B.*,P.*
From student B FULL JOIN course P
 On B.course # = P course # ;

A. Consider the following schema for a Library Database:
BOOK (Book_id, Title, Publisher_Name, Pub_Year)
BOOK_AUTHORS (Book_id, Author_Name)
PUBLISHER (Name, Address, Phone)
BOOK_COPIES (Book_id, Branch_id, No-of_Copies)
BOOK_LENDING (Book_id, Branch_id, Card_No, Date_Out, Due_Date)
LIBRARY_BRANCH (Branch_id, Branch_Name, Address)

// create this table in mysql syntax and in markdown format for table

Table 5: BOOK tables

| Tables | Columns |
|--------|---------|
| BOOK | (Book_id, Title, Publisher_Name, Pub_Year) |
| BOOK_AUTHORS | (Book_id, Author_Name) |
| PUBLISHER | (Name, Address, Phone) |
| BOOK_COPIES | (Book_id, Branch_id, No-of_Copies) |
| BOOK_LENDING | (Book_id, Branch_id, Card_No, Date_Out, Due_Date) |
| LIBRARY_BRANCH | (Branch_id, Branch_Name, Address) |

Write SQL queries to :

1. Retrieve details of all books in the library – id, title, name of publisher, authors, number of copies
in each branch, etc.
Ans:
select b.book_id, b.title, b.publisher_name, ba.author_name, bc.no_of_copies, lb.branch_name, lb.address from book b, book_authors ba, book_copies bc, library_branch lb where b.book_id = ba.book_id and b.book_id = bc.book_id and bc.branch_id = lb.branch_id;

2. Get the particulars of borrowers who have borrowed more than 3 books, but from Jan 2017 to Jun 2017.

Ans:
select bl.card_no, bl.date_out, bl.due_date from book_lending bl where bl.date_out between '01-JAN-17' and '30-JUN-17' group by bl.card_no having count(bl.card_no) > 3;
3. Delete a book in BOOK table. Update the contents of other tables to reflect this data manipulation
operation.
Ans:
delete from book where book_id = 'B0001';

4. 4. Partition the BOOK table based on year of publication. Demonstrate its working with a simple
query.
ans:
select * from book where pub_year between 2000 and 2005;

5. Create a view of all books and its number of copies that are currently available in the Library.

ans:
create view book_view as select b.book_id, b.title, b.publisher_name, ba.author_name, bc.no_of_copies, lb.branch_name, lb.address from book b, book_authors ba, book_copies bc, library_branch lb where b.book_id = ba.book_id and b.book_id = bc.book_id and bc.branch_id = lb.branch_id;

all answers are
select b.book_id, b.title, b.publisher_name, ba.author_name, bc.no_of_copies, lb.branch_name, lb.address from book b, book_authors ba, book_copies bc, library_branch lb where b.book_id = ba.book_id and b.book_id = bc.book_id and bc.branch_id = lb.branch_id;
select bl.card_no, bl.date_out, bl.due_date from book_lending bl where bl.date_out between '01-JAN-17' and '30-JUN-17' group by bl.card_no having count(bl.card_no) > 3;
delete from book where book_id = 'B0001';
select * from book where pub_year between 2000 and 2005;
create view book_view as select b.book_id, b.title, b.publisher_name, ba.author_name, bc.no_of_copies, lb.branch_name, lb.address from book b, book_authors ba, book_copies bc, library_branch lb where b.book_id = ba.book_id and b.book_id = bc.book_id and bc.branch_id = lb.branch_id;

EXPERIMENT NO. 6

Table Creation
CREATE TABLE PUBLISHER
(NAME VARCHAR2 (20) PRIMARY KEY,
PHONE INTEGER,
ADDRESS VARCHAR2 (20));
CREATE TABLE BOOK
(BOOK_ID INTEGER PRIMARY KEY,
TITLE VARCHAR2 (20),
PUB_YEAR VARCHAR2 (20),
PUBLISHER_NAME REFERENCES PUBLISHER (NAME) ON DELETE CASCADE);
CREATE TABLE BOOK_AUTHORS
(AUTHOR_NAME VARCHAR2 (20),
BOOK_ID REFERENCES BOOK (BOOK_ID) ON DELETE CASCADE,
PRIMARY KEY (BOOK_ID, AUTHOR_NAME));
CREATE TABLE LIBRARY_BRANCH
(BRANCH_ID INTEGER PRIMARY KEY,
BRANCH_NAME VARCHAR2 (50),
ADDRESS VARCHAR2 (50));
CREATE TABLE BOOK_COPIES
(NO_OF_COPIES INTEGER,
BOOK_ID REFERENCES BOOK (BOOK_ID) ON DELETE CASCADE,
BRANCH_ID REFERENCES LIBRARY_BRANCH (BRANCH_ID) ON DELETE CASCADE,
PRIMARY KEY (BOOK_ID, BRANCH_ID));
CREATE TABLE CARD
(CARD_NO INTEGER PRIMARY KEY);
CREATE TABLE BOOK_LENDING
(DATE_OUT DATE,
DUE_DATE DATE,
BOOK_ID REFERENCES BOOK (BOOK_ID) ON DELETE CASCADE,
BRANCH_ID REFERENCES LIBRARY_BRANCH (BRANCH_ID) ON DELETE CASCADE,
CARD_NO REFERENCES CARD (CARD_NO) ON DELETE CASCADE,
PRIMARY KEY (BOOK_ID, BRANCH_ID, CARD_NO));
Insertion of Values to Tables
INSERT INTO PUBLISHER VALUES (‗MCGRAW-HILL‘, 9989076587, ‗BANGALORE‘);
INSERT INTO PUBLISHER VALUES (‗PEARSON‘, 9889076565, ‗NEWDELHI‘);
INSERT INTO PUBLISHER VALUES (‗RANDOM HOUSE‘, 7455679345, ‗HYDRABAD‘);
INSERT INTO PUBLISHER VALUES (‗HACHETTE LIVRE‘, 8970862340, ‗CHENAI‘);
INSERT INTO PUBLISHER VALUES (‗GRUPO PLANETA‘, 7756120238, ‗BANGALORE‘);
INSERT INTO BOOK VALUES (1,‘DBMS‘,‘JAN-2017‘, ‗MCGRAW-HILL‘);
INSERT INTO BOOK VALUES (2,‘ADBMS‘,‘JUN-2016‘, ‗MCGRAW-HILL‘);
INSERT INTO BOOK VALUES (3,‘CN‘,‘SEP-2016‘, ‗PEARSON‘);
INSERT INTO BOOK VALUES (4,‘CG‘,‘SEP-2015‘, ‗GRUPO PLANETA‘);
INSERT INTO BOOK VALUES (5,‘OS‘,‘MAY-2016‘, ‗PEARSON‘);
INSERT INTO BOOK_AUTHORS VALUES (‘NAVATHE‘, 1);
INSERT INTO BOOK_AUTHORS VALUES (‘NAVATHE‘, 2);
INSERT INTO BOOK_AUTHORS VALUES (‘TANENBAUM‘, 3);

INSERT INTO BOOK_AUTHORS VALUES (‘EDWARD ANGEL‘, 4);
INSERT INTO BOOK_AUTHORS VALUES (‘GALVIN‘, 5);
INSERT INTO LIBRARY_BRANCH VALUES (10,‘RR NAGAR‘,‘BANGALORE‘);
INSERT INTO LIBRARY_BRANCH VALUES (11,‘RNSIT‘,‘BANGALORE‘);
INSERT INTO LIBRARY_BRANCH VALUES (12,‘RAJAJI NAGAR‘, ‘BANGALORE‘);
INSERT INTO LIBRARY_BRANCH VALUES (13,‘NITTE‘,‘MANGALORE‘);
INSERT INTO LIBRARY_BRANCH VALUES (14,‘MANIPAL‘,‘UDUPI‘);
INSERT INTO BOOK_COPIES VALUES (10, 1, 10);
INSERT INTO BOOK_COPIES VALUES (5, 1, 11);
INSERT INTO BOOK_COPIES VALUES (2, 2, 12);
INSERT INTO BOOK_COPIES VALUES (5, 2, 13);
INSERT INTO BOOK_COPIES VALUES (7, 3, 14);
INSERT INTO BOOK_COPIES VALUES (1, 5, 10);
INSERT INTO BOOK_COPIES VALUES (3, 4, 11);
INSERT INTO CARD VALUES (100);
INSERT INTO CARD VALUES (101);
INSERT INTO CARD VALUES (102);
INSERT INTO CARD VALUES (103);
INSERT INTO CARD VALUES (104);
INSERT INTO BOOK_LENDING VALUES (‘01-JAN-17‘,‘01-JUN-17‘, 1, 10, 101);
INSERT INTO BOOK_LENDING VALUES (‘11-JAN-17‘,‘11-MAR-17‘, 3, 14, 101);
INSERT INTO BOOK_LENDING VALUES (‘21-FEB-17‘,‘21-APR-17‘, 2, 13, 101);
INSERT INTO BOOK_LENDING VALUES (‘15-MAR-17‘,‘15-JUL-17‘, 4, 11, 101);
INSERT INTO BOOK_LENDING VALUES (‗12-APR-17‘,‘12-MAY-17‘, 1, 11, 104);

Queries:

1. Retrieve details of all books in the library – id, title, name of publisher, authors, number of copies
in each branch, etc.
SELECT B.BOOK_ID, B.TITLE, B.PUBLISHER_NAME, A.AUTHOR_NAME, C.NO_OF_COPIES,
L.BRANCH_ID
FROM BOOK B, BOOK_AUTHORS A, BOOK_COPIES C, LIBRARY_BRANCH L
WHERE B.BOOK_ID=A.BOOK_ID
AND B.BOOK_ID=C.BOOK_ID AND L.BRANCH_ID=C.BRANCH_ID;

2. Get the particulars of borrowers who have borrowed more than 3 books, but from Jan 2017 to
Jun 2017.
SELECT CARD_NO FROM BOOK_LENDING
WHERE DATE_OUT BETWEEN ‘01-JAN-2017‘ AND ‘01-JUL-2017‘
GROUP BY CARD_NO HAVING COUNT (*)>3;
3. Delete a book in BOOK table. Update the contents of other tables to reflect this data
manipulation operation.
DELETE FROM BOOK
WHERE BOOK_ID=3;
4. Partition the BOOK table based on year of publication. Demonstrate its working with a simple
query.
CREATE VIEW V_PUBLICATION AS SELECT PUB_YEAR FROM BOOK;
5. Create a view of all books and its number of copies that are currently available in the Library.
CREATE VIEW V_BOOKS AS SELECT B.BOOK_ID, B.TITLE, C.NO_OF_COPIES
FROM BOOK B, BOOK_COPIES C, LIBRARY_BRANCH L
WHERE B.BOOK_ID=C.BOOK_ID AND C.BRANCH_ID=L.BRANCH_ID;

Table 1: client_master table

| columnname | datatype | size |
| --- | --- | --- |
| client_no | varchar | 6 |
| name | varchar | 20 |
| city | varchar | 15 |
| state | varchar | 15 |
| pincode | int | 6 |
| bal_due | decimal | 10,2 |

Table 2: product_master table

| columnname | datatype | size |
| --- | --- | --- |
| product_no | varchar | 6 |
| description | varchar | 20 |
| profit_percent | decimal | 10,2 |
| unit_measure | varchar | 15 |
| qty_on_hand | int | 6 |
| reorder_lvl | int | 6 |
| sell_price | decimal | 10,2 |
| cost_price | decimal | 10,2 |

Table 1: sales_master schema

| Columnname | Datatype | Size | Attributes |
|------------|----------|------|------------|
| salesman_no | varchar | 6 | Primary key/first letter must start with ‘s’ |
| sal_name | varchar | 20 | Not null |
| address | varchar | 20 | Not null |
| city | varchar | 20 | |
| state | varchar | 20 | |
| pincode | int | 6 | |
| sal_amt | decimal | 8,2 | Not null, cannot be 0 |
| tgt_to_get | decimal | 6,2 | Not null, cannot be 0 |
| ytd_sales | decimal | 6,2 | Not null, cannot be 0 |
| remarks | varchar | 30 | |

Table 2: sales_order Schema

| Columnname | Datatype | Size | Attributes |
|------------|----------|------|------------|
| s_order_no | varchar | 6 | Primary/first letter must be 0 |
| s_order_date | date | 6 | Primary key reference clientno of client_master table |
| client_no | varchar | 25 |
| dely_add | varchar | 6 |
| salesman_no | varchar | 6 | Foreign key references salesman_no of salesman_master table |
| dely_type | char | 1 | Delivery part(p)/full(f),default f |
| billed_yn | char | 1 |
| dely_date | date | Can not be lessthan s_order_date |
| order_status | varchar | 10 | Values (‘in process’;’fulfilled’;back order’;’canceled |

Table 3: sales_order_details Schema

| Column | Datatype | Size | Attributes |
|--------|----------|------|------------|
| s_order_no | varchar | 6 | Primary key/foreign key references s_order_no of sales_order |
| product_no | varchar | 6 | Primary key/foreign key references product_no of product_master |
| qty_order | int | 8 |
| qty_disp | int | 8 |
| product_rate | decimal | 10,2 |

Table 4: sales_master table data

| salesman_no | salesman name | address | city | pin code | state | salamt | tgt\_to\_g et | ytd sales | remark |
|-------------|---------------|---------|------|----------|-------|--------|--------------|-----------|--------|
| 500001 | Kiran | A/14 worli | Bomba y | 400002 | Mah | 3000 | 100 | 50 | Good |
| 500002 | Manish | 65,nariman | Bomba y | 400001 | Mah | 3000 | 200 | 100 | Good |
| 500003 | Ravi | P-7 Bandra | Bomba y | 400032 | Mah | 3000 | 200 | 100 | Good |
| 500004 | Ashish | A/5 Juhu | Bomba y | 400044 | Mah | 3500 | 200 | 150 | Good |

Table 5: sales_order table data

| s_order_no | s_order_date | client_no | dely_type | billed_yn | salesman_no | dely_date | order_status |
|------------|--------------|-----------|-----------|-----------|-------------|-----------|--------------|
| 019001 | 12-jan-96 | 0001 | F | N | 50001 | 20-jan-96 | Ip |
| 019002 | 25-jan-96 | 0002 | P | N | 50002 | 27-jan-96 | C |
| 016865 | 18-feb-96 | 0003 | F | Y | 500003 | 20-feb-96 | F |
| 019003 | 03-apr-96 | 0001 | F | Y | 500001 | 07-apr-96 | F |
| 046866 | 20-may-96 | 0004 | P | N | 500002 | 22-may-96 | C |
| 010008 | 24-may-96 | 0005 | F | N | 500004 | 26-may-96 | Ip |

Table 6: sales_order_details table data

| s_order_no | product_no | qty_order | qty_disp | product_rate |
|------------|------------|-----------|----------|--------------|
| 019001 | P00001 | 4 | 4 | 525 |
| 019001 | P07965 | 2 | 1 | 8400 |
| 019001 | P07885 | 2 | 1 | 5250 |
| 019002 | P00001 | 10 | 0 | 525 |
| 046865 | P07868 | 3 | 3 | 3150 |
| 046865 | P07885 | 10 | 10 | 5250 |
| 019003 | P00001 | 4 | 4 | 1050 |
| 019003 | P03453 | 2 | 2 | 1050 |
| 046866 | P06734 | 1 | 1 | 12000 |
| 046866 | P07965 | 1 | 0 | 8400 |
| 010008 | P07975 | 1 | 0 | 1050 |
| 010008 | P00001 | 10 | 5 | 525 |

<div style="page-break-after: always;"></div>

Table 1: Challan_Header table

| Column name | Data type | Size | Attributes |
|-------------|-----------|------|------------|
| challan_no | varchar | 6 | Primary key |
| s_order_no | varchar | 6 | Foreign key references s_order_no of sales_order table |
| challan_date | date | not null | |
| billed_yn | char | 1 | values (‘Y’,’N’). Default ‘N’ |

Table 2: Challan_Details table

| Column name | Data type | Size | Attributes |
|-------------|-----------|------|------------|
| challan_no | varchar | 6 | Primary key/Foreign key references Product_no of product_master |
| qty_disp | number | 4,2 | not null |

Table 3: Challan_Header table data

| challan_no | s_order_no | challan_date | billed_yn |
|------------|------------|--------------|-----------|
| CH9001 | 019001 | 12-DEC-95 | Y |
| CH865 | 046865 | 12-NOV-95 | Y |
| CH3965 | 010008 | 12-OCT-95 | Y |

Table 4: Challan_Details table data

| challan_no | qty_disp |
|------------|----------|
| CH9001 | 4 |
| CH9001 | 1 |
| CH9001 | 1 |
| CH6865 | 3 |
| CH6865 | 4 |
| CH6865 | 10 |
| CH3965 | 5 |
| CH3965 | 2 |

<div style="page-break-after: always;"></div>

Table 5: BOOK tables

| Tables | Columns |
|--------|---------|
| BOOK | (Book_id, Title, Publisher_Name, Pub_Year) |
| BOOK_AUTHORS | (Book_id, Author_Name) |
| PUBLISHER | (Name, Address, Phone) |
| BOOK_COPIES | (Book_id, Branch_id, No-of_Copies) |
| BOOK_LENDING | (Book_id, Branch_id, Card_No, Date_Out, Due_Date) |
| LIBRARY_BRANCH | (Branch_id, Branch_Name, Address) |

OBJECTIVE: Answer the following Queries:
QUERIES -

1. Find out the product which has been sold to ‘Ivan Sayross.’
2. Find out the product and their quantities that will have do delivered.
3. Find the product_no and description of moving products.
4. Find out the names of clients who have purchased ‘CD DRIVE’
5. List the product_no and s_order_no of customers haaving qty ordered less than 5 from the
order details table for the product “1.44 floppies”.
6. Find the products and their quantities for the orders placed by ‘Vandan Saitwal ’ and “Ivan
Bayross”.
7. Find the products and their quantities for the orders placed by client_no “ C00001” and
“C00002”
8. Find the order No,, Client No and salesman No. where a client has been received by more
than one salesman.
9. Display the s_order_date in the format “dd-mm-yy” e.g. “12- feb-96”
10. Find the date , 15 days after date.

all answers are

1

select * from product_master where product_no in (select product_no from sales_order_details where s_order_no in (select s_order_no from sales_order where client_no in (select client_no from client_master where client_name = ‘Ivan Sayross’)));

2

select * from product_master where product_no in (select product_no from sales_order_details where s_order_no in (select s_order_no from sales_order where order_status = ‘Ip’));

3

select product_no, product_desc from product_master where product_no in (select product_no from sales_order_details where qty_disp > 0);

4

select client_name from client_master where client_no in (select client_no from sales_order where s_order_no in (select s_order_no from sales_order_details where product_no = ‘P00001’));

5

select product_no, s_order_no from sales_order_details where qty_order < 5 and product_no = ‘P00001’;

6

select product_no, qty_disp from sales_order_details where s_order_no in (select s_order_no from sales_order where client_no in (select client_no from client_master where client_name = ‘Vandan Saitwal’ or client_name = ‘Ivan Bayross’));

7

select product_no, qty_disp from sales_order_details where s_order_no in (select s_order_no from sales_order where client_no = ‘C00001’ or client_no = ‘C00002’);

8

select s_order_no, client_no, salesman_no from sales_order where client_no in (select client_no from sales_order group by client_no having count(client_no) > 1);

9

select to_char(s_order_date, ‘dd-mm-yy’) from sales_order;

10

select s_order_date + 15 from sales_order;


// now with questions Answered, you can go ahead and try to solve them yourself. If you get stuck, you can always come back to this post and check the answers.
1. Find out the product which has been sold to 'Ivan Sayross'.

answer:

select * from product_master where product_no in (select product_no from sales_order_details where s_order_no in (select s_order_no from sales_order where client_no in (select client_no from client_master where client_name = 'Ivan Sayross')));

2. Find out the product and their quantities that will have do delivered.

answer:

select * from product_master where product_no in (select product_no from sales_order_details where s_order_no in (select s_order_no from sales_order where order_status = 'Ip'));

3. Find the product_no and description of moving products.

answer:

select product_no, product_desc from product_master where product_no in (select product_no from sales_order_details where qty_disp > 0);

4. Find out the names of clients who have purchased 'CD DRIVE'

answer:

select client_name from client_master where client_no in (select client_no from sales_order where s_order_no in (select s_order_no from sales_order_details where product_no = 'P00001'));

5. List the product_no and s_order_no of customers haaving qty ordered less than 5 from the order details table for the product "1.44 floppies".

answer:

select product_no, s_order_no from sales_order_details where qty_order < 5 and product_no = 'P00001';

6. Find the products and their quantities for the orders placed by 'Vandan Saitwal ' and "Ivan Bayross".

answer:

select product_no, qty_disp from sales_order_details where s_order_no in (select s_order_no from sales_order where client_no in (select client_no from client_master where client_name = 'Vandan Saitwal' or client_name = 'Ivan Bayross'));

7. Find the products and their quantities for the orders placed by client_no " C00001" and "C00002"

answer:

select product_no, qty_disp from sales_order_details where s_order_no in (select s_order_no from sales_order where client_no = 'C00001' or client_no = 'C00002');

8. Find the order No,, Client No and salesman No. where a client has been received by more than one salesman.

answer:

select s_order_no, client_no, salesman_no from sales_order where client_no in (select client_no from sales_order group by client_no having count(client_no) > 1);

9. Display the s_order_date in the format "dd-mm-yy" e.g. "12- feb-96"

answer:

select to_char(s_order_date, 'dd-mm-yy') from sales_order;

10. Find the date , 15 days after date.

answer:

select s_order_date + 15 from sales_order;



<div style="page-break-after: always;"></div>

Experiment No.7
Theory & Concept
Objective:- To implement the concept of grouping of Data.
Grouping Data From Tables:
 There are circumstances where we would like to apply the aggregate function not only to a single set
of tuples, but also to a group of sets of tuples, we specify this wish in SQL using the group by clause.
The attribute or attributes given in the group by clause are used to form group. Tuples with the same
value on all attributes in the group by clause are placed in one group.
Syntax:
SELECT columnname, columnname
FROM tablename
GROUP BY columnname;
At times it is useful to state a condition that applies to groups rather than to tuples. For example we
might be interested in only those branches where the average account balance is more than 1200. This
condition does not apply to a single tuple, rather it applies to each group constructed by the GROUP
BY clause. To express such Questionry, we use the having clause of SQL. SQL applies predicates in
the having may be used.
Syntax:
SELECT columnname, columnname
FROM tablename
GROUP BY columnname;
HAVING searchcondition;

Table 1: client_master table

| columnname | datatype | size |
| --- | --- | --- |
| client_no | varchar | 6 |
| name | varchar | 20 |
| city | varchar | 15 |
| state | varchar | 15 |
| pincode | int | 6 |
| bal_due | decimal | 10,2 |

Table 2: product_master table

| columnname | datatype | size |
| --- | --- | --- |
| product_no | varchar | 6 |
| description | varchar | 20 |
| profit_percent | decimal | 10,2 |
| unit_measure | varchar | 15 |
| qty_on_hand | int | 6 |
| reorder_lvl | int | 6 |
| sell_price | decimal | 10,2 |
| cost_price | decimal | 10,2 |

Table 1: sales_master schema

| Columnname | Datatype | Size | Attributes |
|------------|----------|------|------------|
| salesman_no | varchar | 6 | Primary key/first letter must start with ‘s’ |
| sal_name | varchar | 20 | Not null |
| address | varchar | 20 | Not null |
| city | varchar | 20 | |
| state | varchar | 20 | |
| pincode | int | 6 | |
| sal_amt | decimal | 8,2 | Not null, cannot be 0 |
| tgt_to_get | decimal | 6,2 | Not null, cannot be 0 |
| ytd_sales | decimal | 6,2 | Not null, cannot be 0 |
| remarks | varchar | 30 | |

Table 2: sales_order Schema

| Columnname | Datatype | Size | Attributes |
|------------|----------|------|------------|
| s_order_no | varchar | 6 | Primary/first letter must be 0 |
| s_order_date | date | 6 | Primary key reference clientno of client_master table |
| client_no | varchar | 25 |
| dely_add | varchar | 6 |
| salesman_no | varchar | 6 | Foreign key references salesman_no of salesman_master table |
| dely_type | char | 1 | Delivery part(p)/full(f),default f |
| billed_yn | char | 1 |
| dely_date | date | Can not be lessthan s_order_date |
| order_status | varchar | 10 | Values (‘in process’;’fulfilled’;back order’;’canceled |

Table 3: sales_order_details Schema

| Column | Datatype | Size | Attributes |
|--------|----------|------|------------|
| s_order_no | varchar | 6 | Primary key/foreign key references s_order_no of sales_order |
| product_no | varchar | 6 | Primary key/foreign key references product_no of product_master |
| qty_order | int | 8 |
| qty_disp | int | 8 |
| product_rate | decimal | 10,2 |

Table 4: sales_master table data

| salesman_no | salesman name | address | city | pin code | state | salamt | tgt\_to\_g et | ytd sales | remark |
|-------------|---------------|---------|------|----------|-------|--------|--------------|-----------|--------|
| 500001 | Kiran | A/14 worli | Bomba y | 400002 | Mah | 3000 | 100 | 50 | Good |
| 500002 | Manish | 65,nariman | Bomba y | 400001 | Mah | 3000 | 200 | 100 | Good |
| 500003 | Ravi | P-7 Bandra | Bomba y | 400032 | Mah | 3000 | 200 | 100 | Good |
| 500004 | Ashish | A/5 Juhu | Bomba y | 400044 | Mah | 3500 | 200 | 150 | Good |

Table 5: sales_order table data

| s_order_no | s_order_date | client_no | dely_type | billed_yn | salesman_no | dely_date | order_status |
|------------|--------------|-----------|-----------|-----------|-------------|-----------|--------------|
| 019001 | 12-jan-96 | 0001 | F | N | 50001 | 20-jan-96 | Ip |
| 019002 | 25-jan-96 | 0002 | P | N | 50002 | 27-jan-96 | C |
| 016865 | 18-feb-96 | 0003 | F | Y | 500003 | 20-feb-96 | F |
| 019003 | 03-apr-96 | 0001 | F | Y | 500001 | 07-apr-96 | F |
| 046866 | 20-may-96 | 0004 | P | N | 500002 | 22-may-96 | C |
| 010008 | 24-may-96 | 0005 | F | N | 500004 | 26-may-96 | Ip |

Table 6: sales_order_details table data

| s_order_no | product_no | qty_order | qty_disp | product_rate |
|------------|------------|-----------|----------|--------------|
| 019001 | P00001 | 4 | 4 | 525 |
| 019001 | P07965 | 2 | 1 | 8400 |
| 019001 | P07885 | 2 | 1 | 5250 |
| 019002 | P00001 | 10 | 0 | 525 |
| 046865 | P07868 | 3 | 3 | 3150 |
| 046865 | P07885 | 10 | 10 | 5250 |
| 019003 | P00001 | 4 | 4 | 1050 |
| 019003 | P03453 | 2 | 2 | 1050 |
| 046866 | P06734 | 1 | 1 | 12000 |
| 046866 | P07965 | 1 | 0 | 8400 |
| 010008 | P07975 | 1 | 0 | 1050 |
| 010008 | P00001 | 10 | 5 | 525 |

<div style="page-break-after: always;"></div>

Table 1: Challan_Header table

| Column name | Data type | Size | Attributes |
|-------------|-----------|------|------------|
| challan_no | varchar | 6 | Primary key |
| s_order_no | varchar | 6 | Foreign key references s_order_no of sales_order table |
| challan_date | date | not null | |
| billed_yn | char | 1 | values (‘Y’,’N’). Default ‘N’ |

Table 2: Challan_Details table

| Column name | Data type | Size | Attributes |
|-------------|-----------|------|------------|
| challan_no | varchar | 6 | Primary key/Foreign key references Product_no of product_master |
| qty_disp | number | 4,2 | not null |

Table 3: Challan_Header table data

| challan_no | s_order_no | challan_date | billed_yn |
|------------|------------|--------------|-----------|
| CH9001 | 019001 | 12-DEC-95 | Y |
| CH865 | 046865 | 12-NOV-95 | Y |
| CH3965 | 010008 | 12-OCT-95 | Y |

Table 4: Challan_Details table data

| challan_no | qty_disp |
|------------|----------|
| CH9001 | 4 |
| CH9001 | 1 |
| CH9001 | 1 |
| CH6865 | 3 |
| CH6865 | 4 |
| CH6865 | 10 |
| CH3965 | 5 |
| CH3965 | 2 |

<div style="page-break-after: always;"></div>

Table 5: BOOK tables

| Tables | Columns |
|--------|---------|
| BOOK | (Book_id, Title, Publisher_Name, Pub_Year) |
| BOOK_AUTHORS | (Book_id, Author_Name) |
| PUBLISHER | (Name, Address, Phone) |
| BOOK_COPIES | (Book_id, Branch_id, No-of_Copies) |
| BOOK_LENDING | (Book_id, Branch_id, Card_No, Date_Out, Due_Date) |
| LIBRARY_BRANCH | (Branch_id, Branch_Name, Address) |

Objective- Answer the following Queries:
Q1.- Print the description and total quantity sold for each product.
Q2.- Find the value of each product sold.
Q3.- Calculate the average quantity sold for each client that has a maximum order value of
 15000.
Q4.- Find out the products which has been sold to Ivan.
Q5.- Find the names of clients who have ‘CD Drive’.
Q6.- Find the products and their quantities for the orders placed by ‘Vandana’ and ‘Ivan’.
Q7.- Select product_no, total qty_ordered for each product.
Q8.- Select product_no, product description and qty ordered for each product.
Q9.- Display the order number and day on which clients placed their order.
Q10.- Display the month and Date when the order must be delivered.


Answer:



1

select product_description, sum(qty_order) from sales_order_details sod, product_master pm where sod.product_no = pm.product_no group by product_description;

2

select product_description, sum(qty_order * product_rate) from sales_order_details sod, product_master pm where sod.product_no = pm.product_no group by product_description;

3

select client_name, avg(qty_order) from sales_order_details sod, sales_order so, client_master cm where sod.s_order_no = so.s_order_no and so.client_no = cm.client_no and so.order_value = (select max(order_value) from sales_order) group by client_name;

4

select product_description from sales_order_details sod, sales_order so, client_master cm, product_master pm where sod.s_order_no = so.s_order_no and so.client_no = cm.client_no and sod.product_no = pm.product_no and cm.client_name = 'Ivan';

5

select product_description from sales_order_details sod, product_master pm where sod.product_no = pm.product_no and product_description = 'CD Drive';

6

select product_description, qty_order from sales_order_details sod, sales_order so, client_master cm, product_master pm where sod.s_order_no = so.s_order_no and so.client_no = cm.client_no and sod.product_no = pm.product_no and cm.client_name in ('Vandana', 'Ivan');

7

select product_no, sum(qty_order) from sales_order_details group by product_no;

8

select product_no, product_description, sum(qty_order) from sales_order_details sod, product_master pm where sod.product_no = pm.product_no group by product_no, product_description;

9

select s_order_no, to_char(order_date, 'DAY') from sales_order;

10

select to_char(order_date, 'MONTH'), to_char(order_date, 'DD') from sales_order;

<div style="page-break-after: always;"></div>

Experiment NO.8
Theory & Concept
Objective:- To implement the concept of Sub Queries.
Sub Queries:- A Sub Queries is a form of an SQL statement that appears inside another SQL
statement. It also termed as nested Questionry. The statement containing a Sub Queries called a
parent statement. The rows returned bu the Sub Queries are use by the following statement.
It can be used by the following commands:

1. To insert records in the target table.
2. To create tables and insert records in this table.
3. To update records in the target table.
4. To create view.
5. To provide values for the condition in the WHERE , HAVING IN , SELECT,UPDATE, and
DELETE statements.
Example: Creating client master table from oldclient_master, table
Create table client_master AS SELECT * FROM oldclient_master;
Using the Union, Intersect and Minus Clause:
Union Clause:
The user can put together multiple Queries and combine their output using the union clause . The
union clause merges the output of two or more Queries into a single set of rows and column. The
final output of union clause will be
Output: = Records only in Questionry one + records only in Questionry two + A single set of records
with is common in the both Queries.
Syntax: SELECT columnname, columname FROM tablename 1
UNION
SELECT columnname, columnname From tablename2;
Intersect Clause: The use can put together multiple Queries and their output using the interest
clause. The final output of the interest clause will be :
Output =A single set of records which are common in both Queries
Syntax: SELECT columnname, columnname
FROM tablename 1
INTERSECT
SELECT columnname, columnname
FROM tablename 2;
MINUS CLAUSE:- The user can put together multiple Queries and combine their output = records
only in Questionry one
Syntax: SELECT columnname, columnname
FROM tablename MINUS
SELECT columnname, columnname
FROM tablename ;

Objective: Answer the following Queries:
QUERIES:

1. Find the product_no and description of non- moving products.
2. Find the customer name, address, city and pincode for the client who has placed order no
“019001”
3. Find the client names who have placed order before the month of may 96.
4. Find out if product “1.44 Drive” is ordered by only client and print the client_no name to
whom it was sold.
5. find the names of client who have placed orders worth Rs.10000 or more.
6. Select the orders placed by ‘Rahul Desai”
7. Select the names of persons who are in Mr. Pradeep’s department and who have also worked
on an inventory control system.
8. Select all the clients and the salesman in the city of Bombay.
9. Select salesman name in “Bombay” who has atleast one client located at “Bombay”
10. Select the product_no, description, qty_on-hand,cost_price of non_moving items in the
product_master table.


Answer:



1. Find the product_no and description of non- moving products.

select product_no, product_description from product_master where product_no not in (select product_no from sales_order_details);

2. Find the customer name, address, city and pincode for the client who has placed order no “019001”

select client_name, client_address, client_city, client_pincode from client_master where client_no = (select client_no from sales_order where s_order_no = '019001');

3. Find the client names who have placed order before the month of may 96.

select client_name from client_master where client_no in (select client_no from sales_order where order_date < '1996-05-01');

4. Find out if product “1.44 Drive” is ordered by only client and print the client_no name to whom it was sold.

select client_name from client_master where client_no in (select client_no from sales_order where s_order_no in (select s_order_no from sales_order_details where product_no = (select product_no from product_master where product_description = '1.44 Drive')));

5. find the names of client who have placed orders worth Rs.10000 or more.

select client_name from client_master where client_no in (select client_no from sales_order where order_value >= 10000);

6. Select the orders placed by ‘Rahul Desai”

select s_order_no from sales_order where client_no = (select client_no from client_master where client_name = 'Rahul Desai');

7. Select the names of persons who are in Mr. Pradeep’s department and who have also worked on an inventory control system.

select employee_name from employee_master where employee_no in (select employee_no from employee_master where department = (select department from employee_master where employee_name = 'Mr. Pradeep')) and employee_no in (select employee_no from project_master where project_name = 'Inventory Control System');

8. Select all the clients and the salesman in the city of Bombay.

select client_name, employee_name from client_master, employee_master where client_city = 'Bombay' and employee_city = 'Bombay';

9. Select salesman name in “Bombay” who has atleast one client located at “Bombay”

select employee_name from employee_master where employee_no in (select employee_no from client_master where client_city = 'Bombay');

10. Select the product_no, description, qty_on-hand,cost_price of non_moving items in the product_master table.

select product_no, product_description, qty_on_hand, cost_price from product_master where product_no not in (select product_no from sales_order_details);

<div style="page-break-after: always;"></div>

Experiment. 9
Theory and Concept
Objective:- To implement the concept of Indexes and views.
Indexes- An index is an ordered list of content of a column or group of columns in a table. An index
created on the single column of the table is called simple index. When multiple table columns are
included in the index it is called composite index.
Creating an Index for a table:-
Syntax (Simple)
 CREATE INDEX index_name
 ON tablename(column name);
Composite Index:- CREATE INDEX index_name
 ON tablename(columnname,columnname);
Creating an UniQuestion Index:- CREATE UNIQUESTION INDEX indexfilename
 ON tablename(columnname);
Dropping Indexes:- An index can be dropped by using DROP INDEX
SYNTAX:-
 DROP INDEX indexfilename;
Views:-
 Logical data is how we want to see the current data in our database. Physical data is how this
data is actually placed in our database.
 Views are masks placed upon tables. This allows the programmer to develop a method via
which we can display predetermined data to users according to our desire.
 Views may be created fore the following reasons:

1. The DBA stores the views as a definition only. Hence there is no duplication of data.
2. Simplifies Queries.
3. Can be Questionried as a base table itself.
4. Provides data security.
5. Avoids data redundancy.
Creation of Views:- Syntax:- CREATE VIEW viewname AS
 SELECT columnname,columnname
 FROM tablename
 WHERE columnname=expression_list;
Renaming the columns of a view:- Syntax:- CREATE VIEW viewname AS
 SELECT newcolumnname….
 FROM tablename
 WHERE columnname=expression_list;
Selecting a data set from a view- Syntax:- SELECT columnname, columnname
 FROM viewname
 WHERE search condition;

Destroying a viewSyntax:-
 DROP VIEW viewname;
Table 1: client_master table

| columnname | datatype | size |
| --- | --- | --- |
| client_no | varchar | 6 |
| name | varchar | 20 |
| city | varchar | 15 |
| state | varchar | 15 |
| pincode | int | 6 |
| bal_due | decimal | 10,2 |

Table 2: product_master table

| columnname | datatype | size |
| --- | --- | --- |
| product_no | varchar | 6 |
| description | varchar | 20 |
| profit_percent | decimal | 10,2 |
| unit_measure | varchar | 15 |
| qty_on_hand | int | 6 |
| reorder_lvl | int | 6 |
| sell_price | decimal | 10,2 |
| cost_price | decimal | 10,2 |

Table 1: sales_master schema

| Columnname | Datatype | Size | Attributes |
|------------|----------|------|------------|
| salesman_no | varchar | 6 | Primary key/first letter must start with ‘s’ |
| sal_name | varchar | 20 | Not null |
| address | varchar | 20 | Not null |
| city | varchar | 20 | |
| state | varchar | 20 | |
| pincode | int | 6 | |
| sal_amt | decimal | 8,2 | Not null, cannot be 0 |
| tgt_to_get | decimal | 6,2 | Not null, cannot be 0 |
| ytd_sales | decimal | 6,2 | Not null, cannot be 0 |
| remarks | varchar | 30 | |

Table 2: sales_order Schema

| Columnname | Datatype | Size | Attributes |
|------------|----------|------|------------|
| s_order_no | varchar | 6 | Primary/first letter must be 0 |
| s_order_date | date | 6 | Primary key reference clientno of client_master table |
| client_no | varchar | 25 |
| dely_add | varchar | 6 |
| salesman_no | varchar | 6 | Foreign key references salesman_no of salesman_master table |
| dely_type | char | 1 | Delivery part(p)/full(f),default f |
| billed_yn | char | 1 |
| dely_date | date | Can not be lessthan s_order_date |
| order_status | varchar | 10 | Values (‘in process’;’fulfilled’;back order’;’canceled |

Table 3: sales_order_details Schema

| Column | Datatype | Size | Attributes |
|--------|----------|------|------------|
| s_order_no | varchar | 6 | Primary key/foreign key references s_order_no of sales_order |
| product_no | varchar | 6 | Primary key/foreign key references product_no of product_master |
| qty_order | int | 8 |
| qty_disp | int | 8 |
| product_rate | decimal | 10,2 |

Table 4: sales_master table data

| salesman_no | salesman name | address | city | pin code | state | salamt | tgt\_to\_g et | ytd sales | remark |
|-------------|---------------|---------|------|----------|-------|--------|--------------|-----------|--------|
| 500001 | Kiran | A/14 worli | Bomba y | 400002 | Mah | 3000 | 100 | 50 | Good |
| 500002 | Manish | 65,nariman | Bomba y | 400001 | Mah | 3000 | 200 | 100 | Good |
| 500003 | Ravi | P-7 Bandra | Bomba y | 400032 | Mah | 3000 | 200 | 100 | Good |
| 500004 | Ashish | A/5 Juhu | Bomba y | 400044 | Mah | 3500 | 200 | 150 | Good |

Table 5: sales_order table data

| s_order_no | s_order_date | client_no | dely_type | billed_yn | salesman_no | dely_date | order_status |
|------------|--------------|-----------|-----------|-----------|-------------|-----------|--------------|
| 019001 | 12-jan-96 | 0001 | F | N | 50001 | 20-jan-96 | Ip |
| 019002 | 25-jan-96 | 0002 | P | N | 50002 | 27-jan-96 | C |
| 016865 | 18-feb-96 | 0003 | F | Y | 500003 | 20-feb-96 | F |
| 019003 | 03-apr-96 | 0001 | F | Y | 500001 | 07-apr-96 | F |
| 046866 | 20-may-96 | 0004 | P | N | 500002 | 22-may-96 | C |
| 010008 | 24-may-96 | 0005 | F | N | 500004 | 26-may-96 | Ip |

Table 6: sales_order_details table data

| s_order_no | product_no | qty_order | qty_disp | product_rate |
|------------|------------|-----------|----------|--------------|
| 019001 | P00001 | 4 | 4 | 525 |
| 019001 | P07965 | 2 | 1 | 8400 |
| 019001 | P07885 | 2 | 1 | 5250 |
| 019002 | P00001 | 10 | 0 | 525 |
| 046865 | P07868 | 3 | 3 | 3150 |
| 046865 | P07885 | 10 | 10 | 5250 |
| 019003 | P00001 | 4 | 4 | 1050 |
| 019003 | P03453 | 2 | 2 | 1050 |
| 046866 | P06734 | 1 | 1 | 12000 |
| 046866 | P07965 | 1 | 0 | 8400 |
| 010008 | P07975 | 1 | 0 | 1050 |
| 010008 | P00001 | 10 | 5 | 525 |

<div style="page-break-after: always;"></div>

Table 1: Challan_Header table

| Column name | Data type | Size | Attributes |
|-------------|-----------|------|------------|
| challan_no | varchar | 6 | Primary key |
| s_order_no | varchar | 6 | Foreign key references s_order_no of sales_order table |
| challan_date | date | not null | |
| billed_yn | char | 1 | values (‘Y’,’N’). Default ‘N’ |

Table 2: Challan_Details table

| Column name | Data type | Size | Attributes |
|-------------|-----------|------|------------|
| challan_no | varchar | 6 | Primary key/Foreign key references Product_no of product_master |
| qty_disp | number | 4,2 | not null |

Table 3: Challan_Header table data

| challan_no | s_order_no | challan_date | billed_yn |
|------------|------------|--------------|-----------|
| CH9001 | 019001 | 12-DEC-95 | Y |
| CH865 | 046865 | 12-NOV-95 | Y |
| CH3965 | 010008 | 12-OCT-95 | Y |

Table 4: Challan_Details table data

| challan_no | qty_disp |
|------------|----------|
| CH9001 | 4 |
| CH9001 | 1 |
| CH9001 | 1 |
| CH6865 | 3 |
| CH6865 | 4 |
| CH6865 | 10 |
| CH3965 | 5 |
| CH3965 | 2 |

<div style="page-break-after: always;"></div>

Table 5: BOOK tables

| Tables | Columns |
|--------|---------|
| BOOK | (Book_id, Title, Publisher_Name, Pub_Year) |
| BOOK_AUTHORS | (Book_id, Author_Name) |
| PUBLISHER | (Name, Address, Phone) |
| BOOK_COPIES | (Book_id, Branch_id, No-of_Copies) |
| BOOK_LENDING | (Book_id, Branch_id, Card_No, Date_Out, Due_Date) |
| LIBRARY_BRANCH | (Branch_id, Branch_Name, Address) |

Objective: Answer the following Questions
Q1. Create an index on the table client_master, field client_no.
Q2. Create an index on the sales_order, field s_order_no.
Q3. Create an composite index on the sales_order_details table for the columns s_order_no and
product_no.
Q4. Create an composite index ch_index on challan_header table for the columns challan no and
s_order_no.
Q5. Create an uniQuestion index on the table salesman_master, field salesman_no.
Q6. Drop index ch_index on table challan_header.
Q7. Create view on salesman_master whose sal_amt is less than 3500.
Q8. Create a view client_view on client_master and rename the columns as name, add1, add2,
city, pcode, state respectively.
Q9. Select the client names from client_view who lives in city ‘Bombay’.
Q10. Drop the view client_view.


Answer:



1. Create an index on the table client_master, field client_no.

create index client_no_index on client_master(client_no);

2. Create an index on the sales_order, field s_order_no.

create index s_order_no_index on sales_order(s_order_no);

3. Create an composite index on the sales_order_details table for the columns s_order_no and product_no.

create index s_order_no_product_no_index on sales_order_details(s_order_no, product_no);

4. Create an composite index ch_index on challan_header table for the columns challan no and s_order_no.

create index ch_index on challan_header(challan_no, s_order_no);

5. Create an uniQuestion index on the table salesman_master, field salesman_no.

create unique index salesman_no_index on salesman_master(salesman_no);

6. Drop index ch_index on table challan_header.

drop index ch_index;

7. Create view on salesman_master whose sal_amt is less than 3500.

create view salesman_view as select * from salesman_master where sal_amt < 3500;

8. Create a view client_view on client_master and rename the columns as name, add1, add2, city, pcode, state respectively.

create view client_view as select client_name as name, add1, add2, city, pcode, state from client_master;

9. Select the client names from client_view who lives in city ‘Bombay’.

select name from client_view where city = ‘Bombay’;

10. Drop the view client_view.

drop view client_view;

<div style="page-break-after: always;"></div>

Experiment No.10
Theory and Concept
Objective:- To implement the basics of PL/SQL.
Introduction – PL/SQL bridges the gap between database technology and procedural
programming languages. It can be thought of as a development tool that extends the facilities of
Oracles SQL database language. Via PL/SQL you can insert, delete, update and retrieve table data as
well as use procedural techniQuestions such as writing loops or branching to another block of code.
PL/SQL Block structureDECLARE
Declarations of memory variables used later
BEGIN
SQL executable statements for manipulating table data.
EXCEPTIONS
SQL and/or PL.SQL code to handle errors.
END;
Displaying user Messages on the screen – Any programming tool requires a method
through which messages can be displayed to the user.
dbms_output is a package that includes a number of procedure and functions that accumulate
information in a buffer so that it can be retrieved later. These functions can also be used to display
message to the user.
put_line: put a piece of information in the buffer followed by a end of line marker. It can also be used
to display message to the user.
Setting the server output on:
SET SERVER OUTPUT ON:
Example: Write the following code in the PL/SQL block to display message to user
DBMS_OUTPUT.PUT_LINE(‘Display user message’);
Conditional control in PL/SQLSyntax:
IF <condition> THEN
<Action>
ELSEIF<condition>
<Action>
ELSE
<Action>
ENDIF;
The WHILE LOOP:
Syntax:
WHILE <condition>
LOOP

<Action>
END LOOP;
The FOR LOOP statement:
Syntax:
FOR variable IN [REVERSE] start—end
LOOP
<Action>
END LOOP;
The GOTO statement: The goto statement allows you to change the flow of control within a
PL/SQL Block.
Q1. WAP in PL/SQL for addition of two numbers.
Q2. WAP in PL/SQL for addition of 1 to 100 numbers.
Q3. WAP in PL/SQL to check the given number is even or odd.
Q4. WAP in PL/SQL to inverse a number, eg. Number 5639 when inverted must be display
 output 9365.
Q5. WAP in PL/SQL for changing the price of product ‘P00001’ to 4000 if the price is less than
 4000 in product_master table. The change is recorded in the old_price_table along with
 product_no and the date on which the price was changed last.


Answer:



1. WAP in PL/SQL for addition of two numbers.

```sql
DECLARE
a INT := 10;
b INT := 20;
c INT;
BEGIN
c := a + b;
DBMS_OUTPUT.PUT_LINE(c);
END;
```

2. WAP in PL/SQL for addition of 1 to 100 numbers.

```sql
DECLARE
a INT := 100;
b INT := 1;
c INT;
BEGIN
LOOP
c := a + b;
b := b + 1;
DBMS_OUTPUT.PUT_LINE(c);
EXIT WHEN b > a;
END LOOP;
END;
```

3. WAP in PL/SQL to check the given number is even or odd.

```sql
DECLARE
a INT := 2;
b INT := 1;
c INT;
BEGIN
c := a % b;
IF c = 0 THEN
DBMS_OUTPUT.PUT_LINE('Even');
ELSE
DBMS_OUTPUT.PUT_LINE('Odd');
END IF;
END;
```

4. WAP in PL/SQL to inverse a number, eg. Number 5639 when inverted must be display output 9365.

```sql
DECLARE
a INT := 5639;
b INT := 0;
c INT;
BEGIN
LOOP
c := a % 10;
b := b * 10 + c;
a := a / 10;
DBMS_OUTPUT.PUT_LINE(b);
EXIT WHEN a = 0;
END LOOP;
END;
```

5. WAP in PL/SQL for changing the price of product ‘P00001’ to 4000 if the price is less than 4000 in product_master table. The change is recorded in the old_price_table along with product_no and the date on which the price was changed last.

```sql
DECLARE
a INT := 4000;
b INT;
c INT;
d VARCHAR2(20) := 'P00001';
BEGIN
SELECT price INTO b FROM product_master WHERE product_no = d;
IF b < a THEN
UPDATE product_master SET price = a WHERE product_no = d;
INSERT INTO old_price_table VALUES (d, b, SYSDATE);
END IF;
END;
```

<div style="page-break-after: always;"></div>
