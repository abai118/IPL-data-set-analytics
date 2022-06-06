import unittest
import matplotlib.pyplot as plt
import code
import numpy as np


mockMatchesPath = "/home/akhil118/Desktop/git/IPL/mock_matches.csv"
mockDelPath = "/home/akhil118/Desktop/git/IPL/mock_deliveries.csv"


class testcode(unittest.TestCase):

    def test_1st(self):

        test1 = {'2008': 1, '2009': 2, '2010': 1, '2011': 3, '2012': 1,
                 '2013': 4, '2014': 3, '2015': 1, '2016': 1, '2017': 2}
        # test2 = {'2008': 1, '2009': 4, '2010': 3, '2011': 3, '2012': 1,
        #          '2013': 3, '2014': 4, '2015': 1, '2016': 1, '2017': 2}
        result = code.NoOfMatchesPlayedPerYear(mockMatchesPath)
        self.assertEqual(result, test1)
        # self.assertEqual(result,test2)

        x = list(result.keys())
        y1 = list(result.values())
        y2 = list(test1.values())
        data = [y1, y2]
        X = np.arange(len(x))
        plt.bar(X + 0.00, data[0], color='b', width=0.25)
        plt.bar(X + 0.25, data[1], color='g', width=0.25)

        plt.show()

    def test_2nd(self):

        # return(list(totalTeamsPerYear.values())[0])
        test1 = {'Sunrisers Hyderabad': 3, 'Deccan Chargers': 1,
                 'Gujarat Lions': 1, 'Mumbai Indians': 1, 'Kings XI Punjab': 0,
                 'Kochi Tuskers Kerala': 0, 'Rajasthan Royals': 3,
                 'Kolkata Knight Riders': 3, 'Royal Challengers Bangalore': 4}
        # test2 = {'Sunrisers Hyderabad': 3, 'Deccan Chargers': 2,
        #          'Gujarat Lions': 1, 'Mumbai Indians':1,
        #          'Kings XI Punjab': 0,
        #          'Kochi Tuskers Kerala': 0, 'Rajasthan Royals': 3,
        #          'Kolkata Knight Riders': 3,
        #          'Royal Challengers Bangalore': 4}

        result = code.NumberOfMatchesWonPerTeamPerYearInIPL(mockMatchesPath)
        self.assertEqual(result, test1)
        # self.assertEqual(result, test2)

        x = list(result.keys())
        y1 = list(result.values())
        y2 = list(test1.values())
        data = [y1, y2]
        X = np.arange(len(x))
        plt.bar(X + 0.00, data[0], color='b', width=0.25)
        plt.bar(X + 0.25, data[1], color='g', width=0.25)
        plt.show()

    def test_3rd(self):

        # return(list(totalTeamsPerYear.values())[0])
        test1 = {'Mumbai Indians': 0, 'Royal Challengers Bangalore': 0,
                 'Delhi Daredevils': 1, 'Gujarat Lions': 3}
        # test2 = {'Mumbai Indians': 2, 'Royal Challengers Bangalore': 1,
        #          'Delhi Daredevils': 1, 'Gujarat Lions': 3}

        result = code.ExtraRunsPerTeamIn2016(mockDelPath, mockMatchesPath)
        self.assertEqual(result, test1)
        # self.assertEqual(result, test2)

        x = list(result.keys())
        y1 = list(result.values())
        y2 = list(test1.values())
        data = [y1, y2]
        X = np.arange(len(x))
        plt.bar(X + 0.00, data[0], color='b', width=0.25)
        plt.bar(X + 0.25, data[1], color='g', width=0.25)
        plt.show()

    def test_4th(self):

        # return(list(totalTeamsPerYear.values())[0])
        test1 = {'SL Malinga': 0.0, 'D Wiese': 5.142857142857142,
                 'JJ Bumrah': 7.714285714285715, 'J Suchith': 10.0,
                 'S Aravind': 10.5, 'HV Patel': 10.8, 'MJ McClenaghan': 13.0,
                 'MA Starc': 14.399999999999999, 'Harbhajan Singh': 15.0,
                 'YS Chahal': 16.0}
        # test2 = {'SL Malinga': 3.5, 'D Wiese': 5.142857142857,
        #          'JJ Bumrah': 7.714285714285715, 'J Suchith': 1.0,
        #          'S Aravind': 1.5, 'HV Patel': 10.8, 'MJ McClenaghan': 13.0,
        #          'MA Starc': 14.399999999999999, 'Harbhajan Singh': 15.0,
        #          'YS Chahal': 16.0}

        result = code.Top10EconomicalBowlerIn2015(mockDelPath, mockMatchesPath)
        self.assertEqual(result, test1)
        # self.assertEqual(result, test2)

        x = list(result.keys())
        y1 = list(result.values())
        y2 = list(test1.values())
        data = [y1, y2]
        X = np.arange(len(x))
        plt.bar(X + 0.00, data[0], color='b', width=0.25)
        plt.bar(X + 0.25, data[1], color='g', width=0.25)
        plt.show()


if __name__ == "__main__":

    unittest.main()
