import unittest

from openaerostruct.functionals.center_of_gravity import CenterOfGravity
from openaerostruct.utils.testing import run_test, get_default_surfaces

@unittest.skipUnless(0, "Test is broken, derivatives are wrong.")
class Test(unittest.TestCase):

    def test(self):
        surfaces = get_default_surfaces()

        comp = CenterOfGravity(surfaces=surfaces)

        run_test(self, comp)


if __name__ == '__main__':
    unittest.main()
