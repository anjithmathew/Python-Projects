
import requests
data = requests.get("https://madlibz.herokuapp.com/api/random").json()

input_user = data['value'][:-1]

# function to input user data and return it


def user_input(data):
    """ User input """

    print("*** Your story is ", data['title'], "So Input Crazy *** ")
    # list is used because dictionary is not viable for this task
    list_input = []
    for i in data['blanks']:
        list_input.append(input(f"Enter a {i} = "))
    return list_input


def string_formating(input_user, list_input):
    for i in range(len(list_input)):
        for i in range(1,len(input_user),3):
            pos = 1
            input_user.insert(i+pos,list_input[i])
            pos += i
    print(input_user)




x = user_input(data)

string_formating(input_user, x)
