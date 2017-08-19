filereport  = 'port-harcourt-weather.txt'     #Initialised filereport
def phweatherList(filereport):
    with open(filereport) as PHWeather:   # & opening it
        dailyList = []                #Initialised list for days
        dailyHighList = []          #Initialised list for high temperature
        dailyLowList = []           #Initialised list for low temperature
        dailyTempSpread = []        #Initialised list for daily temperature spread
        next(PHWeather)             #move to the next line
        next(PHWeather)             #move to the next line
        for line in PHWeather:     #Iterating over each line
            line.strip()
            # dayDailyTempSpread = []
            splitline = line.split()  #creating list for each line
            try:        #Extracting my relevant data from cols: 1,2 & 3
                dayNum = int(splitline[0]) #avoid the last row starting with string "mo", even if the month is 31
                dailyHigh = int(splitline[1])
                dailyLow = int(splitline[2])
            except ValueError:
                pass
            dailyList.append(dayNum), dailyHighList.append(dailyHigh), dailyLowList.append(dailyLow), dailyTempSpread.append(dailyHigh - dailyLow)

    weatherDict = dict(zip(dailyList,dailyTempSpread))

    print "The day with the smallest temperature spread is day: " + str(min(weatherDict, key=weatherDict.get)) + ", with temperature spread of " + str(min(sorted(weatherDict.values())))

phweatherList(filereport)
