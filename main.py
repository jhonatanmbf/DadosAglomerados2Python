continueInsertData = "S";
dictDataInsertForUsers = {};
dictDataInsertForUsersBackup = {};
countInterationList = 1;

def PrintForDictionaryBackup():
  decisioViewDictionaryBackup = input("Deseja ver os dados do dicionario de bacuk (S/N): ")
  if(decisioViewDictionaryBackup.upper() == "S"):
    print(f"Dicionario de backup: {dictDataInsertForUsersBackup}")
    return;

def ClearDictionaryAndMost():
  if(len(dictDataInsertForUsers["nomes"]) == 5 ):
    print("\n")
    print(f"Dicionario de nome principal: {dictDataInsertForUsers}")
    dictDataInsertForUsers.clear();
    print("\n")
    print("Dados apagados agora eles so possuem no dicionario de backup !")
    print("\n")
    return True;
  else:
    return False;

while(continueInsertData.upper() == "S"):
  nome = input(f"Digite seu {countInterationList}º nome da lista: ");
  
  if ("nomes" in dictDataInsertForUsers):
    dictDataInsertForUsers["nomes"].append(nome)
    dictDataInsertForUsersBackup["nomes"].append(nome)
  elif("nomes" in dictDataInsertForUsersBackup):
    dictDataInsertForUsers["nomes"] = [nome]
  else:
    dictDataInsertForUsers["nomes"] = [nome]
    dictDataInsertForUsersBackup["nomes"] = [nome]

  countInterationList += 1;

  principalDicClear = ClearDictionaryAndMost();
  if(principalDicClear):
    PrintForDictionaryBackup();
  print("\n")
  continueInsertData = input("Deseja continuar digite (S/N): ")