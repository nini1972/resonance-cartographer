import json
import re
import networkx as nx
import matplotlib.pyplot as plt
from collections import defaultdict
from pathlib import Path

# 1. Function to extract mathematical symbols from LaTeX strings
def extract_symbols(latex_str):
    # This regex looks for common LaTeX commands (\Lambda, \Phi), 
    # tensor notations (G_{\mu\nu}), and subscripted variables (a_0, k_B)
    pattern = r'(\\[A-Za-z]+(?:_(?:\{[^{}]*\}|[A-Za-z0-9]+))?(?:\^(?:\{[^{}]*\}|[A-Za-z0-9]+))?)|([A-Za-z]+_(?:\{[^{}]*\}|[A-Za-z0-9]+)(?:\^(?:\{[^{}]*\}|[A-Za-z0-9]+))?)'
    matches = re.findall(pattern, latex_str)
    ignored_commands = {
        '\\approx', '\\ast', '\\bar', '\\cdot', '\\ddot', '\\dot', '\\dots',
        '\\exp', '\\frac', '\\geq', '\\gg', '\\hat', '\\in', '\\infty',
        '\\int', '\\langle', '\\left', '\\leq', '\\lesssim', '\\ln',
        '\\mathcal', '\\max', '\\neq', '\\nabla', '\\partial', '\\pm',
        '\\propto', '\\quad', '\\rangle', '\\right', '\\rm', '\\sim',
        '\\simeq', '\\sqrt', '\\sum', '\\text', '\\times', '\\mathbf',
        '\\mathrm', '\\rightarrow'
    }

    symbols = set()
    for match in matches:
        symbol = match[0] if match[0] else match[1]
        command_match = re.match(r'\\[A-Za-z]+', symbol)
        command = command_match.group() if command_match else symbol
        if command not in ignored_commands:
            symbols.add(symbol.strip())
    return symbols

# 2. Function to build the graph
def build_reverse_time_graph(json_file_path):
    # Load your JSON data (assuming it's a list of JSON objects or JSONL)
    data = []
    with open(json_file_path, 'r', encoding='utf-8') as f:
        if Path(json_file_path).suffix == '.jsonl':
            for line in f:
                data.append(json.loads(line))
        else:
            data = json.load(f)
            if not isinstance(data, list):
                data = [data]

    G = nx.Graph()
    
    # Track which levels each symbol appears in
    symbol_levels = defaultdict(set)
    
    # Add nodes and edges
    for entry in data:
        concept_name = entry.get('concept', 'Unknown Concept')
        level = entry.get('level', 0)
        
        # Add concept node
        G.add_node(concept_name, type='concept', level=level)
        
        equations = entry.get('equations', [])
        for eq in equations:
            symbols = extract_symbols(eq)
            for sym in symbols:
                # Add symbol node
                G.add_node(sym, type='symbol')
                
                # Link symbol to concept
                G.add_edge(concept_name, sym)
                
                # Track the level where this symbol appears
                symbol_levels[sym].add(level)

    # 3. Find the "Seed Variables" (appear in Levels 1, 2, and 3)
    seed_variables = []
    for sym, levels in symbol_levels.items():
        if {1, 2, 3}.issubset(levels):
            seed_variables.append(sym)
            
    return G, seed_variables

# 4. Visualization Function
def visualize_graph(G, seed_variables, output_path):
    plt.figure(figsize=(18, 12))
    
    # Color map for nodes
    color_map = []
    for node in G:
        if G.nodes[node].get('type') == 'concept':
            level = G.nodes[node].get('level')
            if level == 1: color_map.append('lightblue')
            elif level == 2: color_map.append('lightgreen')
            elif level == 3: color_map.append('salmon')
            else: color_map.append('grey')
        else:
            # Highlight Seed Variables in Gold
            if node in seed_variables:
                color_map.append('gold')
            else:
                color_map.append('black')
                
    # Layout: Spring layout works well, but k adjusts spacing
    pos = nx.spring_layout(G, k=0.15, iterations=50)
    
    # Draw edges faintly
    nx.draw_networkx_edges(G, pos, alpha=0.2, edge_color='grey')
    
    # Draw nodes
    nx.draw_networkx_nodes(G, pos, node_color=color_map, node_size=50, alpha=0.8)
    
    plt.axis('off')
    plt.savefig(output_path, dpi=200, bbox_inches='tight')
    plt.close()

# --- MAIN EXECUTION ---
if __name__ == "__main__":
    script_directory = Path(__file__).resolve().parent
    file_path = script_directory / 'equations.jsonl'
    output_path = script_directory / 'assets' / 'images' / 'reverse_time_graph.png'
    seeds_output_path = script_directory / 'seed_crystals.json'


    
    print("Building the Reverse-Time Graph...")
    graph, seeds = build_reverse_time_graph(file_path)
    
    print("\n=== SEED CRYSTALS (Variables surviving Level 1 -> 2 -> 3) ===")
    for seed in sorted(seeds):
        print(f"- {seed}")

    with open(seeds_output_path, 'w', encoding='utf-8') as f:
        json.dump(
            {
                'source_file': file_path.name,
                'seed_count': len(seeds),
                'seed_crystals': sorted(seeds),
            },
            f,
            indent=2,
            ensure_ascii=False,
        )

    print("\nVisualizing graph... (Gold nodes are the Seed Crystals; text is hidden)")
    visualize_graph(graph, seeds, output_path)
    print(f"Saved network map to: {output_path}")
    print(f"Saved seed data to: {seeds_output_path}")