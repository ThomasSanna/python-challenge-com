import urllib.request

url='http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='
newUrl = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345'

digits = '0123456789'

for p in range (400):
    response = urllib.request.urlopen(newUrl)
    html = response.read()
    html = str(html)
    print("non html : ", html,",  p = ", p)
    
    nothinIs = 'nothing is'
    
    if html == "b'Yes. Divide by two and keep going.'":
        nothing = int(nothing) // 2
        nothing = str(nothing)

    for i in range (len(html)):
        if html[i] in digits and nothinIs in html[:i]:
            nothing = html[i:-1]
            break
    newUrl = url + nothing
    
response = urllib.request.urlopen(newUrl)
html = response.read()
html = str(html)
print(html)