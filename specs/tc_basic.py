import unittest
from FireGirlPolicy import FireGirlPolicy
from FireGirlPathway import FireGirlPathway

class TestBasic(unittest.TestCase):
    

    def test_Draw_Ignition_Day(self):
        # This test draws a random day to simulate an ignition. 
        # Possible return values are:
        #  -1 -> no ignition this year
        #  positive integer -> date (out of 365) of the ignition
        policy = FireGirlPolicy(None,0,10)
        landscape = FireGirlPathway(1,policy,True)
        for i in range(10000):
            d = landscape.drawIgnitionDay()
            self.assertGreaterEqual(d, -1)
            self.assertLessEqual(d, 364)
                    
    def test_Temperature_Range(self):
        # This test checks for valid temperatures.
        policy = FireGirlPolicy(None,0,10)
        landscape = FireGirlPathway(1,policy,True)
        for i in range(365):
            mean = landscape.tempMean(i)
            self.assertGreaterEqual(mean, -90.0)
            self.assertLessEqual(mean, 90.0)
            
    def test_Generate_New_Pathway(self):
        # This test checks that the GenerateNewPathway function does not fail.
        policy = FireGirlPolicy(None,0,10)
        landscape = FireGirlPathway(1,policy,True)
        self.assertFalse(landscape.generateNewPathway())
        
        
if __name__ == '__main__':
    unittest.main()