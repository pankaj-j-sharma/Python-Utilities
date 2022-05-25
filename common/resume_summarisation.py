#------------imports ---------------------------------
# It took 1:36 hours to train the model on all the 1513
# records on the laptop as oppoesed to 3:05 on colab
from __future__ import unicode_literals, print_function
import json
import pprint
import re
import plac
import random
from pathlib import Path
import spacy
import time
from spacy.util import minibatch, compounding

#--------------initial setup ------------------------------

start_time = time.time()

#debug variable
temp=[]

# file path from mounted gdrive
#filepath="gdrive/My Drive/Demo Document Annotations.json"

#filepath="C:/Users/User/Downloads/Demo Document Annotations.json"
filepath="C:/Users/User/Downloads/Entity Recognition in Resumes.json"
output_dir="C:\Suven\AdvML\Resume_Summarisation_Project"

# training data
TRAIN_DATA = [
	("Who is Shaka Khan? , I am Pankaj", {"entities": [(7, 17, "PERSON"),(26, 32, "PERSON")]}),
	("I like London and Berlin.", {"entities": [(7, 13, "LOC"), (18, 24, "LOC")]}),
]

TEST_DATA = [
	("I am Peter",{}),
	("I like Mumbai and Calcutta",{})
]

TRAIN_DATA[0][0][26:32]

# # uploading local files onto colab
# from google.colab import files
# uploaded = files.upload()

# #Mounting google drive into colab
# from google.colab import drive
# drive.mount('/content/gdrive')

# with open("gdrive/My Drive/Demo Document Annotations1.json",'rb') as f:
  # for line in f:
	# print(line)
	
training_data = []	
resume_count=len(list(open(filepath,'r',encoding="utf8").readlines()))
print('Total available resumes => ',resume_count)

#------------------------------------------------------
	

def load_data():
	print('loading training data ...')
	lines=open(filepath,'r',encoding="utf8").readlines()	
	for i,line in enumerate(lines):
		# if i>440:
			# break
		data = json.loads(line)
		text = data['content']
		entities = []
		if data['annotation']:
			for annotation in data['annotation']:
				#only a single point in text annotation.
				point = annotation['points'][0]
				labels = [ str(i).upper() for i in annotation['label']]
				#print(labels)
				# handle both list of labels or a single label.
				if not isinstance(labels, list):
					labels = [labels]

				for label in labels:
					#dataturks indices are both inclusive [start, end] but spacy is not [start, end)
					entities.append((point['start'], point['end'] + 1 ,label))

			training_data.append((text, {"entities" : entities}))
	print('loaded training data ...')


	
def loadmodel(model=None, output_dir=None, n_iter=100):
    """Load the model, set up the pipeline and train the entity recognizer."""
    print('loading the model ...')
    if model is not None:
        nlp = spacy.load(model)  # load existing spaCy model
        print("Loaded model '%s'" % model)
    else:
        nlp = spacy.blank("en")  # create blank Language class
        print("Created blank 'en' model")

    # create the built-in pipeline components and add them to the pipeline
    # nlp.create_pipe works for built-ins that are registered with spaCy
    if "ner" not in nlp.pipe_names:
        ner = nlp.create_pipe("ner")
        nlp.add_pipe(ner, last=True)
    # otherwise, get it so we can add labels
    else:
        ner = nlp.get_pipe("ner")

    # add labels
    for _, annotations in TRAIN_DATA:
        for ent in annotations.get("entities"):
            ner.add_label(ent[2])

    # get names of other pipes to disable them during training
    other_pipes = [pipe for pipe in nlp.pipe_names if pipe != "ner"]
    with nlp.disable_pipes(*other_pipes):  # only train NER
        # reset and initialize the weights randomly – but only if we're
        # training a new model
        if model is None:
            nlp.begin_training()
        for itn in range(n_iter):
            random.shuffle(TRAIN_DATA)
            losses = {}
            # batch up the examples using spaCy's minibatch
            batches = minibatch(TRAIN_DATA, size=compounding(4.0, 32.0, 1.001))
            for batch in batches:
                texts, annotations = zip(*batch)
                try:
                  nlp.update(
                      texts,  # batch of texts
                      annotations,  # batch of annotations
                      drop=0.5,  # dropout - make it harder to memorise data
                      losses=losses
                  )
                except Exception as e:
                  temp.append(texts)
                  #print('Exception in => ',texts)
                  #print('Error is => ',str(e),'\n')
                  continue
            if losses:  
                print("losses ",losses)

	# ---------test the trained model ------------------
    
	# print('+'*140)
    # print('testing the trained model ','\n')

    # for text, _ in TRAIN_DATA:
        # doc = nlp(text)
        # #pprint.pprint(doc.ents)
        # print("Entities", [(ent.text, ent.label_) for ent in doc.ents])
        # print('_'*100)
        # #print("Tokens", [(t.text, t.ent_type_, t.ent_iob) for t in doc if t.ent_type_])
        # #print('_'*100)
		
    # ---- save model to output directory --------------
    if output_dir is not None:
        output_dir = Path(output_dir)
        if not output_dir.exists():
            output_dir.mkdir()
        nlp.meta["name"] = "resume_summ"  # rename model
        nlp.to_disk(output_dir)
        print("Saved model to", output_dir)

        # test the saved model
        print("Loading from", output_dir)
        nlp2 = spacy.load(output_dir)
        # Check the classes have loaded back consistently
        assert nlp2.get_pipe("ner").move_names == list(ner.move_names)
        doc2 = nlp2(TRAIN_DATA[random.randrange(10)][0])
        #pprint.pprint(doc2)
        print('Predicted entities > ','\n')
        for ent in doc2.ents:
            print(ent.label_, ent.text)
        print('\n')

#------- Main program begins ---------------------------	
if __name__ =='__main__':	

	load_data()
	TRAIN_DATA=training_data
	temp.clear()
	loadmodel(output_dir=output_dir)

	print('# of resumes failed to be parsed =>',len(temp))
	print('+'*100)

	# for t,a in training_data:
		# for an in a['entities']:
			# print(an[2],'=>',t[an[0]:an[1]])

		# print('-'*100)
		# break

	elapsed_time = time.time() - start_time
	print('\n')
	print('Execution completed in => ',time.strftime("%H:%M:%S", time.gmtime(elapsed_time)))