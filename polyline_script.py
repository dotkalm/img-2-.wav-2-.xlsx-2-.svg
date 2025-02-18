import math 

def make_polyline(polyline_coordinates):
  try:
    multiplier = 1.25
    coordinates = [[] for _ in range(len(polyline_coordinates) + 1)]
    column = None
    for i in range(len(polyline_coordinates)):
      if i > 0:
        coordinates[i] = f"{(polyline_coordinates[i]*32) + column},{i * multiplier}"
      else:
        column = polyline_coordinates[i]
        coordinates[i] = f"{column},0"
    coordinates[len(polyline_coordinates)] = f"L {column}, {len(polyline_coordinates) * multiplier}"
    return " ".join(coordinates)
  except Exception as e:
    print(e)
    return None

def make_polyline_for_animation(polyline_coordinates):
  try:
    multiplier = 1.25
    coordinates = [[] for _ in range(len(polyline_coordinates) + 1)]
    column = None
    for i in range(len(polyline_coordinates)):
      if i > 0:
        coordinates[i] = f"{math.floor(polyline_coordinates[i]*3) + column},{i * multiplier}"
      else:
        column = polyline_coordinates[i]
        coordinates[i] = f"{column},0"
    coordinates[len(polyline_coordinates)] = f"L {column}, {len(polyline_coordinates) * multiplier}"
    return " ".join(coordinates)
  except Exception as e:
    print(e)
    return None
