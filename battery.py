import system_form_wizard as sfw

class Tab2(sfw.Fields):
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
       