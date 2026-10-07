class ServicioTransporte:
    def __init__(self, conductor: str, identificador: str, distancia: float, tarifa_base: float):
        self.conductor = conductor
        self.identificador = identificador  # Placa o ID del vehículo
        self.distancia = distancia
        self.tarifa_base = tarifa_base

    def calcular_tarifa(self) -> float:
        """Método base a ser sobrescrito en las clases hijas."""
        return self.tarifa_base

    def mostrar_resumen(self) -> str:
        """Devuelve una descripción con la información general del servicio."""
        return (f"Conductor: {self.conductor} | Vehículo ID: {self.identificador} | "
                f"Distancia: {self.distancia:.2f} km | Tarifa Total: ${self.calcular_tarifa():.2f}")


class Motocicleta(ServicioTransporte):
    def calcular_tarifa(self) -> float:
        # Motocicleta: tarifa base + distancia * 0.35
        return self.tarifa_base + (self.distancia * 0.35)

    def mostrar_resumen(self) -> str:
        resumen_base = super().mostrar_resumen()
        return f"[MOTOCICLETA] {resumen_base}"


class Automovil(ServicioTransporte):
    def calcular_tarifa(self) -> float:
        # Automóvil: tarifa base + distancia * 0.60
        return self.tarifa_base + (self.distancia * 0.60)

    def mostrar_resumen(self) -> str:
        resumen_base = super().mostrar_resumen()
        return f"[AUTOMÓVIL] {resumen_base}"