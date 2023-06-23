# HyperionDev Capstone Project - Task Manager :memo:

Task Manager project is written in Python as part of a task for HyperionDev's Dfe Software Engineering Bootcamp.  
With this program, a general user can register users, create tasks and show existing tasks. In addition, an admin user can generate reports and display statistics.

## :blossom: Contents
[Installation ](#blossom-installation)  
[Usage](#blossom-usage)  
　　[r  - Register user](#r---registering-a-user)  
　　[a  - Adding a task](#a---adding-a-task)  
　　[va - View all tasks](#va---view-all-tasks)  
　　[vm - View my tasks](#vm---view-my-tasks)   
　　　　[m  - Mark the task as complete](#m---mark-the-task-as-complete)    
　　　　[ea - Edit the user assigning](#ea---edit-the-user-assigning)  
　　　　[ed - Edit the due date of task](#ed---edit-the-due-date-of-task)   
　　[gr - Generate reports (admin only)](#gr---generate-reports)   
　　[ds - Display statistics (admin only](#ds---display-statistics)   
　　[e  - Exit](#e---exit) 

## :blossom: Installation
:bulb: To run this program, you will be need to download the Python interpreter and IDE onto your computer so that you can view and run it.

Please find installation instructions below:

1. Clone this repository `https://github.com/isle88/finalCapstone.git`  
2. Use your preference of IDE (e.g. VS Code).
<p align="center">
<img src="https://github.com/isle88/finalCapstone/assets/93147798/f8b5696b-a944-497f-bcdb-85bee6e23d10">
</p>  

3. You can either open Task Manager folder on IDE or open finalCapstone folder on IDE and enter `cd '.\Task Manager\'` on your terminal.
4. Check the directory has changed (Please see the arrow at the bottom of the image above).
5. Type `python task_manager.py` on your terminal or click :arrow_forward: button at top right of your IDE (Please see the arrow at the top of the image above).
  
## :blossom: Usage
:bulb: Please find below instructions on how to use the program:

Please login as admin first and register new users. If you do not do this, the program will print an error message and ask for login details again.  
 ```
 username : admin
 password: password
 ```    
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src="https://github.com/isle88/finalCapstone/assets/93147798/3f1e6580-f36b-47f3-afd1-7e1fc9312da5">
### r - Registering a user.  

:white_check_mark: If the user enters their new username and confirms their password correctly, the program will add the user and print a confirmation message.   

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src="https://github.com/isle88/finalCapstone/assets/93147798/a6458e25-0468-42be-8d6e-6ee3ddc317ba">      
:x: If the user enters an existing username, it will print an error message and return to the main menu.  
:x: If the user enters a username and password that do not match, the program will print an error message and return to the main menu.  

### a - Adding a task.  
:white_check_mark: If the user enters an existing username and enters the correct format of date, the task will be successfully added.  

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src="https://github.com/isle88/finalCapstone/assets/93147798/eae8e186-0d1d-4e3c-96ca-24ed4b046e8d">  
:x: If the user enters a username that does not exist, the program will print an error message and return to the main menu.  
:x: If the user enters a due date in the past or enters it in the wrong format, the program will print an error message.        
                                                                             
### va - View all tasks.  
:white_check_mark: Reads the task from task.txt file and prints output in a readable format.  

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src="https://github.com/isle88/finalCapstone/assets/93147798/65b8c264-f6aa-4696-82c3-85230aeb0050">    
  
### vm - View my tasks.  
:white_check_mark: Matches the tasks against the logged-in username from task.txt file and prints output in a readable format. It also asks the user whether they want to edit their task or return to the main menu.  

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src="https://github.com/isle88/finalCapstone/assets/93147798/8875ba47-c74f-48a3-8c3c-506ff7571669">    
:x: If the user does not have an assigned task, the program prints an error message.    
  
  #### m - Mark the task as complete.
  :bulb: If the task is marked as being complete, the user cannot change or edit the task.  
  　  If the user enters `y`, the task is marked as being complete. Otherwise, the user can return to the main menu.  
     
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src="https://github.com/isle88/finalCapstone/assets/93147798/8c3c9e5b-9103-4edb-8e35-54d419ca26c5">
      
  #### ea - Edit the user assigning.  
  :white_check_mark: When the user changes who the task is assigned to, if the user enters an existing username, the program will update the assigned user and print confirmation message.  
  
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src="https://github.com/isle88/finalCapstone/assets/93147798/c6c4c139-c72f-4a8d-aa21-1e351a7b934d">  
  :x: If the user enters a username that does not exist, the program will print an error message and return to the main menu.  
       
  #### ed - Edit the due date of task.  
  :white_check_mark: If the user enters a new due date in the correct format, the program will update the due date and print confirmation message.     
  
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src="https://github.com/isle88/finalCapstone/assets/93147798/7f6bc6a2-2730-4365-b5c3-546aaa7f9a4a">  
  :x: If the user has entered a due date in the past or entered it in the wrong format, the program will print an error message and ask the user to enter the date again.  
  
### gr - Generate reports.
This feature is only accessible to the admin user.  
Generate reports, two text files, called task_overview.txt and user_overview.txt and print messages.

Task overview contains: 
- The total number of tasks that have been generated and tracked using the task_manager.py.
- The total number of completed tasks.
- The total number of uncompleted tasks.
- The total number of tasks that have not been completed and are overdue.
- The percentage of tasks that are incomplete.
- The percentage of tasks that are overdue.

User overview contains:
- The total number of users registered with task_manager.py.
- The total number of tasks that have been generated and tracked using task_manager.py.
- For each user, also describe:
  - The total number of tasks assigned to that user.  
  - The percentage of the total number of tasks that have been assigned to that user.
  - The percentage of the tasks assigned to that user that have been completed.
  - The percentage of the tasks assigned to that user that are still to be completed.
  - The percentage of the tasks assigned to that user that have not yet been completed and are overdue.  
   
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src="https://github.com/isle88/finalCapstone/assets/93147798/13243d3b-3a22-437e-8147-fc9fce1f452a">  


### ds - Display statistics.  
This feature is only accessible to the admin user.  
Read task_overview.txt and user_overview.txt and print reports.   

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src="https://github.com/isle88/finalCapstone/assets/93147798/64990032-ec28-4f9e-95c5-39d17c023a2c">   

### e - Exit.
End the program.  

## Credits
This project is written by isle88 in line with HyperionDev instructions.  
