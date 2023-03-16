#!flask/bin/python

# Update the package list
subprocess.call([ 'update'])

# Upgrade the installed package
subprocess.call([ 'upgrade'])


subprocess.call([ 'apt, install, haproxy'])
