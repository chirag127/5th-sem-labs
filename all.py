with open("dbms/all.sql","w",encoding="utf-8") as f:
    f.write("")



for i in range(1,10):

    if i == 5:

        continue
    with open("dbms/all.sql","a",encoding="utf-8") as f:
        with open("dbms/" + str(i)+'.sql', 'r',encoding="utf-8") as f1:
            f.write(f1.read())


# empty dbms/a.md
with open("dbms/a.md","w",encoding="utf-8") as f:
    f.write("")

for i in range(2,5):



    if i == 2:

        continue
    with open("dbms/a.md","a",encoding="utf-8") as f:
        with open("dbms/" + str(i)+'t.md', 'r',encoding="utf-8") as f1:
            f.write(f1.read())