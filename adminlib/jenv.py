import re

import jinja2.ext

    
class DelimNumber(jinja2.ext.Extension):
    """Jinja extension: Display a number with place separators.
    E.g "12,345,678". If the value is not an integer or str(int),
    return it unchanged.
    """
    pat_alldigits = re.compile('^[0-9]+$')

    def __init__(self, env):
        env.filters['delimnumber'] = self.delim_number

    @staticmethod
    def delim_number(val):
        val = str(val)
        if not DelimNumber.pat_alldigits.match(val):
            return val
    
        ls = []
        lenv = len(val)
        pos = lenv % 3
        if pos:
            ls.append(val[ 0 : pos ])
        while pos < lenv:
            ls.append(val[ pos : pos+3 ])
            pos += 3
        return ','.join(ls)
        
class Pluralize(jinja2.ext.Extension):
    """Jinja extension: Display "" or "s", depending on whether the
    value is 1.
    """
    def __init__(self, env):
        env.filters['plural'] = self.pluralize

    @staticmethod
    def pluralize(val, singular='', plural='s'):
        if val == 1 or val == '1':
            return singular
        else:
            return plural
            
        
class SplitURI(jinja2.ext.Extension):
    def __init__(self, env):
        env.filters['splituri'] = self.splituri

    @staticmethod
    def splituri(val):
        ls = val.split('/')
        if not ls:
            return []
        if ls[0] == 'arch':
            res = [ ('Archive', 'arch') ]
            for ix in range(1, len(ls)):
                res.append( (ls[ix], '/'.join(ls[ 0 : ix+1 ])) )
            return res
        return [ (val, val) ]
    
            