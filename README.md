# AllowanceBot
As a year 13 student, I built an allowance tracker to keep track of the clothing allowances of the three Ranui children (fictional family).  

This Python script is an application called "AllowanceBot" that helps manage allowances for a family with multiple children. Here's a short description of its key components and functionality:  
- The script uses the tkinter library to create a Graphical User Interface (GUI). I chose to work with Tkinter, popular for creating GUIs in Python.    
- It imports various libraries, including pandas for data manipulation, tkcalendar for date selection, and others for GUI and file operations.  
- The main class, AllowanceBot, manages the overall application and contains methods for displaying different frames/pages.  
- The application has four main pages: StartPage (for password entry and login), MenuPage (the main menu for selecting a child's account), ChildPage (for managing a child's allowance), and ResetPage (for resetting all account data).  
- The MenuPage allows the selection of a child's account and checking for end-of-year bonuses.  
- The ChildPage allows a child to spend money, record purchases, and view spending history.  
- Data for each child's account is stored in separate text files in the "data" directory.  
- The script manages child allowances, allows them to spend money, and even calculates end-of-year bonuses based on certain conditions. It provides a user-friendly interface for the family to manage their finances.  

Note: The script uses images and specific file paths, so it may require modifications to work in a different environment or with different image resources.

This project demonstrates severeal key skills and concepts in software development, including:  
- Object-Oriented Programming (OOP): The project uses object-oriented programming principles to create and manage different classes (e.g., AllowanceBot, StartPage, MenuPage, ChildPage, ResetPage) and objects to organize and structure the code.
- Graphical User Interface (GUI): The project uses the tkinter library to create a graphical user interface (GUI) for the application. It involves designing and implementing GUI components such as windows, frames, buttons, labels, and entry fields.
- File Handling: The code reads and writes data to files using Python's built-in file handling capabilities. It reads data from CSV files and manages child-specific data in text files.
- Data Management: The project involves data management and manipulation tasks, such as parsing CSV files into DataFrames using pandas and processing data for display in the GUI.
- Date and Time Handling: The project utilizes the datetime module to work with dates and times. It also incorporates a date picker widget from the tkcalendar library.
- Exception Handling: The code includes exception handling to catch and handle errors gracefully, ensuring that the application remains robust even in the face of unexpected user input or file handling issues.
- User Input Validation: The code validates user input, such as checking if entered amounts are numeric and within valid ranges.
- User Interface Design: The project involves designing the user interface layout, including the arrangement and styling of GUI components.
- Software Testing: Proper testing and validation of user inputs and program behavior are important aspects of the project to ensure the application functions as expected.


I received an Excellence grade for this project, and was awarded first in Digital Technologies.
