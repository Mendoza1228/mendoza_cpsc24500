from gallery import Gallery
from circle import Circle
from rectangle import Rectangle
from triangle import Triangle  

def main():
    gallery_name = input("Enter the name of the gallery: ")
    my_gallery = Gallery(gallery_name)


    while True:
        print("\n1. Add a Circle")
        print("2. Add a Rectangle")
        print("3. Add a Triangle")
        print("4. Display all shapes")
        print("5. Show total area")
        print("6. Show largest shape")
        print("7. Exit")    

        choice = input("Choose an option (1-7 ): ")

        try:
            if choice == '1':
                radius = float(input("Enter the radius of the circle: "))
                circle = Circle(radius)
                my_gallery.add_shape(circle)
                print("Circle added successfully.")
            elif choice == '2':
                width = float(input("Enter the width of the rectangle: "))
                height = float(input("Enter the height of the rectangle: "))
                rectangle = Rectangle(width, height)
                my_gallery.add_shape(rectangle)
                print("Rectangle added successfully.")
            elif choice == '3':
                side_a = float(input("Enter side A of the triangle: "))
                side_b = float(input("Enter side B of the triangle: "))
                side_c = float(input("Enter side C of the triangle: "))
                triangle = Triangle(side_a, side_b, side_c)
                my_gallery.add_shape(triangle)
                print("Triangle added successfully.")
            elif choice == '4':
                my_gallery.display_all()
            elif choice == '5':
                total_area = my_gallery.total_area()
                print(f"Total area of all shapes: {total_area:.2f}")
            elif choice == '6':
                largest_shape = my_gallery.largest_shape()
                if largest_shape:
                    print(f"Largest shape: {largest_shape.describe()} with area {largest_shape.area():.2f}")
                else:
                    print("No shapes in the gallery.")
            elif choice == '7':
                print("Exiting the program. Goodbye!")
                break
            else:
                print("Invalid option. Please choose a number between 1 and 7.")
        except ValueError as e:
            print(f"Error: {e}")
if __name__ == "__main__":
    main()

