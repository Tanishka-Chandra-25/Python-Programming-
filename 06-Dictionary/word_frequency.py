sentence=input("Enter a sentence:")
freq={}
for word in sentence.split():
    if word in freq:
        freq[word]+=1
    else:
        freq[word]=1

print("Word frequency:")
for word, count in freq.items():
    print(word,":",count)
