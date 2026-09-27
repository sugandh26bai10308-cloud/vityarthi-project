Library Book Management System
Project Title

Library Book Management System

Overview

A simple Python console application to manage library books. The system allows a librarian to add books, borrow books, return books, and view the current library inventory with available and total copies.

Features

Add new books or increase copies of existing books

Borrow books when copies are available

Return borrowed books

List all books with author, available copies, and total copies

Command-line interface for easy interaction

Beginner-friendly Python implementation

Technologies / Tools Used

Python 3.x

No external libraries or packages required

Command-line / Terminal

Project Structure
vityarthi-project/
│
├── sourcecode.py
├── README.md
└── STATEMENT.md

Steps to Install & Run
1. Install Python

Make sure Python 3.x is installed on your computer.

You can check the installed version using:

python --version


or:

python3 --version

2. Clone the Repository

Clone the GitHub repository or download the project files.

git clone https://github.com/sugandh26bai10308-cloud/vityarthi-project.git

3. Navigate to the Project Folder
cd vityarthi-project

4. Run the Application

Run the following command:

python sourcecode.py


If your system uses python3, run:

python3 sourcecode.py


No additional dependencies or packages are required.

Available Commands

When the application starts, the following commands are available:

add → Add a new book or increase the number of copies

borrow → Borrow a book if a copy is available

return → Return a borrowed book

list → Display all books and their stock details

quit → Exit the application

Instructions for Testing

Run the application using:

python sourcecode.py


Test the add command by entering a book title, author, and number of copies.

Test the list command to verify that the book has been added.

Test the borrow command using the title of an available book.

Test the list command again to verify that the available copy count has decreased.

Test the return command using the same book title.

Test the list command again to verify that the available copy count has increased.

Use the quit command to exit the application.

Example
Library Book Management System

Command (add / borrow / return / list / quit): add
Enter title: Python Basics
Enter author: John Smith
Enter number of copies: 3
Book added successfully.

Command (add / borrow / return / list / quit): borrow
Enter title: Python Basics
Book borrowed successfully.

Command (add / borrow / return / list / quit): list
Python Basics | John Smith | Available: 2 | Total: 3

Project Report

The project report is available in STATEMENT.md.
