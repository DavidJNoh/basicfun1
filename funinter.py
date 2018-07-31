# import random
# print(int(random.random()*100))
# print(int(random.random()*50))
# print(int(random.random()*50)+50)
# print(int(random.random()*450)+50)

# x = [ [5,2,3], [10,8,9] ] 
# students = [
#      {'first_name':  'Michael', 'last_name' : 'Jordan'},
#      {'first_name' : 'John', 'last_name' : 'Rosales'}
# ]
# sports_directory = {
#     'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
#     'soccer' : ['Messi', 'Ronaldo', 'Rooney']
# }
# z = [ {'x': 10, 'y': 20} ]

# # How would you change the value 10 in x to 15?  Once you're done x should then be [ [5,2,3], [15,8,9] ].  

# x[1][0]=15
# print(x)

# students[0]['last_name']='Bryant'
# print(students)

# sports_directory['basketball'][1]='Bryant'
# print(sports_directory)

# z[0]['y']=30
# print(z)

students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]
# def ite(students):
#     for val in students:
#         for key, value in val.items():
#             print(key,"-",value)

# ite(students))

# def stu(students):
#     for x in students:
#         for key, val in x.items():
#             if key=='first_name':
#                 print (val)

# stu(students)

dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}


def fuckyou(dojo):
    print(len(dojo["locations"]))
    for x in dojo:
        if x=='locations':
            print (x)
    for i in dojo['locations']:
        print (i)
    print(len(dojo["instructors"]))
    for x in dojo:
        if x=='instructors':
            print (x)
    for i in dojo['instructors']:
        print (i)

fuckyou(dojo)