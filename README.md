# Evaluación Práctica - Sistema de Servicio de Transporte

## Información General
* **Nombre del Equipo:** [Nombre de tu Equipo]
* **Integrantes:**
  * [Nombre Integrante 1]
  * [Nombre Integrante 2]
  * [Nombre Integrante 3]
* **Escenario Seleccionado:** Escenario C - Servicio de Transporte (Dificultad Avanzada)

---

## Breve Descripción de la Solución
Se ha desarrollado un prototipo funcional que permite simular la cotización y gestión de viajes en una plataforma de transporte. La solución incluye un módulo lógico en Python basado en Programación Orientada a Objetos (POO) y una interfaz gráfica interactiva construida en HTML, CSS y JavaScript para la estimación de tarifas.

---

## Explicación de Conceptos POO (Python)

### 1. Clase Padre y Clases Hijas
* **Clase Padre:** `ServicioTransporte`, la cual define los atributos comunes (`conductor`, `identificador`, `distancia`, `tarifa_base`) y los métodos base `calcular_tarifa()` y `mostrar_resumen()`.
* **Clases Hijas:**
  * `Motocicleta`: Hereda de `ServicioTransporte` y sobrescribe el cálculo utilizando un factor por kilómetro de **0.35**.
  * `Automovil`: Hereda de `ServicioTransporte` y sobrescribe el cálculo utilizando un factor por kilómetro de **0.60**.

### 2. Sobrescritura de Métodos y Polimorfismo
El método `calcular_tarifa()` se implementa de manera general en la clase padre y se **sobrescribe** en cada una de las clases hijas según sus propias reglas de negocio.

El **polimorfismo** se evidencia en `main.py`, donde almacenamos instancias de `Motocicleta` y `Automovil` dentro de una misma lista y las iteramos llamando al mismo método `mostrar_resumen()` (el cual ejecuta dinámicamente el método `calcular_tarifa()` específico de cada tipo de objeto sin necesidad de estructuras condicionales `if/else`).

---

## Rol de Frontend y Tecnologías Web

* **HTML (`index.html`):** Proporciona la estructura semántica de la página, incluyendo formularios para la captura de datos (tipo de servicio y distancia).
* **CSS (`styles.css`):** Define el diseño visual, asegurando una experiencia limpia y clara. Permite **diferenciar visualmente** los tipos de vehículo mediante clases dinámicas (verde/`servicio-moto` y azul/`servicio-auto`).
* **JavaScript (`script.js`):** Gestiona la interacción con el usuario en tiempo real, capturando las entradas del formulario, ejecutando la lógica de cálculo y manipulando el DOM para desplegar el resultado final.

---

## Responsabilidades Frontend vs Backend

* **Responsabilidades del Frontend:**
  * Renderizar la interfaz de usuario.
  * Recopilar las entradas del usuario (distancia, tipo de vehículo).
  * Realizar validaciones de formulario antes de enviar peticiones.
  * Presentar la información procesada visualmente de forma clara.

* **Responsabilidades del Backend:**
  * Almacenar de forma persistente datos de conductores, vehículos y viajes en bases de datos.
  * Ejecutar la lógica de negocios crítica y sensible (tarifas, comisiones, reglas dinámicas).
  * Autenticar a los usuarios y conductores.
  * Procesar cobros y pagos mediante pasarelas financieras.

---

## Requisito Adicional: Explicación Conceptual del Flujo Cliente-Servidor (+1 Punto)

A continuación se detalla el flujo de comunicación conceptual entre el cliente y el servidor en una aplicación real de transporte:

```text
[ Usuario ] ──> (1. Interacción) ──> [ Frontend ]
                                          │
                                   (2. Petición HTTP)
                                          ▼
                                     [ Backend ]
                                          │
                                   (3. Respuesta JSON)
                                          ▼
[ Usuario ] <── (4. Renderizado) <── [ Frontend ]