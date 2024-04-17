# (C) Copyright IBM Corp. 2024.
# Licensed under the Apache License, Version 2.0 (the “License”);
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#  http://www.apache.org/licenses/LICENSE-2.0
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an “AS IS” BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
################################################################################

import os

from blocklist_transform import (
    BlockListTransformConfiguration,
    annotation_column_name_cli_param,
    annotation_column_name_default,
    blocked_domain_list_path_cli_param,
    source_column_name_default,
    source_url_column_name_cli_param,
)
from data_processing.test_support.ray import AbstractTransformLauncherTest
from data_processing.utils import ParamsUtils


class TestRayBlocklistTransform(AbstractTransformLauncherTest):
    """
    Extends the super-class to define the test data for the tests defined there.
    The name of this class MUST begin with the word Test so that pytest recognizes it as a test class.
    """

    def get_test_transform_fixtures(self) -> list[tuple]:
        basedir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../test-data"))
        config = {
            # When running in ray, our Runtime's get_transform_config() method  will load the domains using
            # the orchestrator's DataAccess/Factory. So we don't need to provide the bl_local_config configuration.
            blocked_domain_list_path_cli_param: os.path.abspath(
                os.path.join(os.path.dirname(__file__), "../test-data/domains/arjel")
            ),
            annotation_column_name_cli_param: annotation_column_name_default,
            source_url_column_name_cli_param: source_column_name_default,
        }
        fixtures = [(BlockListTransformConfiguration(), config, basedir + "/input", basedir + "/expected")]
        return fixtures