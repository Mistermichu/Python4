# REPETITIVE FUNCTIONS
def break_lines(quantity):
    print("*" * quantity)


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
                user_input = str(input(":>>> "))
                return user_input
            except ValueError:
                user_input = bad_attribute_value(user_input)


user_class = ["uczeń", "nauczyciel", "wychowawca"]
user_list = {}
user_id = 100

# CREATE USER


def create_student():
    global user_list, user_id
    user_id += 1
    student_name = attribute_type_check(str, "Podaj imie ucznia.")
    student_surname = attribute_type_check(str, "Podaj nazwisko ucznia.")
    student_class = attribute_type_check(str, "Podaj klase ucznia.")
    user_list["S" + str(user_id)] = {
        "Student": {
            "name": student_name,
            "surname": student_surname,
            "class": student_class.upper()
        }
    }
    print(user_list)
    break_lines(10)


def create_teacher():
    print("Hello Teacher")


def create_class_teacher():
    print("Hello Class Teacher")


def create_user():
    select_class = None
    while not isinstance(select_class, str):
        break_lines(20)
        print("Podaj klase użytkownika, jakiego chcesz dodać do bazy.")
        for user_type in user_class:
            print(user_type.upper())
        select_class = attribute_type_check(
            str, "Wprowadź \"STOP\", aby przerwać.").upper()
        if select_class == "UCZEŃ" or select_class == "UCZEN":
            create_student()
        elif select_class == "NAUCZYCIEL":
            create_teacher()
        elif select_class == "WYCHOWAWCA":
            create_class_teacher()
        elif select_class == "STOP":
            break
        else:
            select_class = bad_attribute_value(select_class)


# MAIN MENU


def main_menu():
    user_command = None
    while not isinstance(user_command, str):
        break_lines(40)
        print("Wprowadź komendę:")
        print("UTWÓRZ: Przechodzi do procesu tworzenia użytkowników")
        print("ZARZĄDZAJ: Przechodzi do procesu zarządzania użytkownikami.")
        print("KONIEC: Kończy działanie aplikacji.")
        user_command = str(input(": ")).upper()
        if user_command == "UTWÓRZ" or user_command == "UTWORZ":
            create_user()
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
