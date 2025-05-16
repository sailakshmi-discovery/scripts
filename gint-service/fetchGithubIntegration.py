import requests
import pandas as pd
from datetime import datetime
import csv
import os, sys

# service_name="sai-servicetitle - High"

if len(sys.argv) > 1:
        folder_changed = sys.argv[1]
        service_name=folder_changed.split('/')[1]+' - High'
        print(f"Running with service_name: {service_name}")

#Fetch the list of services from API



def fetch_github_integration_key():
    url = "https://api.pagerduty.com/services"

    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": "Token token=u+4hg4fVR--rvQpC8PLw"
    }

    limit = 25
    offset = 0
    result = []
    while True:
        params_list = {'offset' : offset, 'limit': limit}
        response = requests.get(url, headers=headers, params=params_list).json()

        for service in response['services']:
            # result.append({
            #   'Name': service['name'],
            #   'Id': service['id']
            # })   
            if service_name==service['name']:
                service_id=service['id']            
                for integration in service['integrations']:
                    if integration['summary']=='GitHub':
                        integration_id=integration['id']
                        print(service_id)
                        print(integration_id)        
                        break                
                        
                

        

        if response['more'] == True:
            offset = offset + limit
        else:
            break

    # service_id='P3IQ8PR'
    url = "https://api.pagerduty.com/services/"+service_id+"/integrations/"+integration_id

    response = requests.get(url, headers=headers).json()

    # print(response.json())
    integration_key=response['integration']['integration_key']
    print(integration_key)
    return integration_key

# Main execution flow
def main():
    try:
        integration_key = fetch_github_integration_key()
        return integration_key
        
    except Exception as e:
        print(f"Failed to complete extension update process: {e}")

if __name__ == "__main__":
    main()
  
