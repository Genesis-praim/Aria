import sys as _sys

def stdout_write(message):
    """Escribe un mensaje en la salida estándar."""
    _sys.stdout.write(message + '\\n')
    _sys.stdout.flush()

def stderr_write(message):
    """Escribe un mensaje en la salida de error estándar."""
    _sys.stderr.write(message + '\\n')
    _sys.stderr.flush()

def exit(code=0):
    """Termina el programa con el código de salida dado."""
    _sys.exit(code)
