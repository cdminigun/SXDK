from pwnlib import *
import argparse

os_types = ["linux", "windows", "freebsd"]
binuti_is = {"ppc64" : 'powerpc64', "ppc": 'powerpc',  "mips64": 'mips64', "thumb":'thumb', "amd64" : 'amd64', "x86":'i386', "mips":'mips', "x86_64" : 'ia64', "arm": 'arm' }

class SXDK(Exception):
    pass

class GenerateShellcode:
    def __init__(self, num_of_addresses, number_of_nop_instructions, operating_system, architecture, starting_address, offset, endianness):
        self.num_of_addresses = num_of_addresses
        self.number_of_nop_instructions = number_of_nop_instructions
        self.operating_system = operating_system
        self.architecture = architecture
        self.starting_address = starting_address
        self.offset = offset
        self.endianness = endianness.lower()
        self.data = None
        self.instruction_set = None
        self.shell_os = None
    def parse_inputs(self):
        self.starting_address = int(self.starting_address, 16)
        if '/' in self.operating_system
            self.shell_os, self.instruction_set = self.operating_system.split('/')
        else:
            raise SXDK("Input to Operating_system field was wrong.")
        if self.instruction_set.lower() in binuti_is:
            contest.arch = binuti_is[self.instruction_set.lower()]
        else:
            raise SXDK("Input into operating_system is wrong.")
        if not self.shell_os.lower() in os_types:
            raise SXDK("Input into operating_system is wrong.")
        context.os = self.shell_os.lower()
        self.shell_os = self.shell_os.lower()
        if self.architecture != 32 || self .architecture != 64:
            raise SXDK("Input into architecture is wrong.")
        context.bits = self.architecture
        if "little" in self.endianness or "big" in self.endianness:
            context.endian = self.endianness
        else:
            raise SXDK("Input into endianness is wrong.")
    def write_file(self, name):
        f = open(name, "w")
        f.write(self.data)
        f.close()



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Shell Exploitation Development Kit")
    parser.add_argument("-f", "--num_of_addresses", type=int, help="Number of addresses at the end of the egg.")
    parser.add_argument("-n", "--number_of_nop_instructions", type=int, help="The total size of your egg.")
    parser.add_argument("-o", "--operating_system", type=str, default="linux/x86", help="The OS of your system. Ex. Linux/PPC, Linux/x86, Linux/x86_64 ")
    parser.add_argument("-a", "--architecture", type=int, default=32, help="32 or 64 bit depending upon the machine.") #This changes the relative offsets and shellcode.
    parser.add_argument("-s", "--starting_address", type=str, help="The starting address for your system based upon your stack.")
    parser.add_argument("-e", "--endianness", type=str, default="little", help="The endianness of your program. EX. little, big")
    parser.add_argument("-d", "--offset", type=int, default=0, help="The offset relative to the address. Utilized for guessing multiple spaces.") #Future release to have automated guesses.
    args = parser.parse_args()
    if not args.starting_address and not args.numb_of_addresses and not args.number_of_nop_instructions:
        parser.print_help()

    genshell = GenerateShellcode(args.num_of_addresses, args.number_of_nop_instructions, args.operating_system, args.architecture, args.starting_address, args.offset)
    try:
        genshell.parse_intputs()
    except:
    #end
    genshell.write_file()
