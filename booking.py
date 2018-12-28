import method_chaining

# booking = Book().car('SUD810').at('2018-05-31').with_package('Kommun').for_customer('Kommunen')
class Book:
    def __init__(self, appointment=None, car=None, treatment=None, customer=None):
        self._appointment = appointment
        self._car = car
        self._treatment = treatment
        self._customer = customer

    @method_chaining.chainable
    def car(self, reg_nbr):
        self._car = Car(reg_nbr)
    
    @method_chaining.chainable
    def with_package(self, package):
        self._treatment = Treatment(package)
    
    @method_chaining.chainable    
    def at(self, date):
        self._appointment = Appointment(date)
    
    @method_chaining.chainable    
    def for_customer(self, name):
        self._customer = Customer(name)
    
    @property
    def appointment(self):
        return self._appointment
    
    @property
    def treatment(self):
        return self._treatment

    @property
    def customer(self):
        return self._customer
    
    def __str__(self):
        return 'Booking: {} with {} at {} for {}'.format(self._car, self._treatment, self._appointment, self._customer)

class Appointment:
    def __init__(self, date):
        self._date = date
        self._recurring = False
    
    @method_chaining.chainable
    def collect_at(self, time):
        self._collect_at = time
    
    @method_chaining.chainable
    def return_at(self, time):
        self._return_at = time
    
    @method_chaining.chainable    
    def recurring(self, is_recurring):
        self._recurring = is_recurring
    
    @method_chaining.chainable
    def with_interval(self, interval):
        self._interval = interval
    
    @method_chaining.chainable
    def repeat(self, times):
        self._times = times    

    @property
    def date(self):
        return self._date
    
    @property
    def pickup_tim(self):
        return self._collect_at
    
    @property
    def return_time(self):
        return self._return_at
    
    def __str__(self):
        recurring_descr = ' repeat {} times with {} weeks interval'.format(self._times, self._interval) if self._recurring else ''
        return '{} {} to {}{}'.format(self._date, self._collect_at, self._return_at, recurring_descr)

class Treatment:
    def __init__(self, package):
        self._package = package
        self._washer_fluid = False
        
    @method_chaining.chainable
    def fill_washer_fluid(self):
        self._washer_fluid = True
    
    def __str__(self):
        washer_fluid_descr = ' and fill washer fluid'
        return '{}{}'.format(self._package, washer_fluid_descr) if self._washer_fluid else '{}'.format(self._package)

class Car:
    def __init__(self, reg_nbr):
        self._reg_nbr = reg_nbr

    def __str__(self):
        return '{}'.format(self._reg_nbr)

class Customer:
    def __init__(self, name):
        self._name = name
        self._address = None
        self._postal = None
        self._city = None
        
    @method_chaining.chainable
    def address(self, adress):
        self._address = address
    
    @method_chaining.chainable
    def postal(self, postal):
        self._postal = postal
        
    @method_chaining.chainable
    def city(self, city):
        self._city = city
        
    def __str__(self):
        return '{}'.format(self._name)
    