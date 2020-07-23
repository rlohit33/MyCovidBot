import requests
import json
import pandas
import requests
import pandas as pd
import matplotlib.pyplot as plt


def get_data(msg):
    url = "https://corona-virus-world-and-india-data.p.rapidapi.com/api_india"

    headers = {
    'x-rapidapi-host': "corona-virus-world-and-india-data.p.rapidapi.com",
    'x-rapidapi-key': "bbdf3b05cbmsh4cb487e3d7e8f2ep13fec5jsn5d38336adc63"
    }

    response = requests.request("GET", url, headers=headers)
    data=response.text
    data=json.loads(data)
    
    if msg == 'Hi' or msg =='hi' or msg =='Hello' or msg == 'hello':
        data_complete = "Hey, I am a Covid Bot. Please type in State or District Name"
        
        return(str(data_complete))


    elif msg == 'India':
        Active_cases = data['total_values']['active']
        Total_cases = data['total_values']['confirmed']
        Total_Deaths = data['total_values']['deaths']
        Migrated = data['total_values']['migratedother']
        Recovered = data['total_values']['recovered']
        
        data_complete = "Total Cases : " +str(Total_cases)+"\nActive Cases : " +str(Active_cases)+ "\nTotal Deaths : " +str(Total_Deaths)+ "\nTotal Recovered : "+str(Recovered)+ "\nMigrated : " +str(Migrated)
        return(str(data_complete))
      
    elif msg in data['state_wise']:
       
       Active_cases = data['state_wise'][msg]['active']
       Total_cases = data['state_wise'][msg]['confirmed']
       Total_Deaths = data['state_wise'][msg]['deaths']
       Migrated = data['state_wise'][msg]['migratedother']
       Recovered = data['state_wise'][msg]['recovered']
       data_complete = "Total Cases : " +str(Total_cases)+"\nActive Cases : " +str(Active_cases)+ "\nTotal Deaths : " +str(Total_Deaths)+ "\nTotal Recovered : "+str(Recovered)+ "\nMigrated : " +str(Migrated)
       return(str(data_complete))
       
    
    
    for state in data['state_wise']:  
      #  print(msg)
        if msg in data['state_wise'][state]['district']:
            Active_cases = data['state_wise'][state]['district'][msg]['active']
            Total_cases = data['state_wise'][state]['district'][msg]['confirmed']
            Total_Deaths = data['state_wise'][state]['district'][msg]['deceased']
            Recovered = data['state_wise'][state]['district'][msg]['recovered']
            data_complete = "Total Cases : " +str(Total_cases)+"\nActive Cases : " +str(Active_cases)+ "\nTotal Deaths : " +str(Total_Deaths)+ "\nTotal Recovered : "+str(Recovered)
            return(str(data_complete))
    
    else:
        data_complete = 'Oops, Please type in the correct Name. Make sure first letter is Capital!'
        return(str(data_complete))
        
        

                        
            
    
   








