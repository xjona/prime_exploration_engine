textdoc = open("My_favourite_Primes.txt","w+")

def PrimeGenerator(many):
    textdoc.write("Primenumbers under " + str(many) + "\n")
    prim =[2]
    for i in range(2,many-2):
        temp = True
        for j in prim:
            if i%j == 0:
                temp = False
        if temp == True:
            prim.append(i)
    print(prim)

    for p in prim:
        textdoc.write("No." + str(prim.index(p)+1) + "   " + str(p) + "\n")

PrimeGenerator(100000000)

textdoc.close()
