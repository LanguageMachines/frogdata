#! /bin/sh -x

if [ "$exe_bin" = "" ];
then echo "exe_bin not set";
     exit;
fi

cd ../data
$exe_bin/mbtg -M500 -n 1 -% 5 -p dddwfWawa -P chnppdddwFawasss -O"+vS -G0 +D K: -w1 -a1 U: -a0 -w1 -mM -k9 -dIL" -T Frog.mbt.1.1
