class Challenge_tools: 
    
    
    def get_season(date):
        '''this method finds the season from a given date based on the following assumptions:
                fall starts on: September 20
                winter starts on: December 20
                spring starts on: March 20
                summer start on: June 20
                
            :param date: the date for which we want to get the season 
            
            :return: the season as a string
        '''
        
        
        season= {0:'Fall',1:'Winter',2:'Spring',3:'Summer'}
        day = int(date.day)
        month = int(date.month)
        score = (int(month%3!=0)+int(month%3==0)*int(day>20) + int(month/3))%4
        
        return season[score]