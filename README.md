# Percent Agreeability 

### Benefits over `Cronbachs_Alpha`

After inadequate results with Cronbach's Alpha, I looked online for different inter-rater reliability formulas. The biggest issue I had with using Cronbach's Alpha to determine the reliability between two annotators was the sensitivity to data length.  To make comparisons as accurate as possible, the choice was made to break down all annotation files into milliseconds.  This was the smallest possible time unit in the annotation software, so this was as small as the analysis would go.  This accuracy is needed because the annotation software is mouse-driven, meaning selections of similair time segments would not line up exactly, and annotators in general had different times where they thought things were going on, and whole segments of annotation often times didn't perfectly match up.

This breaking down by millisecond creates data sets that have N = 300,000+, which will always score higher than a 90% when using cronbachs alpha. This is even true when testing on a hand made test that sets **every** annotation to the oppiste of the one in the file being compared; what should be a reliability rating of around 0% comes out as a highly reliable score of 98%+, simply becuase of the size of the data set.

Percent agreeablity scales with the size of the data set, and gives reasonable answers when run on test sets designed to be 100% reliable (returns a high 90s number) and 0% reliable (returns something under 5 percent).

#### Percent Agreeabilty is a pretty simple method. Are you sure it works?

This was also an important fear of mine when making the transition: I am no statistician, and I dont claim to be.  However, the task of the inter-reliability testing is to see how similair the two annotators are, to see if they are reliable enough to go forward with the work. Since we break down the annotations to the smallest possible time segment, there is already no way to mistakenly overlap annotation segments. Percent Agreeability is essentially overlaying the two files on top of each other and pointing out how often they differ from each other, which seems to accomplish the original goal.

### How the program works

Unsurprisingly, `agreeability.py` borrows multiple functions from the `cronbachs_alpha.py` it was made to replace. `create_template_list`, `get_end_time`, and `import_data` are all exact copies.  The following are the new additions. 

#### `get_agreeability`

Pretty straight forward function: takes two files, and imports the data with `import_data`, and then zips the lists to be compared (one list per catagory per file). Counts the similarities per list and then puts that number over the (duration in seconds * 1000), to get a decimal value > 0 and < 1 that represents percetn agreeability.

#### ~~`import_multiple`~~
Since the end goals is comparing two annotators, not two files, this functions takes a list of files and creates the same lists from each file as `import_data`, except when it goes to the next file it simply appends the list to the existing one, creating one long list to be used.

#### ~~`get_agreeability_multiple`~~

~~the same as `get_agreeability`, except uses `import_multiple` instead of `import_data`~~

##### NOTE: `get_agreeabilty_multiple` was deemed to be redundant. Instead, `get_agreeablity` was updated to work with both single files and lists of files.

### Tester Files

`resources_test` contains hand crafted files to test the program.\
The tested variable is the attention catagory, the other two catagories should return 1.0

`tester1.txt` and `tester2.txt` should provide a very low agreeability when run against each other.

`tester3.txt` and `tester4.txt` should provide a very high agreeability when run against each other.

`tester5.txt` and `tester6.txt` should provide a half agreeability when run against each other.