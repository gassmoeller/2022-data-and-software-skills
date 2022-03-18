def solution(test):
  
  numbers = ['0','1','2','3','4','5','6','7','8','9']
  
  import string
  alphabets_lower = string.ascii_lowercase
  tryouts = list(alphabets_lower)
  tryouts.append(' ')

  alphabets_upper = string.ascii_uppercase
  Tryouts = list(alphabets_upper)
  Tryouts.append(' ')
  alphabets = ['100000','110000','100100','100110','100010','110100','110110','110010','010100','010110','101000','111000','101100','101110','101010','111100','111110','111010','011100','011110','101001','111001','010111','101101','101111','101011','000000']

  if len(test) > 51:
    print ('The length of the sign is',len(test),': Not Handled')
    return
  for number in numbers:
    for i,n in enumerate(test):
      if n == number:
        print('Numbers are not handled')
        return
  else:

    for tryout,alphabet,Tryout in zip(tryouts,alphabets,Tryouts):
      capital = '000001'
      capitals = capital + alphabet
    
      for i,n in enumerate(test):
      
        if n == tryout:
          c = tryout = alphabet
          test = test.replace(n,c)

        if n == Tryout:
          d = Tryout = capitals
          test = test.replace(n,d) 
  print (test)
  return