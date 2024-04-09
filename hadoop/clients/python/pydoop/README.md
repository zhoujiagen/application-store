# Pydoop

- https://crs4.github.io/pydoop/installation.html#trying-pydoop-without-installing-it

Build image:

```shell
git clone https://github.com/crs4/pydoop.git
cd pydoop
docker build -t pydoop .

# on erros:
#13.10 WARNING: Requirement 'dist/pydoop-2.0.0\r.tar.gz' looks like a filename, but the file does not exist
#.tar.gzrocessing ./dist/pydoop-2.0.0
# FIX: change CRLF to LR 'VERSION' and other files:
# sudo apt-get install dos2unix
# find . -type f -print0 | xargs -0 dos2unix --
```

Run examples:

```shell
# in container

# script wordcount.py
root@pydoop:/build/pydoop/examples/pydoop_script# ls scripts/
base_histogram.py  caseswitch.py  grep.py  lowercase.py  transpose.py  wc_combiner.py  wordcount.py  wordcount_sw.py
root@pydoop:/build/pydoop/examples/pydoop_script# ./run_script.sh wordcount 
...

root@pydoop:/build/pydoop/examples/pydoop_scrip# hdfs dfs -ls /user/root/input
Found 2 items
... /user/root/input/alice_1.txt
... /user/root/input/alice_2.txt
root@pydoop:/build/pydoop/examples/pydoop_script# hdfs dfs -ls /user/root/output
Found 3 items
... /user/root/output/_SUCCESS
... /user/root/output/part-r-00000
... /user/root/output/part-r-00001

# submit wordcount_minimal.py
root@pydoop:/build/pydoop/examples/pydoop_submit# ls mr/
map_only_java_writer.py  map_only_python_writer.py  nosep.py  wordcount_full.py  wordcount_minimal.py
root@pydoop:/build/pydoop/examples/pydoop_submit# ./run_submit.sh wordcount_minimal
...
root@pydoop:/build/pydoop/examples/pydoop_submit# hdfs dfs -ls /user/root/output
Found 2 items
... /user/root/output/_SUCCESS
... /user/root/output/part-r-00000
```
