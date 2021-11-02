import importlib.util
import logging
import os
import os.path
import sys


class PluginLoader:
    @staticmethod
    def getPlugins(path):
        plugins = []
        if not os.path.isdir(path):
            return plugins
        possibleplugins = os.listdir(path)
        for i in possibleplugins:
            location = os.path.join(path, i)
            if not os.path.isdir(location) or "__init__.py" not in os.listdir(location):
                continue
            plugins.append(i)
        return plugins

    @staticmethod
    def loadPlugin(basePath, pluginName):
        if basePath not in sys.path:
            sys.path.append(basePath)
        module = importlib.import_module(pluginName, basePath)

        try:
            plugin = module.Plugin()
        except Exception as e:
            logging.critical(
                "Couldn't load plugin because class Plugin is missing: "
                + pluginName
                + f" Original error was: {e}"
            )
            return
        return plugin
