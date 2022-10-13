# Changelog

### 1.3 (2022-10-13)

- `create_file()`, `create_dir()`, `add_real_file()`, and `add_real_directory()`
  now also work with Path instances
- fixed `FakeFS.add_real_path()`
- fix requirement of pyfakefs when using Python 2

### 1.2 (2020-09-01)

- add FakeFS `.add_real_path()` and `.add_real_paths()`

### 1.1 (2019-08-20)

- ability to pass `kwargs` to pyfakefs' `Patcher` via `FakeFS.set_up()`

### 1.0 (2018-08-20)

- initial release of separate package
