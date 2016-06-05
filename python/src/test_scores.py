import unittest
import collections

# Solution to https://programmingpraxis.com/2016/05/24/test-scores/


def average_scores(test_scores, top_n=5):
    d = collections.defaultdict(list)
    for name, score in test_scores:
        d[name].append(score)
    r = {}
    for name, scores in d.items():
        if len(scores) >= top_n:
            scores.sort(reverse=True)
            average = sum(scores[0:top_n]) / top_n
            r[name] = average
    return r


class Test(unittest.TestCase):

    def test_average_scores_for_empty_list(self):
        self.assertEqual({}, average_scores([]))

    def test_average_scores(self):
        test_scores = [('a', 10), ('a', 8), ('a', 9),
                       ('a', 10), ('a', 4), ('a', 9),
                       ('b', 10), ('b', 4), ('b', 4),
                       ('b', 4), ('b', 10), ('b', 1),
                       ('c', 5), ('c', 1), ('c', 10)]
        r = average_scores(test_scores)
        self.assertEqual(9, r['a'])
        self.assertEqual(6, r['b'])
        self.assertNotIn('c', r)

if __name__ == '__main__':
    unittest.main()
