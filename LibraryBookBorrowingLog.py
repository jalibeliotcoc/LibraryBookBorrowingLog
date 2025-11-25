from datetime import datetime, timedelta

print("Welcome to the Library Book Borrowing Log System")

Title = ["The Great Gatsby", "Thirst in Blood", "To Kill a Mockingbird", "Pride and Prejudice", "The legendary Sucal"]
Author = ["Arjun", "Joshua", "James", "Aldave", "Jayvie"]
Year = ["2001", "2002", "2003", "2004", "2005"]
Available = [True, True, True, True, True]

Logs = []
Borrowed = []

while True:
    print("\n--- MAIN MENU ---")
    print("1. Librarian/Teacher")
    print("2. Student/Borrower")
    print("3. Exit")
    main_choice = input("Enter your choice: ")

    if main_choice == "1":
        password = input("Enter librarian password: ")
        if password != "admin123":
            print("Incorrect password!")
            continue

        while True:
            print("\n--- LIBRARIAN MENU ---")
            print("1. Record Borrower and Book")
            print("2. Update Borrowed List")
            print("3. Mark Book as Returned")
            print("4. View All Books")
            print("5. View Logs")
            print("6. Back to Main Menu")
            choice = input("Enter your choice: ")

            if choice == "1":
                student = input("Enter borrower name: ")
                if student.isalpha():
                    print()
                else:
                    print("Invalid Input!")
                    continue
                book = input("Enter book title: ")
                found = False
                for i in range(len(Title)):
                    if book.lower() == Title[i].lower():
                        found = True
                        if Available[i]:
                            Available[i] = False
                            due_date = datetime.now() + timedelta(days=7)
                            Borrowed.append({"student": student, "book": Title[i], "due_date": due_date})
                            Logs.append(f"Librarian recorded {student} borrowed '{Title[i]}'. Due on {due_date.strftime('%m-%d-%Y')}.")
                            print(f"Recorded: {student} borrowed '{Title[i]} by {Author[i]} ({Year[i]})' (Due: {due_date.strftime('%m-%d-%Y')})")
                        else:
                            print("That book is already borrowed.")
                        break
                if not found:
                    print("Book not found.")

            elif choice == "2":
                print("\n--- CURRENTLY BORROWED BOOKS ---")
                if not Borrowed:
                    print("No borrowed books yet.")
                else:
                    for b in Borrowed:
                        print(f"{b['student']} borrowed '{b['book']}' (Due: {b['due_date'].strftime('%m-%d-%Y')})")
                print("---------------------------------")

            elif choice == "3":
                book = input("Enter book title to mark as returned: ")
                found = False
                for b in Borrowed:
                    if b["book"].lower() == book.lower():
                        Borrowed.remove(b)
                        for i in range(len(Title)):
                            if Title[i].lower() == book.lower():
                                Available[i] = True
                        Logs.append(f"Librarian marked '{book}' as returned by {b['student']}.")
                        print(f"Book '{book}' marked as returned.")
                        found = True
                        break
                if not found:
                    print("No record found")

            elif choice == "4":
                print("\n----- LIBRARY BOOKS -----")
                for i in range(len(Title)):
                    status = "Available" if Available[i] else "Borrowed"
                    print(f"{i+1}. {Title[i]} by {Author[i]} ({Year[i]}) - {status}")
                print("--------------------------")

            elif choice == "5":
                print("\n----- TRANSACTION LOGS -----")
                if not Logs:
                    print("No logs yet.")
                else:
                    for log in Logs:
                        print(log)
                print("-----------------------------")

            elif choice == "6":
                break
            else:
                print("Invalid option, please try again.")

    elif main_choice == "2":
        student = input("Please enter your name: ")
        if student.isalpha():
            print()
        else:
            print("Invalid input!")
            continue

        while True:
            print(f"\n--- STUDENT MENU ({student}) ---")
            print("1. Request Book")
            print("2. View Due Dates")
            print("3. View Available Books")
            print("4. Back to Main Menu")
            choice = input("Enter your choice: ")

            if choice == "1":
                book = input("Enter book title to request: ")
                found = False
                for i in range(len(Title)):
                    if book.lower() == Title[i].lower():
                        found = True
                        if Available[i]:
                            print(f"Your request for '{Title[i]}' has been submitted. Please wait for librarian approval.")
                            Logs.append(f"{student} requested to borrow '{Title[i]}'.")
                        else:
                            print("Sorry, that book is currently borrowed.")
                        break
                if not found:
                    print("Book not found.")

            elif choice == "2":
                print(f"\n--- DUE DATES for {student} ---")
                has_due = False
                for b in Borrowed:
                    if b["student"].lower() == student.lower():
                        print(f"'{b['book']}' is due on {b['due_date'].strftime('%m-%d-%Y')}")
                        has_due = True
                if not has_due:
                    print("Invalid Input")
                print("-----------------------------")

            elif choice == "3":
                print("\n--- AVAILABLE BOOKS ---")
                for i in range(len(Title)):
                    if Available[i]:
                        print(f"- {Title[i]} by {Author[i]} ({Year[i]})")
                print("-----------------------")

            elif choice == "4":
                break
            else:
                print("Invalid Option")

    elif main_choice == "3":
        print("Exiting system")
        break
    else:
        print("Invalid Input")