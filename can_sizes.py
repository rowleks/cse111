import math

def main():
    cans = [
        (6.83, 10.16),
        (7.78, 11.91),
        (8.73, 11.59),
        (10.32, 11.91),
        (10.79, 17.78),
        (13.02, 14.29),
        (5.40, 8.89),
        (6.83, 7.62),
        (15.72, 17.78),
        (6.83, 12.38),
        (7.62, 11.27),
        (8.10, 11.11),
    ]

    for i, (radius, height) in enumerate(cans, start=1):
        volume = compute_volume(radius, height)
        surface_area = compute_surface_area(radius, height)
        storage_efficiency = compute_storage_efficiency(volume, surface_area)
        print(f"Can {i} storage efficiency: {storage_efficiency:.2f}")

def compute_volume(r, h):
    return math.pi * r**2 * h

def compute_surface_area(r, h):
    return 2 * math.pi * r * (r + h)

def compute_storage_efficiency(v, s):
    return v / s

main()