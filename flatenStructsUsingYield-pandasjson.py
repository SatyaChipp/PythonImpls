
import itertools
from collections import Iterable, Sequence, MutableMapping

input1 = [{  "widgets" :[{"num": "1", "letter": "a",
                         "widgets" :[{"num": "2", "letter": "b",
                                      "widgets" :[{"num": "3","letter": "c"},
                                                  {"num": "4", "letter": "d"}]
                                      }]
                         }]
            }]

input = [1, 2, 3, [4], (1, (7, ((9)))), [[[[[[[[[5]]]]]]]]], 'a', 'l', [['[']]]

def json_readFromFile_FlattenListOfDicts(filepath='./JsonFile.json'):
    import json
    data_ = {}
    with open(filepath, 'r', encoding='utf-8') as fi:
        data_ = json.load(fi)
    import pandas
    ##flatten nested dicts with seperators
    #defualt seperator is .
    df = pandas.io.json.json_normalize(data_) ##have a consistent list of dicts for json normalize, else a dict of nested dicts
    #wont work on a list of random dicts
    print(df.to_dict(orient='records')[0]) ##records means list like format


def flatten_listOfListsnTuples(nested):
    for item in nested:
        if isinstance(item, Iterable) and not isinstance(item, (str, bytes)):
            yield from flatten_listOfListsnTuples(item)
        else:
            yield item

if __name__ == '__main__':
    from pprint import pprint
    pprint(list(flatten_listOfListsnTuples(input)))

    ##################################################################
    #Method 2
    from functools import reduce
    import operator
    #one liner for flattening list of lists, tuples, strings-- not for dict/json objects
    flatten = lambda l: reduce(lambda x, y:operator.add(x, y), map(flatten, l), []) if isinstance(l, Iterable) \
                                                                                       and not isinstance(l, (str,bytes)) else [l]

    print(flatten(input))

    #######################################################################

    json_readFromFile_FlattenListOfDicts()