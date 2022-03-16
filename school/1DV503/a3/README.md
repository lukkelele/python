# a3
## library management
---
A library must keep track of books and their current status (if a person has been lent a book or if it is stored in the library). <br />
### **Entities**: <br />
- User (<u>user_id</u>, f_name, l_name, gender, email, phone, address)
- Librarian (<u>emp_id</u>, f_name, l_name, gender, phone, address)
- Library (<u>lib_id</u>, lib_name, address, city, zipcode, country, company)
- Book (<u>isbn</u>, title, genre, price, publication)
- Author (<u>author_id</u>, f_name, l_name) <br />
- has_published(<u>author_id</u>, <u>isbn</u>)
- loans(<u>user_id</u>, <u>isbn</u>, issued, due_date, fine)
- works_at(<u>emp_id</u>, <u>lib_number</u>, hire_date)
---
Having an ID on *Library* only makes sense if the library in turn is owned by a company that has multiple libraries. I might change the key for *Library* for that reason.  

A book can have more than one genre, therefore genre in *Book* is a potential multivalued attribute. Having book details in a separate table could be a solution. For this assignment I'm just going to acknowledge it but keep things as they are.  

---
<img src="./img/library_db_ER.png" height=620px width=960px>
