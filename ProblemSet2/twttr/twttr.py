def main():
    twitter = input("Input: ")

    twttr = remove_vowels(twitter)

    print("Output: ", twttr)


def remove_vowels(s):
    vowels = ""
    for c in s:
        if isvowel(c):
            s = s.replace(c, "")
    return s


# check for vowels
def isvowel(c):
    match c:
        case 'A' | 'a':
            return True
        case 'E' | 'e':
            return True
        case 'I' | 'i':
            return True
        case 'O' | 'o':
            return True
        case 'U' | 'u':
            return True
        case _:
            return False


# call main
main()
