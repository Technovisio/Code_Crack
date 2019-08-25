#****************************************Coffee Shop Interaction Software**********************************************
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import smtplib
from email.message import EmailMessage
import random
from random import randint
import time
import datetime as dt
import sqlite3
con=sqlite3.connect('CafeDB.db')
cur=con.cursor()

D={'COFFEE','TEA','PEPSI_REG','COKE_REG','COLD_COFFEE','COFFEE_LATTE',
   'CHOCO_MILK','ORANGILLO','MANGO_JUICE','VANILLA_SHAKE','CHOCO_SHAKE','LEMONADE',
   'AMERICANO_1_SHOT','EXPRESSO_2_SHOTS','MANGO_SHAKE','BANANA_SHAKE'}
S={'PATIES','CHOCO_PASTRY','CREAM_ROLL','CHIPS','SANDWICH_VEG','SANDWICH_NONVEG',
   'FRENCH_FRIES','CHICKEN_BURGER','VEG_BURGER','CUP_NOODLES','STUFFED_ROLL','MUFFINS','CHEESE_PIZZA','REG_PIZZA'}
P={'CHOCO_NUTS', 'CHOCO_CHIPS', 'CHOCOLATE_NUTS', 'MILK_COOKIES', 'BUTTER_COOKIES', 'SNICKERS', 'SALTED_NUTS', 'CHIPS'}

DRINKS={'COFFEE':30, 'TEA':20, 'PEPSI_REG':35, 'COKE_REG':40, 'COLD_COFFEE':50, 'COFFEE_LATTE':30, 'CHOCO_MILK':25, 'ORANGILLO':20, 'MANGO_JUICE':30,
        'VANILLA_SHAKE':40, 'CHOCO_SHAKE':30, 'LEMONADE':20, 'AMERICANO_1_SHOT':30, 'EXPRESSO_2_SHOTS':35, 'MANGO_SHAKE':40, 'BANANA_SHAKE':45}
SNACKS={'PATIES':15, 'CHOCO_PASTRY':35, 'CREAM_ROLL':20, 'SANDWICH_VEG':40, 'SANDWICH_NONVEG':60, 'FRENCH_FRIES':40,
        'CHICKEN_BURGER':50, 'CUP_NOODLES':35, 'STUFFED_ROLL':30, 'MUFFINS':20, 'CHEESE_PIZZA':79, 'REG_PIZZA':59}
CRAZY_PACKS={'CHOCO_NUTS':40, 'CHOCO_CHIPS':25, 'CHOCOLATE_NUTS':45, 'MILK_COOKIES':45, 'BUTTER_COOKIES':50, 'SNICKERS':15, 'SALTED_NUTS':30, 'CHIPS':30}

COFFEE=DRINKS['COFFEE']
TEA=DRINKS['TEA']
PEPSI_REG=DRINKS['PEPSI_REG']
COKE_REG=DRINKS['COKE_REG']
COLD_COFFEE=DRINKS['COLD_COFFEE']
COFFEE_LATTE=DRINKS['COFFEE_LATTE']
CHOCO_MILK=DRINKS['CHOCO_MILK']
ORANGILLO=DRINKS['ORANGILLO']
MANGO_JUICE=DRINKS['MANGO_JUICE']
VANILLA_SHAKE=DRINKS['VANILLA_SHAKE']
CHOCO_SHAKE=DRINKS['CHOCO_SHAKE']
LEMONADE=DRINKS['LEMONADE']
AMERICANO_1_SHOT=DRINKS['AMERICANO_1_SHOT']
EXPRESSO_2_SHOTS=DRINKS['EXPRESSO_2_SHOTS']
MANGO_SHAKE=DRINKS['MANGO_SHAKE']
BANANA_SHAKE=DRINKS['BANANA_SHAKE']
PATIES=SNACKS['PATIES']
CHOCO_PASTRY=SNACKS['CHOCO_PASTRY']
CREAM_ROLL=SNACKS['CREAM_ROLL']
SANDWICH_VEG=SNACKS['SANDWICH_VEG']
SANDWICH_NONVEG=SNACKS['SANDWICH_NONVEG']
FRENCH_FRIES=SNACKS['FRENCH_FRIES']
CHICKEN_BURGER=SNACKS['CHICKEN_BURGER']
CUP_NOODLES=SNACKS['CUP_NOODLES']
STUFFED_ROLL=SNACKS['STUFFED_ROLL']
MUFFINS=SNACKS['MUFFINS']
CHEESE_PIZZA=SNACKS['CHEESE_PIZZA']
REG_PIZZA=SNACKS['REG_PIZZA']
CHOCO_NUTS=CRAZY_PACKS['CHOCO_NUTS']
CHOCO_CHIPS=CRAZY_PACKS['CHOCO_CHIPS']
CHOCOLATE_NUTS=CRAZY_PACKS['CHOCOLATE_NUTS']
MILK_COOKIES=CRAZY_PACKS['MILK_COOKIES']
BUTTER_COOKIES=CRAZY_PACKS['BUTTER_COOKIES']
SNICKERS=CRAZY_PACKS['SNICKERS']
SALTED_NUTS=CRAZY_PACKS['SALTED_NUTS']
CHIPS=CRAZY_PACKS['CHIPS']


flag=0
quote='Always be positive, think positive!'
print("\t\t\t|_|CAFE SHOP!!\n")

while True:
    try:
        ch=input("You are User(U)\n or Admin(A) or New(N): \n\t")
        ch=ch.upper().strip()
        if ch=='A':
            print("\n\tWELCOME TO ADMIN PANEL!!\n\n")
            adname=input('Enter your name: ')                               #For admin control enter adname='ADN'
            adname=adname.upper().strip()
            if adname=='BIPUL':
                otp=list(random.sample(range(100000,999999),1))
                
                em=input("Enter your mail id: ")
                with smtplib.SMTP('smtp.gmail.com',587) as smtp:
                    smtp.ehlo()
                    smtp.starttls()
                    smtp.ehlo()
                    smtp.login('thikhai83@gmail.com', 'thikhai@123')
    
                    sub = 'Cafe Shop Verification!!'
                    body = 'Your verification Code is: G- '
                    msg = f'subject: {sub}\n\n{body}{otp}'
    
                    smtp.sendmail('thikhai83@gmail.com', em, msg)
                ver=int(input("Enter 6 digit verification code: G- "))
                if ver==otp[0] :
                    print("Welcome to Admin control! {}\n".format(adname))
                    quote=input("\n\tEnter quote for the day: ")
                    op=input("What would you want to do: \n(U)'Update' items or \n(V)'View' items or \n(E)'Exit Control': ")
                    op=op.upper().strip()
                    if op=='U':
                        upd=input('What would you want to update(\n\t1. )DRINKS(\n\t2. )SNACKS(\n\t3. )CRAZY_PACKS): ')
                        upd=upd.upper().strip()
                        if upd==1:
                            inp=input("Enter new item to be update: ")
                            inp=inp.upper().strip()
                            val=int(input("Enter new value of item: "))
                            DRINKS[inp]=val
                            locals().update(DRINKS)
                            D.add(inp)
                            print(DRINKS)
                            continue
                        elif upd==2:
                            inp=input("Enter new item to be update: ")
                            inp=inp.upper().strip()
                            val=int(input("Enter new value of item: "))
                            SNACKS[inp]=val
                            locals().update(SNACKS)
                            S.add(inp)
                            print(SNACKS)
                            continue
                        elif upd==3:
                            inp=input("Enter new item to be update: ")
                            inp=inp.upper().strip()
                            val=int(input("Enter new value of item: "))
                            SNACKS[inp]=val
                            locals().update(CRAZY_PACKS)
                            P.add(inp)
                            print(CRAZY_PACKS)
                            continue
                        else:
                            print("you can't proceed!")
                            continue
                    elif op=='V':
                        print('DRINKS','SNACKS','CRAZY_PACKS',sep='\n')
                        cu=con.execute("SELECT * FROM Transac")
                        for i in cu:
                            print(i,sep='\n\n')
                        continue
                    elif op=='E':
                        print('Exting the System...........!')
                        time.sleep(1)
                        break
                    else:
                        print("\tYou didn't opt any particular operation!!")
                        continue 
                else:
                    print("Sorry!Wrong otp!")
                    continue
            elif adname=='ADN':
                
                otp=list(random.sample(range(100000,999999),1))
                
                em=input("Enter your mail id: ")
                with smtplib.SMTP('smtp.gmail.com',587) as smtp:
                    smtp.ehlo()
                    smtp.starttls()
                    smtp.ehlo()
                    smtp.login('thikhai83@gmail.com', 'thikhai@123')
    
                    sub = 'Cafe Shop Verification!!'
                    body = 'Your verification Code is: G- '
                    msg = f'subject: {sub}\n\n{body}{otp}'
    
                    smtp.sendmail('thikhai83@gmail.com', em, msg)
                ver=int(input("Enter 6 digit verification code: G- "))
                if ver==otp[0] :
                    print("Welcome to Admin control! {}\n".format(adname))
                    quote=input("\n\tEnter quote for the day: ")
                    op=input("What would you want to do: \n(U)'Update' items or \n(V)'View' items or \n(E)'Exit Control': ")
                    op=op.upper().strip()
                    if op=='U':
                        upd=input('What would you want to update(\n\t1. )DRINKS(\n\t2. )SNACKS(\n\t3. )CRAZY_PACKS): ')
                        upd=upd.upper().strip()
                        if upd==1:
                            inp=input("Enter new item to be update: ")
                            inp=inp.upper().strip()
                            val=int(input("Enter new value of item: "))
                            DRINKS[inp]=val
                            locals().update(DRINKS)
                            D.add(inp)
                            print(DRINKS)
                            continue
                        elif upd==2:
                            inp=input("Enter new item to be update: ")
                            inp=inp.upper().strip()
                            val=int(input("Enter new value of item: "))
                            SNACKS[inp]=val
                            locals().update(SNACKS)
                            S.add(inp)
                            print(SNACKS)
                            continue
                        elif upd==3:
                            inp=input("Enter new item to be update: ")
                            inp=inp.upper().strip()
                            val=int(input("Enter new value of item: "))
                            SNACKS[inp]=val
                            locals().update(CRAZY_PACKS)
                            P.add(inp)
                            print(CRAZY_PACKS)
                            continue
                        else:
                            print("you can't proceed!")
                            continue
                    elif op=='V':
                        print('DRINKS','SNACKS','CRAZY_PACKS',sep='\n')
                        cu=con.execute("SELECT * FROM Transac")
                        for i in cu:
                            print(i,sep='\n\n')
                        continue
                    elif op=='E':
                        print('Exting the System...........!')
                        time.sleep(1)
                        break
                    else:
                        print("\tYou didn't opt any particular operation!!")
                        continue 
                else:
                    print("Sorry!Wrong otp!")
                    continue
                
            else:
                print("YOU DENIED ADMIN CONTROL!")
                continue
            continue
        elif ch=='U':
            print("Welcome User!!\n\n")
            print("\t\t\t!! Cafe Shop !!\t\t\t"+"\nMay I Help you!!\n")
            name=input("What's your name?\t")
            name=name.upper()
            print("Welcome to Cafe Shop! {0}".format(name))
            print("Quote of the day: ",quote)
            #Cost=eval(x)
            while True:
                menu=input("you wanna to see menu card Yes/No: ")
                menu=menu.upper().strip()
                if menu=='YES':
                    print(list(DRINKS.items()))
                    print("\n")
                    print(list(SNACKS.items()))
                    print("\n")
                    print(list(CRAZY_PACKS.items()))
                    print("\n")
                    break
                elif menu=='NO':
                    print('You didn\'t opt for menu card!')
                    break
                else:
                    print('Wrong Input')
                    print("Please select a valid option!!\tTry Again!")
                    continue
            while True:
                try:
                    Choice=input('What would you like to have?\n(D)for DRINKS\n(S)for SNACKS\n(P)for CRAZY_PACKS')
                    Choice=Choice.upper().strip()
                    print(Choice)
                    if Choice=='D':
                        i=input('Enter your order! ')
                        i=i.upper()
                        g=i.split(" ")
                        h=set(g)
                        t=tuple(g)
                        print(h)
                        x=i.replace(" ","+",2)
                        if set(g).intersection(D):
                            flag+=1
                            print("item is available in DRINKS !")
                            print(x+"\n",eval(x))
                            Cost=eval(x)
                            GST=(5*Cost)/100
                            Final_Price=Cost+GST
                            print("Overall Charges with GST(5%) included: ",Final_Price,"Rs/-")
                            break
                        else:
                            flag
                            print("Sorry! Please order something else from Menu Card!\nItem is not present in list!")
                            continue
                    elif Choice=='S':
                        i=input('Enter your order! ')
                        i=i.upper()
                        g=i.split(" ")
                        h=set(g)
                        t=tuple(g)
                        print(h)
                        x=i.replace(" ","+",2)
                        if set(g).intersection(S):
                            flag+=1
                            print("item is available in SNACKS !")
                            print(x+"\n",eval(x))
                            Cost=eval(x)
                            GST=(5*Cost)/100
                            Final_Price=Cost+GST
                            print("Overall Charges with GST(5%) included: ",Final_Price,"Rs/-")
                            break
                        else:
                            flag
                            print("Sorry! Please order something else from Menu Card!\nItem is not present in list!")
                            continue
                    elif Choice=='P':
                        i=input('Enter your order! ')
                        i=i.upper()
                        g=i.split(" ")
                        h=set(g)
                        t=tuple(g)
                        print(h)
                        x=i.replace(" ","+",2)
                        if set(g).intersection(P):
                            flag+=1
                            print("item is available in CRAZY_PACKS !")
                            print(x+"\n",eval(x))
                            Cost=eval(x)
                            GST=(5*Cost)/100
                            Final_Price=Cost+GST
                            print("Overall Charges with GST(5%) included: ",Final_Price,"Rs/-")
                            break
                        else:
                            flag
                            print("Sorry! Please order something else from Menu Card!\nItem is not present in list!")
                            continue
                    else:
                        flag
                        print("Sorry wrong input! Please Try anything else!")
                        continue
                except Exception as e:
                    print(e)
                    break
            
            while True:
                if flag==0:
                    break
                else:
                    print("\t\t\t !!Payment Gateway!! \t\t\t")
                    Payment_Method=input("Please enter Payment Mode: (Cash\nCoffee Bucks\nNet Banking\nPaytm\nDebit Card)\t\t")
                    Payment_Method=Payment_Method.upper().strip()
                    if Payment_Method=='CASH':
                        print("\nOverall Charges with GST(5%) included: ",Final_Price,"Rs/-")
                        Process=input("For Payment Press (Proceed) or (Cancel)")
                        Process=Process.upper().strip()
                        if Process=='PROCEED':
                            counter=randint(1,6)
                            token=randint(1,20)
                            csh=int(input('Enter the cash amount in form of paper currency(single one note at once) to pay! '))
                            if csh!=0 and csh!=10 and csh!=20 and csh!=50 and csh!=100 and csh!=200 and csh!=500 and csh!=2000 :
                                print("Enter a valid currency!!")
                                continue
                            else:
                                try:
                                    counter=randint(1,6)
                                    token=randint(1,30)
                                    if csh<Final_Price:
                                        print("Amount is less than payable!!\n")
                                        break
                                    else:
                                        change=csh-Final_Price
                                        change=int(change)
                                        time.sleep(1.5)
                                        code='ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
                                        tran=''
                                        for c in range(11):
                                            tran+=random.choice(code)
                                        print('\n\tYour transaction id: ',tran)
                                        print('\n\tPlease collect the change: ',change)
                                        print('\n\nYour token no is: {}, & Please visit Counter No.: {}'.format(token,counter))
                                        time.sleep(1.5)
                                        d=dt.datetime.now()
                                        print(d)
                                        p=input('\nDo you want to print a reciept?[Yes/No]')
                                        p=p.lower()
                                except Exception as e:
                                    print(e)
                                    break
                                if p=='yes':
                                    p=f'Cafe_{tran}.pdf'
                                    ca=canvas.Canvas(f'Cafe_{tran}.pdf',pagesize=letter)
                                    ca.setLineWidth(.3)
                                    ca.setFont('Helvetica', 11)
                                    ca.line(25,790,595,790)
                                    ca.line(25,790,25,330)
                                    ca.line(595,790,595,330)
                                    ca.drawString(435,750,"{}".format(d))
                                    ca.line(435,747,590,747)
                                    ca.drawString(30,750,'|_|CAFE SHOP!!')
                                    ca.drawString(30,735,'OF BREAK-ZONE INDUSTRIES')
                                    ca.drawString(30,705,'RECEIVED BY:')
                                    ca.drawString(120,705,":-{}".format(name))
                                    ca.line(120,700,580,700)
                                    ca.drawString(200,680, "***\t\t\tCash Memo\t\t\t***")
                                    ca.drawString(50,650, "Items Purchased: {}".format(t))
                                    ca.line(140,645,590,645)
                                    ca.drawString(50,620, "Price of Items Purchased: __________________________________")
                                    ca.drawString(445,620,":-{}".format(Cost))
                                    ca.drawString(50,595, "TAX on Items Purchased: _______________________________")
                                    ca.drawString(445,595,":-{}".format(GST))
                                    ca.drawString(50,570, "Total Price including GST(5%) on deal: _____________________________")
                                    ca.drawString(445,570,":-Rs.{}/-".format(Final_Price))
                                    ca.drawString(50,545, "Mode of Payment: _______________________________")
                                    ca.drawString(445,545,":-{}".format(Payment_Method))
                                    ca.drawString(50,520, "Your transaction id: _________________________________________")
                                    ca.drawString(445,520,":-{}".format(tran))
                                    ca.drawString(50,495, "Amount Paid by customer at counter: _______________________________")
                                    ca.drawString(445,495,":-{}".format(csh))
                                    ca.drawString(50,470, "Change returned to customer: _______________________________")
                                    ca.drawString(445,470,":-{}".format(change))
                                    ca.drawString(400,450,'Counter NO:')
                                    ca.drawString(510,450,":-{}".format(counter))
                                    ca.line(505,445,530,445)
                                    ca.drawString(400,420,'Token No:')
                                    ca.drawString(510,420,":-{}".format(token))
                                    ca.line(505,415,530,415)
                                    ca.drawString(50,390, "***\t\t\tPayment Successful!\t\t\t***")
                                    ca.drawString(200,370, "******Have a Nice DAY!******")
                                    ca.drawString(50,350, "************************************************************************************************")
                                    ca.line(25,330,595,330)
                                    ca.save()
                                    
                                    t=str(t)
                                    cur.execute("INSERT INTO Transac(customer,items,pay_method,date,transaction_id,total_price,amount_paid,change,reciept) VALUES(?,?,?,?,?,?,?,?,?)",(name,t,Payment_Method,d,tran,Final_Price,csh,change,p))
                                    con.commit()
                                    
                                    try:
                                        msg = EmailMessage()
                                        msg['Subject'] = 'Cafe Shop Invoice!!'
                                        msg['From'] = 'thikhai83@gmail.com'
                                        msg['To'] = input('Enter your Address:\t')
                                        msg.set_content('Invoice Attached......!!')
                                        
                                        files = [p]
                                        for file in files:
                                            with open(file,'rb') as f:
                                                file_data = f.read()
                                                file_name = f.name
                                            msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)
                                            break
                                        with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
                                            
                                            '''smtp.ehlo()
                                            smtp.starttls()
                                            smtp.ehlo()'''
                                            
                                            smtp.login('thikhai83@gmail.com', 'thikhai@123')
                                            
                                        
                                            smtp.send_message(msg)
                                    except Exception as e:
                                        print(e)
                                    '''cu=con.execute("SELECT * FROM Transac")
                                    for i in cu:        #Used for print data from database
                                        print(i)'''
                                        
                                elif p=='no':
                                    print('You saved paper!Well done!')
                                    t=str(t)
                                    cur.execute("INSERT INTO Transac(customer,items,pay_method,date,transaction_id,total_price,amount_paid,change,reciept) VALUES(?,?,?,?,?,?,?,?,?)",(name,t,Payment_Method,d,tran,Final_Price,csh,change,p))
                                    con.commit()
                                    '''cu=con.execute("SELECT * FROM Transac")
                                    for i in cu:
                                        print(i)'''
                                    break
                                else:
                                    print("No choice!")
                                    t=str(t)
                                    cur.execute("INSERT INTO Transac(customer,items,pay_method,date,transaction_id,total_price,amount_paid,change,reciept) VALUES(?,?,?,?,?,?,?,?,?)",(name,t,Payment_Method,d,tran,Final_Price,csh,change,p))
                                    con.commit()
                                    '''cu=con.execute("SELECT * FROM Transac")
                                    for i in cu:
                                        print(i)'''
                                    break
                                print("\tPayment Successful!\t\nEnjoy your Meal, {0}".format(name))
                                break
                            break
                        elif Process=='CANCEL':
                            d=dt.datetime.now()
                            print(d)
                            print("\tPayment UnSuccessful!\t\nPlease Pay to complete your order, {0}".format(name))
                            break
                        else:
                            d=dt.datetime.now()
                            print(d)
                            print("!Sorry! This Payment Unsuccessful!\tPlease Pay !")
                            continue
                    elif Payment_Method=='COFFEE BUCKS':
                        print("Overall Charges with GST(5%) included: ",Final_Price,"Rs/-")
                        Process=input("For Payment Press (Proceed) or (Cancel)")
                        Process=Process.upper().strip()
                        if Process=='PROCEED':
                            try:
                                counter=randint(1,6)
                                token=randint(1,30)
                                csh=int(input('Enter the amount to pay! '))
                                if csh<Final_Price:
                                    print("Amount is less than payable!!\n")
                                    break
                                else:
                                    change=csh-Final_Price
                                    change=int(change)
                                    time.sleep(1.5)
                                    code='ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
                                    tran=''
                                    for c in range(11):
                                        tran+=random.choice(code)
                                    print('\n\tYour transaction id: ',tran)
                                    print('\n\tPlease collect the change: ',change)
                                    print('\n\nYour token no is: {}, & Please visit Counter No.: {}'.format(token,counter))
                                    time.sleep(1.5)
                                    d=dt.datetime.now()
                                    print(d)
                                    p=input('\nDo you want to print a reciept?[Yes/No]')
                                    p=p.lower()
                                    
                            except Exception as e:
                                print(e)
                                break
                            if p=='yes':
                                p=f'Cafe_{tran}.pdf'
                                ca=canvas.Canvas(f'Cafe_{tran}.pdf',pagesize=letter)
                                ca.setLineWidth(.3)
                                ca.setFont('Helvetica', 11)
                                ca.line(25,790,595,790)
                                ca.line(25,790,25,330)
                                ca.line(595,790,595,330)
                                ca.drawString(435,750,"{}".format(d))
                                ca.line(435,747,590,747)
                                ca.drawString(30,750,'|_|CAFE SHOP!!')
                                ca.drawString(30,735,'OF BREAK-ZONE INDUSTRIES')
                                ca.drawString(30,705,'RECEIVED BY:')
                                ca.drawString(120,705,":-{}".format(name))
                                ca.line(120,700,580,700)
                                ca.drawString(200,680, "***\t\t\tCash Memo\t\t\t***")
                                ca.drawString(50,650, "Items Purchased: {}".format(t))
                                ca.line(140,645,590,645)
                                ca.drawString(50,620, "Price of Items Purchased: ____________________________________")
                                ca.drawString(445,620,":-{}".format(Cost))
                                ca.drawString(50,595, "TAX on Items Purchased: _________________________________")
                                ca.drawString(445,595,":-{}".format(GST))
                                ca.drawString(50,570, "Total Price including GST(5%) on deal: ___________________________")
                                ca.drawString(445,570,":-Rs.{}/-".format(Final_Price))
                                ca.drawString(50,545, "Mode of Payment: ________________________________")
                                ca.drawString(445,545,":-{}".format(Payment_Method))
                                ca.drawString(50,520, "Your transaction id: _______________________________________")
                                ca.drawString(445,520,":-{}".format(tran))
                                ca.drawString(50,495, "Amount Paid by customer at counter: ____________________________")
                                ca.drawString(445,495,":-{}".format(csh))
                                ca.drawString(50,470, "Change returned to customer: ______________________________")
                                ca.drawString(445,470,":-{}".format(change))
                                ca.drawString(400,450,'Counter NO:')
                                ca.drawString(510,450,":-{}".format(counter))
                                ca.line(505,445,530,445)
                                ca.drawString(400,420,'Token No:')
                                ca.drawString(510,420,":-{}".format(token))
                                ca.line(505,415,530,415)
                                ca.drawString(50,390, "***\t\t\tPayment Successful!\t\t\t***")
                                ca.drawString(200,370, "******Have a Nice DAY!******")
                                ca.drawString(50,350, "************************************************************************************************")
                                ca.line(25,330,595,330)
                                ca.save()
                                
                                t=str(t)
                                cur.execute("INSERT INTO Transac(customer,items,pay_method,date,transaction_id,total_price,amount_paid,change,reciept) VALUES(?,?,?,?,?,?,?,?,?)",(name,t,Payment_Method,d,tran,Final_Price,csh,change,p))
                                con.commit()
                                
                                try:
                                    msg = EmailMessage()
                                    msg['Subject'] = 'Cafe Shop Invoice!!'
                                    msg['From'] = 'thikhai83@gmail.com'
                                    msg['To'] = input('Enter your Address:\t')
                                    msg.set_content('Invoice Attached......!!')
                                    
                                    files = [p]
                                    for file in files:
                                        with open(file,'rb') as f:
                                            file_data = f.read()
                                            file_name = f.name
                                        msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)
                                        break
                                    with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
                                        
                                        '''smtp.ehlo()
                                        smtp.starttls()
                                        smtp.ehlo()'''
                                        
                                        smtp.login('thikhai83@gmail.com', 'thikhai@123')
                                        
                                        smtp.send_message(msg)
                                except Exception as e:
                                    print(e)
                                '''cu=con.execute("SELECT * FROM Transac")
                                for i in cu:        #Used for print data from database
                                    print(i)'''

                            elif p=='no':
                                print('You saved paper!Well done!')
                                t=str(t)
                                cur.execute("INSERT INTO Transac(customer,items,pay_method,date,transaction_id,total_price,amount_paid,change,reciept) VALUES(?,?,?,?,?,?,?,?,?)",(name,t,Payment_Method,d,tran,Final_Price,csh,change,p))
                                con.commit()
                                '''cu=con.execute("SELECT * FROM Transac")
                                for i in cu:
                                    print(i)'''
                                break
                            else:
                                print("No choice!")
                                t=str(t)
                                cur.execute("INSERT INTO Transac(customer,items,pay_method,date,transaction_id,total_price,amount_paid,change,reciept) VALUES(?,?,?,?,?,?,?,?,?)",(name,t,Payment_Method,d,tran,Final_Price,csh,change,p))
                                con.commit()
                                '''cu=con.execute("SELECT * FROM Transac")
                                for i in cu:
                                    print(i)'''
                                break
                            print("\tPayment Successful!\t\nEnjoy your Meal, {0}".format(name))
                            break
                        elif Process=='CANCEL':
                            d=dt.datetime.now()
                            print(d)
                            print("\tPayment UnSuccessful!\t\nPlease Pay, {0} to complete your order".format(name))
                            continue
                        else:
                            d=dt.datetime.now()
                            print(d)
                            print("\n\t!Sorry! This Payment method is Unsuccessful!\tPlease Pay !")
                            continue
                    elif Payment_Method=='NET BANKING':
                        print("Overall Charges with GST(5%) included: ",Final_Price,"Rs/-")
                        Process=input("For Payment Press (Proceed) or (Cancel)")
                        Process=Process.upper().strip()
                        if Process=='PROCEED':
                            try:
                                bank=input('Enter your bank: ')
                                netbanking=int(input("Enter your netbanking pin no.:\t"))
                                netbanking=str(netbanking)
                                if len(netbanking)==6:
                                    counter=randint(1,6)
                                    token=randint(1,30)
                                    csh=float(input('Enter the amount to pay! '))
                                    if csh<Final_Price:
                                        print("Amount is less than payable!!\n")
                                        break
                                    else:
                                        change=csh-Final_Price
                                        change=int(change)
                                        time.sleep(1.5)
                                        code='ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
                                        tran=''
                                        for c in range(11):
                                            tran+=random.choice(code)
                                        print('\n\tYour transaction id: ',tran)
                                        print('\n\tPlease collect the change: ',change)
                                        print('\n\nYour token no is: {}, & Please visit Counter No.: {}'.format(token,counter))
                                        time.sleep(1.5)
                                        d=dt.datetime.now()
                                        print(d)
                                        p=input('\nDo you want to print a reciept?[Yes/No]')
                                        p=p.lower()
                                else:
                                    continue
                            except Exception as e:
                                print(e)
                                break
                            if p=='yes':
                                p=f'Cafe_{tran}.pdf'
                                ca=canvas.Canvas(f'Cafe_{tran}.pdf',pagesize=letter)
                                ca.setLineWidth(.3)
                                ca.setFont('Helvetica', 11)
                                ca.line(25,790,595,790)
                                ca.line(25,790,25,330)
                                ca.line(595,790,595,330)
                                ca.drawString(435,750,"{}".format(d))
                                ca.line(435,747,590,747)
                                ca.drawString(30,750,'|_|CAFE SHOP!!')
                                ca.drawString(30,735,'OF BREAK-ZONE INDUSTRIES')
                                ca.drawString(30,705,'RECEIVED BY:')
                                ca.drawString(120,705,":-{}".format(name))
                                ca.line(120,700,580,700)
                                ca.drawString(200,680, "***\t\t\tCash Memo\t\t\t***")
                                ca.drawString(50,650, "Items Purchased: {}".format(t))
                                ca.line(140,645,590,645)
                                ca.drawString(50,620, "Price of Items Purchased: _____________________________________")
                                ca.drawString(445,620,":-{}".format(Cost))
                                ca.drawString(50,595, "TAX on Items Purchased: _________________________________")
                                ca.drawString(445,595,":-{}".format(GST))
                                ca.drawString(50,570, "Total Price including GST(5%) on deal: _____________________________")
                                ca.drawString(445,570,":-Rs.{}/-".format(Final_Price))
                                ca.drawString(50,545, "Mode of Payment:          {}  {}".format(bank,Payment_Method))
                                ca.line(150,540,580,540)
                                ca.drawString(50,520, "Your transaction id: ________________________________________")
                                ca.drawString(445,520,":-{}".format(tran))
                                ca.drawString(50,495, "Amount Paid by customer at counter: ___________________________")
                                ca.drawString(445,495,":-{}".format(csh))
                                ca.drawString(50,470, "Change returned to customer: _____________________________")
                                ca.drawString(445,470,":-{}".format(change))
                                ca.drawString(400,450,'Counter NO:')
                                ca.drawString(510,450,":-{}".format(counter))
                                ca.line(505,445,530,445)
                                ca.drawString(400,420,'Token No:')
                                ca.drawString(510,420,":-{}".format(token))
                                ca.line(505,415,530,415)
                                ca.drawString(50,390, "***\t\t\tPayment Successful!\t\t\t***")
                                ca.drawString(200,370, "******Have a Nice DAY!******")
                                ca.drawString(50,350, "************************************************************************************************")
                                ca.line(25,330,595,330)
                                ca.save()
                                
                                t=str(t)
                                cur.execute("INSERT INTO Transac(customer,items,pay_method,date,transaction_id,total_price,amount_paid,change,reciept) VALUES(?,?,?,?,?,?,?,?,?)",(name,t,Payment_Method,d,tran,Final_Price,csh,change,p))
                                con.commit()
                                
                                try:
                                    msg = EmailMessage()
                                    msg['Subject'] = 'Cafe Shop Invoice!!'
                                    msg['From'] = 'thikhai83@gmail.com'
                                    msg['To'] = input('Enter your Address:\t')
                                    msg.set_content('Invoice Attached......!!')
                                    
                                    files = [p]
                                    for file in files:
                                        with open(file,'rb') as f:
                                            file_data = f.read()
                                            file_name = f.name
                                        msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)
                                        break
                                    with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
                                        
                                        '''smtp.ehlo()
                                        smtp.starttls()
                                        smtp.ehlo()'''
                                        
                                        smtp.login('thikhai83@gmail.com', 'thikhai@123')
                                        
                                        smtp.send_message(msg)
                                except Exception as e:
                                    print(e)
                                '''cu=con.execute("SELECT * FROM Transac")
                                for i in cu:        #Used for print data from database
                                        print(i)'''

                            elif p=='no':
                                print('You saved paper!Well done!')
                                t=str(t)
                                cur.execute("INSERT INTO Transac(customer,items,pay_method,date,transaction_id,total_price,amount_paid,change,reciept) VALUES(?,?,?,?,?,?,?,?,?)",(name,t,Payment_Method,d,tran,Final_Price,csh,change,p))
                                con.commit()
                                '''cu=con.execute("SELECT * FROM Transac")
                                for i in cu:
                                    print(i)'''
                                break
                            else:
                                print("No choice!")
                                t=str(t)
                                cur.execute("INSERT INTO Transac(customer,items,pay_method,date,transaction_id,total_price,amount_paid,change,reciept) VALUES(?,?,?,?,?,?,?,?,?)",(name,t,Payment_Method,d,tran,Final_Price,csh,change,p))
                                con.commit()
                                '''cu=con.execute("SELECT * FROM Transac")
                                for i in cu:
                                    print(i)'''
                                break
                            print("\tPayment Successful!\t\nEnjoy your Meal, {0}".format(name))
                            break
                        elif Process=='CANCEL':
                            d=dt.datetime.now()
                            print(d)
                            print("\tPayment UnSuccessful!\t\nPlease Pay, {0} to complete your order".format(name))
                            continue
                        else:
                            d=dt.datetime.now()
                            print(d)
                            print("\n\t!Sorry! This Payment method is Unsuccessful!\tPlease Pay !")
                            continue
                    elif Payment_Method=='PAYTM':
                        print("Overall Charges with GST(5%) included: ",Final_Price,"Rs/-")
                        Process=input("For Payment Press (Proceed) or (Cancel)")
                        Process=Process.upper().strip()
                        if Process=='PROCEED':
                            try:
                                paytmno=int(input("Enter your paytm regestered no.:\t"))
                                paytmno=str(paytmno)
                                if len(paytmno)==10:
                                    counter=randint(1,6)
                                    token=randint(1,30)
                                    csh=float(input('Enter the amount to pay! '))
                                    if csh<Final_Price:
                                        print("Amount is less than payable!!\n")
                                        break
                                    else:
                                        change=csh-Final_Price
                                        change=int(change)
                                        time.sleep(1.5)
                                        code='ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
                                        tran=''
                                        for c in range(11):
                                            tran+=random.choice(code)
                                        print('\n\tYour transaction id: ',tran)
                                        print('\n\tPlease collect the change: ',change)
                                        print('\n\nYour token no is: {}, & Please visit Counter No.: {}'.format(token,counter))
                                        time.sleep(1.5)
                                        d=dt.datetime.now()
                                        print(d)
                                        p=input('\nDo you want to print a reciept?[Yes/No]')
                                        p=p.lower()
                                else:
                                    continue
                            except Exception as e:
                                print(e)
                                break
                            if p=='yes':
                                p=f'Cafe_{tran}.pdf'
                                ca=canvas.Canvas(f'Cafe_{tran}.pdf',pagesize=letter)
                                ca.setLineWidth(.3)
                                ca.setFont('Helvetica', 11)
                                ca.line(25,790,595,790)
                                ca.line(25,790,25,330)
                                ca.line(595,790,595,330)
                                ca.drawString(435,750,"{}".format(d))
                                ca.line(435,747,590,747)
                                ca.drawString(30,750,'|_|CAFE SHOP!!')
                                ca.drawString(30,735,'OF BREAK-ZONE INDUSTRIES')
                                ca.drawString(30,705,'RECEIVED BY:')
                                ca.drawString(120,705,":-{}".format(name))
                                ca.line(120,700,580,700)
                                ca.drawString(200,680, "***\t\t\tCash Memo\t\t\t***")
                                ca.drawString(50,650, "Items Purchased: {}".format(t))
                                ca.line(140,645,590,645)
                                ca.drawString(50,620, "Price of Items Purchased: ___________________________________")
                                ca.drawString(445,620,":-{}".format(Cost))
                                ca.drawString(50,595, "TAX on Items Purchased: ________________________________")
                                ca.drawString(445,595,":-{}".format(GST))
                                ca.drawString(50,570, "Total Price including GST(5%) on deal: _____________________________")
                                ca.drawString(445,570,":-Rs.{}/-".format(Final_Price))
                                ca.drawString(50,545, "Mode of Payment:            {}".format(Payment_Method))
                                ca.line(150,540,580,540)
                                ca.drawString(50,520, "Your transaction id: _______________________________________")
                                ca.drawString(445,520,":-{}".format(tran))
                                ca.drawString(50,495, "Amount Paid by customer at counter: __________________________")
                                ca.drawString(445,495,":-{}".format(csh))
                                ca.drawString(50,470, "Change returned to customer: ____________________________")
                                ca.drawString(445,470,":-{}".format(change))
                                ca.drawString(400,450,'Counter NO:')
                                ca.drawString(510,450,":-{}".format(counter))
                                ca.line(505,445,530,445)
                                ca.drawString(400,420,'Token No:')
                                ca.drawString(510,420,":-{}".format(token))
                                ca.line(505,415,530,415)
                                ca.drawString(50,390, "***\t\t\tPayment Successful!\t\t\t***")
                                ca.drawString(200,370, "******Have a Nice DAY!******")
                                ca.drawString(50,350, "************************************************************************************************")
                                ca.line(25,330,595,330)
                                ca.save()
                                
                                t=str(t)
                                cur.execute("INSERT INTO Transac(customer,items,pay_method,date,transaction_id,total_price,amount_paid,change,reciept) VALUES(?,?,?,?,?,?,?,?,?)",(name,t,Payment_Method,d,tran,Final_Price,csh,change,p))
                                con.commit()
                                
                                try:
                                    msg = EmailMessage()
                                    msg['Subject'] = 'Cafe Shop Invoice!!'
                                    msg['From'] = 'thikhai83@gmail.com'
                                    msg['To'] = input('Enter your Address:\t')
                                    msg.set_content('Invoice Attached......!!')
                                    
                                    files = [p]
                                    for file in files:
                                        with open(file,'rb') as f:
                                            file_data = f.read()
                                            file_name = f.name
                                        msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)
                                        break
                                    with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
                                        
                                        '''smtp.ehlo()
                                        smtp.starttls()
                                        smtp.ehlo()'''
                                        
                                        smtp.login('thikhai83@gmail.com', 'thikhai@123')
                                        
                                        smtp.send_message(msg)
                                except Exception as e:
                                    print(e)
                                '''cu=con.execute("SELECT * FROM Transac")
                                for i in cu:        #Used for print data from database
                                        print(i)'''

                            elif p=='no':
                                print('You saved paper!Well done!')
                                t=str(t)
                                cur.execute("INSERT INTO Transac(customer,items,pay_method,date,transaction_id,total_price,amount_paid,change,reciept) VALUES(?,?,?,?,?,?,?,?,?)",(name,t,Payment_Method,d,tran,Final_Price,csh,change,p))
                                con.commit()
                                '''cu=con.execute("SELECT * FROM Transac")
                                for i in cu:        #Used for print data from database
                                        print(i)'''
                                break
                            else:
                                print("No choice!")
                                t=str(t)
                                cur.execute("INSERT INTO Transac(customer,items,pay_method,date,transaction_id,total_price,amount_paid,change,reciept) VALUES(?,?,?,?,?,?,?,?,?)",(name,t,Payment_Method,d,tran,Final_Price,csh,change,p))
                                con.commit()
                                '''cu=con.execute("SELECT * FROM Transac")
                                for i in cu:
                                    print(i)'''
                                break
                            print("\tPayment Successful!\t\nEnjoy your Meal, {0}".format(name))
                            break
                        elif Process=='CANCEL':
                            d=dt.datetime.now()
                            print(d)
                            print("\tPayment UnSuccessful!\t\nPlease Pay, {0} to complete your order".format(name))
                            continue
                        else:
                            d=dt.datetime.now()
                            print(d)
                            print("\n\t!Sorry! This Payment method is Unsuccessful!\tPlease Pay !")
                            continue
                    elif Payment_Method=='DEBIT CARD':
                        print("Overall Charges with GST(5%) included: ",Final_Price,"Rs/-")
                        Process=input("For Payment Press (Proceed) or (Cancel)")
                        Process=Process.upper().strip()
                        if Process=='PROCEED':
                            try:
                                bank=input('Enter your bank: ')
                                debit=int(input("Enter your card no.:\t"))
                                debit=str(debit)
                                if len(debit)==16:
                                    counter=randint(1,6)
                                    token=randint(1,30)
                                    csh=float(input('Enter the amount to pay! '))
                                    if csh<Final_Price:
                                        print("Amount is less than payable!!\n")
                                        break
                                    else:
                                        change=csh-Final_Price
                                        change=int(change)
                                        time.sleep(1.5)
                                        code='ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
                                        tran=''
                                        for c in range(11):
                                            tran+=random.choice(code)
                                        print('\n\tYour transaction id: ',tran)
                                        print('\n\tPlease collect the change: ',change)
                                        print('\n\nYour token no is: {}, & Please visit Counter No.: {}'.format(token,counter))
                                        time.sleep(1.5)
                                        d=dt.datetime.now()
                                        print(d)
                                        p=input('\nDo you want to print a reciept?[Yes/No]')
                                        p=p.lower()
                                else:
                                    continue
                            except Exception as e:
                                print(e)
                                break
                            if p=='yes':
                                p=f'Cafe_{tran}.pdf'
                                ca=canvas.Canvas(f'Cafe_{tran}.pdf',pagesize=letter)
                                ca.setLineWidth(.3)
                                ca.setFont('Helvetica', 11)
                                ca.line(25,790,595,790)
                                ca.line(25,790,25,330)
                                ca.line(595,790,595,330)
                                ca.drawString(435,750,"{}".format(d))
                                ca.line(435,747,590,747)
                                ca.drawString(30,750,'|_|CAFE SHOP!!')
                                ca.drawString(30,735,'OF BREAK-ZONE INDUSTRIES')
                                ca.drawString(30,705,'RECEIVED BY:')
                                ca.drawString(120,705,":-{}".format(name))
                                ca.line(120,700,580,700)
                                ca.drawString(200,680, "***\t\t\tCash Memo\t\t\t***")
                                ca.drawString(50,650, "Items Purchased: {}".format(t))
                                ca.line(140,645,590,645)
                                ca.drawString(50,620, "Price of Items Purchased: ____________________________________")
                                ca.drawString(445,620,":-{}".format(Cost))
                                ca.drawString(50,595, "TAX on Items Purchased: __________________________________")
                                ca.drawString(445,595,":-{}".format(GST))
                                ca.drawString(50,570, "Total Price including GST(5%) on deal: ____________________________")
                                ca.drawString(445,570,":-Rs.{}/-".format(Final_Price))
                                ca.drawString(50,545, "Mode of Payment:         {}  {}".format(bank,Payment_Method))
                                ca.line(150,540,580,540)
                                ca.drawString(50,520, "Your transaction id: _______________________________________")
                                ca.drawString(445,520,":-{}".format(tran))
                                ca.drawString(50,495, "Amount Paid by customer at counter: ___________________________")
                                ca.drawString(445,495,":-{}".format(csh))
                                ca.drawString(50,470, "Change returned to customer: ______________________________")
                                ca.drawString(445,470,":-{}".format(change))
                                ca.drawString(400,450,'Counter NO:')
                                ca.drawString(510,450,":-{}".format(counter))
                                ca.line(505,445,530,445)
                                ca.drawString(400,420,'Token No:')
                                ca.drawString(510,420,":-{}".format(token))
                                ca.line(505,415,530,415)
                                ca.drawString(50,390, "***\t\t\tPayment Successful!\t\t\t***")
                                ca.drawString(200,370, "******Have a Nice DAY!******")
                                ca.drawString(50,350, "************************************************************************************************")
                                ca.line(25,330,595,330)
                                ca.save()
                                
                                t=str(t)
                                cur.execute("INSERT INTO Transac(customer,items,pay_method,date,transaction_id,total_price,amount_paid,change,reciept) VALUES(?,?,?,?,?,?,?,?,?)",(name,t,Payment_Method,d,tran,Final_Price,csh,change,p))
                                con.commit()
                                
                                try:
                                    msg = EmailMessage()
                                    msg['Subject'] = 'Cafe Shop Invoice!!'
                                    msg['From'] = 'thikhai83@gmail.com'
                                    msg['To'] = input('Enter your Address:\t')
                                    msg.set_content('Invoice Attached......!!')
                                    
                                    files = [p]
                                    for file in files:
                                        with open(file,'rb') as f:
                                            file_data = f.read()
                                            file_name = f.name
                                        msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)
                                        break
                                    with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
                                        
                                        '''smtp.ehlo()
                                        smtp.starttls()
                                        smtp.ehlo()'''
                                        
                                        smtp.login('thikhai83@gmail.com', 'thikhai@123')
                                        
                                        smtp.send_message(msg)
                                except Exception as e:
                                    print(e)
                                '''cu=con.execute("SELECT * FROM Transac")
                                for i in cu:        #Used for print data from database
                                    print(i))'''
    
                            elif p=='no':
                                print('You saved paper!Well done!')
                                t=str(t)
                                cur.execute("INSERT INTO Transac(customer,items,pay_method,date,transaction_id,total_price,amount_paid,change,reciept) VALUES(?,?,?,?,?,?,?,?,?)",(name,t,Payment_Method,d,tran,Final_Price,csh,change,p))
                                con.commit()
                                '''cu=con.execute("SELECT * FROM Transac")
                                for i in cu:
                                    print(i)'''
                                break
                            else:
                                print("No choice!")
                                t=str(t)
                                cur.execute("INSERT INTO Transac(customer,items,pay_method,date,transaction_id,total_price,amount_paid,change,reciept) VALUES(?,?,?,?,?,?,?,?,?)",(name,t,Payment_Method,d,tran,Final_Price,csh,change,p))
                                con.commit()
                                '''cu=con.execute("SELECT * FROM Transac")
                                for i in cu:
                                    print(i)'''
                                break
                            print("\tPayment Successful!\t\nEnjoy your Meal, {0}".format(name))
                            break
                        elif Process=='CANCEL':
                            d=dt.datetime.now()
                            print(d)
                            print("\tPayment UnSuccessful!\t\nPlease Pay, {0} to complete order".format(name))
                            continue
                        else:
                            d=dt.datetime.now()
                            print(d)
                            print("\n\t!Sorry! This Payment method is Unsuccessful!\tPlease Pay !")
                            continue
                    else:
                        d=dt.datetime.now()
                        print(d)
                        print("\n\tSorry this method is not available yet!!\t\\t Please try another Payment Mode Available upon")
                        continue
            print("\tThankyou! For Visit!\n\t\tPlease visit again, {0}".format(name))
            continue
        else:
            print('\n\tOops! You are not admin!You may be a new user!\n')
            print("\t\t\t!! Cafe Shop !!\t\t\t"+"\nMay I Help you!!\n")
            name=input("What's your name?\t")
            name=name.upper()
            print("Welcome to Cafe Shop! {0}".format(name))
            print("Quote of the day: ",quote)
            
            #Cost=eval(x)
            while True:
                menu=input("you wanna to see menu card Yes/No: ")
                menu=menu.upper().strip()
                if menu=='YES':
                    print(list(DRINKS.items()))
                    print("\n")
                    print(list(SNACKS.items()))
                    print("\n")
                    print(list(CRAZY_PACKS.items()))
                    print("\n")
                    break
                elif menu=='NO':
                    print('You didn\'t opt for menu card!')
                    break
                else:
                    print('Wrong Input')
                    print("Please select a valid option!!\tTry Again!")
                    continue
            while True:
                try:
                    Choice=input('What would you like to have?\n(D)for DRINKS\n(S)for SNACKS\n(P)for CRAZY_PACKS')
                    Choice=Choice.upper().strip()
                    print(Choice)
                    if Choice=='D':
                        i=input('Enter your order! ')
                        i=i.upper()
                        g=i.split(" ")
                        h=set(g)
                        t=tuple(g)
                        print(h)
                        x=i.replace(" ","+",2)
                        if set(g).intersection(D):
                            flag+=1
                            print("item is available in DRINKS !")
                            print(x+"\n",eval(x))
                            Cost=eval(x)
                            GST=(5*Cost)/100
                            Final_Price=Cost+GST
                            print("Overall Charges with GST(5%) included: ",Final_Price,"Rs/-")
                            break
                        else:
                            flag
                            print("Sorry! Please order something else from Menu Card!\nItem is not present in list!")
                            continue
                    elif Choice=='S':
                        i=input('Enter your order! ')
                        i=i.upper()
                        g=i.split(" ")
                        h=set(g)
                        t=tuple(g)
                        print(h)
                        x=i.replace(" ","+",2)
                        if set(g).intersection(S):
                            flag+=1
                            print("item is available in SNACKS !")
                            print(x+"\n",eval(x))
                            Cost=eval(x)
                            GST=(5*Cost)/100
                            Final_Price=Cost+GST
                            print("Overall Charges with GST(5%) included: ",Final_Price,"Rs/-")
                            break
                        else:
                            flag
                            print("Sorry! Please order something else from Menu Card!\nItem is not present in list!")
                            continue
                    elif Choice=='P':
                        i=input('Enter your order! ')
                        i=i.upper()
                        g=i.split(" ")
                        h=set(g)
                        t=tuple(g)
                        print(h)
                        x=i.replace(" ","+",2)
                        if set(g).intersection(P):
                            flag+=1
                            print("item is available in CRAZY_PACKS !")
                            print(x+"\n",eval(x))
                            Cost=eval(x)
                            GST=(5*Cost)/100
                            Final_Price=Cost+GST
                            print("Overall Charges with GST(5%) included: ",Final_Price,"Rs/-")
                            break
                        else:
                            flag
                            print("Sorry! Please order something else from Menu Card!\nItem is not present in list!")
                            continue
                    else:
                        flag
                        print("Sorry wrong input! Please Try anything else!")
                        continue
                except Exception as e:
                    print(e)
                    break
            
            while True:
                if flag==0:
                    break
                else:
                    print("\n\t\t\t !!Payment Gateway!! \t\t\t\n")
                    Payment_Method=input("Please enter Payment Mode: (Cash\nCoffee Bucks\nNet Banking\nPaytm\nDebit Card)\n")
                    Payment_Method=Payment_Method.upper().strip()
                    if Payment_Method=='CASH':
                        print("\nOverall Charges with GST(5%) included: ",Final_Price,"Rs/-\n")
                        Process=input("For Payment Press (Proceed) or (Cancel)")
                        Process=Process.upper().strip()
                        if Process=='PROCEED':
                            counter=randint(1,6)
                            token=randint(1,15)
                            csh=int(input('Enter the cash amount in form of paper currency(single one note at once) to pay! '))
                            if csh!=0 and csh!=10 and csh!=20 and csh!=50 and csh!=100 and csh!=200 and csh!=500 and csh!=2000 :
                                print("Enter a valid currency!!")
                                continue
                            else:
                                try:
                                    counter=randint(1,6)
                                    token=randint(1,50)
                                    if csh<Final_Price:
                                        print("Amount is less than payable!!\n")
                                        break
                                    else:
                                        change=csh-Final_Price
                                        change=int(change)
                                        time.sleep(1.5)
                                        code='ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
                                        tran=''
                                        for c in range(11):
                                            tran+=random.choice(code)
                                        print('\n\tYour transaction id: ',tran)
                                        print('\n\tPlease collect the change: ',change)
                                        print('\n\nYour token no is: {}, & Please visit Counter No.: {}'.format(token,counter))
                                        time.sleep(1.5)
                                        d=dt.datetime.now()
                                        print(d)
                                        p=input('\nDo you want to print a reciept?[Yes/No]')
                                        p=p.lower()
                                except Exception as e:
                                    print(e)
                                    break
                                if p=='yes':
                                    p=f'{tran}.pdf'
                                    ca=canvas.Canvas(f'Cafe_{tran}.pdf',pagesize=letter)
                                    ca.setLineWidth(.3)
                                    ca.setFont('Helvetica', 11)
                                    ca.line(25,790,595,790)
                                    ca.line(25,790,25,330)
                                    ca.line(595,790,595,330)
                                    ca.drawString(435,750,"{}".format(d))
                                    ca.line(435,747,590,747)
                                    ca.drawString(30,750,'|_|CAFE SHOP!!')
                                    ca.drawString(30,735,'OF BREAK-ZONE INDUSTRIES')
                                    ca.drawString(30,705,'RECEIVED BY:')
                                    ca.drawString(120,705,":-{}".format(name))
                                    ca.line(120,700,580,700)
                                    ca.drawString(200,680, "***\t\t\tCash Memo\t\t\t***")
                                    ca.drawString(50,650, "Items Purchased: {}".format(t))
                                    ca.line(140,645,590,645)
                                    ca.drawString(50,620, "Price of Items Purchased: __________________________________")
                                    ca.drawString(445,620,":-{}".format(Cost))
                                    ca.drawString(50,595, "TAX on Items Purchased: _______________________________")
                                    ca.drawString(445,595,":-{}".format(GST))
                                    ca.drawString(50,570, "Total Price including GST(5%) on deal: _____________________________")
                                    ca.drawString(445,570,":-Rs.{}/-".format(Final_Price))
                                    ca.drawString(50,545, "Mode of Payment: _______________________________")
                                    ca.drawString(445,545,":-{}".format(Payment_Method))
                                    ca.drawString(50,520, "Your transaction id: _________________________________________")
                                    ca.drawString(445,520,":-{}".format(tran))
                                    ca.drawString(50,495, "Amount Paid by customer at counter: _______________________________")
                                    ca.drawString(445,495,":-{}".format(csh))
                                    ca.drawString(50,470, "Change returned to customer: _______________________________")
                                    ca.drawString(445,470,":-{}".format(change))
                                    ca.drawString(400,450,'Counter NO:')
                                    ca.drawString(510,450,":-{}".format(counter))
                                    ca.line(505,445,530,445)
                                    ca.drawString(400,420,'Token No:')
                                    ca.drawString(510,420,":-{}".format(token))
                                    ca.line(505,415,530,415)
                                    ca.drawString(50,390, "***\t\t\tPayment Successful!\t\t\t***")
                                    ca.drawString(200,370, "******Have a Nice DAY!******")
                                    ca.drawString(50,350, "************************************************************************************************")
                                    ca.line(25,330,595,330)
                                    ca.save()
                                    
                                    t=str(t)
                                    cur.execute("INSERT INTO Transac(customer,items,pay_method,date,transaction_id,total_price,amount_paid,change,reciept) VALUES(?,?,?,?,?,?,?,?,?)",(name,t,Payment_Method,d,tran,Final_Price,csh,change,p))
                                    con.commit()
                                    
                                    try:
                                        msg = EmailMessage()
                                        msg['Subject'] = 'Cafe Shop Invoice!!'
                                        msg['From'] = 'thikhai83@gmail.com'
                                        msg['To'] = input('Enter your Address:\t')
                                        msg.set_content('Invoice Attached......!!')
                                        
                                        files = [p]
                                        for file in files:
                                            with open(file,'rb') as f:
                                                file_data = f.read()
                                                file_name = f.name
                                            msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)
                                            break
                                        with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
                                            
                                            '''smtp.ehlo()
                                            smtp.starttls()
                                            smtp.ehlo()'''
                                            
                                            smtp.login('thikhai83@gmail.com', 'thikhai@123')
                                            
                                            smtp.send_message(msg)
                                    except Exception as e:
                                        print(e)
                                    '''cu=con.execute("SELECT * FROM Transac")
                                    for i in cu:        #Used for print data from database
                                        print(i)'''

                                elif p=='no':
                                    print('You saved paper!Well done!')
                                    t=str(t)
                                    cur.execute("INSERT INTO Transac(customer,items,pay_method,date,transaction_id,total_price,amount_paid,change,reciept) VALUES(?,?,?,?,?,?,?,?,?)",(name,t,Payment_Method,d,tran,Final_Price,csh,change,p))
                                    con.commit()
                                    '''cu=con.execute("SELECT * FROM Transac")
                                    for i in cu:
                                        print(i)'''
                                    break
                                else:
                                    print("No choice!")
                                    t=str(t)
                                    cur.execute("INSERT INTO Transac(customer,items,pay_method,date,transaction_id,total_price,amount_paid,change,reciept) VALUES(?,?,?,?,?,?,?,?,?)",(name,t,Payment_Method,d,tran,Final_Price,csh,change,p))
                                    con.commit()
                                    '''cu=con.execute("SELECT * FROM Transac")
                                    for i in cu:
                                        print(i)'''
                                    break
                                print("\tPayment Successful!\t\nEnjoy your Meal, {0}".format(name))
                                break
                            break
                        elif Process=='CANCEL':
                            d=dt.datetime.now()
                            print(d)
                            print("\tPayment UnSuccessful!\t\nPlease Pay to complete your order, {0}".format(name))
                            break
                        else:
                            d=dt.datetime.now()
                            print(d)
                            print("!Sorry! This Payment Unsuccessful!\tPlease Pay !")
                            continue
                    elif Payment_Method=='COFFEE BUCKS':
                        print("Overall Charges with GST(5%) included: ",Final_Price,"Rs/-")
                        Process=input("For Payment Press (Proceed) or (Cancel)")
                        Process=Process.upper().strip()
                        if Process=='PROCEED':
                            try:
                                counter=randint(1,6)
                                token=randint(1,15)
                                csh=int(input('Enter the amount to pay! '))
                                if csh<Final_Price:
                                    print("Amount is less than payable!!\n")
                                    break
                                else:
                                    change=csh-Final_Price
                                    change=int(change)
                                    time.sleep(1.5)
                                    code='ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
                                    tran=''
                                    for c in range(11):
                                        tran+=random.choice(code)
                                    print('\n\tYour transaction id: ',tran)
                                    print('\n\tPlease collect the change: ',change)
                                    print('\n\nYour token no is: {}, & Please visit Counter No.: {}'.format(token,counter))
                                    time.sleep(1.5)
                                    d=dt.datetime.now()
                                    print(d)
                                    p=input('\nDo you want to print a reciept?[Yes/No]')
                                    p=p.lower()
                            except Exception as e:
                                print(e)
                                break
                            if p=='yes':
                                p=f'{tran}.pdf'
                                ca=canvas.Canvas(f'Cafe_{tran}.pdf',pagesize=letter)
                                ca.setLineWidth(.3)
                                ca.setFont('Helvetica', 11)
                                ca.line(25,790,595,790)
                                ca.line(25,790,25,330)
                                ca.line(595,790,595,330)
                                ca.drawString(435,750,"{}".format(d))
                                ca.line(435,747,590,747)
                                ca.drawString(30,750,'|_|CAFE SHOP!!')
                                ca.drawString(30,735,'OF BREAK-ZONE INDUSTRIES')
                                ca.drawString(30,705,'RECEIVED BY:')
                                ca.drawString(120,705,":-{}".format(name))
                                ca.line(120,700,580,700)
                                ca.drawString(200,680, "***\t\t\tCash Memo\t\t\t***")
                                ca.drawString(50,650, "Items Purchased: {}".format(t))
                                ca.line(140,645,590,645)
                                ca.drawString(50,620, "Price of Items Purchased: __________________________________")
                                ca.drawString(445,620,":-{}".format(Cost))
                                ca.drawString(50,595, "TAX on Items Purchased: _______________________________")
                                ca.drawString(445,595,":-{}".format(GST))
                                ca.drawString(50,570, "Total Price including GST(5%) on deal: _____________________________")
                                ca.drawString(445,570,":-Rs.{}/-".format(Final_Price))
                                ca.drawString(50,545, "Mode of Payment: _______________________________")
                                ca.drawString(445,545,":-{}".format(Payment_Method))
                                ca.drawString(50,520, "Your transaction id: _________________________________________")
                                ca.drawString(445,520,":-{}".format(tran))
                                ca.drawString(50,495, "Amount Paid by customer at counter: _______________________________")
                                ca.drawString(445,495,":-{}".format(csh))
                                ca.drawString(50,470, "Change returned to customer: _______________________________")
                                ca.drawString(445,470,":-{}".format(change))
                                ca.drawString(400,450,'Counter NO:')
                                ca.drawString(510,450,":-{}".format(counter))
                                ca.line(505,445,530,445)
                                ca.drawString(400,420,'Token No:')
                                ca.drawString(510,420,":-{}".format(token))
                                ca.line(505,415,530,415)
                                ca.drawString(50,390, "***\t\t\tPayment Successful!\t\t\t***")
                                ca.drawString(200,370, "******Have a Nice DAY!******")
                                ca.drawString(50,350, "************************************************************************************************")
                                ca.line(25,330,595,330)
                                ca.save()
                                
                                t=str(t)
                                cur.execute("INSERT INTO Transac(customer,items,pay_method,date,transaction_id,total_price,amount_paid,change,reciept) VALUES(?,?,?,?,?,?,?,?,?)",(name,t,Payment_Method,d,tran,Final_Price,csh,change,p))
                                con.commit()
                                
                                try:
                                    msg = EmailMessage()
                                    msg['Subject'] = 'Cafe Shop Invoice!!'
                                    msg['From'] = 'thikhai83@gmail.com'
                                    msg['To'] = input('Enter your Address:\t')
                                    msg.set_content('Invoice Attached......!!')
                                    
                                    files = [p]
                                    for file in files:
                                        with open(file,'rb') as f:
                                            file_data = f.read()
                                            file_name = f.name
                                        msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)
                                        break
                                    with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
                                        
                                        '''smtp.ehlo()
                                        smtp.starttls()
                                        smtp.ehlo()'''
                                        
                                        smtp.login('thikhai83@gmail.com', 'thikhai@123')
                                        
                                        smtp.send_message(msg)
                                except Exception as e:
                                    print(e)
                                '''cu=con.execute("SELECT * FROM Transac")
                                for i in cu:
                                    print(i)'''
                                break
                            elif p=='no':
                                print('You saved paper!Well done!')
                                t=str(t)
                                cur.execute("INSERT INTO Transac(customer,items,pay_method,date,transaction_id,total_price,amount_paid,change,reciept) VALUES(?,?,?,?,?,?,?,?,?)",(name,t,Payment_Method,d,tran,Final_Price,csh,change,p))
                                con.commit()
                                '''cu=con.execute("SELECT * FROM Transac")
                                for i in cu:
                                    print(i)'''

                            else:
                                print("No choice!")
                                t=str(t)
                                cur.execute("INSERT INTO Transac(customer,items,pay_method,date,transaction_id,total_price,amount_paid,change,reciept) VALUES(?,?,?,?,?,?,?,?,?)",(name,t,Payment_Method,d,tran,Final_Price,csh,change,p))
                                con.commit()
                                '''cu=con.execute("SELECT * FROM Transac")
                                for i in cu:
                                    print(i)'''
                                break
                            print("\tPayment Successful!\t\nEnjoy your Meal, {0}".format(name))
                            break
                        elif Process=='CANCEL':
                            d=dt.datetime.now()
                            print(d)
                            print("\tPayment UnSuccessful!\t\nPlease Pay, {0} to complete your order".format(name))
                            continue
                        else:
                            d=dt.datetime.now()
                            print(d)
                            print("\n\t!Sorry! This Payment method is Unsuccessful!\tPlease Pay !")
                            continue
                    elif Payment_Method=='NET BANKING':
                        print("Overall Charges with GST(5%) included: ",Final_Price,"Rs/-")
                        Process=input("For Payment Press (Proceed) or (Cancel)")
                        Process=Process.upper().strip()
                        if Process=='PROCEED':
                            try:
                                bank=input('Enter your bank: ')
                                netbanking=int(input("Enter your netbanking pin no.:\t"))
                                netbanking=str(netbanking)
                                if len(netbanking)==6:
                                    counter=randint(1,6)
                                    token=randint(1,15)
                                    csh=float(input('Enter the amount to pay! '))
                                    if csh<Final_Price:
                                        print("Amount is less than payable!!\n")
                                        break
                                    else:
                                        change=csh-Final_Price
                                        change=int(change)
                                        time.sleep(1.5)
                                        code='ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
                                        tran=''
                                        for c in range(11):
                                            tran+=random.choice(code)
                                        print('\n\tYour transaction id: ',tran)
                                        print('\n\tPlease collect the change: ',change)
                                        print('\n\nYour token no is: {}, & Please visit Counter No.: {}'.format(token,counter))
                                        time.sleep(1.5)
                                        d=dt.datetime.now()
                                        print(d)
                                        p=input('\nDo you want to print a reciept?[Yes/No]')
                                        p=p.lower()
                                else:
                                    continue
                            except Exception as e:
                                print(e)
                                break
                            if p=='yes':
                                p=f'Cafe_{tran}.pdf'
                                ca=canvas.Canvas(f'Cafe_{tran}.pdf',pagesize=letter)
                                ca.setLineWidth(.3)
                                ca.setFont('Helvetica', 11)
                                ca.line(25,790,595,790)
                                ca.line(25,790,25,330)
                                ca.line(595,790,595,330)
                                ca.drawString(435,750,"{}".format(d))
                                ca.line(435,747,590,747)
                                ca.drawString(30,750,'|_|CAFE SHOP!!')
                                ca.drawString(30,735,'OF BREAK-ZONE INDUSTRIES')
                                ca.drawString(30,705,'RECEIVED BY:')
                                ca.drawString(120,705,":-{}".format(name))
                                ca.line(120,700,580,700)
                                ca.drawString(200,680, "***\t\t\tCash Memo\t\t\t***")
                                ca.drawString(50,650, "Items Purchased: {}".format(t))
                                ca.line(140,645,590,645)
                                ca.drawString(50,620, "Price of Items Purchased: ____________________________________")
                                ca.drawString(445,620,":-{}".format(Cost))
                                ca.drawString(50,595, "TAX on Items Purchased: ________________________________")
                                ca.drawString(445,595,":-{}".format(GST))
                                ca.drawString(50,570, "Total Price including GST(5%) on deal: _____________________________")
                                ca.drawString(445,570,":-Rs.{}/-".format(Final_Price))
                                ca.drawString(50,545, "Mode of Payment:         {}  {}".format(bank,Payment_Method))
                                ca.line(150,540,580,540)
                                ca.drawString(50,520, "Your transaction id: ________________________________________")
                                ca.drawString(445,520,":-{}".format(tran))
                                ca.drawString(50,495, "Amount Paid by customer at counter: ____________________________")
                                ca.drawString(445,495,":-{}".format(csh))
                                ca.drawString(50,470, "Change returned to customer: ______________________________")
                                ca.drawString(445,470,":-{}".format(change))
                                ca.drawString(400,450,'Counter NO:')
                                ca.drawString(510,450,"{}".format(counter))
                                ca.line(505,445,530,445)
                                ca.drawString(400,420,'Token No:')
                                ca.drawString(510,420,":-{}".format(token))
                                ca.line(505,415,530,415)
                                ca.drawString(50,390, "***\t\t\tPayment Successful!\t\t\t***")
                                ca.drawString(200,370, "******Have a Nice DAY!******")
                                ca.drawString(50,350, "************************************************************************************************")
                                ca.line(25,330,595,330)
                                ca.save()
                                
                                t=str(t)
                                cur.execute("INSERT INTO Transac(customer,items,pay_method,date,transaction_id,total_price,amount_paid,change,reciept) VALUES(?,?,?,?,?,?,?,?,?)",(name,t,Payment_Method,d,tran,Final_Price,csh,change,p))
                                con.commit()
                                
                                try:
                                    msg = EmailMessage()
                                    msg['Subject'] = 'Cafe Shop Invoice!!'
                                    msg['From'] = 'thikhai83@gmail.com'
                                    msg['To'] = input('Enter your Address:\t')
                                    msg.set_content('Invoice Attached......!!')
                                    
                                    files = [p]
                                    for file in files:
                                        with open(file,'rb') as f:
                                            file_data = f.read()
                                            file_name = f.name
                                        msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)
                                        break
                                    with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
                                        
                                        '''smtp.ehlo()
                                        smtp.starttls()
                                        smtp.ehlo()'''
                                        
                                        smtp.login('thikhai83@gmail.com', 'thikhai@123')
                                        
                                        smtp.send_message(msg)
                                except Exception as e:
                                    print(e)
                                '''cu=con.execute("SELECT * FROM Transac")
                                for i in cu:
                                    print(i)'''

                            elif p=='no':
                                print('You saved paper!Well done!')
                                t=str(t)
                                cur.execute("INSERT INTO Transac(customer,items,pay_method,date,transaction_id,total_price,amount_paid,change,reciept) VALUES(?,?,?,?,?,?,?,?,?)",(name,t,Payment_Method,d,tran,Final_Price,csh,change,p))
                                con.commit()
                                '''cu=con.execute("SELECT * FROM Transac")
                                for i in cu:
                                    print(i)'''
                                break
                            else:
                                print("No choice!")
                                t=str(t)
                                cur.execute("INSERT INTO Transac(customer,items,pay_method,date,transaction_id,total_price,amount_paid,change,reciept) VALUES(?,?,?,?,?,?,?,?,?)",(name,t,Payment_Method,d,tran,Final_Price,csh,change,p))
                                con.commit()
                                '''cu=con.execute("SELECT * FROM Transac")
                                for i in cu:
                                    print(i)'''
                                break
                            print("\tPayment Successful!\t\nEnjoy your Meal, {0}".format(name))
                            break
                        elif Process=='CANCEL':
                            d=dt.datetime.now()
                            print(d)
                            print("\tPayment UnSuccessful!\t\nPlease Pay, {0} to complete your order".format(name))
                            continue
                        else:
                            d=dt.datetime.now()
                            print(d)
                            print("\n\t!Sorry! This Payment method is Unsuccessful!\tPlease Pay !")
                            continue
                    elif Payment_Method=='PAYTM':
                        print("Overall Charges with GST(5%) included: ",Final_Price,"Rs/-")
                        Process=input("For Payment Press (Proceed) or (Cancel)")
                        Process=Process.upper().strip()
                        if Process=='PROCEED':
                            try:
                                paytmno=int(input("Enter your paytm regestered no.:\t"))
                                paytmno=str(paytmno)
                                if len(paytmno)==10:
                                    counter=randint(1,6)
                                    token=randint(1,15)
                                    csh=float(input('Enter the amount to pay! '))
                                    if csh<Final_Price:
                                        print("Amount is less than payable!!\n")
                                        break
                                    else:
                                        change=csh-Final_Price
                                        change=int(change)
                                        time.sleep(1.5)
                                        code='ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
                                        tran=''
                                        for c in range(11):
                                            tran+=random.choice(code)
                                        print('\n\tYour transaction id: ',tran)
                                        print('\n\tPlease collect the change: ',change)
                                        print('\n\nYour token no is: {}, & Please visit Counter No.: {}'.format(token,counter))
                                        time.sleep(1.5)
                                        d=dt.datetime.now()
                                        print(d)
                                        p=input('\nDo you want to print a reciept?[Yes/No]')
                                        p=p.lower()
                                else:
                                    continue
                            except Exception as e:
                                print(e)
                                break
                            if p=='yes':
                                p=f'Cafe_{tran}.pdf'
                                ca=canvas.Canvas(f'Cafe_{tran}.pdf',pagesize=letter)
                                ca.setLineWidth(.3)
                                ca.setFont('Helvetica', 11)
                                ca.line(25,790,595,790)
                                ca.line(25,790,25,330)
                                ca.line(595,790,595,330)
                                ca.drawString(435,750,"{}".format(d))
                                ca.line(435,747,590,747)
                                ca.drawString(30,750,'|_|CAFE SHOP!!')
                                ca.drawString(30,735,'OF BREAK-ZONE INDUSTRIES')
                                ca.drawString(30,705,'RECEIVED BY:')
                                ca.drawString(120,705,":-{}".format(name))
                                ca.line(120,700,580,700)
                                ca.drawString(200,680, "***\t\t\tCash Memo\t\t\t***")
                                ca.drawString(50,650, "Items Purchased: {}".format(t))
                                ca.line(140,645,590,645)
                                ca.drawString(50,620, "Price of Items Purchased: ___________________________________")
                                ca.drawString(445,620,":-{}".format(Cost))
                                ca.drawString(50,595, "TAX on Items Purchased: ________________________________")
                                ca.drawString(445,595,":-{}".format(GST))
                                ca.drawString(50,570, "Total Price including GST(5%) on deal: ______________________________")
                                ca.drawString(445,570,":-Rs.{}/-".format(Final_Price))
                                ca.drawString(50,545, "Mode of Payment:            {}".format(Payment_Method))
                                ca.line(150,540,580,540)
                                ca.drawString(50,520, "Your transaction id: ___________________________________________")
                                ca.drawString(445,520,":-{}".format(tran))
                                ca.drawString(50,495, "Amount Paid by customer at counter: ____________________________")
                                ca.drawString(445,495,":-{}".format(csh))
                                ca.drawString(50,470, "Change returned to customer: ______________________________")
                                ca.drawString(445,470,":-{}".format(change))
                                ca.drawString(400,450,'Counter NO:')
                                ca.drawString(510,450,":-{}".format(counter))
                                ca.line(505,445,530,445)
                                ca.drawString(400,420,'Token No:')
                                ca.drawString(510,420,":-{}".format(token))
                                ca.line(505,415,530,415)
                                ca.drawString(50,390, "***\t\t\tPayment Successful!\t\t\t***")
                                ca.drawString(200,370, "******Have a Nice DAY!******")
                                ca.drawString(50,350, "************************************************************************************************")
                                ca.line(25,330,595,330)
                                ca.save()
                                
                                t=str(t)
                                cur.execute("INSERT INTO Transac(customer,items,pay_method,date,transaction_id,total_price,amount_paid,change,reciept) VALUES(?,?,?,?,?,?,?,?,?)",(name,t,Payment_Method,d,tran,Final_Price,csh,change,p))
                                con.commit()
                                
                                try:
                                    msg = EmailMessage()
                                    msg['Subject'] = 'Cafe Shop Invoice!!'
                                    msg['From'] = 'thikhai83@gmail.com'
                                    msg['To'] = input('Enter your Address:\t')
                                    msg.set_content('Invoice Attached......!!')
                                    
                                    files = [p]
                                    for file in files:
                                        with open(file,'rb') as f:
                                            file_data = f.read()
                                            file_name = f.name
                                        msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)
                                        break
                                    with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
                                        
                                        '''smtp.ehlo()
                                        smtp.starttls()
                                        smtp.ehlo()'''
                                        
                                        smtp.login('thikhai83@gmail.com', 'thikhai@123')
                                        
                                        smtp.send_message(msg)
                                except Exception as e:
                                    print(e)
                                '''cu=con.execute("SELECT * FROM Transac")
                                for i in cu:
                                    print(i)'''

                            elif p=='no':
                                print('You saved paper!Well done!')
                                t=str(t)
                                cur.execute("INSERT INTO Transac(customer,items,pay_method,date,transaction_id,total_price,amount_paid,change,reciept) VALUES(?,?,?,?,?,?,?,?,?)",(name,t,Payment_Method,d,tran,Final_Price,csh,change,p))
                                con.commit()
                                '''cu=con.execute("SELECT * FROM Transac")
                                for i in cu:
                                    print(i)'''
                                break
                            else:
                                print("No choice!")
                                t=str(t)
                                cur.execute("INSERT INTO Transac(customer,items,pay_method,date,transaction_id,total_price,amount_paid,change,reciept) VALUES(?,?,?,?,?,?,?,?,?)",(name,t,Payment_Method,d,tran,Final_Price,csh,change,p))
                                con.commit()
                                '''cu=con.execute("SELECT * FROM Transac")
                                for i in cu:
                                    print(i)'''
                                break
                            print("\tPayment Successful!\t\nEnjoy your Meal, {0}".format(name))
                            break
                        elif Process=='CANCEL':
                            d=dt.datetime.now()
                            print(d)
                            print("\tPayment UnSuccessful!\t\nPlease Pay, {0} to complete your order".format(name))
                            continue
                        else:
                            d=dt.datetime.now()
                            print(d)
                            print("\n\t!Sorry! This Payment method is Unsuccessful!\tPlease Pay !")
                            continue
                    elif Payment_Method=='DEBIT CARD':
                        print("Overall Charges with GST(5%) included: ",Final_Price,"Rs/-")
                        Process=input("For Payment Press (Proceed) or (Cancel)")
                        Process=Process.upper().strip()
                        if Process=='PROCEED':
                            try:
                                bank=input('Enter your bank: ')
                                debit=int(input("Enter your card no.:\t"))
                                debit=str(debit)
                                if len(debit)==16:
                                    counter=randint(1,6)
                                    token=randint(1,15)
                                    csh=float(input('Enter the amount to pay! '))
                                    if csh<Final_Price:
                                        print("Amount is less than payable!!\n")
                                        break
                                    else:
                                        change=int(change)
                                        change=csh-Final_Price
                                        time.sleep(1.5)
                                        code='ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
                                        tran=''
                                        for c in range(11):
                                            tran+=random.choice(code)
                                        print('\n\tYour transaction id: ',tran)
                                        print('\n\tPlease collect the change: ',change)
                                        print('\n\nYour token no is: {}, & Please visit Counter No.: {}'.format(token,counter))
                                        time.sleep(1.5)
                                        d=dt.datetime.now()
                                        print(d)
                                        p=input('\nDo you want to print a reciept?[Yes/No]')
                                        p=p.lower()
                                else:
                                    continue
                            except Exception as e:
                                print(e)
                                break
                            if p=='yes':
                                p=f'Cafe_{tran}.pdf'
                                ca=canvas.Canvas(f'Cafe_{tran}.pdf',pagesize=letter)
                                ca.setLineWidth(.3)
                                ca.setFont('Helvetica', 11)
                                ca.line(25,790,595,790)
                                ca.line(25,790,25,330)
                                ca.line(595,790,595,330)
                                ca.drawString(435,750,"{}".format(d))
                                ca.line(435,747,590,747)
                                ca.drawString(30,750,'|_|CAFE SHOP!!')
                                ca.drawString(30,735,'OF BREAK-ZONE INDUSTRIES')
                                ca.drawString(30,705,'RECEIVED BY:')
                                ca.drawString(120,705,":-{}".format(name))
                                ca.line(120,700,580,700)
                                ca.drawString(200,680, "***\t\t\tCash Memo\t\t\t***")
                                ca.drawString(50,650, "Items Purchased: {}".format(t))
                                ca.line(140,645,590,645)
                                ca.drawString(50,620, "Price of Items Purchased: ____________________________________")
                                ca.drawString(445,620,":-{}".format(Cost))
                                ca.drawString(50,595, "TAX on Items Purchased: __________________________________")
                                ca.drawString(445,595,":-{}".format(GST))
                                ca.drawString(50,570, "Total Price including GST(5%) on deal: ______________________________")
                                ca.drawString(445,570,":-Rs.{}/-".format(Final_Price))
                                ca.drawString(50,545, "Mode of Payment:          {}  {}".format(bank,Payment_Method))
                                ca.line(150,540,580,540)
                                ca.drawString(50,520, "Your transaction id: _____________________________________")
                                ca.drawString(445,520,":-{}".format(tran))
                                ca.drawString(50,495, "Amount Paid by customer at counter: ____________________________")
                                ca.drawString(445,495,":-{}".format(csh))
                                ca.drawString(50,470, "Change returned to customer: ______________________________")
                                ca.drawString(445,470,":-{}".format(change))
                                ca.drawString(400,450,'Counter NO:')
                                ca.drawString(510,450,":-{}".format(counter))
                                ca.line(505,445,530,445)
                                ca.drawString(400,420,'Token No:')
                                ca.drawString(510,420,":-{}".format(token))
                                ca.line(505,415,530,415)
                                ca.drawString(50,390, "***\t\t\tPayment Successful!\t\t\t***")
                                ca.drawString(200,370, "******Have a Nice DAY!******")
                                ca.drawString(50,350, "************************************************************************************************")
                                ca.line(25,330,595,330)
                                ca.save()
                                
                                t=str(t)
                                cur.execute("INSERT INTO Transac(customer,items,pay_method,date,transaction_id,total_price,amount_paid,change,reciept) VALUES(?,?,?,?,?,?,?,?,?)",(name,t,Payment_Method,d,tran,Final_Price,csh,change,p))
                                con.commit()
                                
                                try:
                                    msg = EmailMessage()
                                    msg['Subject'] = 'Cafe Shop Invoice!!'
                                    msg['From'] = 'thikhai83@gmail.com'
                                    msg['To'] = input('Enter your Address:\t')
                                    msg.set_content('Invoice Attached......!!')
                                    
                                    files = [p]
                                    for file in files:
                                        with open(file,'rb') as f:
                                            file_data = f.read()
                                            file_name = f.name
                                        msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)
                                        break
                                    with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
                                        
                                        '''smtp.ehlo()
                                        smtp.starttls()
                                        smtp.ehlo()'''
                                        
                                        smtp.login('thikhai83@gmail.com', 'thikhai@123')
                                        
                                        smtp.send_message(msg)
                                except Exception as e:
                                    print(e)
                                '''cu=con.execute("SELECT * FROM Transac")
                                for i in cu:
                                    print(i)'''

                            elif p=='no':
                                print('You saved paper!Well done!')
                                t=str(t)
                                cur.execute("INSERT INTO Transac(customer,items,pay_method,date,transaction_id,total_price,amount_paid,change,reciept) VALUES(?,?,?,?,?,?,?,?,?)",(name,t,Payment_Method,d,tran,Final_Price,csh,change,p))
                                con.commit()
                                '''cu=con.execute("SELECT * FROM Transac")
                                for i in cu:
                                    print(i)'''
                                break
                            else:
                                print("No choice!")
                                t=str(t)
                                cur.execute("INSERT INTO Transac(customer,items,pay_method,date,transaction_id,total_price,amount_paid,change,reciept) VALUES(?,?,?,?,?,?,?,?,?)",(name,t,Payment_Method,d,tran,Final_Price,csh,change,p))
                                con.commit()
                                '''cu=con.execute("SELECT * FROM Transac")
                                for i in cu:
                                    print(i)'''
                                break
                            print("\tPayment Successful!\t\nEnjoy your Meal, {0}".format(name))
                            break
                        elif Process=='CANCEL':
                            d=dt.datetime.now()
                            print(d)
                            print("\tPayment UnSuccessful!\t\nPlease Pay, {0} to complete order".format(name))
                            continue
                        else:
                            d=dt.datetime.now()
                            print(d)
                            print("\n\t!Sorry! This Payment method is Unsuccessful!\tPlease Pay !")
                            continue
                    else:
                        d=dt.datetime.now()
                        print(d)
                        print("\n\tSorry this method is not available yet!!\t\\t Please try another Payment Mode Available upon")
                        continue
            print("\tThankyou! For Visit!\n\t\tPlease visit again, {0}".format(name))
            continue
        break
    except Exception as e:
        print(e)
        break
    break
con.close()