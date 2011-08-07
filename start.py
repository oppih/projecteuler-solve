#!/usr/bin/env python

"""
This is written for the automation when starting a new problem.
"""

#problem = sys.argv[1]

# git checkout -b %s % problem
# mkdir ./%s % problem
# cp ./func_time.py ./%s/%s.py % (problem, problem)
# git add ./%s/%s.py % (problem, problem)
# git commit -am '%s added' % problem
# import webbrowser
# url = http://projecteuler.net/index.php?section=problems&id= + str(int(problem[1:]))
# webbrowser.open(url)

import subprocess, os, webbrowser

print "Welcome Message"

prompt = '<O.O><projecteuler:>'
which_start = "Which problem would you want to start?\ne.g. enter 12 if you want to solver 12th problem.\n"
problem = raw_input(which_start + prompt)

str_problem = "p0" + problem

url = "http://projecteuler.net/index.php?section=problems&id=" + problem

# git init
cmd_got_00 = "git checkout master"
subprocess.call(cmd_git_00, shell = True)
cmd_git_0 = "git checkout -b %s" % str_problem
subprocess.call(cmd_git_0, shell = True)

# make sure if the branch I want to creat is alraedy exits.
os.mkdir("./" + str_problem)
cmd0 = "cp ./func_time.py ./%s/%s.py" %(str_problem, str_problem)
subprocess.call(cmd0, shell = True)

cmd_git_1 = "git add ./%s/%s.py" %(str_problem, str_problem)
subprocess.call(cmd_git_1, shell = True)

cmd_git_2 = "git status"
subprocess.call(cmd_git_2, shell = True)

webbrowser.open_new_tab(url)

print "\n\nRemember, now your are in branch %s\n" % str_problem
