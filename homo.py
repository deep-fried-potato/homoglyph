homodict= {'A':'Α','B':'В','C':'Ϲ','D':'Ɗ','E':'Ε','F':'Ϝ','G':'Ԍ','H':'Η','I':'І','J':'Ј','K':'K','L':'L','M':'Μ','N':'Ν','O':'О','P':'Р','Q':'Q','R':'Ꮢ','S':'Ѕ','T':'Т','U':'Ս','V':'Ѵ','W':'Ꮃ','X':'Х','Y':'Ү','Z':'Ζ','a':'а','b':'Ь','c':'с','d':'ԁ','e':'е','f':'f','g':'ɡ','h':'h','i':'і','j':'ј','k':'κ','l':'l','m':'m','n':'n','o':'о','p':'р','q':'q','r':'r','s':'ѕ','t':'t','u':'υ','v':'ν','w':'ѡ','x':'х','y':'у','z':'z'}

fileread = open("input.txt","r")
lines = fileread.readlines()
newstr = ""
for line in lines:
    for char in line:
        if char in homodict:
            newstr = newstr + homodict[char]
        else:
            newstr = newstr + char

filewrite = open("output.txt","w",encoding="utf-8")
filewrite.write(newstr)
print(newstr)
