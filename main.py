import argparse,os,sys,itertools
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.stem.wordnet import WordNetLemmatizer

#INPUT
# 1. files_directory = directory containing email files
class VocabBuilder:
	def __init__(self, files_directory):
		self.files_directory = files_directory
		self.vocabulary = set()
		self.lemmatizer = WordNetLemmatizer()
		self.set_of_stop_words = set(stopwords.words("english"))

	def buildVocab(self):
		for spam_file in os.listdir(self.files_directory):
			
			#FQN
			spam_file = self.files_directory + spam_file
			
			with open(spam_file) as f:
				content = f.read()
				sentences = sent_tokenize(content)

				try: 
					words_in_content = [word_tokenize(sentence) for sentence in sentences]
				except e:
					print "here"

				words_in_content = list(itertools.chain(*words_in_content))


				#removal of stop words
				preprocessed_words = filter(lambda word: word not in self.set_of_stop_words, words_in_content)

				#lemmatize
				preprocessed_words = map(lambda word: self.lemmatizer.lemmatize(word), preprocessed_words)

				self.vocabulary.update(preprocessed_words)

	def getVocab(self):
		self.buildVocab()
		return self.vocabulary



if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument('--data-dir', default='email_classification_data/')
	args = parser.parse_args(sys.argv[1:])
	args = vars(args)
	data_dir = args["data_dir"]

	spam_dir = data_dir + "train_data/spam/"
	
	vocab_builder = VocabBuilder(spam_dir)
	print vocab_builder.getVocab()

	
		
		

