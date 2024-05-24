from abc import ABC, abstractmethod
from enum import Enum


class TransportationEnum(Enum):
    """Enumeration of transportation methods."""
    CAR = 1
    BICYCLE = 2
    BUS = 3


class TransportationStrategy(ABC):
    """Abstract base class for transportation strategy."""

    @abstractmethod
    def calculate_time(self, distance):
        """Calculate travel time based on distance."""
        pass

    @abstractmethod
    def calculate_cost(self, distance):
        """Calculate travel cost based on distance."""
        pass


class Car(TransportationStrategy):
    """Concrete implementation of transportation strategy for cars."""

    def calculate_time(self, distance):
        """Calculate travel time for a car based on distance."""
        return distance / 60  # average speed of 60 km/h

    def calculate_cost(self, distance):
        """Calculate travel cost for a car based on distance."""
        return distance * 0.2  # Assuming cost per km is $0.2


class Bicycle(TransportationStrategy):
    """Concrete implementation of transportation strategy for bicycles."""

    def calculate_time(self, distance):
        """Calculate travel time for a bicycle based on distance."""
        return distance / 15  # average speed of 15 km/h

    def calculate_cost(self, distance):
        """Calculate travel cost for a bicycle based on distance."""
        return 0  # Assuming no cost for bicycle transportation


class Bus(TransportationStrategy):
    """Concrete implementation of transportation strategy for buses."""

    def calculate_time(self, distance):
        """Calculate travel time for a bus based on distance."""
        return distance / 30  # average speed of 30 km/h

    def calculate_cost(self, distance):
        """Calculate travel cost for a bus based on distance."""
        return distance * 0.1  # Assuming cost per km is $0.1


class TransportationContext:
    """Context class that uses a transportation strategy."""

    def __init__(self, transportation_strategy):
        """Initialize with a transportation strategy."""
        self.transportation_strategy = transportation_strategy

    def calculate_travel_time(self, distance):
        """Calculate travel time based on distance using the chosen transportation strategy."""
        return self.transportation_strategy.calculate_time(distance)

    def calculate_travel_cost(self, distance):
        """Calculate travel cost based on distance using the chosen transportation strategy."""
        return self.transportation_strategy.calculate_cost(distance)


if __name__ == "__main__":
    # Creating transportation context objects for different strategies
    car_transportation = TransportationContext(Car())
    bicycle_transportation = TransportationContext(Bicycle())
    bus_transportation = TransportationContext(Bus())

    # Distance to be traveled (in km)
    distance = 50

    # Calculate travel time and cost using different methods
    print("Using Car:")
    print("  Travel Time:", car_transportation.calculate_travel_time(distance), "hours")
    print("  Cost:", car_transportation.calculate_travel_cost(distance))

    print("\nUsing Bicycle:")
    print("  Travel Time:", bicycle_transportation.calculate_travel_time(distance), "hours")
    print("  Cost:", bicycle_transportation.calculate_travel_cost(distance))

    print("\nUsing Bus:")
    print("  Travel Time:", bus_transportation.calculate_travel_time(distance), "hours")
    print("  Cost:", bus_transportation.calculate_travel_cost(distance))
