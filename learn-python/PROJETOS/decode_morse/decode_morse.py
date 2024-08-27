import os
import datetime
import pandas as pd

# Definindo o caminho do arquivo e o dicionário Morse
file_path = "decode_morse.csv"
dict_morse = {
    ".-": "A", "-...": "B", "-.-.": "C", "-..": "D", ".": "E", "..-.": "F",
    "--.": "G", "....": "H", "..": "I", ".---": "J", "-.-": "K", ".-..": "L",
    "--": "M", "-.": "N", "---": "O", ".--.": "P", "--.-": "Q", ".-.": "R",
    "...": "S", "-": "T", "..-": "U", "...-": "V", ".--": "W", "-..-": "X",
    "-.--": "Y", "--..": "Z", "-----": "0", ".----": "1", "..---": "2",
    "...--": "3", "....-": "4", ".....": "5", "-....": "6", "--...": "7",
    "---..": "8", "----.": "9"
}

def decode_morse(msg):
    '''
    input : mensagem em código morse com as letras separadas por espaços e palavras separadas por dois espaços
    output : texto decodificado em português, com letras maiúsculas e palavras separadas corretamente
    '''
    msg_claro = []
    words = msg.split("  ") 
    for word in words:
        letters = word.split(" ")  
        decoded_word = "".join([dict_morse.get(letter, '') for letter in letters])
        msg_claro.append(decoded_word)
    return " ".join(msg_claro)  

def save_clear_msg_csv_hdr(msg_claro):
    '''
    input : mensagem em texto claro
    output : texto decodificado salvo em arquivo CSV com timestamp
    '''
    now = datetime.datetime.now()
    df = pd.DataFrame([[msg_claro, now]], columns=["mensagem", "datetime"])
    hdr = not os.path.exists(file_path)
    df.to_csv(file_path, mode="a", index=False, header=hdr)

if __name__ == "__main__":
    for _ in range(3):  
        morse_input = input("Digite a frase em código Morse: ")
        msg_claro = decode_morse(morse_input)
        save_clear_msg_csv_hdr(msg_claro)
        print(f"Mensagem decodificada: {msg_claro}")

        continuar = input("Deseja decodificar outra frase? (s/n): ").strip().lower()
        if continuar != 's':
            break
