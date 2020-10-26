import datetime

bookname=[]

authorname=[]

quantity=[]

cost=[]

def getDate():
    
    now=datetime.datetime.now
    
    return str(now().date())


def getTime():
    
    now=datetime.datetime.now
    
    return str(now().time())


while True:
    
        print('1. Display available books')
        
        print('2. Add a book')
        
        print('3. Borrow a book')
        
        print('4. Return a book')
        
        print('5. Exit')
        
        try:
            
            a=int(input("What would you like to do?"))
            
            if a==1:
                
                f=open("Stock.txt","r")
                
                lines=f.read()
                
                print(lines)
                
            elif a==2:
                
                bname=input('Enter name of book: ')
                
                aname=input('Enter name of author: ')
                
                quant=input('Enter quantity: ')
                
                cost=input('Enter cost of book(in dollars): ')
                
                f=open("Stock.txt","a")
                
                f.write(bname+','+aname+','+quant+','+'$'+cost)
                
                print('Record added')
                
            elif a==3:
                
                    
                firstName=input("Enter the first name of the borrower: ")
                    
                lastName=input("Enter the last name of the borrower: ")
                    
                t="Borrowed_by:"+firstName+".txt"
                
                with open(t,"w+") as f:
                    
                    f.write("               Library Management System  \n")
                    
                    f.write("                   Borrowed By: "+ firstName+" "+lastName+"\n")
                    
                    f.write("    Date: " + getDate()+"    Time:"+ getTime()+"\n\n")
                    
                    f.write("S.N. \t\t Bookname \t      Authorname \n" )
                success=True
                while success==False:
                    
                    print("Please select a option below:")
                    
                    with open("stock.txt","r") as f:
 
                        lines=f.readlines()
                        
                        lines=[x.strip('\n') for x in lines]
                        
                        for i in range(len(lines)):
                            
                            ind=0
                            
                            for a in lines[i].split(','):
                                
                                if(ind==0):
                                    
                                    bookname.append(a)
                                    
                                elif(ind==1):
                                    
                                    authorname.append(a)
                                    
                                elif(ind==2):
                                    
                                    quantity.append(a)
                                    
                                elif(ind==3):
                                    
                                    cost.append(a.strip("$"))
                                    
                                ind+=1
                                
                        print(f.readlines())
                        
                    for i in range(len(bookname)):
                        
                        print("Enter", i, "to borrow book", bookname[i])
                        
                
                    try:
                        
                        a=int(input())
                        
                        try:
                            
                            if(int(quantity[a])>0):
                                
                                print("Book is available")
                                
                                with open(t,"a") as f:
                                    
                                    f.write("1. \t\t"+ bookname[a]+"\t\t  "+authorname[a]+"\n")
                                    

                                quantity[a]=int(quantity[a])-1
                                
                                with open("Stock.txt","w+") as f:
                                    
                                    for i in range(3):
                                        
                                        f.write(bookname[i]+","+authorname[i]+","+str(quantity[i])+","+"$"+cost[i]+"\n")
                                        
                                loop=True
                                
                                count=1

                            
                                while loop==True:
                                    
                                    choice=str(input("Do you want to borrow more books? However you cannot borrow same book twice. Press y for yes and n for no."))
                                    
                                    if(choice.upper()=="Y"):
                                        
                                        count=count+1
                                        
                                        print("Please select an option below:")
                                        
                                        for i in range(len(bookname)):
                                            
                                            print("Enter", i, "to borrow book", bookname[i])
                                            
                                        a=int(input())
                                        
                                        if(int(quantity[a])>0):
                                            
                                            print("Book is available")
                                            
                                            with open(t,"a") as f:
                                                
                                                f.write(str(count) +". \t\t"+ bookname[a]+"\t\t  "+authorname[a]+"\n")
                                                

                                            quantity[a]=int(quantity[a])-1
                                            
                                            with open("Stock.txt","w+") as f:
                                                
                                                for i in range(3):
                                                    
                                                    f.write(bookname[i]+","+authorname[i]+","+str(quantity[i])+","+"$"+cost[i]+"\n")
                                                    
                                                    success=False
                                                    
                                        else:
                                            
                                            loop=False
                                            
                                            break
                                        
                                    elif (choice.upper()=="N"):
                                        
                                        print ("Thank you for borrowing books from us. ")
                                        
                                        print("")
                                        
                                        loop=False
                                        
                                        success=True
                                        
                                    else:
                                        
                                        print("Please choose as instructed")
                                        
                                    
                            else:
                                
                                print("Book is not available")
                                
                                borrowBook()
                                
                                success=False
                                
                        except IndexError:
                            
                            print("")
                            
                            print("Please choose book acording to their number.")
                            
                    except ValueError:
                        
                        print("")
                        
                        print("Please choose as suggested.")
                        
            elif a==4:
                
                name=input("Enter name of borrower: ")
                
                a="Borrowed_by:"+name+".txt"
                
                try:
                    
                    with open(a,"r") as f:
                        
                        lines=f.readlines()
                        
                        lines=[a.strip("$") for a in lines]
                        
                
                    with open(a,"r") as f:
                        
                        data=f.read()
                        
                        print(data)
                        
                except:
                    
                    print("The borrower name is incorrect")
                    
                    returnBook()
                    

                b="Return-"+name+".txt"
                
                with open(b,"w+")as f:
                    
                    f.write("                Library Management System \n")
                    
                    f.write("                   Returned By: "+ name+"\n")
                    
                    f.write("    Date: " + getDate()+"    Time:"+ getTime()+"\n\n")
                    
                    f.write("S.N.\t\tBookname\t\tCost\n")
                    


                total=0.0
                
                print(bookname)
                
                for i in range(3):
                    
                    if bookname[i] in data:
                        
                        with open(b,"a") as f:
                            
                            f.write(str(i+1)+"\t\t"+bookname[i]+"\t\t$"+cost[i]+"\n")
                            
                            quantity[i]=int(quantity[i])+1
                            
                        total+=float(cost[i])
                        
                        
                print("\t\t\t\t\t\t\t"+"$"+str(total))
                
                print("Is the book return date expired?")
                
                print("Press Y for Yes and N for No")
                
                stat=input()
                
                if(stat.upper()=="Y"):
                    
                    print("By how many days was the book returned late?")
                    
                    day=int(input())
                    
                    fine=2*day
                    
                    with open(b,"a")as f:
                        
                        f.write("\t\t\t\t\tFine: $"+ str(fine)+"\n")
                        
                    total=total+fine
                    
                


                print("Final Total: "+ "$"+str(total))
                
                with open(b,"a")as f:
                    
                    f.write("\t\t\t\t\tTotal: $"+ str(total))
                    
                
                    
                with open("Stock.txt","w+") as f:
                    
                        for i in range(3):
                            
                            f.write(bookname[i]+","+authorname[i]+","+str(quantity[i])+","+"$"+cost[i]+"\n")
                            
            elif(a==5):
                
                print("Thank you for using library management system")
                
                break
            
            else:
                
                print("Please enter a valid choice")
                
        except ValueError:
            
            print("Please input as suggested.")
            
