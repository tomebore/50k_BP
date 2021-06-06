# print("salam")
# print("This is my first program")

# print("*")
# print("**")
# print("***")
# print("****")
# print("*****")

# print("1 00 100 1000 10000")


# # Lesson 3
# a = int(input())

# if a % 2==0 and a % 5 ==0:
#     print("its dividing") 
# else:
#     print("no")

# # lesson 4
# b = input("what lesson?")

# if b=="math":
#     print("be programmer")
# elif b=="physic":
#     print("Советую вам подумать о робототехнике")
# elif b=="chem":
#     print(""" “Из Вас может выйти отличный врач,
#     но стать программистом можно намного быстрее""")
# elif b=="sports":
#     print("""Стать профессиональным спортсменом трудно.
#     Как насчет IT? Это намного легче""")
# else:
#     print("""Даже не знаю, что Вам предложить. 
#              Вы знаете, что при желании и упорстве,
#             каждый может работать в IT-сфере? Подумайте над этим :)""")

#------
login = input("login:")

if login=="guest":
    print("Welcome")
elif login=="user":
    id_name = input("name:")
    print("welcome" +""+ id_name)
elif login=="manager":
    password = input("insert a pasword:")
    if password=="manager123":
        print("welcome Boss")
    else:
        print("error! You are not boss")
else:
    print("There no such login")

# lesson5
