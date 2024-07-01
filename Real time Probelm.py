import time
# Constants
TOTAL_SPOTS = 100  # Total parking spots
available_spots = TOTAL_SPOTS  # Available parking spots
def read_sensor_data():
    # Simulate reading sensor data for cars entering or exiting
    # Returning 'enter' or 'exit' based on a simulated condition
    # For demonstration purposes, this will alternate between 'enter' and 'exit'
    time_of_day = int(time.time()) % 2
    if time_of_day == 0:
        return 'enter'
    else:
        return 'exit'
def display_available_spots():
    if available_spots > 0:
        print(f"Available spots: {available_spots}")
    else:
        print("Lot Full")
# Main loop
while True:
    sensor_data = read_sensor_data()
    if sensor_data == 'enter' and available_spots > 0:
        available_spots -= 1
    elif sensor_data == 'exit' and available_spots < TOTAL_SPOTS:
        available_spots += 1
    display_available_spots()
    time.sleep(5)  # Wait for 5 seconds before checking again