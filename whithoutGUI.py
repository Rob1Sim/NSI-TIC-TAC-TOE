# -*- coding: utf-8 -*-
"""
Created on Tue May 18 09:35:08 2021

@author: TNSI-1
"""


def morpion():
    plateau=[[0],[0],[0],[0],[0],[0],[0],[0],[0]]
    n=True
    t=eval(input("Choisissez qui commence"))
    while n==True:
        t=-t
        l1=[[plateau[0]],[plateau[1]],[plateau[2]]]
        l2=[[plateau[3]],[plateau[4]],[plateau[5]]]
        l3=[[plateau[6]],[plateau[7]],[plateau[8]]]
        c1=[[plateau[0]],[plateau[3]],[plateau[6]]]
        c2=[[plateau[1]],[plateau[4]],[plateau[7]]]
        c3=[[plateau[2]],[plateau[5]],[plateau[8]]]
        d1=[[plateau[0]],[plateau[4]],[plateau[8]]]
        d2=[[plateau[2]],[plateau[4]],[plateau[6]]]
        cv=[l1,l2,l3,c1,c2,c3,d1,d2]
        for i in range(0,len(cv)):
            if cv[i][0][0][0]==cv[i][1][0][0] and cv[i][0][0][0]==cv[i][2][0][0] and cv[i][0][0][0]==1:
                n=False
                return "Victoire des croix"
            if cv[i][0][0][0]==cv[i][1][0][0] and cv[i][0][0][0]==cv[i][2][0][0] and cv[i][0][0][0]==-1:
                n=False
                return "Victoire des ronds"
        if plateau[0][0]!=0 and plateau[1][0]!=0 and plateau[2][0]!=0 and plateau[3][0]!=0 and plateau[4][0]!=0 and plateau[5][0]!=0 and plateau[6][0]!=0 and plateau[7][0]!=0 and plateau[8][0]!=0:
            n=False
            return "Matche nul"
        z=True
        while z==True:
            a=eval(input("Entrez le numéro de la case sur laquelle vous voulez jouer"))
            if plateau[a]!=[0]:
                print("Il y a déjà un symbole dans cette case")
            else:
                z=False
        plateau[a][0]=t
        print(l1)
        print(l2)
        print(l3)


