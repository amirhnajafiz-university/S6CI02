import simplejson
from parser import getRules, AND_OPERATOR, OR_OPERATOR


"""
Begin method will get our inputs and will
return answers.
"""
def begin(inputs):
    # getting the rules
    rules = getRules()
    print(simplejson.dumps(rules, sort_keys=True, indent=4, use_decimal=True))
    print(inputs)

    # creating a results set
    results = []
    for rule in rules:
        if rule.get('type') == "NONE":
            temp = {}
            temp['result'] = rule.get('output')
            temp['score'] = inputs.get(rule.get('rules')[0][0]).get(rule.get('rules')[0][1])
            results.append(temp)
        else:
            temp = {}
            temp['result'] = rule.get('output')
            v1 = inputs.get(rule.get('rules')[0][0]).get(rule.get('rules')[0][1])
            v2 = inputs.get(rule.get('rules')[1][0]).get(rule.get('rules')[1][1])
            if rule.get('type') == AND_OPERATOR:
                temp['score'] = min(v1, v2)
            elif rule.get('type') == OR_OPERATOR:
                temp['score'] = max(v1, v2)
            results.append(temp)
    
    return results
