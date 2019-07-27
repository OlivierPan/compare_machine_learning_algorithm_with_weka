import os
import shutil
k=open("/users/pansa/desktop/weka_projet/3001_3500.txt","r",encoding='utf8')
content=k.readlines()

for i in range(len(content)):
    try:
        print(content[i])
        x=input("Number please : ___ ")
        if x=="1":
            fichier=open("/users/pansa/desktop/bon/"+"4bon"+str(i)+".txt","w",encoding='utf-8')
            fichier.write(content[i])
            fichier.close()
        elif x=="2":
            fichier=open("/users/pansa/desktop/mauvais/"+"4mauvais"+str(i)+".txt","w",encoding='utf-8')
            fichier.write(content[i])
            fichier.close()
        elif x=="3":
            fichier=open("/users/pansa/desktop/moyen/"+"4moyen"+str(i)+".txt","w",encoding='utf-8')
            fichier.write(content[i])
            fichier.close()
        elif x=="4":
            fichier=open("/users/pansa/desktop/nondit/"+"4nondit"+str(i)+".txt","w",encoding='utf-8')
            fichier.write(content[i])
            fichier.close()
        print("\n")
    except UnicodeEncodeError:
        print("UnicodeEncoderError, jump this one")
        
k.close()    

