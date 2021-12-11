from textblob import TextBlob

blob = TextBlob("Я люблю пельмени с сметанкой!")
print(blob.translate(to="ai"))

# blob = TextBlob("I love dumplings with sour cream!")
# print(blob.translate(to="ro"))