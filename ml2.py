import csv
import json
from datetime import datetime

# Чтение данных сотрудников из файла CSV
def read_employees_from_csv(file_path):
    employees = []
    with open(file_path, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            row[3] = int(row[3]) if row[3].isdigit() else row[3]
            employees.append(row)
    return employees

# number of years worked
def years_worked(hire_date):
    hire_date = datetime.strptime(hire_date, "%d.%m.%Y")
    return (datetime.now() - hire_date).days // 365

# 1
def programmers_bonus(employees):
    for emp in employees[1:]:
        if 'программист' in emp[1].lower():
            bonus = emp[3] * 0.03
            print(f"Программист {emp[0]} получает бонус: {bonus:.2f} руб.")

# 2
def holiday_bonus(employees):
    for emp in employees[1:]:
        print(f"{emp[0]} получает бонус: 2000 руб. ко Дню 8 марта")
        if "ич" in emp[0].split()[-2]:
            print(f"{emp[0]} получает бонус: 2000 руб. ко Дню 23 февраля")

# 3
def salary_indexation(employees):
    for emp in employees[1:]:
        if years_worked(emp[2]) > 10:
            emp[3] = emp[3] * 1.07
        else:
            emp[3] = emp[3] * 1.05
        print(f"Новый оклад {emp[0]}: {emp[3]:.2f} руб.")

# 4
def vacation_list(employees):
    vacationers = []
    for emp in employees[1:]:
        if years_worked(emp[2]) > 0.5:
            vacationers.append(emp[0])
    return vacationers

# 5
def save_to_csv_json(employees):
    # CSV
    with open('updated_employees.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(employees)
    
    # JSON
    employee_data = []
    for emp in employees[1:]:
        employee_data.append({
            "ФИО": emp[0],
            "Должность": emp[1],
            "Дата найма": emp[2],
            "Оклад": emp[3]
        })
    
    with open('employees.json', 'w', encoding='utf-8') as json_file:
        json.dump(employee_data, json_file, ensure_ascii=False, indent=4)

#---
file_path = 'employees.csv'
employees = read_employees_from_csv(file_path)

programmers_bonus(employees)
holiday_bonus(employees)
salary_indexation(employees)
vacationers = vacation_list(employees)
print("Сотрудники, имеющие право на отпуск:", vacationers)
save_to_csv_json(employees)
