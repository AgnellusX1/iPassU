import hashlib
# Defining the Cracking Functions:

# MD5
def fun_md5():
    try:
        pass_file = open(word_list,"r")
    except:
        print("File Not Found")
        quit()

    flag=0
    counter=0
    print("Running MD5")
    print("=================")
    Lines=pass_file.readlines()
    for word in Lines:
        enc_word=word.encode('utf-8')
        digest=hashlib.md5(enc_word.strip()).hexdigest()

        counter+=1
        if digest == pass_hash:
            print("=================")
            print("Password Found")
            print(word)
            print("=================")
            print("Passwords Checked: "+str(counter))
            flag=1
            break

        if flag == 0:
            print("Searching...")
    if flag==0:
        print("================================================")
        print("Password not found, try another algo or wordlist")
        print("================================================")

# SHA256
def fun_sha256():
    try:
        pass_file = open(word_list,"r")
    except:
        print("File Not Found")
        quit()

    flag=0
    counter=0
    print("Running SHA-256")
    print("=================")
    Lines=pass_file.readlines()
    for word in Lines:
        enc_word=word.encode('utf-8')
        digest=hashlib.sha256(enc_word.strip()).hexdigest()

        counter+=1
        if digest == pass_hash:
            print("=================")
            print("Password Found")
            print(word)
            print("=================")
            print(counter)
            flag=1
            break

        if flag == 0:
            print("Searching...")
    if flag==0:
        print("================================================")
        print("Password not found, try another algo or wordlist")
        print("================================================")

# SHA512
def fun_sha512():
    try:
        pass_file = open(word_list,"r")
    except:
        print("File Not Found")
        quit()

    flag=0
    counter=0
    print("Running SHA-512")
    print("=================")
    Lines=pass_file.readlines()
    for word in Lines:
        enc_word=word.encode('utf-8')
        digest=hashlib.sha512(enc_word.strip()).hexdigest()

        counter+=1
        if digest == pass_hash:
            print("=================")
            print("Password Found")
            print(word)
            print("=================")
            print(counter)
            flag=1
            break

        if flag == 0:
            print("Searching...")
    if flag==0:
        print("================================================")
        print("Password not found, try another algo or wordlist")
        print("================================================")

print("=============================")
print("iPassU")
print("A Hash Based password Cracker")
print("=============================")
pass_hash = input("Enter The hash: ")
print("=============================")
word_list = input("Enter the name of the wordlist: ")
print("=============================")
print("Algorithm ()")
choice=int(input("[1]:MD5\n[2]:SHA256\n[3]:SHA512\nEnter Your Choice:"))
print("=============================")
if choice==1:
    fun_md5()
if choice==2:
    fun_sha256()
if choice==3:
    fun_sha512()