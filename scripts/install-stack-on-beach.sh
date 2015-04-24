#! /bin/bash
#
# Install the WMT-EXE software stack.
#
# Install the entire software stack on beach.colorado.edu into the CURRENT
# DIRECTORY. This is really only specific to beach in the location of java.
#
# Note:
#   You must have ruby in your path. On beach, ruby is installed under
#   /usr/local/ruby.

PREFIX=$(pwd)
JAVA=/usr/java/default/bin/java

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
python ./install --with-java=$JAVA $PREFIX
