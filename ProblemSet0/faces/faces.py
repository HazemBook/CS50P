def main():
    # str input with emoticon
    emoticon = input()
    emoticonTOemoji(emoticon)


def emoticonTOemoji(convert):
    # assign converted emoticon to emoji
    emoji = convert.replace(':)', '🙂').replace(':(', '🙁')
    
    # str output with emoji
    print(emoji)


# call main
main()