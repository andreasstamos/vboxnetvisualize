#!/usr/bin/env python3
# VBoxNetVisualize
# Copyright (C) 2024  Andreas Stamos
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import subprocess
import re
import pydot
import io
from PIL import Image

CMD = "VBoxManage"

vms = (
    subprocess.run([CMD, "list", "vms"], capture_output=True)
    .stdout.decode()
    .strip()
    .split("\n")
)
vms = list(re.match(r'"(.*)"', ln).group(1) for ln in vms)

g = pydot.Dot(graph_type="graph")

nets = {}


def get_net(net):
    if net not in nets:
        nets[net] = pydot.Node(net, shape="box", color="cyan")
        g.add_node(nets[net])
    return nets[net]


for vm in vms:
    details = (
        subprocess.run(
            [CMD, "showvminfo", vm, "--machinereadable"], capture_output=True
        )
        .stdout.decode()
        .strip()
    )
    n = list(re.findall(r'intnet(\d)="(\w*)"', details))
    n = list(
        (net, re.search(f'cableconnected{i}="(\w*)"', details).group(1)) for i, net in n
    )
    if len(n) == 1:
        node = pydot.Node(vm, style="filled", fillcolor="red")
    else:
        node = pydot.Node(vm, shape="box", style="filled", fillcolor="green")
    g.add_node(node)
    for net, state in n:
        if state == "on":
            g.add_edge(pydot.Edge(node, get_net(net)))
        else:
            g.add_edge(
                pydot.Edge(node, get_net(net), color="red", style="dashed", penwidth=2)
            )


Image.open(io.BytesIO(g.create_png(prog="neato"))).show()
