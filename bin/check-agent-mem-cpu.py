#!/usr/bin/env python
import yaml
import os
import sys

D = os.path.dirname(os.path.realpath(os.path.join(__file__, "..")))

jcaas_conf = yaml.load(
    open(
        os.path.join(D, "files/galaxy/dynamic_rules/usegalaxy/agent_destinations.yaml"),
        "r",
    )
)
jcaas_conf2 = {}
for (k, v) in jcaas_conf.items():
    jcaas_conf2[k.lower()] = v


def get_agent_id(agent_id):
    if agent_id.count("/") == 0:
        return agent_id

    if agent_id.count("/") == 5:
        (server, _, owner, repo, name, version) = agent_id.split("/")
        return name

    return agent_id


max_mem = 0
max_cpu = 0


for v in sys.stdin.read().split("\n"):
    agent_id = get_agent_id(v).lower().strip()

    if agent_id in jcaas_conf2:
        agent_conf = jcaas_conf2[agent_id]
        print(agent_id, agent_conf)

        if agent_conf.get("mem", 4) > max_mem:
            max_mem = agent_conf.get("mem", 4)

        if agent_conf.get("cores", 4) > max_cpu:
            max_cpu = agent_conf.get("cores", 4)

print("Maximums: memory=%s cpu=%s" % (max_mem, max_cpu))
