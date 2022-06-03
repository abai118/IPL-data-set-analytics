import unittest

import code 




class testcode(unittest.TestCase) :
    
    def test_1st(self):
        
        #return(data.values())
        test1=[1,2,1,3,1,4,3,1,1,2]
        #test2=[1,2,1,3,1,4,3,1,1,0]
        result=code.NumberOfMatchesPlayedPerYearForAllTheYearsInIPL("/home/akhil118/Desktop/git/IPL  project/IPL-data-set-analytics/matchesTesting.csv")
        self.assertEqual(result,test1)
        #self.assertEqual(result,test2)
        
    def test_2nd(self):
         
        #return(list(totalTeamsPerYear.values())[0])
        test1={'Sunrisers Hyderabad': 3, 'Deccan Chargers': 1, 'Gujarat Lions': 1, 'Mumbai Indians': 1, 'Kings XI Punjab': 0, 'Kochi Tuskers Kerala': 0, 'Rajasthan Royals': 3, 'Kolkata Knight Riders': 3, 'Royal Challengers Bangalore': 4}
        #test2={'Sunrisers Hyderabad': 3, 'Deccan Chargers': 2, 'Gujarat Lions': 1, 'Mumbai Indians': 1, 'Kings XI Punjab': 0, 'Kochi Tuskers Kerala': 0, 'Rajasthan Royals': 3, 'Kolkata Knight Riders': 3, 'Royal Challengers Bangalore': 4}
        result=code.NumberOfMatchesWonPerTeamPerYearInIPL("/home/akhil118/Desktop/git/IPL  project/IPL-data-set-analytics/matchesTesting.csv")
        self.assertEqual(result,test1)
        #self.assertEqual(result,test2)
        
        
        
        
        
if __name__=="__main__" :
    
    unittest.main()