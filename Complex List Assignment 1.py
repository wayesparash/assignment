"""
Make a template using the dictionary data.
Your Template must have at least two sentences.
USD must be converted to BDT
example Output: Xiaomi Note 5 is made in China. The price is 300 USD which is almost equal to 30975 BDT
"""

mobile_data = {
    'status': True,
    'data': [
        {'name': 'Xiaomi Note 5', 'price': '300 USD', 'made': 'China'},
        {'name': 'Samsung Note 6', 'price': '200 USD', 'made': 'USA'},
        {'name': 'Iphone 5', 'price': '180.5 USD', 'made': 'Japan'},
        {'name': 'Pixel 5', 'price': '89.60 USD', 'made': 'Russia'},
        {'name': 'Techno 5', 'price': '110 USD', 'made': 'UK'},
        {'name': 'Huawei 5', 'price': '350 USD', 'made': 'Malaysia'},
    ],
    'exchange_rate': 107.25  # Exchange rate from USD to BDT
}
"""
Need 4 items: 
phone_name, 
phone_made_in, 
price_in_usd (will use float to convert to bdt), 
price_in_bdt
"""
# Loop through each phone in the data
for phone in mobile_data['data']:
    # Extract phone details
    phone_name = phone['name']
    phone_made_in = phone['made']

    # Extract and convert price from USD to BDT
    price_in_usd = float(phone['price'].split()[0]) #split() -space separeted list from string
    price_in_bdt = price_in_usd * mobile_data['exchange_rate']

    # Display information about the phone, including converted price
    print(f"{phone_name} is made in {phone_made_in}. The price is ${price_in_usd} USD which is almost equal to {price_in_bdt} BDT.")
