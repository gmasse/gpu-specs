# Contributing to GPU Specifications for AI Projects

Thank you for your interest in contributing to this project! Your contributions will help create a comprehensive and reliable database for GPU specifications in AI contexts.

## How You Can Contribute

1. **Fix Errors**  
   - Spot an error in the data? Submit a correction.
   
2. **Add Missing Data**  
   - If you know of missing specifications, feel free to update the JSON file.

3. **Document Sources**  
   - Every piece of information should be backed by a reliable source. If you’re adding or correcting data, please include references in the source field.

4. **Improve Documentation**  
   - Help make the README, guidelines, or HTML/Markdown outputs more user-friendly.

5. **Expand Compatibility**  
   - Add specifications for GPUs not yet covered in the database.

## Data Conventions

To maintain consistency across the project, adhere to these conventions when editing or adding data to the JSON:

- **Unsupported Precision:**
  Use a value of `0` to indicate that a specific precision (e.g., FP8) is **not natively supported** by the GPU.

- **Missing Data:**
  Use a value of `null` for fields where the information is currently unavailable or not yet confirmed.

- **Sources:**
  Each GPU entry must include a `sources` field as an array of URLs pointing to reliable references.

## How to Contribute

### 1. Fork the Repository

Start by forking the repository to your own GitHub account.

### 2. Clone the Repository

Clone your fork to your local machine:
```bash
git clone https://github.com/gmasse/gpu-specs.git
```

### 3. Create a Branch

Create a feature branch for your changes:
```bash
git checkout -b feature/your-feature-name
```

### 4. Make Your Changes

Edit the JSON file in the `data/` directory.
Run the scripts in `scripts/` to regenerate the HTML or Markdown (if applicable).

### 5. Submit a Pull Request

Push your changes to your fork:
```bash
git push origin feature/your-feature-name
```
Open a pull request from your branch to the main repository.