def missingCharacters(s):
    # Create sets for all digits and lowercase English letters
    all_digits = set('0123456789')
    all_letters = set('abcdefghijklmnopqrstuvwxyz')

    # Convert the input string to lowercase and create a set from its characters
    s_set = set(s.lower())

    # Find the missing digits and characters
    missing_digits = sorted(all_digits - s_set)
    missing_letters = sorted(all_letters - s_set)

    # Combine the missing digits and letters in the desired order
    result = ''.join(missing_digits + missing_letters)

    return result

if __name__ == '__main__':
    s = '8hypotheticall024y6wxz'
    result = missingCharacters(s)
    print(result)