tic = [[1,1,1],[1,1,1],[1,1,1]]
print("   0  1  2")

for count,row in enumerate(tic):
    print(count,row)

user_input =input("Enter where do you want to input")
print(user_input)

vertical = int(user_input[0]) -1

horizonal = int(user_input[1]) -1

tic[vertical][horizonal] = "x"

for i in tic:
    print(i)

