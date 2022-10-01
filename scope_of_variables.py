#!/usr/bin/env python3

# Created by: Chris Di Bert
# Created on: Sep 30, 2022
# This program shows assignment statements


def main():
    # variable definition
    number_of_students = 2
    width = 22.5
    length = 15.0
    word1 = "Hello"
    word2 = "World!"

    # using assignment statements
    number_of_students = number_of_students + 5
    area_of_rectangle = length * width
    hello_world = word1 + ", " + word2

    # output
    print("The number of students is: " + str(number_of_students))
    print("The area of a rectangle is: " + str(area_of_rectangle) + " cm²")
    print(hello_world)

    print("\nDone.")


if __name__ == "__main__":
    main()
