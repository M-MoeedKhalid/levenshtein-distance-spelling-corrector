An auto-spell collecter based on Levenshtein distance.
Success is calculated based on @1 @5 and @10 

Levenshtein distance is a metric used to measure the differencebetween two sequences (primarily sequences of characters)

We aim to use Levenshtein distance to suggest a spell checker thatis based on this metric. What our software will aim to do is suggestthe user correction of misspelled words based on their comparatived ifferences.

Given a dictionary D, a corpus of misspelled tokens C, and for eachtoken 𝑡 such that 𝑡∈C, top-𝑘 most similar, e.q., least distant, oftoken 𝑡, called top-𝑘𝑡∈𝐶 is desired

Given a text with a mistake such as "additoin" Our program will suggest the word "addition" because its 𝑘 ≥ 1.


This dataset contained 800 of the more commonly misspelled wordsin the English language. We ran our code on a subset of 30 pairs of randomly chosen words (because of performance constraints) see how it will perform. Most of the suggestions made by our pro-gram were exactly as desired on average as 70% of the time thecorrect value was found at k=1. 13% of the times it was found at k=5. Where as 16% of the time the word was not found in the first 10 suggestions.From these results we can interpret that in common English language typing mistakes, our algorithm can suggest the correct wordmore often that not. In 83% of the cases, the correct suggestion hasbeen present in the first two words suggested.


To run this program:
Open your terminal and type:
1) `pip install -r requirements.txt`
2) `python autospell_corrector.py`
