# GPU Specs

Attribute (Unit) | H100 | L40S | L4 | A100 PCIe 40GB | A100 PCIe 80GB | A100 SXM4 40GB | A100 SXM4 80GB | A10 | T4 | Quadro RTX 5000 | V100 PCIe | V100 SXM2 | V100S PCIe
--- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---
FP64 (TFLOPS) | 25.6 | 1.4 | 0.5 | 9.7 | 9.7 | 9.7 | 9.7 | 1 | ? | 0.3 | 7.1 | 7.8 | 8.2
FP64 Tensor Core (TFLOPS) | 51 | ? | ? | 19.5 | 19.5 | 19.5 | 19.5 | ? | N/A | N/A | N/A | N/A | N/A
FP32 (TFLOPS) | 51.2 | 91.6 | 30.3 | 19.5 | 19.5 | 19.5 | 19.5 | 31.2 | 8.1 | 11.2 | 14.1 | 15.7 | 16.4
TF32 Tensor Core (TFLOPS) | ? | 183 | 60 | 156 | 156 | 156 | 156 | 62.5 | N/A | N/A | 112 | 125 | N/A
TF32 Tensor Core with Sparsity (TFLOPS) | 756 | 366 | 120 | 312 | 312 | 312 | 312 | 125 | N/A | N/A | N/A | N/A | N/A
FP16 (TFLOPS) | 204.9 | 91.6 | 30.3 | 78 | 78 | 78 | 78 | 31.2 | 65 | 22.3 | 28.3 | 31.3 | 32.8
FP16 Tensor Core (TFLOPS) | ? | 362 | 121 | 312 | 312 | 312 | 312 | ? | ? | ? | 112 | 125 | 130
FP16 Tensor Core with Sparsity (TFLOPS) | ? | 733 | 242 | 624 | 624 | 624 | 624 | ? | ? | ? | ? | ? | ?
BF16 (TFLOPS) | ? | ? | ? | ? | ? | ? | ? | ? | N/A | N/A | N/A | N/A | N/A
BF16 Tensor Core (TFLOPS) | ? | 362 | 121 | 312 | 312 | 312 | 312 | 125 | N/A | N/A | N/A | N/A | N/A
BF16 Tensor Core with Sparsity (TFLOPS) | 1513 | 733 | 242 | 624 | 624 | 624 | 624 | 250 | N/A | N/A | N/A | N/A | N/A
FP8 (TFLOPS) | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A
FP8 Tensor Core (TFLOPS) | ? | 733 | 242 | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A
FP8 Tensor Core with Sparsity (TFLOPS) | 3026 | 1466 | 485 | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A
INT8 (TOPS) | ? | ? | ? | ? | ? | ? | ? | ? | 130 | ? | ? | ? | ?
INT8 Tensor Core (TOPS) | ? | 733 | 242 | 624 | 624 | 624 | 624 | 250 | ? | ? | N/A | N/A | N/A
INT8 Tensor Core with Sparsity (TOPS) | 3026 | 1466 | 485 | 1248 | 1248 | 1248 | 1248 | 500 | ? | ? | N/A | N/A | N/A
INT4 (TOPS) | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A
INT4 Tensor Core (TOPS) | ? | 733 | ? | ? | ? | ? | ? | 500 | 260 | ? | N/A | N/A | N/A
INT4 Tensor Core with Sparsity (TOPS) | ? | 1466 | ? | ? | ? | ? | ? | 1000 | ? | ? | N/A | N/A | N/A
**Architecture Details** |  |  |  |  |  |  |  |  |  |  |  |  |  | 
GPU Name | H100 | L40S | L4 | A100 PCIe 40GB | A100 PCIe 80GB | A100 SXM4 40GB | A100 SXM4 80GB | A10 | T4 | Quadro RTX 5000 | V100 PCIe | V100 SXM2 | V100S PCIe
Manufacturer | NVIDIA | NVIDIA | NVIDIA | NVIDIA | NVIDIA | NVIDIA | NVIDIA | NVIDIA | NVIDIA | NVIDIA | NVIDIA | NVIDIA | NVIDIA
Architecture | Hopper | Ada Lovelace | Ada Lovelace | Ampere | Ampere | Ampere | Ampere | Ampere | Turing | Turing | Volta | Volta | Volta
NVIDIA RT Cores | ? | 142 (3rd gen) | 60 (3rd gen) | ? | ? | ? | ? | 72 (2nd gen) | ? | 48 | N/A | N/A | N/A
NVIDIA Tensor Cores | 456 (4th gen) | 568 (4th gen) | 240 (4th gen) | 432 (3rd gen) | 432 (3rd gen) | 432 (3rd gen) | 432 (3rd gen) | 288 (3rd gen) | 320 (2nd gen) | 384 (2nd gen) | 640 (1st gen) | 640 (1st gen) | 640 (1st gen)
NVIDIA CUDA Cores | 14592 | 18176 | 7424 | 6912 | 6912 | 6912 | 6912 | 9216 | 2560 | 3072 | 5120 | 5120 | 5120
GPU Memory (GB) | 80 | 48 | 24 | 40 | 80 | 40 | 80 | 24 | 16 | 16 | 16/32 | 16/32 | 32
Memory Bandwidth (GB/s) | 2048 | 864 | 300 | 1555 | 1935 | 1555 | 2039 | 600 | 300 | 448 | 900 | 900 | 1134
Interconnect Type | PCIe Gen5 | PCIe Gen4 | PCIe Gen4 | PCIe Gen4 | PCIe Gen4 | NVLink | NVLink | PCIe Gen4 | PCIe Gen3 | PCIe Gen3 | PCIe Gen3 | NVLink | PCIe Gen3
Encoders and Decoders | 0, 7 | 3, 3 | 2, 4 | 0, 5 | 0, 5 | 0, 5 | 0, 5 | 1, 2 | 1, 2 | 1, 2 | 3, 1 | 3, 1 | 3, 1
CUDA Compute Capability | 9 | 8.9 | 8.9 | 8.0 | 8 | 8.0 | 8 | 8.6 | 7.5 | 7.5 | 7 | 7 | 7
Power Consumption (W) | 350 | 300 | 72 | 250 | 300 | 400 | 400 | 150 | 70 | 230 | 250 | 300 | 250

## Data Conventions

This page presents GPU specifications, following a standardized data structure to ensure clarity and consistency:

- **Unsupported Precision:**
  The value `N/A` indicates that a specific precision (e.g., FP8) is **not natively supported** by the GPU.

- **Missing Data:**
  The value `?` means that the information is currently unavailable or not confirmed.

If you have questions or feedback, feel free to [open an issue](https://github.com/gmasse/gpu-specs/issues) on the project repository.
