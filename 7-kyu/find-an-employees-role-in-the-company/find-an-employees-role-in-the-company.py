def find_employees_role(name):
    full_name = name.split(" ")
    f_name = full_name[0]
    l_name = full_name[1] if len(full_name) > 1 else ""
    
    for employee in employees:
        if employee['first_name'] == f_name and employee['last_name'] == l_name:
            return employee["role"]
    return "Does not work here!"