# similitude
CLI tool to evaluate similarity of two tables.

## TODO
* Implement comparison_engine & add comparison options. all|schema|values etc
* Fix broken setup.py not finding other modules
* Add unit tests
* Define & document common data & schema model to allow for comparisons betwween databases
* Refactor the currently returned prints that are results. Return one struct with results that another module can present.
* Implement column aggregate value comparisons. One for every type of BQ col. (Numeric, String, Datetime...)
* Allow for specific column comparisons or all columns compared.
* Refactor index selection to not require many cols as -k col_1 -k col_2 etc, but instead allow for col_1, col_2, ...

### Comparison workflow:
* Join tables on possible index
* Show what key percentage is t1 unique
* Show what key percentage is t2 unique
* Compare numerical column avg of the intersection, show percentage diff of avg/stddev.
* Compare allotment for string cols & timestamps, show percentage diff.

