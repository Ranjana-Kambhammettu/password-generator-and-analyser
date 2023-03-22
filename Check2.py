special_chars = ['@','$','!','#','%','&','(',')','0','3','8','<','|']
punc = ['@','*','+','-',':','”','/','\\','~','?','[',']','{','}','$','!','#','%','&','(',')','_' ,'<','|']
alphabets = ['a','s','i','r','x','q','c','j','o','e','b','k','l']
numbername = ["zero","one","two","three","four","five","six","seven","eight","nine"]
number2 = ["0","1","2","3","4","5","6","7","8","9"]
c2s = {}
n2s = {}


for i in range(13):
  c2s[alphabets[i]]=special_chars[i]

for i in range(10):
   n2s[number2[i]]=numbername[i]

print(n2s)

   
s = "10R!dERSwA|pA&"

def numToSpecial(s):
   for num in s:
      if num in n2s:
         s=s.replace(num,n2s[num])
         break
   
   return s  


print(numToSpecial("$EEth#Am78<IRAn/"))
