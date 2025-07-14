# Import necessary modules
import time # For sleep functionality
import random  # For simulating sensor readings

# Constants for motor control
FORWARD_SPEED = 100
TURN_SPEED = 50
OBSTACLE_DISTANCE_THRESHOLD = 20  # Distance in cm to detect an obstacle

# Mock functions to simulate motor control and sensor readings
def set_motor_speed(left_speed, right_speed):
    print(f"Left Motor Speed: {left_speed}, Right Motor Speed: {right_speed}")

def read_line_sensor():
    # Simulate line sensor reading (1 for line detected, 0 for no line)
    return random.choice([0, 1])  # Replace with actual sensor reading

def read_obstacle_sensor():
    # Simulate obstacle sensor reading (distance in cm)
    return random.randint(5, 30)  # Replace with actual sensor reading

def follow_line():
    while True:
        line_detected = read_line_sensor()
        obstacle_distance = read_obstacle_sensor()

        if obstacle_distance < OBSTACLE_DISTANCE_THRESHOLD:
            # Obstacle detected, stop and turn
            print("Obstacle detected! Avoiding...")
            set_motor_speed(-TURN_SPEED, TURN_SPEED)  # Turn right
            time.sleep(0.5)  # Adjust time as needed
            set_motor_speed(FORWARD_SPEED, FORWARD_SPEED)  # Move forward
        elif line_detected:
            # Line detected, move forward
            set_motor_speed(FORWARD_SPEED, FORWARD_SPEED)
        else:
            # No line detected, adjust direction
            print("No line detected! Searching...")
            set_motor_speed(TURN_SPEED, -TURN_SPEED)  # Turn left
            time.sleep(0.5)  # Adjust time as needed

        time.sleep(0.1)  # Small delay for loop iteration

# Start the line following behavior
if __name__ == "__main__":
    try:
        follow_line()
    except KeyboardInterrupt:
        print("Stopping the robot.")
        set_motor_speed(0, 0)  # Stop the robot
