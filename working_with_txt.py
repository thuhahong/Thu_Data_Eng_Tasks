# opening and printing file order.txt
def open_and_print_file(file):
    try:
        opened_file = open(file, "r")
        file_line_list = opened_file.readlines()

        print(file_line_list)

        for x in file_line_list:
            print(x)

        opened_file.close()

    except FileNotFoundError as msg:
        print("There is an error! Panic!")
        print(msg)

    finally:
        print("Execution complete")


open_and_print_file("order.txt")


# adding content to file order.txt
def writing_to_file(file, order_item):
    try:
        with open(file, "w") as file:
            file.write(order_item)

    except FileNotFoundError:
        print("Not Found!")


writing_to_file("order.txt", "lemonade")
