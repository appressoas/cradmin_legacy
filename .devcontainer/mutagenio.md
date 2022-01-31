# Mutagen IO

This is an alternative approach to high performance with docker on OSX and windows.
It is very simple, we just:

- Mount a persistent docker volume for the repo root.
- Clone the repo within the container via mutagen.io.
- Work in the container just like you would with a virtual machine.


## Changes to devcontainer.json

Uncomment the following two lines in devcontainer.json (do NOT commit this change):
```
	// "workspaceMount": "source=cradminlegacy_dockerdev_repo,destination=/workspace,type=volume",
	// "workspaceFolder": "/workspace",
```

# Using mutagen.io to sync host and docker image
**WARNING**: Make sure you have comitted and pushed all changes both locally (on the host machine), and within the docker container BEFORE
you start syncing with mutagen. Just in case something goes wrong. First time you read this (before you setup mutagen), just make sure it
is comitted and pushed locally.


## Install mutagen:
```
$ brew install mutagen-io/mutagen/mutagen
```

## First time mutagen setup

Setup a docker container for sync:
```
$ docker volume create cradminlegacy_dockerdev_mutagensync_volume
$ docker container create --name cradminlegacy_dockerdev_mutagensync_container -v cradminlegacy_dockerdev_repo:/volumes/sync mutagenio/sidecar
$ docker container start cradminlegacy_dockerdev_mutagensync_container
$ docker exec cradminlegacy_dockerdev_mutagensync_container chown 1000:1000 /volumes/sync
$ docker exec cradminlegacy_dockerdev_mutagensync_container chmod go+w /volumes/sync
```
**NOTE:** you need to do this again if you delete the ``cradminlegacy_dockerdev_mutagensync_container`` docker container
or the ``cradminlegacy_dockerdev_repo`` docker volume.

Create/start the mutagen sync daemon (the name can be anything you want, it is just used with the other mutagen commands):
```
$ mutagen sync create --name="cradminlegacy-dockerdev-sync" --sync-mode=two-way-resolved --default-owner-beta="id:1000" --default-group-beta="id:1000" --ignore 'node_modules/,.pytest_cache/,.vscode-atest-temp/,dbdev_tempdata/' . docker://cradminlegacy_dockerdev_mutagensync_container/volumes/sync
```

Run the following command, and wait for it to say _Status: Watching for changes_:
```
$ mutagen sync monitor cradminlegacy-dockerdev-sync
```

Mutagen sync is now ready. You can just CTRL-C out of the mutagen sync monitor process. The sync will continue in the background.

Reopen and reload container by using `Remote-containers`

## Pause and resume the mutagen sync
If you want to save some resource because you are not working on this project, simply pause
the sync process and stop the docker image with:

```
$ mutagen sync pause cradminlegacy-dockerdev-sync && docker container stop cradminlegacy_dockerdev_mutagensync_container
```

The use the following commands to resume:
```
$ docker container start cradminlegacy_dockerdev_mutagensync_container && mutagen sync resume cradminlegacy-dockerdev-sync
```

## Things to be careful about with mutagen sync

1. **We do sync .git/.** It does not really matter if you commit on host or in the container, but you should only do one of,
   and within the container is recommended since that is what the git integration in vscode does when you have the repo open
   in the container.
   Comitting and doing git operations like stage on both ends can lead to corruption of ``.git/``.
2. Starting the sync with uncomitted changes should be safe, but it is recommended to have a clean git with all changes up to
   date on both host and container before starting the sync.


## Useful mutagen commands

### Show sync progress and events in realtime
```
$ mutagen sync monitor cradminlegacy-dockerdev-sync
```

### Show/browse files that has been synced
Just use docker exec with normal linux commands as you would with any
docker image. Useful for debugging/checking that the sync works as expected..
```
$ docker exec cradminlegacy_dockerdev_mutagensync_container ls -l /volumes/sync/
$ docker exec cradminlegacy_dockerdev_mutagensync_container cat /volumes/sync/Pipfile
... etc ..
```

### List sync sessions
```
$ mutagen sync list
```

### Terminate the sync session
```
$ mutagen sync terminate cradminlegacy-dockerdev-sync
```


### Full mutagen cleanup
You normally do not need to do this unless something is wrong, or you need to change
the arguments for ``mutagen sync create``, but if you want a full cleanup, do this:
```
$ mutagen sync terminate cradminlegacy-dockerdev-sync
$ docker container stop cradminlegacy_dockerdev_mutagensync_container
$ docker container rm cradminlegacy_dockerdev_mutagensync_container
$ docker volume rm cradminlegacy_dockerdev_mutagensync_volume
```
After this, you can do the steps in _First time setup_ to start again
with a clean slate.


## Python interpreter
The name of the interpreter can now be without `cradminlegacy`. In a terminal, active the virtualenv with `pipen shell` to see the name of the interpreter (should be in the `persistent` folder)
