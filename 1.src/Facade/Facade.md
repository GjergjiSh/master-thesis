# Facade
- operations
- paths
- data models


```c++

#include <Facade.h>
#include <iostream>
#include <map>

struct Actor {
    std::string endpoint;
    enum class Http2Method {
        GET,
        POST,
        PUT,
        DELETE
    };
    typedef void (*GenericFunctionPointer)(void*);
};

Actor::Actor() {
    this->endpoint = "";
}

struct Url {
    std::string url;
    std::string base_path;
};


std::map<Url, Actor> ActorFactory::InitializeActors() {
    // Create the actors
    // Template injection here
    std::map<Url, Actor> actors  {
        {Resource("http://localhost:8000/sensor_data/{sid}"), Actor()},
    };
}

Facade::Facade() {
    // Initialize the http client
    this->httpClient = new HttpClient();
    this->actors = ActorFactory::InitializeActors();

    // Ideally I would like to do:
    actor.SetHttp2Method(Http2Method::GET);

    actor.SetCallback("http://localhost:8000/sensor_data", Facade::get_sensor_data);
    actor.SetCallback("http://localhost:8000/sensor_data", Facade::post_sensor_data);
    actor.SetCallback("http://localhost:8000/sensor_data", Facade::put_sensor_data);
}


// TODO: The parameters need to be flexible
// We need to figure out how to do this
GeneratedFunction::get_sensor_data(void* data) {
    // The Resource is injected by the handlebars template
    Resource resource = Resource("http://localhost:8000/sensor_data");

    // The Method is injected by the handlebars template
    Actor actor = actors[url, Http2Method::GET];

    actor.SendRequest();
}

Facade::Callback Facade::get_callback(std::string url) {
    return this->httpClient->get_callback(url);
}
```

# We need to figure out which parts of the code can be injected via the handlebars template
# We need to keep this design in mind when designing the interface of the facade
# How do we deal with path variables