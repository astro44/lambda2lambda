# lambda2lambda
lambda function to spin up multiple lambdas in a new dummy thread and get results.
Currently as of 2016, limitations on AWS lambda won't allow mulitprocessing to work.

This test will simply spin up and return results from 'minion' or 'child' lambdas.
