from tensorboard.plugins import base_plugin
from paramplot import paramplot_plugin

class ParamPlotLoader(base_plugin.TBLoader):
    def __init__(self):
        self._plugin_class = paramplot_plugin.ParamPlotPlugin
    
    def load(self, context):
        return self._plugin_class(context)
    
    def define_flags(self, parser):
        parser.add_argument(
            '--runParamsPath',
            metavar='RPPATH',
            type=str,
            default='./runparams.json',
            help='Provide the full path to the runparams file which contains the mappings from runs to paramater settings as recognised by ParamPlot e.g. --runParamsPath=/tmp/log/runparam.json')