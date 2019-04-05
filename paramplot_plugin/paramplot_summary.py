# Copyright 2017 The TensorFlow Authors. All Rights Reserved.
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
# ==============================================================================
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import tensorflow as tf


PLUGIN_NAME = 'paramplot'


def op(name,
       value,
       display_name=None,
       description=None,
       collections=None):
  """Create a TensorFlow summary op to record data associated with a particular the given guest.

  Arguments:
    name: A name for this summary operation.
    guest: A rank-0 string `Tensor`.
    display_name: If set, will be used as the display name
      in TensorBoard. Defaults to `name`.
    description: A longform readable description of the summary data.
      Markdown is supported.
    collections: Which TensorFlow graph collections to add the summary
      op to. Defaults to `['summaries']`. Can usually be ignored.
  """

  # The `name` argument is used to generate the summary op node name.
  # That node name will also involve the TensorFlow name scope.
  # By having the display_name default to the name argument, we make
  # the TensorBoard display clearer.
  if display_name is None:
    display_name = name

  # We could pass additional metadata other than the PLUGIN_NAME within the
  # plugin data by using the content parameter, but we don't need any metadata
  # for this simple example.
  summary_metadata = tf.SummaryMetadata(
      display_name=display_name,
      summary_description=description,
      plugin_data=tf.SummaryMetadata.PluginData(
          plugin_name=PLUGIN_NAME))

  # Return a summary op that is properly configured.
  return tf.summary.tensor_summary(
      name,
      value,
      summary_metadata=summary_metadata,
      collections=collections)

