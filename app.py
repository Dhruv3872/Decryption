
# The task is to create a function which can take a text input file,
# and return a decrypted message by processing the file according to
# the Decryption key as follows:
# The file will contain multiple lines in this format:
# '<integer><space><word>><\n>' without the quotes.
# The Decryption key is as follows:
# 1. Sort each pair of 'integer - word' based on the ascending order
# of the integers.
# 2. Make a pyramid structure of the integer values using the
# sorted pairs like this:
# 1
# 2 3
# 4 5 6
# and so on.
# The corresponding words against the last integers in this pyramid
# represent the words which are supposed to be present in the encrypted
# message in order.
# 3. Return the string containing these words in order without quotes
# or full-stop or any leading/trailing spaces.
# Then the code runs a print statement on the function to print
# the message on the console.
# For the sake of simplicity, the text file to be consumed as input
# has been put in the root directory of the project.

def decode(message_file):
    file_at_hand = open(message_file)
    data = file_at_hand.read()
    data_dictionary = dict()
    string_key = ""
    value = ""
    is_key_whole = False
    iteration = 0
    for character in data:
        iteration += 1
        if not is_key_whole:
            if character != ' ':
                string_key += character
            else:
                is_key_whole = True
                continue
        else:
            if character != '\n':
                value += character
                if iteration == len(data):
                    key = int(string_key)
                    data_dictionary[key] = value
                    string_key = ""
                    value = ""
                    is_key_whole = False
            else:
                key = int(string_key)
                data_dictionary[key] = value
                string_key = ""
                value = ""
                is_key_whole = False
    data_keys = list(data_dictionary.keys())
    data_keys.sort()
    sorted_data = {i: data_dictionary[i] for i in data_keys}
    message_dictionary = dict()
    step_size = 1
    current_key = 1
    while current_key < len(sorted_data):
        message_dictionary[current_key] = sorted_data[current_key]
        step_size += 1
        current_key += step_size
    message = ""
    for key in message_dictionary:
        message += message_dictionary[key] + " "
    message.strip()
    return message


encryptedFile = "coding_qual_input.txt"
print(decode(encryptedFile))