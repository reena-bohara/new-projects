print ("BASIC CALCULATOR")
print ('-'*20)

user_choice1 = float(input("your first number :\n"))
user_choice2 = float(input("your second number :\n"))
operators = input("choose between these four operators:+,-,*,/ :\n")

if operators == '+':
    print(f"RESULTS:\n{user_choice1} {operators} {user_choice2} = {user_choice1+user_choice2:.3f}")
elif operators == '-':
    print(f"RESULTS:\n{user_choice1} {operators} {user_choice2} = {user_choice1-user_choice2:.3f}")
elif operators == '*':
    print(f"RESULTS:\n{user_choice1} {operators} {user_choice2} = {user_choice1*user_choice2:.3f}")
elif operators == '/':
    if user_choice2 == 0:
        print("ERROR")
    
    else :
        print(f"RESULTS:\n{user_choice1} {operators} {user_choice2} = {user_choice1/user_choice2:.3f}")    

