from tkinter import *
import tkinter as tk
from tkinter import messagebox


#importing the required libraries 



def mywindow():
    root = Tk()
    root.title("Healthbot")



    def send():
        send = "You -> " + e.get()
        txt.insert(END, "\n" + send)
        user = e.get().lower()



        if (user == "hello"):
            txt.insert(END, "\n" + "Bot -> Hi! how can I help you")




        elif (user == "hi" or user == "hii" or user == "hiiii"):
            txt.insert(END, "\n" + "Bot -> Hello")




        elif (e.get() == "how are you"):
            txt.insert(END, "\n" + "Bot -> fine! and you")



        elif (user == "fine" or user == "i am good" or user == "i am doing good"):
            txt.insert(END, "\n" + "Bot -> Great! how can I help you.")




        elif (
                user == "Strep throat" or user == "strep throat" or user == "a sore throat with white patches" or user == "A sore throat with white patches" or user == "trouble swallowing" or user == "Trouble swallowing"):
            txt.insert(END,
                       "\n" + "You can take PENICILLIN , AMOXICILLLIN, CEPHALEXIN, AZITHROMYCIN." + "\n" + "Home remidies: 1. Gargle with salt water. 2. Drink warm water/liquids like lemon water and tea. 3. Cofsils. 4. Get plenty of rest" + "\n" + "If the symptoms continues for more than 3 days you should go and see a doctor.")
            
            


        elif (
                user == "Swollen throat" or user == "Swelling" or user == "swelling" or user == "soreness in throat" or user == "throat is scratchy" or user == "hoarse voice" or user == "swollen lymph nodes"):
            txt.insert(END,
                       "\n" + "You can take OTC painkillers such as IBUPROFEN, ACETAMINOPHEN and ASPIRIN." + "\n" + "Home remedies: 1. Gargle with salt water. 2. Drink warm water/liquids. 3. Cofsils. 4. Antibiotics if you have any bacterial infection" + "\n" + "If this symptoms continues for more than 3 days you should go and see a doctor.")
            



        elif (
                user == "Headache" or user == "Head is paining" or user == "headpain" or user == "I am having a headache" or user == "I am suffering from headache"):
            txt.insert(END,
                       "\n" + "Do you have migraine? , Do you usually have headache? , Which Part  of head is paining?")
            



        elif (
                user == "Forehead" or user == "Forehead is paining" or user == "front part of the head" or user == "forehead" or user == "forehead is paining"):
            txt.insert(END,
                       "\n" + "You might have Tension headache, You can take OTC painkillers such as"+"\n"+"IBUPROFEN, ACETAMINOPHEN and ASPIRIN." + "\n" + "Lifestyle changes may help  such as "+"\n"+"1. Getting enough sleep"+"\n"+" 2. Management of stress, anxiety or depression")
            



        elif (user == "YES" or user == "Yes" or user == "yes" or user == "migraine"):
            txt.insert(END,
                       "\n" + "There are many triggers for migraine so Treatment option are: IBUPROFEN, NAPROXEN, ACETAMINOPHEN and ASPIRIN. " + "\n" + "Home remidies: 1. Resting in dark places. 2. Ice pack. 3. Drinking water" "\n" + "Lifestyle changes may help  such as 1. Getting enough sleep 2. Management of stress, 3. Anxiety or depression")
            



        elif (
                user == "Around one eye" or user == "around one eye" or user == "around left eye" or user == "Around left eye" or user == "Around right eye" or user == "around right eye"):
            txt.insert(END,
                       "\n" + "You might have Cluster headache, You can take OTC painkillers such as IBUPROFEN, ACETAMINOPHEN and ASPIRIN." + "\n" + "Lifestyle changes may help  such as 1. Getting enough sleep 2. Avoiding Alcohol and smoking, 3. Oxygen Therapy")
            


        elif (
                user == "between eyes and nose" or user == "Between eyes and nose" or user == "Sinus Headache" or user == "sinus headache" or user == "forehead and around nose"):
            txt.insert(END,
                       "\n" + "You might have Sinus headache, You can take OTC painkillers such as IBUPROFEN, ACETAMINOPHEN and ASPIRIN." + "\n" + "Home remedies: 1. Resting enough. 2. Steroid nasal spray or salt water. 3. Drinking water. 4. Antibiotics if you have any bacterial infection")
            


        elif (
                user == "Body pain" or user == "body pain" or user == "body ache" or user == "My body is paining" or user == "I am suffering from body ache"):
            txt.insert(END, "\n" + "Pylenol or Ecotrin")



        elif (user == "Diarrhaea" or user == "Watery stools" or user == "Dehydration"):
            txt.insert(END, "\n" + "Imotium or drink ORS for rehydration")



        elif (user == "Acidity" or user == "acidity" or user == "heartburn"):
            txt.insert(END, "\n" + "Tagamet or Pepsin or AXI or Zantac")



        elif (user == "common cold" or user == "Cold" or user == "I have cold"):
            txt.insert(END,
                       "\n" + "Vicks Vaporub " + "\n" + "Home Remedies: Take steam, consume herbal ginger tea , keep yourself warm")
            


        elif (user == "pimples" or user == "I have pimples" or user == "Suggest me solutions to get rid o my pimples"):
            txt.insert(END,
                       "\n" + "Vicco Turmeric " + "\n" + "Home Remedies: Stay hydrated, apply besan and haldi face pack, apply Fuller's earth i.e. Multani Mitti")
            


        elif (user == "Hairfall" or user == "hairfall" or user == "I have hairfall"):
            txt.insert(END,
                       "\n" + "Kesh King" + "\n" + "Home Remedies: Apply oil regularly,Massage your scalp, keep your scalp clean")
            


        elif (user == "what should I eat for healthy hair" or user == "hairfall control diet" or user == "I have hairfall"):
            txt.insert(END,
                       "\n" + "You should eat a balanced diet that includes fruits, vegetables, whole grains, lean proteins, and healthy fats.")
            


        elif (user == "how much water should I drink"):
            txt.insert(END, "\n" + "You should drink at least 8 glasses of water per day.")



        elif (user == "how often should I exercise" or user == "exercise routine" or user == "exercise tips"):
            txt.insert(END, "\n" + "You should aim to exercise for at least 30 minutes per day, 5 days a week")



        elif (user == "how much sleep do I need" or user == "how many hours to sleep"):
            txt.insert(END, "\n" + "Most adults need 7-9 hours of sleep per night.")



        elif (user == "how can I reduce stress" or user == "stress reduction" or user == "tips to reduce stress"):
            txt.insert(END,
                       "\n" + "You can reduce stress by practicing relaxation techniques like deep breathing, meditation, and yoga.")
            


        elif (user == "cold" or user == "I have cold" or user == "i have cold"):
            txt.insert(END,
                       "\n" + "You can take acetaminophen or ibuprofen for pain relief and to reduce fever. You can also use nasal decongestants or saline nasal spray to relieve congestion.")
            


        elif (user == "flu" or user == "i have flu" ):
            txt.insert(END,
                       "\n" + "You can take acetaminophen or ibuprofen for pain relief and to reduce fever. You can also use cough suppressants or expectorants to relieve cough.")
            


        elif (user == "bronchitis" or user == "Bronchitis" or user == "I have bronchitis"):
            txt.insert(END,
                       "\n" + "You can take cough suppressants to relieve cough. You can also use a humidifier or take a hot shower to help with breathing.")
            


        elif (user == "pneumonia" or user == "I have pneumonia"):
            txt.insert(END,
                       "\n" + "You will need antibiotics prescribed by a healthcare professional. You can also take acetaminophen or ibuprofen for pain relief and to reduce fever.")



        elif (user == "UTI" or user == "Urinary Tract Infection"):
            txt.insert(END,
                       "\n" + "You will need antibiotics prescribed by a healthcare professional. You can also take over-the-counter pain relievers like acetaminophen or ibuprofen for pain relief.")



        elif (user == "how much sleep do I need" or user == "how many hours to sleep"):
            txt.insert(END, "\n" + "Most adults need 7-9 hours of sleep per night.")



        elif (
                user == "headache" or user == "HEADACHE" or user == "Headache" or user == "I have Headache" or user == "I have headache"):
            txt.insert(END,
                       "\n" + "You can take OTC painkillers such as IBUPROFEN, ACETAMINOPHEN and ASPIRIN." + "\n" + "Lifestyle changes may help  such as 1. Getting enough sleep"+"\n"+" 2. Management of stress or anxiety.")
            


        elif (
                user == "Gastroenteritis" or user == "gastroenteritis" or user == "stomach flu" or user == "I have Gastroenteritis" or user == "I have gastroenteritis"):
            txt.insert(END,
                       "\n" + "Medicines: anti-nausea medications (Phenergan, Zofran), anti-diarrheal medications (Imodium, Lomotil), rehydration solutions (Pedialyte, Gatorade)")



        elif (
                user == "stomach cramps" or user == "nausea" or user == "Nausea" or user == "I have Stomach cramps" or user == "I have stomach cramps"):
            txt.insert(END,
                       "\n" + "Medicines: anti-nausea medications (Phenergan, Zofran), anti-diarrheal medications (Imodium, Lomotil), rehydration solutions (Pedialyte,Gatorade)")



            # common allergie
        elif (user == "Hay Fever (Allergic Rhinitis)" or user == "stuffy nose" or user == "itchy or watery eyes"):
            txt.insert(END,
                       "\n" + "Medicines: Antihistamines (e.g., Loratadine, Cetirizine), Decongestants (e.g., Pseudoephedrine), Nasal corticosteroids (e.g., Fluticasone), and Cromolyn sodium.")



        elif (
                user == "Food Allergies" or user == "itching in the mouth" or user == "eczema" or user == "swelling of the lips"):
            txt.insert(END,
                       "\n" + "Medicines: Epinephrine (EpiPen), Antihistamines (e.g., Diphenhydramine), and Omalizumab.")




        elif (
                user == " nasal congestion" or user == "swelling of tongue" or user == "swelling of lips" or user == " swelling of face"):
            txt.insert(END,
                       "\n" + "Medicines: Epinephrine (EpiPen), Antihistamines (e.g., Diphenhydramine), and Omalizumab.")





        elif (
                user == "Drug Allergies" or user == "rash or fever" or user == "swelling of the face" or user == "anaphylaxis."):
            txt.insert(END,
                       "\n" + "Medicines: Epinephrine (EpiPen), Antihistamines (e.g., Diphenhydramine), and Corticosteroids (e.g., Prednisone).")





        elif (
                user == "Insect Sting Allergies" or user == "insect bit me" or user == "redness around the sting area" or user == " itching all over the body"):
            txt.insert(END,
                       "\n" + "Medicines: Epinephrine (EpiPen), Antihistamines (e.g., Diphenhydramine), and Corticosteroids (e.g., Prednisone).")
            



        elif (user == "Skin Allergies" or user == "Itching" or user == "redness" or user == "rash"):
            txt.insert(END,
                       "\n" + "Medicines: Topical corticosteroids (e.g., Hydrocortisone), Oral corticosteroids (e.g., Prednisone), and Antihistamines (e.g.,Loratadine)")
            



        elif (
                user == "Menstrual cramps" or user == "menstrual cramps" or user == "period cramps" or user == "Menstrual cramp" or user == "menstrual cramp"):
            txt.insert(END,
                       "\n" + "You can take Nonsteroidal anti-inflammatory drugs (NSAIDs) such as ibuprofen, naproxen, or aspirin can relieve menstrual cramps. Acetaminophen (Tylenol) may also help alleviate menstrual pain"
                       + "\n" + "Home remedies: Applying heat to the abdomen, such as with a heating pad or hot water bottle, can help relax the muscles and alleviate cramps."
                       + "\n" + "Exercise and stretching can also help reduce menstrual cramps by increasing blood flow and releasing endorphins."
                       + "\n" + "Relaxation techniques such as yoga or meditation can help reduce stress and tension, which may exacerbate menstrual cramps.")




        elif(
                user == "Cancer" or user == "cancer" or user == "I have Cancer" or user == "I have cancer"):
            txt.insert(END,
                 "\n" + "Cancer is a serious disease and you should visit a doctor. You should avoid smoking and Drinking. You should not take a disease like cancer lightly")




        elif (
                user == "Diabetes" or user == "diabetes"  or user == "I have Diabetes" or user == "I have Diabetes"):
            txt.insert(END,
                            "\n" + "For Diabetes you should visit a doctor. You should avoid sugar and carbs. If doctor permits you should take insulin")



        elif (
                user == "Blood Pressure" or user == "blood pressure" or user == "I have Blood pressure" or user == "I have blood pressure"):
            txt.insert(END,"\n" + "Somethings that you can do to keep ur blood pressure normal:"
                                +"\n"+"You should manage your stress. Consult to your doctor. Take proper medication. Quit smoking. eat low sodium diet. Exercise regularly")




        elif (
                user == "Hyper tension" or user == "Hypertension" or user == "hypertension" or user == "I have hypertension" or user == "I have Hypertension" or user == "hyper tension" ):
            txt.insert(END,"\n" + "Somethings that you can do for HyperTension:"
                               +"\n"+"You should manage your stress. Consult to your doctor. Take proper medication. Quit smoking. eat low sodium diet. Exercise regularly")




        elif (
                user == "Chickenpox" or user == "chickenpox" or user == "chicken pox" or user == "I have chickenpox" or user == "I have chicken pox"):
            txt.insert(END,"\n" + "Medicines: Analgesic(relieves pain), Antihistamines(to reduce or stop allergic reaction)"
                            +"\n"+"But you should consult doctor for medical advice")




        elif (
                user == "Malaria" or user == "malaria" or user == "I have Malaria" or user == "I have malaria"):
            txt.insert(END,"\n" + "Medicines: Antiparasitic(kills parasites), Antibiotics(Stops the growth or kill bacteria"
                            +"\n"+"But you should consult doctor for medical advice")
                    



        elif (user == "Measles" or user == "measles" or user == "I have Measles" or user == "I have mealses" or user == "MEASLES"):
                    txt.insert(END,"\n" + "Medicines: Acetaminophen (Tylenol) =, Ibuprofen (Advil, Mortin IB) or Naproxen Sodium (Aleve)")





        elif (user == "tetanus" or user == "Tetanus" or user == "TETANUS" or user == "I have TETANUS" or user == "I have Tetanus" or user == "I have tetanus"):
                    txt.insert(END,"\n" + "You should take tetanus vaccine at any local clinic or nearest hospital")




        elif (user == "TUBERCULOSIS" or user == "Tuberculosis" or user == "tuberculosis" or user == "I have tuberculosis" or user == "I have Tuberculosis"):
                    txt.insert(END,"\n" + "Medicines: Anti tuberculosis medicines are Rifampin, Isoniazid, Pyrazinamide and Ethambutol")




        elif (user == "VIRAL HEPATITIS" or user == "Viral hepatitis" or user == "viral hepatitis" or user == "I have viral hepatitis" or user == "I have Viral hepatitis"):
                    txt.insert(END,"\n" + "Medicines: Entecavir (Baraclude), Tenofovir (Viread), Lamivudine(Epivir) ")





        elif (user == "HEPATITIS" or user == "Hepatitis" or user == "hepatitis" or user == "I have Hepatitis" or user == "I have hepatitis"):
                    txt.insert(END,"\n" + "Medicines: Entecavir (Baraclude), Tenofovir (Viread), Lamivudine(Epivir) ")




        elif (user == "SPANISH FLU" or user == "SWINE FLU" or user == "swine flu" or user == "I have swine flu" or user == "I have Swine flu" or user == "spanish flu"):
                    txt.insert(END,"\n" + "Medicines: You sholud visit your doctor and doctor will conduct some physical exam to confirm")




        elif (user == "chikungunya" or user == "CHIKUNGUNYA" or user == "Chikungunya" or user == "I have Chikungunya" or user == "I have chikungunya"):
            txt.insert(END,"\n" + "Medicines: Acetaminophen (Tylenol), Paracetamol")





        elif (user == "VARICELLA" or user == "varicella" or user == "Varicella" or user == "I have varicella" or user == "I have Varicella"):
                    txt.insert(END,"\n" + "Medicines: Analgesic(relieves pain), Antihistamines(to reduce or stop allergic reaction)"
                            +"\n"+"But you should consult doctor for medical advice")




        
        elif (user == "DENGUE" or user == "Dengue" or user == "dengue" or user == "I have dengue" or user == "I have Dengue"):
            txt.insert(END,"\n"+"But you should consult doctor for medical advice")




        else:
                    txt.insert(END, "\n" + "Bot -> Sorry! I didn't get you")
        e.delete(0, END)





        tokens = word_tokenize(user_input)
        tags = pos_tag(tokens)
        for tag in tags:
            if tag[1] == "NN" or tag[1] == "NNS":
                print("I'm sorry, I'm not able to diagnose medical conditions based on the information you provided.")
            else:
                print(
                    "I'm sorry, I didn't understand what you said. Could you please rephrase your question or statement?")



    txt = Text(root)

    txt.grid(row=0, column=0, columnspan=4)
    e = Entry(root, width=100)
    e.grid(row=1, column=0)
    send = Button(root, text="Send", command=send).grid(row=1, column=1)
    #root.mainloop()


root = Tk()



root.geometry("800x800")
bt = Button(root, text="Open HealthBot", bg="blue", fg="white",command=mywindow)
bt.pack(pady=10,side=BOTTOM)
lbl1 = Label(root, text="HEALTH BOT, designed & developed by RISHITA SHARMA AND SANJEEVANI GUPTA")
lbl1.config(font=("Arial", 18))
lbl1.pack(pady=20,side=BOTTOM)



labelr = Label(root, text="Welcome to HealthBot")
labelr.pack(side="left", anchor="w")



labell = Label(root, text="Happy to Serve You")
labell.pack(side="right",anchor="e")
canvas = Canvas(root, width = 1920, height = 1080)
canvas.pack()
root.configure(background='navy blue')
img = PhotoImage(file="ChatBot.png")
canvas.create_image(250,100, anchor=NW, image=img)



canvas.create_text(800, 50, text="WELCOME TO HEALTHBOT", fill="black", font=('Times 25 bold'))

canvas.pack()




mainloop()
import tkinter as tk
from tkinter import messagebox



def submit_form():
    # Get input from user
    name = entry_name.get()
    email = entry_email.get()
    contact = entry_contact.get()
    message = entry_message.get("1.0", END)



    # Validate input
    if name == "" or email == "" or contact == "" or message == "":
        messagebox.showerror("Error", "Please fill in all fields.")
    else:
        # Save the form data to a file or send it to a database
        # You can customize this part to fit your needs
        messagebox.showinfo("Success", "Thank you for contacting us! We will get back to you soon.")

        # Clear the form fields
        entry_name.delete(0, END)
        entry_email.delete(0, END)
        entry_contact.delete(0, END)
        entry_message.delete("1.0", END)




# Create a window
window = Tk()
window.title("Contact Us")
window.geometry("1500x1000")



canvas = tk.Canvas(window, bg="purple")



# Create a label
lbl_1 = Label(window, text="HEALTH BOT")
lbl_1.config(font=("Arial", 14))
lbl_1.pack(pady=20)



lbl = Label(window, text="FEEDBACK")
lbl.config(font=("Arial", 18))
lbl.pack(pady=20)



# Create a label and an entry field for name
lbl_name = Label(window, text="Name:")
lbl_name.pack()
entry_name = Entry(window, width=30)
entry_name.pack()



# Create a label and an entry field for email
lbl_email = Label(window, text="Email:")
lbl_email.pack()
entry_email = Entry(window, width=30)
entry_email.pack()



# Create a label and an entry field for contact
lbl_contact = Label(window, text="Contact:")
lbl_contact.pack()
entry_contact = Entry(window, width=30)
entry_contact.pack()




# Create a label and a text field for message
lbl_message = Label(window, text="Feedback or Query:")
lbl_message.pack()
entry_message = Text(window, height=5, width=30)
entry_message.pack()




btn_submit = Button(window, text="Submit", padx=20, pady=10, bg="#0099ff", fg="white", command=submit_form)
btn_submit.pack(pady=10)




labelm = Label(window, text="Thank you for using our HealthBot."+"\n"+"DISCLAIMER"+
                            "\n"+"This HealthBot can provide medical advice to adults only."+"\n"+
                            "NOT meant for infants and pregnant women.",font=("Helvetica",14))
labelm.config(font=("Helvetica",16))
labelm.pack(side="left",anchor="w")



lbl1 = Label(window, text="HEALTH BOT, designed & developed by RISHITA SHARMA AND SANJEEVANI GUPTA")
lbl1.config(font=("Arial", 18))
lbl1.pack(pady=20,side=BOTTOM)



bgimg= tk.PhotoImage(file="healthbotpic.png")
limg= Label(window, i=bgimg)
limg.pack()



window.mainloop()
import tkinter as tk


class NavigationApp(tk.Frame):
    def _init_(self, master=None):
        super()._init_(master)
        self.master = master
        self.pack()
        self.create_widgets()


    def create_widgets(self):
        # Create buttons for navigation
        self.btn_prev = tk.Button(self, text='Previous', command=self.navigate_prev)
        self.btn_prev.pack(side='left')


        self.btn_next = tk.Button(self, text='Next', command=self.navigate_next)
        self.btn_next.pack(side='left')


        # Create label to display current page number
        self.lbl_page = tk.Label(self, text='Page 1')
        self.lbl_page.pack(side='left')



    def navigate_prev(self):
        # Logic for navigating to the previous page
        current_page = int(self.lbl_page.cget('text').split(' ')[1])
        if current_page > 1:
            self.lbl_page.config(text=f'Page {current_page - 1}')


    def navigate_next(self):
        # Logic for navigating to the next page
        current_page = int(self.lbl_page.cget('text').split(' ')[1])
        self.lbl_page.config(text=f'Page {current_page + 1}')

# Create the main window
root = tk.Tk()


# Set the window title
root.title("Login")
# Set the window size
root.geometry("400x300")


# Set the background image
bg_image = tk.PhotoImage(file="chatbot1.png")
bg_label = tk.Label(root, image=bg_image)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)


lbletitle = tk.Label(root, text="Premium Membership Registration")
lbletitle.config(font=("Harlow Solid Italic", 28))
lbletitle.pack(pady=20,side=TOP)


text_label = tk.Label(root, text="The above form can be used to provide your valuable feedback and also join our membership to get exclusive discounts on health checkup"+"\n"+"being a premium member will also help you book appointments with specilist doctors in a jiffy!"+"\n"+ "So hurry!REGISTER NOW!!"+"\n"+"Pre-register to be on our priority list.", font=("Arial",18))
text_label.place(relx=0.5, rely=0.5, anchor="center")


lble1 = tk.Label(root, text="HEALTH BOT, designed & developed by RISHITA SHARMA AND SANJEEVANI GUPTA")
lble1.config(font=("Arial", 18))
lble1.pack(pady=20,side=BOTTOM)

# Create the username label and entry field
username_label = tk.Label(root, text="Username:")
username_label.place(x=50, y=100)
username_entry = tk.Entry(root)
username_entry.place(x=150, y=100)


# Create the password label and entry field
password_label = tk.Label(root, text="Password:")
password_label.place(x=50, y=150)
password_entry = tk.Entry(root, show="*")
password_entry.place(x=150, y=150)


# Create the login button
login_button = tk.Button(root, text="Login")
login_button.place(x=150, y=200)


#root.mainloop()

app = NavigationApp(master=root)

app.mainloop()

root.mainloop()
