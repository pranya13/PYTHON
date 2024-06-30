import os

class RecordManager:
    def __init__(self):
        self.doctor_file = 'doctor.txt'
        self.patient_file = 'patient.txt'
        self.check_file_exists(self.doctor_file)
        self.check_file_exists(self.patient_file)

    def check_file_exists(self, filename):
        if not os.path.exists(filename):
            with open(filename, 'w') as f:
                pass

class Menu:
    def __init__(self):
        self.record_manager = RecordManager()

    def display_menu(self):
        print("1. Manage Doctor records")
        print("2. Manage Patient records")
        print("3. Exit")

    def main_menu(self):
        while True:
            self.display_menu()
            choice = int(input("Enter your choice:"))
            if choice == 1:
                self.submenu('doctor')
            elif choice == 2:
                self.submenu('patient')
            elif choice == 3:
                print("Have a nice day!")
                break
            else:
                print("Invalid Choice.")

    def submenu(self, record_type):
        submenu_options = {
            1: self.insert_rec,
            2: self.update_rec,
            3: self.display_rec,
            4: self.delete_rec,
            5: self.search_rec,
            6: self.display_all_rec,
            7: self.main_menu
        }

        while True:
            print(f"Submenu for {record_type} records:")
            print("1. Insert a record")
            print("2. Update a record")
            print("3. Display a record")
            print("4. Delete a record")
            print("5. Search a record")
            print("6. Display all records")
            print("7. Go back to main menu")

            choice = int(input("Enter your choice:"))
            if choice in submenu_options:
                submenu_options[choice](record_type)
            else:
                print("Invalid Choice.")

    def insert_rec(self, record_type):
        # Implementation for inserting a record
        pass

    def update_rec(self, record_type):
        # Implementation for updating a record
        pass

    def display_rec(self, record_type):
        # Implementation for displaying a record
        pass

    def delete_rec(self, record_type):
        # Implementation for deleting a record
        pass

    def search_rec(self, record_type):
        # Implementation for searching a record
        pass

    def display_all_rec(self, record_type):
        # Implementation for displaying all records
        pass

menu = Menu()
menu.main_menu()
