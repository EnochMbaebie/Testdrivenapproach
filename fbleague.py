class FootballLeaguePerformance(object):

    filename = 'football-league-results.txt'

    def fbleagueResult(filename):
        with open(filename) as fbresult:
            clubNamesList =[]
            goalDiff = []
            # smallestClubWithGoalDiff = []
            # smallestGoalDiff = []
            fbresult.next()
            newResult = []
            # tempGoalFor = []
            # tempGoalAgainst = []
            for team in fbresult:
                team = team.split()
                clubNames = []
                clubData = []

                for data in team:

                    try:
                        data = int(data)
                        clubData.append(data)
                        pass
                    except ValueError:
                        stringData = str(data)
                        if stringData != "-":
                            clubNames.append(stringData)
                        pass
                if len (clubData) > 0:
                    goalFor = int(clubData[4])
                    goalAgainst = int(clubData[5])
                    del clubNames[:1]
                    clubNames = ''.join(clubNames)
                    clubNamesList.append(clubNames)

                    goalDiff.append(goalFor - goalAgainst)
                    # goalDiff.append(diffGoal)

                #print teamGoalAgainst
                #print clubData
                #print clubNames, clubGoalDiff
            clubGoalPerformance = dict(zip(clubNamesList, goalDiff))
                #print clubGoalPerformance
            teamWithLowestGoalDiff = min(sorted(clubGoalPerformance.keys()))
            lowestGoalDiff = min(sorted(clubGoalPerformance.values()))

            teamWithLowestGoalDiff = str(teamWithLowestGoalDiff)
            lowestGoalDiff = str(lowestGoalDiff)

                # smallestClubWithGoalDiff.append(lowestclubGoalDiff)

            print "The Club with the lowest goal difference is " + teamWithLowestGoalDiff + ", with: " + lowestGoalDiff + " goal difference"

                #print goalFor, goalAgainst
                #print teamGoalPerformance

    fbleagueResult(filename)
