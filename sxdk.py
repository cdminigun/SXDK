import pwn
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Shell Exploitation Development Kit")
    parser.add_argument("-f", "--address_num", type=int, help="Number of addresses at the end of the egg.")
    parser.add_argument("-n", "--number_of_nop_instructions", type=int, help="The total size of your egg.")
    parser.add_argument("-o", "--operating_system", type=str)
    parser.add_argument("-a", "--architecture", type=str)
