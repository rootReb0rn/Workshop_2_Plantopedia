from experta import *

class Symptom(Fact):
    """
        Plants Fact
    """
    pass

class Lemon(KnowledgeEngine):
    """
        Lemon Inference Engine 
    """
    @Rule(
        Symptom(ques1='no'),
        Symptom(ques2='no'),
        Symptom(ques3='no'),
        Symptom(ques4='yes'),
        Symptom(ques5='yes'),
        Symptom(ques6='no'),
        Symptom(ques7='no'),
        Symptom(ques8='no'),
        Symptom(ques9='no'),
        Symptom(ques10='no')
        )
    def disease01(self):
        self.declare(Symptom(disease='Citrus Canker'))

    @Rule(
        Symptom(ques1='no'),
        Symptom(ques2='no'),
        Symptom(ques3='no'),
        Symptom(ques4='no'),
        Symptom(ques5='no'),
        Symptom(ques6='no'),
        Symptom(ques7='no'),
        Symptom(ques8='yes'),
        Symptom(ques9='yes'),
        Symptom(ques10='yes')
        )
    def disease02(self):
        self.declare(Symptom(disease='Citrus Leaf Miner'))

    @Rule(
        Symptom(ques1='yes'),
        Symptom(ques2='yes'),
        Symptom(ques3='yes'),
        Symptom(ques4='no'),
        Symptom(ques5='no'),
        Symptom(ques6='no'),
        Symptom(ques7='no'),
        Symptom(ques8='no'),
        Symptom(ques9='no'),
        Symptom(ques10='no')
        )
    def disease03(self):
        self.declare(Symptom(disease='Lemon Anthracnose'))

    @Rule(
        Symptom(ques1='yes'),
        Symptom(ques2='no'),
        Symptom(ques3='no'),
        Symptom(ques4='no'),
        Symptom(ques5='no'),
        Symptom(ques6='yes'),
        Symptom(ques7='yes'),
        Symptom(ques8='no'),
        Symptom(ques9='no'),
        Symptom(ques10='no')
        )
    def disease04(self):
        self.declare(Symptom(disease='Lemon Huanglongbing'))

    @Rule(Symptom(disease='Citrus Canker'))
    def findDisease01(self):
        self.response = 'Citrus Canker'

    @Rule(Symptom(disease='Citrus Leaf Miner'))
    def findDisease02(self):
        self.response = 'Citrus Leaf Miner'

    @Rule(Symptom(disease='Lemon Anthracnose'))
    def findDisease03(self):
        self.response = 'Lemon Anthracnose'

    @Rule(Symptom(disease='Lemon Huanglongbing'))
    def findDisease04(self):
        self.response = 'Lemon Huanglongbing'    

    @Rule(NOT(Symptom(disease = W())))
    def findDisease05(self):
        self.response = 'No Disease Found [Lemon]'


class Mango(KnowledgeEngine):
    """
        Mango Inference Engine 
    """
    @Rule(
        Symptom(ques1='yes'),
        Symptom(ques2='yes'),
        Symptom(ques3='no'),
        Symptom(ques4='no'),
        Symptom(ques5='no'),
        Symptom(ques6='no'),
        Symptom(ques7='no'),
        Symptom(ques8='no')
        )
    def disease01(self):
        self.declare(Symptom(disease='Algal Leaf Spot'))

    @Rule(
        Symptom(ques1='no'),
        Symptom(ques2='no'),
        Symptom(ques3='no'),
        Symptom(ques4='no'),
        Symptom(ques5='no'),
        Symptom(ques6='no'),
        Symptom(ques7='yes'),
        Symptom(ques8='yes')
        )
    def disease02(self):
        self.declare(Symptom(disease='Phoma Blight'))

    @Rule(
        Symptom(ques1='no'),
        Symptom(ques2='no'),
        Symptom(ques3='yes'),
        Symptom(ques4='yes'),
        Symptom(ques5='no'),
        Symptom(ques6='no'),
        Symptom(ques7='no'),
        Symptom(ques8='no')
        )
    def disease03(self):
        self.declare(Symptom(disease='Powdery Mildew'))

    @Rule(
        Symptom(ques1='no'),
        Symptom(ques2='no'),
        Symptom(ques3='no'),
        Symptom(ques4='no'),
        Symptom(ques5='yes'),
        Symptom(ques6='yes'),
        Symptom(ques7='no'),
        Symptom(ques8='no')
        )
    def disease04(self):
        self.declare(Symptom(disease='Sooty Mold'))

    @Rule(Symptom(disease='Algal Leaf Spot'))
    def findDisease01(self):
        self.response = 'Algal Leaf Spot'

    @Rule(Symptom(disease='Phoma Blight'))
    def findDisease02(self):
        self.response = 'Phoma Blight'

    @Rule(Symptom(disease='Powdery Mildew'))
    def findDisease03(self):
        self.response = 'Powdery Mildew'

    @Rule(Symptom(disease='Sooty Mold'))
    def findDisease04(self):
        self.response = 'Sooty Mold'    

    @Rule(NOT(Symptom(disease = W())))
    def findDisease05(self):
        self.response = 'No Disease Found [Mango]'

class Noni(KnowledgeEngine):
    """
        Noni Inference Engine
    """
    @Rule(
        Symptom(ques1='no'),
        Symptom(ques2='no'),
        Symptom(ques3='no'),
        Symptom(ques4='yes'),
        Symptom(ques5='yes'),
        Symptom(ques6='no'),
        Symptom(ques7='no'),
        Symptom(ques8='no'),
        Symptom(ques9='no'),
        Symptom(ques10='no'),
        Symptom(ques11='no')
        )
    def disease01(self):
        self.declare(Symptom(disease='Algal Leaf Spot'))

    @Rule(
        Symptom(ques1='no'),
        Symptom(ques2='no'),
        Symptom(ques3='no'),
        Symptom(ques4='no'),
        Symptom(ques5='no'),
        Symptom(ques6='no'),
        Symptom(ques7='no'),
        Symptom(ques8='no'),
        Symptom(ques9='yes'),
        Symptom(ques10='yes'),
        Symptom(ques11='yes')
        )
    def disease02(self):
        self.declare(Symptom(disease='Heliothrips Haemorrhoidalis'))

    @Rule(
        Symptom(ques1='no'),
        Symptom(ques2='no'),
        Symptom(ques3='no'),
        Symptom(ques4='no'),
        Symptom(ques5='no'),
        Symptom(ques6='yes'),
        Symptom(ques7='yes'),
        Symptom(ques8='yes'),
        Symptom(ques9='no'),
        Symptom(ques10='no'),
        Symptom(ques11='no')
        )
    def disease03(self):
        self.declare(Symptom(disease='Noni Anthracnose'))

    @Rule(
        Symptom(ques1='yes'),
        Symptom(ques2='yes'),
        Symptom(ques3='yes'),
        Symptom(ques4='no'),
        Symptom(ques5='no'),
        Symptom(ques6='no'),
        Symptom(ques7='no'),
        Symptom(ques8='no'),
        Symptom(ques9='no'),
        Symptom(ques10='no'),
        Symptom(ques11='no')
        )
    def disease04(self):
        self.declare(Symptom(disease='Noni Black Flag'))

    @Rule(Symptom(disease='Algal Leaf Spot'))
    def findDisease01(self):
        self.response = 'Algal Leaf Spot'

    @Rule(Symptom(disease='Heliothrips Haemorrhoidalis'))
    def findDisease02(self):
        self.response = 'Heliothrips Haemorrhoidalis'

    @Rule(Symptom(disease='Noni Anthracnose'))
    def findDisease03(self):
        self.response = 'Noni Anthracnose'

    @Rule(Symptom(disease='Noni Black Flag'))
    def findDisease04(self):
        self.response = 'Noni Black Flag'    

    @Rule(NOT(Symptom(disease = W())))
    def findDisease05(self):
        self.response = 'No Disease Found [Noni]'


plant_Lemon = Lemon()
plant_Mango = Mango()
plant_Noni = Noni()
