#!/usr/bin/env python
"""
Calculate nucleotide percentages in a DNA/RNA sequence.
"""

import sys
from collections import Counter

def calculate_nucleotide_percentages(sequence):
    """Calculate the percentage of each nucleotide in a sequence."""
    sequence = sequence.upper()
    length = len(sequence)
    
    # Count each nucleotide
    counts = Counter(sequence)
    
    # Calculate percentages
    percentages = {}
    for nucleotide in ['A', 'C', 'G', 'T', 'U']:
        if nucleotide in counts:
            percentages[nucleotide] = (counts[nucleotide] / length) * 100
        else:
            percentages[nucleotide] = 0
    
    return percentages

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 nucleotide_percent.py <sequence>")
        print("Example: python3 nucleotide_percent.py ACTG")
        sys.exit(1)
    
    sequence = sys.argv[1]
    
    # Validate sequence
    if not all(c in 'ACGTUacgtu' for c in sequence):
        print("Error: Invalid sequence. Use only A, C, G, T, U")
        sys.exit(1)
    
    percentages = calculate_nucleotide_percentages(sequence)
    
    print(f"\nSequence: {sequence.upper()}")
    print(f"Length: {len(sequence)}")
    print("\nNucleotide Percentages:")
    print("-" * 30)
    for nucleotide, percentage in percentages.items():
        if percentage > 0:
            print(f"{nucleotide}: {percentage:.1f}%")

if __name__ == "__main__":
    main()


def calculate_gc_content(sequence):
    """Calculate GC content percentage."""
    sequence = sequence.upper()
    gc_count = sequence.count('G') + sequence.count('C')
    return (gc_count / len(sequence)) * 100
