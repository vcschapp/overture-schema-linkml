import click
import os
from linkml.utils.generator import Generator, shared_arguments
from linkml_runtime.linkml_model.meta import SchemaDefinition


class GeoJsonSchemaGenerator(Generator):
    generatorname = os.path.basename(__file__)
    uses_schemaloader = False
    file_extension = "json"
    valid_formats = ["json"]

    def __init__(self, schema: SchemaDefinition, **kwargs):
        super().__init__(schema, **kwargs)

    def serialize(self, **kwargs) -> str:
        return "# Hello from GeoJson generator!\n"


@shared_arguments(GeoJsonSchemaGenerator)
@click.command(name="GeoJson")
def cli(yamlfile, **kwargs):
    """Generate GeoJSON-flavored JSON Schema representation of a LinkML model"""
    print(GeoJsonSchemaGenerator(yamlfile, **kwargs).serialize(**kwargs))


if __name__ == "__main__":
    cli()
