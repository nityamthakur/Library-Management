# Library-Management
This is program that can be used as a Library management system.
It gives the user(librarian) the following options:
1. To display available books
2. To add a book to the library
3. To borrow a book
4. To return a book

The Stock.txt file contains the names of all available books, along with the name of author, quantity and price. Books can be added to the Stock.txt by choosing the Add a book option in the program or by simply adding the names in the text file.
Whenever a book is borrowed, the program asks the user the first ame and last name of the borrower, and then creates a new text file in the format "Borrowed_by:"+firstName+".txt". This file contains all the books the borrower has borrowed along with the date and time of issue.
When a book is returned, the program again aska the user for the first and last name of the borrower, and asks which book is being returned. Then it opens the Borrow file of that person and removes the book from the file.
