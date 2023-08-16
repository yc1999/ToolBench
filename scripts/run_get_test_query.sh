#!/bin/bash
set -ex

test_query_ids=$(ls ./data/test_query_ids)

for query_id in $test_query_ids
do
    python ./scripts/get_test_query.py --query_ids_file ${query_id}
done