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
   Create table client_master AS SELECT \* FROM oldclient_master;
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
| ---------- | -------- | ---- |
| client_no  | varchar  | 6    |
| name       | varchar  | 20   |
| city       | varchar  | 15   |
| state      | varchar  | 15   |
| pincode    | int      | 6    |
| bal_due    | decimal  | 10,2 |

Table 2: product_master table

| columnname     | datatype | size |
| -------------- | -------- | ---- |
| product_no     | varchar  | 6    |
| description    | varchar  | 20   |
| profit_percent | decimal  | 10,2 |
| unit_measure   | varchar  | 15   |
| qty_on_hand    | int      | 6    |
| reorder_lvl    | int      | 6    |
| sell_price     | decimal  | 10,2 |
| cost_price     | decimal  | 10,2 |

Table 1: sales_master schema

| Columnname  | Datatype | Size | Attributes                                   |
| ----------- | -------- | ---- | -------------------------------------------- |
| salesman_no | varchar  | 6    | Primary key/first letter must start with ‘s’ |
| sal_name    | varchar  | 20   | Not null                                     |
| address     | varchar  | 20   | Not null                                     |
| city        | varchar  | 20   |                                              |
| state       | varchar  | 20   |                                              |
| pincode     | int      | 6    |                                              |
| sal_amt     | decimal  | 8,2  | Not null, cannot be 0                        |
| tgt_to_get  | decimal  | 6,2  | Not null, cannot be 0                        |
| ytd_sales   | decimal  | 6,2  | Not null, cannot be 0                        |
| remarks     | varchar  | 30   |                                              |

Table 2: sales_order Schema

| Columnname   | Datatype | Size                             | Attributes                                                  |
| ------------ | -------- | -------------------------------- | ----------------------------------------------------------- |
| s_order_no   | varchar  | 6                                | Primary/first letter must be 0                              |
| s_order_date | date     | 6                                | Primary key reference clientno of client_master table       |
| client_no    | varchar  | 25                               |
| dely_add     | varchar  | 6                                |
| salesman_no  | varchar  | 6                                | Foreign key references salesman_no of salesman_master table |
| dely_type    | char     | 1                                | Delivery part(p)/full(f),default f                          |
| billed_yn    | char     | 1                                |
| dely_date    | date     | Can not be lessthan s_order_date |
| order_status | varchar  | 10                               | Values (‘in process’;’fulfilled’;back order’;’canceled      |

Table 3: sales_order_details Schema

| Column       | Datatype | Size | Attributes                                                      |
| ------------ | -------- | ---- | --------------------------------------------------------------- |
| s_order_no   | varchar  | 6    | Primary key/foreign key references s_order_no of sales_order    |
| product_no   | varchar  | 6    | Primary key/foreign key references product_no of product_master |
| qty_order    | int      | 8    |
| qty_disp     | int      | 8    |
| product_rate | decimal  | 10,2 |

Table 4: sales_master table data

| salesman_no | salesman name | address    | city    | pin code | state | salamt | tgt_to_g et | ytd sales | remark |
| ----------- | ------------- | ---------- | ------- | -------- | ----- | ------ | ----------- | --------- | ------ |
| 500001      | Kiran         | A/14 worli | Bomba y | 400002   | Mah   | 3000   | 100         | 50        | Good   |
| 500002      | Manish        | 65,nariman | Bomba y | 400001   | Mah   | 3000   | 200         | 100       | Good   |
| 500003      | Ravi          | P-7 Bandra | Bomba y | 400032   | Mah   | 3000   | 200         | 100       | Good   |
| 500004      | Ashish        | A/5 Juhu   | Bomba y | 400044   | Mah   | 3500   | 200         | 150       | Good   |

Table 5: sales_order table data

| s_order_no | s_order_date | client_no | dely_type | billed_yn | salesman_no | dely_date | order_status |
| ---------- | ------------ | --------- | --------- | --------- | ----------- | --------- | ------------ |
| 019001     | 12-jan-96    | 0001      | F         | N         | 50001       | 20-jan-96 | Ip           |
| 019002     | 25-jan-96    | 0002      | P         | N         | 50002       | 27-jan-96 | C            |
| 016865     | 18-feb-96    | 0003      | F         | Y         | 500003      | 20-feb-96 | F            |
| 019003     | 03-apr-96    | 0001      | F         | Y         | 500001      | 07-apr-96 | F            |
| 046866     | 20-may-96    | 0004      | P         | N         | 500002      | 22-may-96 | C            |
| 010008     | 24-may-96    | 0005      | F         | N         | 500004      | 26-may-96 | Ip           |

Table 6: sales_order_details table data

| s_order_no | product_no | qty_order | qty_disp | product_rate |
| ---------- | ---------- | --------- | -------- | ------------ |
| 019001     | P00001     | 4         | 4        | 525          |
| 019001     | P07965     | 2         | 1        | 8400         |
| 019001     | P07885     | 2         | 1        | 5250         |
| 019002     | P00001     | 10        | 0        | 525          |
| 046865     | P07868     | 3         | 3        | 3150         |
| 046865     | P07885     | 10        | 10       | 5250         |
| 019003     | P00001     | 4         | 4        | 1050         |
| 019003     | P03453     | 2         | 2        | 1050         |
| 046866     | P06734     | 1         | 1        | 12000        |
| 046866     | P07965     | 1         | 0        | 8400         |
| 010008     | P07975     | 1         | 0        | 1050         |
| 010008     | P00001     | 10        | 5        | 525          |

<div style="page-break-after: always;"></div>

Table 1: Challan_Header table

| Column name  | Data type | Size     | Attributes                                             |
| ------------ | --------- | -------- | ------------------------------------------------------ |
| challan_no   | varchar   | 6        | Primary key                                            |
| s_order_no   | varchar   | 6        | Foreign key references s_order_no of sales_order table |
| challan_date | date      | not null |                                                        |
| billed_yn    | char      | 1        | values (‘Y’,’N’). Default ‘N’                          |

Table 2: Challan_Details table

| Column name | Data type | Size | Attributes                                                      |
| ----------- | --------- | ---- | --------------------------------------------------------------- |
| challan_no  | varchar   | 6    | Primary key/Foreign key references Product_no of product_master |
| qty_disp    | number    | 4,2  | not null                                                        |

Table 3: Challan_Header table data

| challan_no | s_order_no | challan_date | billed_yn |
| ---------- | ---------- | ------------ | --------- |
| CH9001     | 019001     | 12-DEC-95    | Y         |
| CH865      | 046865     | 12-NOV-95    | Y         |
| CH3965     | 010008     | 12-OCT-95    | Y         |

Table 4: Challan_Details table data

| challan_no | qty_disp |
| ---------- | -------- |
| CH9001     | 4        |
| CH9001     | 1        |
| CH9001     | 1        |
| CH6865     | 3        |
| CH6865     | 4        |
| CH6865     | 10       |
| CH3965     | 5        |
| CH3965     | 2        |

<div style="page-break-after: always;"></div>

Table 5: BOOK tables

| Tables         | Columns                                           |
| -------------- | ------------------------------------------------- |
| BOOK           | (Book_id, Title, Publisher_Name, Pub_Year)        |
| BOOK_AUTHORS   | (Book_id, Author_Name)                            |
| PUBLISHER      | (Name, Address, Phone)                            |
| BOOK_COPIES    | (Book_id, Branch_id, No-of_Copies)                |
| BOOK_LENDING   | (Book_id, Branch_id, Card_No, Date_Out, Due_Date) |
| LIBRARY_BRANCH | (Branch_id, Branch_Name, Address)                 |

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
