#Определение того, что можно подставитmasfaenoifvnsaoerfvineofp


#kdsjnsorvnpwsriovnwpqevibpwev


#lszfijvnpsbinvwv


#asofiuadcouehvc

def Answer(part_OfLine, part_OfSequance, position):

  Phrase = "at position " + str(position + 1) + ": expected "

  if part_OfLine == "|":
    
    if part_OfSequance == "|": 
      Phrase += "( or ), found |"
    elif part_OfSequance == None: 
      Phrase += "( or END, found |"

  elif part_OfLine == ")":
    
    if part_OfSequance == "(":
      Phrase += "( or |, found )"
    elif part_OfSequance == None: 
      Phrase += "( or END, found )"
  
  elif part_OfLine == "8":

    if part_OfSequance == "(":
      Phrase += "( or |, found END"
    else: Phrase += "( or ), found END"
  
  return Phrase


#Функция проверки, которая выдаёт не обработанную фразу

def Great_checker(InLine):

  Sequance = [] #Последовательность предшествиников. По ней можно отслеживать, правильно ли поставлен символ

  Almost_End = len(InLine) - 1 #Понадобится позже после цикла

  for i in range(len(InLine)):
    if InLine[i] == "(":
      Sequance = [InLine[i]] + Sequance
  
    if InLine[i] == "|":

      if Sequance == []:
        return Answer(InLine[i], None, i)
      if Sequance[0] == "|":
        return Answer(InLine[i], Sequance[0], i)
    
      Sequance = [InLine[i]] + Sequance
  
    if InLine[i] == ")":

      if Sequance == []:
        return Answer(InLine[i], None, i)
      if Sequance[0] == "(":
        return Answer(InLine[i], Sequance[0], i)
    
      Sequance = Sequance[2:len(Sequance)]

  #Исключенемо остаются два случая, но в одном из случаев надо показать, что мы вышли из цикла. Для этого я буду писать в качестве первого аргумента в функцию строчную 8

  if Sequance == []: 
    return ["correct, length = ", Almost_End + 1]

  elif Sequance[0] == "(" or Sequance[0] == "|":
    return Answer("8", Sequance[0], Almost_End+1)


line = input()

print(Great_checker(line))

  
