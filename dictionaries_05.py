message = input("> ")
words = message.split(' ')
emojis = {
    ":)": "😊",
    ":(": "😞"
}
output = " "
for word in words:
    output += emojis.get(word, word) + " "
print(output)   # prints emoji if available otherwise print same word
