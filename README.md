# DIG-OpenIE

![openie_logo](./res/dig-openie.jpg)

Apply open information extraction technology to extract useful information for avoiding illigle human trafficking behaviours.

This is a direct research outcome when I worked with Prof. Pedro Szekely on DIG project


## Main Idea

Develop capability to automatically build knowledge graphs and their ontologies using extractions from Open Information Extraction (Open IE) systems. These extractions are typically subject/predicate/object triples such as <my name, be, jessica> or <i, be, sweet female>, where each of the elements of the triples are text. The goal is to create a knowledge graph with appropriate nodes and links that represent the information in the extractions. The problem is difficult because Open IE extractions are noisy, and the mapping from the extractions to knowledge graphs is complex and subtle. To address the problem and evaluate progress, we propose to use the knowledge graphs we already built for escorts, weapons and patents as gold standards. We will first address the simpler problem of using Open IE extractions to populate individual attributes of the nodes in a graph. We will train learning algorithms using two of the knowledge graphs, and test on the third one, by removing one attribute definition from the ontology and removing all instances of the attribute in the graph. We will test the ability of our system to recover the removed attribute using Open IE extractions, measuring performance using precision and recall. For example, if we remove the “name” attribute of people, can the system add it back to the ontology and populate the name of every person node in the graph? We will then address increasingly more difficult problems: recreating the relationships among nodes, recreating a class of objects including its attributes and relationships to other objects, and finally recreating the whole graph. This incremental research plan breaks the very hard problem of creating knowledge graphs from Open IE extractions into manageable sub-problems, each representing a valuable capability that we plan to deliver at the end of each stage of the research. During the next year we plan to address the problem or recreating attributes and relationships, and in the last year we plan to address the problem of recreating classes of nodes and the full graph.


## My works

- Run ReVerb on 7 documents from different websites, list extractions from ReVerb, score extractions as useful or useless, and make a note of information that I think should have been extracted, but wasn't.
- Fetch data by elastic search from DIG database, and run it on ReVerb
- Implement feature extraction and build feature vectors to generate training and testing datasets for machine learning process based on scikit-learn library
- Train classifiers, such as decision tree, random forest and svc, to evaluate datasets. The accracy of classifers for decision tree and random forest is around 97%.
- Test classifers on random datasets, by which gets around 97% accuracy for ada boost classifier.
- Improved the precision and recall for random dataset that contains names at around 93% and 83% relatively.
- Conducted a research on random datasets, and low extractions for ReVerb and low precision and recall for these sentences that contain names, by which found that this solution cannot work well for annotating phone numbers.


## To do list

- [ ] Run and analyze the dataset from the forum that contains customer reviews
- [ ] Try to find useful information from the reviews, information like people's description, actions, and relationships.
- [ ] Train and run classifiers to flag these informations
- [ ] write a program to build knowledge graph for specifc description and behaviour

## Achieved

- [*] conduct the experiment for the phone numbers
- [*] in training process, add name dictionary that contains enough names
- [*] remove names from feature set
- [*] improve feature extraction: add reverb accuracy








