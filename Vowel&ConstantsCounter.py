program_is_on = True
while program_is_on:
    user_input = input("Enter a string:")
    if user_input == "":
        print("Enter a non-empty string")
    else:
        vowels_count = 0
        constants_count = 0
        constants = ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Y', 'Z',
           'b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
        vowels = ["A", "a", "i", "I", "o", "O", "u", "U", "e", "E"]
        for letter in user_input:
            if letter in vowels:
                constants_count += 1
                vowels_count += 1
        print("The Number of Vowels in", user_input, "is", vowels_count,"and The number of constants is",constants_count)
        program_is_on = False