import webbrowser
import sys

# make sure the input in command line is  2 i.e. python3 [test2.py address]
if len(sys.argv) != 2:
    print("Invalid usage, must be: python3 test.py 'address'")
    sys.exit()
else:
    # input is correct so extract the address and send user to webpage of google maps on that address
    address = sys.argv[1]

    # this opens up the users input from command line as the address on maps
    webbrowser.open(f'https://www.google.com/maps/place/{address}')

    # this loops through the text file and opens each line as a link
    destinations = open('address.txt', 'r')

    for line in destinations:
        webbrowser.open(f'https://www.google.com/maps/place/{line}')

