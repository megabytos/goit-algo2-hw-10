class Teacher:
    def __init__(self, first_name, last_name, age, email, can_teach_subjects):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.can_teach_subjects = set(can_teach_subjects)
        self.assigned_subjects = set()


def create_schedule(subjects, teachers):
    schedule = []
    remaining_subjects = set(subjects)

    while remaining_subjects:
        teachers.sort(key=lambda teacher: (-len(teacher.can_teach_subjects & remaining_subjects), teacher.age))
        best_teacher = teachers[0]
        subjects_to_assign = best_teacher.can_teach_subjects & remaining_subjects
        if not subjects_to_assign:
            return None
        best_teacher.assigned_subjects = subjects_to_assign
        schedule.append(best_teacher)
        remaining_subjects -= subjects_to_assign

    return schedule


if __name__ == '__main__':
    subjects = {'Математика', 'Фізика', 'Хімія', 'Інформатика', 'Біологія'}

    teachers = [Teacher("Олександр", "Іваненко", 45, "o.ivanenko@example.com", {'Математика', 'Фізика'}),
                Teacher('Марія', 'Петренко', 38, 'm.petrenko@example.com', {'Хімія'}),
                Teacher('Сергій', 'Коваленко', 50, 's.kovalenko@example.com', {'Інформатика', 'Математика'}),
                Teacher('Наталія', 'Шевченко', 29, 'n.shevchenko@example.com', {'Біологія', 'Хімія'}),
                Teacher('Дмитро', 'Бондаренко', 35, 'd.bondarenko@example.com', {'Фізика', 'Інформатика'}),
                Teacher('Олена', 'Гриценко', 42, 'o.grytsenko@example.com', {'Біологія'})]

    schedule = create_schedule(subjects, teachers)

    if schedule:
        print("Розклад занять:")
        for teacher in schedule:
            print(f"{teacher.first_name} {teacher.last_name}, {teacher.age} років, email: {teacher.email}")
            print(f"   Викладає предмети: {', '.join(teacher.assigned_subjects)}\n")
    else:
        print("Неможливо покрити всі предмети наявними викладачами.")
