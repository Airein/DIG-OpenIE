# DIG-OpenIE

![openie_logo](./res/dig-openie.jpg)

Apply open information extraction technology to extract useful information for avoiding illigle human trafficking behaviours.

This is a direct research outcome when I worked with Prof. [Pedro Szekely](http://usc-isi-i2.github.io/szekely/) on [DIG project](http://usc-isi-i2.github.io/dig/)


## Main Idea

Develop capability to automatically build knowledge graphs and their ontologies using extractions from Open Information Extraction (Open IE) systems. These extractions are typically subject/predicate/object triples such as <my name, be, jessica> or <i, be, sweet female>, where each of the elements of the triples are text. The goal is to create a knowledge graph with appropriate nodes and links that represent the information in the extractions. The problem is difficult because Open IE extractions are noisy, and the mapping from the extractions to knowledge graphs is complex and subtle. To address the problem and evaluate progress, we propose to use the knowledge graphs we already built for escorts, weapons and patents as gold standards. We will first address the simpler problem of using Open IE extractions to populate individual attributes of the nodes in a graph. We will train learning algorithms using two of the knowledge graphs, and test on the third one, by removing one attribute definition from the ontology and removing all instances of the attribute in the graph. We will test the ability of our system to recover the removed attribute using Open IE extractions, measuring performance using precision and recall. For example, if we remove the “name” attribute of people, can the system add it back to the ontology and populate the name of every person node in the graph? We will then address increasingly more difficult problems: recreating the relationships among nodes, recreating a class of objects including its attributes and relationships to other objects, and finally recreating the whole graph. This incremental research plan breaks the very hard problem of creating knowledge graphs from Open IE extractions into manageable sub-problems, each representing a valuable capability that we plan to deliver at the end of each stage of the research. During the next year we plan to address the problem or recreating attributes and relationships, and in the last year we plan to address the problem of recreating classes of nodes and the full graph.


## My Progress

### Task One

Run ReVerb on 7 documents from different websites, list extractions from ReVerb, score extractions as useful or useless, and make a note of information for extractions.

- Ran ReVerb on 5 documents from each web site, camera reviews, and 2 forum sites in the weapons domain.
- For each document, listed the extractions and score them as useful or useless. (A useful extraction is one we could use to build a knowledge graph, use your judgment.)
- Made a note of information that should have been extracted, but wasn’t.

### Task Two

Write a program to train and run classifers based on the human trafficking datasets from ISI for annotating person's name.

- Fetched data by elastic search from DIG database, run it on ReVerb and get extractions.
- Implement feature extraction and build feature vectors to generate training and testing datasets for machine learning process.
- Wrote code for automatically labeling based on given names.
- Applied scikit-learn library ot train and test classifers, such as Decision Tree, random forest, ada boost, svm, and naive bayes.
- Improved the implementation for feature extraction, by which the accuracy for decision tree and random forest are at around 97% relatively.

### Task Three

Evaluate the performance of classifers on random datasets that contain person names or that contain phone numbers

- Tested the classifers on random datasets that contain person names, and get accuracy at around 90%.
- Refined implementation for training process by adding a name dictionary that contains enough names instead of the names from original datasets.
- Updated the feature set from the feature extractions by removing real person names and adding reverb accuracy.
- Improved the precision and recall for random dataset that contains names at around 93% and 83% relatively.
- Tested the classifers on random datasets that contain phone numbers, and found that this solution can not work well for annotating phone numbers.
- Generated datasets with bigram and trigram tuples from original one, and trained and ran classifers based on new datasets. (classifers work better on original one than datasets in bigram and trigram)
- Conducted a research on random datasets, and low extractions for ReVerb and low precision and recall for these sentences that contain phone number, by which found that this solution cannot work well for annotating phone numbers.

### Task Four

Write a program to extract useful information and build knowledge graph for the dataset from an escorts forum that contain reviews.

- [ ] Run and analyze the dataset from the forum that contains customer reviews
- [ ] Try to find useful information from the reviews, information like people's description, actions, and relationships.
- [ ] Train and run classifiers to flag these informations
- [ ] write a program to build knowledge graph for specifc description and behaviour
















