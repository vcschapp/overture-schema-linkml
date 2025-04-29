"""
Main CLI entrypoint for Overture extensions to ``linkml`` executable
"""

import click

from generators.geojsongen import cli as gen_geojson
from generators.sparkgen import cli as gen_spark
from linkml.cli.main import linkml as cli
from linkml.cli.main import generate


generate.add_command(gen_geojson, name="geojson")
generate.add_command(gen_spark, name="spark")
