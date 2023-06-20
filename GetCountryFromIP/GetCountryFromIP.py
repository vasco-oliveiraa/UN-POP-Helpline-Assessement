import requests
import socket
import geoip2.database
import os

def get_country_from_ip():
    try:
        hostname = socket.gethostname()
        ip_address = socket.gethostbyname(hostname)
    except socket.error:
        ip_address = None
        
    if ip_address:
        
        dataset_path = 'GeoLite2-Country.mmdb'
        current_directory = os.path.dirname(os.path.abspath(__file__))
        dataset_full_path = os.path.join(current_directory, dataset_path)

        # Load the GeoLite2 database
        reader = geoip2.database.Reader(dataset_full_path)
    
        try:
            # Lookup the IP address
            response = reader.country(ip_address)
            country = response.country.name
        except geoip2.errors.AddressNotFoundError:
            # Handle the case when IP address is not found in the database
            country=None
    
    if country:
        return country
    
    else:
        try:
            response = requests.get('https://api.ipify.org?format=json')
            data = response.json()
            ip_address = data['ip']

        except requests.exceptions.RequestException:
            return None
        
        if ip_address:
            
            dataset_path = 'GeoLite2-Country.mmdb'
            current_directory = os.path.dirname(os.path.abspath(__file__))
            dataset_full_path = os.path.join(current_directory, dataset_path)

            # Load the GeoLite2 database
            reader = geoip2.database.Reader(dataset_full_path)

            try:
                # Lookup the IP address
                response = reader.country(ip_address)
                country = response.country.name
            except geoip2.errors.AddressNotFoundError:
                # Handle the case when IP address is not found in the database
                country=None
    
            return country    