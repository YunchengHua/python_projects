class Hero:
    def __init__(self,name,level,health_points,Q_hurt,W_hurt,E_hurt):
        self._name = name
        self._level = level
        self._health_points = health_points
        self._Q_hurt = Q_hurt
        self._W_hurt = W_hurt
        self._E_hurt = E_hurt

    def get_name(self):
        return self._name

    def Q_attack(self,enemy):
        print('%s Q %s'%(self.get_name(),enemy.get_name()))
        enemy.attack(self._Q_hurt)

    def W_attack(self, enemy):
        print('%s W %s' % (self.get_name(), enemy.get_name()))
        enemy.attack(self._W_hurt)

    def E_attack(self, enemy):
        print('%s E %s' % (self.get_name(), enemy.get_name()))
        enemy.attack(self._E_hurt)

    def attack(self,attack_points):
        self._health_points -= attack_points
        if self._health_points > 0:
            print('%s life : %d %%'%(self.get_name(),self._health_points))
        else:
            print('%s died.'% self.get_name())


if __name__ =='__main__':
    hero0 = Hero('hero0', 10, 100, 15,2,35)
    hero1 = Hero('hero1',1, 25, 15, 12, 12)
    hero0.Q_attack(hero1)
    hero0.W_attack(hero1)
    hero0.E_attack(hero1)