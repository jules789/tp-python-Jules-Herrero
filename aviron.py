class Bateau:
    def __init__(self, nom, vitesse_moyenne):
        self.nom = nom
        self.vitesse_moyenne = vitesse_moyenne
        self.distance_parcourue = 0

    def avancer(self):
        self.distance_parcourue += self.vitesse_moyenne

    def get_nom(self):
        return self.nom

    def get_distance_parcourue(self):
        return self.distance_parcourue


class Course:
    def __init__(self, type_bateau):
        self.bateaux = []
        self.type_bateau = type_bateau
        self.distance_course = 2000  # 2 km
        self.en_cours_course = False

    def ajout_bateau_ligne_depart(self, bateau):
        if isinstance(bateau, Bateau) and (
                self.type_bateau == '2x' or
                (self.type_bateau == '2-' and isinstance(bateau, Bateau)) or
                (self.type_bateau == 'skiff' and isinstance(bateau, Bateau))
        ):
            self.bateaux.append(bateau)
        else:
            print("Le bateau n'a pas pu être ajouté.")

    def depart(self):
        self.en_cours_course = True

    def en_cours(self):
        return self.en_cours_course

    def next_loop(self):
        for bateau in self.bateaux:
            bateau.avancer()
            if bateau.get_distance_parcourue() >= self.distance_course:
                self.en_cours_course = False

    def affiche_positions(self):
        return '\n'.join([f"{bateau.get_nom()},{bateau.get_distance_parcourue()}" for bateau in self.bateaux])

    def vainqueur(self):
        if not self.bateaux:
            return "Pas de bateaux en course."

        fastest_bateau = max(self.bateaux, key=lambda x: x.get_distance_parcourue())
        return fastest_bateau.get_nom()


bateau_1 = Bateau('Jules', 70)
bateau_2 = Bateau('Blabla', 80)
bateau_3 = Bateau('Blablabla', 110)

course_cadets = Course('2x')
course_cadets.ajout_bateau_ligne_depart(bateau_1)
course_cadets.ajout_bateau_ligne_depart(bateau_2)
course_cadets.ajout_bateau_ligne_depart(bateau_3)

course_cadets.depart()
while course_cadets.en_cours():
    course_cadets.next_loop()

print(course_cadets.affiche_positions())
print("Le vainqueur est :", course_cadets.vainqueur())
