# Name: ...
# CSE 140
# Homework 2: DNA analysis

# This program reads DNA sequencer output and computes statistics, such as
# the GC content.  Run it from the command line like this:
#   python dna_analysis.py myfile.fastq


###########################################################################
### Libraries
###

# The sys module supports reading files, command-line arguments, etc.
import sys


###########################################################################
### Read the nucleotides into a variable named seq
###

# You need to specify a file name
if len(sys.argv) < 2:
    print("You must supply a file name as an argument when running this program.")
    sys.exit(2)
# The file name specified on the command line, as a string.
filename = sys.argv[1]
# A file object from which data can be read.
inputfile = open(filename)

# All the nucleotides in the input file that have been read so far.
seq = ""
# The current line number (= the number of lines read so far).
linenum = 0


for line in inputfile:
    linenum = linenum + 1
    # if we are on the 2nd, 6th, 10th line...
    if linenum % 4 == 2:
        # Remove the newline characters from the end of the line
        line = line.rstrip()
        seq = seq + line


###########################################################################
### Compute statistics
###

# Total nucleotides seen so far.
total_count = 0
# Number of G and C nucleotides seen so far.
gc_count = 0
# Number of A and T nucleotides seen so far.
at_count = 0
# Number of A nucleotides
a_count = 0
# Number of T nucleotides
t_count = 0
# Number of G nucleotides
g_count = 0
# Number of C nucleotides
c_count = 0


# for each base pair in the string,
for bp in seq:
    # increment the total number of bps we've seen
    total_count = total_count + 1

    # next, if the bp is a G or a C,
    if bp == 'C':
        # increment the count of c
        c_count += 1
        # increment the count of gc
        gc_count = gc_count + 1
    elif bp == 'G':
        # increment the count of c
        g_count += 1
        # increment the count of gc
        gc_count = gc_count + 1
    elif bp == 'A':
        # increment the count of a
        a_count += 1
        # increment the count of at
        at_count += 1
    elif bp == 'T':
        # increment the count of t
        t_count += 1
        # increment the count of at
        at_count += 1


# divide the gc_count by the total_count
gc_content = float(gc_count) / (a_count + t_count + g_count + c_count)
at_content = float(at_count) / (a_count + t_count + g_count + c_count)


# Print the answer
print('GC-content:', gc_content)
print('AT-content:', at_content)
print('G-content:', g_count)
print('C-content:', c_count)
print('A-content:', a_count)
print('T-content:', t_count)


# Compare sum of nucleotide counts, total_count, and seq length
print('Sum count:', a_count + t_count + g_count + c_count)
print('Total Count:', total_count)
print('Sequence length:', len(seq))


# Compute the AT/GC ratio
print('AT/GC Ratio:', at_count / gc_count)


# Use GC content to determine classification
if gc_content > .6:
    print ('GC Classifcation: high GC content')
elif gc_content < .4:
    print ('GC Classifcation: low GC content')
else:
    print ('GC Classifcation: moderate GC content')
