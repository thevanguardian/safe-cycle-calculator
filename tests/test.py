import unittest
from main import find_optimal_ips_to_remove

class TestFindOptimalIpsToRemove(unittest.TestCase):
    def test_find_optimal_ips_to_remove(self):
        ip_app_dict = {
            '1.1.1.10': ['app_alpha', 'app_beta'],
            '1.1.1.11': ['app_gamma'],
            '1.1.1.12': ['app_delta', 'app_alpha'],
            '1.1.1.13': ['app_beta', 'app_gamma', 'app_delta'],
            '1.1.1.14': ['app_alpha', 'app_gamma'],
            '1.1.1.15': ['app_beta', 'app_delta'],
            '1.1.1.16': ['app_alpha', 'app_beta', 'app_gamma'],
            '1.1.1.17': ['app_gamma', 'app_delta'],
            '1.1.1.18': ['app_alpha'],
            '1.1.1.19': ['app_beta', 'app_gamma', 'app_alpha', 'app_delta']
        }
        removed_ips = find_optimal_ips_to_remove(ip_app_dict, 50)
        self.assertIsInstance(removed_ips, list)
        self.assertTrue(len(removed_ips) > 0)

if __name__ == '__main__':
    unittest.main()
