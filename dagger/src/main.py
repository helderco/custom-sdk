import dagger
from dagger import dag, field, function, object_type


@object_type
class CustomSdk:
    sdk_source_dir: dagger.Directory = field()
    required_paths: list[str] = field(default=list)

    @function
    def module_runtime(self, mod_source: dagger.ModuleSource, introspection_json: str) -> dagger.Container:
        return dag.python_sdk(sdk_source_dir=self.sdk_source_dir).module_runtime(mod_source, introspection_json)

    @function
    def codegen(self, mod_source: dagger.ModuleSource, introspection_json: str) -> dagger.GeneratedCode:
        return dag.python_sdk(sdk_source_dir=self.sdk_source_dir).codegen(mod_source, introspection_json)

