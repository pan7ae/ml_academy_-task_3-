import requests
import concurrent.futures
from typing import Dict, Any, List

# Function to send a request and get the response
def send_request(url: str, params: Dict[str, int]) -> Dict[str, Any]:
    """
    Sends a GET request to the specified URL with given parameters.

    Args:
    - url (str): The URL to send the request to.
    - params (Dict[str, int]): Parameters to include in the request.

    Returns:
    - Dict[str, Any]: JSON response from the server.
    """
    response = requests.get(url, params=params)
    return response.json()

if __name__ == "__main__":
    # URL of your API
    url = "http://0.0.0.0:8000/forecast/"
    
    # List of different parameters (years) for requests
    years = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018]
    
    # Number of threads for execution
    num_threads = len(years)
    
    # Creating a thread pool
    with concurrent.futures.ThreadPoolExecutor(max_workers=num_threads) as executor:
        # Sending requests and getting results
        future_to_year = {executor.submit(send_request, url, {"year": year}): year for year in years}
        for future in concurrent.futures.as_completed(future_to_year):
            year = future_to_year[future]
            try:
                data = future.result()
                print(f"Year: {year}, Response: {data}")
            except Exception as e:
                print(f"Year: {year}, Error: {e}")
