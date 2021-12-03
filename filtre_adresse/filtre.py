import h5py
import os
from PIL import Image
import scipy.io
#import cv2
from random import randint
import numpy as np
import sys


def getCategorie():
    file = open("lienFilted2.txt","r")
    
    tab = []
    for line in file:
        tab.append(line.split("/"))
       
        
    tab_avec_cat = []
    i = 0
    for line in tab: 
        
        here = line[0]+"/"+line[1]+"/"+line[2]+"/"+line[3]+"/"
        if line[3][:2].isdigit() and('eme-' in line[3] or 'e-s' in line[3]  or 'siecle' in line[3]): # categorie de siecle
            tab_avec_cat.append([here,"categorie de siecle"])
            continue
        elif line[3][:4].isdigit() ==True and line[3][4:6]=='-2': #rdm
            tab_avec_cat.append([here,"categorie de siecle"])
            continue
        elif ( line[3][-4:-1].isdigit() and line[3][:2].isdigit() and line[3][3].isdigit()==False) or 'xzacasta-1803'in line[3] or 'zzfrigga1912' in line[3]:#sauvetage bateau de peche
            tab_avec_cat.append([here,"sauvetage bateau"])
            continue
        elif  ( line[3][-5:-2].isdigit() and line[3][-1]=='b' ) or ( line[3][:2].isdigit() and line[3][-1]=='b' ) or ( line[3][:2].isdigit() and line[3][8]=='b'):#sauvetage bateau de peche
            tab_avec_cat.append([here,"sauvetage bateau"])
            #tabSauvetage.append(line)
            continue
        elif  'b-' in line[3]:#sauvetage bateau de peche
            tab_avec_cat.append([here,"sauvetage bateau"])
            #tabSauvetage.append(line)
            continue
        elif 'sauvind' in line[3] : #Sauvetages individuels
            tab_avec_cat.append([here,"sauvetage individuel"])
            continue
            #print(line[3])
        elif line[3][:2].isdigit()==False and 'estamine' in line[3]  : # article
            tab_avec_cat.append([here,"article"])
            continue
            #print(line[3])
        elif line[3][-1]=='h' and line[3][len(line[3])-2].isdigit() : # personne avec honneur
            tab_avec_cat.append([here,"personne avec honneur"])
            #print(line[3])
            continue
        elif line[3][:2].isdigit()==False and  line[3][:3] =='pat' and line[3][4].isdigit()==True or 'polp' in line[3]: # patronyme 
            #i+=1
            tab_avec_cat.append([here,"patronyme"])
            
            #print(line[3])
            continue
            #print(line[3])
        elif line[3][len(line[3])-3:].isdigit()==True and not line[3][len(line[3])-4].isdigit()==True and not line[3][4].isdigit()==True : # patronyme 
            tab_avec_cat.append([here,"patronyme"])
            #print(line[3])
            continue
        elif 'canot-sh' in line[3]  : # Canot de la Société Humaine
            tab_avec_cat.append([here,"Société Humaine"])
            #print(line[3])
            continue
            #print(line[3])
        elif 'snsm' in line[3] :
            tab_avec_cat.append([here,"chronologie"])
            print(line[3])
            continue
        elif line[3][-4:-1].isdigit()==True and line[3][0].isdigit()==False: # document 
            #i+=1
            tab_avec_cat.append([here,"document"])
            continue
        elif line[3][-4:-1].isdigit()==True  : # Actes de sauvetage pendant une periode
            #i+=1
            tab_avec_cat.append([here,"Actes de sauvetage pendant une periode"])
            continue
        elif line[3][:2].isdigit()==True and line[3][3].isdigit()!=True:  # nauffrage
            tab_avec_cat.append([here,"nauffrage"])
            #print(line[3])
            continue
        else:                                # bordel
            tab_avec_cat.append([here,"bordel"])
            continue
        
    #print(i)
    """
    file2 = open("lienFilted2.txt","w")
    for line in tabFilted: 
        file2.write(line+"\n")
    file2.close()
    """
    file.close()
    return tab_avec_cat

if __name__ == "__main__":
    
    tab = getCategorie()
    for i in tab:
        print(i)

