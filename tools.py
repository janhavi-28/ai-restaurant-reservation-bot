import json

# Load restaurant data
with open("restaurants.json", "r", encoding="utf-8") as f:
    RESTAURANTS = json.load(f)

def search_restaurants(location, cuisine, guests, time):
    matches = [r for r in RESTAURANTS if r["location"].lower() == location.lower()
               and r["cuisine"].lower() == cuisine.lower()
               and r["seating"] >= guests]

    if matches:
        names = [r["name"] for r in matches]
        return f"Here are some {cuisine} restaurants in {location} for {guests} guests at {time}:\n- " + "\n- ".join(names)
    else:
        return f"📌 Sorry, no {cuisine} restaurants in {location} with seating for {guests} available at {time}."

def book_table(location, cuisine, guests, time):
    matches = [r for r in RESTAURANTS if r["location"].lower() == location.lower()
               and r["cuisine"].lower() == cuisine.lower()
               and r["seating"] >= guests]

    if matches:
        return f"✅ Table for {guests} at a {cuisine} restaurant in {location} at {time} has been booked!"
    else:
        return f"📌 Sorry, no available {cuisine} restaurants in {location} for {guests} people at {time}."