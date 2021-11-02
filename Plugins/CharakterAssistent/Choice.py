from Wolke import Wolke


class Choice(object):
    def __init__(self):
        super().__init__()
        self.name = ""
        self.wert = 0
        self.typ = "Fertigkeit"
        self.kommentar = ""

    def toString(self):
        valueStr = ""
        prefix = ""
        if self.typ == "Attribut":
            valueStr = " +" + str(self.wert) if self.wert >= 0 else " " + str(self.wert)
        elif self.typ == "Fertigkeit":
            valueStr = " +" + str(self.wert) if self.wert >= 0 else " " + str(self.wert)
            current = Wolke.Char.fertigkeiten[self.name].wert
            valueStr += " (aktuell +" + str(current) + ")"
        elif self.typ == "Freie-Fertigkeit":
            if self.wert == 1:
                valueStr = " (+) I"
            elif self.wert == 2:
                valueStr = " (+) II"
            elif self.wert == 3:
                valueStr = " III"
            else:
                return None
        elif self.typ == "Übernatürliche-Fertigkeit":
            valueStr = " +" + str(self.wert) if self.wert >= 0 else " " + str(self.wert)
            current = Wolke.Char.übernatürlicheFertigkeiten[self.name].wert
            valueStr += " (aktuell +" + str(current) + ")"
        else:
            prefix = self.typ + " "
        return prefix + self.name + valueStr


class ChoiceList(object):
    def __init__(self):
        super().__init__()
        self.name = ""
        self.beschreibung = None
        self.varianten = None
        self.keineVarianten = None
        self.geschlecht = None
        self.choices = []

    def hasVarianten(self):
        return self.varianten and len(self.varianten) > 0

    def meetsConditions(self, geschlecht, variantsSelected):
        if self.geschlecht and self.geschlecht != geschlecht:
            return False

        if self.keineVarianten:
            for index in variantsSelected:
                if index in self.keineVarianten:
                    return False

        if self.varianten:
            return any(index in self.varianten for index in variantsSelected)
        return True

    def doVariantenIntersect(self, other):
        if not self.varianten or not other.varianten:
            return False

        return any(index in other.varianten for index in self.varianten)

    def filter(self, choice):
        self.choices = [
            c for c in self.choices if c.name != choice.name or c.typ != choice.typ
        ]


class ChoiceListCollection(object):
    def __init__(self):
        super().__init__()
        self.chooseOne = True
        self.choiceLists = []

    def filter(self, startIndex, choice):
        # Remove choice further down the choices list
        choiceList = self.choiceLists[startIndex]
        if startIndex + 1 == len(self.choiceLists):
            return
        for i in range(startIndex + 1, len(self.choiceLists)):
            cl = self.choiceLists[i]
            if (
                not choiceList.hasVarianten() and not cl.hasVarianten()
            ) or choiceList.doVariantenIntersect(cl):
                cl.filter(choice)
