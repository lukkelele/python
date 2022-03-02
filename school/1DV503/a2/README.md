## python-sql 
---
![](./simple_csv.png "database ER diagram")
 
It is not certain that a specie *currently* lives on its **homeworld** but for the sake of simplicity I assume that in this case.


---
skin_colors are multivalued attributes which means that they are going to be separate relations.\\
hair_colors are also multivalued but are also NULL quite often.\\
Same goes for eye_colors who has some NULL values (NA) and the rest are single or multivalues.\\
\\
FOREIGN KEY Specie(homeworld) REFERENCES Planet(p_name) \\
Climate should be its own table. CREATE TABLE Environment(climate varchar(20), FOREIGN KEY Planet(p_name));\\
