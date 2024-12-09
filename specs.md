Attribute (Unit) | V100 | V100S | Quadro RTX 5000 | T4 | L4 | A10 | L40S | A100 | H100
--- | --- | --- | --- | --- | --- | --- | --- | --- | ---
FP64 (TFLOPS) | 7 | 8.2 | 0.3 | ? | 0.5 | 1 | 1.4 | 9.7 | 25.6
FP64 Tensor Core (TFLOPS) | N/A | N/A | N/A | N/A | ? | ? | ? | 19.5 | 51
FP32 (TFLOPS) | 14 | 16.4 | 11.2 | 8.1 | 30.3 | 31.2 | 91.6 | 19.5 | 51.2
TF32 Tensor Core (TFLOPS) | N/A | N/A | N/A | N/A | 60 | 62.5 | 183 | 156 | ?
TF32 Tensor Core with Sparsity (TFLOPS) | N/A | N/A | N/A | N/A | 120 | 125 | 366 | 312 | 756
FP16 (TFLOPS) | 28.3 | 32.7 | 22.3 | 65 | 30.3 | 31.2 | 91.6 | 78 | 204.9
FP16 Tensor Core (TFLOPS) | 112 | 130 | ? | ? | 121 | ? | 362 | 312 | ?
FP16 Tensor Core with Sparsity (TFLOPS) | ? | ? | ? | ? | 242 | ? | 733 | 624 | ?
BF16 (TFLOPS) | N/A | N/A | N/A | N/A | ? | ? | ? | ? | ?
BF16 Tensor Core (TFLOPS) | N/A | N/A | N/A | N/A | 121 | 125 | 362 | 312 | ?
BF16 Tensor Core with Sparsity (TFLOPS) | N/A | N/A | N/A | N/A | 242 | 250 | 733 | 624 | 1513
FP8 (TFLOPS) | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A
FP8 Tensor Core (TFLOPS) | N/A | N/A | N/A | N/A | 242 | N/A | 733 | N/A | ?
FP8 Tensor Core with Sparsity (TFLOPS) | N/A | N/A | N/A | N/A | 485 | N/A | 1466 | N/A | 3026
INT8 (TOPS) | ? | ? | ? | 130 | ? | ? | ? | ? | ?
INT8 Tensor Core (TOPS) | N/A | N/A | ? | ? | 242 | 250 | 733 | 624 | ?
INT8 Tensor Core with Sparsity (TOPS) | N/A | N/A | ? | ? | 485 | 500 | 1466 | 1248 | 3026
INT4 (TOPS) | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A
INT4 Tensor Core (TOPS) | N/A | N/A | ? | 260 | ? | 500 | 733 | ? | ?
INT4 Tensor Core with Sparsity (TOPS) | N/A | N/A | ? | ? | ? | 1000 | 1466 | ? | ?
**Architecture Details** |  |  |  |  |  |  |  |  |  | 
GPU Name | V100 | V100S | Quadro RTX 5000 | T4 | L4 | A10 | L40S | A100 | H100
Manufacturer | NVIDIA | NVIDIA | NVIDIA | NVIDIA | NVIDIA | NVIDIA | NVIDIA | NVIDIA | NVIDIA
Architecture | Volta | Volta | Turing | Turing | Ada Lovelace | Ampere | Ada Lovelace | Ampere | Hopper
NVIDIA RT Cores | ? | ? | 48 | ? | 60 (3rd gen) | 72 (2nd gen) | 142 (3rd gen) | ? | ?
NVIDIA Tensor Cores | 640 (1st gen) | 640 (1st gen) | 384 (2nd gen) | 320 (2nd gen) | 240 (4th gen) | 288 (3rd gen) | 568 (4th gen) | 432 (3rd gen) | 456 (4th gen)
NVIDIA CUDA Cores | 5120 | 5120 | 3072 | 2560 | 7424 | 9216 | 18176 | 6912 | 14592
GPU Memory (GB) | 16 | 32 | 16 | 16 | 24 | 24 | 48 | 80 | 80
Memory Bandwidth (GB/s) | 900 | 1134 | 448 | 300 | 300 | 600 | 864 | 1935 | 2048
Interconnect Type | PCIe Gen3 | PCIe Gen3 | PCIe Gen3 | PCIe Gen3 | PCIe Gen4 | PCIe Gen4 | PCIe Gen4 | PCIe Gen4 | PCIe Gen5
Encoders and Decoders | ? | ? | 1, 2 | ? | 2, 4, 4 | 1, 1 | 3, 3 | ? | ?, 7, 7
CUDA Compute Capability | 7 | 7 | 7.5 | 7.5 | 8.9 | 8.6 | 8.9 | 8 | 9
