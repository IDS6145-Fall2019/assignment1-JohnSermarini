## Subway Moving Walkways Model

We have created classes corresponding to every class listed in the [**Class Diagram**](model/class_diagram.md). [**Station**](code/Station.py) contains our **main** class, and a demonstration of how our model will function can be ran using it. Currently, running **main** will create instances of all classes listed below and print their type to the screen to show they have been successfully instantiated.

* [**Station**](code/Station.py) - Contains the main class and advances time so **Passenger** objects can continuously update. It also holds the data for all the walkways and outputs of the simulation. 
* [**Passenger**](code/Passenger.py) - Represent the people in the subway station. **Passenger** contains data such as enter/exit times, speed, passenger movement state, and the passenger's route.
* [**Walkway**](code/Walkway.py) - Contains all data regarding the walkways the passengers travel on. It is used by **Station** to determine total cost and if passengers are currently using it.
* [**PassengerRoute**](code/PassengerRoute.py) - Contains the list of path that the passeneger will follow.
* [**Position**](code/Posiiton.py) - A 3D coordinate that is used by a variety of classes to represent the position of objects in the simulation.
