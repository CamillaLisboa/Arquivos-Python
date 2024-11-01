from random import randint, shuffle

def shuffleWord(word):
    word_list = list(word)
    shuffle(word_list)
    word = ''.join(word_list)
    return word
    
def getWord(words):
    word = words[randint(0,len(words)-1)]
    shufword = shuffleWord(word)
    return word, shufword

def verifyEntry(entrada, word):
    if entrada == word:
        return True
    return False

words =  ['amor', 'capacete', 'abacaxi', 'agulha']
cont = 0

word, shufword = getWord(words)
print(shufword)

while cont <= 6:
    entrada = input()
    tentativa = verifyEntry(entrada, word)
    if tentativa:
        print("Parabéns, você acertou!")
        break
    cont+=1
    print(f'Resposta errada. Tente novamente.... {6-cont} tentativas')
    if cont == 6:    
        print(f"Você esgotou suas sentativas... T^T   Resposta Correta: {word}")


    
    
