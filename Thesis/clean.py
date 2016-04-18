#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
import shutil


def run():
    root_directory = os.path.split(os.path.realpath(__file__))[0]
    os.chdir(root_directory)
    # os.system('xelatex tjumain.tex')
    # os.system('xelatex tjumain.tex')

    # clean
    for folder_name in os.listdir('.'):
        if os.path.isdir(os.path.join(root_directory, folder_name)):
            os.chdir(os.path.join(root_directory, folder_name))
            for file_name in os.listdir('.'):
                portion = os.path.splitext(file_name)
                if portion[1] == '.aux' or portion[1] == '.log' or portion[1] == '.out' or portion[1] == '.thm' or portion[1] == '.toc' or portion[1] == '.bbl' or portion[1] == '.blg' or portion[1] == '.fdb_latexmk' or portion[1] == '.fls' or portion[1] == '.gz':
                    os.remove(os.path.join(os.getcwd(), file_name))
            os.chdir(root_directory)
        else:
            portion = os.path.splitext(folder_name)
            if portion[1] == '.aux' or portion[1] == '.log' or portion[1] == '.out' or portion[1] == '.thm' or portion[1] == '.toc' or portion[1] == '.bbl' or portion[1] == '.blg' or portion[1] == '.fdb_latexmk' or portion[1] == '.fls' or portion[1] == '.gz':
                os.remove(os.path.join(os.getcwd(), folder_name))

    print 'All log files cleaned.'


if __name__ == '__main__':
    run()