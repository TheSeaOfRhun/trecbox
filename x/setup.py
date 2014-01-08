import sys, os
from SysTerrier import *
from SysIndri import *
from SysLucene import *
from Topics import Topics

home = ""

# bootstrap env ('config' usually left out of version control)
with open("config", "r") as f:
    home = f.readline().rstrip("\n")

root = os.path.join(home, "exp")

env = {
    "doc"     : os.path.join(home, "doc"),
    "topics"  : os.path.join(home, "topics"),
    "qrels"   : os.path.join(home, "qrels"),
    "treceval": os.path.join(home, "trec_eval.9.0"),
    "lucene"  : os.path.join(home, "lucene.TREC"),
    "terrier" : os.path.join(home, "terrier-3.5"),
    "indri"   : os.path.join(home, "indri-5.6"),
    "utils"   : os.path.join(home, "utils"),
    "index"   : os.path.join(root, "index"),
    "runs"    : os.path.join(root, "runs"),
    "evals"   : os.path.join(root, "evals"),
    "attic"   : os.path.join(root, "attic")
    }

doc = {"test" : os.path.join(env["doc"], "test"),
       "test1": os.path.join(env["doc"], "test1"),
       "bunch": os.path.join("/tmp", "bunch"),
       "fbis" : os.path.join(env["doc"], "cd45/fbis"),
       "fr94" : os.path.join(env["doc"], "cd45/fr94"),
       "ft"   : os.path.join(env["doc"], "cd45/ft"),
       "la"   : os.path.join(env["doc"], "cd45/latimes")
       }

topic = {"test1": os.path.join(env["topics"], "test1"),
         "test2": os.path.join(env["qrels"], "test2"),
         "test3": os.path.join(env["qrels"], "test3"),
         "f3": os.path.join("/tmp", "f3"),
         "t6": os.path.join(env["topics"], "topics.301-350"),
         "t7": os.path.join(env["topics"], "topics.351-400"),
         "t8": os.path.join(env["topics"], "topics.401-450")
         }

qrels = {"test1": os.path.join(env["qrels"], "test1"),
         "t6": os.path.join(env["qrels"], "qrels.trec6.adhoc.parts1-5"),
         "t7": os.path.join(env["qrels"], "qrels.trec7.adhoc.parts1-5"),
         "t8": os.path.join(env["qrels"], "qrels.trec8.adhoc.parts1-5")
         }

model = ["tfidf", "bm25"]

def main(argv):

    #t = Topics(topic["t6"])
    t = Topics(topic["test1"])
    t1 = Topics(topic["test2"])
    t2 = Topics(topic["test3"])
    t3 = Topics(topic["f3"])

    s = SysTerrier(env)

    s.index("bunch", doc["bunch"], ["None", "None"])
    #s.retrieve("bunch", "bunch", ["None", "None"], "tfidf", t.query("terrier", "t"))
    #s.evaluate("bunch", qrels["test1"])

    #s.retrieve("xyz", "xyz", ["None", "None"], "tfidf", t.query("terrier"))
    #s.evaluate("xyz", qrels["test1"])

    #s.retrieve("xyz", "xyz.1", ["None", "None"], "tfidf", t1.query("terrier"))
    #s.evaluate("xyz.1", qrels["test1"])

    #s.retrieve("xyz", "xyz.2", ["None", "None"], "tfidf", t3.query("terrier"))
    #s.evaluate("xyz.2", qrels["test1"])

    #s.index("xyz.s", doc["test1"], ["stoptest", "None"])
    #s.retrieve("xyz.s", "xyz.s", ["stoptest", "None"], "tfidf", t.query("terrier"))
    #s.evaluate("xyz.s", qrels["test1"])

    #s = SysIndri(env)
    #s.index("xyz", doc["test"], ["stop", "porter"]])

    #s = SysLucene(env)
    #s.index("xyz", doc["test"], ["stop", "porter"]])

    #s.retrieve("xyz", "xyz", "tfidf", t.query("lucene"))
    #s.retrieve("uvw", "uvw", "tfidf", t.query("indri"))
    
    
    
if __name__ == "__main__":
   main(sys.argv[1:])
