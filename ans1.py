def addemp(eid, nm, dp, sal):
    global data
    if (eid in data.keys()):
        print(f"Employee with ID {eid} already present\n")
    else:
        data[eid] = {'name': nm,
                   'dept': dp,
                   'sal': sal}
        print("Data succesfully added\n")

def upemp(eid, nm, dp, sal):
    global data
    if (eid not in data.keys()):
        print(f"Employee with ID {eid} not present\n")
    else:
        data[eid] = {'name': nm,
                   'dept': dp,
                   'sal': sal}
        print("Data succesfully updated\n")      

def searchemp(eid):
    global data
    if (eid not in data.keys()):
        print(f"Employee with ID {eid} not present\n")
    else:
        print(f"name: {data[eid]['name']}")
        print(f"department: {data[eid]['dept']}")
        print(f"salary: {data[eid]['sal']} \n")

def report():
    global data
    deptlist = set()
    for key, value in data.items():
        for field, details in value.items():
              if (field == 'dept'):
                  deptlist.add(details)
    #deptlist = list(deptlist)    
    
    for dp in deptlist:
        print("----" + dp + "----")
        for key, value in data.items():
              if (value['dept'] == dp):
                print(f"Id: {key}")
                print(f"Name: {value['name']}")
                print(f"Salary: {value['sal']}")
                print()
              
# Data
data = {1: {'name': 'Abhinav',
           'dept': 'Sales',
           'sal': 12_00_000},
        2: {'name': 'Shivam',
           'dept': 'IT',
           'sal': 1_00_000},
        3: {'name': 'Gaurav',
           'dept': 'Sales',
           'sal': 2_00_000},
}

# Main
while (1):
    opt = int(input("""Select option: 
    1. Add employee
    2. Update employee
    3. Search employee
    4. Delete employee
    5. Generate report
    6. Exit
    
    Enter option: """))
    
    if (opt > 6):
        print("Invalid!\n")
    elif (opt == 6):
        break
    elif (opt == 1):
        eid = int(input("id: "))
        nm = input("name: ")
        dp = input("dept: ")
        sal = int(input("salary: "))
        addemp(eid, nm, dp, sal)
    elif (opt == 2):
        eid = int(input("id: "))
        nm = input("name: ")
        dp = input("dept: ")
        sal = int(input("salary: "))
        upemp(eid, nm, dp, sal)
    elif (opt == 3):
        eid = int(input("id: "))
        searchemp(eid)
    elif (opt == 5):
        report()
    elif (opt == 4):
        eid = int(input("id: "))
        if (eid not in data.keys()):
            print(f"Employee with ID {eid} not present\n") 
        else:
            del data[eid]
            print("Successfully deleted employee\n")
