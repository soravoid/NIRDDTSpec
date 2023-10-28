import math


SENSOR_INTENSITY: int = 1500 # microwatts/cm^2
CENTERS: list[int] = [610, 680, 730, 760, 810, 860]
STD_DEV: float = 20/(2*math.sqrt(2*math.log(2)))

def make_gaussian(center: float):
    return lambda x: math.exp(-(x - center)**2 / (2*STD_DEV**2))/(STD_DEV*math.sqrt(2*math.pi))

def resample_data(data: dict[float, float]):
    resampled_data: list[float] = []
    for center in CENTERS:
        gaussian = make_gaussian(center)
        # Scale reflectance factor to sensor intensity
        new_data = {x: y * gaussian(x) * SENSOR_INTENSITY for x, y in data.items()}
        resampled_data.append(sum(new_data.values()))
    return resampled_data
