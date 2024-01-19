import tkinter as tk
from tkinter import messagebox

class Contactbook:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Book")

        self.contacts = []

        #creating main_frame

        self.main_frame = tk.Frame(root,bg='coral',highlightthickness=5,highlightbackground='black',width=500,height=400)
        self.main_frame.place(x=10,y=10)

        #creating name label and entry field

        self.name_label = tk.Label(self.main_frame,bg='coral',text="Name:",font=('bold',10))
        self.name_label.place(x=10,y=10)

        self.name_entry = tk.Entry(self.main_frame)
        self.name_entry.place(x=70,y=10)

        #creating phone number label and entry field

        self.phone_label = tk.Label(self.main_frame,bg='coral',text="Phone:",font=('bold',10))
        self.phone_label.place(x=10,y=50)

        self.phone_entry = tk.Entry(self.main_frame)
        self.phone_entry.place(x=70,y=50)
        
        #creating email label and entry field

        self.email_label = tk.Label(self.main_frame,bg='coral',text="Email:",font=('bold',10))
        self.email_label.place(x=10,y=90)

        self.email_entry = tk.Entry(self.main_frame)
        self.email_entry.place(x=70,y=90)

        #creating address label and entry field

        self.address_label = tk.Label(self.main_frame,bg='coral', text="Address:",font=('bold',10))
        self.address_label.place(x=10,y=130)

        self.address_entry = tk.Entry(self.main_frame)
        self.address_entry.place(x=70,y=130)

        #creating Listbox to display all contacts

        self.contacts_listbox = tk.Listbox(self.main_frame, selectmode=tk.SINGLE,width=60,height=9)
        self.contacts_listbox.place(x=120,y=190)

        #creating Listbox to display search results
        self.search_results_listbox = tk.Listbox(self.main_frame, selectmode=tk.SINGLE,width=40,height=6)
        self.search_results_listbox.place(x=240,y=50)


        # Buttons
        self.add_button = tk.Button(self.main_frame, text="Add Contact", command=self.add_contact)
        self.add_button.place(x=10,y=200)

        self.edit_button = tk.Button(self.main_frame, text="Edit Contact", command=self.edit_contact)
        self.edit_button.place(x=10,y=250)

        self.delete_button = tk.Button(self.main_frame, text="Delete Contact", command=self.delete_contact)
        self.delete_button.place(x=10,y=300)

        self.search_button = tk.Button(self.main_frame, text="Search Contact", command=self.search_contact)
        self.search_button.place(x=310,y=10)

    def update_contacts_listbox(self):
        self.contacts_listbox.delete(0, tk.END)
        for contact in self.contacts:
            self.contacts_listbox.insert(tk.END,  contact["name"], contact["phone"])

    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        self.name_entry.delete(0,tk.END)
        self.phone_entry.delete(0,tk.END)
        self.email_entry.delete(0,tk.END)
        self.address_entry.delete(0,tk.END) 
 
        if name and phone:
            self.contacts.append({"name": name, "phone": phone})
            self.update_contacts_listbox()
            messagebox.showinfo("Success", "Contact added successfully.")
            
        else:
            messagebox.showwarning("Error", "Please enter both name and phone.")
           

    def edit_contact(self):
        selected_index = self.contacts_listbox.curselection()
        if selected_index:
            selected_index = selected_index[0]
            name_to_edit = self.name_entry.get()
            new_phone = self.phone_entry.get()
            self.name_entry.delete(0,tk.END)    
            self.phone_entry.delete(0,tk.END)

            self.contacts[selected_index]["name"] = name_to_edit
            self.contacts[selected_index]["phone"] = new_phone
            self.update_contacts_listbox()
            messagebox.showinfo("Success", "Contact edited successfully.")
        else:
            messagebox.showwarning("Error", "Please select a contact to edit.")
            

    def delete_contact(self):
        selected_index = self.contacts_listbox.curselection()
        if selected_index:
            selected_index = selected_index[0]
            del self.contacts[selected_index]
            self.update_contacts_listbox()
            messagebox.showinfo("Success", "Contact deleted successfully.")
        else:
            messagebox.showwarning("Error", "Please select a contact to delete.")

    def search_contact(self):
        name_to_search = self.name_entry.get()

        # Clear previous search results and name_entry
        
        self.search_results_listbox.delete(0, tk.END)
        self.name_entry.delete(0,tk.END)

        for contact in self.contacts:
            if name_to_search.lower() in contact["name"].lower():
                self.search_results_listbox.insert(tk.END, contact["name"],contact["phone"])
            
if __name__ == "__main__":   
    root = tk.Tk()
    root.geometry('550x450')
    app = Contactbook(root)
    root.mainloop()