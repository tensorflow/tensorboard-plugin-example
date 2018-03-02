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
"""Simple demo which greets several people."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os.path

import tensorflow as tf

import greeter_summary

# Directory into which to write tensorboard data.
LOGDIR = '/tmp/greeter_demo'


def run(logdir, run_name, characters, extra_character):
  """Greet several characters from a given cartoon."""

  tf.reset_default_graph()

  input_ = tf.placeholder(tf.string)

  summary_op = greeter_summary.op("greetings", input_)

  writer = tf.summary.FileWriter(os.path.join(logdir, run_name))

  sess = tf.Session()

  for character in characters:
    summary = sess.run(summary_op, feed_dict={input_: character})
    writer.add_summary(summary)

  # Demonstrate that we can also add summaries without using the
  # TensorFlow session or graph.
  summary = greeter_summary.pb("greetings", extra_character)
  writer.add_summary(summary)

  writer.close()



def run_all(logdir, unused_verbose=False):
  """Run the simulation for every logdir.
  """
  run(logdir, "steven_universe", ["Garnet", "Amethyst", "Pearl"], "Steven")
  run(logdir, "futurama", ["Fry", "Bender", "Leela"],
      "Lrrr, ruler of the planet Omicron Persei 8")


def main(unused_argv):
  print('Saving output to %s.' % LOGDIR)
  run_all(LOGDIR, unused_verbose=True)
  print('Done. Output saved to %s.' % LOGDIR)


if __name__ == '__main__':
  tf.app.run()
