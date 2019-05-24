#!/bin/sh
find -E $(dirname "$0") -regex ".*\.(aux|log|out|thm|toc|bbl|blg|fdb_latexmk|fls|gz)" -delete
