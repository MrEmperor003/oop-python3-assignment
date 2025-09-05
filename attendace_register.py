class AttendanceRegister:
    def __init__(self):
        self.register = {}
    def mark_present(self, name):
        self.register[name] = "Present"
    def mark_apsent(self, name):
        self.register[name] = "Apsent"
    def check_status(self, name):
        if name in self.register:
            returnself.register[name]
        else:
            return "Student not found in register"
    def show_register(self):
        return self.register

# Menu-driven program

def main():
    register = AttendanceRegister()

    while True:
        print("\n===== Attendance Register Menu =====")
        print()
        print("1. Mark Present")
        print("2. Mark Absent")
        print("3. Check Student Status")
        print("4. Show Full Register")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            name = input("Enter student name: ")
            register.mark_present(name)
            print(f"{name} marked as Present.")

        elif choice == "2":
            name = input("Enter student name: ")
            register.mark_absent(name)
            print(f"{name} marked as Absent.")

        elif choice == "3":
            name = input("Enter student name: ")
            print(f"{name}: {register.check_status(name)}")

        elif choice == "4":
            print("Full Register:")
            for student, status in register.show_register().items():
                print(f"{student}: {status}")

        elif choice == "5":
            print("Exiting Attendance Register. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


# Run the program
if __name__ == "__main__":
    main()

