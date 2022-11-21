-- 1. Create an index on the table client_master, field client_no.
create index client_no_index on client_master(client_no);
-- 2. Create an index on the sales_order, field s_order_no.
create index s_order_no_index on sales_order(s_order_no);
-- 3. Create an composite index on the sales_order_details table for the columns s_order_no and product_no.
create index s_order_no_product_no_index on sales_order_details(s_order_no, product_no);
-- 4. Create an composite index ch_index on challan_header table for the columns challan no and s_order_no.
--
create index ch_index on challan_header(challan_no, s_order_no);
-- 5. Create an uniQuestion index on the table salesman_master, field salesman_no.
create unique index salesman_no_index on sales_master(salesman_no);
-- 6. Drop index ch_index on table challan_header.
drop index ch_index on challan_header;
-- 7. Create view on salesman_master whose sal_amt is less than 3500.
create view salesman_view as
select *
from sales_master
where sal_amt < 3500;
-- 8. Create a view client_view on client_master and rename the columns as name, add1, add2, city, pcode, state respectively.
create view client_view as
select name,
    city,
    pincode as pcode,
    state
from client_master;
-- 9. Select the client names from client_view who lives in city ‘Bombay’.
select name
from client_view
where city = 'Bombay';
-- 10. Drop the view client_view.
drop view client_view;
-- <div style="page-break-after: always;"></div>