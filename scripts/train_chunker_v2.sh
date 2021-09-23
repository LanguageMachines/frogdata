#! /bin/sh -x

if [ "$exe_bin" = "" ];
then echo "exe_bin not set";
     exit;
fi

cd ../data
$exe_bin/chunkgen  -c $exe_bin/../share/frog/nld//frog.cfg chunker.train -O chunkgen/
