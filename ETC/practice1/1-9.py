salary = {'David':30000, 'John':50000, 'Andrew':45000, 'Rita':70000, 'Michale':10000}

for a in salary.keys():
    if salary[a] >= 50000:
        print(a + '\'s salary is', salary[a])
