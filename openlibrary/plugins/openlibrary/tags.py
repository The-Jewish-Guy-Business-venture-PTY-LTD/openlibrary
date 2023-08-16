from infogami.utils.view import public
import web
import json


@public
def load_plugin_json(plugins_str):
    return json.loads(plugins_str)


@public
def display_plugins_data(data):
    plugin_type = list(data.keys())[0]
    # Split the string into key-value pairs
    parameters = data[plugin_type].split(',')

    # Create a dictionary to store the formatted parameters
    plugin_fields = []

    # Iterate through the pairs and extract the key-value information
    for pair in parameters:
        try:
            key, value = pair.split('=', 1)
            key = key.strip()
            plugin_fields.append(f'{key}={value}')
        except ValueError:
            plugin_fields.append(pair)

    plugin_data = ', '.join(plugin_fields)

    return plugin_type, plugin_data


@public
def get_tag_types():
    return ["subject", "work", "collection"]


@public
def get_plugin_types():
    return ["RelatedSubjects", "QueryCarousel", "ListCarousel"]


def setup():
    pass