#!/usr/bin/env python

import sys, re
from argparse import ArgumentParser

# Create command-line argument parser

parser = ArgumentParser(description = 'Classify a sequence as DNA or RNA')
parser.add_argument("-s", "--seq", type = str, required = True, help = "Input sequence")
parser.add_argument("-m", "--motif", type = str, required = False, help = "Motif")

# Display help if no arguments provided

if len(sys.argv) == 1:
    parser.print_help()
    sys.exit(1)

# Parse command-line arguments


args = parser.parse_args()

# Convert input sequence to uppercase for case-insensitive processing

args.seq = args.seq.upper()



# Improved classification logic:
# - Detects sequences containing both T and U (invalid)
# - Properly identifies DNA (contains T) and RNA (contains U)
# - Handles ambiguous sequences with no T or U
# - Provides clear error messages for invalid sequences

# Validate sequence contains only valid nucleotides
if re.search('^[ACGTU]+$', args.seq):
    # Check if sequence contains both T and U (invalid)
    if re.search('T', args.seq) and re.search('U', args.seq):
        print ('Error: Sequence contains both T (DNA) and U (RNA). Cannot classify.')
    # Check for DNA (contains T but no U)
    elif re.search('T', args.seq):
        print ('The sequence is DNA')
    # Check for RNA (contains U but no T)
    elif re.search('U', args.seq):
        print ('The sequence is RNA')
    # If no T or U detected, ambiguous case
    else:
        print ('The sequence can be DNA or RNA (no T or U detected)')
else:
    print ('Error: Invalid sequence. Use only A, C, G, T, U')


# Search for a motif if provided by user

if args.motif:
    args.motif = args.motif.upper()
    print(f'Motif search enabled: looking for motif "{args.motif}" in sequence "{args.seq}"... ', end = '')
    if re.search(args.motif, args.seq):

        print("MOTIF FOUND - MAIN VERSION")
        
    else:
        print("MOTIF NOT PRESENT")
