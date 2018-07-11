"""
Pyglatin game
@Bodavijay 
"""
#newly added string
pyg = 'ay'
#taking input
original = raw_input('Enter a word:')
#Checking whether it has any characters
if len(original) > 0 and original.isalpha():
#making the word lower 
  word=original.lower()
#extracting first word
  first=word[0]
#concatenating all the three strings
  new_word= word + first+pyg
#slicing inorder to get desired outcome
  new_word=new_word[1:len(new_word)]
#printing it
  print new_word
 
else:
  print 'empty'
