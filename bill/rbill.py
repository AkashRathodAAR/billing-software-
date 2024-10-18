from tkinter import*
from tkinter import messagebox
import random,os,tempfile,smtplib

#...function part....

def clear():
    bathsoapentery.delete(0,END)
    facecreamentery.delete(0,END)
    heairsparyentery.delete(0,END)
    heairgelentery.delete(0,END)
    facewashentery.delete(0,END)
    bodylotionentery.delete(0,END)
    
    riceentery.delete(0,END)
    oilentery.delete(0,END)
    wheatentery.delete(0,END)
    dalentery.delete(0,END)
    sugarentery.delete(0,END)
    teaentery.delete(0,END)
    
    maazaentery.delete(0,END)
    pepsientery.delete(0,END)
    spriteentery.delete(0,END)
    dewentery.delete(0,END)
    cocaentery.delete(0,END)
    frootientery.delete(0,END)
    
    
    bathsoapentery.insert(0,0)
    facecreamentery.insert(0,0)
    heairsparyentery.insert(0,0)
    heairgelentery.insert(0,0)
    facewashentery.insert(0,0)
    bodylotionentery.insert(0,0)
    
    riceentery.insert(0,0)
    oilentery.insert(0,0)
    wheatentery.insert(0,0)
    dalentery.insert(0,0)
    sugarentery.insert(0,0)
    teaentery.insert(0,0)
    
    maazaentery.insert(0,0)
    pepsientery.insert(0,0)
    spriteentery.insert(0,0)
    dewentery.insert(0,0)
    cocaentery.insert(0,0)
    frootientery.insert(0,0)
    
    cosmeticstax.delete(0,END)
    grocerytax.delete(0,END)
    colddrinktax.delete(0,END)
    
    cosmeticsprice.delete(0,END)
    groceryprice.delete(0,END)
    drinkprice.delete(0,END)
    
    nameenter.delete(0,END)
    phoneenter.delete(0,END)
    billenter.delete(0,END)
    
    textarea.delete(1.0,END)
    

def send_email():
    def send_gmail():
        try:
         ob=smtplib.SMTP('smtp.gmail.com',587)
         ob.starttls()
         ob.login(senderentery.get(),passwordentery.get())
         message=email_textarea.get(1.0,END)
         ob.sendmail(senderentery.get(),reciverentery.get(),message)
         ob.quit()
         messagebox.showinfo('Sucess','Bill is sucesfully send',parent=root1)
         root1.destroy()
        except:
            messagebox.showerror('Error','Something went wong please try again.!',parent=root1)
             
    if textarea.get(1.0,END)=='\n':
        messagebox.showerror('Error','Bill is empty')
    else:
        root1=Toplevel()
        root1.grab_set()
        root1.title('Send Email')
        root1.config(bg='gray20')
        root1.resizable(0,0)
        
        senderframe=LabelFrame(root1,text='Sender',font=('arial',16,'bold'),bd=6,bg="gray20",fg="white")
        senderframe.grid(row=0,column=0,padx=40,pady=20)
        
        senderlabel=Label(senderframe,text="Sender's Email",font=('arial',14,'bold'),bg="gray20",fg="white")
        senderlabel.grid(row=0,column=0,padx=10,pady=8)
        
        senderentery=Entry(senderframe,font=('arial',14,'bold'),bd=2,width=23,relief=RIDGE)
        senderentery.grid(row=0,column=1,padx=10,pady=8)
        
        passwordlabel=Label(senderframe,text="Password",font=('arial',14,'bold'),bg="gray20",fg="white")
        passwordlabel.grid(row=1,column=0,padx=10,pady=8)
        
        passwordentery=Entry(senderframe,font=('arial',14,'bold'),bd=2,width=23,relief=RIDGE,show='*')
        passwordentery.grid(row=1,column=1,padx=10,pady=8)
        
        recipientframe=LabelFrame(root1,text='RECIPIENT',font=('arial',16,'bold'),bd=6,bg="gray20",fg="white")
        recipientframe.grid(row=1,column=0,padx=40,pady=20)
        
        reciverlabel=Label(recipientframe,text="Email_Address",font=('arial',14,'bold'),bg="gray20",fg="white")
        reciverlabel.grid(row=0,column=0,padx=10,pady=8)
        
        reciverentery=Entry(recipientframe,font=('arial',14,'bold'),bd=2,width=23,relief=RIDGE)
        reciverentery.grid(row=0,column=1,padx=10,pady=8)
        
        messagelabel=Label(recipientframe,text="Message",font=('arial',14,'bold'),bg="gray20",fg="white")
        messagelabel.grid(row=1,column=0,padx=10,pady=8)
        
        email_textarea=Text(recipientframe,font=('arial',14,'bold'),bd=2,relief=SUNKEN,width=42,height=11)
        email_textarea.grid(row=2,column=0,columnspan=2)
        email_textarea.delete(1.0,END)
        email_textarea.insert(END,textarea.get(1.0,END).replace('=','').replace('-',' ').replace('\t\t\t','\t\t'))
        
        sendbutton=Button(root1,text='SEND',font=('arial',16,'bold'),width=15,command=send_gmail)
        sendbutton.grid(row=2,column=0,pady=20)
        root1.mainloop()    
    

def print_bill():
    if textarea.get(1.0,END)=='\n':
        messagebox.showerror('Error','Bill is empty')
    else:
      file= tempfile.mktemp('.txt')  
      open(file,'w').write(textarea.get(1.0,END))  
      os.startfile(file,'print')

    
    


def search_bill():
    for i in os.listdir('bills/'):
        if i.split('.')[0]==billenter.get():
            f=open(f'bills/{i}','r')
            textarea.delete(1.0,END)
            for data in f:
                textarea.insert(END,data)
                f.close()
                break
        else:
            messagebox.showerror('Error','invalid bill number')  
            
                  
if not os.path.exists('bills'):
    os.mkdir('bills')

def save_bill():
   result= messagebox.askyesno("Confrim","Do you want to the save bill")
   if result:
       
       bill_content=textarea.get(1.0,END)
       file= open(f'bills/{billnumber}.txt','w')
       file.write(bill_content)
       file.close()
       messagebox.showinfo("show",f'bill number{billnumber}is save is sucesfully')

billnumber=random.randint(500,1000)

#..bill button area...

def bill_area():
    if nameenter.get()==''or phoneenter.get()=='':
        messagebox.showerror("Error","customer details are required")
    elif cosmeticsprice.get()==''and groceryprice.get()==''and drinkprice.get()=='':
        messagebox.showerror("Error","No product are selected")
    elif cosmeticsprice.get()=='0 Rs'and groceryprice.get()=='0 Rs'and drinkprice.get()=='0 Rs':
        messagebox.showerror("Error","No product selected")
    else:
        textarea.delete(1.0,END)
        textarea.insert(END,'\t\t***Welcome Customer***\n')
        textarea.insert(END,f'\nBill Number:{billnumber}\n')  
        textarea.insert(END,f'\nCoustomer Name:{nameenter.get()}\n')
        textarea.insert(END,f'\nPhone Number:{phoneenter.get()}\n')  
        textarea.insert(END,'\n===========================================================================')
        textarea.insert(END,'Product\t\t\tQuantity\t\t\tPrices') 
        textarea.insert(END,'\n===========================================================================')
        if bathsoapentery.get()!='0':
            textarea.insert(END,f'\nBath Soap\t\t\t{bathsoapentery.get()}\t\t\t{soapprice} Rs')
        if facecreamentery.get()!='0':
            textarea.insert(END,f'\nFace Cream\t\t\t{facecreamentery.get()}\t\t\t{facecreamprice} Rs') 
        if facewashentery.get()!='0':
            textarea.insert(END,f'\nHeair Spary\t\t\t{facewashentery.get()}\t\t\t{facewashprice} Rs')
        if heairsparyentery.get()!='0':
            textarea.insert(END,f'\nFace Wash\t\t\t{heairsparyentery.get()}\t\t\t{heairsparyprice} Rs')              
        if heairgelentery.get()!='0':
            textarea.insert(END,f'\nHeair Gel\t\t\t{heairgelentery.get()}\t\t\t{heairgelprice} Rs')
        if bodylotionentery.get()!='0':
            textarea.insert(END,f'\nBody Locatin\t\t\t{bodylotionentery.get()}\t\t\t{bodylotioneprice} Rs')    
        #...grocery entery...
        if riceentery.get()!='0':
            textarea.insert(END,f'\nRice\t\t\t{riceentery.get()}\t\t\t{riceprice} Rs')  
        if oilentery.get()!='0':
            textarea.insert(END,f'\nOil\t\t\t{facecreamentery.get()}\t\t\t{oilprice} Rs')
        if dalentery.get()!='0':
            textarea.insert(END,f'\nDaal\t\t\t{dalentery.get()}\t\t\t{daalprice} Rs')
        if wheatentery.get()!='0':
            textarea.insert(END,f'\nWheat\t\t\t{wheatentery.get()}\t\t\t{wheatprice} Rs')
        if sugarentery.get()!='0':
            textarea.insert(END,f'\nSugar\t\t\t{facecreamentery.get()}\t\t\t{sugarprice} Rs')
        if teaentery.get()!='0':
            textarea.insert(END,f'\nTea\t\t\t{teaentery.get()}\t\t\t{teaprice} Rs')    
            
         #...cold drink entery...
        if maazaentery.get()!='0':
            textarea.insert(END,f'\nMaaza\t\t\t{maazaentery.get()}\t\t\t{mazaprice} Rs') 
        if frootientery.get()!='0':
            textarea.insert(END,f'\nFrooti\t\t\t{frootientery.get()}\t\t\t{frootiprice} Rs') 
        if dewentery.get()!='0':
            textarea.insert(END,f'\nDew\t\t\t{dewentery.get()}\t\t\t{dewprice} Rs') 
        if pepsientery.get()!='0':
            textarea.insert(END,f'\nPepsi\t\t\t{pepsientery.get()}\t\t\t{pepsiprice} Rs')    
        if cocaentery.get()!='0':
            textarea.insert(END,f'\nCoca Cola\t\t\t{cocaentery.get()}\t\t\t{cocaprice} Rs')
        if spriteentery.get()!='0':
            textarea.insert(END,f'\nSprite\t\t\t{spriteentery.get()}\t\t\t{spriteprice} Rs')                      
        textarea.insert(END,'\n---------------------------------------------------------------------------\n') 
        #...tax print...
        if cosmeticstax.get()!='0.0 Rs':
            textarea.insert(END,f'\nCosmetics Tax\t\t\t\t {cosmeticstax.get()}')      
        if grocerytax.get()!='0.0 Rs':
            textarea.insert(END,f'\nGrocery Tax\t\t\t\t {grocerytax.get()}')  
        if colddrinktax.get()!='0.0 Rs':
            textarea.insert(END,f'\nCold Drink Tax\t\t\t\t {colddrinktax.get()}')                
        textarea.insert(END,f'\n\nTotal Bill\t\t\t\t{totalbill}') 
        textarea.insert(END,'\n---------------------------------------------------------------------------\n') 
        save_bill()
#..total functionlity part...
def total():
    #....cosmetices price ....
    global soapprice,facecreamprice,facewashprice,heairsparyprice,heairgelprice,bodylotioneprice
    #..grocery price global ver...
    global riceprice,oilprice,daalprice,wheatprice,sugarprice,teaprice
    
    #..cold drink global var...
    global mazaprice,frootiprice,dewprice,pepsiprice,cocaprice,spriteprice
    
    global totalbill
    
    soapprice=int(bathsoapentery.get())*20
    facecreamprice=int(facecreamentery.get())*50
    facewashprice=int(facewashentery.get())*100
    heairsparyprice=int(heairsparyentery.get())*150
    heairgelprice=int(heairgelentery.get())*80
    bodylotioneprice=int(bodylotionentery.get())*60
    
    totalcosmosticsprice=soapprice+facecreamprice+facewashprice+heairsparyprice+heairgelprice+bodylotioneprice
    cosmeticsprice.delete(0,END)
    cosmeticsprice.insert(0,f'{totalcosmosticsprice} Rs')
    
    cosmeticstaxx=totalcosmosticsprice*0.12
    cosmeticstax.delete(0,END)
    cosmeticstax.insert(0,f'{cosmeticstaxx} Rs')
    
    #....grocery price....
    riceprice=int(riceentery.get())*30
    oilprice=int(oilentery.get())*120
    daalprice=int(dalentery.get())*100
    wheatprice=int(wheatentery.get())*80
    sugarprice=int(sugarentery.get())*50
    teaprice=int(teaentery.get())*140
    
    totalgroceryprice=riceprice+oilprice+daalprice+wheatprice+sugarprice+teaprice
    groceryprice.delete(0,END)
    groceryprice.insert(0,f'{totalgroceryprice} Rs')
    
    grocerytaxx=totalgroceryprice*0.5
    grocerytax.delete(0,END)
    grocerytax.insert(0,f'{grocerytaxx} Rs')
    
    #...cold drink price...
    mazaprice=int(maazaentery.get())*50
    frootiprice=int(frootientery.get())*20
    dewprice=int(dewentery.get())*30
    pepsiprice=int(pepsientery.get())*20
    cocaprice=int(cocaentery.get())*90
    spriteprice=int(spriteentery.get())*40
    
    totaldrinkprice=mazaprice+frootiprice+dewprice+pepsiprice+cocaprice+spriteprice
    drinkprice.delete(0,END)
    drinkprice.insert(0,f'{totaldrinkprice} Rs')
    
    drinktaxx=totaldrinkprice*0.08
    colddrinktax.delete(0,END)
    colddrinktax.insert(0,f'{drinktaxx} Rs')
    
    totalbill=totalcosmosticsprice+totalgroceryprice+totaldrinkprice+cosmeticstaxx+grocerytaxx+drinktaxx
    
    
    
root=Tk()
root.title("Retail Billing")
root.geometry("1270x685")
headinglabel=Label(root,text="Retail Billing System",font=('times new roman',30,'bold'),bg="gray20",fg="gold",bd=12,relief=GROOVE)
headinglabel.pack(fill=X)
custer_details=LabelFrame(root,text="Customer Details",font=("times new roman",15,"bold"),fg="gold",bd=8,relief=GROOVE,bg="gray20")
custer_details.pack(fill=X)
namelabel=Label(custer_details,text="Name",font=("times new roman",15,"bold"),bg="gray20",fg="white")
namelabel.grid(row=0,column=0,padx=20,pady=2)

nameenter=Entry(custer_details,font=("arial",15),bd=7,width=18)
nameenter.grid(row=0,column=1,padx=8)

phonelabel=Label(custer_details,text="Phone Number",font=("times new roman",15,"bold"),bg="gray20",fg="white")
phonelabel.grid(row=0,column=2,padx=20,pady=2)

phoneenter=Entry(custer_details,font=("arial",15),bd=7,width=18)
phoneenter.grid(row=0,column=3,padx=8)

bill_label=Label(custer_details,text="Bill Number",font=("times new roman",15,"bold"),bg="gray20",fg="white")
bill_label.grid(row=0,column=4,padx=20,pady=2)

billenter=Entry(custer_details,font=("arial",15),bd=7,width=18)
billenter.grid(row=0,column=5,padx=8)

searchbutton=Button(custer_details,text="SEARCH",font=("arial",12,"bold"),bd=7,width=10,command=search_bill)
searchbutton.grid(row=0,column=6,padx=20,pady=8)

productframe=Frame(root)
productframe.pack()
#...cosmetics

cosmeticsframe=LabelFrame(productframe,text="Cosmetics",font=("times new roman",15,"bold"),fg="gold",bd=8,relief=GROOVE,bg="gray20")
cosmeticsframe.grid(row=0,column=0)

bathsoaplabel=Label(cosmeticsframe,text="Bath Soap",font=("times new roman",15,"bold"),bg="gray20",fg="white")
bathsoaplabel.grid(row=0,column=0,pady=9,padx=10)

bathsoapentery=Entry(cosmeticsframe,font=("times new roman",15,"bold"),width=10,bd=5)
bathsoapentery.grid(row=0,column=1,sticky="w")
bathsoapentery.insert(0,0)

facecreamlabel=Label(cosmeticsframe,text="Face Cream",font=("times new roman",15,"bold"),bg="gray20",fg="white")
facecreamlabel.grid(row=1,column=0,pady=9,padx=10,sticky="w")

facecreamentery=Entry(cosmeticsframe,font=("times new roman",15,"bold"),width=10,bd=5)
facecreamentery.grid(row=1,column=1)
facecreamentery.insert(0,0)

heairsparylabel=Label(cosmeticsframe,text="Heair Spary",font=("times new roman",15,"bold"),bg="gray20",fg="white")
heairsparylabel.grid(row=2,column=0,pady=9,padx=10,sticky="w")

heairsparyentery=Entry(cosmeticsframe,font=("times new roman",15,"bold"),width=10,bd=5)
heairsparyentery.grid(row=2,column=1)
heairsparyentery.insert(0,0)

facewashlabel=Label(cosmeticsframe,text="Face Wash",font=("times new roman",15,"bold"),bg="gray20",fg="white")
facewashlabel.grid(row=3,column=0,pady=9,padx=10,sticky="w")

facewashentery=Entry(cosmeticsframe,font=("times new roman",15,"bold"),width=10,bd=5)
facewashentery.grid(row=3,column=1)
facewashentery.insert(0,0)

heairgellabel=Label(cosmeticsframe,text="Heair Gel",font=("times new roman",15,"bold"),bg="gray20",fg="white")
heairgellabel.grid(row=4,column=0,pady=9,padx=10,sticky="w")

heairgelentery=Entry(cosmeticsframe,font=("times new roman",15,"bold"),width=10,bd=5)
heairgelentery.grid(row=4,column=1)
heairgelentery.insert(0,0)

bodylotionlabel=Label(cosmeticsframe,text="Body Lotion",font=("times new roman",15,"bold"),bg="gray20",fg="white")
bodylotionlabel.grid(row=5,column=0,pady=9,padx=10,sticky="w")

bodylotionentery=Entry(cosmeticsframe,font=("times new roman",15,"bold"),width=10,bd=5)
bodylotionentery.grid(row=5,column=1)
bodylotionentery.insert(0,0)
#....grocery....

groceryframe=LabelFrame(productframe,text="Grocery",font=("times new roman",15,"bold"),fg="gold",bd=8,relief=GROOVE,bg="gray20")
groceryframe.grid(row=0,column=1)

ricelabel=Label(groceryframe,text="Rice",font=("times new roman",15,"bold"),bg="gray20",fg="white")
ricelabel.grid(row=0,column=0,pady=9,padx=10,sticky="w")

riceentery=Entry(groceryframe,font=("times new roman",15,"bold"),width=10,bd=5)
riceentery.grid(row=0,column=1)
riceentery.insert(0,0)

oillabel=Label(groceryframe,text="Oil",font=("times new roman",15,"bold"),bg="gray20",fg="white")
oillabel.grid(row=1,column=0,pady=9,padx=10,sticky="w")

oilentery=Entry(groceryframe,font=("times new roman",15,"bold"),width=10,bd=5)
oilentery.grid(row=1,column=1)
oilentery.insert(0,0)

dallabel=Label(groceryframe,text="Daal",font=("times new roman",15,"bold"),bg="gray20",fg="white")
dallabel.grid(row=2,column=0,pady=9,padx=10,sticky="w")

dalentery=Entry(groceryframe,font=("times new roman",15,"bold"),width=10,bd=5)
dalentery.grid(row=2,column=1)
dalentery.insert(0,0)

wheatlabel=Label(groceryframe,text="Wheat",font=("times new roman",15,"bold"),bg="gray20",fg="white")
wheatlabel.grid(row=3,column=0,pady=9,padx=10,sticky="w")

wheatentery=Entry(groceryframe,font=("times new roman",15,"bold"),width=10,bd=5)
wheatentery.grid(row=3,column=1)
wheatentery.insert(0,0)

sugarlabel=Label(groceryframe,text="Sugar",font=("times new roman",15,"bold"),bg="gray20",fg="white")
sugarlabel.grid(row=4,column=0,pady=9,padx=10,sticky="w")

sugarentery=Entry(groceryframe,font=("times new roman",15,"bold"),width=10,bd=5)
sugarentery.grid(row=4,column=1,)
sugarentery.insert(0,0)

tealabel=Label(groceryframe,text="Tea",font=("times new roman",15,"bold"),bg="gray20",fg="white")
tealabel.grid(row=5,column=0,pady=9,padx=10,sticky="w")

teaentery=Entry(groceryframe,font=("times new roman",15,"bold"),width=10,bd=5)
teaentery.grid(row=5,column=1)
teaentery.insert(0,0)

#...cold drink....
drinksframe=LabelFrame(productframe,text="Cold Drinks",font=("times new roman",15,"bold"),fg="gold",bd=8,relief=GROOVE,bg="gray20")
drinksframe.grid(row=0,column=2 )

maazalabel=Label(drinksframe,text="Maaza",font=("times new roman",15,"bold"),bg="gray20",fg="white")
maazalabel.grid(row=0,column=0,pady=9,padx=10,sticky="w")

maazaentery=Entry(drinksframe,font=("times new roman",15,"bold"),width=10,bd=5)
maazaentery.grid(row=0,column=1)
maazaentery.insert(0,0)

pepsilabel=Label(drinksframe,text="Pepsi",font=("times new roman",15,"bold"),bg="gray20",fg="white")
pepsilabel.grid(row=1,column=0,pady=9,padx=10,sticky="w")

pepsientery=Entry(drinksframe,font=("times new roman",15,"bold"),width=10,bd=5)
pepsientery.grid(row=1,column=1)
pepsientery.insert(0,0)

spritelabel=Label(drinksframe,text="Sprite",font=("times new roman",15,"bold"),bg="gray20",fg="white")
spritelabel.grid(row=2,column=0,pady=9,padx=10,sticky="w")

spriteentery=Entry(drinksframe,font=("times new roman",15,"bold"),width=10,bd=5)
spriteentery.grid(row=2,column=1)
spriteentery.insert(0,0)

dewlabel=Label(drinksframe,text="Dew",font=("times new roman",15,"bold"),bg="gray20",fg="white")
dewlabel.grid(row=3,column=0,pady=9,padx=10,sticky="w")

dewentery=Entry(drinksframe,font=("times new roman",15,"bold"),width=10,bd=5)
dewentery.grid(row=3,column=1)
dewentery.insert(0,0)

frootilabel=Label(drinksframe,text="Frooti",font=("times new roman",15,"bold"),bg="gray20",fg="white")
frootilabel.grid(row=4,column=0,pady=9,padx=10,sticky="w")

frootientery=Entry(drinksframe,font=("times new roman",15,"bold"),width=10,bd=5)
frootientery.grid(row=4,column=1)
frootientery.insert(0,0)

cocalabel=Label(drinksframe,text="Coca Cola",font=("times new roman",15,"bold"),bg="gray20",fg="white")
cocalabel.grid(row=5,column=0,pady=9,padx=10,sticky="w")

cocaentery=Entry(drinksframe,font=("times new roman",15,"bold"),width=10,bd=5)
cocaentery.grid(row=5,column=1)
cocaentery.insert(0,0)

#....bill frame....
billframe=Frame(productframe,bd=8,relief=GROOVE)
billframe.grid(row=0,column=3,padx=10)

bilframelable=Label(billframe,text="Bill Area",font=("times new roman",15,"bold"),bd=7,relief=GROOVE)
bilframelable.pack(fill=X)

scrollbar=Scrollbar(billframe,orient=VERTICAL)
scrollbar.pack(side=RIGHT,fill=Y)

#...text area....

textarea=Text(billframe,height=16,width=75,yscrollcommand=scrollbar.set)
textarea.pack()
scrollbar.config(command=textarea.yview)

#...bill menu entery...

billmenuframe=LabelFrame(root,text="Bill Menu",font=("times new roman",15,"bold"),fg="gold",bd=8,relief=GROOVE,bg="gray20")
billmenuframe.pack()

cosmeticspricelabel=Label(billmenuframe,text="Cosmetics Price",font=("times new roman",15,"bold"),bg="gray20",fg="white")
cosmeticspricelabel.grid(row=0,column=0,pady=9,padx=10,sticky="w")

cosmeticsprice=Entry(billmenuframe,font=("times new roman",15,"bold"),width=10,bd=5)
cosmeticsprice.grid(row=0,column=1,padx=10,pady=9)

grocerypricelabel=Label(billmenuframe,text="Grocery Price",font=("times new roman",15,"bold"),bg="gray20",fg="white")
grocerypricelabel.grid(row=1,column=0,pady=9,padx=10,sticky="w")

groceryprice=Entry(billmenuframe,font=("times new roman",15,"bold"),width=10,bd=5)
groceryprice.grid(row=1,column=1,padx=10,pady=9)

drinkpricelabel=Label(billmenuframe,text="Cold Drink Price",font=("times new roman",15,"bold"),bg="gray20",fg="white")
drinkpricelabel.grid(row=2,column=0,pady=9,padx=10,sticky="w")

drinkprice=Entry(billmenuframe,font=("times new roman",15,"bold"),width=10,bd=5)
drinkprice.grid(row=2,column=1,padx=10,pady=9)

#....tax area....

cosmeticstaxlabel=Label(billmenuframe,text="Cosmetics Tax",font=("times new roman",15,"bold"),bg="gray20",fg="white")
cosmeticstaxlabel.grid(row=0,column=2,pady=9,padx=10,sticky="w")

cosmeticstax=Entry(billmenuframe,font=("times new roman",15,"bold"),width=10,bd=5)
cosmeticstax.grid(row=0,column=3,padx=10,pady=9)

grocerytaxlabel=Label(billmenuframe,text="Grocery Tax",font=("times new roman",15,"bold"),bg="gray20",fg="white")
grocerytaxlabel.grid(row=1 ,column=2,pady=9,padx=10,sticky="w")

grocerytax=Entry(billmenuframe,font=("times new roman",15,"bold"),width=10,bd=5)
grocerytax.grid(row=1,column=3,padx=10,pady=9)

colddrinktaxlabel=Label(billmenuframe,text="Cold Drink Tax",font=("times new roman",15,"bold"),bg="gray20",fg="white")
colddrinktaxlabel.grid(row=2,column=2,pady=9,padx=10,sticky="w")

colddrinktax=Entry(billmenuframe,font=("times new roman",15,"bold"),width=10,bd=5)
colddrinktax.grid(row=2,column=3,padx=10,pady=9)

#...button frame...
buttonfreame=Frame(billmenuframe,bd=8,relief=GROOVE)
buttonfreame.grid(row=0,column=4,rowspan=3)

totalbutton=Button(buttonfreame,text="Total",font=("arial",16,"bold"),bg="gray20",fg="white",bd=5,width=8,pady=10,command=total)
totalbutton.grid(row=0,column=0,pady=20,padx=5)

billbutton=Button(buttonfreame,text="Bill",font=("arial",16,"bold"),bg="gray20",fg="white",bd=5,width=8,pady=10,command=bill_area)
billbutton.grid(row=0,column=1,pady=20,padx=5)

emailbutton=Button(buttonfreame,text="Email",font=("arial",16,"bold"),bg="gray20",fg="white",bd=5,width=8,pady=10,command=send_email)
emailbutton.grid(row=0,column=2,pady=20,padx=5)

printbutton=Button(buttonfreame,text="Print",font=("arial",16,"bold"),bg="gray20",fg="white",bd=5,width=8,pady=10,command=print_bill)
printbutton.grid(row=0,column=3,pady=20,padx=5)

clearbutton=Button(buttonfreame,text="Clear",font=("arial",16,"bold"),bg="gray20",fg="white",bd=5,width=8,pady=10,command=clear)
clearbutton.grid(row=0,column=4,pady=20,padx=5)









root.mainloop()

