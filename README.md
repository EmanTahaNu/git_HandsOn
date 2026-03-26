# Git Hands-On Project

A Python script to classify DNA/RNA sequences and search for motifs. This project was created as part of a Git tutorial to learn version control concepts.

## Description

`seqClass.py` is a command-line tool that:
- Classifies a sequence as DNA, RNA, or invalid
- Converts input sequences to uppercase for case-insensitive processing
- Searches for specific motifs in the sequence (optional)

## Usage

```bash
# Basic classification
python3 seqClass.py -s ACTG
# Output: The sequence is DNA

# With motif search
python3 seqClass.py -s ACTG -m TG
# Output:
# The sequence is DNA
# Motif search enabled: looking for motif "TG" in sequence "ACTG"... FOUND

# RNA example
python3 seqClass.py -s ACGUA -m CG
# Output:
# The sequence is RNA
# Motif search enabled: looking for motif "CG" in sequence "ACGUA"... FOUND
