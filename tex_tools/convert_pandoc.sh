#!/bin/bash
for s in $(ls /opt/input_data/); do docker exec mastersthesistext_devcontainer_pandoc_1 pandoc -t latex /opt/input_data/$s -o /opt/output_data/$(echo $s | sed 's/.md/.tex/g'); done