from pygame import *
import pygame
from pygame.locals import *

surfaceW = 720  # Dimension de la fenêtre / Largeur
surfaceH = 500  # Dimension de la fenêtre / Longueur

pygame.init()
demarrage = pygame.mixer.Sound("Sounds_effect/Opening_Theme.ogg")
demarrage.play()

class Menu:
    """ Création et gestion des boutons d'un menu """

    def __init__(self, application, *groupes):
        self.couleurs = dict( normal='red',survol='white')
        font = pygame.font.SysFont('Helvetica', 24, bold=True)
        # noms des menus et commandes associées
        items = (
            ('START', application.jeu),
            ('QUIT', application.quitter),('CREDIT', application.credit)
        )
        x = surfaceW/2
        y = 200
        self._boutons = []
        for texte, cmd in items:
            mb = MenuBouton(
                texte,
                self.couleurs['normal'],
                font,
                x,
                y,
                200,
                50,
                cmd
            )
            self._boutons.append(mb)
            y += 120
            for groupe in groupes:
                groupe.add(mb)

    def update(self, events):
        clicGauche, *_ = pygame.mouse.get_pressed()
        posPointeur = pygame.mouse.get_pos()
        for bouton in self._boutons:
            # Si le pointeur souris est au-dessus d'un bouton
            if bouton.rect.collidepoint(*posPointeur):
                # Changement du curseur par un quelconque
                pygame.mouse.set_cursor(*pygame.cursors.tri_left)
                # Changement de la couleur du bouton
                bouton.dessiner(self.couleurs['survol'])
                # Si le clic gauche a été pressé
                if clicGauche:
                    # Appel de la fonction du bouton
                    bouton.executerCommande()
                break
            else:
                # Le pointeur n'est pas au-dessus du bouton
                bouton.dessiner(self.couleurs['normal'])
        else:
            # Le pointeur n'est pas au-dessus d'un des boutons
            # initialisation au pointeur par défaut
            pygame.mouse.set_cursor(*pygame.cursors.arrow)

    def detruire(self):
        pygame.mouse.set_cursor(*pygame.cursors.arrow)  # initialisation du pointeur


class MenuBouton(pygame.sprite.Sprite):
    """ Création d'un simple bouton rectangulaire """

    def __init__(self, texte, couleur, font, x, y, largeur, hauteur, commande):
        super().__init__()
        self._commande = commande

        self.image = pygame.Surface((largeur, hauteur))

        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

        self.texte = font.render(texte, True, (0, 0, 0))
        self.rectTexte = self.texte.get_rect()
        self.rectTexte.center = (largeur / 2, hauteur / 2)

        self.dessiner(couleur)

    def dessiner(self, couleur):
        self.image.fill(couleur)
        self.image.blit(self.texte, self.rectTexte)

    def executerCommande(self):
        # Appel de la commande du bouton
        self._commande()


class Jeu:
    """ Simulacre de l'interface du jeu """

    def __init__(self, jeu, *groupes):
        self._fenetre = jeu.fenetre
        jeu.fond = (0, 0, 0)

        from itertools import cycle
        couleurs = [(0, 48, i) for i in range(0, 256, 15)]
        couleurs.extend(sorted(couleurs[1:-1], reverse=True))
        self._couleurTexte = cycle(couleurs)

        self._font = pygame.font.SysFont('Helvetica', 36, bold=True)
        self.creerTexte()
        self.rectTexte = self.texte.get_rect()
        self.rectTexte.center = (surfaceW / 2, surfaceH / 2)
        # Création d'un event
        self._CLIGNOTER = pygame.USEREVENT + 1
        pygame.time.set_timer(self._CLIGNOTER, 80)

        demarrage.stop()
        from jeu import setup_game


    def creerTexte(self):
        self.fenetre = pygame.display.set_mode((surfaceW, surfaceH))
        self.fond = (150,) * 3
        self.fenetre.fill(self.fond)
        self.texte = self._font.render(
            'LANCEMENT DE JEUX',
            True,
            next(self._couleurTexte)
        )
        
    def update(self, events):
        self._fenetre.blit(self.texte, self.rectTexte)
        for event in events:
            if event.type == self._CLIGNOTER:
                self.creerTexte()
                break

    def detruire(self):
        pygame.time.set_timer(self._CLIGNOTER, 0)  # désactivation du timer

class credit:
    """Credit"""
    def __init__(self, credit, *groupes):
        pygame.init()
        pygame.display.set_caption("CREDIT")
        self.fenetre = pygame.display.set_mode((surfaceW, surfaceH))

        #self.fenetre.blit(back, (0, 0))
        self._fenetre = credit.fenetre
        back = pygame.image.load("image_credits.jpg").convert()
        width = surfaceW
        height = surfaceH

        for i in range(255, 0, -4):
            self.fenetre.blit(back, (0, 0))  # le coin en haut à gauche est de coordonnées (0,0)
            self.fenetre.fill((i, i, i), special_flags=BLEND_RGB_SUB)
            #display.flip()

        self.textCredit()
        self.rectTexte = self.texte.get_rect()
        self.rectTexte.center = (surfaceW / 2, surfaceH / 2)
        # Création d'un event
        self._CLIGNOTER = pygame.USEREVENT + 1


    def textCredit(self):

        self._font = pygame.font.SysFont('Helvetica', 50)
        self.texte = self._font.render('Créer par LES MARMOTTES ', True, 'white')
        demarrage.stop()
        credit_sound = pygame.mixer.Sound("Sounds_effect/La_Cucaracha.ogg")
        credit_sound.play()


    def update(self, events):
        self._fenetre.blit(self.texte, self.rectTexte)
        for event in events:
            if event.type == self._CLIGNOTER:
                self.textCredit()
                break

    def detruire(self):
        pygame.time.set_timer(self._CLIGNOTER, 0)  # désactivation du timer


class Application:
    """ Classe maîtresse gérant les différentes interfaces du jeu """

    def __init__(self):
        pygame.init()
        pygame.display.set_caption("PONG GAME")

        #self.fond = (150,) * 3

        self.fenetre = pygame.display.set_mode((surfaceW, surfaceH))
        back = pygame.image.load("image_start.jpg").convert()
        width = surfaceW
        height = surfaceH
        for i in range(255, 0, -4):
            self.fenetre.blit(back, (0, 0))  # le coin en haut à gauche est de coordonnées (0,0)
            self.fenetre.fill((i, i, i), special_flags=BLEND_RGB_SUB)
            #time.wait(20)
            #display.flip()
        BLANC = 255, 255, 255
        # Groupe de sprites utilisé pour l'affichage
        self.groupeGlobal = pygame.sprite.Group()
        self.statut = True

    def _initialiser(self):
        try:
            self.ecran.detruire()
            # Suppression de tous les sprites du groupe
            self.groupeGlobal.empty()
        except AttributeError:
            pass

    def menu(self):
        # Affichage du menu
        self._initialiser()
        self.ecran = Menu(self, self.groupeGlobal)

    def jeu(self):
        # Affichage du jeu
        self._initialiser()
        self.ecran = Jeu(self, self.groupeGlobal)
    

    def quitter(self):
        self.statut = False

    def update(self):
        events = pygame.event.get()

        for event in events:
            if event.type == pygame.QUIT:
                self.quitter()
                return

        self.ecran.update(events)
        self.groupeGlobal.update()
        self.groupeGlobal.draw(self.fenetre)
        pygame.display.update()

    def credit(self):
            # Affichage du jeu
        self._initialiser()
        self.ecran = credit(self, self.groupeGlobal)


app = Application()
app.menu()

clock = pygame.time.Clock()

while app.statut:
    app.update()
    clock.tick(30)

pygame.quit()