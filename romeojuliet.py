import requests

# this document right here requests the webpage in get, opens a new text file and writes that webpage onto that text file

res = requests.get('https://www.gutenberg.org/cache/epub/1112/pg1112.txt')

file = open('romeojuliet.txt', 'w')

for line in res.text:
    file.write(line)
