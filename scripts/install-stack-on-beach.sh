#! /bin/bash
#
# Install the WMT-EXE software stack.
#
# Install the entire software stack on beach.colorado.edu into the CURRENT
# DIRECTORY. This is really only specific to beach in the location of java.
#
# It's usually a good idea to run this script in a clean environment. However, there
# are a few environment variables that need to be defined for the install script to
# work. Running this script like the following will accomplish this,
#
#     /usr/bin/env -i HOME=$HOME USER=$USER TERM=$TERM SHELL=$SHELL /bin/bash install-stack-on-beach.sh
#
# Note:
#   You must have ruby in your path. On beach, ruby is installed under
#   /usr/local/ruby.

PREFIX=$(pwd)
JAVA=/usr/java/default/bin/java
RUBY=/usr/local/ruby/bin/ruby

export PATH=/usr/bin:/bin:/usr/sbin:/sbin:/etc:/usr/lib

echo "Installing the entire wmt stack in:"
echo ""
echo "    $PREFIX"
echo ""
read -p "Are you sure you want to do this? " answer

while true
do
    case $answer in
      [y]* )
          echo "OK."
          break;;

      * )
          echo "Exiting"
          exit
          break;;
    esac
done

echo "installing..."

wget https://raw.githubusercontent.com/csdms/wmt-exe/master/scripts/install
python ./install --with-java=$JAVA --with-ruby=$RUBY $PREFIX
