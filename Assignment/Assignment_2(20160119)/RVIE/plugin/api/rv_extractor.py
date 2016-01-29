"""

ReVerb output information:
(# minus 1 before using)
1. The filename (or stdin if the source is standard input)
2. The sentence number this extraction came from.
3. Argument1 words, space separated
4. Relation phrase words, space separated
5. Argument2 words, space separated
6. The start index of argument1 in the sentence. For example, if the value is i, then the first word of argument1 is the i-1th word in the sentence.
7. The end index of argument1 in the sentence. For example, if the value is j, then the last word of argument1 is the jth word in the sentence.
8. The start index of relation phrase.
9. The end index of relation phrase.
10. The start index of argument2.
11. The end index of argument2.
12. The confidence that this extraction is correct. The higher the number, the more trustworthy this extraction is.
13. The words of the sentence this extraction came from, space-separated.
14. The part-of-speech tags for the sentence words, space-separated.
15. The chunk tags for the sentence words, space separated. These represent a shallow parse of the sentence.
16. A normalized version of arg1. See the BinaryExtractionNormalizer javadoc for details about how the normalization is done.
17. A normalized version of rel.
18. A normalized version of arg2.

"""


import subprocess
import os.path

from ... import __root_dir__, __raw_outputs__, __reverb_outputs__

REVERB_EXEC_PATH = __root_dir__ + 'res/' + 'reverb-core-1.4.3-SNAPSHOT-jar-with-dependencies.jar'

class RVHelper():

    def __init__(self):
        pass

    def lauch_reverb(self, filename_list):
        # print REVERB_EXEC_PATH
        # print __root_dir__ + __reverb_outputs__ + 'reverb.output'
        path = __root_dir__ + __reverb_outputs__
        # print path
        filename = path + 'reverb.output'
        if os.path.isfile(filename):
            os.remove(filename)
        rv_output = open(filename, 'a')
        argsArray = ['java', '-Xmx512m', '-jar', REVERB_EXEC_PATH]
        argsArray.extend(filename_list)
        subprocess.call(argsArray, stdout=rv_output)


    def load_rv_data(self, filename=None):
        reverb_file = open(filename, 'rU')
        reverb_data = []
        for line in reverb_file:
            # row = str(line)
            line = line.split('\t')
            reverb_data.append(line)
        return reverb_data




