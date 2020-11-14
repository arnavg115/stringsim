import numpy as np
import math as mt
def ngramgen(str1,lol):
  h=[]
  for n in range(len(str1)):
    substr = str1[n:n+lol]
    if len(substr)==lol:
      h.append(substr)
  return h
def compare(lst1,lst2):
  total = len(lst1)+len(lst2)
  match = 0
  for i in lst1:
    for g in lst2:
      if i ==g:
        match+=1
        total-=1
  ratio = match/total
  return ratio
def createarray(str1,str2):
    mat = np.zeros((len(str1)+1,len(str2)+1))
    for x in range(len(str1)):
        mat[x+1][0]=x+1
    for y in range(len(str2)):
        mat[0][y+1]=y+1
    return mat
def levdist(str1, str2, mat):
    for h in range(len(str1)):
        curval1 = str1[h:h+1]
        for j in range(len(str2)):
            diag = mat[h][j]
            left = mat[h+1][j]
            above = mat[h][j+1]
            curval2 = str2[j:j+1]
            if curval1 == curval2:
                mat[h+1][j+1]=diag
            else:
                min1 = min(diag,above,left)
                mat[h+1][j+1]=min1+1
    levd = mat[len(str1)][len(str2)]
    return levd
def lettonum(strw,n):
  vect = np.zeros((1,n))
  for c in range(len(strw)):
    curlet = strw[c:c+1]
    b = ord(curlet)-96
    vect[0][c]=b
  return vect
def mag(vect,n):
  h =0
  for s in range(n):
    cur = vect[0][s]
    cur = cur**2
    h+=cur
  h = mt.sqrt(h)
  return h
def cossim(vect1,vect2,mag1,mag2,num):
    d = 0
    for c in range(num):
        cur1 = vect1[0][c]
        cir2 = vect2[0][c]
        ds = cur1*cir2
        d+=ds
    prodmag = mag1*mag2
    j = d/prodmag
    return j
def comp(str, lst):
    l1 = []
    dict1 = {}
    ng = ngramgen(str,2)
    for word in lst:
        max1 = max(len(str),len(word))
        ny = ngramgen(word,2)
        ngsc = compare(ny, ng)
        vec1 = lettonum(str, max1)
        vec2 = lettonum(word, max1)
        mag1=mag(vec1,max1)
        mag2 = mag(vec2,max1)
        cos = cossim(vec1,vec2, mag1,mag2,max1)
        mat = createarray(str, word)
        levd = levdist(str,word, mat)
        levd = 1/levd+1
        sum = levd+cos+ngsc
        avg = sum/3
        l1.append(avg)
    for i in range(len(l1)):
        dict1[lst[i]]=l1[i]
    dicty = sorted(dict1.items(),key = lambda t:t[1], reverse = True)
    return dicty




        

