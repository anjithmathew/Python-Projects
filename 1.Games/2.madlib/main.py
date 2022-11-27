
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
    ans = zip(input_user,list_input)
    str_ans = []
    for i in ans:
        str_ans.append(i)
    y = [list(x) for x in str_ans]
    z = []
    for x in y:
        z.append(" ".join(x))
    
    xxx ="  ".join(z)

    print(xxx)

x = user_input(data)

string_formating(input_user, x)
