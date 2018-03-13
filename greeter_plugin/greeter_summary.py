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
"""Simple demo which greets several people.

This module provides summaries for the Greeter plugin.
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import tensorflow as tf


PLUGIN_NAME = 'greeter'


def op(name,
       guest,
       display_name=None,
       description=None,
       collections=None):
  """Create a TensorFlow summary op to greet the given guest.

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

  message = tf.string_join(['Hello, ', guest, '!'])

  # Return a summary op that is properly configured.
  return tf.summary.tensor_summary(
      name,
      message,
      summary_metadata=summary_metadata,
      collections=collections)


def pb(tag, guest, display_name=None, description=None):
  """Create a greeting summary for the given guest.

  Arguments:
    tag: The string tag associated with the summary.
    guest: The string name of the guest to greet.
    display_name: If set, will be used as the display name in
      TensorBoard. Defaults to `tag`.
    description: A longform readable description of the summary data.
      Markdown is supported.
    """
  message = 'Hello, %s!' % guest
  tensor = tf.make_tensor_proto(message, dtype=tf.string)

  # We have no metadata to store, but we do need to add a plugin_data entry
  # so that we know this summary is associated with the greeter plugin.
  # We could use this entry to pass additional metadata other than the
  # PLUGIN_NAME by using the content parameter.
  summary_metadata = tf.SummaryMetadata(
      display_name=display_name,
      summary_description=description,
      plugin_data=tf.SummaryMetadata.PluginData(
          plugin_name=PLUGIN_NAME))

  summary = tf.Summary()
  summary.value.add(tag=tag,
                    metadata=summary_metadata,
                    tensor=tensor)
  return summary
