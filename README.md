# Codsoft-1
TODO LIST
To-Do List application using the Tkinter library for the graphical user interface, MySQL database for storing tasks, and the PIL (Pillow) library for image handling. Here's a summary of the project:

1. GUI Interface:
- The application creates a graphical user interface (GUI) using Tkinter.
- It includes labels, entry fields, buttons, and a table (Treeview) to display tasks.

2. Application Features:
- Users can add, update, delete, and view tasks in a list.
- Tasks are stored in a MySQL database.

3. Key Components:
- ToDoList class: Manages the entire application.
- Labels and Entry fields for entering task details (ID, Task, Status).
- Buttons for adding, updating, deleting, and exiting the application.
- A Treeview widget to display tasks in a tabular format.
- MySQL database connection and operations for storing and retrieving tasks.

4. Database:
- The application uses a MySQL database named "todolist" to store task information.
- It connects to the database with username and password "root."

5. Functionality:
- Users can add tasks by entering task details and clicking the "ADD" button.
- Tasks can be updated by selecting a task in the table, making changes, and clicking the "UPDATE" button.
- Users can delete a selected task by clicking the "DELETE" button.
- Exiting the application is possible by clicking the "EXIT" button.

6. Data Display:
- The Treeview displays tasks with columns for S.No., Task, and Status.
- Users can click on a task to select it and update or delete it.

7. Image:
- The application displays an image using the PIL library at the top.

8. Error Handling:
- The application provides error messages for various scenarios (e.g., empty task, database connection issues).

9. Main Function:
- The main function initializes the Tkinter application and starts the event loop.

10. Project Execution:
- You need to have Tkinter, MySQL, and the PIL (Pillow) library installed to run this code.
- Ensure you have a MySQL database named "todolist" available with the required structure (columns: S.No., Task, Status).
