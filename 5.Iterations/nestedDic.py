phone_num_dic = {
    'Marketing' : {
        'Robert': '111-111-1111',
        'Shawn' : '222-222-2222',
        'Bryce': '333-333-3333'
    },
    'It' : {
        'Lisa': '444-444-4444',
        'Jason':'555-555-5555'
    }
}

# Get All departments in phone_num_dic
department = []
for dep , emp in phone_num_dic.items():
    print(dep)
    department.append(dep)

print(f"All department is dictionary is {department}")

# Get All employee in phone_num_dic
employee = []
for dep, emp in phone_num_dic.items():
    #print(emp.items())
    for name, phone in emp.items():
        employee.append(name)
print(f"All Employee is dictionary is {employee}")


''' Using a list comprehension, get all employee's Name '''
employees = [list(emp.keys()) for dep, emp in phone_num_dic.items()]

print(employees) #[['Robert', 'Shawn', 'Bryce'], ['Lisa', 'Jason']]

''' for employee in employees:
    for e in employee:
        print(e) '''
# Flatten to remove list of lists and convert to a single list
employee = [employee for employee in employees for employee in employee] 
print(employee) 


'''Using a list comprehension & intertools chain, get all phone number '''
from itertools import chain
phonenumbers = [list(emp.values()) for dep, emp in phone_num_dic.items()]
print(phonenumbers) # [['111-111-1111', '222-222-2222', '333-333-3333'], ['444-444-4444', '555-555-5555']]

phoneNumbers =list(chain.from_iterable([list(emp.values()) for dep, emp in phone_num_dic.items()]))
print(phoneNumbers) #['111-111-1111', '222-222-2222', '333-333-3333', '444-444-4444', '555-555-5555']

 