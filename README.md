# IsServiceUp
[![irc](https://img.shields.io/badge/irc%20channel-%23isserviceup-blue.svg)](https://webchat.freenode.net/?channels=isserviceup)

IsServiceUp helps you monitor all the cloud services you rely on in a single web page. 

![](https://raw.githubusercontent.com/marcopaz/is-service-up/master/Screenshot.png)

## Maintainers
* [Marco Pazzaglia](https://github.com/marcopaz)
* [Alessandro Cosentino](https://github.com/cosenal)


## How to run
### Using Docker
`docker-compose up --build`

and you're up and running! :sparkles:
## How to contribute
If you want to add something to the project, please fork this repository and create a Pull request.

### Extend it with a new service
Adding a new service that you want to be monitored is straightforward.
Of course, this is only possible if the service exposes a status page. Find that out first. 

Next, figure out if the status page is built using [Atlassian StatusPage](https://www.statuspage.io/). If that's the case, check out [this commit](https://github.com/marcopaz/is-service-up/commit/39df5a9124a01d39d66e7637a297896827a4262e) for an example on how to create your new service.

If it's a more generic status page, then the implementation depends on the specific service. If you're lucky, the status will be exposed through a beautiful API, like in [the case of GitHub](https://github.com/marcopaz/is-service-up/blob/master/isserviceup/services/github.py). Otherwise, find your inspiration from all others services that we have implemented for you. Good luck! :satellite:




