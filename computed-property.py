from pydantic import BaseModel, computed_field, Field


class Product(BaseModel):
    price: float
    quantity: int


    @computed_field
    @property
    def total_price(self) -> float:
        return self.price * self.quantity
    

class Booking(BaseModel):
    user_id: int
    room_id: int
    nights: int = Field(..., gt=0, description="Number of nights for the booking", example=3)
    rate_per_night: float = Field(..., gt=0, description="Rate per night for the booking", example=100.00)


    @computed_field
    @property
    def total_cost(self) -> float:
        return self.nights * self.rate_per_night
    

booking = Booking(user_id=1, room_id=101, nights=3, rate_per_night=100.00)
print(booking)
print(f"Total cost for the booking: {booking.total_cost}")

print(booking.model_dump())  # This will include the computed field 'total_cost' in the output