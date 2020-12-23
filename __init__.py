class Organ():
    def __init__(self,name,condition='fair'):
        self.condition = condition
        self.name = name
    def __str__(self):
        return f'{self.name} is doing {self.condition}'
class Stomach(Organ):
    def __init__(self,contents=[],condition='fair'):
        super().__init__(
            name='stomach',
            condition=condition
            )
        self.contents = contents
    def __str__(self):
        if len(self.contents) == 0:
            return f'The {self.name} is empty, feed it please.'
        else:
            return f'The {self.name} has some {len(self.contents)} items remaining.'
    def digest(self):
        if len(self.contents)>0:
            self.contents = self.contents[1:]
            return 1
        else:
            return 0
class Heart(Organ):
    def __init__(self,resting_bpm,condition='fair'):
        super().__init__(
            name='heart',
            condition=condition
            )
        self.resting_bpm = resting_bpm
        self.bpm = self.resting_bpm
    def __str__(self):
        return f'The {self.name} is in {self.condition} condition and the resting beats per minute is {self.resting_bpm}'
class Body():
    def __init__(self,**kwargs):
        self.Heart = Heart(
            resting_bpm=kwargs.pop(
                'resting_bpm',
                80
                )
            )
        self.Stomach = Stomach(contents=kwargs.pop('contents',[]))
        self.energy = kwargs.pop('energy',0)
    def __str__(self):
        return 'This is a body'
    def meal(self,*args):
        for item in args:
            self.Stomach.contents.append(item)
    def exercise(self,*args):
        self.energy += self.Stomach.digest()
        self.energy += -1
        self.Heart.bpm += 10
        if self.energy <0:
            print('Hungry!')
        if self.Heart.bpm > 140:
            print('Overworked!')