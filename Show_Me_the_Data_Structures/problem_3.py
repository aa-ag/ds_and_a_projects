import collections


def frequency(s):
    freqs = collections.Counter(s)
    return freqs


def sortFreq(freqs):
    letters = freqs.keys()
    tuples = []
    for let in letters:
        tuples.append((freqs[let], let))
    tuples.sort()
    return tuples


def buildTree(tuples):
    while len(tuples) > 1:
        leastTwo = tuple(tuples[0:2])                  # get the 2 to combine
        theRest = tuples[2:]                          # all the others
        combFreq = leastTwo[0][0] + leastTwo[1][0]     # the branch points freq
        # add branch point to the end
        tuples = theRest + [(combFreq, leastTwo)]
        # sort it into place
        tuples = sorted(tuples, key=lambda x: x[0])
    return tuples[0]  # Return the single tree inside the list


def trimTree(tree):
    # Trim the freq counters off, leaving just the letters
    p = tree[1]                                    # ignore freq count in [0]
    if type(p) == type(""):
        return p              # if just a leaf, return it
    else:
        # trim left then right and recombine
        return (trimTree(p[0]), trimTree(p[1]))


def assignCodes(node, pat=''):
    global codes
    if type(node) == type(""):
        codes[node] = pat                # A leaf. set its code
    else:                              #
        assignCodes(node[0], pat+"0")    # Branch point. Do the left branch
        assignCodes(node[1], pat+"1")


def encode(s):
    global codes
    output = ""
    for ch in s:
        output += codes[ch]
    return output


def decode(tree, s):
    output = ""
    p = tree
    for bit in s:
        if bit == '0':
            p = p[0]     # Head up the left branch
        else:
            p = p[1]     # or up the right branch
        if type(p) == type(""):
            output += p              # found a character. Add to output
            p = tree                 # and restart for next character
    return output


##############------ DRIVER CODE -----------############
codes = {}

s = 'aaabccdeeeeeffg'

freqs = frequency(s)
# print(frequency)

tuples = sortFreq(freqs)
# print(tuples)

tree = buildTree(tuples)
trim = trimTree(tree)
# print(trim)

assignCodes(trim)
# print(codes)

encoded_data = encode(s)
print(encoded_data)

print(decode(trim, encoded_data))
