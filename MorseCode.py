code_dict =  {'.-...': '&', '--..--': ',', '....-': '4', '.....': '5',
         '...---...': 'SOS', '-...': 'B', '-..-': 'X', '.-.': 'R',
         '.--': 'W', '..---': '2', '.-': 'A', '..': 'I', '..-.': 'F',
         '.': 'E', '.-..': 'L', '...': 'S', '..-': 'U', '..--..': '?',
         '.----': '1', '-.-': 'K', '-..': 'D', '-....': '6', '-...-': '=',
         '---': 'O', '.--.': 'P', '.-.-.-': '.', '--': 'M', '-.': 'N',
         '....': 'H', '.----.': "'", '...-': 'V', '--...': '7', '-.-.-.': ';',
         '-....-': '-', '..--.-': '_', '-.--.-': ')', '-.-.--': '!', '--.': 'G',
         '--.-': 'Q', '--..': 'Z', '-..-.': '/', '.-.-.': '+', '-.-.': 'C', '---...': ':',
         '-.--': 'Y', '-': 'T', '.--.-.': '@', '...-..-': '$', '.---': 'J', '-----': '0',
         '----.': '9', '.-..-.': '"', '-.--.': '(', '---..': '8', '...--': '3'
         }

def decodeMorse(morseCode):
    for item in morseCode.split(' '):
        return [code_dict[item] for item in morseCode.split(' ')]




print decodeMorse('-- .- .... -- ..- -..')
