class Cuenta:
    def __init__ (self, titular, numero_cuenta, saldo):
        self.titular = titular
        self.__numero_cuenta = numero_cuenta
        self.__saldo = saldo

    @property
    def numero_cuenta(self):
        return self.__numero_cuenta
    @property
    def saldo(self):
        return self.__saldo
    
    def depositar(self, cantidad):
        try:
            if cantidad > 0:
                self.__saldo += cantidad
                print(f"Depósito exitoso. Nuevo saldo: {self.__saldo}")
            else:
                print("Cantidad inválida para depósito.")
        except Exception as e:
            print(f"Error al depositar revise los valores: {e}")

    def retirar(self, cantidad):
        try:
            if cantidad <= 0:
                print("Cantidad inválida para retiro.")           
            elif cantidad <= self.__saldo:
                self.__saldo -= cantidad
                print(f"Retiro exitoso. Nuevo saldo: {self.__saldo}")
            else:
                print("Fondos insuficientes")
        except Exception as e:
            print(f"Error al retirar revise los valores: {e}")


cuenta_bancaria = Cuenta("Richard Power", "12345", 999.99)
print(f"Titular: {cuenta_bancaria.titular}")
print(f"Numero de cuenta: {cuenta_bancaria.numero_cuenta}")
print(f"Saldo inicial: {cuenta_bancaria.saldo}\n")

cuenta_bancaria.depositar(500)
cuenta_bancaria.retirar(220)
cuenta_bancaria.retirar(5000)

cuenta_bancaria.__numero_cuenta = "999"
print(f"Numero de cuenta: {cuenta_bancaria.numero_cuenta}")