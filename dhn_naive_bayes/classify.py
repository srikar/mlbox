import re, string

from nltk import FreqDist
from nltk.tokenize import word_tokenize

from nltk.stem.porter import PorterStemmer

class Model(object):
    def __init__(self):
        self.feature_count = {}
        self.category_count = {}

    def get_feature_count(self, feature, category):
        if feature in self.feature_count and category in self.feature_count[feature]:
            return float(self.feature_count[feature][category])
        else:
            return 0.0
            
    def get_category_count(self, category):
        if category in self.category_count:
            return float(self.category_count[category])
        else:
            return 0.0

    def increment_feature(self, feature, category):
        self.feature_count.setdefault(feature,{})
        self.feature_count[feature].setdefault(category, 0)
        self.feature_count[feature][category] += 1
        
    def increment_cat(self, category):
        self.category_count.setdefault(category, 0)
        self.category_count[category] += 1
                
    def probability(self, item, category):
        category_prob = self.get_category_count(category) / sum(self.category_count.values())
        return self.document_probability(item, category) * category_prob
    
    def document_probability(self, item, category):
        features = get_features(item)
        
        p = 1
        for feature in features:
            # print "%s - %s - %s" % (feature, category, self.weighted_prob(feature, category))
            p *= self.weighted_prob(feature, category)
            
        return p

    def feature_prob(self, f, category): # Pr(A|B)
        if self.get_category_count(category) == 0:
            return 0
        
        return (self.get_feature_count(f, category) / self.get_category_count(category))
        
    def weighted_prob(self, f, category, weight=1.0, ap=0.5):
        basic_prob = self.feature_prob(f, category)
        
        totals = sum([self.get_feature_count(f, category) for category in self.category_count.keys()])
        
        w_prob = ((weight*ap) + (totals * basic_prob)) / (weight + totals)
        return w_prob
        
class Trainer(object):
    def __init__(self, data):
        self.data = data
        self.model = Model()

    def train_model(self):
        for category, documents in self.data.items():
            for doc in documents:
                self.train(doc, category)
        return self.model

    def train(self, item, category):
        features = get_features(item)
        
        for f in features:
            self.model.increment_feature(f, category)
        
        self.model.increment_cat(category)

def get_features(document):
    all_words = word_tokenize(document)
    all_words_freq = FreqDist(all_words)
    return all_words_freq

#def get_features(document):
#    document = re.sub('[%s]' % re.escape(string.punctuation), '', document) # removes punctuation
#    document = document.lower() # make everything lowercase
#    all_words = [w for w in word_tokenize(document) if len(w) > 3 and len(w) < 16]
#    p = PorterStemmer()
#    all_words = [p.stem(w) for w in all_words]
#    all_words_freq = FreqDist(all_words)
#    
#    # print sorted(all_words_freq.items(), key=lambda(w,c):(-c, w))
#    return all_words_freq
        

class Data(object):
    def __init__(self, labels):
        self.labels = labels
        self.data = {}

    def items(self):
        return self.data.items()

    def load(self):
        for label in self.labels:
            f = open(label, 'r')
            self.data[label] = f.readlines()
            f.close()
        return self

if __name__ == "__main__":
    data = Data(['arts', 'sports']).load()
    model = Trainer(data).train_model()
    print model.probability("Early Friday afternoon, the lead negotiators for the N.B.A. and the players union will hold a bargaining session", 'arts')
    print model.probability("Early Friday afternoon, the lead negotiators for the N.B.A. and the players union will hold a bargaining session", 'sports')
