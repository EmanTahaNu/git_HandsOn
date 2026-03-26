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

if re.search('^[ACGTU]+$', args.seq):
    if re.search('T', args.seq):
        print ('The sequence is DNA')
    elif re.search('U', args.seq):
        print ('The sequence is RNA')
    else:
        print ('The sequence can be DNA or RNA')
else:
    print ('The sequence is not DNA nor RNA')


# Search for a motif if provided by user

if args.motif:
    args.motif = args.motif.upper()
    print(f'Motif search enabled: looking for motif "{args.motif}" in sequence "{args.seq}"... ', end = '')
    if re.search(args.motif, args.seq):

        print("MOTIF FOUND - MAIN VERSION")
        
    else:
        print("MOTIF NOT PRESENT")
