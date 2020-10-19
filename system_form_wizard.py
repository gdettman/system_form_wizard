from tkinter import *
from tkinter import ttk
import math
import error_handling as error
import system as t1
import battery as t2
import rack_xy as t3

class Fields:
    """Parent class containing fields and defaults for all other classes"""
    def frame_fields(self):
        self.tab0_text = "Start"
        self.tab1_text = "System Details"
        self.tab2_text = "Battery Details"
        self.tab3_text = "Rack X & Y Axis"
        self.tab4_text = "Rack Z Axis"
        self.tab5_text = "Summary"

    def frame_defaults(self):
        self.message1=StringVar(value="")
        self.message2=StringVar(value="")
        self.message3=StringVar(value="")

    def system_fields(self):
        self.lx_string_list = ["1 string", "2 strings", "3 strings", "4 strings",
                                "5 strings", "6 strings", "7 strings", "8 strings"]
        self.mx_string_list = ["1 string", "2 strings", "3 strings", "4 strings"]
        self.block_voltage_list = ["12V", "2V", "1.2V", "3.6V", 
                                    "4V", "6V", "8V", "16V"]
        self.model_list = ["LX", "MX"]
        self.lx_supply_list = ["110/230VAC", "110VAC", "48VDC", "24VDC"]
        self.mx_supply_list = ["110/230VAC", "24/48VDC"]
        self.port_list = ["None", "RS485"]
        self.max_current_list = ["0 to 100A", "100 to 200A", "200 to 500A", "500 to 800A"]
    
    def system_defaults(self):
        self.systems = IntVar(value="")
        self.strings = StringVar(value="")
        self.blocks = IntVar(value="")
        self.model = StringVar(value="")
        self.block_voltage = StringVar(value="")
        self.supply = StringVar(value="")
        self.max_current = StringVar(value="")
        self.port2 = StringVar(value="")

    def battery_fields(self):
        self.term_size_list = ["6mm", "8mm", "10mm", "12mm"]
        self.term_pos_list = ["Front", "Top"]
        self.term_align_list = ["Width", "Length"]
        self.term_number_list = ["2", "4+"]
    
    def battery_defaults(self):
        self.block_length = DoubleVar(value="")
        self.block_width = DoubleVar(value="")
        self.block_height = DoubleVar(value="")
        self.term_size = StringVar(value="")
        self.term_align = StringVar(value="")
        self.term_pos = StringVar(value="")
        self.term_number = StringVar(value="")
        try:
            self.batt_canvas.destroy()
            self.batt_canvas = Canvas(frame.tab2, height=150, width=150)
            self.batt_canvas.grid(row=3, rowspan=4, column=7)
        except:
            pass
        
    def rack_xy_fields(self):
        self.num_rows_list = [i for i in range(1,9)]

    def rack_xy_defaults(self):
        self.row_width = DoubleVar(value="")
        self.row_height = DoubleVar(value="500")
        self.block_distance = DoubleVar(value="25")
        self.row_var1 = IntVar(value="")
        self.row_var2 = IntVar(value="")
        self.row_var3 = IntVar(value="")
        self.row_var4 = IntVar(value="")
        self.row_var5 = IntVar(value="")
        self.row_var6 = IntVar(value="")
        self.row_var7 = IntVar(value="")
        self.row_var8 = IntVar(value="")
        self.destroy_rows()
        
    def rack_z_fields(self):
        pass

    def rack_z_defaults(self):
        pass

    def summary_fields(self):
        pass
    
    def summary_defaults(self):
        pass

class Frame(Fields):
    """GUI frame setup"""
    def __init__(self, master):
        super().frame_fields()
        super().frame_defaults()
        self.master = master
        master.title("PowerShield System Form Wizard")
        master.resizable(False, False)

        self.custom_tabs = ttk.Style()
        self.custom_tabs.configure('Custom.TNotebook.Tab', padding=[1, 7])

        self.notebook = ttk.Notebook(master, style='Custom.TNotebook')
        self.notebook.bind('<<NotebookTabChanged>>', self.tab_click)
        self.tab0 = ttk.Frame(self.notebook)
        self.tab1 = ttk.Frame(self.notebook)
        self.tab2 = ttk.Frame(self.notebook)
        self.tab3 = ttk.Frame(self.notebook)
        self.tab4 = ttk.Frame(self.notebook)
        self.tab5 = ttk.Frame(self.notebook)
        self.notebook.add(self.tab0, text=self.tab0_text)
        self.notebook.add(self.tab1, text=self.tab1_text)
        self.notebook.add(self.tab2, text=self.tab2_text)
        self.notebook.add(self.tab3, text=self.tab3_text)
        self.notebook.add(self.tab4, text=self.tab4_text)
        self.notebook.add(self.tab5, text=self.tab5_text)
        self.notebook.grid(row=1,column=1)
        
        self.bottom = ttk.Frame(master)
        self.bottom.grid(row=2,column=1)
        
        self.right = ttk.LabelFrame(master, text="Values")
        self.right.grid(row=1,column=3, sticky=N, padx=1, pady=28)

        self.message_line1 = ttk.Label(self.bottom, justify="center", textvariable=self.message1)
        self.message_line1.grid(row=1, rowspan= 2, column=1, columnspan=3, ipady=2, padx=5, pady=5)

        self.message_line2 = ttk.Label(self.bottom, justify="center", textvariable=self.message2)
        self.message_line2.grid(row=2, rowspan= 2, column=1, columnspan=3, ipady=2, padx=5, pady=5)

        self.message_line3 = ttk.Label(self.bottom, justify="center", textvariable=self.message3)
        self.message_line3.grid(row=3, rowspan= 2, column=1, columnspan=3, ipady=2, padx=5, pady=5)

        self.back_button = ttk.Button(self.bottom, text="Back", command=self.back_button)
        self.back_button.grid(row=3, column=1, ipady=2, padx=5, pady=5)

        self.reset_button = ttk.Button(self.bottom, text="Reset", command=self.reset_button)
        self.reset_button.grid(row=3, column=2, ipady=2, padx=5, pady=5)

        self.next_button = ttk.Button(self.bottom, text="Next", command=self.next_button)
        self.next_button.grid(row=3, column=3, ipady=2, padx=5, pady=5)
    
    def get_current_tab(self, *args): #bound to notebook tab changes
        #print("get current <tab changed>", self.notebook.tab(self.notebook.select(), "text"))
        return self.notebook.tab(self.notebook.select(), "text")

    def tab_click(self, *args): #bound to notebook tab changes
        #print("tab click <tab changed>", self.notebook.tab(self.notebook.select(), "text"))
        self.tab_functions()
        return self.notebook.tab(self.notebook.select(), "text")

    def tab_functions(self):
        if self.get_current_tab() == self.tab0_text:
            pass
        elif self.get_current_tab() == self.tab1_text:
            pass
        elif self.get_current_tab() == self.tab2_text:
            pass
        elif self.get_current_tab() == self.tab3_text:
            pass
        elif self.get_current_tab() == self.tab4_text:
            pass
        elif self.get_current_tab() == self.tab5_text:
            pass

    def next_button(self, *args):
        if self.get_current_tab() == self.tab0_text:
            self.notebook.select(1)
        elif self.get_current_tab() == self.tab1_text:
            r_systems = ttk.Label(self.right, text=t1)
            r_systems.grid(row=1, column=1)
            self.notebook.select(2)
        elif self.get_current_tab() == self.tab2_text:
            self.notebook.select(3)
        elif self.get_current_tab() == self.tab3_text:
            self.notebook.select(4)
        elif self.get_current_tab() == self.tab4_text:
            self.notebook.select(5)
        elif self.get_current_tab() == self.tab5_text:
            pass
    
    def back_button(self, *args):
        if self.get_current_tab() == self.tab0_text:
            pass
        elif self.get_current_tab() == self.tab1_text:
            self.notebook.select(0)
        elif self.get_current_tab() == self.tab2_text:
            self.notebook.select(1)
        elif self.get_current_tab() == self.tab3_text:
            self.notebook.select(2)
        elif self.get_current_tab() == self.tab4_text:
            self.notebook.select(3)
        elif self.get_current_tab() == self.tab5_text:
            self.notebook.select(4)

    def reset_button(self, *args):
        if self.get_current_tab() == self.tab0_text:
            pass
        elif self.get_current_tab() == self.tab1_text:
            t1.reset()
        elif self.get_current_tab() == self.tab2_text:
            t2.reset()
        elif self.get_current_tab() == self.tab3_text:
            t3.reset()
        elif self.get_current_tab() == self.tab4_text:
            pass
        elif self.get_current_tab() == self.tab5_text:
            pass

root = Tk()
t1()
t2()
t3()
frame = Frame(root)
root.mainloop()