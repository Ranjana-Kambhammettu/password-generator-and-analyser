from bs4 import BeautifulSoup
import requests
import pandas as pd
# Scraping Website 1
url1 = "https://en.wikipedia.org/wiki/Wikipedia:10,000_most_common_passwords"
webdata  = requests.get(url1).text
soup = BeautifulSoup(webdata,"html.parser")
cols = soup.find_all('div',class_='div-col')
data = {"Common Passwords":[]}
for col in cols:
    passwds=col.find_all('li')
    for passwd in passwds:
        if passwd.text.strip()!='':
            data["Common Passwords"].append(passwd.text)

#Scraping Website 2
url2 = 'https://github.com/OWASP/passfault/blob/master/wordlists/wordlists/10k-worst-passwords.txt'
webdata  = requests.get(url2).text
soup = BeautifulSoup(webdata,"html.parser")
passwds = soup.find_all('td',class_="blob-code blob-code-inner js-file-line")
for passwd in passwds:
    data["Common Passwords"].append(passwd.text)
    pass


#Scraping Website 3
url3='https://github.com/danielmiessler/SecLists/blob/master/Passwords/Common-Credentials/10-million-password-list-top-100000.txt'
webdata = requests.get(url3).text
soup = BeautifulSoup(webdata,"html.parser")
passwds = soup.find_all('td',class_='blob-code blob-code-inner js-file-line')
for passwd in passwds:
    data["Common Passwords"].append(passwd.text)
    

#Writing all unique passwrods into a csv file    
common_password = pd.DataFrame.from_dict(data)
common_password = common_password.drop_duplicates(subset='Common Passwords', keep="first")
common_password = common_password.reset_index(drop=True)



def w1(s):
    c=0
    for char in s:
        if char.isalpha():
            c+=1
    return c*4
def w2(s):
    c=0
    for char in s:
        if char.islower():
            c+=1
    return (len(s)-c)*2
def w3(s):
    c=0
    for char in s:
        if char.isupper():
            c+=1
    return (len(s)-c)*2
def w4(s):
    c=0
    for char in s:
        if char.isdigit():
            c+=1
    return c*4
def w5(s):
    c=0
    for char in s:
        if not (char.isalpha() or char.isdigit()):
            c+=1
    return c*6
def w6(s):
    c=0
    for char in s[1:-1]:
        if char.isdigit():
            c+=1
        elif char.isalpha():
            pass
        else:
            c+=1
    return c*2
def w7(s):
    if s.isalpha():
        return -len(s)
    else:
        return 0
def w8(s):
    if s.isdigit():
        return -len(s)
    else:
        return 0
def w9(s):
    d,c={},0
    for char in s:
        if char not in d:
            d[char]=1
        else:
            d[char]+=1
    for char in d:
        if d[char]>1:
            c+=1
    return -(c*(c-1))

def w10(s):
    n = 0
    for i in range(0,len(s)):
        if s[i-1].islower()==s[i].islower()==True:
            n+=1
    return -(n*2)

def w11(s):
    n = 0
    for i in range(0,len(s)):
        if s[i-1].isupper()==s[i].isupper()==True:
            n+=1
    return -(n*2)

def w12(s):
    t=[]
    for i in range(ord('a'), ord('z')+1):
        t.append(chr(i))

    n = 0
    for j in range (0,len(s)):
        for g in range(0,len(t)):
            if s[j-1] == (t[g]) and s[j] == (t[g+1]):   
                n+=1
                
    return -(n*3)


# To find number of sequential digits
def w13(s):
    t=[]
    for i in range(0, 10):
        t.append(i)

    n = 0
    for j in range (0,len(s)-1):
        for g in range(0,len(t)):
            if((s[j]) == str(t[g]) and s[j+1] ==  str(t[g+1])):
                if int(s[j]) == (t[g]) and int(s[j+1]) == (t[g+1]):   
                    n+=1
                
    return -(n*3)

def w14(s):
    line1 = [1,2,3,4,5,6,7,8,9,0]
    line2 = ["q","w","e","r","t","y","u","i","o","p"]
    line3 = ["a","s","d","f","g","h","j","k","l"]
    line4 = ["z","x","c","v","b","n","m"]
    n = 0

    for j in range (0,len(s)-1):
            for g in range(0,len(line1)):
                if((s[j-2]) == str(line1[g-2]) and s[j-1] ==  str(line1[g-1]) and s[j] == str(line1[g])):   
                        n+=1
            for g in range(0,len(line2)):
                if((s[j-2]) == str(line2[g-2]) and s[-1] ==  str(line2[g-1]) and s[j] == str(line2[g])):   
                        n+=1    
            for g in range(0,len(line3)):
                if((s[j-2]) == str(line3[g-2]) and s[j-1] ==  str(line3[g-1]) and s[j] == str(line3[g])):   
                        n+=1
            for g in range(0,len(line4)):
                if((s[j-2]) == str(line4[g-2]) and s[j-1] ==  str(line4[g-1]) and s[j] == str(line4[g])):   
                        n+=1
    return -(n*2)

#Mirror patterns , again here we consider it as a pattern only if it is 3 characters or more

def w14(s):

    seq = {}
    seqlen = 3
    for i in range(len(s) - seqlen + 1):
            sequence = s[i:i+seqlen]

            if sequence in seq:
                seq[sequence] += 1
            else:
                seq[sequence] = 1

    n = sum(1 for n in seq.nues() if n > 1)

    return -(n*2)



# Mirrored sequence
def w15(s):

    n = 0
    for i in range(len(s)-2):
            for j in range(i+2, len(s)):
                if s[i:j] == s[i:j][::-1]:
                    n += 1


    return -(n*3)

common_password["w1"]=common_password["Common Passwords"].apply(w1)
common_password["w2"]=common_password["Common Passwords"].apply(w2)
common_password["w3"]=common_password["Common Passwords"].apply(w3)
common_password["w4"]=common_password["Common Passwords"].apply(w4)
common_password["w5"]=common_password["Common Passwords"].apply(w5)
common_password["w6"]=common_password["Common Passwords"].apply(w6)
common_password["w7"]=common_password["Common Passwords"].apply(w7)
common_password["w8"]=common_password["Common Passwords"].apply(w8)
common_password["w9"]=common_password["Common Passwords"].apply(w9)
common_password["w10"]=common_password["Common Passwords"].apply(w10)
common_password["w11"]=common_password["Common Passwords"].apply(w11)
common_password["w12"]=common_password["Common Passwords"].apply(w12)
common_password["w13"]=common_password["Common Passwords"].apply(w13)
common_password["w14"]=common_password["Common Passwords"].apply(w14)
common_password["w15"]=common_password["Common Passwords"].apply(w15)


cols=["w1","w2","w3","w4","w5","w6","w7","w8","w9","w10","w11","w12","w13","w14","w15"]
common_password["score"]=common_password[cols].sum(axis=1)
common_password.to_csv('common_passwords.csv')
