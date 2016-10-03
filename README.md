# SXDK
##ShellcodeEXploitDevelopmentKit

usage: sxdk.py [-h] [-f NUM_OF_ADDRESSES] [-t TOTAL_SIZE]
               [-o OPERATING_SYSTEM] [-a ARCHITECTURE] [-s STARTING_ADDRESS]
               [-e ENDIANNESS] [-d OFFSET] [-n NAME_OF_FILE]


###optional arguments:
  -h, --help            show this help message and exit


  -f NUM_OF_ADDRESSES, --num_of_addresses NUM_OF_ADDRESSES


                        Number of addresses at the end of the egg.


  -t TOTAL_SIZE, --total_size TOTAL_SIZE


                        The total size of your egg.


  -o OPERATING_SYSTEM, --operating_system OPERATING_SYSTEM


                        The OS of your system. Ex. Linux/PPC, Linux/x86,


                        Linux/x86_64


  -a ARCHITECTURE, --architecture ARCHITECTURE


                        32 or 64 bit depending upon the machine.


  -s STARTING_ADDRESS, --starting_address STARTING_ADDRESS


                        The starting address for your system based upon your stack.


  -e ENDIANNESS, --endianness ENDIANNESS


                        The endianness of your program. EX. little, big


  -d OFFSET, --offset OFFSET


                        The offset relative to the address. Utilized for


                        guessing multiple spaces.


  -n NAME_OF_FILE, --name_of_file NAME_OF_FILE


