# a3
## library management
---
A library must keep track of books and their current status (if a person has been lent a book or if it is stored in the library). <br />
**Entities**: <br />
- User (<u>user_id</u>, f_name, l_name, gender, email, phone, address)
- Librarian (<u>emp_id</u>, f_name, l_name, gender, phone, address)
- Library (<u>lib_id</u>, lib_name, address, city, zipcode, country, company)
- Book (<u>isbn</u>, title, genre, price, publication)
- Author (<u>author_id</u>, f_name, l_name) <br />
**Relation entities** <br />
- has_published(<u>author_id</u>, <u>isbn</u>)
- loans(__user_id__, <u>isbn</u>, issued, due_date, fine)
- works_at(__emp_id__, <u>lib_number</u>, hire_date)
---
<img src="./img/library_db_ER.png" height=620px width=960px>
