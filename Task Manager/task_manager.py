# Notes:
# 1. Use the following username and password to access the admin rights
# username: admin
# password: password
# 2. Ensure you open the whole folder for this task in VS Code otherwise the
# program will look in your root directory for the text files.

# =====importing libraries===========
import os
from datetime import datetime, date

DATETIME_STRING_FORMAT = "%Y-%m-%d"

# Create tasks.txt if it doesn't exist
if not os.path.exists("tasks.txt"):
    with open("tasks.txt", "w") as default_file:
        pass

with open("tasks.txt", "r") as task_file:
    task_data = task_file.read().split("\n")
    task_data = [t for t in task_data if t != ""]

task_list = []
for t_str in task_data:
    curr_t = {}

    # Split by semicolon and manually add each component
    task_components = t_str.split(";")
    curr_t["username"] = task_components[0]
    curr_t["title"] = task_components[1]
    curr_t["description"] = task_components[2]
    curr_t["due_date"] = datetime.strptime(task_components[3], DATETIME_STRING_FORMAT)
    curr_t["assigned_date"] = datetime.strptime(
        task_components[4], DATETIME_STRING_FORMAT
    )
    curr_t["completed"] = task_components[5]

    task_list.append(curr_t)

# ====Login Section====
"""This code reads usernames and password from the user.txt file to
    allow a user to login.
"""
# If no user.txt file, write one with a default account
if not os.path.exists("user.txt"):
    with open("user.txt", "w") as default_file:
        default_file.write("admin;password")

# Read in user_data
with open("user.txt", "r") as user_file:
    user_data = user_file.read().split("\n")

# Convert to a dictionary
username_password = {}
for user in user_data:
    username, password = user.split(";")
    username_password[username] = password

# User validation
logged_in = False
while not logged_in:
    print("💻 LOGIN 💻\n")
    curr_user = input("Username: ")
    curr_pass = input("Password: ")
    if curr_user not in username_password.keys():
        print("❌ User does not exist.\n")
        continue
    elif username_password[curr_user] != curr_pass:
        print("❗Wrong password.\n")
        continue
    else:
        print(f"✔️  Login Successful.")
        logged_in = True


def reg_user():
    """Add a new user to the user.txt file and print relevant message"""
    # - Request input of the new username
    new_username = input("New Username: ")

    # - Request input of the new password
    new_password = input("New Password: ")

    # - Request input of the password again to confirm.
    confirm_password = input("Confirm Password: ")

    # - Check if the username is duplicated or not.
    if new_username in username_password.keys():
        print(" ❗Username exist. Try a different username.")

    else:
        # - Check if the new password matches and confirm that the passwords are the same.
        if new_password == confirm_password:
            # - If they are the same, add them to the user.txt file,
            print("✔️  New user added.")
            username_password[new_username] = new_password

            with open("user.txt", "w") as out_file:
                user_data = []
                for k in username_password:
                    user_data.append(f"{k};{username_password[k]}")
                out_file.write("\n".join(user_data))

            # - Otherwise present a relevant message.
        else:
            print(" ❗Passwords do not match.")


def check_options(input_value, option_list):
    """Check if the user's selected option is valid or not"""
    # - Check the user's entered value, if the value matches one of the options, return the value.
    while input_value not in option_list:
        input_value = input(" ❗Please select a option: ")
    return input_value


def check_date():
    """Check if the user has entered the date and return due_date_time and curr_date_time.
    If the user has entered a due date in the past or entered it in the wrong format, print the error message
    """
    while True:
        try:
            task_due_date = input("Due date of task (YYYY-MM-DD): ")
            due_date_time = datetime.strptime(task_due_date, DATETIME_STRING_FORMAT)
            curr_date_time = date.today()

            # - If the due date time is a past date, print an error message and ask the user to enter the date.
            num_curr = int(str(curr_date_time).replace("-", ""))
            num_due = int(str(due_date_time).replace("-", "")[:9])
            if num_curr > num_due:
                print(" ❗due date must be same or later than today.")
                continue
            break

        except ValueError:
            print(" ❗Invalid datetime format. Please use the format specified.")
    # - return due_date_time
    return due_date_time, curr_date_time


def update_task(str="✔️  Task successfully added."):
    """Writes data to the file task.txt and print relevant message."""
    with open("tasks.txt", "w") as task_file:
        task_list_to_write = []
        for t in task_list:
            str_attrs = [
                t["username"],
                t["title"],
                t["description"],
                t["due_date"].strftime(DATETIME_STRING_FORMAT),
                t["assigned_date"].strftime(DATETIME_STRING_FORMAT),
                t["completed"],
            ]
            task_list_to_write.append(";".join(str_attrs))
        task_file.write("\n".join(task_list_to_write))
    print(str)


def add_task():
    """Allow a user to add a new task to task.txt file and print message.
    Prompt a user for the following:
        - A username of the person whom the task is assigned to,
        - A title of a task,
        - A description of the task and
        - the due date of the task."""
    task_username = input("Name of person assigned to task: ")

    # - If the user does not exist, print error message and return to the main menu.
    if task_username not in username_password.keys():
        print(" ❗User does not exist. Please enter a valid username.")
        return

    task_title = input("Title of Task: ")
    task_description = input("Description of Task: ")

    # - Get the due_date_time and curr_date_time from check_date()
    due_date_time, curr_date_time = check_date()

    # - Make a dictionary with the user's input values.
    new_task = {
        "username": task_username,
        "title": task_title,
        "description": task_description,
        "due_date": due_date_time,
        "assigned_date": curr_date_time,
        "completed": "No",
    }

    task_list.append(new_task)
    update_task()


def print_task(t):
    """Set data in an easy to read format and print"""
    disp_str = f"\n\tTask:\t\t\t{t['title']}\n"
    disp_str += f"\tAssigned to:\t\t{t['username']}\n"
    disp_str += (
        f"\tDate Assigned:\t\t{t['assigned_date'].strftime(DATETIME_STRING_FORMAT)}\n"
    )
    disp_str += f"\tDue Date:\t\t{t['due_date'].strftime(DATETIME_STRING_FORMAT)}\n"
    disp_str += f"\tTask Complete?\t\t{t['completed']}\n"
    disp_str += f"\tTask Description:\n\t  {t['description']}\n"
    disp_str += f"\t__________________________________________________"
    print(disp_str)


def view_all():
    """Reads the task from task.txt file and prints to the console in the
    format of Output 2 presented in the task pdf (i.e. includes spacing
    and labelling)
    """
    disp_str = "\n\t\t\t📝 All tasks\n"
    disp_str += "\t=================================================="
    print(disp_str)
    for t in task_list:
        print_task(t)


def view_mine():
    """Reads the task from task.txt file and prints to the console in the
    format of Output 2 presented in the task pdf (i.e. includes spacing
    and labelling)
    """
    i = 1
    my_list = []
    for t in task_list:
        if t["username"] == curr_user:
            disp_str = f"\n\t\t\tTASK No. {i}\n"
            disp_str += "\t=================================================="
            print(disp_str)
            print_task(t)
            my_list.append(t)
            i += 1

    # - If the user does not have an assigned task, print error message.
    if not len(my_list):
        print(f" ❗No task assigned for user {curr_user}.")
        return

    # - If the user has assigned tasks, allow the user to select either a specific task number or -1 to return to the main menu.
    while True:
        try:
            task_no = int(
                input(
                    "\n👉 To edit the task, Please select the a specific task number or -1 to return to the main menu: "
                )
            )
            # - when the user enters -1 return to the main menu.
            if task_no == -1:
                return
            # - when the user enters a task number that does not exist.
            elif (task_no > len(my_list)) or (task_no < 0):
                print(" ❗Please select a task number.")
            elif (task_no > 0) and (task_no <= len(my_list)):
                option = input(
                    """👉 Please select option below.
            m - Mark the task as complete.
            e - Edit the task.
            : """
                )
                break
        except:
            print(" ❗Please select a number.")

    # - Check the entered value against check_option().
    option = check_options(option, ["m", "e"])

    if option == "m":  # - Mark the task as completed.
        mark_completed = input(
            """👉 Do you want mark your task as completed (y/n)? 
        💡 If the task is marked as completed you can not change or edit the task. 
        : """
        )
        mark_completed = check_options(mark_completed, ["y", "n"])
        if mark_completed == "y":
            my_list[task_no - 1]["completed"] = "Yes"
            msg = "✔️  Your task has been marked as completed."
        elif mark_completed == "n":
            return

    elif option == "e":  # - Edit the task.
        is_completed = my_list[task_no - 1]["completed"]
        # Check if the task completed or not.
        if is_completed == "Yes":
            print(" ❗The task is completed. no more changes allowed.")
            return

        else:
            edit_option = input(
                """👉 Please select option below.
        a - Edit the user assigning.
        d - Edit the due date of task.
        : """
            )
            edit_option = check_options(edit_option, ["a", "d"])
            if edit_option == "a":  # - Edit the user that is assigned to the task.
                name = input("Name of person assigned to task: ")
                my_list[task_no - 1]["username"] = name
                msg = "✔️  User assign successfully changed."

            if edit_option == "d":  # - Edit the due date of the task.
                due_date_time = check_date()
                my_list[task_no - 1]["due_date"] = due_date_time
                msg = "✔️  Due date successfully changed"
    update_task(msg)


def generate_reports():
    """generate reports, two text files, called task_overview.txt and user_overview.txt"""

    """
    # - Create task_overview.txt if it doesn't exist.
        t_overview_file contains:
            - The total number of tasks that have been generated and tracked using the task_manager.py
            - The total number of completed tasks.
            - The total number of uncompleted tasks.
            - The total number of tasks that haven't been completed and that are overdue.
            - The percentage of tasks that are incomplete.
            - The percentage of tasks that are overdue.
    """

    with open("task_overview.txt", "w") as t_overview_file:
        curr_date_time = date.today()
        num_curr = int(str(curr_date_time).replace("-", ""))
        total_t = len(task_list)
        completed_t, uncompleted_t, uncompleted_overdue = 0, 0, 0

        for t in task_list:
            if t["completed"] == "Yes":
                completed_t += 1
            else:
                uncompleted_t += 1
                num_due = int(str(t["due_date"]).replace("-", "")[:9])
                if num_curr > num_due:
                    uncompleted_overdue += 1
        p_uc = round((uncompleted_t / total_t) * 100)
        p_uc_over = round((uncompleted_overdue / total_t) * 100)
        str_t = f"""
        __________________________________________________
        >>> Task overview

            Total tasks:                    {total_t}
            Completed tasks:                {completed_t}
            Uncompleted tasks:              {uncompleted_t}
            Uncompleted and overdue tasks:  {uncompleted_overdue}

            Uncompleted:                    {p_uc} %
            Overdue:                        {p_uc_over} %
        __________________________________________________
        """
        print(str_t)
        t_overview_file.write(str_t)

    """
    # - Create user_overview.txt if it doesn't exist.
        user_overview.txt contains:
            - The total number of users registered with task_manager.py.
            - The total number of tasks that have been generated and tracked using task_manager.py.
            - For each user also describe:
                - The total number of tasks assigned to that user.
                - The percentage of the total number of tasks that have been assigned to that user
                - The percentage of the tasks assigned to that user that have been completed
                - The percentage of the tasks assigned to that user that must still be completed
                - The percentage of the tasks assigned to that user that have not yet been completed and are overdue
    """
    with open("user_overview.txt", "w") as u_overview_file:
        total_u = username_password.keys()
        str_u = f"""
        __________________________________________________
        >>> User_overview

            Total number of users: {len(total_u)}
            Total number of tasks: {total_t}
        ==================================================
        """

        for u in total_u:
            cnt_tasks, com_tasks, unc_tasks, unc_over = 0, 0, 0, 0
            for t in task_list:
                if t["username"] != u:
                    continue
                # - When the user id matches the username
                else:
                    cnt_tasks += 1
                    if t["completed"] == "Yes":
                        com_tasks += 1
                    else:
                        unc_tasks += 1
                        num_due = int(str(t["due_date"]).replace("-", "")[:9])
                        if num_curr > num_due:
                            unc_over += 1

            p_user = round((cnt_tasks / total_t) * 100)
            if cnt_tasks == 0:
                p_com, p_unc, p_u_over = 0, 0, 0
            else:
                p_com = round((com_tasks / cnt_tasks) * 100)
                p_unc = round((unc_tasks / cnt_tasks) * 100)
                p_u_over = round((unc_over / cnt_tasks) * 100)

            str_u += f"""
            Username:                   {u}

            Tasks assigned:             {p_user} % ({cnt_tasks})
            Completed tasks:            {p_com} %
            Uncompleted tasks:          {p_unc} %
            Uncompleted and overdue:    {p_u_over} %
        __________________________________________________
            """
        print(str_u)
        u_overview_file.write(str_u)


def display_statistics():
    """If the user is an admin read task_overview.txt and user_overview.txt then, print reports."""
    try:
        with open("task_overview.txt", "r") as t_overview:
            print(t_overview.read())

        with open("user_overview.txt", "r") as u_overview:
            print(u_overview.read())
    except:
        generate_reports()


while True:
    # - Presenting the menu to the user.
    # - Making sure that the user input is converted to lower case.
    print()
    gen_option = """
    r  - Registering a user
    a  - Adding a task
    va - View all tasks
    vm - View my tasks
    e  - Exit
    """
    admin_option = """   gr - Generate reports
    ds - Display statistics
    e  - Exit
    """

    # - General user can see options without 'gr' and 'ds'
    option_str = gen_option

    # - Admin user can see options with 'gr' and 'ds'
    if curr_user == "admin":
        option_str = gen_option[:100] + admin_option

    menu = input(
        f"""👉 Please select one of the following options:
    {option_str}
: """
    ).lower()

    if menu == "r":
        reg_user()

    elif menu == "a":
        add_task()

    elif menu == "va":
        view_all()

    elif menu == "vm":
        view_mine()

    elif menu == "gr" and curr_user == "admin":  # - Only available for admin user.
        generate_reports()

    elif menu == "ds" and curr_user == "admin":  # - Only available for admin user.
        display_statistics()

    elif menu == "e":
        print("Goodbye!!!")
        exit()

    else:
        print(" ❗You have made a wrong choice, Please Try again.")
