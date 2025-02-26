import sys
def login():
    print("Welcome to the APU Programming Café, your gateway to a rich learning experience in the world of programming excellence. \nPlease enter your username and password to log in")
    login_successful = False

    # Provide the user with three attempts to enter their username and password
    max_attempts = 0
    while max_attempts < 3:
        max_attempts += 1
        username = input("Enter your username: ")
        password = input("Enter your password: ")

        # Check student login
        with open("student_information", "r") as student_file:
            for line in student_file:
                data = line.strip().split(",")
                if username == data[0] and password == data[1]:
                    print("Login successful!")
                    login_successful = True
                    student_menu()  # Redirect to student menu
                    break

        # Check lecturer login if not successful as student
        if not login_successful:
            with open("lecturer_information", "r") as lecturer_file:
                for line in lecturer_file:
                    data = line.strip().split(",")
                    if username == data[0] and password == data[1]:
                        print("Login successful!")
                        login_successful = True
                        lecturer_menu()  # Redirect to lecturer menu
                        break

        # Check admin login if not successful as student or lecturer
        if not login_successful:
            with open("admin.txt", "r") as admin_file:
                for line in admin_file:
                    data = line.strip().split(",")
                    if username == data[0] and password == data[1]:
                        print("Login successful!")
                        login_successful = True
                        display_menu()
                        break

        # Check trainer login if not successful as student, lecturer, or admin
        if not login_successful:
            with open("register.txt", "r") as trainer_file:
                for line in trainer_file:
                    data = line.strip().split(",")
                    if username == data[0] and password == data[1]:
                        print("Login successful!")
                        login_successful = True
                        trainer_menu()  # Redirect to trainer menu
                        break

        # Check if login was successful
        if login_successful:
            break
        else:
            print("Login failed. Please check your username and password and try again")

    # If login failed after max attempts
    if not login_successful and max_attempts == 3:
        print("You have exceeded the maximum number of login attempts. Please rerun the program to log in")

# Admin
def register_new_trainer():
    name = input("Enter trainer name: ")
    level = input("Enter trainer level: beginner, intermediate, advanced: ")
    password = input("Create password: ")

    if level == "beginner":
        with open("register.txt", 'a') as file:
            file.write(f"{name},{password},{level},python\n")
            print(f"({name}) registered successfully!!")
    elif level == "intermediate":
        with open("register.txt", 'a') as file:
            file.write(f"{name},{password},{level},c++\n")
            print(f"({name}) registered successfully!!")
    elif level == "advanced":
        with open("register.txt", 'a') as file:
            file.write(f"{name},{password},{level},java\n")
            print(f"({name}) registered successfully!!")
    else:
            print("invalid selection")

    display_menu()


def delete_trainer(name):
    lines_to_keep = []
    deleted = False

    with open("register.txt", 'r') as file:
        for line in file:
            trainer_name = line.split(',')[0].strip()
            if name.lower() == trainer_name.lower():
                deleted = True
            else:
                lines_to_keep.append(line)

    if deleted:
        with open("register.txt", 'w') as file:
            file.writelines(lines_to_keep)

        print(f"{name} has been deleted.")
    else:
        print(f"{name} not found in the register.")

    display_menu()


def display_trainers():
    with open("register.txt", 'r') as file:
        for line in file:
            data = line.strip().split(",")
            print(f"{data[0]},{data[2]}")

    display_menu()


def display_trainers_income():
    course = input("Choose the trainer's module (python, c++, java): ").lower()
    total_income = 0

    try:
        with open("enrolled_students.txt", "r") as file:
            for line in file:
                data = line.strip().split(",")
                if len(data) == 4 and course in data[1].lower():
                    total_income += int(data[3])

            print(f"Total income for the trainer: {total_income}")

    except FileNotFoundError:
        print("Enrolled students file not found.")

    display_menu()


def display_feedback_sent_by_trainer():
    with open("feedback.txt","r") as f:
        for line in f:
            data = line.strip().split(",")
            print(f"Trainer: {data[0]} \nFeedback: {data[2]}")

    display_menu()


def display_own_profile():
    try:
        with open('admin.txt', 'r') as file:
            profile_data = file.readline().strip().split(',')
            if len(profile_data) == 4:
                name, password, age, origin,  = profile_data
                print(f"Name: {name}\nPassword: {password} \nAge: {age}\nOrigin: {origin}")
            else:
                print("Invalid data format in the file.")
    except FileNotFoundError:
        print("Profile not found. Please create a profile first.")

    display_menu()


def update_own_profileA():
    name = input("Enter your name: ")
    password = input("Enter your password: ")
    age = input("Enter your age: ")
    origin = input("Enter your origin: ")

    profile_data = f"{name},{password},{age},{origin}\n"

    with open('admin.txt', 'w') as file:
        file.write(profile_data)

    display_menu()


def display_menu():
    print("welcome to apu administrator section:-")
    print("1. Register new trainer ")
    print("2. Delete trainer ")
    print("3. Display trainers ")
    print("4. Display trainers income ")
    print("5. view feedback sent by trainer")
    print("6. display own profile")
    print("7. update own profile status ")
    choice = input("Enter your choice: ")
    if choice == "1":
        register_new_trainer()
    elif choice == "2":
        name_to_delete = input("Enter the name to delete: ")
        delete_trainer(name_to_delete)
    elif choice == "3":
        display_trainers()
    elif choice == "4":
        display_trainers_income()
    elif choice == "5":
        display_feedback_sent_by_trainer()
    elif choice == "6":
        display_own_profile()
    elif choice == "7":
        update_own_profileA()
    else:
        print("Invalid choice. Please enter from 1 to 7")









# Trainer
def add_coaching_class_information():
    # Prompt the user to enter their username
    username_to_find = input("Enter your username: ").strip().capitalize()

    # Prompt the user to input additional information to append to the line
    class_name = input("Enter class name:").strip()
    charges = int(input("Enter class charges:"))
    class_schedule = input("Enter class schedule:").strip()

    found = False

    # Read all lines from the file
    with open("register.txt", "r") as file:
        lines = file.readlines()

    # Open the file in write mode
    with open("register.txt", "w") as file:
        # Iterate over each line in the file
        for line in lines:
            # Split the line by comma and get the username (located at index 0)
            data = line.strip().split(",")
            username = data[0].strip().capitalize()

            # If the username matches the one entered by the user
            if username == username_to_find:
                # Append the additional information to the line
                line = line.strip() + f",{class_name},{charges},{class_schedule}\n"
                found = True

            # Write the modified line back to the file
            file.write(line)

    # Print a message if username is not found
    if not found:
        print("Username not found.")
    else:
        print("Information appended successfully.")

    trainer_menu()


def update_coaching_class_information():
    username_to_find = input("Enter your username: ").strip()

    found = False

    # Read all lines from the file
    with open("register.txt", "r") as file:
        lines = file.readlines()

    # Open the file in write mode
    with open("register.txt", "w") as file:
        # Iterate over each line in the file
        for line in lines:
            # Split the line by comma and get the username (located at index 0)
            data = line.strip().split(",")
            username = data[0].strip()

            # If the username matches the one entered by the user
            if username == username_to_find:
                # Prompt the user to enter the new information
                class_name = input("Enter new class name:").strip()
                charges = int(input("Enter new class charges:"))
                class_schedule = input("Enter new class schedule:").strip()

                # Keep the password and level from the previous register_new_trainer function
                password = data[1].strip()
                level = data[2].strip()

                # Update the line with the new information
                line = f"{username},{password},{level},{data[3]},{class_name},{charges},{class_schedule}\n"

                found = True

            # Write the modified line back to the file
            file.write(line)


    # Print a message if username is not found
    if not found:
        print("Username not found.")
    else:
        print("Information updated successfully.")


    trainer_menu()


def delete():
    username = input("Enter your username: ")
    Flag = False

    # Read the lines from the file
    with open("register.txt", "r") as f:
        lines = f.readlines()

    # Check if the username exists in the file
    for line in lines:
        data = line.strip().split(",")
        if username == data[0]:
            Flag = True
            # Remove indices 4, 5, and 6 from the line
            del data[4:7]
            # Join the remaining data to reconstruct the line
            new_line = ",".join(data) + "\n"
            break

    # If the username exists
    if Flag:
        with open("register.txt", "w") as f:
            # Rewrite the file excluding the line with the specified username
            for l in lines:
                if l.strip().split(",")[0] != username:
                    f.write(l)
            # Write the modified line back to the file
            f.write(new_line)
        print(f"{username} deleted successfully.")
        trainer_menu()
    else:
        print("Trainer not found.")
        trainer_menu()


def view_list_of_students_enrolled_and_paid_for_his_her_module():
    with open("enrolled_students.txt", "r") as f:
        for line in f:
            # Process each line as needed
            print(line.strip())  # For example, printing each line after removing leading/trailing whitespaces

    trainer_menu()


def send_feedback_to_administrator():
    with open("feedback.txt","a") as f:
        Name = input("Enter your name: ")
        TP_Number = input("Enter your tp number: ")
        feedback = input("Please enter your feedback:")
        f.write(f"{Name},{TP_Number},{feedback}")

    trainer_menu()


def update_own_profileT():
    username_to_find = input("Enter your username: ").strip().capitalize()

    found = False

    # Read all lines from the file
    with open("register.txt", "r") as file:
        lines = file.readlines()

    # Open the file in write mode
    with open("register.txt", "w") as file:
        # Iterate over each line in the file
        for line in lines:
            # Split the line by comma and get the username (located at index 0)
            data = line.strip().split(",")
            username = data[0].strip().capitalize()

            # If the username matches the one entered by the user
            if username == username_to_find:
                # Prompt the user to enter the new name and password
                new_name = input("Enter new name: ").strip()
                new_password = input("Enter new password: ").strip()

                # Update the name and password in the line
                data[0] = new_name
                data[1] = new_password

                # Join the modified data back into a comma-separated string
                line = ",".join(data) + "\n"

                found = True

            # Write the modified line back to the file
            file.write(line)

    # Print a message if username is not found
    if not found:
        print("Username not found.")
    else:
        print("Profile updated successfully.")

    trainer_menu()


def trainer_menu():
    print("Welcome to trainer menu:\n1. add coaching class information\n2. update coaching class information\n3. delete\n4. view list of students enrolled and paid for his/her module\n5. send feedback to administrator\n6. update own profile \n7. to exit")

    while True:
        try:
            choice = int(input("Please enter a choice (1-7): "))
            if choice == 1:
                add_coaching_class_information()
            elif choice == 2:
                update_coaching_class_information()
            elif choice == 3:
                delete()
            elif choice == 4:
                view_list_of_students_enrolled_and_paid_for_his_her_module()
            elif choice == 5:
                send_feedback_to_administrator()
            elif choice == 6:
                update_own_profileT()
            elif choice == 7:
                print("Goodbye")
                sys.exit()  # sys.exit() is a function from the sys module in Python used to terminate the program execution. It allows you to exit the program immediately, regardless of its current state or any ongoing processes. Upon encountering sys.exit(), the program halts execution and returns control to the operating system.

            else:
                print("Invalid choice. Please enter an integer number between 1 and 6.")
        except ValueError:
            print("Invalid input. Please enter a valid integer number.")










# Lecturer
def register_and_enroll_student():
    # Function to register and enroll a student
    full_name = input("Enter student's full name: ")
    username = input("Enter student's username: ")
    password = input("Enter student's password: ")
    tp_number = input("Enter student's TP number: ")
    email = input("Enter student's email: ")
    contact_number = input("Enter student's contact number: ")
    address = input("Enter student's address: ")
    gender = input("Enter student's gender (M,F): ")
    birthday = input("Enter student's birthday (YYYY-MM-DD): ")
    month_of_enrollment = input("Enter month of enrollment: ")
    module = input("Enter the modules to enroll in: ")
    level = input("Enter the level to enroll in (Beginner, Intermediate, Advanced): ")

    # Flag to indicate if modules and level combination is found
    Flag = False

    # Read existing lines from the file
    with open("register.txt", "r") as file:
        lines = file.readlines()

    # Check if modules and level combination already exists
    for line in lines:
        data = line.strip().split(",")
        if module.lower() == data[3] and level.lower() == data[2]:
            Flag = True
            break
    # Save student's information in student_information.txt
    if Flag:
        with open("student_information", "a") as file:
            file.write(f"{username},{password},{tp_number},{module.lower()},{level.lower()},{full_name},{email},{contact_number},{address},{gender},{month_of_enrollment},{birthday},{data[0]},{data[5]},{data[6]}\n")
        print(f"Successfully registered {full_name}.")

    if not Flag:
        print("This Module or level is currently unavailable.")


    navigation_menu_L()


def update_subject_enrollment():
    username = input("Enter student's username: ")
    tp_number = input("Enter student's tp number: ")
    student_found = False
    module_level_found = False
    current_leve_or_module = False
    new_level = None
    new_module = None
    current_level = None
    current_module = None

    # Search for the student in the file
    with open("student_information", "r") as f:
        lines = f.readlines()

    # Search for the module and level in the register file
    with open("register.txt", "r") as f:
        register_lines = f.readlines()

    # Check if the student exists in the file
    for line in lines:
        data = line.strip().split(",")
        if username == data[0] and tp_number == data[2]:
            current_module = input("Enter your current module: ").lower()
            current_level = input("Enter your current level: ").lower()
            new_module = input("Enter a new module: ").lower()
            new_level = input("Enter a new level: ").lower()
            student_found = True
            break

    # Check if the module and level exist in the register file
    for line in register_lines:
        data = line.strip().split(",")
        if new_module == data[3] and new_level == data[2]:
            module_level_found = True
            selected_register_line = data
            break
    # Check if the current level and module exist in student information file
    for line in lines:
        data = line.strip().split(",")
        if current_module == data[3] and current_level == data[4]:
            current_leve_or_module = True


    # If the student exists in the file and the module and level exist in the register file, update the register file
    if student_found and module_level_found and current_leve_or_module:
        with open("student_information", "w") as f:
            for line in lines:
                data = line.strip().split(",")
                if username == data[0] and tp_number == data[2] and current_level == data[4] and current_module == data[3]:
                    data[12] = selected_register_line[0]  # Update username
                    data[13] = selected_register_line[5]  # Update full name
                    data[14] = selected_register_line[6]  # Update email
                    data[3] = selected_register_line[3]   # Update module
                    data[4] = selected_register_line[2]   # Update level
                    line = ",".join(data) + '\n'
                f.write(line)
        print("Successfully updated student information.")
    elif not student_found:
        print("Student not found.")
    elif not module_level_found:
        print("This module or level is currently unavailable. Please try again later.")
    elif not current_leve_or_module:
        print("This student is currently not enrolled in this module or level.")

    navigation_menu_L()


def approve_additional_coaching_request():
    Flag = False

    # Search for the student requests in the student requests file
    with open("register.txt", "r") as file:
        register_lines = file.readlines()


    with open("student_requests", "r") as f:
        for line in f:
            requests_data = line.strip().split(",")
            choice = input(f"Would you approve of student {requests_data[0]} enrolling in an additional coaching class {requests_data[3]} (yes, no)? ")
            if choice.lower() == "yes":

                # Check if requests data exist in register.txt file
                for line in register_lines:
                    register_data = line.strip().split(",")
                    if requests_data[3] == register_data[3] and requests_data[4] == register_data[2]:
                          Flag = True
                          break

                # Save student's information in student_information
                if Flag:
                    with open("student_information", "a") as file:
                        file.write(f"{requests_data[0]},{requests_data[1]},{requests_data[2]},{requests_data[3]},{requests_data[4]},{requests_data[5]},{requests_data[6]},{requests_data[7]},{requests_data[8]},{requests_data[9]},{requests_data[10]},{requests_data[11]},{register_data[0]},{register_data[5]},{register_data[6]}\n")
                        print(f"Thank you for your approval. Student {requests_data[0]} will be enrolled in the additional coaching class for subject {requests_data[3]}.")


            elif choice.lower() == "no":
                print(f"Thank you for your response. Student {requests_data[0]} will not be enrolled in the additional coaching class for subject {requests_data[3]}.")


            else:
                print("Invalid input. Please enter 'yes' or 'no'.")

            if not Flag and choice == "yes":
                print("This Module or level is currently unavailable.")

    navigation_menu_L()


def delete_completed_students():
    username = input("Enter student's username: ")
    tp_number = input("Enter student's tp number: ")
    current_module = input("Enter student's module: ")
    student_deleted = False
    student_found = False

    # Read existing student information
    with open("student_information", "r") as f:
        lines = f.readlines()

    # Search for the student in the file
    with open("student_information", "w") as f:
        for line in lines:
            data = line.strip().split(",")
            # Check if username, tp_number, and module match the provided criteria
            if username == data[0] and tp_number == data[2] and current_module == data[3]:
                student_found = True
                delete_student = input(f"Student {username} started on {data[10]}. \nWould you like to delete this student? (yes, no): ")
                if delete_student.lower() == "yes":
                    print(f"Student {username} was deleted successfully.")
                    student_deleted = True
                else:
                    f.write(line)
            else:
                f.write(line)

    if student_found:
        if not student_deleted:
            print("Student not deleted.")
    else:
        print("Student not found, or student is currently not enrolled in this module.")

    navigation_menu_L()


def update_own_profile_L():
    username = input("Enter your current username: ")
    tp_number = input("Enter your current tp number: ")
    Flag = False

    # Read all lines from the file
    with open("lecturer_information", "r") as f:
        lines = f.readlines()

    # Iterate through each line to find the matching user
    for line in lines:
        data = line.strip().split(",")
        if username == data[0] and tp_number == data[2]:
            Flag = True
            full_name = input("Enter a new full name: ")
            new_username = input("Enter a new username: ")
            password = input("Enter a new password: ")
            tp_number = input("Enter a new tp number: ")
            experience = input("Enter your new teaching experience: ")
            email = input("Enter a new email: ")
            contact_number = input("Enter a new contact number: ")
            address = input("Enter a new address: ")
            nationality = input("Enter a new nationality: ")
            birthday = input("Enter a new birthday(YYYY-MM-DD): ")
            gender = input("Enter a new gender(M,F): ")

            # Update the data in the list
            updated_line = f"{new_username},{password},{tp_number},{full_name},{email},{contact_number},{address},{gender},{nationality},{birthday},{experience}\n"
            lines[lines.index(line)] = updated_line
            break  # No need to continue searching after finding the match

    # If the user was not found, print a message
    if not Flag:
        print("Lecturer not found")
    else:
        # Write the updated lines back to the file
        with open("lecturer_information", "w") as f:
            f.writelines(lines)
        print("Lecturer information updated successfully.")

    navigation_menu_L()


def lecturer_menu():
    print("Welcome to lecturer menu:\n1. Register and enroll student\n2. Update subject enrollment of student\n3. Approve request from student to enroll in additional coaching class\n4. Delete student who have completed their coaching class\n5. Update own profile \n6. Exit")

    while True:
        try:
            choice = int(input("Please enter a choice (1-6): "))
            if choice == 1:
                register_and_enroll_student()
            elif choice == 2:
                update_subject_enrollment()
            elif choice == 3:
                approve_additional_coaching_request()
            elif choice == 4:
                delete_completed_students()
            elif choice == 5:
                update_own_profile_L()
            elif choice == 6:
                print("Goodbye")
                sys.exit()
            else:
                print("Invalid choice. Please enter an integer number between 1 and 6.")
        except ValueError:
            print("Invalid input. Please enter a valid integer number.")


def navigation_menu_L():
    # This function is used to navigate the user to the different functions in the program.
    while True:
        try:
            option = int(input("Enter 1 to proceed to the lecturer menu, 2 to return to the login menu, or 3 to exit: "))
            if option == 1:
                lecturer_menu()
            elif option == 2:
                login()
            elif option == 3:
                print("Exiting. We look forward to serving you again in the future.")
                sys.exit()
            else:
                print("Invalid choice. Please enter 1 or 2.")
        except ValueError:
            print("Invalid input. Please enter a valid integer number.")










# Student
def view_schedule_of_student():
        name = input("Enter your name: ")
        Flag = False
       # Read all lines from the file
        with open("student_information", "r") as f:
            lines = f.readlines()

        # Search for the student in the file
        for line in lines:
            data = line.strip().split(",")
            if name == data[0]:  # Assuming the student's name is at index 0 in each line
                schedule = data[14]  # Assuming the schedule is at index 14 in each line
                Flag = True
                print(f"Schedule for {name}: {schedule}")

        if not Flag:
            print("Student not found.")


        navigation_menuS()


def send_request_to_lecturer():
   with open("student_requests", "a") as f:
       username = input("Enter your username: ")
       password = input("Enter your password: ")
       tp_number = input("Enter your tp number: ")
       module = input("Enter the module you would like to request: ")
       level = input("Enter the level you would like to request: ")
       full_name = input("Enter your full name: ")
       gmail = input("Enter your gmail: ")
       contact_number = input("Enter your contact number: ")
       address = input("Enter your address: ")
       gender = input("Enter your gender: ")
       month = input("Enter the month you would like to start: ")
       birthday = input("Enter your birthday(YY-MM-DD): ")
       f.write(f"{username},{password},{tp_number},{module},{level},{full_name},{gmail},{contact_number},{address},{gender},{month},{birthday}\n")
       print("Request has been sent successfully.")

   navigation_menuS()


def delete_request():
    username = input("Enter your student username: ")
    tp_number = input("Enter your student tp number: ")
    Flag = False

    # Search for the student in the file
    with open("student_requests", "r") as f:
        lines = f.readlines()

    # Display student information and ask if they want to delete
    with open("student_requests", "r") as f:
        for line in f:
            data = line.strip().split(",")
            if username == data[0] and tp_number == data[2]:
                Flag = True


    # Rewrite the file excluding the deleted student
    if Flag:
        with open("student_requests", "w") as f:
            for line in lines:
                data = line.strip().split(",")
                if username != data[0] and tp_number != data[2]:
                    f.write(line)


    if not Flag:
        print("Student not found")
        navigation_menuS()


    if Flag:
        print(f"Student {username} was deleted successfully. ")
        navigation_menuS()


def view_invoice_and_make_payment_for_modules_enrolled():
        name = input("Enter your name: ")

        # Read all lines from the student information file
        with open("student_information", "r") as f:
            lines = f.readlines()

        # Search for the student in the file
        for line in lines:
            data = line.strip().split(",")
            if name == data[0]:  # Assuming the student's name is at index 0 in each line
                payment_status = data[13]  # Assuming the payment status is at index 13 in each line

                # Check if the student wants to enroll
                enroll_choice = input(f"Do you want to enroll? (yes or no): ").lower()

                if enroll_choice == "yes":
                    print(f"{name} has paid: {payment_status}")

                    # Add enrolled student information to "enrolled_students.txt"
                    with open("enrolled_students.txt", "a") as enrolled_file:
                        enrolled_file.write(f"{name},{data[3]},{data[4]},{data[13]}\n")

                    print(f"{name} has been enrolled in {data[3]} at level {data[4]} with a charge of {data[13]}.")
                    navigation_menuS()

                else:
                    print(f"{name} has not enrolled.")
                    navigation_menuS()

                return



        print("Student not found.")
        navigation_menuS()


def update_own_profileS():
    username = input("Enter your current username: ")
    tp_number = input("Enter your current tp number: ")
    Flag = False

    # Read all lines from the file
    with open("student_information", "r") as f:
        lines = f.readlines()

    # Iterate through each line to find the matching user
    for line in lines:
        data = line.strip().split(",")
        if username == data[0] and tp_number == data[2]:
            Flag = True
            new_username = input("Enter a new username: ")
            password = input("Enter a new password: ")
            tp_number = data[2]
            module = data[3]  # Keep the existing module
            level = data[4]  # Keep the existing level
            full_name = input("Enter a new full name: ")
            gmail = input("Enter a new gmail: ")
            contact_number = input("Enter a new contact number: ")
            address = input("Enter a new address: ")
            gender = data[9]  # Keep the existing gender
            month = data[10]  # Keep the existing month
            birthday = input("Enter your birthday(YY-MM-DD): ")
            trainer = data[12] # Keep the existing trainer
            charge = data[13]  # Keep the existing charge
            schedule = data[14] # Keep the existing schedule

            # Construct the updated line
            updated_line = f"{new_username},{password},{tp_number},{module},{level},{full_name},{gmail},{contact_number},{address},{gender},{month},{birthday},{trainer},{charge},{schedule}\n"
            # Update the line in the list of lines
            lines[lines.index(line)] = updated_line

    # Write the modified lines back to the file
    with open("student_information", "w") as f:
        f.writelines(lines)

    if Flag:
        print("Profile updated successfully.")
    else:
        print("User not found.")

    navigation_menuS()


def student_menu():
    print("Welcome to student menu:\n1. view_schedule_of_student\n2. send_request_to_lecturer\n3. delete_request\n4. view_invoice_and_make_payment_for_modules_enrolled\n5. Update own profile \n6. Exit")

    while True:
        try:
            choice = int(input("Please enter a choice (1-6): "))
            if choice == 1:
                view_schedule_of_student()
            elif choice == 2:
                send_request_to_lecturer()
            elif choice == 3:
                delete_request()
            elif choice == 4:
                view_invoice_and_make_payment_for_modules_enrolled()
            elif choice == 5:
                update_own_profileS()
            elif choice == 6:
                print("Goodbye")
                sys.exit()  # sys.exit() is a function from the sys module in Python used to terminate the program execution. It allows you to exit the program immediately, regardless of its current state or any ongoing processes. Upon encountering sys.exit(), the program halts execution and returns control to the operating system.

            else:
                print("Invalid choice. Please enter an integer number between 1 and 6.")
        except ValueError:
            print("Invalid input. Please enter a valid integer number.")


def navigation_menuS():
    while True:
        try:
            option = int(input("Enter 1 to proceed to the student menu, or 2 to return to the login menu: "))
            if option == 1:
                student_menu()
            elif option == 2:
                login()
            else:
                print("Invalid choice. Please enter 1 or 2.")
        except ValueError:
            print("Invalid input. Please enter a valid integer number.")


login()
