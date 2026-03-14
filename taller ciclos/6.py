
word = input("Ingrese una palabra: ")

for i in range(len(word)):
    if(word[i]=="a" or word[i]=="e" or word[i]=="i" or word[i]=="o" or word[i]=="u"):
        continue
    else:
        print (word[i])