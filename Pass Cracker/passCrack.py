import hashlib

flag=0
counter=0

pass_hash = input("Enter The hash: ")

word_list = input("Enter the name of the wordlist: ")

try:
    pass_file = open(word_list,"r")
except:
    print("File Not Found")
    quit()

for word in pass_file:
    enc_word=word.encode('utf-8')
    digest=hashlib.md5(enc_word.strip()).hexdigest()

    counter+=1
    if digest == pass_hash:
        print("=================")
        print("Password Found")
        print(word)
        print(counter)
        flag=1
        break

if flag == 0:
    print("Password does not exist in the Word list")