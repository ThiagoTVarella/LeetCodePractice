def valid_abbr(word: str, abbr: str) -> bool:
    # Define two pointers
    word_pointer = 0
    abbr_pointer = 0

    # Run through pointers
    while word_pointer < len(word):
        # Read relevant characters
        word_ch = word[word_pointer]
        abbr_ch = abbr[abbr_pointer]

        # Check if characters are equal
        if word_ch == abbr_ch:
            word_pointer += 1
            abbr_pointer += 1

        else:
            # If not number, end
            if not abbr_ch.isdigit():
                return False

            # Read number from string
            number = ''
            while abbr_ch.isdigit():
                number += abbr_ch
                abbr_pointer += 1
                # Read new character from abbreviation, otherwise break
                if abbr_pointer < len(abbr):
                    abbr_ch = abbr[abbr_pointer]
                else:
                    break
            # If number started with 0
            if number[0] == '0':
                return False
            # Add number to word pointer
            else:
                number = int(number)
                word_pointer += number
    if word_pointer > len(word):
        return False

    return True

print(valid_abbr('apple','a2e'))