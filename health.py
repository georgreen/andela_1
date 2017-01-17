
class Viruse(object):
    """
    a simple class that models Viruse
    Input ->
    """
    def __init__(self, name = '', hostility = '', season = '', cureRable = None):
        self.name = name
        self.hostility = hostility
        self.season = season
        self.cureRable = cureRable

    def get_name(self):
        return self.name

    def get_season(self):
        return self.season

    def get_hostility(self):
        return self.hostility

    def get_cureRable(self):
        return self.cureRable


class cold_Viruse(Viruse):
    """ a simple class inherit's from Viruse
        Input -> Name
    """
    def __init__(self, name, season, cureRable = True):
        self.name = name
        self.season = season
        self.cureRable = cureRable

    Host = "Children"
    LifeSpan_in_Days = 15




class Flu_Viruses(Viruse):
    """ a simple class inherit from Viruse
    """
    def __init__(self, name, cureRable = False):
        self.name = name

    Host = "EveryBody"
    lifespan = None




class Patient(object):
    """
    A simple class modeling the host
    """
    def __init__(self, Age, name, capcity = "1000", infected = None):
        self.name = name
        self.Age = Age
        self.capcity = capcity
        self.infections = []
        self.num_of_viruses = 0

    def get_Viruses_hosted(self):
        return self.infections

    def take_meds(self, injection = 0, tablets = 0):
        if(injection == 0 and tablets == 0):
            self.num_of_viruses += 4
            print("getting Worse")
        else:
            if self.num_of_viruses > 4:
                self.num_of_viruses = self.num_of_viruses - 4
            else:
                print("You fine cured!")
            print("getting better")


    def get_infected(self, list_viruse):
        for viruse in list_viruse:
            self.infections.append(viruse)


class Doctor(object):
    """
    models a doctor
    """
    known_Viruse = {'Homa' : 'cold_Viruse', 'ring0' : 'Flu_Viruses', 'supperBug' : 'Flu_Viruses'}
    def __init__(self,skill_Level = 4):
        self.skill_Level = skill_Level

    def get_cure(self, list_Viruses):
        results = []
        for viruse in list_Viruses:
            results.append(Doctor.known_Viruse.get(Viruse))
        if len(results) > 2:
            return [ 4, 60]
        else:
            return [1, 5]

def Treament_process():
    careless_human = Patient(19, "Lovi", True)
    striking_doctors = Doctor(10)

    #infect patient with all Viruses
    careless_human.get_infected(['Homa', 'ring0', 'supperBug'])
    careless_human.num_of_viruses = 4


    #doesn't take medicine for some time population increase
    for i in range(0, 30):
        careless_human.take_meds()

    #goes to hos[ital doctor can't identify exact viruses, but all viruses are viruses!
    meds = striking_doctors.get_cure(careless_human.get_Viruses_hosted())

    #hope he gets better
    for i in range(meds[1]):
        #given some general medicine
        careless_human.take_meds(meds[0], meds[1])
        if(careless_human.num_of_viruses <= 4):
            print("cured")

if __name__ == '__main__':
    Treament_process()
