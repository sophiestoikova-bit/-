import random

EVENTS = [
    ("Микрометеорит пробил обшивку",    -15, 0.4),
    ("Солнечная вспышка: радиация",     -10, 0.2),
    ("Удачная коррекция курса",          +5, 0.2),
    ("Найдены запасы предыдущей миссии",+20, 0.1),
    ("Отказ системы охлаждения",        -25, 0.1),
]

def random_event(seed=None):
    """(описание, изменение ресурса) - случайное событие с весами."""
    rnd = random.Random(seed)
    names, weight = [e[0] for e in EVENTS], [e[2] for e in EVENTS]

    ...

import math
GO = 9.80665

def delta_v(m0, m1, isp=300):
    """Формула Циолковского, м/с."""
    if m1 <= 0 or m0 < m1:
        raise ValueError("Требуется m0 >= m1 > 0")
    return isp * GO * math.log(m0 / m1)

def flight_time(distance_km, accel):
    """Время перелета в часах: разгон на полпути + торможение."""

    ...

def fuel_needed(m_dry, target_dv, isp=300):
    """Масса топлива для заданного dv (обратная формула Циольского)."""

    ...
