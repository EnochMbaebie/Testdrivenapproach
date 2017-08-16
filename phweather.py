filename = 'port-harcourt-weather.txt'

with open(filename) as file:
    next(file)
    next(file)
    daylist = []
    dailyTempSpread = []
    for line in file:
        splitted_line = line.split()
        # if isinstance(splitted_line[0],int):
        # daylist.append(splitted_line[0])
        #print splitted_line[0],splitted_line[1],splitted_line[2]
        try:
            dailylistNum = int(splitted_line[0])
            dailyHigh = int(splitted_line[1])
            dailylow = int(splitted_line[2])
            # print int(splitted_line[0])
        except ValueError:
            pass
        dailyTempSpread.append(dailyHigh - dailylow)
        daylist.append(dailylistNum)
    # print len(daylist)
    # print len(dailyTempSpread)
weatherDict = dict(zip(daylist,dailyTempSpread))
print weatherDict
