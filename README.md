# Senior-Project

For this project, I explore the topic of lexical simplification and create four basic simplification models. The framework for these models is
sourced from a survey titled "A Survey on Lexical Simplification" by G. H. Paetzold and L. Specia. I do make tweaks to the framework for
simplicity and clarity. For specific information about methodology, results, and analysis, please refer to the paper included in this repository:
**[Dumonym: Crafting and Assessing Lexical Simplification, from algorithms to models](Dym.pdf)**

---

**Pipeline**
- Complex Word Identfication: identifies words as complex from a given sentence
- Substitution Generation: generates synonyms or alternatives for each word in a given list of complex words
- Substitution Ranking: ranks which substitute terms are most appropriate from a given list of alternative terms
- Substitution Replacement: replaces identified complex words with alternatives

Each model follows this pipeline with distinct aspects to improve quality.

## Libraries
- NLTK
- Gensim
- JSON
  
## Datasets
*(All text data used for saved dictionary)
- Children Stories (lower reading level): ["Children Stories Text Corpus"](https://www.kaggle.com/datasets/edenbd/children-stories-text-corpus?resource=download), accessed May 02, 2024.
- Short Stories: ["Short Stories for Children"](https://andonovicmilica.wordpress.com/wp-content/uploads/2018/07/short-stories-for-children.pdf).
- Diary of a Wimpy Kid: Double Down by Jeff Kinney, 2016: [PDF](https://thebookshelfbeforeme.files.wordpress.com/2020/04/diary-of-a-wimpy-kid-double-down-by-jeff-kinney.pdf).
- The Stoic (higher reading level) by John Galsworthy, 1920: [PDF](https://theshortstory.co.uk/devsitegkl/wp-content/uploads/2016/02/Short-stories-by-John-Galsworthy.pdf), accessed May 02, 2024.
