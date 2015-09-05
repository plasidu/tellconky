import sys, re

class Log(object):
    """
    A file object with lines of text in it.

    :object: A filename of the text file.
    """

    def __init__(self, object):
        self.file = open(object, 'r')

        
    def line_offsets(self):
        """(object with open file mode 'r' in .file method) -> list
        Read in the file once and return a list of line offsets.
    
        :self: A pointer to file opened in readmode.
        :return: A list of offsets.
    
        >>> log = readlog.Log('foo.bar')
        >>> log.file.readlines()
        ['This\n', 'is\n', 'Sparta.\n']
        >>> log.line_offsets()
        [0, 5, 8]
        """ 
    
        self.file.seek(0)
        collector = []
        offset = 0
        for line in self.file:
            collector.append(offset)
            offset += len(line)
        self.file.seek(0)
        return collector
    
    def tail(self, stop_line='', verbose=False):
        """(object with open file mode 'r' in .file method) -> list
    
        :stop_line: Stop reading when found in file.
        :self: A pointer to file opened in readmode.
        :returns: List of lines found in log until the stop_line in reverse order, e.g. starting from last line.

        >>> log = readlog.Log('foo.bar')
        >>> log.file.readlines()
        ['This\n', 'is\n', 'Sparta.\n']
        >>> log.tail('This\n')
        ['Sparta.\n', 'is\n']
        """

        unfound = True
        collector = []
        linenumber = -1
        while unfound:
            try:
                self.file.seek(self.line_offsets()[linenumber])
                line = self.file.readline()
                if line == stop_line or line == '':
                    unfound = False
                else:
                    collector.append(line)
                    linenumber -= 1
            except:
                if verbose:
                    print '\nReturning whole linewise reversed file.'
                break
        return collector
    
    def last_line(self):
        """(object with open file mode 'r' in .file method) -> string
        Grabs the last line of file.
    
        :self: A file opened for reading.
        :returns: Last line of the file as a string.
   
        >>> log = readlog.Log('foo.bar')
        >>> log.file.readlines()
        ['This\n', 'is\n', 'Sparta.\n']
        >>> log.last_line()
        'Sparta.\n'
        """

        self.file.seek(self.line_offsets()[-1])
        last_line = self.file.readline()
        return last_line

def filter_regex(lines, *args):
    """(list, string) -> list
    Searches list of strings for keywords and returns matches in a list.
    [[Journal:2015:09:04|2015-09-04 22:25]] note: intended keywords were 'Start of synchronisation' and 'Finish of upload'. 

    :lines: List of lines to be searched through.
    :*args: List of keyword to be queried in lines.
    :returns: List of lines in which query was found.
    
    >>> tail = log.tail()
    >>> readlog.filter_regex(tail, '.*Start\sof.*')
    ['SYNC.PY\t|| 02 Sep 2015 13:57:28 Start of synchronisation \n']

    >>> l = ['I am red.', 'I am blue.', 'You too.']
    >>> readlog.filter_regex(l, 'I am')
    ['I am red.', 'I am blue.']
    """

    collector = []
    for line in lines:
        for regex in args:
            if re.match(regex, line):
                collector.append(line)
    return collector

def filter_time(line, regex):
    """(string, string) -> string
    Get time information from lines.

    >>> filter_time('SYNC.PY\t|| 02 Sep 2015 13:57:28 Start of synchronisation \n', '.*(\d\d\s\w+\s\d+\s\d+:\d+:\d+)\s.*')
    '02 Sep 2015 13:57:28'

    :line: Line in which to search for time.
    :returns: A time strings.

    """
    match = re.match(regex, line)
    return match.groups(1)
