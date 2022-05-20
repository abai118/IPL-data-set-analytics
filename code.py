import csv
import matplotlib.pyplot as plt


def rawdata(filename): #collecting the .csv files and converting into data
    file=open(filename)
    deliveries = csv.reader(file)
    data = []
    for row in deliveries:
            data.append(row)
            
    return data

    

def totalRunsByEachTeam():#collecting the data from "deliveries.csv" and dividing the total runs of each team
    matchdata=rawdata("deliveries.csv")  # importing the file of deliveries.csv and converting them into data
    details=matchdata.pop(0)
    teams=[]
    for team in matchdata :
        teams.append(team[2])
    teams=list(set(teams))
    #print(teams)
    teamscores=[0]*len(teams)

    data=dict(zip(teams,teamscores))

    #print(data)
    #print(details[17])

    for team in matchdata :
        data[team[2]]=data[team[2]]+int(team[17])
    
    plt.bar(data.keys(),data.values())
    plt.show()
    
def topBatsmanOfRCB() : #collecting data from "deliveries.csv" and finding the player scored topruns for RCB in entire game
    matchdata=rawdata("deliveries.csv")  #importing the file of deliveries.csv and converting them into data
    RCBdata=[]
    
    for team in matchdata :
        
       if team[2]=="Royal Challengers Bangalore" :
           
           RCBdata.append(team)
    players=[]   
    for player in RCBdata :
        
        players.append(player[6])
        
    players=list(set(players))
    
    runs=[0]*len(players)
    
    
    playerdata=dict(zip(players,runs))
    
    
    for runs in RCBdata :
        playerdata[runs[6]]=playerdata[runs[6]]+int(runs[17])
        
    
    
    topBatsman=list(max(zip(playerdata.values(),playerdata.keys())))
    print(topBatsman[1]+" = "+str(topBatsman[0]))

def umpireAnalysisChart() : # collecting the data from "umpires.csv" and finding the barchart of umpires on basis of country and no of umpires per country
    umpiresdata=rawdata("umpires.csv")  #importing the file of umpires.csv and converting them into data
    countries=[]
    
    for data in umpiresdata:
        
        countries.append(data[1].strip())
        
    uniqueCountries=list(set(countries))
    uniqueCountries.remove("India")
    uniqueCountries.remove("Nationality")
    #print(uniqueCountries)
    
    nums=[0]*len(uniqueCountries)

    countriesdata=dict(zip(uniqueCountries,nums))
    
    
    for data in uniqueCountries :
        
        countriesdata[data]=countries.count(data)
        
   
    print(countriesdata)
    
    plt.bar(countriesdata.keys(), countriesdata.values())
    plt.show()
    
def StackedchartOfMatchesPlayedByTeamAndBySeason(): # collecting data from "matches.csv" file and finding StackedchartOfMatchesPlayedByTeamAndBySeason
    matchsdata=rawdata("matches.csv")
    years=[]
    teams=[]
    for season in matchsdata :
        years.append(season[1])
        teams.append(season[4])
    years=sorted(list(set(years)))
    teams=sorted(list(set(teams)))
  
    values=[0]*len(years)
    
    nums=[0]*len(teams)
    
    dataYears=dict(zip(years,values))
    dataTeams=dict(zip(teams,nums))
    
    
    print(dataTeams)

    for matches in matchsdata:
        dataYears[matches[1]]=dataYears[matches[1]]+1
        dataTeams[matches[4]]=dataTeams[matches[4]]+1
        
    dataYears.pop("season")
    dataTeams.pop("team1")
    
        
    
    
   
    plt.bar(dataYears.keys(),dataYears.values())
    plt.show()
    plt.bar(dataTeams.keys(),dataTeams.values())
    plt.show()




def main():
    
    
    totalRunsByEachTeam()
    topBatsmanOfRCB()
    umpireAnalysisChart()
    StackedchartOfMatchesPlayedByTeamAndBySeason()



main()