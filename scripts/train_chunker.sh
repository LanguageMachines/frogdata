#! /bin/sh -x

if [ "$exe_bin" = "" ];
then echo "exe_bin not set";
     exit;
fi

cd ../data
$exe_bin/mbtg -M1000 -p dddwfWawa -P chnppddwFawsss -O"-G0 +D +vs K:-a IGTree -w gr U:-a ib1 -m M -L 2 -k 5 -w gr -d ID" -T chunker.train
