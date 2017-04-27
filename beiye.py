#coding:utf-8
import simplebayes
class beiyeshi(object):
    def __init__(self):
        self.beiyeshi=simplebayes.SimpleBayes()
bayes=simplebayes.SimpleBayes()
bayes.train('good', 'sunshine drugs love sex lobster sloth')
bayes.train('bad', 'fear death horror government zombie')

assert bayes.classify('sloths are so cute i love them') == 'good'
assert bayes.classify('i would fear a zombie and love the government') == 'bad'

print bayes.score('i fear zombies and love the government')
bayes.cache_persist()
dir(simplebayes)
print bayes.cache_file
print bayes.cache_path
print bayes.__doc__
print bayes.__module__

