#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Copyspecial Assignment"""

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# give credits
__author__ = "Larry Scott with help from John"

import re
import os
import sys
import shutil
import subprocess
import argparse


def get_special_paths(dirname):
    """Given a dirname, returns a list of all its special files."""
    special_list = []
    the_paths = os.listdir(dirname)
    for name in the_paths:
        same = re.search(r'__(\w+)__', name)
        if same:
            special_list.append(os.path.abspath(os.path.join(dirname, name)))
    return special_list


def copy_to(path_list, dest_dir):
    """Copy the files to the directory."""
    if not os.path.isdir(dest_dir):
        os.makedirs(dest_dir)
    for path in path_list:
        shutil.copy(path, dest_dir)
    return


def zip_to(path_list, dest_zip):
    """Zip the files to a new zip file."""
    for path in path_list:
        subprocess.run(['zip', "-j", dest_zip, path])
    return


def main(args):
    """Main driver code for copyspecial."""
    # This snippet will help you get started with the argparse module.
    parser = argparse.ArgumentParser()
    parser.add_argument('--todir', help='dest dir for special files')
    parser.add_argument('--tozip', help='dest zipfile for special files')
    # TODO: add one more argument definition to parse the 'from_dir' argument
    parser.add_argument('from_dir', help='target dir for special files')
    ns = parser.parse_args(args)

    special_paths = get_special_paths(ns.from_dir)
    # TODO: you must write your own code to get the command line args.
    # Read the docs and examples for the argparse module about how to do this.
    if not sys.argv:
        parser.print_usage()
    if ns.todir:
        copy_to(special_paths, ns.todir)
    elif ns.tozip:
        zip_to(special_paths, ns.tozip)
    else:
        for path in special_paths:
            print(path)
    # Parsing command line arguments is a must-have skill.
    # This is input data validation. If something is wrong (or missing) with
    # any required args, the general rule is to print a usage message and
    # exit(1).

    # Your code here: Invoke (call) your functions


if __name__ == "__main__":
    main(sys.argv[1:])
