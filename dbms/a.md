<center>
<h1> Experiment 3</h1>
</center>

# Tables

## Table 1: sales_master schema

| Columnname  | Datatype | Size | Attributes                                   |
| ----------- | -------- | ---- | -------------------------------------------- |
| salesman_no | varchar  | 6    | first letter must start with ‘s’ |
| sal_name    | varchar  | 20   | Not null                                     |
| address     | varchar  | 20   | Not null                                     |
| city        | varchar  | 20   |                                              |
| state       | varchar  | 20   |                                              |
| pincode     | int      | 6    |                                              |
| sal_amt     | decimal  | 8,2  | Not null, cannot be 0                        |
| tgt_to_get  | decimal  | 6,2  | Not null, cannot be 0                        |
| ytd_sales   | decimal  | 6,2  | Not null, cannot be 0                        |
| remarks     | varchar  | 30   |                                              |

## Table 2: sales_order Schema

| Columnname   | Datatype | Size                             | Attributes                                                  |
| ------------ | -------- | -------------------------------- | ----------------------------------------------------------- |
| s_order_no   | varchar  | 6                                | Primary/first letter must be 0                              |
| s_order_date | date     | 6                                |                                                             |
| client_no    | varchar  | 25                               | Foreign key reference clientno of client_master table       |
| dely_add     | varchar  | 6                                |
| salesman_no  | varchar  | 6                                | references salesman_no of salesman_master table |
| dely_type    | char     | 1                                | Delivery part(p)/full(f),default f                          |
| billed_yn    | char     | 1                                |
| dely_date    | date     | |Can not be lessthan s_order_date |
| order_status | varchar  | 10                               | Values (‘in process’;’fulfilled’;back order’;’canceled      |

<div style="page-break-after: always;"></div>

## Table 3: sales_order_details Schema

| Column       | Datatype | Size | Attributes                                                      |
| ------------ | -------- | ---- | --------------------------------------------------------------- |
| s_order_no   | varchar  | 6    | Primary key/foreign key references s_order_no of sales_order    |
| product_no   | varchar  | 6    | Primary key/foreign key references product_no of product_master |
| qty_order    | int      | 8    |
| qty_disp     | int      | 8    |
| product_rate | decimal  | 10,2 |

## Table 4: sales_master table data

| salesman_no | salesman name | address    | city    | state | pin code | salamt | tgt_to_g et | ytd sales | remark |
| ----------- | ------------- | ---------- | ------- | ----- | -------- | ------ | ----------- | --------- | ------ |
| 500001      | Kiran         | A/14 worli | Bomba y | Mah   | 400002   | 3000   | 100         | 50        | Good   |
| 500002      | Manish        | 65,nariman | Bomba y | Mah   | 400001   | 3000   | 200         | 100       | Good   |
| 500003      | Ravi          | P-7 Bandra | Bomba y | Mah   | 400032   | 3000   | 200         | 100       | Good   |
| 500004      | Ashish        | A/5 Juhu   | Bomba y | Mah   | 400044   | 3500   | 200         | 150       | Good   |

## Table 5: sales_order table data

| s_order_no | s_order_date | client_no | dely_type | billed_yn | salesman_no | dely_date | order_status |
| ---------- | ------------ | --------- | --------- | --------- | ----------- | --------- | ------------ |
| 019001     | 12-jan-96    | 0001      | F         | N         | 50001       | 20-jan-96 | Ip           |
| 019002     | 25-jan-96    | 0002      | P         | N         | 50002       | 27-jan-96 | C            |
| 016865     | 18-feb-96    | 0003      | F         | Y         | 500003      | 20-feb-96 | F            |
| 019003     | 03-apr-96    | 0001      | F         | Y         | 500001      | 07-apr-96 | F            |
| 046866     | 20-may-96    | 0004      | P         | N         | 500002      | 22-may-96 | C            |
| 010008     | 24-may-96    | 0005      | F         | N         | 500004      | 26-may-96 | Ip           |

<div style="page-break-after: always;"></div>

## Table 6: sales_order_details table data

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
<center>
<h1> Experiment 4</h1>
</center>

# Tables

## Table 1: Challan_Header table

| Column name | Data type | Size | Attributes |
|-------------|-----------|------|------------|
| challan_no | varchar | 6 | Primary key |
| s_order_no | varchar | 6 | Foreign key references s_order_no of sales_order table |
| challan_date | date | not null | |
| billed_yn | char | 1 | values (‘Y’,’N’). Default ‘N’ |

## Table 2: Challan_Details table

| Column name | Data type | Size | Attributes |
|-------------|-----------|------|------------|
| challan_no | varchar | 6 | Primary key/Foreign key references Product_no of product_master |
| qty_disp | number | 4,2 | not null |

## Table 3: Challan_Header table data

| challan_no | s_order_no | challan_date | billed_yn |
|------------|------------|--------------|-----------|
| CH9001 | 019001 | 12-DEC-95 | Y |
| CH865 | 046865 | 12-NOV-95 | Y |
| CH3965 | 010008 | 12-OCT-95 | Y |


<div style="page-break-after: always;"></div>


## Table 4: Challan_Details table data

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

<center>
<h1> Experiment 5</h1>
</center>

## Table 5: BOOK tables

| Tables | Columns |
|--------|---------|
| BOOK | (Book_id, Title, Publisher_Name, Pub_Year) |
| BOOK_AUTHORS | (Book_id, Author_Name) |
| PUBLISHER | (Name, Address, Phone) |
| BOOK_COPIES | (Book_id, Branch_id, No-of_Copies) |
| BOOK_LENDING | (Book_id, Branch_id, Card_No, Date_Out, Due_Date) |
| LIBRARY_BRANCH | (Branch_id, Branch_Name, Address) |
