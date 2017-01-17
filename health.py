
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

class Docter(object):
    """
    models a doctor
    """
    Known_Viruse = {}
    def __init__(self,skill_Level = 4):
        self.skill_Level = skill_Level

    def get_cure(self, list_Viruses):
        results = []
        for viruse in list_Viruses:
            results.append(Known_Viruse.get(Viruse))
        return results

def Treament_process():
    pass
    #infect patient with all Viruses

    #doesn't take medicine for some time population increase

    #goes to hos[ital doctor can't identify exact viruses, but all viruses are viruses!

    #given some general medicine

    #hope he gets better

    #Exit
