from urllib import request
import toml
from project import Project


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")

        parsed_toml = toml.loads(content)

        tool = parsed_toml["tool"]

        poetry = tool["poetry"]

        project_name = poetry["name"]
        project_description = poetry["description"]
        project_dependencies = poetry["dependencies"]
        project_dev_dependencies = poetry["group"]["dev"]["dependencies"]


        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(project_name, project_description, project_dependencies, project_dev_dependencies)
