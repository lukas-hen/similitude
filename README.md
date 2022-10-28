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
