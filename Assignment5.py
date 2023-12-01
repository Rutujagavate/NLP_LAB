##  Assignment No 5 ###
# Name : Gavate Rutuja Pandurang
# Batch : B2
# Roll No : 21
# Assignment Title :Implement regular expression function to find Postal Code, PAN
#number, Mobile number in textual data using python libraries
import re

def find_entities(text):

    result = {
        'Postal Code': re.findall(r'[0-9]{3}[-]{1}[0-9]{3}', text),
        'PAN Numbers': re.findall(r'[A-Z]{5}[0-9]{4}[A-Z]', text),
        'Mobile Number':re.findall(r'[+]{1}[0-9]{2}[ ]{1}[0-9]{10}', text),         
    }
    return result

# Example usage:
sample_text = """
First Dataset
Postal Code of Pimpalgaon is 414503.
My PAN Number is CTDPN0259J.
Mobile Number is +91 9356537050.


Second Dataset
Postal Code of Ahmednagar is 410-001
My PAN Number is KLERU6729T.
Mobile Number is +91 9653338962.
"""

result = find_entities(sample_text)

for entity_type, entities in result.items():
    print(f"{entity_type}: {entities}")

# Output
''' 
Postal Code: ['414503', '410-001']
PAN Numbers: ['CTDPN0259J', 'KLERU6729T']
Mobile Number: ['+91 9356537050', '+91 9653338962']

'''
