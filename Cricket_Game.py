import random
print("=============================================================================")
print("@@@@@        #      --------------------------------------       #      @@@@@")      
print(" @@@        ###     |    WELCOME TO PYTHON CRIKET GAME   |      ###      @@@ ")
print("  @        #####    --------------------------------------     #####      @  ") 
print("               Developed By: Sachin Kumar and Pratham Maan Yadav             ")
print("=============================================================================")
print()
print("---------------------The Rules Of The Game are as follows:-------------------")
print("  1.  This is a Two Player Cricket Game.")
print("  2.  You Can Press(q,w,e,a,s,d) keys to Bat.")

print("\n")
player1=input("Player 1 Your Name: ")
player2=input("Player 2 Your Name: ")
print("Its Time to Toss :)")
print(player1,"plss type Heads or Tails below..")
	
toss=int(input("Enter (0) for Heads or (1) for Tails: "))
t1=toss
if toss==0:
	print("You selected: Heads")
elif toss==1:
	print("You selected: Tails")
else:
	print("Invalid Option")
ht=random.randint(0,1)
ht1=ht
print("tossing..")
if ht==0:
	print("Final Result: Heads")
elif ht==1:
	print("Final Result: Tails")
if toss==ht:
	print("You Won!")
	print(player1,"Bat First")
else:
	print("You Lost!")
	print(player2,"Bat First")
		
score=0
SCORE=0
def over1():
	print("\n")
	global score
	print("Over 1 Ball 1")
	a1=input("Enter (q,w,e,a,s,d) to Bat: ")
	if (a1=='q'or a1=='w' or a1=='e' or a1=='a' or a1=='s' or a1=='d'):
		x1=random.randint(0,6)
		print("You Hit:",x1)
		if x1==0:
			print("Bowled!")
			print('''

   

                                
             *__       *__      :(
            -|__|-    -|__|-   
           _     _*    _   *     
          | |   | |   | |       :(
          | |   | |   | |         
          | |   | |   | |          
    :(    | |   | |   | |        
          | |   | |   | |
          | |   | |   | |
    :(   -----------------       
    
    

''')
			score=score+0
		elif x1==6:
			print('''

                6666666        *  
              66               | 
             66                  |  
             66                  *
      *      66666666666
     |       66        66
      |       66       66
     *         666666666          



''')
			score=score+6
			print("Score:",score)
		elif x1==4:
			print('''



                 44      44      *
                 44      44       |
                 44      44      |
                 4444444444       *
          *              44
         |               44
           |             44
          *                  



''')
			score=score+4
			print("Score:",score)
		else:
			score=score+x1
			print("Score:",score)
	else:
		score=score+0
		print(score)

	print("Over 1 Ball 2")
	a2=input("Enter (q,w,e,a,s,d) to Bat: ")
	if (a2=='q'or a2=='w' or a2=='e' or a2=='a' or a2=='s' or a2=='d'):
		x2=random.randint(0,6)
		print("You Hit:",x2)
		if x2==0:
			print("Bowled!")
			print('''

   

                                
             *__       *__      :(
            -|__|-    -|__|-   
           _     _*    _   *     
          | |   | |   | |       :(
          | |   | |   | |         
          | |   | |   | |          
    :(    | |   | |   | |        
          | |   | |   | |
          | |   | |   | |
    :(   -----------------       
    
    

''')
			score=score+0
		elif x2==6:
			print('''

                6666666        *  
              66               | 
             66                  |  
             66                  *
      *      66666666666
     |       66        66
      |       66       66
     *         666666666          



''')
			score=score+6
			print("Score:",score)
		elif x2==4:
			print('''



                 44      44      *
                 44      44       |
                 44      44      |
                 4444444444       *
          *              44
         |               44
           |             44
          *                  



''')
			score=score+4
			print("Score:",score)
		else:
			score=score+x2
			print("Score:",score)
	else:
		score=score+0
		print(score)
	
	print("Over 1 Ball 3")
	a3=input("Enter (q,w,e,a,s,d) to Bat: ")
	if (a3=='q'or a3=='w' or a3=='e' or a3=='a' or a3=='s' or a3=='d'):
		x3=random.randint(0,6)
		print("You Hit:",x3)
		if x3==0:
			print("Bowled!")
			print('''

   

                                
             *__       *__      :(
            -|__|-    -|__|-   
           _     _*    _   *     
          | |   | |   | |       :(
          | |   | |   | |         
          | |   | |   | |          
    :(    | |   | |   | |        
          | |   | |   | |
          | |   | |   | |
    :(   -----------------       
    
    

''')
			score=score+0
		elif x3==6:
			print('''

                6666666        *  
              66               | 
             66                  |  
             66                  *
      *      66666666666
     |       66        66
      |       66       66
     *         666666666          



''')
			score=score+6
			print("Score:",score)
		elif x3==4:
			print('''



                 44      44      *
                 44      44       |
                 44      44      |
                 4444444444       *
          *              44
         |               44
           |             44
          *                  



''')
			score=score+4
			print("Score:",score)
		else:
			score=score+x3
			print("Score:",score)
	else:
		score=score+0
		print("Score:",score)
		
	print("Over 1 Ball 4")
	a4=input("Enter (q,w,e,a,s,d) to Bat: ")
	if (a4=='q'or a4=='w' or a4=='e' or a4=='a' or a4=='s' or a4=='d'):
		x4=random.randint(0,6)
		print("You Hit:",x4)
		if x4==0:
			print("Bowled!")
			print('''

   

                                
             *__       *__      :(
            -|__|-    -|__|-   
           _     _*    _   *     
          | |   | |   | |       :(
          | |   | |   | |         
          | |   | |   | |          
    :(    | |   | |   | |        
          | |   | |   | |
          | |   | |   | |
    :(   -----------------       
    
    

''')
			score=score+0
		elif x4==6:
			print('''

                6666666        *  
              66               | 
             66                  |  
             66                  *
      *      66666666666
     |       66        66
      |       66       66
     *         666666666          



''')
			score=score+6
			print("Score:",score)
		elif x4==4:
			print('''



                 44      44      *
                 44      44       |
                 44      44      |
                 4444444444       *
          *              44
         |               44
           |             44
          *                  



''')
			score=score+4
		else:
			score=score+x4
			print("Score:",score)
	else:
		score=score+0
		print(score)
		
	print("Over 1 Ball 5")
	a5=input("Enter (q,w,e,a,s,d) to Bat: ")
	if (a5=='q'or a5=='w' or a5=='e' or a5=='a' or a5=='s' or a5=='d'):
		x5=random.randint(0,6)
		print("You Hit:",x5)
		if x5==0:
			print("Bowled!")
			print('''

   

                                
             *__       *__      :(
            -|__|-    -|__|-   
           _     _*    _   *     
          | |   | |   | |       :(
          | |   | |   | |         
          | |   | |   | |          
    :(    | |   | |   | |        
          | |   | |   | |
          | |   | |   | |
    :(   -----------------       
    
    

''')
			score=score+0
			print("Score:",score)
		elif x5==6:
			print('''

                6666666        *  
              66               | 
             66                  |  
             66                  *
      *      66666666666
     |       66        66
      |       66       66
     *         666666666          



''')
			score=score+6
		elif x5==4:
			print('''



                 44      44      *
                 44      44       |
                 44      44      |
                 4444444444       *
          *              44
         |               44
           |             44
          *                  



''')
			score=score+4
			print("Score:",score)
		else:
			score=score+x5
			print("Score:",score)
	else:
		score=score+0
		print(score)
		
	print("Over 1 Ball 6")
	a6=input("Enter (q,w,e,a,s,d) to Bat: ")
	if (a6=='q'or a6=='w' or a6=='e' or a6=='a' or a6=='s' or a6=='d'):
		x6=random.randint(0,6)
		print("You Hit:",x6)
		if x6==0:
			print("Bowled!")
			print('''

   

                                
             *__       *__      :(
            -|__|-    -|__|-   
           _     _*    _   *     
          | |   | |   | |       :(
          | |   | |   | |         
          | |   | |   | |          
    :(    | |   | |   | |        
          | |   | |   | |
          | |   | |   | |
    :(   -----------------       
    
    

''')
			score=score+0
		elif x6==6:
			print('''

                6666666        *  
              66               | 
             66                  |  
             66                  *
      *      66666666666
     |       66        66
      |       66       66
     *         666666666          



''')
			score=score+6
			print("Score:",score)
		elif x6==4:
			print('''



                 44      44      *
                 44      44       |
                 44      44      |
                 4444444444       *
          *              44
         |               44
           |             44
          *                  



''')
			score=score+4
			print("Score:",score)
		else:
			score=score+x6
			print("Score:",score)
	else:
		score=score+0
		print(score)
		
	print("\n")
	print("Total Score in 1st Over:",score)

def over2():
	print("\n")
	global score
	print("Over 2 Ball 1")
	b1=input("Enter (q,w,e,a,s,d) to Bat: ")
	if (b1=='q'or b1=='w' or b1=='e' or b1=='a' or b1=='s' or b1=='d'):
		x7=random.randint(0,6)
		print("You Hit:",x7)
		if x7==0:
			print("Bowled!")
			print('''

   

                                
             *__       *__      :(
            -|__|-    -|__|-   
           _     _*    _   *     
          | |   | |   | |       :(
          | |   | |   | |         
          | |   | |   | |          
    :(    | |   | |   | |        
          | |   | |   | |
          | |   | |   | |
    :(   -----------------       
    
    

''')
			score=score+0
		elif x7==6:
			print('''

                6666666        *  
              66               | 
             66                  |  
             66                  *
      *      66666666666
     |       66        66
      |       66       66
     *         666666666          



''')
			score=score+6
			print("Score:",score)
		elif x7==4:
			print('''



                 44      44      *
                 44      44       |
                 44      44      |
                 4444444444       *
          *              44
         |               44
           |             44
          *                  



''')
			score=score+4
			print("Score:",score)
		else:
			score=score+x7
			print("Score:",score)
	else:
		score=score+0
		print(score)

	print("Over 2 Ball 2")
	b2=input("Enter (q,w,e,a,s,d) to Bat: ")
	if (b2=='q'or b2=='w' or b2=='e' or b2=='a' or b2=='s' or b2=='d'):
		x8=random.randint(0,6)
		print("You Hit:",x8)
		if x8==0:
			print("Bowled!")
			print('''

   

                                
             *__       *__      :(
            -|__|-    -|__|-   
           _     _*    _   *     
          | |   | |   | |       :(
          | |   | |   | |         
          | |   | |   | |          
    :(    | |   | |   | |        
          | |   | |   | |
          | |   | |   | |
    :(   -----------------       
    
    

''')
			score=score+0
		elif x8==6:
			print('''

                6666666        *  
              66               | 
             66                  |  
             66                  *
      *      66666666666
     |       66        66
      |       66       66
     *         666666666          



''')
			score=score+6
			print("Score:",score)
		elif x8==4:
			print('''



                 44      44      *
                 44      44       |
                 44      44      |
                 4444444444       *
          *              44
         |               44
           |             44
          *                  



''')
			score=score+4
			print("Score:",score)
		else:
			score=score+x8
			print("Score:",score)
	else:
		score=score+0
		print(score)
	
	print("Over 2 Ball 3")
	b3=input("Enter (q,w,e,a,s,d) to Bat: ")
	if (b3=='q'or b3=='w' or b3=='e' or b3=='a' or b3=='s' or b3=='d'):
		x9=random.randint(0,6)
		print("You Hit:",x9)
		if x9==0:
			print("Bowled!")
			print('''

   

                                
             *__       *__      :(
            -|__|-    -|__|-   
           _     _*    _   *     
          | |   | |   | |       :(
          | |   | |   | |         
          | |   | |   | |          
    :(    | |   | |   | |        
          | |   | |   | |
          | |   | |   | |
    :(   -----------------       
    
    

''')
			score=score+0
		elif x9==6:
			print('''

                6666666        *  
              66               | 
             66                  |  
             66                  *
      *      66666666666
     |       66        66
      |       66       66
     *         666666666          



''')
			score=score+6
			print("Score:",score)
		elif x9==4:
			print('''



                 44      44      *
                 44      44       |
                 44      44      |
                 4444444444       *
          *              44
         |               44
           |             44
          *                  



''')
			score=score+4
			print("Score:",score)
		else:
			score=score+x9
			print("Score:",score)
	else:
		score=score+0
		print("Score:",score)
		
	print("Over 2 Ball 4")
	b4=input("Enter (q,w,e,a,s,d) to Bat: ")
	if (b4=='q'or b4=='w' or b4=='e' or b4=='a' or b4=='s' or b4=='d'):
		xq=random.randint(0,6)
		print("You Hit:",xq)
		if xq==0:
			print("Bowled!")
			print('''

   

                                
             *__       *__      :(
            -|__|-    -|__|-   
           _     _*    _   *     
          | |   | |   | |       :(
          | |   | |   | |         
          | |   | |   | |          
    :(    | |   | |   | |        
          | |   | |   | |
          | |   | |   | |
    :(   -----------------       
    
    

''')
			score=score+0
		elif xq==6:
			print('''

                6666666        *  
              66               | 
             66                  |  
             66                  *
      *      66666666666
     |       66        66
      |       66       66
     *         666666666          



''')
			score=score+6
			print("Score:",score)
		elif xq==4:
			print('''



                 44      44      *
                 44      44       |
                 44      44      |
                 4444444444       *
          *              44
         |               44
           |             44
          *                  



''')
			score=score+4
		else:
			score=score+xq
			print("Score:",score)
	else:
		score=score+0
		print(score)
		
	print("Over 2 Ball 5")
	b5=input("Enter (q,w,e,a,s,d) to Bat: ")
	if (b5=='q'or b5=='w' or b5=='e' or b5=='a' or b5=='s' or b5=='d'):
		xw=random.randint(0,6)
		print("You Hit:",xw)
		if xw==0:
			print("Bowled!")
			print('''

   

                                
             *__       *__      :(
            -|__|-    -|__|-   
           _     _*    _   *     
          | |   | |   | |       :(
          | |   | |   | |         
          | |   | |   | |          
    :(    | |   | |   | |        
          | |   | |   | |
          | |   | |   | |
    :(   -----------------       
    
    

''')
			score=score+0
			print("Score:",score)
		elif xw==6:
			print('''

                6666666        *  
              66               | 
             66                  |  
             66                  *
      *      66666666666
     |       66        66
      |       66       66
     *         666666666          



''')
			score=score+6
		elif xw==4:
			print('''



                 44      44      *
                 44      44       |
                 44      44      |
                 4444444444       *
          *              44
         |               44
           |             44
          *                  



''')
			score=score+4
			print("Score:",score)
		else:
			score=score+xw
			print("Score:",score)
	else:
		score=score+0
		print(score)
		
	print("Over 2 Ball 6")
	b6=input("Enter (q,w,e,a,s,d) to Bat: ")
	if (b6=='q'or b6=='w' or b6=='e' or b6=='a' or b6=='s' or b6=='d'):
		xw=random.randint(0,6)
		print("You Hit:",xw)
		if xw==0:
			print("Bowled!")
			print('''

   

                                
             *__       *__      :(
            -|__|-    -|__|-   
           _     _*    _   *     
          | |   | |   | |       :(
          | |   | |   | |         
          | |   | |   | |          
    :(    | |   | |   | |        
          | |   | |   | |
          | |   | |   | |
    :(   -----------------       
    
    

''')
			score=score+0
		elif xw==6:
			print('''

                6666666        *  
              66               | 
             66                  |  
             66                  *
      *      66666666666
     |       66        66
      |       66       66
     *         666666666          



''')
			score=score+6
			print("Score:",score)
		elif xw==4:
			print('''



                 44      44      *
                 44      44       |
                 44      44      |
                 4444444444       *
          *              44
         |               44
           |             44
          *                  



''')
			score=score+4
			print("Score:",score)
		else:
			score=score+xw
			print("Score:",score)
	else:
		score=score+0
		print(score)
		
	print("\n")
	print("Total Score in 2nd Over:",score)

def OVER1():
	print("\n")
	global SCORE
	print("Over 1 Ball 1")
	c1=input("Enter (q,w,e,a,s,d) to Bat: ")
	if (c1=='q'or c1=='w' or c1=='e' or c1=='a' or c1=='s' or c1=='d'):
		xp=random.randint(0,6)
		print("You Hit:",xp)
		if xp==0:
			print("Bowled!")
			print('''

   

                                
             *__       *__      :(
            -|__|-    -|__|-   
           _     _*    _   *     
          | |   | |   | |       :(
          | |   | |   | |         
          | |   | |   | |          
    :(    | |   | |   | |        
          | |   | |   | |
          | |   | |   | |
    :(   -----------------       
    
    

''')
			SCORE=SCORE+0
		elif xp==6:
			print('''

                6666666        *  
              66               | 
             66                  |  
             66                  *
      *      66666666666
     |       66        66
      |       66       66
     *         666666666          



''')
			SCORE=SCORE+6
			print("Score:",SCORE)
		elif xp==4:
			print('''



                 44      44      *
                 44      44       |
                 44      44      |
                 4444444444       *
          *              44
         |               44
           |             44
          *                  



''')
			SCORE=SCORE+4
			print("Score:",SCORE)
		else:
			SCORE=SCORE+xp
			print("Score:",SCORE)
	else:
		SCORE=SCORE+0
		print(SCORE)

	print("Over 1 Ball 2")
	c2=input("Enter (q,w,e,a,s,d) to Bat: ")
	if (c2=='q'or c2=='w' or c2=='e' or c2=='a' or c2=='s' or c2=='d'):
		xo=random.randint(0,6)
		print("You Hit:",xo)
		if xo==0:
			print("Bowled!")
			print('''

   

                                
             *__       *__      :(
            -|__|-    -|__|-   
           _     _*    _   *     
          | |   | |   | |       :(
          | |   | |   | |         
          | |   | |   | |          
    :(    | |   | |   | |        
          | |   | |   | |
          | |   | |   | |
    :(   -----------------       
    
    

''')
			SCORE=SCORE+0
		elif xo==6:
			print('''

                6666666        *  
              66               | 
             66                  |  
             66                  *
      *      66666666666
     |       66        66
      |       66       66
     *         666666666          



''')
			SCORE=SCORE+6
			print("Score:",SCORE)
		elif xo==4:
			print('''



                 44      44      *
                 44      44       |
                 44      44      |
                 4444444444       *
          *              44
         |               44
           |             44
          *                  



''')
			SCORE=SCORE+4
			print("Score:",SCORE)
		else:
			SCORE=SCORE+xo
			print("Score:",SCORE)
	else:
		SCORE=SCORE+0
		print(SCORE)
	
	print("Over 1 Ball 3")
	c3=input("Enter (q,w,e,a,s,d) to Bat: ")
	if (c3=='q'or c3=='w' or c3=='e' or c3=='a' or c3=='s' or c3=='d'):
		xi=random.randint(0,6)
		print("You Hit:",xi)
		if xi==0:
			print("Bowled!")
			print('''

   

                                
             *__       *__      :(
            -|__|-    -|__|-   
           _     _*    _   *     
          | |   | |   | |       :(
          | |   | |   | |         
          | |   | |   | |          
    :(    | |   | |   | |        
          | |   | |   | |
          | |   | |   | |
    :(   -----------------       
    
    

''')
			SCORE=SCORE+0
		elif xi==6:
			print('''

                6666666        *  
              66               | 
             66                  |  
             66                  *
      *      66666666666
     |       66        66
      |       66       66
     *         666666666          



''')
			SCORE=SCORE+6
			print("Score:",SCORE)
		elif xi==4:
			print('''



                 44      44      *
                 44      44       |
                 44      44      |
                 4444444444       *
          *              44
         |               44
           |             44
          *                  



''')
			SCORE=SCORE+4
			print("Score:",SCORE)
		else:
			SCORE=SCORE+xi
			print("Score:",SCORE)
	else:
		SCORE=SCORE+0
		print("Score:",SCORE)
		
	print("Over 1 Ball 4")
	c4=input("Enter (q,w,e,a,s,d) to Bat: ")
	if (c4=='q'or c4=='w' or c4=='e' or c4=='a' or c4=='s' or c4=='d'):
		xu=random.randint(0,6)
		print("You Hit:",xu)
		if xu==0:
			print("Bowled!")
			print('''

   

                                
             *__       *__      :(
            -|__|-    -|__|-   
           _     _*    _   *     
          | |   | |   | |       :(
          | |   | |   | |         
          | |   | |   | |          
    :(    | |   | |   | |        
          | |   | |   | |
          | |   | |   | |
    :(   -----------------       
    
    

''')
			SCORE=SCORE+0
		elif xu==6:
			print('''

                6666666        *  
              66               | 
             66                  |  
             66                  *
      *      66666666666
     |       66        66
      |       66       66
     *         666666666          



''')
			SCORE=SCORE+6
			print("Score:",SCORE)
		elif xu==4:
			print('''



                 44      44      *
                 44      44       |
                 44      44      |
                 4444444444       *
          *              44
         |               44
           |             44
          *                  



''')
			SCORE=SCORE+4
		else:
			SCORE=SCORE+xu
			print("Score:",SCORE)
	else:
		SCORE=SCORE+0
		print(SCORE)
		
	print("Over 1 Ball 5")
	c5=input("Enter (q,w,e,a,s,d) to Bat: ")
	if (c5=='q'or c5=='w' or c5=='e' or c5=='a' or c5=='s' or c5=='d'):
		xy=random.randint(0,6)
		print("You Hit:",xy)
		if xy==0:
			print("Bowled!")
			print('''

   

                                
             *__       *__      :(
            -|__|-    -|__|-   
           _     _*    _   *     
          | |   | |   | |       :(
          | |   | |   | |         
          | |   | |   | |          
    :(    | |   | |   | |        
          | |   | |   | |
          | |   | |   | |
    :(   -----------------       
    
    

''')
			SCORE=SCORE+0
			print("Score:",SCORE)
		elif xy==6:
			print('''

                6666666        *  
              66               | 
             66                  |  
             66                  *
      *      66666666666
     |       66        66
      |       66       66
     *         666666666          



''')
			SCORE=SCORE+6
		elif xy==4:
			print('''



                 44      44      *
                 44      44       |
                 44      44      |
                 4444444444       *
          *              44
         |               44
           |             44
          *                  



''')
			SCORE=SCORE+4
			print("Score:",SCORE)
		else:
			SCORE=SCORE+xy
			print("Score:",SCORE)
	else:
		SCORE=SCORE+0
		print(SCORE)
		
	print("Over 1 Ball 6")
	c6=input("Enter (q,w,e,a,s,d) to Bat: ")
	if (c6=='q'or c6=='w' or c6=='e' or c6=='a' or c6=='s' or c6=='d'):
		xt=random.randint(0,6)
		print("You Hit:",xt)
		if xt==0:
			print("Bowled!")
			print('''

   

                                
             *__       *__      :(
            -|__|-    -|__|-   
           _     _*    _   *     
          | |   | |   | |       :(
          | |   | |   | |         
          | |   | |   | |          
    :(    | |   | |   | |        
          | |   | |   | |
          | |   | |   | |
    :(   -----------------       
    
    

''')
			SCORE=SCORE+0
		elif xt==6:
			print('''

                6666666        *  
              66               | 
             66                  |  
             66                  *
      *      66666666666
     |       66        66
      |       66       66
     *         666666666          



''')
			SCORE=SCORE+6
			print("Score:",SCORE)
		elif xt==4:
			print('''



                 44      44      *
                 44      44       |
                 44      44      |
                 4444444444       *
          *              44
         |               44
           |             44
          *                  



''')
			SCORE=SCORE+4
			print("Score:",SCORE)
		else:
			SCORE=SCORE+xt
			print("Score:",SCORE)
	else:
		SCORE=SCORE+0
		print(SCORE)
		
	print("\n")
	print("Total Score in 1st Over:",score)

def OVER2():
	print("\n")
	global SCORE
	print("Over 2 Ball 1")
	d1=input("Enter (q,w,e,a,s,d) to Bat: ")
	if (d1=='q'or d1=='w' or d1=='e' or d1=='a' or d1=='s' or d1=='d'):
		xl=random.randint(0,6)
		print("You Hit:",xl)
		if xl==0:
			print("Bowled!")
			print('''

   

                                
             *__       *__      :(
            -|__|-    -|__|-   
           _     _*    _   *     
          | |   | |   | |       :(
          | |   | |   | |         
          | |   | |   | |          
    :(    | |   | |   | |        
          | |   | |   | |
          | |   | |   | |
    :(   -----------------       
    
    

''')
			SCORE=SCORE+0
		elif xl==6:
			print('''

                6666666        *  
              66               | 
             66                  |  
             66                  *
      *      66666666666
     |       66        66
      |       66       66
     *         666666666          



''')
			SCORE=SCORE+6
			print("Score:",SCORE)
		elif xl==4:
			print('''



                 44      44      *
                 44      44       |
                 44      44      |
                 4444444444       *
          *              44
         |               44
           |             44
          *                  



''')
			SCORE=SCORE+4
			print("Score:",SCORE)
		else:
			SCORE=SCORE+xl
			print("Score:",SCORE)
	else:
		SCORE=SCORE+0
		print(SCORE)

	print("Over 2 Ball 2")
	d2=input("Enter (q,w,e,a,s,d) to Bat: ")
	if (d2=='q'or d2=='w' or d2=='e' or d2=='a' or d2=='s' or d2=='d'):
		xk=random.randint(0,6)
		print("You Hit:",xk)
		if xk==0:
			print("Bowled!")
			print('''

   

                                
             *__       *__      :(
            -|__|-    -|__|-   
           _     _*    _   *     
          | |   | |   | |       :(
          | |   | |   | |         
          | |   | |   | |          
    :(    | |   | |   | |        
          | |   | |   | |
          | |   | |   | |
    :(   -----------------       
    
    

''')
			SCORE=SCORE+0
		elif xk==6:
			print('''

                6666666        *  
              66               | 
             66                  |  
             66                  *
      *      66666666666
     |       66        66
      |       66       66
     *         666666666          



''')
			SCORE=SCORE+6
			print("Score:",SCORE)
		elif xk==4:
			print('''



                 44      44      *
                 44      44       |
                 44      44      |
                 4444444444       *
          *              44
         |               44
           |             44
          *                  



''')
			SCORE=SCORE+4
			print("Score:",SCORE)
		else:
			SCORE=SCORE+xk
			print("Score:",SCORE)
	else:
		SCORE=SCORE+0
		print(SCORE)
	
	print("Over 2 Ball 3")
	d3=input("Enter (q,w,e,a,s,d) to Bat: ")
	if (d3=='q'or d3=='w' or d3=='e' or d3=='a' or d3=='s' or d3=='d'):
		xj=random.randint(0,6)
		print("You Hit:",xj)
		if xj==0:
			print("Bowled!")
			print('''

   

                                
             *__       *__      :(
            -|__|-    -|__|-   
           _     _*    _   *     
          | |   | |   | |       :(
          | |   | |   | |         
          | |   | |   | |          
    :(    | |   | |   | |        
          | |   | |   | |
          | |   | |   | |
    :(   -----------------       
    
    

''')
			SCORE=SCORE+0
		elif xj==6:
			print('''

                6666666        *  
              66               | 
             66                  |  
             66                  *
      *      66666666666
     |       66        66
      |       66       66
     *         666666666          



''')
			SCORE=SCORE+6
			print("Score:",SCORE)
		elif xj==4:
			print('''



                 44      44      *
                 44      44       |
                 44      44      |
                 4444444444       *
          *              44
         |               44
           |             44
          *                  



''')
			SCORE=SCORE+4
			print("Score:",SCORE)
		else:
			SCORE=SCORE+xj
			print("Score:",SCORE)
	else:
		SCORE=SCORE+0
		print("Score:",SCORE)
		
	print("Over 2 Ball 4")
	d4=input("Enter (q,w,e,a,s,d) to Bat: ")
	if (d4=='q'or d4=='w' or d4=='e' or d4=='a' or d4=='s' or d4=='d'):
		xh=random.randint(0,6)
		print("You Hit:",xh)
		if xh==0:
			print("Bowled!")
			print('''

   

                                
             *__       *__      :(
            -|__|-    -|__|-   
           _     _*    _   *     
          | |   | |   | |       :(
          | |   | |   | |         
          | |   | |   | |          
    :(    | |   | |   | |        
          | |   | |   | |
          | |   | |   | |
    :(   -----------------       
    
    

''')
			SCORE=SCORE+0
		elif xh==6:
			print('''

                6666666        *  
              66               | 
             66                  |  
             66                  *
      *      66666666666
     |       66        66
      |       66       66
     *         666666666          



''')
			SCORE=SCORE+6
			print("Score:",SCORE)
		elif xh==4:
			print('''



                 44      44      *
                 44      44       |
                 44      44      |
                 4444444444       *
          *              44
         |               44
           |             44
          *                  



''')
			SCORE=SCORE+4
		else:
			SCORE=SCORE+xh
			print("Score:",SCORE)
	else:
		SCORE=SCORE+0
		print(SCORE)
		
	print("Over 2 Ball 5")
	d5=input("Enter (q,w,e,a,s,d) to Bat: ")
	if (d5=='q'or d5=='w' or d5=='e' or d5=='a' or d5=='s' or d5=='d'):
		xg=random.randint(0,6)
		print("You Hit:",xg)
		if xg==0:
			print("Bowled!")
			print('''

   

                                
             *__       *__      :(
            -|__|-    -|__|-   
           _     _*    _   *     
          | |   | |   | |       :(
          | |   | |   | |         
          | |   | |   | |          
    :(    | |   | |   | |        
          | |   | |   | |
          | |   | |   | |
    :(   -----------------       
    
    

''')
			SCORE=SCORE+0
			print("Score:",SCORE)
		elif xg==6:
			print('''

                6666666        *  
              66               | 
             66                  |  
             66                  *
      *      66666666666
     |       66        66
      |       66       66
     *         666666666          



''')
			SCORE=SCORE+6
		elif xg==4:
			print('''



                 44      44      *
                 44      44       |
                 44      44      |
                 4444444444       *
          *              44
         |               44
           |             44
          *                  



''')
			SCORE=SCORE+4
			print("Score:",SCORE)
		else:
			SCORE=SCORE+xg
			print("Score:",SCORE)
	else:
		SCORE=SCORE+0
		print(SCORE)
		
	print("Over 2 Ball 6")
	d6=input("Enter (q,w,e,a,s,d) to Bat: ")
	if (d6=='q'or d6=='w' or d6=='e' or d6=='a' or d6=='s' or d6=='d'):
		xf=random.randint(0,6)
		print("You Hit:",xf)
		if xf==0:
			print("Bowled!")
			print('''

   

                                
             *__       *__      :(
            -|__|-    -|__|-   
           _     _*    _   *     
          | |   | |   | |       :(
          | |   | |   | |         
          | |   | |   | |          
    :(    | |   | |   | |        
          | |   | |   | |
          | |   | |   | |
    :(   -----------------       
    
    

''')
			SCORE=SCORE+0
		elif xf==6:
			print('''

                6666666        *  
              66               | 
             66                  |  
             66                  *
      *      66666666666
     |       66        66
      |       66       66
     *         666666666          



''')
			SCORE=SCORE+6
			print("Score:",SCORE)
		elif xf==4:
			print('''



                 44      44      *
                 44      44       |
                 44      44      |
                 4444444444       *
          *              44
         |               44
           |             44
          *                  



''')
			SCORE=SCORE+4
			print("Score:",SCORE)
		else:
			SCORE=SCORE+xf
			print("Score:",SCORE)
	else:
		SCORE=SCORE+0
		print(SCORE)
		
	print("\n")
	print("Total Score in 2nd Over:",SCORE)

over1()
over2()
print("First Inning Over!")
print("Total Score in First Inning:",score)
OVER1()
OVER2()
print("Second Inning Over!")	
print("Total Score in Second Inning:",SCORE)
print("\n")
print("Total Score in First Inning:",score)
print("Total Score in Second Inning:",SCORE)

if t1==ht1:
    if(score>SCORE):
          print(player1,"Won!")
    elif(SCORE>score):
          print(player2,"Won!")       
    elif(SCORE==score):
          print("Match Tie! ;)")
else:
    print("")
    
#Trophy
print("                                 ")
print("      @ @ @ @ @ @ @ @ @ @ @      ")
print("       @                 @       ")
print("    @@@@@    WINNER!    @@@@@    ")
print("    @   @    WINNER!    @   @    ")
print("    @   @               @   @    ")
print("    @   @    Congo!!    @   @    ")
print("     @@@@@@           @@@@@@     ")
print("            @ @   @ @            ")
print("              @   @              ")
print("              @   @              ")
print("            @ @   @ @            ")
print("      @ @ @           @ @ @      ")
print("      @ @ @ @ @ @ @ @ @ @ @      ")
