def calculate_green_time(vehicle_count, K=2, Tmin=10, Tmax=60):
    time = K * vehicle_count
    return max(Tmin, min(time, Tmax))


def decision(vehicle_count):
    if vehicle_count == 0:
        return "EMPTY"
    elif vehicle_count < 10:
        return "NORMAL"
    else:
        return "HEAVY"