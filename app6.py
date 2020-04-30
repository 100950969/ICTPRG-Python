def main():

    num1 = input("Enter a large number: ")
    num_list = [int(x) for x in str(num1)]
    res = str(num_list)[1:-1]
    res = res.replace(',', ' +')

    print('The sum of your number is:', res, "=", sum(num_list)) 

main()