#!/usr/bin/env python3
"""Backfill two Chem 2025 candidate summaries transcribed from publisher pages."""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
SUMMARIES = {
    '10.1016/j.chempr.2024.10.027': (
        'Lead-halide perovskites exhibit highly tunable optical properties, making them suitable for applications in photovoltaics and optoelectronics. Although considerable effort has gone into the development of methods that accurately predict the optical properties of perovskite materials based on structure, the reverse—predicting composition from optical data—is far less explored. In this study, high-throughput approaches were employed to synthesize and spectroscopically analyze a wide array of perovskites composed of mono-halide, di-halide, and tri-halides with a general formula, MAxCs1−xPb(ClxBryI1−x−y)3. The spectroscopic data were used to train an artificial neural network (ANN)-based chemical space-property predictor model designed to work with multiple responses and multiple predictors. The model predicted the chemical composition of perovskites from terahertz (THz) Raman spectroscopic data with approximately 85% accuracy. When the dataset also incorporated UV-visible spectroscopic data, the accuracy increased to nearly 92%. This study opens the possibility of real-time monitoring and defect detection, degradation analysis, and streamlined material selection and optimization of perovskite materials in industrial production.',
        'https://www.sciencedirect.com/science/article/abs/pii/S2451929424005539',
    ),
    '10.1016/j.chempr.2025.102624': (
        'Protein-based nanomedicines represent a paradigm shift in cancer theranostics, capitalizing on superior biocompatibility, molecular recognition, and multifunctional adaptability. This review delineates their evolution from supramolecular self-assembly to artificial intelligence (AI)-driven design, emphasizing their transformative role in cancer chemotherapy, phototherapy, chemodynamic therapy, and immunotherapy. Supramolecular strategies, including metal coordination, electrostatic interactions, host-guest chemistry, hydrogen bonding, π-π stacking, and hydrophobic interactions, not only enable precise control over protein assemblies but also facilitate drug delivery and performance. AI tools like AlphaFold 3 and RFdiffusion have accelerated de novo protein design and dynamic interaction prediction, overcoming limitations in structural prototyping. Despite breakthroughs, challenges persist in the mechanistic insights into assembly dynamics, experimental validation of AI-generated constructs, and scalable clinical translation. Future directions prioritize integrated theranostics platforms, multi-omics-guided precision medicine, and synthetic biology. By synergizing supramolecular chemistry, AI, and nanotechnology, this review envisions protein-based nanomedicines as intelligent, adaptive systems poised to redefine paradigms of cancer theranostics.',
        'https://www.sciencedirect.com/science/article/abs/pii/S2451929425002141',
    ),
}

for rel in [
    'metadata/j-73ae0ea805/2025/papers.json',
    'metadata/j-73ae0ea805/2025/ai4s.json',
    'metadata/2025/ai4s.json',
    'reviews/2025/Blueblue1101.json',
]:
    path = ROOT / rel
    rows = json.loads(path.read_text())
    matched = set()
    for row in rows:
        doi = row.get('doi') or row['id']
        if doi not in SUMMARIES:
            continue
        assert not row.get('abstract') or row['abstract'] == SUMMARIES[doi][0]
        row['abstract'] = SUMMARIES[doi][0]
        matched.add(doi)
    assert matched == set(SUMMARIES), (rel, matched)
    path.write_text(json.dumps(rows, ensure_ascii=False, indent=2) + '\n')
    print(rel, len(matched))
