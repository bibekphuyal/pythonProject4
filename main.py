def find_smallest_number(numbers_array):
    # Check if the list is empty
    if not numbers_array:
        return None

    # Initialize the smallest number with the first element of the array
    smallest_number = numbers_array[0]

    # Iterate through the array to find the smallest number
    for num in numbers_array:
        if num < smallest_number:
            smallest_number = num

    return smallest_number

def to_find_smallest_number():
    while True:
        # Get input of numbers from users
        input_numbers = input("Enter the list of numbers separated by spaces:")

        try:
            numbers_array = [int(num) for num in input_numbers.split()]

            # Check if the users have entered valid numbers
            if not numbers_array:
                print("Enter valid integers")
            else:
                # Call the function to find the smallest number
                smallest_number = find_smallest_number(numbers_array)
                print(f"The smallest number is: {smallest_number}")
                break  # Exit the loop if valid input is provided

        except ValueError:
            print("Invalid input, enter valid integers")

# Call the main function
to_find_smallest_number()