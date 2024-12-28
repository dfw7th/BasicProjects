import sqlite3  # Import the sqlite3 library for data persistence

print("\nMy To-do List")
while True:  # Will execute until I break the loop
    # Connecting to a database,
    # you create one upon calling the function
    db = sqlite3.connect("task.db")
    cur = db.cursor()

    # Creating a table in out database
    cur.execute(
        """CREATE TABLE IF NOT EXISTS tasks(
        ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        to_dos TEXT (30) NOT NULL,
        status BOOLEAN DEFAULT 0);"""
    )

    # This will be the menu OPTION for our CLI app
    print("\nPlease select an OPTION: ")
    print("1. Add Task")
    print("2. View Task")
    print("3. Delete Task")
    print("4. Quit")

    # Assigning OPTION to be None so the code
    # can access 'OPTION' outside the try block
    OPTION = None

    # Error handling for the OPTION Input
    while OPTION is None:
        try:
            # Designating OPTIONs for the menu selections
            OPTION = int(input("What do you want to do(1-4): "))
        except ValueError:
            print("Please select a valid OPTION")

    # If user selects OPTION 1
    if OPTION == 1:
        task_ = input("Add the task: ")
        # Basically loop will continue to run until the user
        # Enters input
        # If task isn't empty or 0(for our main menu exit block)
        if task_ != "":
            # This is how we insert a row into our table
            # Since we are using user_input, we add the question mark
            QRY = "insert into tasks (to_dos) values(?);"
            # exception handling for our user_input
            try:
                cur = db.cursor()
                cur.execute(QRY, (task_,))  # adding the row
                db.commit()
                print("Task succesfully added")
            except sqlite3.Error as e:
                print(f"error in operation: {e}")
                db.rollback()
            finally:
                # We close the table connection after use
                db.close()
        # Ensures the user adds input
        else:
            while task_ == "":
                print("\nYou didn't add a task, enter a task")
                print("0. Exit to main menu\n")
                task_ = input("Add a task: ")
                if task_ != "":
                    QRY = "insert into tasks (to_dos) values(?);"
                    try:
                        cur = db.cursor()
                        cur.execute(QRY, (task_,))
                        db.commit()
                        print("Task succesfully added")
                    except sqlite3.Error as e:
                        print(f"error in operation: {e}")
                        db.rollback()
                    finally:
                        db.close()

    # Might add a stop block incase user doesn't wanna add a task
    # Incase user don't wanna add a task after selecting this OPTION

    elif OPTION == 2:
        db = sqlite3.connect("task.db")
        SQL = "SELECT * from tasks;"
        cur = db.cursor()
        cur.execute(SQL)
        while True:
            record = cur.fetchone()
            if record is None:
                break
            print(record)
        db.close()

    # If user chooses to delete a row,
    # we print all the rows first, making it easy
    elif OPTION == 3:
        db = sqlite3.connect("task.db")
        SQL = "SELECT * from tasks;"
        cur = db.cursor()
        cur.execute(SQL)
        while True:
            record = cur.fetchone()
            if record is None:
                break
            print(record)
        del_ = int(input("What's the ID of the task you wanna delete: "))
        QRY = "DELETE from tasks where ID=?;"
        try:
            cur.execute(QRY, (del_,))
            db.commit()
            print("Task deleted successfully")
        except sqlite3.Error as e:
            print(f"Error in operation: {e}")
            db.rollback()
        db.close()

    # Breaks from the loop meaning the user is done
    elif OPTION == 4:
        print("Thank you for using our To-do app")
        db.close()
        break

    else:
        print("Please select a valid OPTION")

    db.close()
