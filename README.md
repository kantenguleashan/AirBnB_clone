# AirBnB_clone
## Description
This team project is part of the ALX Full-Stack Software Engineer program. 
It's the first step towards building a first full web application: an AirBnB clone.
The first step consists of a custom command-line interface for data management, and the base classes for the storage of this data.

Step 1: Write a command interpreter<console>

written in Python3, and will be used to do CRUD operations (Create, Read, Update, Delete) on our AirBnB objects (User, City, Review, etc.).
Currnetly have 7 models: BaseModel, User, State, City, Amenity, Place, and Review, each instance of which is given:

a unique id generated using uuid package
the attribute created_at, a datetime object, indicating when the object is created
the attribute updated_at, a datetime object, indicating when the object is last updated
the attribute __class__, a str object, indicating what is the object's type (model)
Other attributes will be given based on the model:

User
    first_name: str object
    last_name: str object
    password: str object
    email: str
State
    name: str object
City
    state_id: str object
    name: str object
Amenity
    name: str object
Place
    city_id: str object
    user_id: str object
    name: str object
    description: str object
    number_rooms: int object
    number_bathrooms: int object
    max_guest: int object
    price_by_night: int object
    latitude: float object
    longitude: float object
    amenity_ids: list object
Review
    place_id: str object
    user_id: str object
    text: `str object
Usage:

Run ./console at the root directory of the repo to start the console Commands: create

Create an object of type . id of the newly created object will be printed after creation.

update ""

Update the attribute attribute name of the object specified by the object id with value attribute value.

destroy

Delete an object of type with id object id

show

Display an of type type with id object id

all []

Display all objects of type type. If type is not specified, display all objects.

help [command]

Show help information of command. If command is not specified, display all documented commands.

## Author
* **Ashan Kamtengule** - [kantenguleashan](https://github.com/kantenguleashan)
