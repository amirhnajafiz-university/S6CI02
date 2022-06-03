import simplejson
from fuzz.fuzz import EFS


def initialize():
    # create a EFS instance
    f = EFS()

    # our parameters
    # -----
    f.NewParam('chest_pain').NewSession('typical_anginal').Range([1, 1, 1])
    f.With('chest_pain').NewSession('atypical_anginal').Range([2, 2, 2])
    f.With('chest_pain').NewSession('non_aginal_pain').Range([3, 3, 3])
    f.With('chest_pain').NewSession('asymptomatic').Range([4, 4, 4])

    f.NewParam('sex').NewSession('male').Range([0, 0, 0])
    f.With('sex').NewSession('female').Range([1, 1, 1])

    f.NewParam('exercise').NewSession('true').Range([1, 1, 1])
    f.With('exercise').NewSession('false').Range([0, 0, 0])

    f.NewParam('age').NewSession('young')
    f.With('age').NewSession('mid')
    f.With('age').NewSession('old')
    f.With('age').NewSession('veryold')

    f.NewParam('blood_pressure').NewSession('low')
    f.With('blood_pressure').NewSession('medium')
    f.With('blood_pressure').NewSession('high')
    f.With('blood_pressure').NewSession('veryhigh')

    f.NewParam('blood_sugar').NewSession('veryhigh')

    f.NewParam('cholesterol').NewSession('low')
    f.With('cholesterol').NewSession('medium')
    f.With('cholesterol').NewSession('high')
    f.With('cholesterol').NewSession('veryhigh')

    f.NewParam('heart_rate').NewSession('low')
    f.With('heart_rate').NewSession('medium')
    f.With('heart_rate').NewSession('high')

    f.NewParam('ecg').NewSession('normal')
    f.With('ecg').NewSession('abnormal')
    f.With('ecg').NewSession('hypertrophy')

    f.NewParam('old_peak').NewSession('low')
    f.With('old_peak').NewSession('risk')
    f.With('old_peak').NewSession('terrible')

    f.NewParam('thallium_scan').NewSession('normal').Range([3, 3, 3])
    f.With('thallium_scan').NewSession('medium').Range([6, 6, 6])
    f.With('thallium_scan').NewSession('high').Range([7, 7, 7])
    # -----

    return f


def fuzzify(input):
    system = initialize()
    res = {}

    for x in input.keys():
        res[x] = system.Input(x, input.get(x))
    
    return res
