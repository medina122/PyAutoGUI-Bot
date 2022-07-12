import pyautogui as pg
import os, random, time
import colorama
from colorama import Fore

class PyAutoGUI_Bot():

    # Inicializamos Colorama para agregar colores a los print
    colorama.init()

    # Asignamos las variables que necesitaremos
    def __init__(self):
        self.cords = None
        self.conf = 0.7
        self.path = os.getcwd()
        self.tweens = [pg.easeInQuad,
            pg.easeOutQuad,
            pg.easeInOutQuad,
            pg.easeInCubic,
            pg.easeOutCubic,
            pg.easeInOutCubic,
            pg.easeInQuart,
            pg.easeOutQuart,
            pg.easeInOutQuart,
            pg.easeInQuint,
            pg.easeOutQuint,
            pg.easeInOutQuint,
            pg.easeInSine,
            pg.easeOutSine,
            pg.easeInOutSine,
            pg.easeInExpo,
            pg.easeOutExpo,
            pg.easeInOutExpo,
            pg.easeInCirc,
            pg.easeOutCirc,
            pg.easeInOutCirc,
            pg.easeInElastic,
            pg.easeOutElastic,
            pg.easeInOutElastic,
            pg.easeInBack,
            pg.easeOutBack,
            pg.easeInOutBack,
            pg.easeInBounce,
            pg.easeOutBounce,
            pg.easeInOutBounce]
        self.size = pg.size()

    # Ubicamos imagenes en pantalla y realizamos acciones en consecuencia
    def locate(self, name, check=False, wait=0, move=False, click=True, auto=True):
        
        # Inicio retardado si es diferente a 0
        if wait != 0: time.sleep(wait)
        
        # Establecemos la carpeta de los recursos, por defecto 
        path = os.path.join(self.path, 'src', name)+'.png'
        self.cords = pg.locateOnScreen(path, self.conf)
        count = 0
        
        # Si tenemos check buscara la imagen en bucle
        while not self.cords and check:
            count +=1
            time.sleep(1)
            print(f"{Fore.YELLOW}[...]{Fore.WHITE} Trying to locate {name}, attempt: {count}")
            self.cords = pg.locateOnScreen(path, self.conf) 

        # Si encuentra la imagen realizara las acciones que se le indique
        if self.cords != None:
            print(f"{Fore.GREEN}[+]{Fore.WHITE} Found {name} at {self.cords}")

            # Para simular comportamiento humano agregaremos lo siguiente:
            time.sleep(random.randint(1,5))
            if move: pg.moveTo(self.cords, duration=random.uniform(0.25, 0.4), tween=random.choice(self.tweens))
            if click: pg.click(self.cords, duration=random.uniform(0.25, 0.4), tween=random.choice(self.tweens))
            if auto: pg.moveTo(x=random.randint(0, self.size[0]), y=random.randint(0, self.size[1]), duration=random.uniform(0.25, 0.4), tween=random.choice(self.tweens))
            return True
        
        # Si no encuentra nada, retornara False
        else:
            print(f"{Fore.RED}[-]{Fore.WHITE} Not found {name}") 
            return False
    
    # Obtenemos la posicion de una imagen
    def get_position(self, name):
        path = os.path.join(self.path, 'src', name)+'.png'
        return pg.locateOnScreen(path, self.conf)
    