#!/bin/bash

echo "Starting computation"
echo "Running add_object_SOR"
python scripts/add_object_SOR.py
echo "Running heatmap_objects"
python scripts/heatmap_objects.py
echo "Running objects_omega"
python scripts/objects_omega.py
echo "Running vibrating_string"
python scripts/vibrating_string.py
echo "Running visualize_heatmap_insulation"
python scripts/visualize_heatmap_insulation.py
echo "Running visualize_heatmap_objects"
python scripts/visualize_heatmap_objects.py
echo "Running visualize_Laplace"
python scripts/visualize_Laplace.py
echo "Running visualize_objects"
python scripts/visualize_objects.py
echo "Running visualize_time_dep_diff"
python scripts/visualize_time_dep_diff.py
echo "Running visualize_vibrating_string"
python scripts/visualize_vibrating_string.py
echo "Finished analysis, hooman. You can find figures in the results folder."
