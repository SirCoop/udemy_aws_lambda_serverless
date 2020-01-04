# When the function is first created, it must
# be deployed with the entire stack. From there,
# function updates can be deployed without the stack.
# If any permissions or libraries or dependencies are
# added, full stack must be deployed again.

# deploy function with entire stack to aws with:
# serverless deploy -v

# deploy only the function to aws with:
# serverless deploy function -f <functionName>

# invoke function via command line with:
# serverless invoke -f (function) <functionName> -l (list)

# create log stream and view logs with:
# serverless logs -f <functionName> -t (tail)

# destroy all functions with:
# serverless remove

import time

def hello(event, context):
    time.sleep(4)
    print('third update for cooper. ')
    return "hello-world-cooper"
