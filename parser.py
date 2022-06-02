"""
Parser get rules method reads the rules files and returns the rules.
"""
def getRules():
    with open('rules.fcl', 'r') as file:
        lines = file.readlines()
        for line in lines:
            # check for empty line
            if line == "\n":
                continue
            # remove the before IF
            removeIF = line.strip().replace(";", "").split("IF")[1].strip()
            # split into two parts by then
            parts = removeIF.split(" THEN ")
            # result
            res = parts[1].split(" IS ")
            print(res[1])

getRules()