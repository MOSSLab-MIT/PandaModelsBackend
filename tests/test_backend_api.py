import unittest
from grid2op.tests.aaa_test_backend_interface import AAATestBackendAPI

from PandaModelsBackend import PandaModelsBackend

class TestBackendAPI_PandaModelsBackend(AAATestBackendAPI, unittest.TestCase):
    def make_backend(self, detailed_infos_for_cascading_failures=False):
        return PandaModelsBackend(detailed_infos_for_cascading_failures=detailed_infos_for_cascading_failures)


if __name__ == "__main__":
    unittest.main()
