class Chainon(object):
    def __init__(self, v=None,s=None):
        self.val=v
        self.suiv=s

    def __str__(self):
        if self.val is None:
            return str(self.val)
        else :
            return str(self.val)+'--'+str(self.suiv)

class Liste_chainee(object):
    def __init__(self):
        self.tete=None

    def ajouter_debut(self,element):
        self.tete=Chainon(element,self.tete)

    def __str__(self):
        return str(self.tete)

    def est_vide(self):
        if self.tete is None:
            return True
        return False

    def ajouter_fin(self,element):
        C=Chainon(element)
        if self.est_vide():
            self.tete=C
        else :
            Cur=self.tete
            while Cur.suiv is not None:
                Cur=Cur.suiv
            Cur.suiv=C

    def Supprimer_tete(self):
        if self.tete.val == None :
            raise IndexError("Les valeurs sont vides")
        else :
            self.tete=self.tete.suiv

    def Supprimer_queue(self):
        if self.est_vide():
            raise IndexError("la liste est vide")
        Cur=self.tete
        a=None
        while Cur.suiv is not None :
            a=Cur
            Cur=Cur.suiv
        a.Suiv=None

    def taille(self):
        taille=1
        Cur=self.tete
        if self.est_vide():
            return 0
        while Cur.suiv is not None :
            Cur=Cur.suiv
            taille += 1

        return taille

    def get_dernier_chainon(self):
        if self.est_vide():
            return None
        else :
            Cur=self.tete
            while Cur.suiv is not None :
                Cur=Cur.suiv
        return Cur.val


    def get_chainon_indice(self,i):
        if self.taille()<+1:
            raise IndexError("la liste n'a pas d'élèments d'indice i")
        j=0
        Cur=self.tete
        while j<i:
            Cur=Cur.suiv
            j=j+1
        return Cur.val

    def inserer_indice(self,i,elt):
        element=Chainon(elt)
        if self.taille()<+1:
            raise IndexError("la liste est trop petite")
        if i == 0 :
            self.ajouter_debut(element)
        else :
            j=0
            Cur=self.tete
            while j<i:
                Cur=Cur.suiv
                j=j+1
            element.suiv=Cur.suiv
            Cur.suiv = element


    def supprimer_indice(self,i):
        if self.taille()<+1:
            raise IndexError("la liste est trop petite")
        if i==0:
            self.tete=self.tete.suiv
        else :
            j=0
            Cur=self.tete
            while j<i-1:
                j=j+1
            Cur.suiv=Cur.suiv.suiv

    def concatener(self,L):
        if self.est_vide():
            self.tete=L.tete
            return self
        if L.est_vide():
            return self
        Cur=self.tete
        while Cur.suiv is not None :
            Cur=Cur.suiv
        Cur.suiv=L.tete
        return self







liste=Liste_chainee()
liste.ajouter_debut(3)
liste.ajouter_debut(2)
liste.ajouter_debut(1)

##t=liste.taille()
##print(t)

ch=liste.get_dernier_chainon()
print(ch)

print(liste)

