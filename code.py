import csv
from importlib.resources import path
from optparse import Values
import matplotlib.pyplot as plt


def rawdata(filename):  # collecting the .csv files and converting into data
    with open(filename,"r") as file :
        csvReader=csv.DictReader(file)
        data=list(csvReader)
        
    return data
              
    

def totalRunsByEachTeam(deliveriesCsv):#collecting the data from "deliveries.csv" and dividing the total runs of each team
    matchdata=rawdata(deliveriesCsv)  # importing the file of deliveries.csv and converting them into data
    #details=matchdata.pop(0)
    teams=[]
    for team in matchdata :
        teams.append(team["batting_team"])
    teams=list(set(teams))
    #print(teams)
    teamscores=[0]*len(teams)

    teamsDict=dict(zip(teams,teamscores))

    #print(data)
    #print(details[17])

    for team in matchdata :
        teamsDict[team["batting_team"]]=teamsDict[team["batting_team"]]+int(team["total_runs"])
    
    plt.bar(teamsDict.keys(),teamsDict.values())
    plt.show()
    
def topBatsmanOfRCB(deliveriesCsv) : #collecting data from "deliveries.csv" and finding the player scored topruns for RCB in entire game
    matchdata=rawdata(deliveriesCsv)  #importing the file of deliveries.csv and converting them into data
    RCBdata=[]
    
    for team in matchdata :
        
       if team["batting_team"]=="Royal Challengers Bangalore" :
           
           RCBdata.append(team)
    players=[]   
    for player in RCBdata :
        
        players.append(player["batsman"])
        
    players=list(set(players))
    
    runs=[0]*len(players)
    
    
    playerdata=dict(zip(players,runs))
    
    
    for runs in RCBdata :
        playerdata[runs["batsman"]]=playerdata[runs["batsman"]]+int(runs["total_runs"])
        
    
    
 
    plt.bar(playerdata.keys(),playerdata.values())
    plt.show()

def umpireAnalysisChart(umpairesCsv) : # collecting the data from "umpires.csv" and finding the barchart of umpires on basis of country and no of umpires per country
    umpiresdata=rawdata(umpairesCsv)  #importing the file of umpires.csv and converting them into data
    countries=[]
    
    for data in umpiresdata:
        
        countries.append(data["Nationality"].strip())
        
    uniqueCountries=list(set(countries))
    
    uniqueCountries.remove("India")
    #uniqueCountries.remove("Nationality")
    #print(uniqueCountries)
    
    nums=[0]*len(uniqueCountries)

    countriesdata=dict(zip(uniqueCountries,nums))
    
    
    for data in uniqueCountries :
        
        countriesdata[data]=countries.count(data)
        
   
    #print(countriesdata)
    
    plt.bar(countriesdata.keys(), countriesdata.values())
    plt.show()
    
def StackedchartOfMatchesPlayedByTeamAndBySeason(matchesCsv): # collecting data from "matches.csv" file and finding StackedchartOfMatchesPlayedByTeamAndBySeason
    matchsdata=rawdata(matchesCsv)
    years=[]
    teams=[]
    for season in matchsdata :
        years.append(season["season"])
        teams.append(season["team1"])
    years=sorted(list(set(years)))
    teams=sorted(list(set(teams)))
  
    values=[0]*len(years)
    
    nums=[0]*len(teams)
    
    dataYears=dict(zip(years,values))
    dataTeams=dict(zip(teams,nums))
    
    
    #print(dataTeams)

    for matches in matchsdata:
        dataYears[matches["season"]]=dataYears[matches["season"]]+1
        dataTeams[matches["team1"]]=dataTeams[matches["team1"]]+1
        
    # dataYears.pop("season")
    # dataTeams.pop("team1")
    
        
    
    
   
    plt.bar(dataYears.keys(),dataYears.values())
    plt.show()
    plt.bar(dataTeams.keys(),dataTeams.values())
    plt.show()


def NumberOfMatchesPlayedPerYearForAllTheYearsInIPL(matchesCsv):
    matchdata=rawdata(matchesCsv)  # importing the file of matches.csv and converting them into data
    years=[]
    
    for year in matchdata :
        
        years.append(year["season"])
        
    years=sorted(list(set(years)))
    
    #print(years)
    
    matches=[0]*len(years)
    
    data=dict(zip(years,matches))
    
    #print(data)
    
    
    for matches in matchdata :
        
        data[matches["season"]]=data[matches["season"]] +1
        
    print(data)
    #return(list(data.values()))   #using for test case
    
def NumberOfMatchesWonPerTeamPerYearInIPL(matchesCsv) :
    
    matchdata=rawdata(matchesCsv)  # importing the file of maatches.csv and converting them into data
    years=[]
    teams=[]
    
    for data in matchdata :
        
        years.append(data["season"])
        teams.append(data["team1"])
            
    years=sorted(list(set(years)))
    teams=list(set(teams))

    
    
    #print(teams,years)
    values=[0]*len(teams)
    teamsPerYear=dict(zip(teams,values))
    teamValue=[teamsPerYear]*len(years)
    totalTeamsPerYear=dict(zip(years,teamValue))
    
    #print(totalTeamsPerYear)
    
    
    for data in matchdata :
        year=data["season"]
        winner=data["winner"]
        try :
            totalTeamsPerYear[year][winner] += 1
        except:
            pass 
    
    
    print(totalTeamsPerYear)
    #return(list(totalTeamsPerYear.values())[0])    #using for test case
    
    
    
def ExtraRunsConcededPerTeamInTheYear2016(deliveriesCsv,matchesCsv) :
    
    deliveriesdata=rawdata(deliveriesCsv)  # importing the file of deliveries.csv and converting them into data
    
    matchdata=rawdata(matchesCsv) 
    teams=[]
    
    for data in deliveriesdata :    
        teams.append(data["batting_team"])
            
    
    teams=list(set(teams))

    values=[0]*len(teams)

    teamsWithRuns=dict(zip(teams,values))
    
    id=[]
    for ids in matchdata :
        
        if ids["season"]=="2016" :
            id.append(ids["id"])
            
    #print(id)
    
    
    
    for data in deliveriesdata :
        
        if data["match_id"] in id :
            teamsWithRuns[data["batting_team"]]=teamsWithRuns[data["batting_team"]]+int(data["extra_runs"])
            
    print(teamsWithRuns)
    
def Top10EconomicalBowlerInTheYear2015(deliveriesCsv,matchesCsv) :
    deliveriesdata=rawdata(deliveriesCsv)  # importing the file of deliveries.csv and converting them into data
    matchdata=rawdata(matchesCsv) 
   
    
    id=[]
    for ids in matchdata :
        
        if ids["season"]=="2015" :
            id.append(ids["id"])
            
    bowlers=[]
    
    for data in deliveriesdata :    
        
        if data["match_id"] in id :
            bowlers.append(data["bowler"])
            
    
    bowlers=list(set(bowlers))

    values=[0]*len(bowlers)

    bowlersWithRuns=dict(zip(bowlers,values))
    bowlersWithOvers=dict(zip(bowlers,values))
    
    for data in deliveriesdata :
        
        if data["match_id"] in id :
            bowlersWithRuns[data["bowler"]]=bowlersWithRuns[data["bowler"]]+int(data["total_runs"])
            bowlersWithOvers[data["bowler"]]=bowlersWithOvers[data["bowler"]] +1
            
    #print(bowlersWithOvers,bowlersWithRuns)
    #print(len(bowlersWithOvers.keys()),len(bowlersWithRuns.keys()))


    
    totalBowlers = list(bowlersWithRuns.keys())
    
    totalRunsByBowler= list(bowlersWithRuns.values())
    totalOversByBowler=list(bowlersWithOvers.values())
    
    
    bowlerEconomyList=[]
    count=0
    for bowler in totalBowlers :
        
        economy=(totalRunsByBowler[count]/totalOversByBowler[count])*6
        bowlerDetails=[economy,bowler]
        bowlerEconomyList.append(bowlerDetails)
        count=count+1
        
    top10EconomyBowlersList=sorted(bowlerEconomyList)[:10]
    
    top10EconomyBowlers ={}
    
    for bowlers in top10EconomyBowlersList :
        
        top10EconomyBowlers[bowlers[-1]]=bowlers[0]
        
    print(top10EconomyBowlers)
        
    

def main():
    
    matchesPath="/home/akhil118/Desktop/git/IPL-data-set-analytics/matches.csv"
    deliveriesPath="/home/akhil118/Desktop/git/IPL-data-set-analytics/deliveries.csv"
    umpairesPath="/home/akhil118/Desktop/git/IPL-data-set-analytics/umpires.csv"
    
    totalRunsByEachTeam(deliveriesPath)
    topBatsmanOfRCB(deliveriesPath)
    umpireAnalysisChart(umpairesPath)
    StackedchartOfMatchesPlayedByTeamAndBySeason(matchesPath)
    NumberOfMatchesPlayedPerYearForAllTheYearsInIPL(matchesPath)
    NumberOfMatchesWonPerTeamPerYearInIPL(matchesPath)
    ExtraRunsConcededPerTeamInTheYear2016(deliveriesPath,matchesPath)
    Top10EconomicalBowlerInTheYear2015(deliveriesPath,matchesPath)


main()