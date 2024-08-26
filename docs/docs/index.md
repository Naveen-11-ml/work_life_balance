# work_life_balance documentation!

## Description

Machine Learning Model to rate an individuals Work Life Balance in a scale of 1-10

## Commands

The Makefile contains the central entry points for common tasks related to this project.

### Syncing data to cloud storage

* `make sync_data_up` will use `aws s3 sync` to recursively sync files in `data/` up to `s3://remote-storage-life-notes/data/`.
* `make sync_data_down` will use `aws s3 sync` to recursively sync files from `s3://remote-storage-life-notes/data/` to `data/`.


