# d = {'a':1, 'b':2}
# for key,val in d.items():
#     exec(key + '=val')
#class CreateRows:
import main_method

rows = main_method.rows
row_label_dict = {}
row_entry_dict = {} 
row_label_grid_dict = {}
row_entry_grid_dict = {}

if rows > 0:
    for i in range(rows):
        row_label_dict['row{0}'.format(i+1)] = "ttk.Label(frame.tab3, text='No. Blocks in Row {0}')".format(i+1)
        row_entry_dict['entry{0}'.format(i+1)] = "ttk.Entry(frame.tab3, textvariable=self.row_var{0})".format(i+1)
        row_label_grid_dict['row{0}.grid'.format(i+1)] = "row={0}, column={1}".format(i+2, 3)
        row_entry_grid_dict['entry{0}.grid'.format(i+1)] = "row={0}, column={1}".format(i+2, 4)
    print(row_label_dict)
    print(row_entry_dict)
    print(row_label_grid_dict)
    print(row_entry_grid_dict)
    for key, val in row_label_dict.items():
        exec (key + '=abc')

# for key, val in row_label_dict:
#     exec(key + '=val')

    #def populate_rows(self, *args):     
#        for i in range(t3.num_rows.get()):
            # self.row_label_dict[i+1] = "ttk.Label(frame.tab3, text='No. Blocks in Row {0}')".format(i+1)
            # self.row_entry_dict[i+1] = "ttk.Entry(frame.tab3, textvariable=self.row_var{0})".format(i+1)
            # self.row_label_grid_dict[i+1] = "row={0}, column={1}".format(i+2, 3)
            # self.row_entry_grid_dict[i+1] = "row={0}, column={1}".format(i+2, 4)
            #print(self.create_rows(2))
        # print(self.row_label_dict)
        # print(self.row_entry_dict)
        # print(self.row_label_grid_dict)
        # print(self.row_entry_grid_dict)
        # #for k,v in self.row_label_dict.items()
            #self.row_label_dict[i]
            # self.row_entry_dict[i]
            # self.row_label_grid_dict[i]
            # self.row_entry_grid_dict[i]