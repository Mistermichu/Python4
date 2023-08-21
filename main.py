# REPETITIVE FUNCTIONS
def bad_attribute_value(attribute):
    print(
        f"Podana wartość: \"{attribute}\" jest niepoprawna. Spóbuj ponownie.")
    return None


def attribute_type_check(attribute_type, message):
    if attribute_type == str:
        print(message)
        user_input = None
        while not isinstance(user_input, str):
            try:
                user_input = str(input(": "))
                return user_input
            except ValueError:
                user_input = bad_attribute_value(user_input)


user_class = ["uczeń", "nauczyciel", "wychowawca"]
user_list = {}
user_id = 100

# CREATE USER


class Student:
    def __init__(self, name, surname, school_class):
        global user_id
        self.name = name
        self.surname = surname
        self.school_class = school_class
        user_id += 1
        self.id = "S" + str(user_id)


def create_student():
    global user_list
    student_name = attribute_type_check(str, "Podaj imie ucznia.")
    student_surname = attribute_type_check(str, "Podaj nazwisko ucznia.")
    student_class = attribute_type_check(str, "Podaj klase ucznia.")
    new_student = Student(student_name, student_surname, student_class)
    user_list[new_student.id] = {
        "Student": {
            "name": new_student.name,
            "surname": new_student.surname,
            "class": new_student.school_class
        }
    }


def create_user():
    print("Podaj klase użytkownika, jakiego chcesz dodać do bazy:")
    for user_type in user_class:
        print(user_type.upper())
    create_student()
# MAIN MENU


def main_menu():
    user_command = None
    while not isinstance(user_command, str):
        user_command = str(input(": ")).upper()
        if user_command == "UTWÓRZ" or user_command == "UTWORZ":
            print("Utwórz")
            create_user()
            print(user_list)
            user_command = None
        elif user_command == "ZARZĄDZAJ" or user_command == "ZARZADZAJ":
            print("Zarządzaj")
            user_command = None
        elif user_command == "KONIEC":
            print("Koniec")
        else:
            user_command = bad_attribute_value(user_command)


run_app = True
while run_app:
    main_menu()
    run_app = False
