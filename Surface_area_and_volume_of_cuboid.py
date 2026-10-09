#!/usr/bin/env python3
# Created By: Fred
# Date: Feb 2008 18
# Calculates surface area and volume of a cuboid
def main():

    print("Hello")
    print("How are you doing ?")
    print(
        "This code only takes in numbers\n"
        "So please don't enter anything that is not a number\n"
        "Or else it will crash\n"
        "Thank you !!!"
    )
    # Get the length of the cuboid
    Length = float(input("Enter the length of the cuboid (m):"))

    # Get the width of the cuboid
    Width = float(input("Enter the width of the cuboid (m):"))

    # Get the width of the cuboid
    Height = float(input("Enter the height of the cuboid (m):"))

    # Calculate the volume
    Volume = Length * Width * Height

    # calculate the surface area
    Surface_area = 2 * (Length * Width + Length * Height + Width * Height)

    # Display surface area
    print("The Surface area of the cuboid is {;.2f} m²".format(Surface_area))

    # Display volume
    print("The volume of the cuboid is {;.2f} m³".format(Volume))


if __name__ == "__main__":

    main()
