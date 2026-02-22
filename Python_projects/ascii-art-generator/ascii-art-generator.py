from art import text2art


def main():
    user_input = input("Enter text: ")

    if user_input.strip():
        ascii_art = text2art(user_input)
        print(ascii_art)
    else:
        print("Error: Input is empty.")


if __name__ == "__main__":
    main()
