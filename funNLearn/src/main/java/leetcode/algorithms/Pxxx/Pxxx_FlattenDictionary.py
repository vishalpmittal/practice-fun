"""
    Tag: recursive

    Given a dictionary, or json, that might have nested dictionary or jsons
    Flatten that into one level dictionary/json
    
    Input : {
        'a' : {'b': 1},
        'c' : {'d': {'e': 2, 'f':3}},
        'g' : 4
    }

    Output: 
    {
        'a_b': 1,
        'c_d_e' : 2,
        'c_d_f' : 3, 
        'g' : 4
    }
"""


class Solution(object):
    spacer = '_'

    @staticmethod
    def flatten_dict(dict_of_dict):
        """
        :param dict_of_dict: can be any level of nested dictionary
        :return: returns a dictionary of 1 level with appended keys and respective values
        """
        if not dict_of_dict or not isinstance(
                dict_of_dict, dict) or len(dict_of_dict) == 0:
            return dict_of_dict

        fl_dict = dict()
        Solution._fd_helper(fl_dict, dict_of_dict)
        return fl_dict

    @staticmethod
    def _fd_helper(fl_dict, prev_value, prev_key=''):
        """
        Recursive helper method for flatten_dict
        """
        if not isinstance(prev_value, dict):
            fl_dict[prev_key] = prev_value
        else:
            for sub_key, sub_val in prev_value.iteritems():
                if prev_key:
                    new_key = '{}{}{}'.format(prev_key, Solution.spacer, sub_key)
                else:
                    new_key = '{}{}'.format(prev_key, sub_key)
                Solution._fd_helper(fl_dict, sub_val, new_key)


def test_code():
    in_dict = {'a' : {'b': 1}, 'c' : {'d': {'e': 2, 'f':3}}, 'g' : 4}
    assert Solution.flatten_dict(in_dict) == {
        'a_b': 1, 'c_d_e' : 2, 'c_d_f' : 3, 'g' : 4
    }


test_code()
