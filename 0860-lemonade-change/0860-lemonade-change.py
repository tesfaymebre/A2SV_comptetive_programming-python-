class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        fives = 0
        tens = 0
        
        for bill in bills:
            if bill == 5:
                fives += 1
            elif bill == 10:
                tens += 1
                
                if fives == 0:
                    return False
                
                fives -= 1
            else:
                if tens > 0 and fives > 0:
                    tens -= 1
                    fives -= 1
                elif fives >= 3:
                    fives -= 3
                else:
                    return False
                
        return True
                    