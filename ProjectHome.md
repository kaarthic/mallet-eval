**Some Named Entity Recognition evaluation for MALLET, including English and Chinese samples**

20110422 MALLET-EVAL PROJECT

GENERAL

This is a project for evaluating MALLET (MAchine Learning for
LanguagE Toolkit). MALLET's binary and source codes are not included,
you can check out them from this site:

> http://mallet.cs.umass.edu/

This distribution only contains sample annotation data  and scripts for
converting, importing and evaluating. The articles in the two corpora are not included
for copyright reasons. That is why you need their cds for building the complete data
sets.

We provide two sample corpora: Penn Treebank Sample (5% fragment of Penn
Treebank) and HIT CIR LTP Corpora Sample (10% fragemnt of the whole
Corpora)

> http://web.mit.edu/course/6/6.863/OldFiles/share/data/corpora/treebank/

> http://ir.hit.edu.cn/demo/ltp/Sharing_Plan.htm


BUILDING THE TRAIN AND TEST DATA FILES

In order to obtain the data files you need to perform three steps:


<pre>
1. Get a local copy of the mallet-eval repository with this command:<br>
<br>
hg clone https://mallet-eval.googlecode.com/hg/ mallet-eval<br>
<br>
2. Set up $MALLET_HOME enviroment: export MALLET_HOME=/path/to/mallet/<br>
<br>
3. Train and test with provided Chunking, POS Tagging and Named Entity<br>
Recognition data (chunking/ pos-tagging/ ner/)<br>
<br>
4a (Chunking) ./conlleval < chunking/conlleval.out<br>
<br>
4b (POS-Tagging) cd pos-tagging | ./verify.py<br>
<br>
4c (Named Entity Recognition) ./chn-conlleval < ner/conlleval.out<br>
</pre>