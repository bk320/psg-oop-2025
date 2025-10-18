class cuenta_bancaria:
    def __init__ (self):
        self.titular = "Richard Power"
        self.__numero_cuenta = "12345"
        self.__saldo = 999.99

    @property
    def numero_cuenta(self):
        return self.__numero_cuenta
    @property
    def saldo(self):
        return self.__saldo
    
    def depositar(self, cantidad):
        try:
            self.__saldo += cantidad
            print(f"Depósito exitoso. Nuevo saldo: {self.__saldo}")
        except Exception as e:
            print(f"Error al depositar revise los valores: {e}")

    def retirar(self, cantidad):
        try:
            if 0 < cantidad <= self.__saldo:
                self.__saldo -= cantidad
                print(f"Retiro exitoso. Nuevo saldo: {self.__saldo}")
            else:
                print("Fondos insuficientes o cantidad inválida.")
        except Exception as e:
            print(f"Error al retirar revise los valores: {e}")

# Implementando la clase
cuenta1 = cuenta_bancaria()
print(f"Titular: {cuenta1.titular}")
print(f"Número de cuenta: {cuenta1.numero_cuenta}")
print(f"Saldo inicial: {cuenta1.saldo}")
cuenta1.depositar(500)
cuenta1.retirar(200.50)
cuenta1.retirar(5000)

cuenta1.__numero_cuenta = "999"
print(f"Número de cuenta después del intento de cambio: {cuenta1.numero_cuenta}")