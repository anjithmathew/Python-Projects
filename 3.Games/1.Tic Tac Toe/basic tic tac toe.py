tic = [[1,1,1],[1,1,1],[1,1,1]]
for i in tic:
    print(i)

user_input =input("Enter where do you want to input")
print(user_input)

vertical = int(user_input[0]) -1

horizonal = int(user_input[1]) -1

tic[vertical][horizonal] = "x"

for i in tic:
    print(i)

