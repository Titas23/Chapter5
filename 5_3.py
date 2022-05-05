
# # translate = {
# #     "red": "rojo",
# #     "blue": "aloz",
# #     "green": "verdi",
# #     "white": "blanco"
# # }

# # alist = [

# # ]

# # def translate(color):
# #     if color == "red":
# #         return "rojo"
# #     elif color == "blue":
# #         return "aloz"
# #     elif color == "green":
# #         return "verdi"
# #     elif color == "white":
# #         return "blanco"

# # print(translate("red"))


# user = {
#     "first_name": "Robert",
#     "last_name": "Smith",
#     "age": 19,
#     "school":{
#         "school_name": "Fresno"
#     }
# }

# if "school" in user:
#     print("true")
# else:
#     print("false")


# # print(user["school"]["school_name"])
# # print(len(user["school"]))

# # user_data = list(user)
# # user_data = set(user)
# # print(user_data)

# # print(max(user))
# # print(min(user))

# original_dict = {}

# dict = {
#     "a": "A",
#     "b": "B",
#     "c": "C",
# }
# dict2 = {
#     "a": "A",
#     "d": "D",
#     "e": "E",
# }


# dict.update(dict2)
# print(dict)

# print(original_dict.update(dict2))

# def main():
#     print("Main running..")
#     d = {}
#     print(d)

#     d.update(dict2)
#     print()


def main():
    textese_dict = create_dictionary("Textese.txt")
    print("Enter a simple sintence in lowercase letters without")
    sentence = input("any punctuation: ")
    translate(sentence, textese_dict)


def create_dictionary(file_name):
    infile = open(file_name, 'r')
    text_list = [line.rstrip() for line in infile]
    infile.close()
    return dict([x.split(',') for x in text_list])


def translate(sentence, textese_dict):
    words = sentence.split()
    for word in words:
        print(textese_dict.get(word, word) + " ", end="")


main()
