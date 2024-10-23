# Senior-Project
Crafting and Assessing Basic Lexical Simplification Models

For this project I create four basic lexical simplification models to approach the issue of language complexity.
The general framework for these models is sourced from a survey titled "A Survey on Lexical Simplification" by
G. H. Paetzold and L. Specia. I do make tweaks to the framework for simplicity and understanding. In my framework,
the pipeline is as follows:

Complex Word Identfication -> Substitution Generation -> Substitution Ranking -> Substitution Replacement 

    CWI: method to identify words as complex from a given sentence
    SG: method to generate synonyms or alternatives for each word in a given list of complex words
    SRk: method to rank which substitute terms are most appropriate from a given list of alternative terms
    SRp: method to replace complex words with alternatives

  ^Each model follows this pipeline with some distinct aspects^.

These models are then tested with a set of complex sentences from the New York State regents exam.
Using the Chi-Squared formula, I compare the observed results and reflect on any strengths and weakness.
