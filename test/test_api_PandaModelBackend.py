import unittest
from grid2op.tests.aaa_test_backend_interface import AAATestBackendAPI


from grid2op.Backend import PandaModelsBackend

class TestBackendAPI_PandaPowerBackend(AAATestBackendAPI, unittest.TestCase):
    def make_backend(self, detailed_infos_for_cascading_failures=False):
        return PandaModelsBackend(detailed_infos_for_cascading_failures=detailed_infos_for_cascading_failures)


if __name__ == "__main__":
    unittest.main()
