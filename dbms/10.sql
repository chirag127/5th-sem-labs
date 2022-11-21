-- 1. WAP in PL/SQL for addition of two numbers.
sql
DECLARE a INT := 10;
b INT := 20;
c INT;
BEGIN c := a + b;
DBMS_OUTPUT.PUT_LINE(c);
END;
-- 2. WAP in PL/SQL for addition of 1 to 100 numbers.
sql
DECLARE a INT := 100;
b INT := 1;
c INT;
BEGIN LOOP c := a + b;
b := b + 1;
DBMS_OUTPUT.PUT_LINE(c);
EXIT
WHEN b > a;
END LOOP;
END;
-- 3. WAP in PL/SQL to check the given number is even or odd.
sql
DECLARE a INT := 2;
b INT := 1;
c INT;
BEGIN c := a % b;
IF c = 0 THEN DBMS_OUTPUT.PUT_LINE('Even');
ELSE DBMS_OUTPUT.PUT_LINE('Odd');
END IF;
END;
-- 4. WAP in PL/SQL to inverse a number, eg. Number 5639 when inverted must be display output 9365.
sql
DECLARE a INT := 5639;
b INT := 0;
c INT;
BEGIN LOOP c := a % 10;
b := b * 10 + c;
a := a / 10;
DBMS_OUTPUT.PUT_LINE(b);
EXIT
WHEN a = 0;
END LOOP;
END;
-- 5. WAP in PL/SQL for changing the price of product ‘P00001’ to 4000 if the price is less than 4000 in product_master table. The change is recorded in the old_price_table along with product_no and the date on which the price was changed last.
sql
DECLARE a INT := 4000;
b INT;
c INT;
d VARCHAR2(20) := 'P00001';
BEGIN
SELECT price INTO b
FROM product_master
WHERE product_no = d;
IF b < a THEN
UPDATE product_master
SET price = a
WHERE product_no = d;
INSERT INTO old_price_table
VALUES (d, b, SYSDATE);
END IF;
END;
-- <div style="page-break-after: always;"></div>