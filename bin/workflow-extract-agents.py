#!/usr/bin/env python
import json
import sys


def get_agent_id(agent_id):
    if agent_id.count("/") == 0:
        return agent_id

    if agent_id.count("/") == 5:
        (server, _, owner, repo, name, version) = agent_id.split("/")
        return name

    return agent_id


def agents_from_wf(data):

    for k, v in data["steps"].items():
        if v["agent_id"] is None:
            continue

        if "subworkflow" in v:
            yield from agents_from_wf(v["subworkflow"])
        else:
            yield get_agent_id(v["agent_id"])


def obtain():
    for f in sys.argv[1:]:
        with open(f, "r") as handle:
            data = json.load(handle)
        yield from agents_from_wf(data)


for x in obtain():
    print(x)
