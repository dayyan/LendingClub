'''
Created on May 30, 2013

@author: gczajkow

/**
  * TX and NY are good.
  *
  * States with substantial volume and higher-than-average returns:
  * CA, AZ, FL, GA, IL, MD, MO, NV, 
  */
'''
from Filter import Filter
from LoanEnum import LOAN_ENUM_addr_state

class State(Filter):
    '''
    classdocs
    '''

    def __init__(self, args, current=None):
        '''
        Constructor
        '''
        state_bitmap = {'AK': 1 << 0,
                        'AL': 1 << 1,
                        'AR': 1 << 2,
                        'AZ': 1 << 3,
                        'CA': 1 << 4,
                        'CO': 1 << 5,
                        'CT': 1 << 6,
                        'DC': 1 << 7,
                        'DE': 1 << 8,
                        'FL': 1 << 9,
                        'GA': 1 << 10,
                        'HI': 1 << 11,
                        'IA': 1 << 12,
                        'ID': 1 << 13,
                        'IL': 1 << 14,
                        'IN': 1 << 15,
                        'KS': 1 << 16,
                        'KY': 1 << 17,
                        'LA': 1 << 18,
                        'MA': 1 << 19,
                        'MD': 1 << 20,
                        'ME': 1 << 21,
                        'MI': 1 << 22,
                        'MN': 1 << 23,
                        'MO': 1 << 24,
                        'MS': 1 << 25,
                        'MT': 1 << 26,
                        'NC': 1 << 27,
                        'NE': 1 << 28,
                        'NH': 1 << 29,
                        'NJ': 1 << 30,
                        'NM': 1 << 31,
                        'NV': 1 << 32,
                        'NY': 1 << 33,
                        'OH': 1 << 34,
                        'OK': 1 << 35,
                        'OR': 1 << 36,
                        'PA': 1 << 37,
                        'RI': 1 << 38,
                        'SC': 1 << 39,
                        'SD': 1 << 40,
                        'TN': 1 << 41,
                        'TX': 1 << 42,
                        'UT': 1 << 43,
                        'VA': 1 << 44,
                        'VT': 1 << 45,
                        'WA': 1 << 46,
                        'WI': 1 << 47,
                        'WV': 1 << 48,
                        'WY': 1 << 49,
                        'NULL': 1 << 50,
                        }

        self.conversion_table = state_bitmap.copy()

        options = self.powerBitSet([state_bitmap[state] for state in ["CA", "AZ", "FL", "GA", "IL", "MD", "MO", "NV"]])

        # self.options = self.powerSet(["AK", "AL", "AR", "AZ", "CA", "CO", "CT", "DC", "DE", "FL", "GA",
        # "HI", "IA", "ID", "IL", "IN", "KS", "KY", "LA", "MA", "MD", "ME",
        # "MI", "MN", "MO", "MS", "MT", "NC", "NE", "NH", "NJ", "NM", "NV",
        # "NY", "OH", "OK", "OR", "PA", "RI", "SC", "SD", "TN", "TX", "UT",
        # "VA", "VT", "WA", "WI", "WV", "WY", "NULL"])

        Filter.__init__(self, args, options, current)

    def convert(self, raw_data):
        return self.conversion_table[raw_data] if raw_data else self.conversion_table["NULL"]

    def __str__(self):
        l = []
        for key, val in self.conversion_table.items():
            if val & self.current > 0:
                l.append(key)
        return str(l)

    def apply(self, loan, LOAN_ENUM_addr_state=LOAN_ENUM_addr_state):
        current = self.getCurrent()
        return loan[LOAN_ENUM_addr_state] & current > 0
