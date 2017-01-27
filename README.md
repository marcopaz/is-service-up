# IsServiceUp

IsServiceUp helps you monitor all the cloud services you rely on in a single web page. 

You can customize it with the services you want to monitor and host it on your own server.

![](https://raw.githubusercontent.com/marcopaz/is-service-up/master/Screenshot.png)

Sorry, Compose, bad timing :smile:

## How to run
### Using Docker
`docker-compose up --build`

and you're up and running! :sparkles:
### List of services
You can customize very easily the list of services you want to monitor by editing the variable `SERVICES` in the [config file](https://github.com/marcopaz/is-service-up/blob/master/isserviceup/config/config.py).

## How to contribute
If you want to add something to the project, please fork this repository and create a Pull request.

### Extend it with a new service

The way services are handled is based on a _plugin_ system, so monitoring a new service is straightforward: you can either file a feature request and hope that someone will implement the plugin, or you can implement it yourself. If you do decide to implement a plugin for a new service, we'd be thankful if you could share it with everyone by creating a pull request on this repository...thanks!

Of course, creating a plugin for a new service is only possible if the service exposes a status page. Find that out first. 

Next, figure out if the status page is built using [Atlassian StatusPage](https://www.statuspage.io/). If that's the case, check out [this commit](https://github.com/marcopaz/is-service-up/commit/39df5a9124a01d39d66e7637a297896827a4262e) for an example on how to create your plugin.

If it's a more generic status page, then the implementation depends on the specific service. If you're lucky, the status will be exposed through a beautiful API, like in [the case of GitHub](https://github.com/marcopaz/is-service-up/blob/master/isserviceup/services/github.py). Otherwise, find your inspiration from all others services that we have implemented for you. Good luck! :satellite:

## Maintainers
* [Marco Pazzaglia](https://github.com/marcopaz)
* [Alessandro Cosentino](https://github.com/cosenal)



