"""
Parser get rules method reads the rules files and returns the rules.
"""

import simplejson


NORMAL = 'NONE'
AND_OPERATOR = 'AND'
OR_OPERATOR = 'OR'


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
            # check the AND
            if AND_OPERATOR in parts[0]:
                line_info['type'] = AND_OPERATOR
                two = parts[0].split(" " + AND_OPERATOR + " ")
                line_info['condition_1'] = two[0].replace("(", "").replace(")", "").split(" IS ")
                line_info['condition_2'] = two[1].replace("(", "").replace(")", "").split(" IS ")
            elif OR_OPERATOR in parts[0]:
                line_info['type'] = OR_OPERATOR
                two = parts[0].split(" " + OR_OPERATOR + " ")
                line_info['condition_1'] = two[0].replace("(", "").replace(")", "").split(" IS ")
                line_info['condition_2'] = two[1].replace("(", "").replace(")", "").split(" IS ")
            else:
                line_info['type'] = NORMAL
                line_info['condition_1'] = parts[0].replace("(", "").replace(")", "").split(" IS ")
            # result
            line_info['result'] = parts[1].split(" IS ")[1]

            res.append(line_info)

        return res


print(simplejson.dumps(getRules(), sort_keys=True, indent=4, use_decimal=True))
