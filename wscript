#!/usr/bin/env python

SUPPORTED_PLATFORMS = ["win32", "msys", "cygwin", "linux", "darwin"]

import sys
import os

if sys.platform not in SUPPORTED_PLATFORMS:
    raise Exception("Your platform is not supported!")

top = "."
out = "bin"

sources = ["breakpad_test.cpp"]

from waflib.Tools import compiler_cxx
compiler_cxx.cxx_compiler = {"default": ["clang++"]}  # force clang

def options(opt):
    opt.load("compiler_cxx")

def configure(conf):
    conf.load("compiler_cxx")

    conf.env.CXXFLAGS = ["-pedantic", "-Wall", "-Wextra", "-Wshadow",
                       "-Wstrict-overflow", "-Werror", "-std=c++1z",
                       "-O2", "-fno-strict-aliasing",
                       "--system-header-prefix=client/linux/handler/"]

    conf.check_cfg(package="breakpad-client", args=["--cflags", "--libs"], 
                   uselib_store="breakpad-client")

def build(bld):
    bld.program(features="cxx cxxprogram", source=sources, target="app",
                use=["breakpad-client"], lib="stdc++fs")
    bld.program(features="cxx cxxprogram", source=sources, target="app_debug",
                use=["breakpad-client"], lib="stdc++fs", cxxflags=["-g"])