# STARTER

### 1. Printing
Write a program print.py, which will print the phrase Knowledge is power!

    on one line,  
    on three lines, one word on each line,  
    inside a rectangle made up by the characters = and |.  
	
---

### 2. Quote
Write a program quote.py which reads a line of text from the keyboard and then prints the same line as a quote (that is inside " "). An example of an execution:

    Write a line of text:  I wish I was a punk rocker with flowers in my hair.
    Quote: "I wish I was a punk rocker with flowers in my hair."
		
  
---

### 3. Fahrenheit
Write a program fahrenheit.py that reads a The Fahrenheit temperature F (a float) from the keyboard and then print the corresponding Celsius temperature C. The realtionship between C and F is:

	     F = (9/5)*C + 32
	     

An example of an execution:

	Provide a temperature in Fahrenheit: 100
	Corresponding temperature in Celsius is 37.77778
	     
	       

---
  
### 4. 5-year Interest
Write a program interest.py which computes the value of your savings S after five years given a certain interest rate P (percentage). You can assume that both S and P are integers. The value should be an integer correctly rounded off. An example of an execution:

    Initial savings: 1000
    Interest rate (in percentages): 9
    
    The value of your savings after 5 years is: 1539
		

---

### 5. Area
Write a program area.py which reads a radius (R, a float) and computes the area A of a circle with radius R. An example of an execution:
  
    Provide radius: 2.5
      
    Corresponding area is 19.6
  
The result should be presented with a single decimal correctly rounded off.  

---

### 6. Time
Write a program time.py, which reads a number of seconds (an integer) and then prints the same amount of time given in hours, minutes and seconds. An example of an execution:

    Give a number of seconds: 9999
    This corresponds to: 2 hours, 46 minutes and 39 seconds.

Hint: Use integer division and the modulus (remainder) operator.

---
  
### 7. Sum of Three
Write a program sumofthree.py which asks the user to provide a three digit number. The program should then compute the sum of the three digits. For example:

    Provide a three digit number: 483
    Sum of digits: 15

---

### 8. Change
Write a program change.py that computes the change a customer should receive when she/he has paid a certain sum. The program should exactly describe the minimum number of Swedish bills and coins that should be returned rounded off to nearest krona (kr). Example:

Price: 372.38
Payment: 1000

Change: 628 kr
1000kr bills: 0
 500kr bills: 1
 200kr bills: 0
 100kr bills: 1
  50kr bills: 0
  20kr bills: 1
  10kr coins: 0
   5kr coins: 1
   2kr coins: 1
   1kr coins: 1
	
---

## IF STATEMENTS

### 1. Largest
Write a program largest.py which reads three integers A, B, C and then prints the largest number. For example

Please provide three integers A, B, C.
Enter A: 23
Enter B: 46
Enter C: -11

The largest number is: 46

Notice: You should solve this problem using if statements. You are not allowed to use any of the max and sort functions that comes with Python.

---

### 2. Taxes
In a (very) simplified version of the Swedish income tax system we have three tax levels depending on your monthly salary:

    You pay a 30% tax on all income below 38.000 SEK/month
    You pay an additional 5% tax on all income in the interval 38.000 SEK/month to 50.000 SEK/month
    You pay an additional 5% tax on all income above 50.000 SEK/month 

Write a program tax.py which reads a (positive) monthly income from the keyboard and then prints the corresponding income tax. For example

Please provide monthly income: 32000
Corresponding income tax:  9600

Please provide monthly income: 46000
Corresponding income tax:  14200

Please provide monthly income: 79000
Corresponding income tax:  27200

---

### 3. Random Number
Write a program randomsum.py generating and printing the sum of five random numbers in the interval [1,100]. For example

    Five random numbers: 78 13 91 2 36
    
    The sum is 222

Hint: Use the function random.randint in the random module
Notice: No reading from the keyboard in this exercise

---

### 4. Classify Numbers
Write a program oddpositive.py which generates a random numer in the interval [-10,10] and classifies it as odd/even and as positive/negative. For example

The generated number is -7

-7 is odd and negative

Notice: No reading from the keyboard in this exercise

---

### 5. Short Name
Write a program shortname.py, reading a first name and a last name (given name and family name) as two strings. The output should consist of the first letter of the first name followed by a dot and a space, followed by the first four letters of the last name. An example of an execution:

    First name: Anakin
    Last name: Skywalker
    Short name: A. Skyw

What happens if the last name consists of less than four letters? 

---