def vigenere(string='', key='', t='e'):
    result_text = []
    adder = 0
    decryption = 1
    alphabet_len = 26
    if t == 'd':
        adder = alphabet_len
        decryption = -1
    for i in range(len(string)):
        if string[i] == " ":
            result_text.append(string[i])
            continue
        x = (ord(string[i]) +
             decryption * ord(key[i % len(key)]) + adder) % alphabet_len
        x += ord('A')
        result_text.append(chr(x))
    return "".join(result_text)

