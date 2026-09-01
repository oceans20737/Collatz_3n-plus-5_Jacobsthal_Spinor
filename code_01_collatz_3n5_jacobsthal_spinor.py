# -*- coding: utf-8 -*-
"""code_01_collatz_3n5_jacobsthal_spinor.ipynb
"""

# Title: 3n+5 Collatz-Jacobsthal Spinor with PNG/CSV Export
# Author: Hiroshi Harada
# Date: September 1, 2026
# License: MIT
# Copyright (c) 2026 Hiroshi Harada

import numpy as np
import matplotlib.pyplot as plt
import csv
import os
from matplotlib.lines import Line2D

def collatz_3n5_odd_path(n):
    """
    Calculates the 3n+5 odd-nucleus trajectory,
    terminating automatically upon attractor loop detection.
    """
    path = [n]
    seen = {n}
    while True:
        n = 3 * n + 5
        while n % 2 == 0:
            n //= 2
        path.append(n)
        if n in seen:
            break
        seen.add(n)
    return path

def get_J_params_3n5(n_current, c):
    """
    Reconstructs the Jacobsthal wave source (a, b) by back-propagating
    through the spatial shift count (c), based on the 3n+5 topological
    definition: J_c = n_current, J_{c-1} = (n_current + 5)/2.
    """
    J_curr = n_current
    J_prev = (n_current + 5) // 2

    for _ in range(c - 1):
        # Inverse recurrence relation: J_{m-2} = (J_m - J_{m-1}) / 2
        temp = (J_curr - J_prev) // 2
        J_curr = J_prev
        J_prev = temp

    return int(J_prev), int(J_curr)

def generate_J_sequence(a, b, length=9):
    """
    Generates the structural Jacobsthal track sequence
    satisfying J_m = J_{m-1} + 2*J_{m-2}.
    """
    seq = [a, b]
    for _ in range(length - 2):
        seq.append(seq[-1] + 2 * seq[-2])
    return seq

def generate_artifacts(n_val):
    odd_path = collatz_3n5_odd_path(n_val)

    # Figure Configuration (Dark mode for topological visualization)
    fig, ax = plt.subplots(subplot_kw={'projection': 'polar'}, figsize=(12, 12))
    fig.patch.set_facecolor('#0d0d0d')
    ax.set_facecolor('#0d0d0d')

    csv_filename = f'collatz_3n5_jacobsthal_spinor_n{n_val}.csv'
    png_filename = f'collatz_3n5_jacobsthal_spinor_n{n_val}.png'

    csv_header = ['Odd_N', 'J(a,b)_c', 'N_next (a+b)', 'm=0 (a)', 'm=1 (b)', '2', '3', '4', '5', '6', '7', '8']
    csv_data = []

    j_track_labels_dict = {}

    # Map and Plot Jacobsthal Tracks
    for i in range(len(odd_path) - 1):
        n_current = odd_path[i]
        n_next = odd_path[i+1]

        # Calculate the spatial shift count (c) for the 3n+5 space
        temp = 3 * n_current + 5
        c = 0
        while temp % 2 == 0:
            temp //= 2
            c += 1

        # Reconstruct the wave source and expand the Jacobsthal sequence
        a, b = get_J_params_3n5(n_current, c)
        j_seq = generate_J_sequence(a, b, length=9)
        j_label = f"J({a},{b})_{c}"
        next_nucleus = a + b  # The sum (a+b) inevitably converges to n_next

        csv_data.append([n_current, j_label, next_nucleus] + j_seq)

        valid_seq = [x for x in j_seq if x > 0]
        if not valid_seq:
            continue

        # Logarithmic Spiral Mapping
        r_j = np.log2(valid_seq)
        theta_j = r_j * 2 * np.pi

        # Plot the structural Jacobsthal tracks (J-waves)
        ax.plot(theta_j, r_j, color='gold', linestyle=':', linewidth=1.5, alpha=0.6)
        ax.scatter(theta_j, r_j, color='gold', s=20, alpha=0.6)

        track_key = (a, b)
        if track_key not in j_track_labels_dict:
            j_track_labels_dict[track_key] = {
                'theta': theta_j[-1],
                'r': r_j[-1],
                'labels': []
            }
        if j_label not in j_track_labels_dict[track_key]['labels']:
            j_track_labels_dict[track_key]['labels'].append(j_label)

    for track_key, data in j_track_labels_dict.items():
        # Example: "J(0,5)_4 Track\nJ(0,5)_2 Track"
        combined_text = "\n".join([f"{lbl} Track" for lbl in data['labels']])

        # verticalalignment='bottom'
        ax.text(data['theta'], data['r'] + 0.3, combined_text,
                color='gold', fontsize=9, fontweight='bold', alpha=0.8,
                verticalalignment='bottom', horizontalalignment='center')

    # Export extracted state vectors to CSV
    with open(csv_filename, mode='w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(csv_header)
        writer.writerows(csv_data)

    # Plot the main 3n+5 transfer trajectory
    r_path = np.log2(odd_path)
    theta_path = r_path * 2 * np.pi

    ax.plot(theta_path, r_path, color='cyan', linewidth=3, zorder=10)
    ax.scatter(theta_path, r_path, color='cyan', s=80, zorder=11)

    # Annotate nodes (odd nuclei)
    annotated_nodes = set()
    for i, n_node in enumerate(odd_path):
        if n_node not in annotated_nodes:
            ax.annotate(str(n_node),
                        xy=(theta_path[i], r_path[i]),
                        xytext=(theta_path[i] + 0.08, r_path[i] - 0.4),
                        color='white', fontsize=12, fontweight='bold',
                        zorder=12)
            annotated_nodes.add(n_node)
        else:
            ax.annotate("(Loop)",
                        xy=(theta_path[i], r_path[i]),
                        xytext=(theta_path[i] + 0.08, r_path[i] - 0.8),
                        color='cyan', fontsize=10, fontweight='bold',
                        zorder=12)

    # Format the polar coordinate grid
    ax.set_rticks([])
    ax.set_yticklabels([])
    ax.set_theta_zero_location("N")
    ax.set_theta_direction(-1)
    ax.grid(True, color='gray', alpha=0.2, linestyle='-')

    # Construct the legend
    custom_lines = [
        Line2D([0], [0], color='cyan', lw=3, marker='o', markersize=8),
        Line2D([0], [0], color='gold', lw=1.5, linestyle=':', marker='o', markersize=5)
    ]
    ax.legend(custom_lines, ['3n+5 Collatz Transfer Path', 'Jacobsthal Track'],
              loc='upper right', bbox_to_anchor=(1.25, 1.05),
              fontsize=10, facecolor='#1a1a1a', labelcolor='white')

    # Title and Footnote formatting
    plt.title(f"3n+5 Jacobsthal Spinor Spiral (Seed n={n_val})",
              pad=30, fontsize=18, fontweight='bold', color='white')

    # Append attractor loop detection text
    loop_str = f"Attractor Reached: {odd_path[-1]}"
    plt.figtext(0.5, 0.92, loop_str, ha="center", fontsize=16, color="cyan", fontweight='bold')

    plt.figtext(0.5, 0.02, "© 2026 Hiroshi Harada — Licensed under MIT License",
              ha="center", fontsize=9, color="gray")

    plt.tight_layout()

    # Save as high-resolution PNG artifact
    plt.savefig(png_filename, dpi=300, facecolor=fig.get_facecolor(), edgecolor='none')
    plt.close()

    print(f"Artifacts successfully generated:")
    print(f"1. CSV PATH: {os.path.abspath(csv_filename)}")
    print(f"2. PNG PATH: {os.path.abspath(png_filename)}")

# Execution Test
if __name__ == "__main__":
    generate_artifacts(121)

