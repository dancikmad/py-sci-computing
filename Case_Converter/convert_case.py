def convert_to_snake_case(pascal_or_camel_cased_string):
    snake_cased_char_list = [
        "_" + char.lower() if char.isupper() else char
        for char in pascal_or_camel_cased_string
    ]


    return "".join(snake_cased_char_list).strip("_")


def main():
    print(convert_to_snake_case("IAmPascalCasedString"))


if __name__ == "__main__":
    main()

# Output:
# >>> i_am_a_pascal_cased_string
