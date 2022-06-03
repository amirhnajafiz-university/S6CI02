from fuzz.fuzz import EFS
from decimal import Decimal


"""
this method will create our expert fuzzy system
with the parameters that we set.
"""
def create_system():
    # create a EFS instance
    f = EFS()

    # our parameters
    # -----
    f.NewParam('chest_pain').NewSession('typical_anginal').Range([1, 1, 1])
    f.Param('chest_pain').NewSession('atypical_anginal').Range([2, 2, 2])
    f.Param('chest_pain').NewSession('non_aginal_pain').Range([3, 3, 3])
    f.Param('chest_pain').NewSession('asymptomatic').Range([4, 4, 4])

    f.NewParam('sex').NewSession('male').Range([0, 0, 0])
    f.Param('sex').NewSession('female').Range([1, 1, 1])

    f.NewParam('exercise').NewSession('true').Range([1, 1, 1])
    f.Param('exercise').NewSession('false').Range([0, 0, 0])

    f.NewParam('age').NewSession('young').Range([29, 38, 29]).LeftValue(1)
    f.Param('age').NewSession('mild').Range([33, 45, 38])
    f.Param('age').NewSession('old').Range([40, 58, 48])
    f.Param('age').NewSession('very_old').Range([52, 60, 60]).RightValue(1)

    f.NewParam('blood_pressure').NewSession('low').Range([111, 134, 111]).LeftValue(1)
    f.Param('blood_pressure').NewSession('medium').Range([127, 153, 139])
    f.Param('blood_pressure').NewSession('high').Range([142, 172, 157])
    f.Param('blood_pressure').NewSession('very_high').Range([154, 171, 171]).RightValue(1)

    f.NewParam('blood_sugar').NewSession('true').Range([105, 120, 120]).RightValue(1)

    f.NewParam('cholestrol').NewSession('low').Range([151, 197, 151]).LeftValue(1)
    f.Param('cholestrol').NewSession('medium').Range([188, 250, 215])
    f.Param('cholestrol').NewSession('high').Range([217, 307, 263])
    f.Param('cholestrol').NewSession('very_high').Range([281, 347, 347]).RightValue(1)

    f.NewParam('heart_rate').NewSession('low').Range([100, 141, 100]).LeftValue(1)
    f.Param('heart_rate').NewSession('medium').Range([111, 194, 152])
    f.Param('heart_rate').NewSession('high').Range([152, 210, 210]).RightValue(1)

    f.NewParam('ecg').NewSession('normal').Range([0, 0.4, 0]).LeftValue(1)
    f.Param('ecg').NewSession('abnormal').Range([0.2, 1.4, 1])
    f.Param('ecg').NewSession('hypertrophy').Range([1.4, 1.9, 1.9]).RightValue(1)

    f.NewParam('old_peak').NewSession('low').Range([1, 2, 1]).LeftValue(1)
    f.Param('old_peak').NewSession('risk').Range([1.5, 4.2, 2.8])
    f.Param('old_peak').NewSession('terrible').Range([2.5, 4.1, 4.1]).RightValue(1)

    f.NewParam('thallium_scan').NewSession('normal').Range([3, 3, 3])
    f.Param('thallium_scan').NewSession('medium').Range([6, 6, 6])
    f.Param('thallium_scan').NewSession('high').Range([7, 7, 7])
    # -----

    return f


"""
fuzzify method will get our inputs and then
change them to fuzzy logic data.
"""
def fuzzify(input):
    system = create_system()
    res = {}

    for x in input.keys():
        res[x] = system.Input(x, Decimal(input.get(x)))
    
    return res
