def shift_alphabets(n):
  word=input("")
  letter="abcdefghijklmnopqrstuvwxyz"
  Letter="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  for i in range(len(word)):
    for j in range(len(letter)):
      if word[i] == letter[j]:
        word =word[:i]+word[i].replace(letter[j],letter[(j+n)%26])+word[i+1:]
        break
      elif word[i] == Letter[j]:
        word =word[:i]+word[i].replace(Letter[j],Letter[(j+n)%26])+word[i+1:]
        break
  print(word)