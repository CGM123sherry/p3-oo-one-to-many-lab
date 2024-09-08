# owner_pet.py

class Owner:
    def __init__(self, name):
        self.name = name

    def pets(self):
        """Returns a list of all pets that belong to this owner."""
        return [pet for pet in Pet.all if pet.owner == self]

    def add_pet(self, pet):
        """
        Adds a pet to this owner after validating that the pet is an instance of Pet.
        Raises:
            Exception: If the pet is not an instance of Pet.
        """
        if not isinstance(pet, Pet):
            raise Exception("pet must be an instance of Pet class")
        pet.owner = self

    def get_sorted_pets(self):
        """Returns a list of the owner's pets sorted by their names."""
        return sorted(self.pets(), key=lambda pet: pet.name)


class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner=None):
        """
        Initializes a new Pet instance.
        
        Args:
            name (str): The name of the pet.
            pet_type (str): The type of the pet. Must be one of PET_TYPES.
            owner (Owner, optional): The owner of the pet. Defaults to None.
        
        Raises:
            Exception: If pet_type is not in PET_TYPES.
            Exception: If owner is provided but is not an instance of Owner.
        """
        if pet_type not in Pet.PET_TYPES:
            raise Exception(f"Invalid pet_type '{pet_type}'. Must be one of {Pet.PET_TYPES}.")
        
        if owner is not None and not isinstance(owner, Owner):
            raise Exception("owner must be an instance of Owner class")
        
        self.name = name
        self.pet_type = pet_type
        self._owner = None  # Use a protected attribute to store owner
        if owner:
            self.owner = owner  # Utilize the setter for validation
        
        Pet.all.append(self)

    @property
    def owner(self):
        """Gets the owner of the pet."""
        return self._owner

    @owner.setter
    def owner(self, value):
        """
        Sets the owner of the pet after validating that the value is an instance of Owner.
        
        Args:
            value (Owner): The new owner to assign to the pet.
        
        Raises:
            Exception: If value is not an instance of Owner.
        """
        if not isinstance(value, Owner):
            raise Exception("owner must be an instance of Owner class")
        self._owner = value

    def __repr__(self):
        return f"Pet(name='{self.name}', pet_type='{self.pet_type}', owner='{self.owner.name if self.owner else None}')"
