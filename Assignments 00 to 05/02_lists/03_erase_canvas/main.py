import tkinter as tk  # Import tkinter to create GUI (window) and draw on canvas

def main():

  root = tk.Tk()  # Create the main window
  root.title("Canvas Eraser")  # Set a title for the window

  canvas = tk.Canvas(root, width=400, height=400)  # Create a canvas (a blank area to draw on)
  canvas.pack()  # Display the canvas inside the window

  CELL_SIZE = 40  # The size of each cell (blue square)
  ROWS = 20  # Number of rows of cells
  COLS = 20  # Number of columns of cells
  cells = []  # List to store the created cells

# Create a grid of blue rectangles
  for row in range(ROWS):  # Loop through each row
    for col in range(COLS):  # Loop through each column
        x1 = col * CELL_SIZE  # Left side of the cell (based on the column)
        y1 = row * CELL_SIZE  # Top side of the cell (based on the row)
        x2 = x1 + CELL_SIZE  # Right side of the cell
        y2 = y1 + CELL_SIZE  # Bottom side of the cell
        
        # Create a blue rectangle on the canvas (a blue cell)
        rect = canvas.create_rectangle(x1, y1, x2, y2, fill="black", outline="green")
        
        # Add the rectangle to our cells list
        cells.append((rect, x1, y1, x2, y2))  # Store info about the rectangle


  ERASER_SIZE = 40  # Size of the eraser (same as the cells)

# Create the eraser (a white square) at position (0, 0)
  eraser = canvas.create_rectangle(0, 0, ERASER_SIZE, ERASER_SIZE, outline="black")

  def on_mouse_drag(event):
    # Get the mouse position (where the user is dragging the mouse)
    x1 = event.x - ERASER_SIZE // 2  # Calculate the new position of the eraser (centered on the mouse)
    y1 = event.y - ERASER_SIZE // 2
    x2 = x1 + ERASER_SIZE  # Bottom-right corner of the eraser
    y2 = y1 + ERASER_SIZE
    
    # Move the eraser to the new position
    canvas.coords(eraser, x1, y1, x2, y2)

    # Erase any blue cell that overlaps with the eraser
    for rect, cx1, cy1, cx2, cy2 in cells:
        # Check if the eraser overlaps with the cell
        if not (x2 < cx1 or x1 > cx2 or y2 < cy1 or y1 > cy2):
            canvas.itemconfig(rect, fill="white")  # Change the color of the cell to white (erase it)


  canvas.bind("<B1-Motion>", on_mouse_drag)  # Bind the drag event to the function
  root.mainloop()

if __name__ == '__main__':
    main()