from setup import Base, engine, session
from models import Restaurant, Hotel
from sqlalchemy import or_

Base.metadata.create_all(engine)

def add_rest(name, city, famous_dish):
    new_rest = Restaurant(name=name, city=city, famous_dish=famous_dish)

    session.add(new_rest)
    session.commit()
    print(f"New Restaurant {new_rest.name} added")

#add_rest("Con Tho", "Berlin", "Happy Monk")
# add_rest("Yami", "Berlin", "Noodles")
# add_rest("The Chef", "Berlin", "Pancakes")
# add_rest("The Cook", "Berlin", "Pizza")


def delete_rest(id, name):
    delete_rest = session.query(Restaurant).filter_by(id=id).first()

    if delete_rest:
        session.delete(delete_rest)
        session.commit()
        print(f"Restaurant: {delete_rest.name} deleted")
    else:
        print("Restaurant not found")

# delete_rest(4, "The Cook")



def update_rest(name, famous_dish):
    new_data = session.query(Restaurant).filter_by(name=name).first()

    if new_data:
        new_data.famous_dish = famous_dish
        session.commit()
        print(f"Restaurant {Restaurant.name} updated")
    else:
        print("Restaurant not found")


#update_rest("Yami", "Noodles")
#update_rest("Con Th", "Happy Monk")




def show_all_rest():
    # restaurants = session.query(Restaurant) \
    #                .order_by(Restaurant.name.desc()) \
    #                .all()


    # restaurant = session.query(Restaurant) \
    #               .filter(Restaurant.name == "Yami") \
    #               .one()
    # print(restaurant)

    restaurants = session.query(Restaurant) \
                  .filter(or_(Restaurant.city == "Berlin", Restaurant.city == "Munich")) \
                  .all()

    for rest in restaurants:
        print(f"Name: {rest.name}, City: {rest.city}, Famous Dish: {rest.famous_dish}")

show_all_rest()


def add_hotel(name, city):
    new_hotel = Hotel(hotel_name=name, hotel_city=city)

    session.add(new_hotel)
    session.commit()
    print(f"New Hotel {new_hotel.hotel_name} added")

add_hotel("The Inn", "Berlin")
# add_hotel("Hilton", "Berlin")
# add_hotel("The Castle", "Berlin")


def delete_hotel(hotel_city):
    delete_hotel = session.query(Hotel).filter_by(hotel_city=hotel_city).all()
    if delete_hotel:
        for hotel in delete_hotel:
            session.delete(hotel)
            print(f"Hotel: {hotel.hotel_name} deleted")
        session.commit()

    else:
        print("Hotel not found")

#delete_hotel("Berlin")


def update_hotels(hotel_id, hotel_name, hotel_city):
    new_data = session.query(Hotel).filter_by(hotel_id=hotel_id).first()

    if new_data:
        new_data.hotel_name = hotel_name
        new_data.hotel_city = hotel_city
        session.commit()
        print(f"Hotel {Hotel.hotel_name} updated")
    else:
        print("Hotel not found")

#update_hotels(3,"The Hilton", "New York")


def show_hotels():
    # hotels = session.query(Hotel) \
    #          .filter(Hotel.hotel_name == "The Inn") \
    #          .all()

    # hotels = session.query(Hotel) \
    #         .order_by(Hotel.hotel_name.asc()) \
    #         .all()

    # hotels = session.query(Hotel) \
    #         .filter(Hotel.hotel_city == "Berlin") \
    #         .all()

    hotels = session.query(Hotel) \
            .filter(Hotel.hotel_name.like("T%")) \
            .all()

    for hotel in hotels:
        print(hotel.hotel_name, hotel.hotel_city)

show_hotels()





