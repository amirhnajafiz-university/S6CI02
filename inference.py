import simplejson
from parser import getRules


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
    results = {}
    for rule in rules:
        out = ""
        score = 0
        if rule.get('type') == "NONE":
            out = rule.get('output')
            score = inputs.get(rule.get('rules')[0][0]).get(rule.get('rules')[0][1])
        else:
            out = rule.get('output')
            v1 = inputs.get(rule.get('rules')[0][0]).get(rule.get('rules')[0][1])
            v2 = inputs.get(rule.get('rules')[1][0]).get(rule.get('rules')[1][1])
            if rule.get('type') == "AND":
                score = min(v1, v2)
            elif rule.get('type') == "OR":
                score = max(v1, v2)
        
        if score == None:
            score = 0
        
        if out in results.keys():
            results[out] = max(results[out], score)
        else:
            results[out] = score
    
    return results
