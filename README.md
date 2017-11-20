# Purpose   
One of problems I commonly run into is testing and verifying Salt states
for a stand alone minion or a cluster(Salt master with minions). This 
README focuses on the latter but the work here can be easily modified to
work for a single Salt minion.

I also wanted to this to embrace some "devops" principals 

* Ability to replicate a similar production environment
* provide a quick feedback loop
* Automate:
   * Bringing an environment up quickly
   * Ensure it is repeatable. 
* Testing

Nice to have:
* Plugging this into a a build process and have it read in the test results for pass/fail


## Requirements:
* docker
* docker-compose
* Python 3.6
* pipenv: `pip3 install pipenv`
* mo: `pip3 install mo`    

## Getting Started 

The steps below will launch a Salt master and two Salt minions.  To get you started the minions will expose ports 9090 and 9091 and the example states will setup nginx and serve a custom index.yaml.

1. `git clone https://github.com/chhibber/saltstack-docker.git` 
2. `mo up`
3. Make you Salt state edits.  The Salt states are mounted into the running salt-master instance. This allows you to modify them on the fly outside of the container
4. `docker exec saltstackdocker_master_1 salt "*" state.highstate`   
 

## Example 

To a see a full walkthrough that:
 * cleans ups
 * bootstraps a new environment
 * Runs highstate (puts nginx on the box and has it serve a index.yaml)
 * Runs tests against the minions to verify they are configured correctly
 * Modifies nginx to revert back to the default index file: `index.nginx-debian.html`
 * Run tests against the minions to verify the default index is in place

```
mo example-run
```


## Notable

* Using mo - a yaml based task runner. I appreciate and prefer the YAML based syntax of defining simple jobs over Make.
* Using pipenv for virtual env and dependency management
* Using testinfra to verify system configuration after running the Salt states