"""
DojoAllocation

Usage:
  dojoapp.py create_room <room_type> <room_name>...
  dojoapp.py add_person <person_name> <FELLOW|STAFF> [wants_accomodation]
  

Options:
  -h --help     Show help info.


"""

from docopt import docopt

if __name__ == '__main__':
    arguments = docopt(__doc__, version='Denis-Kaniu-Dojo-Allocation v_0')
print(arguments)
