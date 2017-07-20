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

import datetime

from tensorboard.backend import http_util
from tensorboard.plugins import base_plugin
from werkzeug import wrappers


class MyPlugin(base_plugin.TBPlugin):
  """Example plugin for TensorBoard."""

  plugin_name = 'my-plugin'

  def __init__(self, context):
    """Instantiates MyPlugin via TensorBoard core.

    Args:
      context: A magic container of TensorBoard state.

    :type context: base_plugin.TBContext
    """
    self._multiplexer = context.multiplexer

  # @Override
  def get_plugin_apps(self):
    return {'/time': self.handle_time_request}

  # @Override
  def is_active(self):
    return True

  @wrappers.Request.application
  def handle_time_request(self, request):
    """Sends formatted ISO 8601 timestamp to browser.

    :type request: wrappers.Request
    """
    response = {'time': str(datetime.datetime.now())}
    return http_util.Respond(request, response, 'application/json')
