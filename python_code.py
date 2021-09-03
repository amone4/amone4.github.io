

# Ignore this garbage
import sys
if __name__ == '__main__':
    if (len(sys.argv) == 2):
        N = int(sys.argv[1])

        # Size of canvas
        ROWS = 17
        COLS = 106

        def inequality_satisfied(x, y):
            # //    => Floor
            # %     => Modulus
            # **    => Power
            return 0.5 < (((y//ROWS) // (2**(ROWS*x + y%ROWS))) % 2)

        # Going through canvas
        for y in range(0, ROWS):
            for x in range(0, COLS):

                # Converting to proper x,y coordinates
                real_x = x
                real_y = N + (ROWS - y - 1)

                # Checking for inequality
                if inequality_satisfied(real_x, real_y):
                    print("|", end="")
                else:
                    print(" ", end="")
            print("")



