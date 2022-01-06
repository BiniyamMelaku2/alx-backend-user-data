# 0x00. Personal data

## Resources
Read or watch:

* [What Is PII, non-PII, and Personal Data?](https://piwik.pro/blog/what-is-pii-personal-data/)
* [logging documentation](https://docs.python.org/3/library/logging.html)
* [bcrypt package](https://github.com/pyca/bcrypt/)
* [Logging to Files, Setting Levels, and Formatting](https://www.youtube.com/watch?v=-ARI4Cz-awo)

# Tasks

## [0. Regex-ing](./filtered_logger.py)
Write a function called `filter_datum` that returns the log message obfuscated:

* Arguments:

    `fields`: a list of strings representing all fields to obfuscate

    `redaction`: a string representing by what the field will be obfuscated

    `message`: a string representing the log line

    `separator`: a string representing by which character is separating all fields in the log line (`message`)

* The function should use a regex to replace occurrences of certain field values.

* `filter_datum` should be less than 5 lines long and use `re.sub` to perform the substitution with a single regex.
```
bob@dylan:~$ ./main.py
name=egg;email=eggmin@eggsample.com;password=xxx;date_of_birth=xxx;
name=bob;email=bob@dylan.com;password=xxx;date_of_birth=xxx;
```
