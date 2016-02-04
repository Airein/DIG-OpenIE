# DIG-OpenIE

![openie_logo](./res/dig-openie.jpg)

My direct research and student works at ISI (DIG - Open Information Extraction)
Worked with Prof. Pedro Szekely on DIG project for Open Information Extraction

## Task Description

Develop capability to automatically build knowledge graphs and their ontologies using extractions from Open Information Extraction (Open IE) systems. These extractions are typically subject/predicate/object triples such as <my name, be, jessica> or <i, be, sweet female>, where each of the elements of the triples are text. The goal is to create a knowledge graph with appropriate nodes and links that represent the information in the extractions. The problem is difficult because Open IE extractions are noisy, and the mapping from the extractions to knowledge graphs is complex and subtle. To address the problem and evaluate progress, we propose to use the knowledge graphs we already built for escorts, weapons and patents as gold standards. We will first address the simpler problem of using Open IE extractions to populate individual attributes of the nodes in a graph. We will train learning algorithms using two of the knowledge graphs, and test on the third one, by removing one attribute definition from the ontology and removing all instances of the attribute in the graph. We will test the ability of our system to recover the removed attribute using Open IE extractions, measuring performance using precision and recall. For example, if we remove the “name” attribute of people, can the system add it back to the ontology and populate the name of every person node in the graph? We will then address increasingly more difficult problems: recreating the relationships among nodes, recreating a class of objects including its attributes and relationships to other objects, and finally recreating the whole graph. This incremental research plan breaks the very hard problem of creating knowledge graphs from Open IE extractions into manageable sub-problems, each representing a valuable capability that we plan to deliver at the end of each stage of the research. During the next year we plan to address the problem or recreating attributes and relationships, and in the last year we plan to address the problem of recreating classes of nodes and the full graph.


## My works

- Run ReVerb on 7 documents from different websites, list extractions from ReVerb, score extractions as useful or useless, and make a note of information that I think should have been extracted, but wasn't.
- Fetch data by elastic search from DIG database, and then use machine learning algorithm to train a classifier to identify real person's name.


