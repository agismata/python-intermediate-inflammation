import numpy as np
import unittest
from functools import reduce

def attach_names(data,names):
    """ Attach names to a patient dataset"""
    output = []
    for i in range(len(data)):
        output.append({
                        'name': names[i],
                        'data': data[i]
                        })

    return output

def attach_names_better (data, names):
    """Create datastructure containing patient records."""
    assert len(data) == len(names)
    output = []

    for data_row, name in zip(data, names):
        output.append({'name': name,
                       'data': data_row})

    return output


data = np.array([[1., 2., 3.],
                 [4., 5., 6.]])
print(data)
output = attach_names_better(data, ['Alice', 'Bob'])
print(output)


def append_item_1(a_list, item):
    a_list.append(item)
    return a_list

def append_item_2(a_list, item):
    result = a_list + [item]
    return result

a_list=[]
print(append_item_1(a_list,'new'))
print(append_item_1(a_list,'second'))
a_list=[]
print(append_item_2(a_list,'new'))
print(append_item_2(a_list,'second'))

class RandomTest(unittest.TestCase):
    def test_random_numpy(self):
        mean = 5
        sdev = 3
        sample_size = 1000000

        sample = np.random.normal(mean, sdev, sample_size)

        self.assertAlmostEqual(mean, np.mean(sample), places=2)
        self.assertAlmostEqual(sdev, np.std(sample), places=2)

def add_one(num):
    return num + 1

def add_ones(in_list):
    return [add_one(x) for x in in_list]

result = add_ones([0, 1, 2])
print(result)

def sum_of_squares(l):
    print([x(0) for x in l])
    integers = [int(x) for x in l if x != '#']
    squares = [x * x for x in integers]
    return reduce(lambda a, b: a + b, squares)

print(sum_of_squares([0]))
print(sum_of_squares([1]))
print(sum_of_squares([1, 2, 3]))
print(sum_of_squares([-1]))
print(sum_of_squares([-1, -2, -3]))

print(sum_of_squares(['1', '2', '3']))
print(sum_of_squares(['-1', '-2', '-3']))
print(' ')
print(sum_of_squares(['1', '2', '3']))
print(sum_of_squares(['-1', '-2', '-3']))
print(sum_of_squares(['1', '2', '#100', '3']))