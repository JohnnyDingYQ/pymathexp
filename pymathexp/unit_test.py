from pymathexp.shunting_yard import shunting_yard
from pymathexp.rpn_parse import rpn_parse

import json


def unit_test(function, test_data: list):
    for data in test_data:

        given = data.get("input")
        given_str = str(given)
        expected = data.get("expected")
        expected_str = str(expected)
        result = function(given)

        if result != expected:
            print("{} - {} is expected but {} is given".format(
                given_str,
                expected_str,
                str(result)
            ))

    print("Unit testing for {} has ended".format(function.__name__))


path = "pymathexp/unit_test_data.json"
data = json.load(open(path))

shunting_yard_data = data.get("shunting_yard")
unit_test(shunting_yard, shunting_yard_data)

rpn_parse_data = data.get("rpn_parse")
unit_test(rpn_parse, rpn_parse_data)