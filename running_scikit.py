# training_data = import training data set
# training_targets = import training data set target list

sports_vs_rest = training
sports_vs_rest_targets = training_targets

from sklearn.feature_extraction.text import CountVectorizer
count_vect = CountVectorizer()
X_train_counts = count_vect.fit_transform(twenty_train.data)
print(X_train_counts.shape)

tfidf_transformer = TfidfTransformer()
X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)
print(X_train_tfidf.shape)

from sklearn.naive_bayes import MultinomialNB
clf = MultinomialNB().fit(X_train_tfidf, twenty_train.target)

input_string = input("Please paste the whole news story as one string: ")
predicted = clf.predict([input_string])
