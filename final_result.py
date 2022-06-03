from fuzzification import fuzzify
from inference import begin
from defuzzification import defuzzify

class ProvideResult(object):
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(ProvideResult, cls).__new__(cls)
        return cls.instance

    @staticmethod
    def get_final_result(input_dict: dict) -> str:
        f = fuzzify(input_dict)  # fuzzification
        print(f'[Fuzzify] len: {len(f)}')

        r = begin(f)  # inference
        print(r)

        d = defuzzify(r)  # defuzzification
        print(f'[Result] {d}')

        return d
