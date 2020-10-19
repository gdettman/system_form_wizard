
print("Let's get some information about the quantity of systems, strings and blocks")

qtySystems = int(input("How many systems? "))
qtyStrings = int(input("How many strings per system? "))
qtyBlocks = int(input("How many blocks per string? "))
blockVoltage = int(input("What is the block voltage? "))
controllerVoltage = int(input("What is the Controller supply voltage? "))

print("Qty. Systems: {0}".format(qtySystems))
print("Qty. Strings: {0}".format(qtyStrings))
print("Qty. Blocks: {0}".format(qtyBlocks))
print("Block Voltage: {0}".format(blockVoltage))
print("Controller Voltage: {0}".format(controllerVoltage))

#block info
print("Let's get some information on the battery block")
lengthBlock = float(input("Enter block length (in mm): "))
widthBlock = 400 #float(input("Enter block width (in mm): "))
heightBlock = float(input("Enter block height (in mm): "))
#terminal arrangement needed ie. Front facing, forward facing, etc. to estimate lead length
print("Let's get some information on the battery rack")
qtyRows = int(input("Enter number of physical rows (per string): "))

blocksPerRow = []
for rowNumber in range(1, qtyRows + 1):
    blocksPerRow.append(int(input("How many blocks in row number {0}? ".format(rowNumber))))
#qtyLayers = int(input("How many layers of blocks per row? "))
#if qtyLayers > 0 and qtyLayers != 1:
#    typeLayer = input("How are the additional layers wired up, North-South or East-West? " )
#    betweenLayers = float(input("What is the distance between layers (in mm)? "))
betweenBlocks = float(input("Enter the distance between blocks (in mm): "))

estWidthPerRow = []
for mb in blocksPerRow:
    estWidthPerRow.append(mb * (widthBlock + betweenBlocks) - betweenBlocks)

widthRow = float(input("Enter the width of each row to determine mounting rail size (or press 0 to estimate Widths based on blocks per row: "))
if widthRow == 0:
    print("Estimated mounting rail per row (in mm) is: {0}".format(estWidthPerRow))

#create lists containing number of sensors per row
dualPerRow = []
singlePerRow = []
for blocks in blocksPerRow:
    if blocks % 2 == 0:
        dualPerRow.append(int(blocks / 2))
        singlePerRow.append(int(0))
    else:
        dualPerRow.append(int(blocks / 2))
        singlePerRow.append(int(1))

print("Blocks per row = {0}".format(blocksPerRow))
print("Dual sensors per row = {0}".format(dualPerRow))
print("Single sensors per row = {0}".format(singlePerRow))
print("Dual sensors in Total = {0}".format(sum(dualPerRow)))
print("Single sensors in Total = {0}".format(sum(singlePerRow)))