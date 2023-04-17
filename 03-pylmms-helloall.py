#!/usr/bin/env python

# https://github.com/kagisearch/pyllms

import llms
from   pprint import pprint

# claude-instant-v1 is an option as wel...
model = llms.init(model=['gpt-3.5-turbo', 'claude-v1', 'claude-instant-v1'])
model.list()
result = model.complete("Please tell me about yourself.")

pprint(result.meta)
pprint(result.text)
