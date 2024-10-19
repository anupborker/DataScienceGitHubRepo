import json
import pymongo

def read_json(file_path):
    with open(file_path) as f:
        return json.load(f)

def create_city_to_country_map():
    """Generate a mapping of cities to their respective countries."""
    return {
        "newyork": "usa",
        "dallas": "usa",
        "beijing": "china",
        "colombo": "sri_lanka",
        "hongkong": "china",
        "kandy": "sri_lanka",
        "wuhan": "china",
        "chicago": "usa"
    }

def mongo_connection(database, collection):
    """Connect to a specified MongoDB database and collection."""
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client[database]
    return db[collection]

def compute_total_cost(ticket_info, visa_fees, city_country_map):
    """Compute the total cost associated with a ticket."""
    last_location = ticket_info['visa_stamped_location'][-1]
    associated_country = city_country_map.get(last_location)
    if associated_country:
        visa_fee = visa_fees[associated_country]
        return visa_fee + int(ticket_info['ticket_price'])
    return None

def display_passenger_info(ticket_list, visa_fees, city_country_map):
    """Display the information for each passenger along with total cost."""
    print('Passenger Information:')
    for ticket_info in ticket_list:
        total_cost = compute_total_cost(ticket_info, visa_fees, city_country_map)
        if total_cost is not None:
            print(f"Passenger ID {ticket_info['ticket_id']}: Name: {ticket_info['passenger_name']}, Total Cost: {total_cost}")

def execute():
    json_data = read_json("data.json")
    city_country_map = create_city_to_country_map()
    ticket_collection = mongo_connection("Passenger_Management_System", "tickets")

    ticket_list = list(ticket_collection.find({}))
    display_passenger_info(ticket_list, json_data['visa_rates'], city_country_map)

if __name__ == "__main__":
    execute()
