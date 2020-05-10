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
            print("Please wait....Searching...")
    if flag==0:
        print("================================================")
        print("Password not found, try another algo or wordlist")
        print("================================================")

# SHA1
def fun_sha1():
    try:
        pass_file = open(word_list,"r")
    except:
        print("File Not Found")
        quit()

    flag=0
    counter=0
    print("Running SHA-1")
    print("=================")
    Lines=pass_file.readlines()
    for word in Lines:
        enc_word=word.encode('utf-8')
        digest=hashlib.sha1(enc_word.strip()).hexdigest()

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
            print("Please wait....Searching...")
    if flag==0:
        print("================================================")
        print("Password not found, try another algo or wordlist")
        print("================================================")

# SHA 2 Algorithms

# SHA2-224
def fun_sha224():
    try:
        pass_file = open(word_list,"r")
    except:
        print("File Not Found")
        quit()

    flag=0
    counter=0
    print("Running SHA2-224")
    print("=================")
    Lines=pass_file.readlines()
    for word in Lines:
        enc_word=word.encode('utf-8')
        digest=hashlib.sha224(enc_word.strip()).hexdigest()

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
            print("Please wait....Searching...")
    if flag==0:
        print("================================================")
        print("Password not found, try another algo or wordlist")
        print("================================================")

# SHA2-256
def fun_sha256():
    try:
        pass_file = open(word_list,"r")
    except:
        print("File Not Found")
        quit()

    flag=0
    counter=0
    print("Running SHA2-256")
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
            print("Passwords Checked: "+str(counter))
            flag=1
            break

        if flag == 0:
            print("Please wait....Searching...")
    if flag==0:
        print("================================================")
        print("Password not found, try another algo or wordlist")
        print("================================================")

# SHA2-384
def fun_sha384():
    try:
        pass_file = open(word_list,"r")
    except:
        print("File Not Found")
        quit()

    flag=0
    counter=0
    print("Running SHA2-384")
    print("=================")
    Lines=pass_file.readlines()
    for word in Lines:
        enc_word=word.encode('utf-8')
        digest=hashlib.sha384(enc_word.strip()).hexdigest()

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
            print("Please wait....Searching...")
    if flag==0:
        print("================================================")
        print("Password not found, try another algo or wordlist")
        print("================================================")

# SHA2-512
def fun_sha512():
    try:
        pass_file = open(word_list,"r")
    except:
        print("File Not Found")
        quit()

    flag=0
    counter=0
    print("Running SHA2-512")
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
            print("Passwords Checked: "+str(counter))
            flag=1
            break

        if flag == 0:
            print("Please wait....Searching...")
    if flag==0:
        print("================================================")
        print("Password not found, try another algo or wordlist")
        print("================================================")

#  SHA 3 Algorithms

# SHA3-224
def fun_sha3_224():
    try:
        pass_file = open(word_list,"r")
    except:
        print("File Not Found")
        quit()

    flag=0
    counter=0
    print("Running SHA3-224")
    print("=================")
    Lines=pass_file.readlines()
    for word in Lines:
        enc_word=word.encode('utf-8')
        digest=hashlib.sha3_224(enc_word.strip()).hexdigest()

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
            print("Please wait....Searching...")
    if flag==0:
        print("================================================")
        print("Password not found, try another algo or wordlist")
        print("================================================")

# SHA3-256
def fun_sha3_256():
    try:
        pass_file = open(word_list,"r")
    except:
        print("File Not Found")
        quit()

    flag=0
    counter=0
    print("Running SHA3-256")
    print("=================")
    Lines=pass_file.readlines()
    for word in Lines:
        enc_word=word.encode('utf-8')
        digest=hashlib.sha3_256(enc_word.strip()).hexdigest()

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
            print("Please wait....Searching...")
    if flag==0:
        print("================================================")
        print("Password not found, try another algo or wordlist")
        print("================================================")

# SHA3-384
def fun_sha3_384():
    try:
        pass_file = open(word_list,"r")
    except:
        print("File Not Found")
        quit()

    flag=0
    counter=0
    print("Running SHA3-384")
    print("=================")
    Lines=pass_file.readlines()
    for word in Lines:
        enc_word=word.encode('utf-8')
        digest=hashlib.sha3_384(enc_word.strip()).hexdigest()

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
            print("Please wait....Searching...")
    if flag==0:
        print("================================================")
        print("Password not found, try another algo or wordlist")
        print("================================================")

# SHA3-512
def fun_sha3_512():
    try:
        pass_file = open(word_list,"r")
    except:
        print("File Not Found")
        quit()

    flag=0
    counter=0
    print("Running SHA3-512")
    print("=================")
    Lines=pass_file.readlines()
    for word in Lines:
        enc_word=word.encode('utf-8')
        digest=hashlib.sha3_512(enc_word.strip()).hexdigest()

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
            print("Please wait....Searching...")
    if flag==0:
        print("================================================")
        print("Password not found, try another algo or wordlist")
        print("================================================")

# Driver Code
print("=============================")
print("========||| iPassU |||========")
print("A Hash Based password Cracker")
print("=============================")
pass_hash = input("Enter The hash: ")
know=input("Do you know the Hashing Algorithm used ??\n\tY\tN\n: ")
print("=============================")
word_list = input("Enter the name of the wordlist: ")
print("=============================")
if know =='Y'or know =='y':
    print("Select the Algotithm used : ")
    choice=int(input("[0]: MD5\n[1]: SHA-1\n[2]: SHA-2\n[3]: SHA-3\nEnter Your Choice: "))
    print("=============================")
    if choice==0:
        fun_md5()
    elif choice==1:
        fun_sha1()
    elif choice==2:
        ch_sha2=int(input("[1]: SHA2-224\n[2]: SHA2-256\n[3]: SHA2-384\n[4]: SHA2-512\nEnter Your Choice: "))
        if ch_sha2==1:
            fun_sha224()
        elif ch_sha2==2:
            fun_sha256()
        elif ch_sha2==3:
            fun_sha384()
        elif ch_sha2==4:
            fun_sha512()
        else:
            print("=============================")
            print("Enter a Valid Choice!!")
            print("=============================")
    elif choice==3:
        ch_sha2=int(input("[1]: SHA3-224\n[2]: SHA3-256\n[3]: SHA3-384\n[4]: SHA3-512\nEnter Your Choice: "))
        if ch_sha2==1:
            fun_sha3_224()
        elif ch_sha2==2:
            fun_sha3_256()
        elif ch_sha2==3:
            fun_sha3_384()
        elif ch_sha2==4:
            fun_sha3_512()
        else:
            print("=============================")
            print("Enter a Valid Choice!!")
            print("=============================")

    else:
        print("=============================")
        print("Enter a Valid Choice!!")
        print("=============================")
        
else:
    print("=============================")
    print("Trying all avaliable algorithms: Please wait..")
    try:
        pass_file = open(word_list,"r")
    except:
        print("File Not Found")
        quit()
    flag=0
    counter=0
    print("=================")
    print("Please wait.. This will take some time")
    Lines=pass_file.readlines()
    for word in Lines:
        enc_word=word.encode('utf-8')
        # MD5
        digest_md5=hashlib.md5(enc_word.strip()).hexdigest()
        # SHA1
        digest_SHA1=hashlib.sha1(enc_word.strip()).hexdigest()
        # SHA2
        digest_SHA2_224=hashlib.sha224(enc_word.strip()).hexdigest()
        digest_SHA2_256=hashlib.sha256(enc_word.strip()).hexdigest()
        digest_SHA2_384=hashlib.sha384(enc_word.strip()).hexdigest()
        digest_SHA2_512=hashlib.sha512(enc_word.strip()).hexdigest()
        # SHA3
        digest_SHA3_224=hashlib.sha3_224(enc_word.strip()).hexdigest()
        digest_SHA3_256=hashlib.sha3_256(enc_word.strip()).hexdigest()
        digest_SHA3_384=hashlib.sha3_384(enc_word.strip()).hexdigest()
        digest_SHA3_512=hashlib.sha3_512(enc_word.strip()).hexdigest()

        counter+=1
        if digest_md5 == pass_hash or digest_SHA1==pass_hash or digest_SHA2_224==pass_hash or digest_SHA2_256==pass_hash or digest_SHA2_384==pass_hash or digest_SHA2_512==pass_hash or digest_SHA3_224== pass_hash or digest_SHA3_256== pass_hash or digest_SHA3_384==pass_hash or digest_SHA3_512==pass_hash:
            print("=================")
            print("Password Found")
            print(word)
            print("=================")
            print("Passwords Checked: "+str(counter))
            flag=1
            break
    if flag==0:
        print("================================================")
        print("Password not found, try another algo or wordlist")
        print("================================================")