
filename = 'football-league-results.txt'

def fbleagueResult():
    with open(filename) as fbresult:
        fbresult.next()
        for team in fbresult:
            team = team.split()
            clubNames = []
            clubData = []

            for data in team:
                try:
                    data = int(data)
                    clubData.append(data)

                except ValueError:
                    stringData = str(data)
                    if stringData != "-":
                        clubNames.append(stringData)
                    pass

            print clubNames
            print clubData
fbleagueResult()
