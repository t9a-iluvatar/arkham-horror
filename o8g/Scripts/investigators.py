investigators = {}

def get_investigator(name):
    if not name in investigators:
        investigator = Investigator(name)
    return investigators[name]


class Investigator:
    def __init__(self, name):
        self.name = name
        investigators[name] = self
    

sefina_rousseau = Investigator('Sefina Rousseau')
sefina_rousseau.openingHandSize = 10
