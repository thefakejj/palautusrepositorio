class Project:
    def __init__(self, name, description, proj_license, authors, dependencies, dev_dependencies):
        self.name = name
        self.description = description
        self.proj_license = proj_license
        self.authors = authors
        self.dependencies = dependencies
        self.dev_dependencies = dev_dependencies

    def _bullet_point_list(self, data):
        if len(data) > 0:
            bullet_point = ""
            for element in data:
                bullet_point += f"\n- {element}"
            return bullet_point
        return "-"

    def __str__(self):
        return (
            f"Name: {self.name}"
            f"\nDescription: {self.description or '-'}"
            f"\nLicense: {self.proj_license or '-'}"
            f"\n"
            f"\nAuthors: {self._bullet_point_list(self.authors)}"
            f"\n"
            f"\nDependencies: {self._bullet_point_list(self.dependencies)}"
            f"\n"
            f"\nDevelopment dependencies: {self._bullet_point_list(self.dev_dependencies)}"
        )
