#!/usr/bin/env python3
# Created By: Fred
# Date: Feb 2008 18
# Calculates cost of producing a pizza
def main():

    print("Hello")
    print("How are you doing ?")
    print(
        "This code only takes in numbers"
        "So please don't enter anything that is not a number"
        "Or else it will crash"
        "Thank you !!!"
    )
    # Get the length of the cuboid
    Length = int(input("Enter the length of the cuboid"))

    # Get the width of the cuboid
    Width = int(input("Enter the width of the cuboid"))

    # Get the width of the cuboid
    Height = int(input("Enter the height of the cuboid"))

    # Calculate the volume
    Volume = Length * Width * Height

    # calculate the surface area
    Surface_area = 2 * 0(Length * Width + Length * Height + Width * Height)

    # Display surface area
    print("the Surface area of the cuboid is {}".format(Surface_area))

    # Display volume
    print("The volume of the cuboid is {}".format(Volume))


if __name__ == "__main__":

    main()
