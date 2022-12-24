s = input()

hg = {'a':'aespa', 'b':'baekjoon', 'c':'cau', 'd':'debug', 'e':'edge', 'f':'firefox', 'g':'golang', 'h':'haegang', 'i':'iu', 'j':'java', 'k':'kotlin', 'l':'lol', 'm':'mips', 'n':'null', 'o':'os','p':'python','q':'query','r':'roka','s':'solvedac','t':'tod','u':'unix','v':'virus','w':'whale','x':'xcode','y':'yahoo','z':'zebra'}

sl = len(s)
index = 0
result = []
while index < sl:
  x = s[index]
  xl = len(hg[x])
  if hg[x] == s[index:index+xl]:
    index += xl
    result.append(x)
  else:
    print("ERROR!")
    exit(0)

print("It's HG!")
for w in result:
  print(w, end='')
