
-- 1. Find the product_no and description of non- moving products.

select product_no, description from product_master where product_no not in (select product_no from sales_order_details where s_order_no in (select s_order_no from sales_order where order_status = 'Ip'));

-- 2. Find the customer name, city and pincode for the client who has placed order no “019001”

select name,  city, pincode from client_master where client_no in (select client_no from sales_order where s_order_no = '019001');

-- 3. Find the client names who have placed order before the month of may 96.


select name from client_master where client_no in (select client_no from sales_order where s_order_date < '1996-05-01');


-- 4. Find out if product “1.44 Drive” is ordered by only client and print the client_no name to whom it was sold.


select client_no, name from client_master where client_no in (select client_no from sales_order where s_order_no in (select s_order_no from sales_order_details where product_no = 'P00001'));


-- 5. find the names of client who have placed orders worth Rs.10000 or more.


select name from client_master where client_no in (select client_no from sales_order where s_order_no in (select s_order_no from sales_order_details where qty_order * product_rate >= 10000));

-- 6. Select the orders placed by ‘Rahul Desai”


select s_order_no from sales_order where client_no in (select client_no from client_master where name = 'Rahul Desai');


-- 7. Select the names of persons who are in Mr. Pradeep’s department and who have also worked on an inventory control system.


-- select name from emp where name= 'Pradeep' and pname = 'Inventory Control System';

-- 8. Select all the clients and the salesman in the city of Bombay.


select name from client_master where city = 'Bombay' UNION select sal_name from sales_master where city = 'Bombay';


-- 9. Select salesman name in “Bombay” who has atleast one client located at “Bombay”


select DISTINCT sal_name from sales_master where salesman_no in (select salesman_no from sales_order where client_no in (select client_no from client_master where city = 'Bombay'));


-- 10. Select the product_no, description, qty_on-hand,cost_price of non_moving items in the product_master table.


select product_no, description, qty_on_hand, cost_price from product_master where product_no not in (select product_no from sales_order_details where s_order_no in (select s_order_no from sales_order where order_status = 'Ip'));
