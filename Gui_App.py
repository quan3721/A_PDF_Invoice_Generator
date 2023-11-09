# --- Project about A PDF Invoice Generator ( Medicines )  --- #

# -- Import Libraries -- #
from tkinter import *
from fpdf import FPDF

# -- Create a new window -- #
window = Tk()

# -- Create title for the window -- #
window.title("Invoice Generator")

# -- Create a directory contain info medicine -- #
medicines = {
    "MedicineA":10,
    "MedicineB":20,
    "MedicineC":15,
    "MedicineD":20
}

# -- Create a list to contain information of invoice -- #
invoice_items = []

# -- Create a function to add medicine -- #
def add_medicine():
    selected_medicine = medicine_listbox.get(ANCHOR) # get the value name of medicine
    # print(selected_medicine)
    quantity = int(quantity_entry.get()) # -- get the quantity of medicine after entering quantity
    price = medicines[selected_medicine] # -- get the price of each medicine from medicines directory
    item_total = price * quantity # -- calculate total price
    invoice_items.append((selected_medicine, quantity, item_total)) # -- add information to invoice items list
    # print(invoice_items)

    total_amount_entry.delete(0, END) # -- Refresh data after select more medinces
    total_amount_entry.insert(END, str(calculate_total()))
    update_invoice_text()

# -- Create a function to calculate total amount of invoice -- #
def calculate_total():
    total = 0.9
    for item in invoice_items:
        total = total + item[2]
    return total


# -- Create a function to update data for text box -- #
def update_invoice_text():
    invoice_text.delete(1.0, END) # -- delete data to refresh trong đó 1.0 ( first line and 0 column index )
    for item in invoice_items:
        invoice_text.insert(END, f"Medicine: {item[0]}, Quantity: {item[1]}, Total: {item[2]} \n") # -- insert data, start from beggining

def generate_invoice_to_pdf():
    customer_name = customer_entry.get() # -- get the name customer

    # -- Create a pdf file -- #
    pdf =FPDF()
    pdf.add_page() # add page for pdf
    pdf.set_font("Helvetica", size=12) # -- set font size of content of pdf file

    pdf.cell(0, 10, text="Invoice", new_x="LMARGIN", new_y="NEXT", align="C") # create a content for header
    pdf.cell(0, 10, text="Customer: "+customer_name, new_x="LMARGIN", new_y="NEXT", align="L")
    pdf.cell(0, 10, text="", new_x="LMARGIN", new_y="NEXT")

    for item in invoice_items:
        medicine_name, quantity, item_total = item
        pdf.cell(0, 10, text=f"Medicine: {medicine_name}, Quantity: {quantity}, Total: {item_total}",
                 new_x="LMARGIN", new_y="NEXT", align="L")

    pdf.cell(0,10, text="Total Amount: "+str(calculate_total()), new_x="LMARGIN", new_y="NEXT", align="L")
    pdf.output("invoice.pdf")
    print("Successful !")

# -- Create label for medicine -- #
medicine_label = Label(window, text="Medicine: ")
medicine_label.pack()

# -- Create list box for choose kind of medicines -- #
medicine_listbox = Listbox(window, selectmode=SINGLE)
for medicine in medicines: # add information of medicines into list box
    medicine_listbox.insert(END,medicine)
    # print(medicine)
medicine_listbox.pack()

# -- Create an entry for entering quantity of medicine -- # ( số lượng )
quantity_label = Label(window, text="Quantity") # -- create label for quantity
quantity_label.pack()
quantity_entry = Entry(window)
quantity_entry.pack()

# -- Create button -- #
add_button = Button(window, text="Add Medicine", command=add_medicine)
add_button.pack()

# -- Create total amount of medicines -- #
total_amount_label = Label(window, text="Total amount")
total_amount_label.pack()
total_amount_entry = Entry(window)
total_amount_entry.pack()

# -- Create label and entry for entering name customer -- #
customer_label = Label(window, text='Customer Name:')
customer_label.pack()
customer_entry = Entry(window)
customer_entry.pack()

# -- Create a button for generating to PDF file -- #
generate_button = Button(window, text="Generate Invoice", command=generate_invoice_to_pdf)
generate_button.pack()

# -- Create a text box to show the information -- #
invoice_text = Text(window, height=10, width=50)
invoice_text.pack()

# -- Create a loop to show the window -- #
window.mainloop()
