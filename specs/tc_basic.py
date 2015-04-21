import unittest

class TestBasic(unittest.TestCase):
    
    def test_Draw_Ignition_Day(self):
        
        from FireGirlPolicy import FireGirlPolicy
        from FireGirlPathway import FireGirlPathway
        
        policy = FireGirlPolicy(None,0,10)
        landscape = FireGirlPathway(1,policy,True)
        
        #This function draws a random day to simulate an ignition. 
        #Possible return values are:
        #  -1 -> no ignition this year
        #  positive integer -> date (out of 365) of the ignition
        for i in range(10000):
            d = landscape.drawIgnitionDay()
            self.assertGreaterEqual(d, -1)
            self.assertLessEqual(d, 364)
                    
                    
if __name__ == '__main__':
    unittest.main()