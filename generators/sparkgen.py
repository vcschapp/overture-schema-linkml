import click
import os
from linkml.utils.generator import Generator, shared_arguments
from linkml_runtime.linkml_model.meta import SchemaDefinition


class SparkSchemaGenerator(Generator):
    generatorname = os.path.basename(__file__)
    uses_schemaloader = False
    file_extension = "json"
    valid_formats = ["json"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def serialize(self, **kwargs) -> str:
        return "# Hello from Spark generator!\n"


@shared_arguments(SparkSchemaGenerator)
@click.command(name="spark")
def cli(yamlfile, **kwargs):
    """Generate Spark schema representation of a LinkML model"""
    print(SparkSchemaGenerator(yamlfile, **kwargs).serialize(**kwargs))


if __name__ == "__main__":
    cli()
