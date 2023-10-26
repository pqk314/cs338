from hashlib import sha256
import random

# Part 1

# Used later
words = [line.strip().lower() for line in open('words.txt')]

# Not used later
# hashes = [line.strip() for line in open('passwords1.txt')]
# passhashes = [hash[hash.index(":")+1 : hash.find(":", hash.find(":")+1)] for hash in hashes]
# wordsdict = {}
# answer = []

# for word in words:
#     encodedWord = sha256(word.encode('utf-8')).hexdigest()
#     wordsdict[encodedWord] = word

# for x in range(len(passhashes)):
#     if(wordsdict[passhashes[x]] != None):
#         # Check if jondich:marmot is correct
#         # if(wordsdict[passhashes[x]] == "marmot"):
#         #     print(hashes[x][0 : hashes[x].index(":")]+ ":"+ wordsdict[passhashes[x]])
#         answer.append(hashes[x][0 : hashes[x].index(":")]+ ":"+ wordsdict[passhashes[x]])

# # Prints my answers for the first problem to cracked1.txt
# with open("cracked1.txt", "w") as text_file:
#     for catch in answer:
#         text_file.write(catch)
#         text_file.write("\n")

# Checks number of hashes computed
# print(len(wordsdict))




# Part 2

# # words = list of all english words
# hashes2 = [line.strip() for line in open('passwords2.txt')]
# passhashes2 = [hash[hash.index(":")+1 : hash.find(":", hash.find(":")+1)] for hash in hashes2]
# wordsdict2 = {}
# answer2 = []
# doublewords = []

# for x in range(30000):
#     y = x + random.randint(0, 267516-30001)
#     for a in range(30000):
#         b = a + random.randint(0, 267516-30001)
#         doublewords.append(words[y]+words[b])


# for word in doublewords:
#     encodedWord = sha256(word.encode('utf-8')).hexdigest()
#     wordsdict2[encodedWord] = word

# for x in range(len(passhashes2)):
#     if(passhashes2[x] in wordsdict2):
#         answer2.append(hashes2[x][0 : hashes2[x].index(":")]+ ":"+ wordsdict2[passhashes2[x]])
# for x in answer2:
#     print(x)

# # Prints my answers for the second problem to cracked2.txt
# with open("cracked2.txt", "w") as text_file:
#     for catch in answer2:
#         text_file.write(catch)
#         text_file.write("\n")


# Part 3

# # words = list of all words in english
hashes3 = [line.strip() for line in open('passwords3.txt')]
passhashes3 = [hash[hash.index(":")+1+3+9 : hash.find(":", hash.find(":")+1)] for hash in hashes3]
wordsdict3 = {}
answer3 = []
saltedwords = []
salts = [hash[hash.index(":")+1+3 : hash.index(":")+1+3+8] for hash in hashes3]

for word in words:
    # # set the size of the salts range to choose how many passwords to crack
    for salt in salts[0:100]:
        saltedwords.append(salt+word)


for word in saltedwords:
    encodedWord = sha256(word.encode('utf-8')).hexdigest()
    wordsdict3[encodedWord] = word[8:]


for x in range(len(passhashes3)):
    if(passhashes3[x] in wordsdict3):
        answer3.append(hashes3[x][0 : hashes3[x].index(":")]+ ":"+ wordsdict3[passhashes3[x]])

for x in answer3:
    print(x)

# # Prints my answers for the third problem to cracked3.txt
# with open("cracked3.txt", "w") as text_file:
#     for catch in answer3:
#         text_file.write(catch)
#         text_file.write("\n")
