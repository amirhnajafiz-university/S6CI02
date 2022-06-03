from parser import getRules


"""
Begin method will get our inputs and will
return answers.
"""
def begin(inputs):
    # getting the rules
    rules = getRules()

    # creating a results set
    outputs = {}

    for rule in rules:
        # each rule has an result and score
        result = ""
        score = 0
        # check the rule type
        if rule.get('type') == "NONE":  # a single rule
            result = rule.get('output')
            score = inputs.get(rule.get('rules')[0][0]).get(rule.get('rules')[0][1])
        else:  # a complex rule
            result = rule.get('output')
            # calculating each parts value
            v1 = inputs.get(rule.get('rules')[0][0]).get(rule.get('rules')[0][1])
            v2 = inputs.get(rule.get('rules')[1][0]).get(rule.get('rules')[1][1])
            # check the complex rule type
            if rule.get('type') == "AND":  # for and we use min
                score = min(v1, v2)
            elif rule.get('type') == "OR":  # for or we use max
                score = max(v1, v2)
        
        # now we update the outputs
        if result in outputs.keys():
            outputs[result] = max(outputs[result], score)
        else:
            outputs[result] = score
    
    return outputs
