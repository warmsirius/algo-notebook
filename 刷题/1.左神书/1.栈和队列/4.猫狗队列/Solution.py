class Pet(object):
    def __init__(self, type):
        self._type = type

    def getPetType(self):
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

    def getPet(self) -> Pet:
        return self.pet

    def getCount(self) -> int:
        return self.count

    def getPetType(self) -> str:
        return self.pet.getPetType()


class DogCatQueue(object):
    def __init__(self):
        self._dogQ = Queue()
        self._catQ = Queue()
        self._count = 0

    def add(self, pet: Pet):
        if pet.getPetType() == "dog":
            self._count += 1
            self._dogQ.put(PetEnterQueue(pet, self._count))
        elif pet.getPetType() == "cat":
            self._count += 1
            self._catQ.put(PetEnterQueue(pet, self._count))
        else:
            raise RuntimeError("err, not dog or cat")

    def pollAll(self):
        if (not self._dogQ.isEmpty()) and (not self._catQ.isEmpty()):
            if self._dogQ.peek().getCount() < self._catQ.peek().getCount():
                return self._catQ.poll().getPet()
            else:
                return self._dogQ.poll().getPet()
        elif not self._dogQ.isEmpty():
            return self._dogQ.poll().getPet()
        elif not self._catQ.isEmpty():
            return self._catQ.poll().getPet()
        else:
            raise RuntimeError("err, queue is empty!")

    def pollDog(self):
        if not self._dogQ.isEmpty():
            return self._dogQ.poll().getPet()
        else:
            raise RuntimeError("err, dog queue is empty!")

    def pollCat(self):
        if not self._catQ.isEmpty():
            return self._catQ.poll().getPet()
        else:
            raise RuntimeError("err, cat queue is empty!")

    def isEmpty(self):
        return self._dogQ.isEmpty() and self._catQ.isEmpty()

    def isDogEmpty(self):
        return self._dogQ.isEmpty()

    def isCatEmpty(self):
        return self._catQ.isEmpty()


class Queue(object):
    """队列"""

    def __init__(self):
        self.queue = []

    def push(self, data):
        self.queue.append(data)

    def poll(self):
        if not self.isEmpty():
            return self.queue.pop(0)
        else:
            raise RuntimeError('StackError: fail to pop, the stack is empty.')

    def isEmpty(self):
        return self.length() == 0

    def peek(self):
        if not self.isEmpty():
            return self.queue[0]
        else:
            raise RuntimeError("The queue is empty.")

    def length(self):
        return len(self.queue)
