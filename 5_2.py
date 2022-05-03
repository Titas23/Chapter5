# Afghanistan,Asia,31.8,251772
# Albania,Europe,3.0,11100
# Algeria,Africa,38.3,919595


def main():

    continent = input("Enter the name of a continent: ")
    continent = continent.title()
    if continent != "Antartica":
        infile = open("UN.txt", 'r')
        found = False
        for line in infile:
            data = line.split(',')
            if data[1] == continent:
                print(data[0])
                found = True
            print("Found: ",found)
        else:
            print("There are no countries in Antartica.")

main()
