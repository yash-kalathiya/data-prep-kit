from blocklist_transform import (
    BlockListTransformConfiguration,
    blocked_domain_list_path_key,
)
from data_processing.test_support.ray import AbstractTransformLauncherTest


class TestRayBlocklistTransform(AbstractTransformLauncherTest):
    """
    Extends the super-class to define the test data for the tests defined there.
    The name of this class MUST begin with the word Test so that pytest recognizes it as a test class.
    """

    def get_test_transform_fixtures(self) -> list[tuple]:
        basedir = "../test-data/"
        config = {
            # When running in ray, our Runtime's get_transform_config() method  will load the domains using
            # the orchestrator's DataAccess/Factory. So we don't need to provide the bl_local_config configuration.
            # "bl_local_config": {"input_folder": "/tmp", "output_folder": "/tmp"},
            blocked_domain_list_path_key: "../test-data/domains/arjel",
        }
        fixtures = [(BlockListTransformConfiguration(), config, basedir + "input", basedir + "expected")]
        return fixtures