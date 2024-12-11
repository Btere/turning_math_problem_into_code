Solution 1

distance_to_cover = 450
time_to_get_to_destination = 6
David_speed = distance_to_cover / time_to_get_to_destination
print(David_speed)


Solution 2

def average_speed()-> float:
  distance_to_cover = 450
  time_to_get_to_destination = 6
  David_speed = distance_to_cover / time_to_get_to_destination
  #print(David_speed)
  return David_speed

result = average_speed()
