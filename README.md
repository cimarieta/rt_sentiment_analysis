# rt_sentiment_analysis
Sentiment Analysis on reviews from Rotten Tomatoes.

## About the dataset

The original dataset has over 10,000 reviews in different languages, mostly in English, classified with one of the labels, `positive` (`1`) or `negative` (`0`). Here, we use the [python interface for fasttext](https://github.com/salestock/fastText.py) to build a sentiment analyzer.

## Implementation details

There are five steps involved in this sentiment analysis project:
* removing non English reviews from dataset
* text processing:
    * cleaning the text from reviews, by removing punctuation and other "distracting" elements (e.g. html tags)
    * removing entity names and stopwords
    * using part-of-speech tagging
* preparation of the input for training the fasttext model
* use of cross-validation and grid-search from a selected range of values for some hyperparamers to choose the best model (in terms of precision)
* validation of the model by analyzing how well it performed in the test set

## Results

* the best option (among the ones we explored) for the text processing was to just remove the entity names and keep the stopwords
* the best model (selected from the implemented grid-search) yielded a precision of `0.91`.

## Next possible steps

There are still some directions to explore in this project:
* use other datasets containing more reviews (e.g. [Large Movie Review Dataset](http://ai.stanford.edu/~amaas/data/sentiment/) or [SAR14](https://sites.google.com/site/nquocdai/resources)) to build a better classifier, either by using them to make our training dataset larger or as an input for a skipgram model, so that it can be used as a pretrained vector for the training of the sentiment analyzer in the original dataset
* use some machine translation to be able to classify reviews in languages other than English.

## General instructions

#### Please install necessary requirements by running:
    pip install -r requirements.txt
  
#### Also, please install the english model data for using [spacy](https://spacy.io/) by running:
    python -m spacy download en_core_web_ms
