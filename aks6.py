import csv
with open("gp3.csv") as f:
   csv_file=csv.reader(f)
   data=list(csv_file)
   s=data[1][:-1]
   g=[['?'for i in range(len(s))]for j in range(len(s))]
   for i in data:
       if i[-1]=='yes':
          for j in range(len(s)):
              if i[j]!=s[j]:
                  s[j]='?'
                  g[j][j]='?'
       elif i[-1]=='no':
          for j in range(len(s)):
              if i[j]!=s[j]:
                  g[j][j]=s[j]
              else:
                   g[j][j]='?'
       print("\n steps of candidate elimination algorithm",data.index(i)+1)
       print(s)
       print(g)
   gh=[]
   for i in g:
       for j in i:
          if j!='?':
              gh.append(i)
              break
   print("\n final specific hypothesis:\n",s)
   print("\n final general hypothesis:\n",gh)
 
