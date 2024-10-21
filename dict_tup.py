def age_dictionary():
    d={}
    while True:
        person=input('Enter the name of the person:')
        if person=='':
            break
        age= input('enter age:')
        d[person]=age

    print('building dictionary os complete. Now enter name of the person and I will you his\her age')
    while True:
        name= input('Enter name of the person:')
        if name=='':
            break
        if name in d:
            print(f"Age of {name} is {d[name]}")
        else:
            print(f"I dont know the age of {name}")

age_dictionary()