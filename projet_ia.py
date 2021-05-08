# -*- coding: utf-8 -*-
"""Projet_IA.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1yyV0DPi79GGkKgHEzki9NWVTVtuluwet
"""

from copy import deepcopy
import timeit

class taquin(object) : 
  t = [] 
  tf =[[1,2,3],[4,5,6],[7,8,0]]
  def __init__(self,tab):
      self.t = tab
 
  def etat_finale(self,t) : 
    for i in range(3) :
      for j in range(3):
        if (t[i][j] != self.tf[i][j]):
          return False
    return True 
 
  def position_case_vide(self,tb):
    for i in range(3) :
      for j in range(3):
        if (tb[i][j] == 0):
            return i,j
    return -1
 
  def permuter(self,t,c1,c2):
    i,j =c1 
    ii,jj=c2
    aux=t[i][j]
    t[i][j] = t[ii][jj]
    t[ii][jj] = aux 
    return t
 
 
  def affiche(self,t):
    j=0
    for i in range(7):
      if(i%2==0):
        print("|__|")

      else:
        print("|",t[j][0],"|",t[j][1],"|",t[j][2]," |")
        j=j+1

  def numero(self,x,y):
    return self.t[x][y]
 
  def transition(self,arr):
    tb=[]
    x,y=self.position_case_vide(arr)
    l=[]
    
    if(x-1>=0):
      l.append(((x-1),y))
    if(y-1>=0):
      l.append((x,(y-1)))
    if(x+1<3):
      l.append(((x+1),y))
    if(y+1<3):
      l.append((x,(y+1)))

    for i in range(len(l)):
      t1=deepcopy(arr)
      self.permuter(t1,self.position_case_vide(t1),l[i])
      tb.append(t1)
    return tb

  def dfs(self):
      #commencer de compter le temps d'exe
      start_algo=timeit.default_timer() 
      freeNodes = []
      closed = []
      success = False 
      freeNodes.append(self.t)
      l=0
      lenGeneratedState = len(self.transition(freeNodes[0]))
      while (success == False and len(freeNodes) != 0) and l<9:
      
        generatedStates = self.transition(freeNodes[0])
        
        #print('Free Node 1  = ',freeNodes)
        closed.append(freeNodes[0])
        freeNodes.pop(0)
        #print('first Node after del =  ',freeNodes)
        #print('Generated state  =  ',generatedStates)
        moved = False
        for i in generatedStates:
          if ( i not in closed) or (i not in freeNodes) :
            #print(i in closed)  
            freeNodes.insert(0,i)
            moved = True
        if moved==True: 
          l+=1 
        else:
          if (lenGeneratedState <= 1 ):
            l-=1 ; 
          else:
            lenGeneratedState-= 1 
        
        #print('free Node after insert generated =  ',freeNodes)
        if(self.etat_finale(closed[-1])):
          stop_algo = timeit.default_timer()
          time = stop_algo-start_algo
          success=True
          for i in closed:
            self.affiche(i)
          print(time,'s')
        lenGeneratedState = len(generatedStates)
        
      
  def bfs(self):
      start_algo=timeit.default_timer() #commencer de compter le temps d'exe     
      freeNodes = []
      closed = []
      success = False 
      freeNodes.append(self.t)

      while (success == False and len(freeNodes) != 0) :
        
        generatedStates= self.transition( freeNodes[0])
        closed.append(freeNodes[0])
        freeNodes.pop(0)
        for i in generatedStates:
          if ( i not in closed) or (i not in freeNodes) :
            freeNodes.append(i)
            
        if(self.etat_finale(closed[-1])):
          stop_algo = timeit.default_timer()
          time = stop_algo-start_algo          
          success=True
          success=True
          for i in closed:
            self.affiche(i) 
          print('success')
          print(time)   

        
  def G(self,n):
    nodeX,nodeY = self.position_case_vide(n)
    goalX,goalY=self.position_case_vide(self.tf)
    dx = abs(nodeX - goalX);
    dy = abs(nodeY - goalY);
    return 1 * (dx + dy);
  
  def H(self,n):
    nodeX,nodeY = self.position_case_vide(n)
    goalX,goalY=self.position_case_vide(self.t)
    dx = abs(nodeX - goalX);
    dy = abs(nodeY - goalY);
    return 1 * (dx + dy);   
  
  def Best(self,arr):
    min=self.H(arr[0])+self.G(arr[0])
    node=arr[0]
    for i in arr:
      curr=self.H(i)+self.G(i)
      if (curr<min):
        node=i
        min=curr
    return node
  
  def aStar(self):
    start_algo=timeit.default_timer() #commencer de compter le temps d'exe     
    freeNodes = []
    closed = []
    success = False 
    freeNodes.append(self.t)
    while (success == False and len(freeNodes) != 0) :
        
        generatedStates= self.transition(freeNodes[0])
        bestNoued = self.Best(generatedStates)
        closed.append(bestNoued)
        
        if(self.etat_finale(closed[-1])):
          stop_algo = timeit.default_timer()
          time = stop_algo-start_algo
          success=True
          for i in closed:
            self.affiche(i) 
          print('succes')
          print(time)   
    
        freeNodes.pop(0)
        for i in generatedStates:
          if ( i not in closed) or (i not in freeNodes) :
            freeNodes.append(i)

tab= [[1, 2, 3], [4, 5, 6], [0, 7, 8]]

t=taquin(tab)

t.bfs()

t.dfs()

t.aStar()

