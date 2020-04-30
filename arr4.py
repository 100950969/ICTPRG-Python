def main():


    name = input('Full Name: ')
    name_list = name.split()

    first = name_list[0][0]
    second = name_list[1][0]
    last = name_list[2][0]

    print("Intials: ", first.upper(), second.upper(), last.upper()) 


main()