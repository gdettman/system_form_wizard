import system_form_wizard as sfw

class Tab1(sfw.Fields):
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
