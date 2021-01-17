
MEMBER = []

class Person:

    def __init__(self, name, age, gender, phone):
        self.name = name
        self.age = age
        self.gender = gender
        self.phone = phone

    def show_id(self):
        return (f"Name : {self.name}\nAge : {self.age}\nGender : {self.gender}\n")

class Operations:

    @staticmethod
    def add_member():
        new_phone = input("Phone: ")

        for i in range(len(MEMBER)):
            if new_phone == MEMBER[i].phone:
                print("\nPhone number has been registered!")
                print(MEMBER[i].show_id())
                break
        
        else:
            new_name = input("Name: ")
            new_age = int(input("Age: "))
            new_gender = input("Gender: ")

            MEMBER.append(Person(new_name, new_age, new_gender, new_phone)) 

    @staticmethod
    def show_id():
        find_phone = input("Phone: ")

        for i in range(len(MEMBER)):
            if find_phone == MEMBER[i].phone:
                print(MEMBER[i].show_id())
                break

        else:
            print("No User Found!")
            
    
    @staticmethod
    def change_id():
        pass


class Display:

    @staticmethod
    def menus():
        print("1. Add new member")
        print("2. Show member ID")
        print("3. Change ID")
        print("4. Quit")

    @staticmethod
    def main_menu():
        print("\n" * 100)
        Display.menus()
        member = []

        while True:
            choosen = (input("\nChoose a process: "))
            
            if int(choosen) == 1:
                Operations.add_member()

            elif int(choosen) == 2:
                Operations.show_id()

            elif int(choosen) == 3:
                pass

            elif int(choosen) == 4:
                break

            else:
                print("INVALID PROCESS (Choose between 1 - 4)\n")

Display.main_menu()