def get_speed(dist, urg):
    base = 50
    t_factor = urg * 3
    f_factor = max(10 - urg, 1) * 2
    e_factor = max(10 - urg, 1) * 1.5

    spd = base + t_factor - (f_factor + e_factor)/2
    spd = max(30, min(120, spd))

    time = dist / spd
    fuel = 100 - (spd - 50) * 0.5
    emission = 100 - (spd - 50) * 0.4

    return {
        "speed": round(spd, 1),
        "time": round(time, 2),
        "fuel": round(fuel, 1),
        "emission": round(emission, 1)
    }