from orders import db
from datetime import date, datetime


class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    car_number = db.Column(db.Integer, unique=True)
    client_passport_number = db.Column(db.String, unique=True)
    add_date = db.Column(db.Date, default=date.today(), nullable=False)
    rental_time = db.Column(db.Integer, nullable=False)
    car_rental_cost = db.Column(db.Float, nullable=False)
    total_cost = db.Column(db.Float, nullable=False)
    owner = db.Column(db.Integer(), db.ForeignKey("client.id"))

    __table_args__ = (
        db.CheckConstraint(rental_time >= 1, name='minimal_rental_time'),
    )

    def calculate_total_cost(self):
        self.total_cost = self.rental_time * self.car_rental_cost


class Client(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    registration_date = db.Column(db.Date, default=date.today(), nullable=False)
    number_of_orders = db.Column(db.Integer, default=0)
    order = db.relationship("Order", backref="owned_user", lazy=True)

    def __repr__(self):
        return '<Client {} {}>'.format(self.first_name, self.last_name)


