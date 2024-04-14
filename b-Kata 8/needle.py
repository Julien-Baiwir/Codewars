haystack = ["hay", "junk", "hay", "hay", "moreJunk", "needle", "randomJunk"]

def find_needle(haystack):
    for i, item in enumerate(haystack):
        if item == "needle":
            return f"found the needle at position {i}"

def find_needle(haystack):
    return f'found the needle at position {haystack.index("needle")}'

def find_needle(haystack): return 'found the needle at position %d' % haystack.index('needle')

def find_needle(haystack):
	return 'found the needle at position {}'.format(haystack.index('needle'))

def find_needle(haystack):
    return "found the needle at position " + str(haystack.index("needle"))