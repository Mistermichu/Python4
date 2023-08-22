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
    global user_list, user_id
    user_id += 1
    teacher_name = attribute_type_check(str, "Podaj imie nauczyciela.")
    teacher_surname = attribute_type_check(str, "Podaj nazwisko nauczyciela.")
    teacher_subject = attribute_type_check(
        str, "Podaj nazwe przedmiotu nauczanego.")
    add_class = True
    teacher_classes = []
    print("Wprowadź klasy nauczyciela. Zostaw puste pole aby zastopować")
    while add_class:
        class_input = str(input("Klasa: "))
        if len(class_input) == 0:
            add_class = False
        elif isinstance(class_input, str):
            teacher_classes.append(class_input)
        else:
            class_input = bad_attribute_value(class_input)
    user_list["T" + str(user_id)] = {
        "Teacher": {
            "name": teacher_name,
            "surname": teacher_surname,
            "subject": teacher_subject,
            "classes": teacher_classes
        }
    }
    print(user_list)
    break_lines(10)


def create_class_teacher():
    global user_list, user_id
    teacher_name = attribute_type_check(str, "Podaj imie nauczyciela.")
    teacher_surname = attribute_type_check(str, "Podaj nazwisko nauczyciela.")
    for id in user_list.items():
        print(f"ID: {id}")
        for user_class in id:
            import ipdb
            ipdb.set_trace()
            print(f"User class: {user_class}")
            if user_class == "Teacher":
                name = user_list.get(id, "Teacher", "name")
                surname = user_list.get(id, "Teacher", "surname")
                if name == teacher_name and surname == teacher_surname:
                    print(
                        f"Nauczyciel obecnie w bazie. ID: {id}. Czy to ten sam użytkownik?")
                    user_input = None
                    while not isinstance(user_input, str):
                        user_input = attribute_type_check(
                            str, "TAK/NIE").upper()
                        if user_input == "TAK":
                            assigned_class = attribute_type_check(
                                str, "Podaj nazwe prowadzonej klasy.")
                            user_list[id, "Teacher",
                                      "assigned_class"] = assigned_class
                            print(user_list)
                            break_lines(10)
                        elif user_input == "NIE":
                            user_id += 1
                            user_list["T" + str(user_id)] = {
                                "Teacher": {
                                    "name": teacher_name,
                                    "surname": teacher_surname
                                }
                            }
                            print(user_list)
                            break_lines(10)
                        else:
                            user_input = bad_attribute_value(user_input)
    assigned_class = attribute_type_check(
        str, "Podaj nazwe prowadzonej klasy.")
    user_id += 1
    user_list["T" + str(user_id)] = {
        "Teacher": {
            "name": teacher_name,
            "surname": teacher_surname,
            "assigned_class": assigned_class
        }
    }
    print(user_list)
    break_lines(10)


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
