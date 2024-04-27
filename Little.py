import turtle
import tkinter as tk
from PIL import ImageTk, Image

def start_game():
    # Close the start window
    start_window.destroy()

    # Screen and turtle setup
    screen = turtle.Screen()
    screen.title("Little Pirate's Code Adventure")
    screen.setup(width=800, height=600)

    # Set background image
    screen.bgpic("C:/Users/Lewis/OneDrive/Documents/Coding/Python_project/Turtles.gif")  # Replace "path/to/your/background/image.png" with the actual path to your image file

    # Define turtle objects
    pirate = turtle.Turtle()
    pirate.shape("turtle")
    pirate.color("black")
    pirate.penup()
    pirate.goto(-200, 0)
    pirate.pendown()
    # Increase the size of the pirate
    pirate.shapesize(4)  # Change the factor as needed

    parrot = turtle.Turtle()
    parrot.shape("turtle")
    parrot.color("blue")
    parrot.penup()
    parrot.goto(200, 70)
    parrot.pendown()
    # Increase the size of the parrot
    parrot.shapesize(4)  # Change the factor as needed

    # Function to move the pirate
    def move_pirate(direction, steps):
        if direction == "forward":
            pirate.forward(steps)
        elif direction == "left":
            pirate.left(90 * steps)
        elif direction == "right":
            pirate.right(90 * steps)
        else:
            print("Invalid direction. Please enter 'forward', 'left', or 'right'.")

    # Function to check if parrot is found
    def check_parrot():
        if abs(pirate.xcor() - parrot.xcor()) <= 10 and abs(pirate.ycor() - parrot.ycor()) <= 10:
            return True
        else:
            return False

    # Function to display hint based on pirate's position
    def get_hint():
        x_distance = parrot.xcor() - pirate.xcor()
        y_distance = parrot.ycor() - pirate.ycor()
        if x_distance > 0:
            print("Turn right or move forward to get closer to your parrot!")
        elif x_distance < 0:
            print("Turn left or move forward to get closer to your parrot!")
        if y_distance > 0:
            print("Move down to get closer to your parrot!")
        elif y_distance < 0:
            print("Move up to get closer to your parrot!")

    # Game loop
    while not check_parrot():
        # Get user input for direction and steps
        direction = input("Enter a direction (forward, left, right): ")
        steps = int(input("Enter the number of steps: "))
        
        # Move the pirate
        move_pirate(direction, steps)
        
        # Display hint if needed
        if not check_parrot():
            get_hint()

    # Parrot found! Display congratulations message
    print("Congratulations! You found your parrot!")

    # Exit the game on screen click
    screen.exitonclick()

# Create the startup window
start_window = tk.Tk()
start_window.title("Welcome to Little Pirate's Code Adventure")

# Load the image
image_path = "C:/Users/Lewis/OneDrive/Documents/Coding/Python_project/Picture.jpg"  # Replace "path/to/your/startup/image.png" with the actual path to your image file
image = Image.open(image_path)
# Resize the image if needed
image = image.resize((300, 200), Image.LANCZOS)
photo = ImageTk.PhotoImage(image)

# Add a label with the image
image_label = tk.Label(start_window, image=photo)
image_label.pack(pady=10)

# Add a label with text
label = tk.Label(start_window, text="Welcome to Little Pirate's Code Adventure", font=("Helvetica", 16))
label.pack(pady=10)

# Add a start button
start_button = tk.Button(start_window, text="Start Game", font=("Helvetica", 14), command=start_game)
start_button.pack(pady=10)

# Run the startup window
start_window.mainloop()
