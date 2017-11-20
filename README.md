# Purpose   
One of problems I commonly run into is testing and verifying Salt states
for a stand alone minion or a cluster (Salt master with minions). This 
README focuses on the latter but the work here can be easily modified to
work for a single Salt minion.

I also wanted this example to embrace some "devops" principles 

* Ability to replicate a similar production environment
* Provide a quick feedback loop
* Automate:
   * Bringing an environment up quickly
   * Ensure it is repeatable. 
* Testing


## Requirements:
* docker
* docker-compose
* Python 3.6
* pipenv: `pip3 install pipenv`
* mo: `pip3 install mo`    

## Getting Started 

The steps below will launch a Salt master and two Salt minions.  To get you started, the minions will expose ports 9090 and 9091 and the example states will setup nginx and serve a custom index.yaml.

1. `git clone https://github.com/chhibber/saltstack-docker.git` 
2. `mo up`
3. Make your Salt state edits. The Salt states are mounted into the running salt-master instance. This allows you to modify them on the fly outside of the container
4. `docker exec saltstackdocker_master_1 salt "*" state.highstate`   
 

## Example 

To a see a full walkthrough that:
 * Cleans up
 * Bootstraps a new environment
 * Runs highstate (puts nginx on the box and has it serve a index.yaml)
 * Runs tests against the minions to verify they are configured correctly
 * Modifies nginx to revert back to the default index file: `index.nginx-debian.html`
 * Run tests against the minions to verify the default index is in place

```
mo example-run
```


## Notable

* Using mo - a yaml based task runner. I appreciate and prefer the YAML based syntax of defining simple jobs over Make.  You see this as a common pattern in a number of modern build systems.
* Using pipenv for virtual env and dependency management
* Using testinfra to verify system configuration after running the Salt states.  The backend connection features are great and took what originally would have been a tedious job and made it really simple. 