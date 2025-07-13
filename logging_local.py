import sys
import datetime

class Logger:
    def __init__(self, nombre="AriaLogger", nivel="INFO"):
        self.nombre = nombre
        self.nivel = nivel
        self.niveles = {"DEBUG": 10, "INFO": 20, "WARNING": 30, "ERROR": 40, "CRITICAL": 50}

    def _debe_loggear(self, nivel):
        return self.niveles.get(nivel, 100) >= self.niveles.get(self.nivel, 100)

    def _formatear_mensaje(self, nivel, mensaje):
        tiempo = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return f"{tiempo} - {self.nombre} - {nivel} - {mensaje}"

    def debug(self, mensaje):
        if self._debe_loggear("DEBUG"):
            print(self._formatear_mensaje("DEBUG", mensaje), file=sys.stdout)

    def info(self, mensaje):
        if self._debe_loggear("INFO"):
            print(self._formatear_mensaje("INFO", mensaje), file=sys.stdout)

    def warning(self, mensaje):
        if self._debe_loggear("WARNING"):
            print(self._formatear_mensaje("WARNING", mensaje), file=sys.stderr)

    def error(self, mensaje):
        if self._debe_loggear("ERROR"):
            print(self._formatear_mensaje("ERROR", mensaje), file=sys.stderr)

    def critical(self, mensaje):
        if self._debe_loggear("CRITICAL"):
            print(self._formatear_mensaje("CRITICAL", mensaje), file=sys.stderr)

# Instancia global para uso sencillo
logger = Logger()
