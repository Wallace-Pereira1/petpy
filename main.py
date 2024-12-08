# Tamagotchi Teste

from random import randrange

class Tamagochi(object):
    """um bichinho virtual"""
    humor_reduce = 3
    humor_max = 10
    humor_warning = 3
    comida_reduce = 2
    comida_max = 10
    comida_warning = 3
    voz = ['"que odio mano"']

    def _init_(self, name, animal_type):
        self.name = name
        self.animal_tyle = animal_type
        self.food = randrange(self.comida_max)
        self.humor = randrange(self.humor_max)
        self.voz = self.voz[:]

        def __clock_tick(self):
            self.humor -= 1
            self.comida -= 1

        @property
        def mood(self):
            if self.comida > self.comida_warning and self.humor > self.humor_warning:
                return "feliz"
            elif self.comida < self.comida_warning:
                return "que fome..."
            else:
                return "estou entediado..."
        def __str__(self):
            return "\nI'm " + self.name + "." + "\nI estou" + self.mood() + "."
        def teach(self, word):
            self.voz.append(word)
            self._clock_tick()

        def talk(self):
            print("I am a ", self.animal_type, " named ", self.name, ".", "I feel", self.mood(), now.\n")
                  self.animal_type,
                  " named ",

        )