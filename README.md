# Unit testing
I have created this repository to test some unit testing techniques. Unit testing is a bag of techniques used to assure data quality. Once data is being pipelined from one point to another, premises may change - trailing zeros, lower/uppercasing, data type changes, etc. Bug fixes, new features and refactoring are other factors. To assure that everything that is feed into a data environment is kept integer, automation should raise any of these inconsistencies as soon as they are identifiable. This is where unit testing comes in.

# Why do unit testing?
Time savings and reduced downtime are the major benefits of unit testing, while improved documentation and more user trust are great side effects. Unit testing is thus a great ally to a data scientist, data engineer or a ML engineer to ensure data quality.

# Storytelling: DATAMIN, our mining company
To showcase some unit testing cases, we will create our own company, DATAMIN. DATAMIN works as a consulting company for mineral exploration companies and offers services on prospecting mineral deposits. Thus, our data will have features such as location, metal concentration and reserves.