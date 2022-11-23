"""'value': ['Today, my fabulous camp group went to a(an) ', ' amusement park. It was a fun park with lots of cool ', ' 
and enjoyable play structures. When we got there, my kind counselor shouted loudly, "Everybody off the ', '." 
My counselor handed out yellow tickets, and we scurried in. I was so excited! I couldn\'t
figure out what exciting thing to do first. I saw a scary roller coaster I really liked so, I ', '  
ran over to get in the long line that had about ', ' people in it. when I finally got on the roller coaster I was ', '. 
In fact, I was so nervous my two knees were knocking together. This was the ', ' ride I had ever been on! In about two minutes
 I heard the crank and grinding of the gears. Thats when the ride began! When I got to the bottom, I was a little ', ' but I 
 was proud of myself. The rest of the day went ', '. It was a ', ' day at the fun park.', 0]"""


import requests
data = requests.get("https://madlibz.herokuapp.com/api/random").json()

input_user = data['value'][:-1]
print(input_user)


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
    index = input_user.index (",")
    print(index)
    # print(list_to_string)
    # for i in list_input:
    #     print(i)

    #     list_to_string.replace(" ", i)

    print(list_to_string)


x = user_input(data)

string_formating(input_user, x)
