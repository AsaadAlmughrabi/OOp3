import pytest
from stratgy_design.stratgy_design import Car, Bicycle, Bus, TransportationContext

@pytest.fixture
def car_transportation():
    return TransportationContext(Car())

@pytest.fixture
def bicycle_transportation():
    return TransportationContext(Bicycle())

@pytest.fixture
def bus_transportation():
    return TransportationContext(Bus())

def test_car_travel_time(car_transportation):
    distance = 50
    assert car_transportation.calculate_travel_time(distance) == distance / 60

def test_car_travel_cost(car_transportation):
    distance = 50
    assert car_transportation.calculate_travel_cost(distance) == distance * 0.2

def test_bicycle_travel_time(bicycle_transportation):
    distance = 50
    assert bicycle_transportation.calculate_travel_time(distance) == distance / 15

def test_bicycle_travel_cost(bicycle_transportation):
    distance = 50
    assert bicycle_transportation.calculate_travel_cost(distance) == 0

def test_bus_travel_time(bus_transportation):
    distance = 50
    assert bus_transportation.calculate_travel_time(distance) == distance / 30

def test_bus_travel_cost(bus_transportation):
    distance = 50
    assert bus_transportation.calculate_travel_cost(distance) == distance * 0.1
