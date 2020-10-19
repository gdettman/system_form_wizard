from tkinter import *
from tkinter import ttk
import math
import error_handling as error

class Fields:
    """Parent class containing fields and defaults for all other classes"""
    def frame_fields(self):
        self.tab0_text = "Start"
        self.tab1_text = "System Details"
        self.tab2_text = "Battery Details"
        self.tab3_text = "Rack X & Y Axis"
        self.tab4_text = "Rack Z Axis"
        self.tab5_text = "Summary"
        # self.tab0_text_alt 
        # self.tab1_text_alt += *
        # self.tab2_text_alt = "Battery Details"
        # self.tab3_text_alt = "Rack X & Y Axis"
        # self.tab4_text_alt = "Rack Z Axis"
        # self.tab5_text_alt = "Summary"

    def frame_defaults(self):
        self.message1=StringVar(value="")
        self.message2=StringVar(value="")
        self.message3=StringVar(value="")

    def home_fields(self):
        pass

    def home_defaults(self):
        pass

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
        

        # tester1 = ttk.Label(self.right1, justify="right", text="No. of Systems")
        # tester2 = ttk.Entry(self.right1, textvariable="test")
        # tester1.grid(row=1, column=1 )
        # tester2.grid(row=1, column=2 )
        # tester3 = ttk.Label(self.right1, justify="right", text="No. of Systems")
        # tester4 = ttk.Entry(self.right1, textvariable="test")
        # tester3.grid(row=1, column=1 )
        # tester4.grid(row=1, column=2,columnspan=10 )
     


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
            #print("t0")
            pass
        elif self.get_current_tab() == self.tab1_text:
            #print("t1")
            pass
        elif self.get_current_tab() == self.tab2_text:
            #print("t2")
            pass
        elif self.get_current_tab() == self.tab3_text:
            #print("t3")
            pass
        elif self.get_current_tab() == self.tab4_text:
            #print("t4")
            pass
        elif self.get_current_tab() == self.tab5_text:
            #print("t5")
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

class Tab1(Fields):
    """System details tab"""
    def __init__(self):
        super().system_fields()
        self.reset()
        
        # defaults for ipady, padx, pady, width
        IY = 2      
        PX = 5
        PY = 5 
        WD = 12 

        systems_label = ttk.Label(frame.tab1, justify="right", text="No. of Systems")
        systems_entry = ttk.Entry(frame.tab1, textvariable=self.systems, width=WD+3)
        systems_label.grid(row=1, column=1, sticky=E, ipady=IY, padx=PX, pady=PY)
        systems_entry.grid(row=1, column=2, sticky=W, ipady=IY, padx=PX, pady=PY)
        
        model_label = ttk.Label(frame.tab1, justify="right", text="Controller\nType")
        model_combo = ttk.Combobox(frame.tab1, values=self.model_list, 
                                        textvariable=self.model, 
                                        state='readonly', width=WD)
        model_combo.bind('<<ComboboxSelected>>', self.get_model)
        model_label.grid(row=1, column=3, sticky=E, ipady=IY, padx=PX, pady=PY)
        model_combo.grid(row=1, column=4, sticky=W, ipady=IY, padx=PX, pady=PY)
       
        strings_label = ttk.Label(frame.tab1, justify="right", 
                                        text="No. of Strings*\nPer System")
        self.strings_combo = ttk.Combobox(frame.tab1, state='readonly',
                                        textvariable=self.strings, width=WD)
        self.strings_combo['state'] = 'disabled'
        self.strings_combo.bind('<<ComboboxSelected>>', self.get_strings)
        strings_label.grid(row=2, column=1, sticky=E, ipady=IY, padx=PX, pady=PY)
        self.strings_combo.grid(row=2, column=2, sticky=W, ipady=IY, padx=PX, pady=PY)
        
        block_voltage_label = ttk.Label(frame.tab1, justify="right", 
                                        text="Block Voltage")
        block_voltage_combo = ttk.Combobox(frame.tab1, values=self.block_voltage_list, 
                                        textvariable=self.block_voltage, 
                                        state='readonly', width=WD)
        block_voltage_combo.bind('<<ComboboxSelected>>', self.get_block_voltage)
        block_voltage_label.grid(row=2, column=3, sticky=E, ipady=IY, padx=PX, pady=PY)
        block_voltage_combo.grid(row=2, column=4, sticky=W, ipady=IY, padx=PX, pady=PY)

        blocks_label = ttk.Label(frame.tab1, justify="right", text="No. of Blocks\nPer String")
        blocks_entry = ttk.Entry(frame.tab1, textvariable=self.blocks, width=WD+3)
        blocks_label.grid(row=3, column=1, sticky=E, ipady=IY, padx=PX, pady=PY)
        blocks_entry.grid(row=3, column=2, sticky=W, ipady=IY, padx=PX, pady=PY)

        supply_label = ttk.Label(frame.tab1, justify="right", text="Power Supply*")
        self.supply_combo = ttk.Combobox(frame.tab1, textvariable=self.supply, 
                                        state='readonly', width=WD)
        self.supply_combo['state'] = 'disabled'        
        self.supply_combo.bind('<<ComboboxSelected>>', self.get_supply)
        supply_label.grid(row=3, column=3, sticky=E, ipady=IY, padx=PX, pady=PY)
        self.supply_combo.grid(row=3, column=4, sticky=W, ipady=IY, padx=PX, pady=PY)

        max_current_label = ttk.Label(frame.tab1, justify="right", 
                                        text="Max. Current\nPer String (Amp)")
        max_current_combo = ttk.Combobox(frame.tab1, values=self.max_current_list, 
                                        textvariable=self.max_current,
                                        state='readonly', width=WD)
        max_current_label.grid(row=4, column=1, sticky=E, ipady=2, padx=5, pady=5)
        max_current_combo.grid(row=4, column=2, columnspan=5, sticky=W, ipady=IY, padx=PX, pady=PY)

        port2_label = ttk.Label(frame.tab1, justify="right", text="Comms\nOption")
        port2_combo = ttk.Combobox(frame.tab1, values=self.port_list, 
                                        textvariable=self.port2, 
                                        state='readonly', width=WD)
        port2_combo.bind('<<ComboboxSelected>>', self.get_port2)
        port2_label.grid(row=4, column=3, sticky=E, ipady=IY, padx=PX, pady=PY)
        port2_combo.grid(row=4, column=4, sticky=W, ipady=IY, padx=PX, pady=PY)

        block_temp_label = ttk.Label(frame.tab1, justify="right", 
                                        text="Include Block Temperature Measurement")
        self.block_temp = ttk.Checkbutton(frame.tab1, command=self.get_block_temp)
        self.block_temp.invoke()
        block_temp_label.grid(row=5, column=1, columnspan=3, sticky=E, ipady=IY, padx=PX, pady=PY)
        self.block_temp.grid(row=5, column=4, sticky=W, ipady=IY, padx=PX, pady=PY)
    
    def reset(self):
        super().system_defaults()

    def get_systems(self, *args):
        return self.systems.get()

    def get_strings(self, *args):
        return self.strings.get()

    def int_strings(self, *args):
        for arg in args:
            return int(arg[:1])

    def get_blocks(self, *args):
        return self.blocks.get()
    
    def get_block_temp(self, *args):
        """returns True if block temp selected"""
        return self.block_temp.instate(['selected'])

    def get_model(self, *args):
        if self.model.get() == "LX":
            self.strings_combo['values'] = self.lx_string_list
            self.supply_combo['values'] = self.lx_supply_list
        elif self.model.get() == "MX":
            self.strings_combo['values'] = self.mx_string_list
            self.supply_combo['values'] = self.mx_supply_list
        self.strings_combo['state'] = 'enabled'
        self.strings_combo['state'] = 'readonly'
        self.supply_combo['state'] = 'enabled'
        self.supply_combo['state'] = 'readonly'
        return self.model.get()

    def get_block_voltage(self, *args):
        return self.block_voltage.get()

    def get_supply(self, *args):
        return self.supply.get()

    def get_max_current(self, *args):
        return self.max_current.get()

    def get_port2(self, *args):
        return self.port2.get()

     
    def completed(self, *args):
        if self.get_systems() > 0 and \
           self.int_strings(get_strings()) > 0 and \
           self.get_blocks() > 0  and \
           self.get_max_current() in self.max_current_list and \
           self.get_model() in self.model_list and \
           self.get_block_voltage() in self.block_voltage_list and \
           self.get_port2() in self.port_list and \
           self.get_supply() in self.lx_supply_list or self.get_supply in self.mx_supply_list:
            return True
        else:
            return False

    def error_check(self, *args):
        # try:
            #     error.not_positive(t1.get_systems(), t1.get_blocks())
            #     error.excess_blocks(t1.get_model(), t1.get_systems(), 
            #                         t1.int_strings(t1.get_strings()), t1.get_blocks())
            # except error.NotPositive:
            #     self.message1.set(error.NotPositive.message)
            # except error.ExcessBlocks:
            #     self.message1.set("Too many blocks, max. 512 for LX or 200 for MX")
            # except (TypeError, TclError):
            #     self.message1.set("Error, ensure all fields are filled in")
            # else:                
            #     
            #     self.message1.set(t1)
            pass

    def __str__(self):
        if self.get_port2() == self.port_list[1]:
            return  "System Details\n"\
                    "================================\n"\
                    "{0}x {1}\n"\
                    "{2} of {3}x {4} blocks\n"\
                    "Power Supply: {5}\n"\
                    "Max String Current {6}\n"\
                    "Measure Block Temperature: {7}\n"\
                    "Inc. Modbus RTU/RS485".format(self.get_systems(),
                    self.get_model(), self.get_strings(), self.get_blocks(), self.get_block_voltage(), 
                    self.get_supply(), self.get_max_current(), self.get_block_temp())
        else:
            return  "System Details\n"\
                    "================================\n"\
                    "{0}x {1}\n"\
                    "{2} of {3}x {4} blocks\n"\
                    "Power Supply: {5}\n"\
                    "Max String Current {6}\n"\
                    "Measure Block Temperature: {7}\n".format(self.get_systems(),
                    self.get_model(), self.get_strings(), self.get_blocks(), self.get_block_voltage(), 
                    self.get_supply(), self.get_max_current(), self.get_block_temp())    

class Tab2(Fields):
    """Battery details tab"""
    def __init__(self):
        super().battery_fields()
        self.reset()
        
        # defaults for ipady, padx, pady, width
        IY = 2
        PX = 5
        PY = 5
        WD = 6

        block_length_label = ttk.Label(frame.tab2, text = "Length (mm)")
        block_width_label = ttk.Label(frame.tab2, text = "Width (mm)")
        block_height_label = ttk.Label(frame.tab2, text = "Height (mm)")
        
        block_dimensions_label = ttk.Label(frame.tab2, justify="right", text="Block\nDimensions")
        x1_label = ttk.Label(frame.tab2, justify = "center", text = "x")
        x2_label = ttk.Label(frame.tab2, justify = "center", text = "x")
        block_length_entry = ttk.Entry(frame.tab2, textvariable=self.block_length, width=WD)
        #block_length_entry.bind("<FocusIn>", self.entries_focusin)
        #block_length_entry.bind("<FocusOut>", self.entries_focusout)
        block_width_entry = ttk.Entry(frame.tab2, textvariable=self.block_width, width=WD)
        #block_width_entry.bind("<FocusIn>", self.entries_focusin)
        #block_width_entry.bind("<FocusOut>", self.entries_focusout)
        block_height_entry = ttk.Entry(frame.tab2, textvariable=self.block_height, width=WD)
        #block_height_entry.bind("<FocusIn>", self.entries_focusin)
        #block_height_entry.bind("<FocusOut>", self.entries_focusout)
        block_dimensions_label.grid(row=2, column=1, sticky=E, ipady=IY, padx=PX, pady=0)
        x1_label.grid(row=2, column=3, sticky=(E,W))
        x2_label.grid(row=2, column=5, sticky=(E,W))
        set_button = ttk.Button(frame.tab2, text="Set", command=self.set_button1)
        
        block_length_label.grid(row=1, column=2, sticky=S)
        block_length_entry.grid(row=2, column=2, sticky=(E,W), ipady=IY, padx=PX, pady=PY)
        block_width_label.grid(row=1, column=4, sticky=S)
        block_width_entry.grid(row=2, column=4, sticky=(E,W), ipady=IY, padx=PX, pady=PY)
        block_height_label.grid(row=1, column=6, sticky=S)
        block_height_entry.grid(row=2, column=6, sticky=(E,W), ipady=IY, padx=PX, pady=PY)
        set_button.grid(row=2, column=7, sticky=W, ipady=1, padx=PX, pady=PY)

        term_position_label = ttk.Label(frame.tab2, justify="right",text="Terminal\nPosition")
        term_position_combo = ttk.Combobox(frame.tab2, values=self.term_pos_list,
                                        textvariable=self.term_pos, 
                                        state='readonly', width = WD)
        term_position_label.grid(row=3, column=1, sticky=E, ipady=IY, padx=PX, pady=PY)
        term_position_combo.grid(row=3, column=2, columnspan=5, sticky=W, ipady=IY, padx=PX, pady=PY)


        term_number_label = ttk.Label(frame.tab2, justify="right",text="No. of\nTerminals")
        term_number_combo = ttk.Combobox(frame.tab2, values=self.term_number_list, 
                                        textvariable=self.term_number,
                                        state='readonly',width=WD)
        term_number_label.grid(row=3, column=4, sticky=E, ipady=IY, padx=PX, pady=PY)
        term_number_combo.grid(row=3, column=6, sticky=W, ipady=IY, padx=PX, pady=PY)
        term_align_label = ttk.Label(frame.tab2, justify="right",text="Terminal\nAlignment")
        term_align_combo = ttk.Combobox(frame.tab2, values=self.term_align_list,
                                        textvariable=self.term_align, 
                                        state='readonly', width = WD)
        term_align_label.grid(row=4, column=1, sticky=E, ipady=IY, padx=PX, pady=PY)
        term_align_combo.grid(row=4, column=2, columnspan=5, sticky=W, ipady=IY, padx=PX, pady=PY)

        term_size_label = ttk.Label(frame.tab2, justify="right", text="Terminal\nScrew Size")
        self.term_size_combo = ttk.Combobox(frame.tab2, values=self.term_size_list, 
                                        textvariable=self.term_size,
                                        state='readonly', width = WD)
        self.term_size_combo['state'] = 'disabled'
        self.term_size_combo.bind('<<ComboboxSelected>>', self.draw_terminals)
        term_size_label.grid(row=5, column=1, sticky=E, ipady=IY, padx=PX, pady=PY)
        self.term_size_combo.grid(row=5, column=2, columnspan=5, sticky=W, ipady=IY, padx=PX, pady=PY)

        self.batt_canvas = Canvas(frame.right, height=150, width=150, bg="white")
        self.batt_canvas.grid(row=2, column=1)
        # self.batt_canvas.grid(row=3, rowspan=4, column=7)

    def reset(self):
        super().battery_defaults()

    def set_button1(self, *args):   
        self.term_size_combo['state'] = 'enabled'
        try:
            self.batt_canvas.destroy()
            self.batt_canvas = Canvas(frame.right, height=150, width=150)
            self.batt_canvas.grid(row=2, column=1)
        except:
            pass
        if self.block_length.get() > 0 and self.block_width.get() > 0 and self.block_height.get() > 0:
            self.draw_battery(self.get_block_length(), self.get_block_width(), self.get_block_height())

    def draw_battery(self, length, width, height):
    
        padding = 15
        self.x_offset = 2
        self.y_offset = float(self.batt_canvas['height']) - 12.5

        overall_H = 1.5 * height
        overall_W = math.sqrt(length**2 + height**2) \
                    * (math.cos(math.radians(45)) / 2) + width # diagonal line (pythagoras + cos(45)/2)) + width 
        overall_size = (overall_H, overall_W)
        self.scale = (float(self.batt_canvas['height']) - padding) / max(overall_size)
        self.batt_L = length * self.scale
        self.batt_W = width * self.scale
        self.batt_H = height * self.scale
        self.diagonal_L = math.sqrt(self.batt_L**2 + self.batt_H**2) \
                    * (math.cos(math.radians(45)) / 2) # diagonal line = pythogoras + cos(45)/2
        diagonal_angle = math.degrees(math.acos(self.diagonal_L \
                        / math.sqrt((.5 * self.batt_H)**2 + self.diagonal_L**2))) # angle in degrees of diagonal line

        front_top_left=     (self.x_offset,                                self.y_offset - self.batt_H)
        front_top_right =   (self.x_offset + self.batt_W,                  self.y_offset - self.batt_H)
        front_bot_left =    (self.x_offset,                                self.y_offset)
        front_bot_right =   (self.x_offset + self.batt_W,                  self.y_offset)
        upper_top_left =    (self.x_offset + self.diagonal_L,              self.y_offset - 1.5 * self.batt_H)
        upper_top_right =   (self.x_offset + self.diagonal_L + self.batt_W,self.y_offset - 1.5 * self.batt_H)
        upper_bot_left =    front_top_left
        upper_bot_right =   front_top_right
        side_top_left =     front_top_right
        side_top_right =    upper_top_right
        side_bot_left =     front_bot_right
        side_bot_right =    (self.x_offset + self.diagonal_L + self.batt_W,self.y_offset - .5 * self.batt_H)
       
        self.batt_front = self.batt_canvas.create_polygon([front_top_left, front_bot_left, 
                                                    front_bot_right, front_top_right], 
                                                    outline="#636363", fill="#EAECEE",
                                                    joinstyle="bevel")
        self.batt_upper = self.batt_canvas.create_polygon([upper_bot_left, upper_top_left, 
                                                    upper_top_right, upper_bot_right], 
                                                    outline="#636363", fill="#EAECEE",
                                                    joinstyle="bevel") 
        self.batt_side  = self.batt_canvas.create_polygon([side_bot_left, side_bot_right, 
                                                    side_top_right, side_top_left], 
                                                    outline="#636363", fill="#D5D5D5",
                                                    joinstyle="bevel")
        self.length_text = self.batt_canvas.create_text(self.x_offset + self.batt_W + (2/3) * self.diagonal_L, 
                                                    self.y_offset-(self.batt_H/5), 
                                                    text=("L:"+str(length)+"mm"), 
                                                    angle=diagonal_angle,
                                                    justify='center', font=('Arial', '8'))
        self.width_text = self.batt_canvas.create_text(self.x_offset + self.batt_W/2, 
                                                    float(self.batt_canvas['height']) - 5, 
                                                    text=("W:"+str(width)+"mm"), 
                                                    justify='center', font=('Arial', '8'))
        self.height_text = self.batt_canvas.create_text(self.x_offset + self.diagonal_L + self.batt_W + 7.5, 
                                                    self.y_offset - self.batt_H, 
                                                    text=("H:"+str(height)+"mm"), angle=90, 
                                                    justify='center', font=('Arial', '8'))
        term_screw = self.get_term_size()
        term_screw = term_screw[:2]
        self.draw_terminals(self.get_term_size())

    def draw_terminals(self, arg):
        if self.get_term_pos() == "Front":
            term1_x0 = self.x_offset + (self.batt_W/2) - (self.batt_W/3)
            term1_y0 = self.y_offset - .8 * self.batt_H
            term1_x1 = term1_x0 + 8 * self.scale
            term1_y1 = term1_y0 + 8 * self.scale
            self.batt_term1 = self.batt_canvas.create_oval(term1_x0, term1_y0, term1_x1, term1_y1)
            
            term2_x0 = self.x_offset + (self.batt_W/2) + (self.batt_W/3)
            term2_y0 = self.y_offset - .8 * self.batt_H
            term2_x1 = term2_x0 - 8 * self.scale
            term2_y1 = term2_y0 + 8 * self.scale
            self.batt_term2 = self.batt_canvas.create_oval(term2_x0, term2_y0, term2_x1, term2_y1)
            

        # term2_x0 = self.x_offset + (self.batt_W/2) + (self.batt_W/3)
        # term2_y0 = self.y_offset - .8 * self.batt_H
        # term2_x1 = term2_x0 - 8 * self.scale
        # term2_y1 = term2_y0 + 8 * self.scale
        # self.batt_term2 = self.batt_canvas.create_oval(term2_x0, term2_y0, term2_x1, term2_y1)

        # term2_x0 = self.x_offset + (self.batt_W/2) + (self.batt_W/3)
        # term2_y0 = self.y_offset - .8 * self.batt_H
        # term2_x1 = term2_x0 - 8 * self.scale
        # term2_y1 = term2_y0 + 8 * self.scale
        # self.batt_term2 = self.batt_canvas.create_oval(term2_x0, term2_y0, term2_x1, term2_y1)
        
    def get_block_length(self, *args):
        return self.block_length.get()

    def get_block_width(self, *args):
        return self.block_width.get()

    def get_block_height(self, *args):
        return self.block_height.get()

    def get_term_size(self, *args):
        return self.term_size.get()

    def get_term_align(self, *args):
        return self.term_align.get()

    def get_term_pos(self, *args):
        return self.term_pos.get()

    def completed(self, *args):
        if True:
            return True
        else:
            return False
       
class Tab3(Fields):
    """Rack X&Y Axis tab"""
    def __init__(self):
        super().rack_xy_fields()
        self.reset()
        self.num_rows = IntVar(value="1")
        
        # defaults for ipady, padx, pady, width
        self.IY = 2
        self.PX = 5
        self.PY = 2
        self.WD = 8 

        num_rows_label = ttk.Label(frame.tab3, justify="right",
                                    text="Number of Rows\nPer String")
        self.num_rows_combo = ttk.Combobox(frame.tab3, values=self.num_rows_list, 
                                    textvariable=self.num_rows, state='readonly', width=8)
        self.num_rows_combo.bind('<<ComboboxSelected>>', self.populate_rows)
        num_rows_label.grid(row=1,column=1, sticky=E)
        self.num_rows_combo.grid(row=1,column=2, sticky=W, ipady=self.IY, padx=self.PX, pady=self.PY)

        row_width_label = ttk.Label(frame.tab3, justify="right",
                                    text="Row Width (mm)")
        row_width_entry = ttk.Entry(frame.tab3, textvariable=self.row_width, width=8)
        row_width_label.grid(row=2,column=1, sticky=E, ipady=self.IY, padx=self.PX, pady=self.PY)
        row_width_entry.grid(row=2,column=2, sticky=W, ipady=self.IY, padx=self.PX, pady=self.PY)

        row_height_label = ttk.Label(frame.tab3, justify="right", 
                                    text="Distance Between Rows\n(Height in mm)")
        row_height_entry = ttk.Entry(frame.tab3, textvariable=self.row_height, width=8)
        row_height_label.grid(row=3,column=1, sticky=E, ipady=self.IY, padx=self.PX, pady=self.PY)
        row_height_entry.grid(row=3,column=2, sticky=W, ipady=self.IY, padx=self.PX, pady=self.PY)

        block_distance_label = ttk.Label(frame.tab3, justify="right", 
                                    text = "Gap Between Blocks (mm)")
        block_distance_entry = ttk.Entry(frame.tab3, textvariable=self.block_distance, width=8)
        block_distance_label.grid(row=4, column=1, sticky=E, ipady=self.IY, padx=self.PX, pady=self.PY)
        block_distance_entry.grid(row=4, column=2, sticky=W, ipady=self.IY, padx=self.PX, pady=self.PY)

        self.row1_label = ttk.Label(frame.tab3, text="No. of Blocks in Row 1 ")
        self.row1_entry = ttk.Entry(frame.tab3, textvariable=self.row_var1, width=self.WD)
        self.row1_label.grid(row=1, column=3, ipady=self.IY, padx=self.PX, pady=self.PY)
        self.row1_entry.grid(row=1, column=4, ipady=self.IY, padx=self.PX, pady=self.PY)

    def reset(self):
        super().rack_xy_defaults()

    def row1(self):
        self.row1_label['state'] = 'normal'
        self.row1_entry['state'] = 'normal'
    
    def row2(self):
        self.row2_label = ttk.Label(frame.tab3, text="No. of Blocks in Row 2 ")
        self.row2_entry = ttk.Entry(frame.tab3, textvariable=self.row_var2, width=self.WD)
        self.row2_label.grid(row=2, column=3, ipady=self.IY, padx=self.PX, pady=self.PY)
        self.row2_entry.grid(row=2, column=4, ipady=self.IY, padx=self.PX, pady=self.PY)
    
    def row3(self):    
        self.row3_label = ttk.Label(frame.tab3, text="No. of Blocks in Row 3 ")
        self.row3_entry = ttk.Entry(frame.tab3, textvariable=self.row_var3, width=self.WD)
        self.row3_label.grid(row=3, column=3, ipady=self.IY, padx=self.PX, pady=self.PY)
        self.row3_entry.grid(row=3, column=4, ipady=self.IY, padx=self.PX, pady=self.PY)
    
    def row4(self):    
        self.row4_label = ttk.Label(frame.tab3, text="No. of Blocks in Row 4 ")
        self.row4_entry = ttk.Entry(frame.tab3, textvariable=self.row_var4, width=self.WD)
        self.row4_label.grid(row=4, column=3, ipady=self.IY, padx=self.PX, pady=self.PY)
        self.row4_entry.grid(row=4, column=4, ipady=self.IY, padx=self.PX, pady=self.PY)
    
    def row5(self):    
        self.row5_label = ttk.Label(frame.tab3, text="No. of Blocks in Row 5 ")
        self.row5_entry = ttk.Entry(frame.tab3, textvariable=self.row_var5, width=self.WD)
        self.row5_label.grid(row=5, column=3, ipady=self.IY, padx=self.PX, pady=self.PY)
        self.row5_entry.grid(row=5, column=4, ipady=self.IY, padx=self.PX, pady=self.PY)
    
    def row6(self):    
        self.row6_label = ttk.Label(frame.tab3, text="No. of Blocks in Row 6 ")
        self.row6_entry = ttk.Entry(frame.tab3, textvariable=self.row_var6, width=self.WD)
        self.row6_label.grid(row=6, column=3, ipady=self.IY, padx=self.PX, pady=self.PY)
        self.row6_entry.grid(row=6, column=4, ipady=self.IY, padx=self.PX, pady=self.PY)
    
    def row7(self):    
        self.row7_label = ttk.Label(frame.tab3, text="No. of Blocks in Row 7 ")
        self.row7_entry = ttk.Entry(frame.tab3, textvariable=self.row_var7, width=self.WD)
        self.row7_label.grid(row=7, column=3, ipady=self.IY, padx=self.PX, pady=self.PY)
        self.row7_entry.grid(row=7, column=4, ipady=self.IY, padx=self.PX, pady=self.PY)
    
    def row8(self):    
        self.row8_label = ttk.Label(frame.tab3, text="No. of Blocks in Row 8 ")
        self.row8_entry = ttk.Entry(frame.tab3, textvariable=self.row_var8, width=self.WD)
        self.row8_label.grid(row=8, column=3, ipady=self.IY, padx=self.PX, pady=self.PY)
        self.row8_entry.grid(row=8, column=4, ipady=self.IY, padx=self.PX, pady=self.PY)
    
    def populate_rows(self, *args):
        self.destroy_rows()
        if int(self) == 1:
            self.row1()
        elif int(self) == 2:
            self.row1(), self.row2()
        elif int(self) == 3:
            self.row1(), self.row2(), self.row3()
        elif int(self) == 4:
            self.row1(), self.row2(), self.row3(), self.row4()
        elif int(self) == 5:
            self.row1(), self.row2(), self.row3(), self.row4(), 
            self.row5()
        elif int(self) == 6:
            self.row1(), self.row2(), self.row3(), self.row4(), 
            self.row5(), self.row6()
        elif int(self) == 7:
            self.row1(), self.row2(), self.row3(), self.row4(), 
            self.row5(), self.row6(), self.row7()
        elif int(self) == 8:
            self.row1(), self.row2(), self.row3(), self.row4(),
            self.row5(), self.row6(), self.row7(), self.row8() 

    def destroy_rows(self):
        try:
            self.row2_label.destroy(), self.row2_entry.destroy()
            self.row3_label.destroy(), self.row3_entry.destroy()
            self.row4_label.destroy(), self.row4_entry.destroy()
            self.row5_label.destroy(), self.row5_entry.destroy()
            self.row6_label.destroy(), self.row6_entry.destroy()
            self.row7_label.destroy(), self.row7_entry.destroy()
            self.row8_label.destroy(), self.row8_entry.destroy()
        except:
            pass

    def __int__(self):
        return int(self.num_rows.get())

root = Tk()
frame = Frame(root)
t1 = Tab1()
t2 = Tab2()
t3 = Tab3()
root.mainloop()