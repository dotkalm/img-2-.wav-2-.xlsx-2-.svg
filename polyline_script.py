import math

def make_polyline(polyline_coordinates, multiplier=1.25, is_animation=False, peak_multiplier=5):
  """
  Generate SVG polyline coordinates from FFT data.

  Args:
    polyline_coordinates: List of FFT values
    multiplier: Vertical spacing between points (default: 1.25)
    is_animation: If True, uses compressed horizontal amplitude for animation morphing (default: False)
  """
  try:
    coordinates = [[] for _ in range(len(polyline_coordinates) + 1)]
    column = None
    for i in range(len(polyline_coordinates)):
      if i > 0:
        if is_animation:
          coordinates[i] = f"{math.floor(polyline_coordinates[i]*peak_multiplier) + column},{i * multiplier}"
        else:
          coordinates[i] = f"{(polyline_coordinates[i]*peak_multiplier) + column},{i * multiplier}"
      else:
        column = polyline_coordinates[i]
        coordinates[i] = f"{column},0"
    coordinates[len(polyline_coordinates)] = f"L {column}, {len(polyline_coordinates) * multiplier}"
    return " ".join(coordinates)
  except Exception as e:
    print(e)
    return None
