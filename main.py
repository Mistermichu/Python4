# GLOBALS

user_class = ["uczeń", "nauczyciel", "wychowawca"]
manage_option = ["klasa", "uczeń", "nauczyciel", "wychowawca"]
user_list = {}
user_id = 100

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


def continue_request():
    print("Czy kontynować?")
    user_confirm = False
    while not user_confirm:
        user_confirm = attribute_type_check(str, ">>>TAK/NIE").upper()
        if user_confirm == "TAK":
            return True
        elif user_confirm == "NIE":
            return False
        else:
            user_confirm = bad_attribute_value(user_confirm)
            user_confirm = False


def confirm_input(*args):
    user_confirm = False
    while not user_confirm:
        break_lines(10)
        print("Czy podane wartości są poprawne")
        for position, input in enumerate(args):
            print(f"{position}.: {input}")
        user_confirm = attribute_type_check(str, ">>>TAK/NIE<<<").upper()
        if user_confirm == "TAK" or user_confirm == "tak":
            return True
        elif user_confirm == "NIE" or user_confirm == "nie":
            return False
        else:
            user_confirm = bad_attribute_value(user_confirm)
            user_confirm = False


def get_student_data(id):
    global user_list
    user_data = user_list[id].get("student", {})
    name = user_data.get("name")
    surname = user_data.get("surname")
    class_room = user_data.get("class")
    teacher_subject = []
    for id, user in user_list.items():
        teacher = None
        subject = None
        if "teacher" in user:
            teacher_class = user["teacher"].get("classes")
            if class_room in teacher_class:
                teacher_name = user["teacher"].get("name")
                teacher_surname = user["teacher"].get("surname")
                teacher = teacher_name + " " + teacher_surname
                subject = user["teacher"].get("subject")
                combined_data = [teacher, subject]
                teacher_subject.append(combined_data)
                continue
    if len(teacher_subject) == 0:
        print(f"Uczeń {name} {surname}")
        print("Brak danych dotyczących przypisanych przedmiotów i nauczycieli.")
    else:
        break_lines(20)
        print(f"Uczeń {name} {surname}")
        break_lines(5)
        print("***NAUCZYCIEL / PRZEDMIOT***")
        for number, teacher_and_subject in enumerate(teacher_subject):
            teacher_name = teacher_and_subject[0]
            subject = teacher_and_subject[1]
            print(f"{number + 1}.: {teacher_name} - {subject}")


# CREATE USER


def check_if_user_exist(input_name, input_surname, user_class):
    global user_list
    if len(user_list) > 0:
        for id, user_data in user_list.items():
            data = user_data.get(user_class, {})
            name = data.get("name")
            surname = data.get("surname")
            if input_name == name and input_surname == surname:
                print(
                    f"Użytkownik {input_name} {input_surname} obecnie w bazie w kategori {(str(user_class).upper())}.")
                continue_process = continue_request()
                if not continue_process:
                    return False
        return True
    else:
        return True


def create_student():
    global user_list, user_id
    user_id += 1
    new_user_class = "student"
    user_confirm = False
    while not user_confirm:
        student_name = attribute_type_check(str, "Podaj imie ucznia.").upper()
        student_surname = attribute_type_check(
            str, "Podaj nazwisko ucznia.").upper()
        new_user = check_if_user_exist(
            student_name, student_surname, new_user_class)
        if not new_user:
            user_id -= 1
            break
        else:
            student_class = attribute_type_check(str, "Podaj klase ucznia.")
            user_confirm = confirm_input(
                student_name, student_surname, student_class)
            if not user_confirm:
                continue_proccess = continue_request()
                if not continue_proccess:
                    user_id -= 1
                    break
            else:
                user_list["S" + str(user_id)] = {
                    new_user_class: {
                        "name": student_name,
                        "surname": student_surname,
                        "class": student_class.upper()
                    }
                }
                break_lines(10)


def create_teacher():
    global user_list, user_id
    user_id += 1
    new_user_class = "teacher"
    user_confirm = False
    while not user_confirm:
        teacher_name = attribute_type_check(
            str, "Podaj imie nauczyciela.").upper()
        teacher_surname = attribute_type_check(
            str, "Podaj nazwisko nauczyciela.").upper()
        new_user = check_if_user_exist(
            teacher_name, teacher_surname, new_user_class)
        if not new_user:
            user_id -= 1
            break
        else:
            teacher_subject = attribute_type_check(
                str, "Podaj nazwe przedmiotu nauczanego.").upper()
            add_class = True
            teacher_classes = []
            print("Wprowadź klasy nauczyciela. Zostaw puste pole aby zastopować")
            while add_class:
                class_input = str(input("Klasa: ")).upper()
                if len(class_input) == 0:
                    add_class = False
                elif isinstance(class_input, str):
                    teacher_classes.append(class_input)
                else:
                    class_input = bad_attribute_value(class_input)
            user_confirm = confirm_input(
                teacher_name, teacher_surname, teacher_subject, teacher_classes)
            if not user_confirm:
                continue_process = continue_request()
                if not continue_process:
                    user_id -= 1
                    break
            else:
                user_list["T" + str(user_id)] = {
                    new_user_class: {
                        "name": teacher_name,
                        "surname": teacher_surname,
                        "subject": teacher_subject,
                        "classes": teacher_classes
                    }
                }
                break_lines(10)


def create_class_teacher():
    global user_list, user_id
    user_id += 1
    new_user_class = "class_teacher"
    user_confirm = False
    while not user_confirm:
        teacher_name = attribute_type_check(
            str, "Podaj imie wychowawcy.").upper()
        teacher_surname = attribute_type_check(
            str, "Podaj nazwisko wychowawcy.").upper()
        new_user = check_if_user_exist(
            teacher_name, teacher_surname, new_user_class)
        if not new_user:
            user_id -= 1
            break
        else:
            leading_class = attribute_type_check(
                str, "Podaj nazwe prowadzonej klasy.").upper()
            user_confirm = confirm_input(
                teacher_name, teacher_surname, leading_class)
            if not user_confirm:
                continue_process = continue_request()
                if not continue_process:
                    user_id -= 1
                    break
            else:
                user_list["CT" + str(user_id)] = {
                    new_user_class: {
                        "name": teacher_name,
                        "surname": teacher_surname,
                        "leading_class": leading_class
                    }
                }
                break_lines(10)


def create_user():
    select_class = None
    while not isinstance(select_class, str):
        break_lines(20)
        print("Podaj klase użytkownika, jakiego chcesz dodać do bazy.")
        for user_type in user_class:
            print(user_type.upper())
        select_class = attribute_type_check(
            str, "Wprowadź \"KONIEC\", aby przerwać.").upper()
        if select_class == "UCZEŃ" or select_class == "UCZEN":
            create_student()
            select_class = None
        elif select_class == "NAUCZYCIEL":
            create_teacher()
            select_class = None
        elif select_class == "WYCHOWAWCA":
            create_class_teacher()
            select_class = None
        elif select_class == "KONIEC":
            break
        else:
            select_class = bad_attribute_value(select_class)


# MANAGE USERS

def manage_class():
    global user_list
    class_name = attribute_type_check(
        str, "Wprowadź nazwę klasy do przeglądu: ").upper()
    student_list = []
    for id, user in user_list.items():
        data = user.get("student", {})
        student_in_class = data.get("class")
        if student_in_class == class_name:
            student = data.get("name") + " " + data.get("surname")
            student_list.append(student)
    class_teacher = "Do klasy nie jest przypisany wychowawca."
    for id, user in user_list.items():
        data = user.get("class_teacher", {})
        if_class_teacher = data.get("leading_class")
        if if_class_teacher == class_name:
            class_teacher = data.get("name") + " " + data.get("surname")
    break_lines(20)
    print(f"Klasa: {class_name}")
    print(f"Wychowawca: {class_teacher}")
    print("Lista uczniów:")
    for student_number, student_name_surname in enumerate(student_list):
        print(f"{student_number + 1}.: {student_name_surname}")
    break_lines(20)


def manage_student():
    global user_list
    name = attribute_type_check(str, "Wprowadź imię ucznia: ").upper()
    surname = attribute_type_check(str, "Wprowadź nazwisko ucznia: ").upper()
    if len(user_list) == 0:
        print("Brak użytkowników w bazie")
    else:
        user_name = None
        user_surname = None
        for id, user in user_list.items():
            if "student" not in user:
                continue
            else:
                user_name = user["student"].get("name")
                user_surname = user["student"].get("surname")
                if name == user_name and surname == user_surname:
                    get_student_data(id)
                    break
                else:
                    user_name = None
                    user_surname = None
                    continue
        if user_name == None and user_surname == None:
            print(f"Nie znaleziono ucznia: {name} {surname}")


def manage_user():
    select_option = None
    while not isinstance(select_option, str):
        break_lines(20)
        print("Wybierz opcje do zarządzania.")
        for option in manage_option:
            print(option.upper())
        select_option = attribute_type_check(
            str, "Wprowadź \"KONIEC\", aby przerwać").upper()
        if select_option == "KLASA":
            manage_class()
            select_option = None
        elif select_option == "UCZEŃ" or select_option == "UCZEN":
            manage_student()
            select_option = None
        elif select_option == "NAUCZYCIEL":
            print("Zarządzaj nauczycielami")
            select_option = None
        elif select_option == "WYCHOWAWCA":
            print("Zarządzaj wychowawcą")
            select_option = None
        elif select_option == "KONIEC":
            break
        else:
            select_option = bad_attribute_value(select_option)


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
            manage_user()
            user_command = None
        elif user_command == "PRINT_USERS":
            for user in user_list.items():
                print(user)
            user_command = None
        elif user_command == "KONIEC":
            print("Koniec")
        else:
            user_command = bad_attribute_value(user_command)


run_app = True
while run_app:
    main_menu()
    run_app = False
