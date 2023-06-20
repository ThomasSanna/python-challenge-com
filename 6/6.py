import zipfile, re

f = zipfile.ZipFile("channel.zip")

comments = []


numbers = 90052
path = "./txtfiles/"
url = '.txt'
nothing = 'nothing is'
digits = '1234567890'
newUrl = path + str(numbers) + url

for i in range (909):
    newUrl = path + str(numbers) + url
    comments.append(f.getinfo(str(numbers) + '.txt').comment.decode('utf-8'))
    string = open(newUrl).read()

    for i in range (len(string)):
        if (string[i] in digits) and (nothing in string[:i]) :
            numbers = int(string[i:-1] + string[-1])
            break
print(''.join(comments))