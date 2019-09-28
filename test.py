from vigenere import kasiski, vigenere, frequency


def validate_message(string):
    alphabet = "ABCDEFGHIKLMNOPQRSTVXYZ "
    string = string.upper()
    result_string = ""
    for char in string:
        if char in alphabet:
            result_string += char
    return result_string


def plot_data_message_vary(key, messages):
    for message in messages:
        cypher_text = vigenere.vigenere(validate_message(message), key, 'e')
        key_len = kasiski.find_key_length(cyphertext=cypher_text)
        print(key_len)
        print(frequency.restore_key(cypher_text, key_len))


with open("cypher_text") as f:
    original_text = f.readlines()
    key = "VIGENE"
    messages = [original_text[0][:700]]
    plot_data_message_vary(key, messages)
