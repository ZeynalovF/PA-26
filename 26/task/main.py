synonyms = {"quick": "fast", "small": "little", "happy": "glad"}

word = input("Enter a word: ")

if word in synonyms.keys():
    print(synonyms[word])
else:
    print("Word not found")