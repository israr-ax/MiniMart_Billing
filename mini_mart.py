import tkinter as tk
from tkinter import messagebox
import random


class BillApp:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.configure(bg="#F5F5DC")
        self.root.title("Mini Mart Billing System")

        title = tk.Label(self.root, text="Mini Mart Billing System", bd=12, relief=tk.RIDGE, font=("Arial Black", 20),
                         bg="#654321", fg="white")
        title.pack(fill=tk.X)

        # Variables
        self.nutella = tk.IntVar()
        self.noodles = tk.IntVar()
        self.lays = tk.IntVar()
        self.oreo = tk.IntVar()
        self.muffin = tk.IntVar()
        self.silk = tk.IntVar()
        self.namkeen = tk.IntVar()
        self.atta = tk.IntVar()
        self.pasta = tk.IntVar()
        self.rice = tk.IntVar()
        self.oil = tk.IntVar()
        self.sugar = tk.IntVar()
        self.dal = tk.IntVar()
        self.tea = tk.IntVar()
        self.soap = tk.IntVar()
        self.shampoo = tk.IntVar()
        self.lotion = tk.IntVar()
        self.cream = tk.IntVar()
        self.foam = tk.IntVar()
        self.mask = tk.IntVar()
        self.sanitizer = tk.IntVar()
        self.total_snacks_price = tk.StringVar()
        self.total_grocery_price = tk.StringVar()
        self.total_hygiene_price = tk.StringVar()
        self.snacks_tax = tk.StringVar()
        self.grocery_tax = tk.StringVar()
        self.hygiene_tax = tk.StringVar()
        self.customer_name = tk.StringVar()
        self.bill_no = tk.StringVar()
        self.phone = tk.StringVar()
        self.total_bill = tk.StringVar()

        self.bill_no.set(str(random.randint(1000, 9999)))

        # Customer Details
        details_frame = tk.LabelFrame(self.root, text="Customer Details", font=("Arial Black", 12), bg="#654321",
                                      fg="white", relief=tk.GROOVE, bd=10)
        details_frame.place(x=0, y=80, relwidth=1)

        tk.Label(details_frame, text="Customer Name", font=("Arial Black", 14), bg="#654321", fg="white").grid(row=0,
                                                                                                               column=0,
                                                                                                               padx=15)
        tk.Entry(details_frame, borderwidth=4, width=30, textvariable=self.customer_name).grid(row=0, column=1, padx=8)

        tk.Label(details_frame, text="Contact No.", font=("Arial Black", 14), bg="#654321", fg="white").grid(row=0,
                                                                                                             column=2,
                                                                                                             padx=10)
        tk.Entry(details_frame, borderwidth=4, width=30, textvariable=self.phone).grid(row=0, column=3, padx=8)

        tk.Label(details_frame, text="Bill No.", font=("Arial Black", 14), bg="#654321", fg="white").grid(row=0,
                                                                                                          column=4,
                                                                                                          padx=10)
        tk.Entry(details_frame, borderwidth=4, width=30, textvariable=self.bill_no).grid(row=0, column=5, padx=8)

        # Menu
        self.create_menu_section("Snacks", 5, 180, 380, [
            ("Nutella", self.nutella),
            ("Noodles", self.noodles),
            ("Lays", self.lays),
            ("Oreo", self.oreo),
            ("Muffin", self.muffin),
            ("Kitkat", self.silk),
            ("Namkeen ", self.namkeen)
        ])

        self.create_menu_section("Grocery ", 340, 180, 380, [
            ("Flour", self.atta),
            ("Pasta", self.pasta),
            ("Basmathi Rice", self.rice),
            ("Oil", self.oil),
            ("Sugar", self.sugar),
            ("Daal", self.dal),
            ("Tea", self.tea)
        ])

        self.create_menu_section("Beauty & Hygiene", 677, 180, 380, [
            ("Soap", self.soap),
            ("Shampoo", self.shampoo),
            ("Lotion", self.lotion),
            ("Cream", self.cream),
            ("foam", self.foam),
            ("Mask", self.mask),
            ("Senizer", self.sanitizer)
        ])



        # Bill Area
        bill_area_frame = tk.Frame(self.root, bd=10, relief=tk.GROOVE, bg="#D2B48C")
        bill_area_frame.place(x=1010, y=188, width=330, height=372)

        bill_title = tk.Label(bill_area_frame, text="Bill Area", font=("Arial Black", 17), bd=7, relief=tk.GROOVE,
                              bg="#D2B48C", fg="#333333")
        bill_title.pack(fill=tk.X)

        scrol_y = tk.Scrollbar(bill_area_frame, orient=tk.VERTICAL)
        self.txtarea = tk.Text(bill_area_frame, yscrollcommand=scrol_y.set)
        scrol_y.pack(side=tk.RIGHT, fill=tk.Y)
        scrol_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=tk.BOTH, expand=1)

        # Billing Summary
        billing_summary_frame = tk.LabelFrame(self.root, text="Billing Summary", font=("Arial Black", 12),
                                              relief=tk.GROOVE, bd=10, bg="#654321", fg="white")
        billing_summary_frame.place(x=0, y=560, relwidth=1, height=137)

        tk.Label(billing_summary_frame, text="Total Snacks Price", font=("Arial Black", 11), bg="#654321",
                 fg="white").grid(row=0, column=0)
        tk.Entry(billing_summary_frame, width=30, borderwidth=2, textvariable=self.total_snacks_price).grid(row=0,
                                                                                                            column=1,
                                                                                                            padx=10,
                                                                                                            pady=7)

        tk.Label(billing_summary_frame, text="Total Grocery Price", font=("Arial Black", 11), bg="#654321",
                 fg="white").grid(row=1, column=0)
        tk.Entry(billing_summary_frame, width=30, borderwidth=2, textvariable=self.total_grocery_price).grid(row=1,
                                                                                                             column=1,
                                                                                                             padx=10,
                                                                                                             pady=7)

        tk.Label(billing_summary_frame, text="Total Beauty & Hygiene Price", font=("Arial Black", 11), bg="#654321",
                 fg="white").grid(row=2, column=0)
        tk.Entry(billing_summary_frame, width=30, borderwidth=2, textvariable=self.total_hygiene_price).grid(row=2,
                                                                                                             column=1,
                                                                                                             padx=10,
                                                                                                             pady=7)

        tk.Label(billing_summary_frame, text="Snacks Tax", font=("Arial Black", 11), bg="#654321", fg="white").grid(
            row=0, column=2)
        tk.Entry(billing_summary_frame, width=30, borderwidth=2, textvariable=self.snacks_tax).grid(row=0, column=3,
                                                                                                    padx=10, pady=7)

        tk.Label(billing_summary_frame, text="Grocery Tax", font=("Arial Black", 11), bg="#654321", fg="white").grid(
            row=1, column=2)
        tk.Entry(billing_summary_frame, width=30, borderwidth=2, textvariable=self.grocery_tax).grid(row=1, column=3,
                                                                                                     padx=10, pady=7)

        tk.Label(billing_summary_frame, text="Beauty & Hygiene Tax", font=("Arial Black", 11), bg="#654321",
                 fg="white").grid(row=2, column=2)
        tk.Entry(billing_summary_frame, width=30, borderwidth=2, textvariable=self.hygiene_tax).grid(row=2, column=3,
                                                                                                     padx=10, pady=7)

        button_frame = tk.Frame(billing_summary_frame, bd=7, relief=tk.GROOVE, bg="#D2B48C")
        button_frame.place(x=830, width=500, height=95)

        tk.Button(button_frame, text="Total Bill", font=("Arial Black", 15), pady=10, bg="#D2B48C", fg="#333333",
                  command=self.total).grid(row=0, column=0, padx=12)
        tk.Button(button_frame, text="Clear Field", font=("Arial Black", 15), pady=10, bg="#D2B48C", fg="#333333",
                  command=self.clear).grid(row=0, column=1, padx=10, pady=6)
        tk.Button(button_frame, text="Exit", font=("Arial Black", 15), pady=10, bg="#D2B48C", fg="#333333",
                  command=self.exit).grid(row=0, column=2, padx=10, pady=6)

    def create_menu_section(self, title, x, y, width, items):
        frame = tk.LabelFrame(self.root, text=title, font=("Arial Black", 12), bg="#654321", fg="white",
                              relief=tk.GROOVE, bd=10)
        frame.place(x=x, y=y, width=width, height=372)

        for index, (item, var) in enumerate(items):
            tk.Label(frame, text=item, font=("Arial Black", 11), bg="#654321", fg="white").grid(row=index, column=0,
                                                                                                padx=10, pady=5,
                                                                                                sticky="w")
            tk.Entry(frame, borderwidth=2, textvariable=var, width=18).grid(row=index, column=1, padx=10, pady=5)

    def total(self):
        self.calculate_snacks_total()
        self.calculate_grocery_total()
        self.calculate_hygiene_total()

        self.snacks_tax.set(f"Rs. {self.calculate_tax(float(self.total_snacks_price.get()))}")
        self.grocery_tax.set(f"Rs. {self.calculate_tax(float(self.total_grocery_price.get()))}")
        self.hygiene_tax.set(f"Rs. {self.calculate_tax(float(self.total_hygiene_price.get()))}")

        total_tax = float(self.snacks_tax.get().split(' ')[1]) + float(self.grocery_tax.get().split(' ')[1]) + float(
            self.hygiene_tax.get().split(' ')[1])
        total_bill = float(self.total_snacks_price.get()) + float(self.total_grocery_price.get()) + float(
            self.total_hygiene_price.get()) + total_tax
        self.total_bill.set(f"Rs. {total_bill}")

        self.bill_area()

    def calculate_snacks_total(self):
        snacks_total = sum([self.nutella.get(), self.noodles.get(), self.lays.get(), self.oreo.get(), self.muffin.get(),
                            self.silk.get(), self.namkeen.get()]) * 20
        self.total_snacks_price.set(snacks_total)

    def calculate_grocery_total(self):
        grocery_total = sum(
            [self.atta.get(), self.pasta.get(), self.rice.get(), self.oil.get(), self.sugar.get(), self.dal.get(),
             self.tea.get()]) * 50
        self.total_grocery_price.set(grocery_total)

    def calculate_hygiene_total(self):
        hygiene_total = sum(
            [self.soap.get(), self.shampoo.get(), self.lotion.get(), self.cream.get(), self.foam.get(), self.mask.get(),
             self.sanitizer.get()]) * 30
        self.total_hygiene_price.set(hygiene_total)

    def calculate_tax(self, amount):
        return round(amount * 0.05, 2)

    def clear(self):
        self.txtarea.delete(1.0, tk.END)
        self.total_snacks_price.set("")
        self.total_grocery_price.set("")
        self.total_hygiene_price.set("")
        self.snacks_tax.set("")
        self.grocery_tax.set("")
        self.hygiene_tax.set("")
        self.customer_name.set("")
        self.bill_no.set(str(random.randint(1000, 9999)))
        self.phone.set("")
        self.nutella.set(0)
        self.noodles.set(0)
        self.lays.set(0)
        self.oreo.set(0)
        self.muffin.set(0)
        self.silk.set(0)
        self.namkeen.set(0)
        self.atta.set(0)
        self.pasta.set(0)
        self.rice.set(0)
        self.oil.set(0)
        self.sugar.set(0)
        self.dal.set(0)
        self.tea.set(0)
        self.soap.set(0)
        self.shampoo.set(0)
        self.lotion.set(0)
        self.cream.set(0)
        self.foam.set(0)
        self.mask.set(0)
        self.sanitizer.set(0)

    def exit(self):
        self.root.destroy()

    def bill_area(self):
        self.txtarea.delete(1.0, tk.END)
        self.txtarea.insert(tk.END, f"\nBill No.: {self.bill_no.get()}")
        self.txtarea.insert(tk.END, f"\nCustomer Name: {self.customer_name.get()}")
        self.txtarea.insert(tk.END, f"\nPhone Number: {self.phone.get()}")
        self.txtarea.insert(tk.END, f"\n====================================")
        self.txtarea.insert(tk.END, f"\nProducts\t\tQTY\t\tPrice")
        self.txtarea.insert(tk.END, f"\n====================================")

        self.insert_item_in_bill("Nutella", self.nutella.get(), 20)
        self.insert_item_in_bill("Noodles", self.noodles.get(), 20)
        self.insert_item_in_bill("Lays", self.lays.get(), 20)
        self.insert_item_in_bill("Oreo", self.oreo.get(), 20)
        self.insert_item_in_bill("Muffin", self.muffin.get(), 20)
        self.insert_item_in_bill("Silk", self.silk.get(), 20)
        self.insert_item_in_bill("Namkeen", self.namkeen.get(), 20)
        self.insert_item_in_bill("Atta", self.atta.get(), 50)
        self.insert_item_in_bill("Pasta", self.pasta.get(), 50)
        self.insert_item_in_bill("Rice", self.rice.get(), 50)
        self.insert_item_in_bill("Oil", self.oil.get(), 50)
        self.insert_item_in_bill("Sugar", self.sugar.get(), 50)
        self.insert_item_in_bill("Dal", self.dal.get(), 50)
        self.insert_item_in_bill("Tea", self.tea.get(), 50)
        self.insert_item_in_bill("Soap", self.soap.get(), 30)
        self.insert_item_in_bill("Shampoo", self.shampoo.get(), 30)
        self.insert_item_in_bill("Lotion", self.lotion.get(), 30)
        self.insert_item_in_bill("Cream", self.cream.get(), 30)
        self.insert_item_in_bill("Foam", self.foam.get(), 30)
        self.insert_item_in_bill("Mask", self.mask.get(), 30)
        self.insert_item_in_bill("Sanitizer", self.sanitizer.get(), 30)

        self.txtarea.insert(tk.END, f"\n------------------------------------")
        self.txtarea.insert(tk.END, f"\nTotal Snacks Price: \t\t\tRs. {self.total_snacks_price.get()}")
        self.txtarea.insert(tk.END, f"\nTotal Grocery Price: \t\t\tRs. {self.total_grocery_price.get()}")
        self.txtarea.insert(tk.END, f"\nTotal Hygiene Price: \t\t\tRs. {self.total_hygiene_price.get()}")
        self.txtarea.insert(tk.END, f"\nSnacks Tax: \t\t\t{self.snacks_tax.get()}")
        self.txtarea.insert(tk.END, f"\nGrocery Tax: \t\t\t{self.grocery_tax.get()}")
        self.txtarea.insert(tk.END, f"\nHygiene Tax: \t\t\t{self.hygiene_tax.get()}")
        self.txtarea.insert(tk.END, f"\nTotal Bill: \t\t\t{self.total_bill.get()}")
        self.txtarea.insert(tk.END, f"\n====================================")
        self.txtarea.insert(tk.END, f"\nThank you for shopping with us!")
        self.txtarea.insert(tk.END, f"\n====================================")

    def insert_item_in_bill(self, item, qty, price):
        if qty != 0:
            self.txtarea.insert(tk.END, f"\n{item}\t\t{qty}\t\t{qty * price}")


if __name__ == "__main__":
    root = tk.Tk()
    app = BillApp(root)
    root.mainloop()
