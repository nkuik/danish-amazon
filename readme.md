[![Build Status](https://dev.azure.com/kubernetes-test/eks-practice/_apis/build/status/nkuik.slack-client?branchName=master)](https://dev.azure.com/kubernetes-test/eks-practice/_build/latest?definitionId=2&branchName=master)
![codecov](https://codecov.io/gh/nkuik/slack-client/branch/master/graph/badge.svg)

# Slack Client

Simple async client to receive events from a slack chatbot.

## Todo

- [X] Get sanic running
- [X] Fix config load
- [X] Automatic tests
- [X] Test coverage
- [X] Add health endpoint
- [X] Load config as object instead of file
- [X] Get docker image working with alpine image
- [X] Push app to Docker Hub after merging changes
- [X] Get app up on EKS (generic provide on Azure pipelines)
- [X] Create service on Kubernetes
- [ ] Add Nginx
- [ ] Automate EKS deployments (Helm)
- [ ] Actually get backend working with Slack Command
