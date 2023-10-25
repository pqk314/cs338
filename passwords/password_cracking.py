from hashlib import sha256
words = [line.strip().lower() for line in open('words.txt')]
hashes = [line.strip() for line in open('passwords1.txt')]
passhashes = [hash[hash.index(":")+1 : hash.find(":", hash.find(":")+1)] for hash in hashes]

wordsdict = {}

for word in words:
    encodedWord = sha256(word.encode('utf-8')).hexdigest()
    wordsdict[encodedWord] = word


# Everthing workds until here, just need to look through
answer = []

for x in range(len(passhashes)):
    if(wordsdict[passhashes[x]] != None):
        # Check if jondich:marmot is correct
        # if(wordsdict[passhashes[x]] == "marmot"):
        #     print(hashes[x][0 : hashes[x].index(":")]+ ":"+ wordsdict[passhashes[x]])
        answer.append(hashes[x][0 : hashes[x].index(":")]+ ":"+ wordsdict[passhashes[x]])

with open("cracked1.txt", "w") as text_file:
    for catch in answer:
        text_file.write(catch)
        text_file.write("\n")


