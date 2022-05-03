
# translate = {
#     "red": "rojo",
#     "blue": "aloz",
#     "green": "verdi", 
#     "white": "blanco"
# }

# alist = [

# ]

# def translate(color):
#     if color == "red":
#         return "rojo"
#     elif color == "blue":
#         return "aloz"
#     elif color == "green":
#         return "verdi"
#     elif color == "white":
#         return "blanco"

# print(translate("red"))


user = {
    "first_name": "Robert", 
    "last_name": "Smith", 
    "age": 19,
    "school":{
        "school_name": "Fresno"
    }
}

if "school" in user: 
    print("true")
else:
    print("false")



# print(user["school"]["school_name"])
# print(len(user["school"]))

# user_data = list(user)
# user_data = set(user)
# print(user_data)

# print(max(user))
# print(min(user))

dict = {
    "a": "A", 
    "b": "B", 
    "c": "C", 
}
dict2 = {
    "a": "A", 
    "d": "D", 
    "e": "E", 
}

# merged_dict = dict + dict2

# print(merged_dict)

def main():
    print("Main running..")
    d = {}
    print(d)

    d.update(dict2)
    print()