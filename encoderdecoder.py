alp = ['a','b','c','d','e','f','g','h','i','j','k', 'l','m', 'n', 'o', 'p', 'q','r','s','t','u','v','w','x','y','z']

text2=[]
text = input("Enter the text to code: ")
key=int(input("Enter a key number: "))
for i in text:
    ind= alp.index(i)
    ind= (ind+key)%26
    text2.append(alp[ind])
print("Encrypted:","".join(text2))
 
text3=[]
for i in text2:
    ind= alp.index(i)
    ind= (ind-key)%26
    text3.append(alp[ind])
print("Decrypted: ",''.join(text3))
    