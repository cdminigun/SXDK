from pwn import *
import argparse

class generate_shellcode:
    def __init__(self, num_of_addresses, number_of_nop_instructions, operating_system, architecture, starting_address, offset, instruction_set):
        self.num_of_addresses = num_of_addresses
        self.number_of_nop_instructions = number_of_nop_instructions
        self.operating_system = operating_system
        self.architecture = architecture
        self.starting_address = starting_address
        self.offset = offset
        self.data = None
    def parse_inputs():
        parsing happens here
    def set_arch():

    def write_file(name):
        f = open(name, "w")
        f.write(self.data)
        f.close()



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Shell Exploitation Development Kit")
    parser.add_argument("-f", "--num_of_addresses", type=int, help="Number of addresses at the end of the egg.")
    parser.add_argument("-n", "--number_of_nop_instructions", type=int, help="The total size of your egg.")
    parser.add_argument("-o", "--operating_system", type=str, default="linux", help="The OS of your system. Ex. Linux/PPC, Linux/x86, Linux/x86_64 ")
    parser.add_argument("-a", "--architecture", type=int, default=32, help="32 or 64 bit depending upon the machine.") #This changes the relative offsets and shellcode.
    parser.add_argument("-s", "--starting_address", type=int, help="The starting address for your system based upon your stack.")
    parser.add_argument("-d", "--offset", type=int, default=0, help="The offset relative to the address. Utilized for guessing multiple spaces.") #Future release to have automated guesses.
    args = parser.parse_args()
    if not args.starting_address and not args.numb_of_addresses and not args.number_of_nop_instructions:
        parser.print_help()
    genshell = generate_shellcode(args.num_of_addresses, args.number_of_nop_instructions, args.operating_system, args.architecture, args.starting_address, args.offset)

