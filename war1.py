reading = open("/home/hduser/custs")
readilines = reading.readlines();
j = 0
splitting = []
for i in range(0, readilines.__len__()):
    fool = readilines[i].split(",")
    splitting.append((fool[3], fool[4][0:fool[4].__len__() - 1]))
for o in range(0, splitting.__len__()):
    print(splitting[o])
