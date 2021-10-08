def frequently_use_word(s):
  input("")
  s=s.replace(".", " ")
  s=s.replace(",", " ")
  s=s.replace("?", " ")
  s=s.replace("!", " ")
  s=s.replace("(", " ")
  s=s.replace(")", " ")
  s=s.replace("\'", " ")
  s=s.replace("\"", " ")
#  print(s)
  s=s.lower()
  s=s.split(" ")
  most_word = 'zzz'
  a=[]
#  print(s)
#  most_word_collection = set()
  for i in s:
    if s.count(i)>s.count(most_word) and i!= '':
      most_word=i
  for i in s:
    if s.count(i)==s.count(most_word):
      a += [i] 
  for i in list(set(a)):
    print("The most frequently use word are: "+"\""+ i +"\""+ ", it shows up "+str(s.count(most_word))+" times")