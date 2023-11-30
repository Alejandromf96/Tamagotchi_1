import random

class Tamagotchi():
    def __init__(self, nombre):
        self.nombre = nombre
        self.energia = 100
        self.hambre = 30
        self.felicidad = 70
        self.vivo = True
        
    def jugar(self):
        if self.energia <= 20:
            print(f"{self.nombre} no tiene energia para jugar")
        else:
            diversion = random.randint(0, 10)
            self.energia -= diversion
            self.hambre -= diversion
            self.felicidad += diversion
            print(f"{self.nombre} se divirtio jugando")
            
    def mostrar_estado(self):
        print(f"Nombre del tamagotchi: {self.nombre}")
        print(f"Energia: {self.energia}")
        print(f"Hambre: {self.hambre}")
        print(f"Felicidad: {self.felicidad}")
        print(f"Vivo: {self.vivo}")
            
    def comer(self):
        if self.hambre > 20:
            print(f"{self.nombre} no tiene hambre para comer")
        else:
            comida = random.randint(0, 15)
            self.hambre -= comida
            self.energia += comida
            print(f"{self.nombre} ha comido y se siente mejor")
            
    def dormir(self):
        if self.energia >= 50:
            print(f"{self.nombre} no necesita dormir")
        else:
            self.energia += 20
            print(f"{self.nombre} descanso y se siente mejor")
            
    def envejecer(self):
        self.hambre += random.randint(0, 15)
        self.felicidad -= random.randint(0, 15)
        self.energia -= random.randint(0, 15)
        print(f"{self.nombre} ha envejecido")
        if self.energia == 0:
            self.vivo = False
            print(f"{self.nombre} ha muerto")
            
    def saludar(self):
        if self.felicidad >= 30:
            print(f"{self.nombre} te saluda")
        else:
            print(f"{self.nombre} no quiere hablarte")
            
def main():
    nombre = input("El nombre de tu tamagotchi es: ")
    mi_tamagotchi = Tamagotchi(nombre)
    
    while mi_tamagotchi.vivo:
        mi_tamagotchi.mostrar_estado()
        print("\nQue deseas hacer")
        print("1. Comer")
        print("2. Jugar")
        print("3. Dormir")
        print("4. Envejecer")
        print("5. Saludar")
        print("6. Salir")
        opcion = input("\nElija una opcion: ")
        
        if opcion == "1":
            mi_tamagotchi.comer()
        elif opcion == "2":
            mi_tamagotchi.jugar()
        elif opcion == "3":
            mi_tamagotchi.dormir()
        elif opcion == "4":
            mi_tamagotchi.envejecer()
        elif opcion == "5":
            mi_tamagotchi.saludar()
        elif opcion == "6":
            break
        else:
            print("Opcion no valida, intentelo nuevamente")
        
    print("Gracias por jugar")
    
if __name__ == "__main__":
    main()