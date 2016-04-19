"""SecTalks CTF 101 - Cryptanalysis
Frequency analysis of ngrams (bigram, trigram, etc.)

Inspiered from:
    http://community.websense.com/blogs/securitylabs/archive/2010/05/20/
    a-simple-n-gram-calculator-pyngram.aspx
"""

from operator import itemgetter  # used for sorting


def get_ngrams(message, size):
    """Return a sorted list of ngrams <= size

    Usage:
        for i in get_ngram("ciphertext", 2):
            print("{0}: {1} times".format(i[0], i[1]))

    Args:
        message (str): input string
        size (int): size of ngrams

    Return:
        [] sorted list of available ngrams in message
    """

    result = {}

    # Perform some valdation
    if size < 1:
        raise ValueError("ngram size most be bigger than 1")
    if len(message) < 1:
        raise ValueError("message most be bigger than 1 character")

    # Count frequency of ngrams
    for i in xrange(len(message) - size+1):
        # TODO: find word boundary and skip non-alphabetic characters
        ngram = message[i:i+size]
        if ngram in result.keys():
            result[ngram] += 1
        else:
            result[ngram] = 1

    # Sort
    return sorted(result.iteritems(), key=itemgetter(1), reverse=True)
