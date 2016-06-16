# BigQueryJson

Simple script to convert the result of BigQuery's "Download as JSON" to valid JSON

# Usage

Reads from stdin and writes to stdout

    python bigQueryJson.py < results-20160616-123456.json

# Testing

Manually tested on python 2.7

Output validated using [JSONLint](http://jsonlint.com/)

# Licence

MIT - http://abovethewater.mit-license.org/

See full license text in LICENSE