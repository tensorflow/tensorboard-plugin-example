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
"""Simple demo which writes a bunch of toy metrics to events file in various run directories for tensorboard to read"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os.path
import random

import tensorflow as tf
import paramplot_summary

# Directory into which to write tensorboard data.
LOGDIR = '/tmp/paramplotdemo'

def run(logdir, run_name, tag_value_map):
  """Greet several characters from a given cartoon."""

  tf.reset_default_graph()

  placeholders = {tag: tf.placeholder(tf.float32) for tag in tag_value_map}
  summary_ops = {tag: paramplot_summary.op(tag, placeholders[tag]) for tag in tag_value_map}

  writer = tf.summary.FileWriter(os.path.join(logdir, run_name))

  # Write the value under the final_loss summary for that particular run
  with tf.Session() as session:
    for tag_name in tag_value_map:
      summary = session.run(summary_ops[tag_name], feed_dict={placeholders[tag_name]: tag_value_map[tag_name]})
      writer.add_summary(summary)

  writer.close()

def run_all(logdir, run_names, tag_value_maps, unused_verbose=False):
  """Run the simulation for every logdir.
  """
  for run_name in run_names:
    run(logdir, run_name, tag_value_maps[run_name])


def main(unused_argv):
  print('Saving output to %s.' % LOGDIR)

  runs = ["run1", "run2", "run3", "run4", "run5"]
  tag_value_maps = {
    "run1": {
      "final_loss": random.uniform(0, 12),
      "correlation_validation_train": random.random()
    },
    "run2": {
      "final_loss": random.uniform(0, 12),
      "correlation_validation_train": random.random()
    },
    "run3": {
      "final_loss": random.uniform(0, 12),
      "correlation_validation_train": random.random()
    },
    "run4": {
      "final_loss": random.uniform(0, 12),
      "correlation_validation_train": random.random()
    },
    "run5": {
      "final_loss": random.uniform(0, 12),
      "correlation_validation_train": random.random()
    },
  }
  run_all(LOGDIR, runs, tag_value_maps, unused_verbose=True)
  print('Done. Output saved to %s.' % LOGDIR)


if __name__ == '__main__':
  tf.app.run()
