def main():
    # camel case input
    camel = input("camelCase: ")
    
    # convert to snake case
    snake = snake_case(camel)

    # snake case output
    print("snake_case: ", snake)


def snake_case(camelCase):
    snake = ""
    #for each letter
    for letter in camelCase:
        # if in upper case
        if letter.isupper():
            # add '_' before and lower case the letter
            snake += '_' + letter.lower()
        else:
            snake += letter

    return snake


main()
