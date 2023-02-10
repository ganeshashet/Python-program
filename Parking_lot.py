import random
class ParkingLot:
    def __init__(self, square_footage):
        self.square_footage = square_footage
        self.parking_spot_size = 96
        self.num_spots = square_footage // self.parking_spot_size
        self.lot = [None for _ in range(self.num_spots)]

    def park(self, car, spot):
        if self.lot[spot] is None:
            self.lot[spot] = car
            return f"Car with license plate {car.license_plate} parked successfully in spot {spot}"
        else:
            return f"Car with license plate {car.license_plate} could not be parked in spot {spot}"


class Car:
    def __init__(self, license_plate):
        self.license_plate = license_plate

    def __str__(self):
        return self.license_plate

    def park(self, parking_lot, spot):
        return parking_lot.park(self, spot)


def main(cars, parking_lot):
    for car in cars:
        parked = False
        while not parked:
            spot = random.randint(0, len(parking_lot.lot) - 1)
            result = car.park(parking_lot, spot)
            if "success" in result:
                parked = True
                print(result)
            else:
                print(result)

        if all(spot is not None for spot in parking_lot.lot):
            print("Parking lot is full. Exiting program.")
            break

if __name__ == "__main__":
    cars = [Car(str(i)) for i in range(10)]
    parking_lot = ParkingLot(1000)
    main(cars, parking_lot)