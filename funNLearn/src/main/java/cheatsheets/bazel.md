## Why

* Correct
* Functional
* Isolated / Repeatable / Hermetic
* Icremental
* Fast (at scale)
* Composable
* Universal / Multi - platform
* Proven
* Scalable
* Extensible

## Configuration Files

* **WORKSPACE** : (or WORKSPACE. bazel) file at the top of a project / workspace
  + **name**: good to have a name for workspace
  ``` 
  workspace(name = "up_and_running")
  ```

  + **load**: is more like a import statement
  ``` bash
   # from @io_bazel_rules_go import go_register_toolchains and go_rules_dependencies
  
   load("@io_bazel_rules_go//go:deps.bzl", "go_register_toolchains", "go_rules_dependencies")
  ```

  + **@bazel_tools**: pile of inbuild tools from bazel
  + http_archive: tool to fetch files/dependencies from web

* **BUILD. bazel** : file at the top of each Bazel module (or BUILD); ideally 
maintained automatically

* **. bzl** : files to define macros and rules - to customize and extend the vocabulary 
available in the above files

* **. bazelrc** : at the same level as WORKSPACE file. used for specifying primarily 

two cache (repository_cache and disk_cache)

* **. bazelversion** : 

## Glossary

* **Gazelle** is a tool for auto-creating BUILD. bazel files for Go projects
