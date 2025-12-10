# Restaurante

Un restaurante quiere ofrecer hamburguesas
Los clientes pueden elegir entre hamburguesa de: res, pollo o vegetariana.
Los clientes pueden agregar extras como: lechuga, tomate, cebolla y mayonesa
Ademas los clientes pueden decidir comer en el restaurante o llevar su pedido

## Análisis

Requisitos:

- La hamburguesa debe regstrar su tipo de carne: res, pollo o vegetariana
- La hamburguesa debe permitir agregar o no, extra de lechuga
- La hamburguesa debe permitir agregar o no, extra de tomate
- La hamburguesa debe permitir agregar o no, extra de cebolla
- La hamburguesa debe permitir agregar o no, extra de mayonesa
- La hamburguesa debe registrar si es para comer en el restaurante o para llevar.

Objetos:

- Hamburguesa

Caracteristicas:

- Hamburguesa
  - tipo_hamburguesa
  - lechuga
  - tomate
  - cebolla
  - mayonesa
  - para_llevar

Acciones:

- (No hay acciones)

## Diseño

Clases:

- Hamburguesa:
  - Nombre: Hamburguesa
  - Atributos:
    - tipo_hamburguesa
    - lechuga
    - tomate
    - cebolla
    - mayonesa
    - para_llevar
  - Metodos:
    - (no hay métodos)

```mermaid
classDiagram
    class Hamburguesa {
        tipo_hamburguesa
        lechuga
        tomate
        cebolla
        mayonesa
        para_llevar
    }
```
