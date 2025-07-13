import datetime as _datetime

def now():
    """Devuelve la fecha y hora actual."""
    return _datetime.datetime.now()

def today():
    """Devuelve la fecha actual sin la hora."""
    return _datetime.date.today()

def format_datetime(dt, formato="%Y-%m-%d %H:%M:%S"):
    """Formatea un objeto datetime según el formato dado."""
    return dt.strftime(formato)
