# Copyright 2017 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os
import sys

from tensorboard import default
from tensorboard import program
import tensorflow as tf

from greeter_plugin import greeter_plugin


if __name__ == '__main__':
  plugins = default.get_plugins() + [greeter_plugin.GreeterPlugin]
  assets = os.path.join(tf.resource_loader.get_data_files_path(), 'assets.zip')
  tensorboard = program.TensorBoard(plugins, lambda: open(assets, 'rb'))
  tensorboard.configure(sys.argv)
  sys.exit(tensorboard.main())
