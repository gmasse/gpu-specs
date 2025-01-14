# GPU Specifications for AI Projects

Welcome to the **GPU Specifications for AI Projects** repository!  
This project aims to centralize detailed specifications for GPUs, particularly in the context of AI workloads. 

## Why This Project?

Finding comprehensive and accurate GPU specifications for AI can be challenging. Many sources are either incomplete, inconsistent, or unavailable. This repository consolidates information into a single, accessible resource to assist AI researchers, developers, and enthusiasts.

If you believe this project duplicates an existing effort, or if a similar database already exists, please let us know by opening an issue or contacting us directly. Collaboration or linking efforts can benefit the entire community!

## What’s Included?

The core of this project is a [JSON database](data/specs.json) containing detailed specifications of GPUs:
- Precision support (e.g., FP32, FP16, INT8, etc.)
- Compute & Memory capabilities
- Additional details relevant to AI workloads

The JSON data is rendered into:
- [HTML](https://g.masse.me/gpu-specs) for easy browsing.
- [Markdown](specs.md) for lightweight documentation.

## Contributing

If you spot errors, have missing data, or can add reliable sources, we welcome your input!
See the [CONTRIBUTING.md](CONTRIBUTING.md) file for details.

## Roadmap

- Add missing specifications for GPUs.
- Expand support to cover GPUs from various vendors (NVIDIA, AMD, etc.).

## Sample GPU Specifications

Below is a sample of the GPU specifications data included in the repository:

Attribute (Unit) | H100 | L40S | A100 PCIe 80GB
--- | --- | --- | ---
FP64 (TFLOPS) | 25.6 | 1.4 | 9.7
FP64 Tensor Core (TFLOPS) | 51 | ? | 19.5
FP32 (TFLOPS) | 51.2 | 91.6 | 19.5
TF32 Tensor Core (TFLOPS) | ? | 183 | 156
TF32 Tensor Core with Sparsity (TFLOPS) | 756 | 366 | 312
FP16 (TFLOPS) | 204.9 | 91.6 | 78
FP16 Tensor Core (TFLOPS) | ? | 362 | 312
FP16 Tensor Core with Sparsity (TFLOPS) | ? | 733 | 624
BF16 (TFLOPS) | ? | ? | ?
BF16 Tensor Core (TFLOPS) | ? | 362 | 312
BF16 Tensor Core with Sparsity (TFLOPS) | 1513 | 733 | 624
FP8 (TFLOPS) | N/A | N/A | N/A
FP8 Tensor Core (TFLOPS) | ? | 733 | N/A
FP8 Tensor Core with Sparsity (TFLOPS) | 3026 | 1466 | N/A
INT8 (TOPS) | ? | ? | ?
INT8 Tensor Core (TOPS) | ? | 733 | 624
INT8 Tensor Core with Sparsity (TOPS) | 3026 | 1466 | 1248
INT4 (TOPS) | N/A | N/A | N/A
INT4 Tensor Core (TOPS) | ? | 733 | ?
INT4 Tensor Core with Sparsity (TOPS) | ? | 1466 | ?
**Architecture Details** |  |  |  | 
GPU Name | H100 | L40S | A100 PCIe 80GB
Manufacturer | NVIDIA | NVIDIA | NVIDIA
Architecture | Hopper | Ada Lovelace | Ampere
NVIDIA RT Cores | ? | 142 (3rd gen) | ?
NVIDIA Tensor Cores | 456 (4th gen) | 568 (4th gen) | 432 (3rd gen)
NVIDIA CUDA Cores | 14592 | 18176 | 6912
GPU Memory (GB) | 80 | 48 | 80
Memory Bandwidth (GB/s) | 2048 | 864 | 1935
Interconnect Type | PCIe Gen5 | PCIe Gen4 | PCIe Gen4
Encoders and Decoders | 0, 7 | 3, 3 | 0, 5
CUDA Compute Capability | 9 | 8.9 | 8
Power Consumption (W) | 350 | 300 | 300

