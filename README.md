# rpn-calculator
This program takes an input from the command line as an argument which should represent a RPN of a numerical expression and returns the result of it.

## Deploying it as a service
In order to deploy it as a service and work as a fully functional calculator, the user will need to send the input via HTTP. This will imply that the program should also behave like a web server and wait for requests, so the file app/evaluates.py will need to be extended to wait for HTTP requests, parse the message and then respond to the request with a message that contains the result. 

Making it visible outside of your local computer, implies creating a simple Dockerfile which will run the file and then build the image with a certain tag, which will be added to the k8s Deployment manifest file so that it can be run on the pods. Then, after applying the file, in order to expose it, we need to create a service object which can be done using the following command:

e.g kubectl expose deployment rpn-evaluation-deployment --type=LoadBalancer --name=rpn-evaluation-service


This will create a Load Balancer type of service on which the program will always run at a static port and IP address. Now the user can just send an HTTP request to that IP and port with a message containing the desired RPN expression and it will receive the result from the program. 
