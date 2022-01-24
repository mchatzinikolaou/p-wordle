def preprocess():
    wordlist=[]

    with open(r"C:\Users\Michalis\PycharmProjects\wordle\words.txt", "r") as initFile,open(r"C:\Users\Michalis\PycharmProjects\wordle\5words.txt", "w") as destFile:
        line=initFile.readline()
        lineNum=1
        while(line !=""):
            if(len(line)-1==5):
                wordlist.append(line)
            line=initFile.readline()
            lineNum+=1
        initFile.close()
        destFile.writelines(wordlist)
        destFile.close()


def generateWord():
    import random
    wordlist=readList()

    return random.choice(wordlist)

def readList():
    wordlist = []
    with open(r"C:\Users\Michalis\PycharmProjects\wordle\5words.txt", "r") as wordFile:
        line = wordFile.readline()
        if (line == ""):
            return None
        while (line != ""):
            line = wordFile.readline()
            wordlist.append(line[:-1])
        wordFile.close()
    return wordlist

wordlist=readList()
def guess(currentAttemp,maxAttempts,secretWord,wordlist):
    while(currentAttemp<maxAttempts):
        word=input("Enter word guess:")
        while(len(word)!=5 or word.upper() not in wordlist):
            print("Wrong input, try again:")
            word = input("Enter word guess:")
        currentAttemp+=1
        notify="_____"
        for index in range(len(secretWord)):
            if(secretWord[index]==word[index].upper()):
                new = list(notify)
                new[index] = word[index].upper()
                notify=''.join(new)
            elif(word[index].upper() in secretWord):
                new = list(notify)
                new[index] = word[index].lower()
                notify = ''.join(new)
            else:
                new = list(notify)
                new[index] = '_'
                notify = ''.join(new)

        print(notify)
        if(word.upper()==secretWord):
            print("Congratulations, you found it in",currentAttemp,"attempt!"if currentAttemp==1 else "attempts!")
            return

secretWord=generateWord()
print(secretWord)

maxAttempts=10


guess(0,5,secretWord,wordlist)

