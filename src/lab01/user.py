class User:
    total_users = 0
    
    def __init__(self, name: str, blood_type: str, weight: float, age: int, email: str, city: str):
        self.name = name
        self.blood_type = blood_type
        self.weight = weight
        self.age = age
        self.email = email
        self.city = city
        User.total_users += 1

    def _validate_email(self, email):
        if '@' not in email:
            raise ValueError("Invalid email address")
        return email
        
    def _validate_blood_type(self, blood_type):
        valid_blood_types = ['A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', 'O+', 'O-']
        if blood_type not in valid_blood_types: 
            raise ValueError("Invalid blood type")
        return blood_type
    
    def _validate_weight(self, weight):
        if weight <= 0:
            raise ValueError("Weight must be positive")
        return weight
        
    def _validate_age(self, age):
        if age <= 0: 
            raise ValueError("Age must be greater than 0")
        return age
        
    def _validate_city(self, city):
        if not city or not city.strip():    
            raise ValueError("City cannot be empty")    
        return city  
    
    @property
    def email(self):
        return self._email  
    
    @email.setter
    def email(self, value):
        self._validate_email(value)
        self._email = value
    
    @property
    def blood_type(self):
        return self._blood_type
    
    @blood_type.setter
    def blood_type(self, value):
        self._validate_blood_type(value)
        self._blood_type = value

    @property
    def weight(self):
        return self._weight 
    
    @weight.setter
    def weight(self, value):
        self._validate_weight(value)
        self._weight = value

    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, value):
        self._validate_age(value)
        self._age = value
    
    @property
    def name(self):
        return self._name   
    
    @name.setter
    def name(self, value):
        if not value or not value.strip():
            raise ValueError("Name cannot be empty")
        self._name = value

    @property
    def city(self):
        return self._city
    
    @city.setter
    def city(self, value):  
        self._validate_city(value)
        self._city = value
    
    def __str__(self):
        return f"User(name={self._name}, blood_type={self._blood_type}, weight={self._weight}, age={self._age}, email={self._email}, city={self._city})"
    
    def __eq__(self, other):
        if isinstance(other, User):
            return self._email == other._email
        return False
    
    def is_adult(self):
        return self._age >= 18