user_name = input("Entre you name to store in file or entre to proceed: ")

if user_name:
    with open("name.txt", "a") as file:
        file.write(user_name + '\n')

show_info = input("Entre y/n: ") 

try:
    with open("name.txt", "r") as file:
        content = file.readlines()
except Exception as e:
    print(e, type(e))

else:
    for line in content:
        print(f'{line.rstrip()}')
