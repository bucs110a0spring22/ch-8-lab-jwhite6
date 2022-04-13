class StringUtility:
  def __init__(self, string):
    self.string = string

  def __str__(self):
    return self.string

  def vowels(self):
    vowel = set("aeiouAEIOU")
    count = 0
    for char in self.string:
      if char in vowel:
        count = count + 1
      
    if count >= 5:
      return 'many'
    else: 
      return str(count)
        
  def bothEnds(self):
    for char in self.string:
      newString = self.string[0] + self.string[1] + self.string[-2] + self.string[-1]
    
    if len(self.string) <= 2:
      return ''
    else: 
      return newString
      
  def fixStart(self):
    if (len(self.string) >= 1):
      first_char = self.string[0]
    else:
      first_char = ''
    newString = first_char
    for char in range (1, len(self.string)):
      if self.string[char] == first_char:
        newString += '*'
      else:
        newString += self.string[char]
    return newString
    
  def asciiSum(self):
    ascii_sum = 0
    for char in self.string:
      ascii_sum += ord(char)
    return ascii_sum  
    
  def cipher(self):
    newString = ''
    for char in self.string:
      i = ord(char)
      i += len(self.string)
      if not char.isalpha():
        newString += char
        continue
      if char.isupper():
        while i > ord('Z'):
          i = i - 26
      if char.islower():
        while i > ord('z'):
          i = i - 26
      character = chr(i)
      newString += character
    return newString