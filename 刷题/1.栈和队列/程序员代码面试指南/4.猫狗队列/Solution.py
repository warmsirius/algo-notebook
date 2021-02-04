class Queue(object):
    """队列"""

    def __init__(self):
        self.queue = []

    def put(self, data):
        self.queue.append(data)

    def poll(self):
        if not self.is_empty():
            return self.queue.pop(0)
        else:
            raise RuntimeError('StackError: fail to pop, the stack is empty.')

    def is_empty(self):
        return self.length() == 0

    def peek(self):
        if not self.is_empty():
            return self.queue[0]
        else:
            raise RuntimeError("The queue is empty.")

    def length(self):
        return len(self.queue)


class Pet(object):
    def __init__(self, type):
        self._type = type

    @property
    def pet_type(self):
        return self._type


class Cat(Pet):
    def __init__(self):
        super().__init__("cat")


class Dog(Pet):
    def __init__(self):
        super().__init__("dog")


class PetEnterQueue(object):
    def __init__(self, pet: Pet, count: int):
        self.pet = pet
        self.count = count

    def get_pet(self) -> Pet:
        return self.pet

    def get_count(self) -> int:
        return self.count

    def get_pet_type(self) -> str:
        return self.pet.pet_type


class DogCatQueue(object):
    def __init__(self):
        self._CatQ = Queue()
        self._DogQ = Queue()
        self._count = 0

    def add(self, pet):
        if pet.pet_type == "cat":
            self._count += 1
            self._CatQ.put(PetEnterQueue(pet, self._count))
        elif pet.pet_type == "dog":
            self._count += 1
            self._DogQ.put(PetEnterQueue(pet, self._count))
        else:
            raise RuntimeError("err: not dog or cat!")

    def poll_all(self):
        if self._CatQ.is_empty() and self._DogQ.is_empty():
            return None
        elif self._CatQ.is_empty() and not self._DogQ.is_empty():
            return self._DogQ.poll().get_pet()
        elif not self._CatQ.is_empty() and self._DogQ.is_empty():
            return self._CatQ.poll().get_pet()
        elif self._CatQ.peek().get_count() > self._DogQ.poll().get_count():
            return self._CatQ.poll().get_pet()
        else:
            return self._DogQ.poll().get_pet()

    def poll_cat(self):
        if self._CatQ.is_empty():
            return None
        else:
            return self._CatQ.poll().get_pet()

    def poll_dog(self):
        if self._DogQ.is_empty():
            return None
        else:
            return self._DogQ.poll().get_pet()


if __name__ == "__main__":
    dog_cat_q = DogCatQueue()
    dog_cat_q.add(Cat())
    dog_cat_q.add(Dog())
    dog_cat_q.add(Cat())
    dog_cat_q.add(Dog())
    dog_cat_q.add(Dog())

    assert dog_cat_q.poll_dog().pet_type == "dog"
    assert dog_cat_q.poll_cat().pet_type == "cat"
    assert dog_cat_q.poll_all().pet_type == "dog"
