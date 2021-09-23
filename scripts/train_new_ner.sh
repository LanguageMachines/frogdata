#! /bin/sh -x

if [ "$exe_bin" = "" ];
then echo "exe_bin not set";
     exit;
fi

$exe_bin/nergen -O NERDATA -c $exe_bin/../share/frog/nld/frog.cfg --gazeteer=$exe_bin/../share/frog/nld/ners.known NERDATA/ner.train
