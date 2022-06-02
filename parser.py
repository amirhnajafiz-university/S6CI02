"""
Parser get rules method reads the rules files and returns the rules.
"""


import simplejson


AND_OPERATOR = 'AND'
OR_OPERATOR = 'OR'


def atomic_trim(input):
    return input.replace("(", "").replace(")", "").split(" IS ")


def getRules():
    with open('rules.fcl', 'r') as file:
        # create a dict
        res = []

        lines = file.readlines()
        for line in lines:
            # check for empty line
            if line == "\n":
                continue
            # create a dict
            line_info = {}
            # remove the before IF
            removeIF = line.strip().replace(";", "").split("IF")[1].strip()
            # split into two parts by then
            parts = removeIF.split(" THEN ")
            # the rules check
            rules = []
            if AND_OPERATOR in parts[0]:
                line_info['type'] = 'MIN'
                two = parts[0].split(" " + AND_OPERATOR + " ")
                rules.append(atomic_trim(two[0]))
                rules.append(atomic_trim(two[1]))
            elif OR_OPERATOR in parts[0]:
                line_info['type'] = 'MAX'
                two = parts[0].split(" " + OR_OPERATOR + " ")
                rules.append(atomic_trim(two[0]))
                rules.append(atomic_trim(two[1]))
            else:
                line_info['type'] = 'NONE'
                rules.append(atomic_trim(parts[0]))
            # result
            line_info['rules'] = rules
            line_info['output'] = parts[1].split(" IS ")[1]

            res.append(line_info)

        return res


print(simplejson.dumps(getRules(), sort_keys=True, indent=4, use_decimal=True))
