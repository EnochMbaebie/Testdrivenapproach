
filename = 'football-league-results.txt'

def fbleagueResult():
    with open(filename) as fbresult:
        fbresult.next()        
        for team in fbresult:
            team = team.split()
            try:
                team.remove('-')
                team = team[1:]
            except Exception as e:
                pass
            print team

fbleagueResult()
