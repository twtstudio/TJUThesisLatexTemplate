#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
import shutil


def isCache(file_name):
    portion = os.path.splitext(file_name)
    cache_file_extensions = ['.aux', '.log', '.out', '.thm', '.toc', '.bbl', '.blg', '.fdb_latexmk', '.fls', '.gz']
    if portion[1] in cache_file_extensions:
        return True
    else:
        return False


def run():
    root_directory = os.path.split(os.path.realpath(__file__))[0]
    os.chdir(root_directory)

    # clean
    for folder_name in os.listdir('.'):
        if os.path.isdir(os.path.join(root_directory, folder_name)):
            os.chdir(os.path.join(root_directory, folder_name))
            for file_name in os.listdir('.'):
                if isCache(file_name):
                    os.remove(os.path.join(os.getcwd(), file_name))
            os.chdir(root_directory)
        else:
            if isCache(folder_name):
                os.remove(os.path.join(os.getcwd(), folder_name))

    print 'All log files cleaned.'


if __name__ == '__main__':
    run()
