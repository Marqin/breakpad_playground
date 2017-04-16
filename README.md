# breakpad-playground

**Tested only on Linux.**

Simple test of [https://github.com/google/breakpad](https://github.com/google/breakpad) 

Build depends on:
* python (for WAF)
* Breakpad (added to pkgconfig)
* clang 3.9+ and libstd++ with Filesystem TS support

Usage:
```sh
python ./waf configure build
sh ./prepare_symbols.sh bin/app_debug app
./bin/app
```

App will print path to minidump, `prepare_symbols.sh` will put symbols into `./symbols` directory.

Example (if you have breakpad tools in your PATH):
```sh
minidump_stackwalk ./some.dmp ./symbols
```