import system_form_wizard as sfw

class Tab3(sfw.Fields):
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