# CSCE 160 - Prof. Kim - HW3
#Names: Rares-Mihail Neagu, Tyler Fortune
#Dates:10/22/2021,10/23/2021,10/24/2021,10/26/2021
#Connect4 Game Program
#------------------IMPORTS------------------------------------
import random

#------------------FUNCTIONS----------------------------------
#--------GRAPHICS FUNCTIONS-----------------------------------
def displayBoard(Board):
    #this function displays the gameboard on the screen
    for j in range(7):
        print("|",j,end=" ")
    print("|")
    print("-----------------------------")
    for i in range(6):
        print("-----------------------------")
        for j in range(7):
            print("|",Board[i][j],end=" ")
        print("|")
    print("-----------------------------")
#--------STATUS FUNCTIONS--------------------------------------
def StoreBoardState(B):
    #this function takes in the gameboard
    #this function stores the state of the gameboard in another matrix to avoid common reference
    #creating a matrix to store the state
    K=[0]*6
    for k in range(6):
        K[k]=[" "] * 7#copying element by element 
    #copying element by element
    for i in range(0,6,1):#copying element by element
        for j in range(0,7,1):
            K[i][j]=B[i][j]
    return K
def checkWin(B):
    #this function checks if the game was won
    #uses the variable k to control the starting point in the table 
    #thus, for columns k has the values 0,1,2,3, while for rows 0,1,2
    win=False#creates a flag to hold the win information
    #1.check the horizontal lines
    for i in range(6):
        for k in range(4):
            if(B[i][k]==B[i][k+1] and B[i][k+1]==B[i][k+2] and B[i][k+2]==B[i][k+3] and B[i][k]!=" "):
                win=True #if 4 horizontal tiles are the same then there is a win
                break#and it breaks out of the inner loop
        if(win):#after finding a win it breaks out of the outer loop
            break
    #2.check the vertical lines
    for j in range(7):
        for k in range(3):
            if(B[k][j]==B[k+1][j] and B[k+1][j]==B[k+2][j] and B[k+2][j]==B[k+3][j] and B[k][j]!=" "):
                win=True#if 4 vertical tiles are the same then there is a win
                break#and it breaks out of the inner loop
        if(win):#after finding a win it breaks out of the outer loop
            break
    #3.check the diagonals
       #3.1 check the major diagonals
    for k in range(5,2,-1):
        for p in range(3,7):#uses also the variable p to control the column starting point in the table 
            if(B[k][p]==B[k-1][p-1] and B[k-1][p-1]==B[k-2][p-2] and B[k-2][p-2]==B[k-3][p-3] and B[k][p]!=" "):
                win=True#if a 4 tiles in a diagonal are the same there is win
                break#and it breaks out of the inner loop
        if(win):#after finding a win it breaks out of the outer loop
            break
        #3.2 check the minor diagonals
    for k in range(5,2,-1):
        for p in range(4):#uses also the variable p to control the column starting point in the table 
            if(B[k][p]==B[k-1][p+1] and B[k-1][p+1]==B[k-2][p+2] and B[k-2][p+2]==B[k-3][p+3] and B[k-3][p+3]!=" "):
                win=True#if a 4 tiles in a diagonal are the same there is win
                break#and it breaks out of the inner loop
        if(win):#after finding a win it breaks out of the outer loop
            break
    return win

def checkTie(B):
    #this function takes in the gameboard
    #it returns if there is a tie
    tie=False#creates a flag to hold the tie information
    if(checkWin(B)==False):#checks if there is no win 
       if(fullBoard(B)==True):#checks if the board is full
          tie=True
    return tie
    
def fullColumnCheck(B,choice):
    #this function takes in the gameboard and the column choice of the user
    #it returns if the row is full or not, in the variable "full"
    full=True#create a flag and assume it is full/true 
    for i in range(6):
        if(B[i][choice]==" "):
            full=False#when a blank has been found, it becomes false
            break#as soon as it finds a blank, it breaks
    return full

def fullBoard(B):
    #this function takes in the gameboard and checks if it's full
    full=True#create a flag and assume it is full/true
    #checks if all columns are full
    for j in range(0,7,1):
        if(fullColumnCheck(B,j)==False):
            full=False
            break#as soon as an empty spot was found, it breaks
    return full

#------RULE-BASED FUNCTIONS--------------------------------------
def ColumnReassign(B,choice,t):
    #this function takes in the gameboard, the choice, and the turn
    #this function reassigns the value of the column, if it's full
    #returns y, the new column
    x=fullColumnCheck(B,choice)#checks if the column is full
    if(x==False):
        y=choice#no reassigning needed
    else:#it has to reassign the column
        if(t==0):#it's the player's turn
            y=int(input("The column you chose is full,enter another one:"))
            while(fullColumnCheck(B,y)==True):#force the player to do it
                y=int(input("The column you chose is full,enter another one:"))
        elif(t==1):#it's the computer's turn
            y=random.randint(0,6)
            while(fullColumnCheck(B,y)==True):
                y=random.randint(0,6)        
    return y
        

def rowPlacement(B,choice,t):
    #this function takes the column from the input,the gameboard,and the turn
    #checks if the rows are empty and which one should be filled 
    for i in range(5,-1,-1):
            if(B[i][choice]==" "):
                row=i#stores the row of the box that should be filled
                break#after finding the lowest empty box, it breaks   
    return row


#---------------AI FUNCTIONS-------------------------------------   
def fourBlocking(B):
    #this function takes in the gameboard
    #this function allows the computer to block three-in-a-rows
    #the returned variable x stores the column number
    #1.blocking horizontally
    found=False#creates a flag to keep track if a block has been found
    for i in range(5,-1,-1):
        for p in range(0,5,1):#using the variable p to control the column starting point
             if(B[i][p]==B[i][p+1] and B[i][p+1]==B[i][p+2] and B[i][p]!=" " and B[i][p]=="X"):#check if there's a three-in-a-row
               if(p==0 or p==4):#taking care of edgecases
                  if(i==5):#taking care of the row edgecase
                     if(B[i][3]==" "):#check if the adjacent box is empty
                          found=True
                          x=3#the index in the middle is the only blocking strategy for both edgecases
                          break#after finding a block, break
                     else:#the box is full, no blocking needed
                          x=-1                      
                  else:#check the other cases
                   if(B[i][3]==" "):#check if the adjacent box is empty
                       #it is empty, so it has to block
                       if(B[i+1][3]!=" "):#check if the box below is empty
                           found=True
                           x=3#the index in the middle is the only blocking strategy for both edgecases
                           break#after finding a block, break
                       else:#it is empty,no blocking needed
                           x=-1
                   else:#the box is full, no blocking needed
                       x=-1#assign to x a sentinel value if no three-in-a-row was found
               else:#check the other cases
                   if(B[i][p-1]==" " and B[i][p+3]==" "):#check if both the adjacent boxes are empty
                       if(i==5):#taking care of the row edgecase
                          choice=random.randint(0,1)#uses the random variable to randomly block before or after
                          if(choice==0):#blocks at p-1
                                  found=True
                                  x=p-1
                                  break#after finding a block, break
                          elif(choice==1):#blocks at p+3
                                  found=True
                                  x=p+3
                                  break#after finding a block, break
                       else:#check the other cases   
                       #check if there are pawns under boxes adjacent to the three-in-a-row
                          if(B[i+1][p-1]!=" " and B[i+1][p+3]!=" "):#both of them are filled
                              choice=random.randint(0,1)#uses the random variable to randomly block before or after
                              if(choice==0):#blocks at p-1
                                      found=True
                                      x=p-1
                                      break#after finding a block, break
                              elif(choice==1):#blocks at p+3
                                      found=True
                                      x=p+3
                                      break#after finding a block, break
                          elif(B[i+1][p-1]!=" "):#the box under p-1 is full
                               found=True
                               x=p-1
                               break#after finding a block, break
                          elif(B[i+1][p+3]!=" "):#the box under p+3 is full
                               found=True
                               x=p+3
                               break#after finding a block, break
                          else:#the adjacent boxes are empty,no blocking needed
                              x=-1                           
                   elif(B[i][p-1]==" "):#blocks at p-1
                       #check if there are pawns under boxes adjacent to the three-in-a-row
                       if(i==5):#taking care of row edgecase
                            found=True
                            x=p-1
                            break#after finding a block, break
                       else:#check the other cases
                            if(B[i+1][p-1]!=" "):#blocking needed
                                found=True
                                x=p-1
                                break#after finding a block, break
                            else:#no pawns, no blocking needed
                                x=-1
                   elif(B[i][p+3]==" "):#blocks at p+3
                   #check if there are pawns under boxes adjacent to the three-in-a-row
                       if(i==5):#taking care of row edgecase       
                            found=True
                            x=p+3 
                            break#after finding a block, break
                       else:#check the other cases
                            if(B[i+1][p+3]!=" "):#blocking needed
                               found=True
                               x=p+3
                               break#after finding a block, break
                            else:#no pawns, no blocking needed
                                x=-1
                   else:#all are full,no blocking needed
                       x=-1#assign to x a sentinel value if no blocking is needed
             else:#there is no three-in-a-row, no blocking needed
                  x=-1#assign to x a sentinel value if no blocking is needed
        #as soon as it founds a block, it breaks out of the outer loop
        if(found==True):
            break
    #2.blocking vertically
    if(found==False):#if no horizontal block is needed,it checks for vertical ones
        for j in range(0,7,1):
            for k in range(5,2,-1):#using the variable k to control the row starting point
                if(B[k][j]==B[k-1][j] and B[k-1][j]==B[k-2][j] and B[k][j]!=" " and B[k][j]=="X"):#check if there's a three-in-a-row
                  if(B[k-3][j]==" "):#check if the box above is empty
                      found=True
                      x=j
                      break#after finding a block, break
                  else:
                      x=-1#assign to x a sentinel value if no blocking is needed
                else:#there is no three-in-a-row, no blocking needed
                  x=-1#assign to x a sentinel value if no blocking is needed
            #as soon as it founds a block, it breaks out of the outer loop
            if(found==True):
                break
    #3.blocking diagonally
    #3.1 blocking major diagonals
    if(found==False):
        for k in range(5,2,-1):#again, using k and p to control the starting points
            for p in range(3,7,1):
                #check if there's a three-in-a-row
                if(B[k-2][p-2]==B[k-1][p-1] and B[k-1][p-1]==B[k][p] and B[k][p]!=" "):
                    if(B[k-3][p-3]==" "):#check if the fourth box is empty or not
                    #check if the boxes under the fourth are full
                        full=True#create a flag to see if the three boxes under are full
                        for i in range(5,k-2,-1):
                              if(B[i][p-3]==" "):
                                  full=False
                                  break#as soon as it finds one empty,it breaks
                        if(full==True):
                                  found=True
                                  x=p-3
                                  break#after finding a block, break
                    else:
                        x=-1#assign to x a sentinel value if no blocking is needed
                else:
                    x=-1#assign to x a sentinel value if no blocking is needed
            #as soon as it founds a block, it breaks out of the outer loop
            if(found==True):
                break
    #3.2 blocking minor diagonals
    if(found==False):
         for k in range(5,2,-1):#again, using k and p to control the starting points
             for p in range(0,4,1):
                 #check if there's a three-in-a-row
                 if(B[k][p]==B[k-1][p+1] and B[k-1][p+1]==B[k-2][p+2] and B[k][p]!=" "):
                     if(B[k-3][p+3]==" "):#check if the fourth box is empty or not
                     #check if the boxes under the fourth are full
                        full=True#create a flag to see if the three boxes under are full
                        for i in range(5,k-2,-1):
                              if(B[i][p+3]==" "):
                                  full=False
                                  break#as soon as it finds one empty,it breaks
                        if(full==True):
                                  found=True
                                  x=p+3
                                  break#after finding a block, break
                     else:
                         x=-1#assign to x a sentinel value if no blocking is needed
                 else:
                     x=-1#assign to x a sentinel value if no blocking is needed
             #as soon as it founds a block, it breaks out of the outer loop 
             if(found==True):
                 break
    return x   

def XX_XtypeBlocking(B):
    #this function takes in the gameboard
    #it blocks XX_X or X_XX traps
    #it returns the variable x storing the value of the column 
    #1.blocking horizontally
    #1.1 blocking XX_X horizontally
    found=False#creates a flag to keep track if a block has been found
    for i in range(5,-1,-1):
        for p in range(0,4,1):#using the variable p to control the column starting point
           #check if there is a XX_X trap
           if(B[i][p]==B[i][p+1] and B[i][p+1]==B[i][p+3] and B[i][p+2]==" " and B[i][p]!=" "):
                   if(i==5):#take care of the edge case
                      found=True
                      x=p+2
                      break#when it finds a block, it breaks
                   else:#takes care of the other cases
                       if(B[i+1][p+2]!=" "):#checks if the box under is full
                          found=True
                          x=p+2
                          break#when it finds a block, it breaks
                       else:
                           x=-1#assign to x a sentinel value if no blocking is needed
           else:
                x=-1#assign to x a sentinel value if no blocking is needed
        #as soon as it founds a block, it breaks out of the outer loop 
        if(found==True):
              break
    #1.2 blocking X_XX horizontally 
    if(found==False):
        for i in range(5,-1,-1):
            for p in range(0,4,1):#using the variable p to control the column starting point
               #check if there is a XX_X trap
               if(B[i][p]==B[i][p+2] and B[i][p+2]==B[i][p+3] and B[i][p+1]==" " and B[i][p]!=" "):
                       if(i==5):#take care of the edge case
                          found=True
                          x=p+1
                          break#when it finds a block, it breaks
                       else:#takes care of the other cases
                           if(B[i+1][p+1]!=" "):#checks if the box under is full
                              found=True
                              x=p+1
                              break#when it finds a block, it breaks
                           else:
                               x=-1#assign to x a sentinel value if no blocking is needed
               else:
                    x=-1#assign to x a sentinel value if no blocking is needed
            #as soon as it founds a block, it breaks out of the outer loop 
            if(found==True):
                  break
    #2-there is no vertical trap
    #3.blocking diagonally
    #3.1 blocking the major diagonals
    #3.1.1 blocking XX_X on the major diagonals
    if(found==False):
        for k in range(5,2,-1):
            for p in range(3,7,1):#again, using k and p to control the starting points
               #check if there is a XX_X trap
               if(B[k][p]==B[k-2][p-2] and B[k-2][p-2]==B[k-3][p-3] and B[k-1][p-1]==" " and B[k][p]!=" "):
                       if(i==5):#take care of the edge case
                          found=True
                          x=p-1
                          break#when it finds a block, it breaks
                       else:#takes care of the other cases
                           if(B[k][p-1]!=" "):#checks if the box under is full
                              found=True
                              x=p-1
                              break#when it finds a block, it breaks
                           else:
                               x=-1#assign to x a sentinel value if no blocking is needed
               else:
                    x=-1#assign to x a sentinel value if no blocking is needed
            #as soon as it founds a block, it breaks out of the outer loop 
            if(found==True):
                  break
    #3.1.2 blocking X_XX on the major diagonals
    if(found==False):
        for k in range(5,2,-1):
            for p in range(3,7,1):#again, using k and p to control the starting points
               #check if there is a XX_X trap
               if(B[k][p]==B[k-1][p-1] and B[k-1][p-1]==B[k-3][p-3] and B[k-2][p-2]==" " and B[k][p]!=" "):
                       if(i==5):#take care of the edge case
                          found=True
                          x=p-2
                          break#when it finds a block, it breaks
                       else:#takes care of the other cases
                           if(B[k-1][p-2]!=" "):#checks if the box under is full
                              found=True
                              x=p-2
                              break#when it finds a block, it breaks
                           else:
                               x=-1#assign to x a sentinel value if no blocking is needed
               else:
                    x=-1#assign to x a sentinel value if no blocking is needed
            #as soon as it founds a block, it breaks out of the outer loop 
            if(found==True):
                  break
    #3.2 blocking the minor diagonals
    #3.2.1 blocking XX_X on the minor diagonals
    if(found==False):
        for k in range(5,2,-1):
            for p in range(0,4,1):#again, using k and p to control the starting points
               #check if there is a XX_X trap
               if(B[k][p]==B[k-2][p+2] and B[k-2][p+2]==B[k-3][p+3] and B[k-1][p+1]==" " and B[k][p]!=" "):
                       if(i==5):#take care of the edge case
                          found=True
                          x=p+1
                          break#when it finds a block, it breaks
                       else:#takes care of the other cases
                           if(B[k][p+1]!=" "):#checks if the box under is full
                              found=True
                              x=p+1
                              break#when it finds a block, it breaks
                           else:
                               x=-1#assign to x a sentinel value if no blocking is needed
               else:
                    x=-1#assign to x a sentinel value if no blocking is needed
            #as soon as it founds a block, it breaks out of the outer loop 
            if(found==True):
                  break
    #3.2.2 blocking X_XX on the minor diagonals
    if(found==False):
        for k in range(5,2,-1):
            for p in range(0,4,1):#again, using k and p to control the starting points
               #check if there is a XX_X trap
               if(B[k][p]==B[k-1][p+1] and B[k-1][p+1]==B[k-3][p+3] and B[k-2][p+2]==" " and B[k][p]!=" "):
                       if(i==5):#take care of the edge case
                          found=True
                          x=p+2
                          break#when it finds a block, it breaks
                       else:#takes care of the other cases
                           if(B[k-1][p+2]!=" "):#checks if the box under is full
                              found=True
                              x=p+2
                              break#when it finds a block, it breaks
                           else:
                               x=-1#assign to x a sentinel value if no blocking is needed
               else:
                    x=-1#assign to x a sentinel value if no blocking is needed
            #as soon as it founds a block, it breaks out of the outer loop 
            if(found==True):
                  break
              
    
    return x

def ZeroesContinue(B):
    #this function takes in the gameboard
    #it builds three zeroes from two and four from three
    #it returns the variable var which holds one of the values:-1,0,1,2,3,4
    #0=vertical,1=left,2=right,3=left fiagonal,4=right diagonal
    found=False#creates a flag to see if something was found
    #1.vertical continue
    for j in range(0,7,1):
        for k in range(5,0,-1):#using the variable k to control the row starting point
            #checks if there are two zeroes in a row
            if(B[k][j]==B[k-1][j] and B[k][j]=="O"):
                if(B[k-2][j]==" "):
                    found=True
                    var=0
                    break
                else:
                    var=-1#assign a sentinel value if nothing was found
            else:
                var=-1#assign a sentinel value if nothing was found
        if(found==True):
            break
    #2.horizontal continue
    if(found==False):
        for i in range(5,-1,-1):
            for p in range(0,6,1):#using the variable p to control the column starting point
                if(p==0):#taking care of the first column edgecase
                   if(i==5):#taking care of the row edgecase
                       #checks if there are two zeroes in a row
                       if(B[i][p]==B[i][p+1] and B[i][p]=="O"):
                           if (B[i][p+2]==" "):
                               found=True
                               var=2
                               break
                           else:
                               var=-1#assign a sentinel value if nothing was found
                       else:
                            var=-1#assign a sentinel value if nothing was found
                   else:#taking care of the other rows
                        #checks if there are two zeroes in a row
                        if(B[i][p]==B[i][p+1] and B[i][p]=="O"):
                            if (B[i][p+2]==" " and B[i+1][p+2]!=" "):
                                found=True
                                var=2
                                break
                            else:
                                var=-1#assign a sentinel value if nothing was found
                        else:
                             var=-1#assign a sentinel value if nothing was found
                elif(p==5):#taking care of the last column edgecase
                    if(i==5):#taking care of the row edgecase
                        #checks if there are two zeroes in a row
                        if(B[i][p]==B[i][p+1] and B[i][p]=="O"):
                            if (B[i][p-1]==" "):
                                found=True
                                var=1
                                break
                            else:
                                var=-1#assign a sentinel value if nothing was found
                        else:
                             var=-1#assign a sentinel value if nothing was found
                    else:#taking care of the other rows
                         #checks if there are two zeroes in a row
                         if(B[i][p]==B[i][p+1] and B[i][p]=="O"):
                             if (B[i][p-1]==" " and B[i+1][p-1]!=" "):
                                 found=True
                                 var=1
                                 break
                             else:
                                 var=-1#assign a sentinel value if nothing was found
                         else:
                              var=-1#assign a sentinel value if nothing was found
                else:#taking care of the other columns
                     if(i==5):#taking care of the row edgecase
                         #checks if there are two zeroes in a row
                         if(B[i][p]==B[i][p+1] and B[i][p]=="O"):
                             if(B[i][p-1]==" " and B[i][p+2]==" "):
                                 found=True
                                 rand=random.randint(1,2)#chooses randomly between the two possible places
                                 var=rand
                                 break
                             elif(B[i][p-1]==" "):#checks if the box before is empty
                                 found=True
                                 var=1
                                 break
                             elif(B[i][p+2]==" "):#checks if the box after is empty
                                 found=True
                                 var=2
                                 break
                             else:
                                 var=-1#assign a sentinel value if nothing was found
                         else:
                             var=-1#assign a sentinel value if nothing was found
                     else:#takes care of the other rows
                         #checks if there are two zeroes in a row
                         if(B[i][p]==B[i][p+1] and B[i][p]=="O"):
                             if(B[i][p-1]==" " and B[i][p+2]==" " and B[i+1][p-1]!=" " and B[i+1][p+2]==" "):
                                 found=True
                                 rand=random.randint(1,2)#chooses randomly between the two possible places
                                 var=rand
                                 break
                             elif(B[i][p-1]==" " and B[i+1][p-1]!=" "):#checks if the box before is empty
                                 found=True
                                 var=1
                                 break
                             elif(B[i][p+2]==" " and B[i+1][p+2]!=" "):#checks if the box after is empty
                                 found=True
                                 var=2
                                 break
                             else:
                                 var=-1#assign a sentinel value if nothing was found
                         else:
                             var=-1#assign a sentinel value if nothing was found
            if(found==True):
                break
    #3.diagonal continue
    #3.1 major diagonal continue
    if(found==False):
        for p in range(2,7,1):
            for k in range(5,1,-1):#again, using p and k as starting points
              #check if there are two zeroes in a row
              if(B[k][p]==B[k-1][p-1] and B[k][p]=="O"):
                  if(B[k-2][p-2]==" " and B[k-1][p-2]!=" "):
                      found=True
                      var=3
                      break
                  else:
                      var=-1#assign a sentinel value if nothing was found
              else:
                  var=-1#assign a sentinel value if nothing was found
            if(found==True):
                 break
    #3.2 minor diagonals continue
    if(found==False):
        for p in range(0,5,1):
            for k in range(5,1,-1):#again, using p and k as starting points
               #check if there are two zeroes in a row
               if(B[k][p]==B[k-1][p+1] and B[k][p]=="O"):
                   if(B[k-2][p+2]==" " and B[k-1][p+2]!=" "):
                       found=True
                       var=4
                       break
                   else:
                       var=-1#assign a sentinel value if nothing was found
               else:
                  var=-1#assign a sentinel value if nothing was found
            if(found==True):
                break
    return var                 
                         

def ZeroBuilder(B):
    #this function takes in the gameboard
    #it builds on an already present zeroes instead of choosing randomly
    #it returns the variable x which stores the column
    #1.it searches the matrix for a zero
    found=False #creates a flag to keep track if it can build
    var=ZeroesContinue(B)
    print(var)
    if(var==-1):
        for i in range(5,-1,-1):
            for j in range(0,7,1):
                #it checks if there is a zero present
                if(B[i][j]=="O"):           
                    if(i==5):#taking care of the first row edgecase
                        if(j==0):#taking care of first coulmn edgecase
                            if(B[i-1][j]==" "):#checks if the box above is empty
                                found=True#a vertical build can be done
                                x=j
                                break#break as soon as it finds a build
                            elif(B[i][j+1]==" "):#looks for a right build
                                found=True#a right build can be done
                                x=j+1
                                break#break as soon as it finds a build
                            elif(B[i][j+1]!=" " and B[i-1][j+1]==" "):#looks for a right diagonal build
                                found=True#a right diagonalbuild can be done
                                x=j+1
                                break#break as soon as it finds a build
                            else:
                                x=-1#a sentinel value is assigned to x if it cannot build
                        elif(j==6):#taking care of the last column edgecase
                            if(B[i-1][j]==" "):#checks if the box above is empty
                                found=True#a vertical build can be done
                                x=j
                                break#break as soon as it finds a build
                            elif(B[i][j-1]==" "):#looks for a left build
                                found=True#a left build can be done
                                x=j-1
                                break#break as soon as it finds a build
                            elif(B[i][j-1]!=" " and B[i-1][j-1]==" "):#looks for a left diagonal build
                                found=True#a left diagonal build can be done
                                x=j-1
                                break#break as soon as it finds a build
                            else:
                                x=-1#a sentinel value is assigned to x if it cannot build
                        else:#takes care of the other column cases
                            if(B[i-1][j]==" "):#checks if the box above is empty
                                found=True#a vertical build can be done
                                x=j
                                break#break as soon as it finds a build
                            elif(B[i][j+1]==" "):#looks for a right build
                                found=True#a right build can be done
                                x=j+1
                                break#break as soon as it finds a build
                            elif(B[i][j+1]!=" " and B[i-1][j+1]==" "):#looks for a right diagonal build
                                found=True#a right diagonalbuild can be done
                                x=j+1
                                break#break as soon as it finds a build
                            elif(B[i][j-1]==" "):#looks for a left build
                                found=True#a left build can be done
                                x=j-1
                                break#break as soon as it finds a build
                            elif(B[i][j-1]!=" " and B[i-1][j-1]==" "):#looks for a left diagonal build
                                found=True#a left diagonal build can be done
                                x=j-1
                                break#break as soon as it finds a build
                            else:
                                x=-1#a sentinel value is assigned to x if it cannot build      
                    elif(i==0):#taking care of the last row edgecase
                          if(j==0):#taking care of first coulmn edgecase
                             #checks if it can do a right build
                             if(B[i][j+1]==" " and B[i+1][j+1]!=" "):
                                 found=True#a right build can be done
                                 x=j+1
                                 break#break as soon as it finds a build
                             else:
                                 x=-1#a sentinel value is assigned to x if it cannot build
                          elif(j==6):#taking care of the last column edgecase
                              #checks if it can do a left build
                              if(B[i][j-1]==" " and B[i+1][j-1]!=" "):
                                  found=True#a left build can be done
                                  x=j-1
                                  break#break as soon as it finds a build
                              else:
                                  x=-1#a sentinel value is assigned to x if it cannot build
                          else:#takes care of the other column cases
                              #checks if it can do a right build
                              if(B[i][j+1]==" " and B[i+1][j+1]!=" "):
                                  found=True#a right build can be done
                                  x=j+1
                                  break#break as soon as it finds a build
                              #checks if it can do a left build
                              elif(B[i][j-1]==" " and B[i+1][j-1]!=" "):
                                   found=True#a left build can be done
                                   x=j-1
                                   break#break as soon as it finds a build
                              else:
                                  x=-1#a sentinel value is assigned to x if it cannot build
                    else:#takes care of the other row cases
                        if(j==0):#taking care of first coulmn edgecase
                            if(B[i-1][j]==" "):#checks if the box above is empty
                                found=True#a vertical build can be done
                                x=j
                                break#break as soon as it finds a build
                            #checks if it can do a right build
                            if(B[i][j+1]==" " and B[i+1][j+1]!=" "):
                                found=True#a right build can be done
                                x=j+1
                                break#break as soon as it finds a build
                            elif(B[i][j+1]!=" " and B[i-1][j+1]==" "):#looks for a right diagonal build
                                found=True#a right diagonalbuild can be done
                                x=j+1
                                break#break as soon as it finds a build
                            else:
                                x=-1#a sentinel value is assigned to x if it cannot build
                        elif(j==6):#taking care of the last column edgecase
                            if(B[i-1][j]==" "):#checks if the box above is empty
                                found=True#a vertical build can be done
                                x=j
                                break#break as soon as it finds a build
                            #checks if a left build can be done
                            elif(B[i][j-1]==" " and B[i+1][j-1]!=" "):
                                 found=True#a left build can be done
                                 x=j-1
                                 break#break as soon as it finds a build
                            elif(B[i][j-1]!=" " and B[i-1][j-1]==" "):#looks for a left diagonal build
                                found=True#a left diagonal build can be done
                                x=j-1
                                break#break as soon as it finds a build
                            else:
                                x=-1#a sentinel value is assigned to x if it cannot build
                        else:#takes care of the other column cases
                            if(B[i-1][j]==" "):#checks if the box above is empty
                                found=True#a vertical build can be done
                                x=j
                                break#break as soon as it finds a build
                            #checks if it can do a right build
                            if(B[i][j+1]==" " and B[i+1][j+1]!=" "):
                                found=True#a right build can be done
                                x=j+1
                                break#break as soon as it finds a build
                            elif(B[i][j+1]!=" " and B[i-1][j+1]==" "):#looks for a right diagonal build
                                found=True#a right diagonalbuild can be done
                                x=j+1
                                break#break as soon as it finds a build
                            #checks if a left build can be done
                            elif(B[i][j-1]==" " and B[i+1][j-1]!=" "):
                                 found=True#a left build can be done
                                 x=j-1
                                 break#break as soon as it finds a build
                            elif(B[i][j-1]!=" " and B[i-1][j-1]==" "):#looks for a left diagonal build
                                found=True#a left diagonal build can be done
                                x=j-1
                                break#break as soon as it finds a build
                            else:
                                x=-1#a sentinel value is assigned to x if it cannot build
                else:
                    x=-1#a sentinel value is assigned to x if it cannot build
            if(found==True):
                    break
    else:
        for i in range(5,-1,-1):
            for j in range(0,7,1):
                #it checks if there is a zero present
                if(B[i][j]=="O"):           
                    if(i==5):#taking care of the first row edgecase
                        if(j==0):#taking care of first coulmn edgecase
                            if(B[i-1][j]==" " and var==0):#checks if the box above is empty
                                found=True#a vertical build can be done
                                x=j
                                break#break as soon as it finds a build
                            elif(B[i][j+1]==" " and var==2):#looks for a right build
                                found=True#a right build can be done
                                x=j+1
                                break#break as soon as it finds a build
                            elif(B[i][j+1]!=" " and B[i-1][j+1]==" " and var==4):#looks for a right diagonal build
                                found=True#a right diagonalbuild can be done
                                x=j+1
                                break#break as soon as it finds a build
                            else:
                                x=-1#a sentinel value is assigned to x if it cannot build
                        elif(j==6):#taking care of the last column edgecase
                            if(B[i-1][j]==" " and var==0):#checks if the box above is empty
                                found=True#a vertical build can be done
                                x=j
                                break#break as soon as it finds a build
                            elif(B[i][j-1]==" " and var==1):#looks for a left build
                                found=True#a left build can be done
                                x=j-1
                                break#break as soon as it finds a build
                            elif(B[i][j-1]!=" " and B[i-1][j-1]==" " and var==3):#looks for a left diagonal build
                                found=True#a left diagonal build can be done
                                x=j-1
                                break#break as soon as it finds a build
                            else:
                                x=-1#a sentinel value is assigned to x if it cannot build
                        else:#takes care of the other column cases
                            if(B[i-1][j]==" " and var==0):#checks if the box above is empty
                                found=True#a vertical build can be done
                                x=j
                                break#break as soon as it finds a build
                            elif(B[i][j+1]==" " and var==2):#looks for a right build
                                found=True#a right build can be done
                                x=j+1
                                break#break as soon as it finds a build
                            elif(B[i][j+1]!=" " and B[i-1][j+1]==" " and var==4):#looks for a right diagonal build
                                found=True#a right diagonalbuild can be done
                                x=j+1
                                break#break as soon as it finds a build
                            elif(B[i][j-1]==" " and var==1):#looks for a left build
                                found=True#a left build can be done
                                x=j-1
                                break#break as soon as it finds a build
                            elif(B[i][j-1]!=" " and B[i-1][j-1]==" " and var==3):#looks for a left diagonal build
                                found=True#a left diagonal build can be done
                                x=j-1
                                break#break as soon as it finds a build
                            else:
                                x=-1#a sentinel value is assigned to x if it cannot build      
                    elif(i==0):#taking care of the last row edgecase
                          if(j==0):#taking care of first coulmn edgecase
                             #checks if it can do a right build
                             if(B[i][j+1]==" " and B[i+1][j+1]!=" " and var==2):
                                 found=True#a right build can be done
                                 x=j+1
                                 break#break as soon as it finds a build
                             else:
                                 x=-1#a sentinel value is assigned to x if it cannot build
                          elif(j==6):#taking care of the last column edgecase
                              #checks if it can do a left build
                              if(B[i][j-1]==" " and B[i+1][j-1]!=" " and var==1):
                                  found=True#a left build can be done
                                  x=j-1
                                  break#break as soon as it finds a build
                              else:
                                  x=-1#a sentinel value is assigned to x if it cannot build
                          else:#takes care of the other column cases
                              #checks if it can do a right build
                              if(B[i][j+1]==" " and B[i+1][j+1]!=" " and var==2):
                                  found=True#a right build can be done
                                  x=j+1
                                  break#break as soon as it finds a build
                              #checks if it can do a left build
                              elif(B[i][j-1]==" " and B[i+1][j-1]!=" " and var==1):
                                   found=True#a left build can be done
                                   x=j-1
                                   break#break as soon as it finds a build
                              else:
                                  x=-1#a sentinel value is assigned to x if it cannot build
                    else:#takes care of the other row cases
                        if(j==0):#taking care of first coulmn edgecase
                            if(B[i-1][j]==" " and var==0):#checks if the box above is empty
                                found=True#a vertical build can be done
                                x=j
                                break#break as soon as it finds a build
                            #checks if it can do a right build
                            if(B[i][j+1]==" " and B[i+1][j+1]!=" " and var==2):
                                found=True#a right build can be done
                                x=j+1
                                break#break as soon as it finds a build
                            elif(B[i][j+1]!=" " and B[i-1][j+1]==" " and var==4):#looks for a right diagonal build
                                found=True#a right diagonalbuild can be done
                                x=j+1
                                break#break as soon as it finds a build
                            else:
                                x=-1#a sentinel value is assigned to x if it cannot build
                        elif(j==6):#taking care of the last column edgecase
                            if(B[i-1][j]==" " and var==0):#checks if the box above is empty
                                found=True#a vertical build can be done
                                x=j
                                break#break as soon as it finds a build
                            #checks if a left build can be done
                            elif(B[i][j-1]==" " and B[i+1][j-1]!=" " and var==1):
                                 found=True#a left build can be done
                                 x=j-1
                                 break#break as soon as it finds a build
                            elif(B[i][j-1]!=" " and B[i-1][j-1]==" " and var==3):#looks for a left diagonal build
                                found=True#a left diagonal build can be done
                                x=j-1
                                break#break as soon as it finds a build
                            else:
                                x=-1#a sentinel value is assigned to x if it cannot build
                        else:#takes care of the other column cases
                            if(B[i-1][j]==" " and var==0):#checks if the box above is empty
                                found=True#a vertical build can be done
                                x=j
                                break#break as soon as it finds a build
                            #checks if it can do a right build
                            if(B[i][j+1]==" " and B[i+1][j+1]!=" " and var==2):
                                found=True#a right build can be done
                                x=j+1
                                break#break as soon as it finds a build
                            elif(B[i][j+1]!=" " and B[i-1][j+1]==" " and var==4):#looks for a right diagonal build
                                found=True#a right diagonalbuild can be done
                                x=j+1
                                break#break as soon as it finds a build
                            #checks if a left build can be done
                            elif(B[i][j-1]==" " and B[i+1][j-1]!=" " and var==1):
                                 found=True#a left build can be done
                                 x=j-1
                                 break#break as soon as it finds a build
                            elif(B[i][j-1]!=" " and B[i-1][j-1]==" " and var==3):#looks for a left diagonal build
                                found=True#a left diagonal build can be done
                                x=j-1
                                break#break as soon as it finds a build
                            else:
                                x=-1#a sentinel value is assigned to x if it cannot build
                else:
                    x=-1#a sentinel value is assigned to x if it cannot build
            if(found==True):
                    break
    return x
        
                        

#-----------MAIN FUNCTION-------------------------------                        
def main():
    #creates the gameboard which is a matrix
    gameBoard=[0]*6
    for i in range(6):
        gameBoard[i]=[" "]*7#copying element by element
    displayBoard(gameBoard)#displays the gameboard on the screen
    print("------------------------------")
    print("Your choices are:")
    print("1.No")
    print("2.Yes")
    print("------------------------------")
    undo_choice=int(input("Do you want to be able to undo your moves during the game?(1/2):"))
    #it starts the game itself
    while(True):#creates an infinite loop for the game
        K=StoreBoardState(gameBoard)#saves the state of gamboard before the turns begin    
        turn=0#this variable holds the turn, it is used to trigger different
        #actions when it's the player's turn
        #The player's turn
        x=int(input("Enter the column:"))#asks the player for the column
        x=ColumnReassign(gameBoard,x,turn)#it reassigns it if it's full
        r0=rowPlacement(gameBoard,x,turn)#finds the row index of the box that should be filled
        gameBoard[r0][x]="X"#modifies the gambeoard by filling the right spot
        check1=checkWin(gameBoard)
        if(check1==True):#check if the player has won after making his move
            displayBoard(gameBoard)
            print("You won!")
            break
        if(checkTie(gameBoard)):#check if there is a tie after the player's move
            displayBoard(gameBoard)
            print("It's a tie!")
            break
        turn=1#The computer's turn
        z=fourBlocking(gameBoard)
        if(z!=-1):#check if the computer has to block a three-in-a row
           #the computer has to block
           r1=rowPlacement(gameBoard,z,turn)
           gameBoard[r1][z]="O"
        else:#the computer does not have to to block a three-in a row 
            w=XX_XtypeBlocking(gameBoard)
            if(w!=-1):#check if there is XX_X type trap to be blocked
               r1=rowPlacement(gameBoard,w,turn)
               gameBoard[r1][w]="O"       
            else:#the computer does not have to block so it tries to build
                build=ZeroBuilder(gameBoard)
                if(ZeroBuilder!=-1):#the computer can build zero structures
                  build=ColumnReassign(gameBoard,build,turn)
                  r1=rowPlacement(gameBoard,build,turn)
                  gameBoard[r1][build]="O"
                else:#the computer does not have to do anything so it chooses randomly
                   rand=random.randint(0,6)
                   rand=ColumnReassign(gameBoard,rand,turn)#it reassigns it if it's full
                   r1=rowPlacement(gameBoard,rand,turn)#finds the row index of the box that should be filled
                   gameBoard[r1][rand]="O"
        check2=checkWin(gameBoard)
        if(check2==True):#check if the computer has won after making his move
             displayBoard(gameBoard)
             print("You lost!")
             break 
        if(checkTie(gameBoard)):#check if there is a tie after the computer's move
             displayBoard(gameBoard)
             print("It's a tie!")
             break
        displayBoard(gameBoard)#displays the gameboard on the screen
        #printing the continue/undo menu
        if(undo_choice==2):
            print("------------------------------")
            print("Do you want to continue or to undo your action?")
            print("1.Continue")
            print("2.Undo")
            print("------------------------------")
            undo=int(input("Do you want to undo your move?:"))
            if(undo==2):#it undoes the move
                gameBoard=K#it rolls back to the state before the moves
                displayBoard(gameBoard)#displays the gameboard on the screen
            
          
#------------MAIN PROGRAM---------------------------------        
main()
