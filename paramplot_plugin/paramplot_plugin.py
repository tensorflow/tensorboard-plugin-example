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

import json
import tensorflow as tf
from werkzeug import wrappers

from tensorboard.backend import http_util
from tensorboard.backend.event_processing import event_multiplexer
from tensorboard.plugins import base_plugin

class ParamPlotPlugin(base_plugin.TBPlugin):
  """A plugin that serves greetings recorded during model runs."""

  # This static property will also be included within routes (URL paths)
  # offered by this plugin. This property must uniquely identify this plugin
  # from all other plugins.
  plugin_name = 'paramplot'

  def __init__(self, context: base_plugin.TBContext):
    """Instantiates a ParamPlotPlugin.

    Args:
      context: A base_plugin.TBContext instance. A magic container that
        TensorBoard uses to make objects available to the plugin.
    """
    # We retrieve the multiplexer from the context and store a reference
    # to it.
    self._multiplexer: event_multiplexer.EventMultiplexer = context.multiplexer
    self._context = context

    # Read in the runparams.json file
    runparams_path = self._context.flags.runParamsPath
    with open(runparams_path, 'r') as read_file:
      self._runparams_json = json.load(read_file.read())


  def define_flags(self, parser):
    parser.add_argument(
        '--runParamsPath',
        metavar='RPPATH',
        type=str,
        default='./runparams.json',
        help='Provide the full path to the runparams file which contains the mappings from runs to paramater settings as recognised by ParamPlot e.g. --runParamsPath=/tmp/log/runparam.json')

  def _get_valid_runs(self):
    return [run.run_name for run in self._multiplexer.Runs() if run.run_name in self._runparams_json]

  @wrappers.Request.application
  def tags_route(self, request):
    """A route (HTTP handler) that returns a response with tags.

    Returns:
      A response that contains a JSON object. The keys of the object
      are all the runs. Each run is mapped to a (potentially empty)
      list of all tags that are relevant to this plugin.
    """
    # This is a dictionary mapping from run to (tag to string content).
    # To be clear, the values of the dictionary are dictionaries.
    all_runs = self._multiplexer.PluginRunToTagToContent(
        ParamPlotPlugin.plugin_name)

    # tagToContent is itself a dictionary mapping tag name to string
    # content. We retrieve the keys of that dictionary to obtain a
    # list of tags associated with each run.
    response = {
        run: list(tagToContent.keys())
        for (run, tagToContent) in all_runs.items()
    }
    return http_util.Respond(request, response, 'application/json')

  def get_plugin_apps(self):
    """Gets all routes offered by the plugin.

    This method is called by TensorBoard when retrieving all the
    routes offered by the plugin.

    Returns:
      A dictionary mapping URL path to route that handles it.
    """
    # Note that the methods handling routes are decorated with
    # @wrappers.Request.application.
    return {
        '/tags': self.tags_route,
        '/rundata': self._runparams_route,
        '/paramdatabytag': self._paramdatabytag_route,
    }

  def is_active(self):
    """Determines whether this plugin is active.

    This plugin is only active if there are runs in the runparams file which intersect with the available runs being monitored in the logdir

    Returns:
      Whether this plugin is active.
    """
    if not self._multiplexer:
      return False

    # The plugin is active if there are any runs in the runparam dictionary which are in the logdir
    return bool(any(self._get_valid_runs()))

  def _process_tensor_event(self, event):
    """Convert a TensorEvent into a JSON-compatible response."""
    data_arr = tf.make_ndarray(event.tensor_proto)
    return {
        'wall_time': event.wall_time,
        'step': event.step,
        'data': data_arr,
    }
  
  def _get_tensor_events_payload(self, run, tag):
    # We fetch all the tensor events that contain greetings.
    tensor_events = self._multiplexer.Tensors(run, tag)

    # Convert the tensor data to an nd array for processing on the frontend.
    return [self._process_tensor_event(ev) for ev in tensor_events]
  
  @wrappers.Request.application
  def _runparams_route(self, request):
    """A route which returns the runparams for a particular run along with the tag specific data

    Returns:
      A JSON object of the form:
      {
        runparams: ...,
        payload: [Events]
      }
    """

    run = request.args.get('run')
    tag = request.args.get('tag')

    response = {
      "runparams": self._runparams_json[run],
      "payload": self._get_tensor_events_payload(run, tag)
    }

    return http_util.Respond(request, response, 'application/json')
  
  @wrappers.Request.application
  def _paramdatabytag_route(self, request):
    """A route which for a given tag will return all the run data for that tag (for all runs which are labelled in the runparams file)
    as well as the parameter values associated with the given run

    Returns:
      A JSON object as the http response which will be of the form:
      {
        "run1": {
          payload: [Events...],
          paramaters: {
            num_layers: 3, 
            ...
          }
        },
        "run2": ...
      } 
    """
    tag = request.args.get('tag')

    # Fetch all the runs which are in the runparams file and get the intersection of those with the runs in the logdir
    valid_runs = self._get_valid_runs()

    response = {
      run: {
        "payload": self._get_tensor_events_payload(run, tag),
        "parameters": self._runparams_json[run]
      } for run in valid_runs
    }

    return http_util.Respond(request, response, 'application/json')


    

