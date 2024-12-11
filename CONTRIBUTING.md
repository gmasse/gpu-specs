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

Run the scripts in `scripts/` to serve HTML or generate Markdown (if applicable).

#### Licensing for new files
 
This project is licensed under Apache License, Version 2.0. Anything
contributed to this project must be released under this license.
 
When introducing a new file into the project, please make sure it has a
copyright header making clear under which license it's being released.

### 5. Submitting Modifications

The contributions should follow the DCO which is defined below.

Push your changes to your fork:
```bash
git push origin feature/your-feature-name
```
Open a pull request from your branch to the main repository.
 
## Developer Certificate of Origin (DCO)
 
To improve tracking of contributions to this project we will use a
process modeled on the modified DCO 1.1 and use a "sign-off" procedure
on patches that are being emailed around or contributed in any other
way.
 
The sign-off is a simple line at the end of the explanation for the
patch, which certifies that you wrote it or otherwise have the right
to pass it on as an open-source patch.  The rules are pretty simple:
if you can certify the below:
 
By making a contribution to this project, I certify that:
 
(a) The contribution was created in whole or in part by me and I have
    the right to submit it under the open source license indicated in
    the file; or
 
(b) The contribution is based upon previous work that, to the best of
    my knowledge, is covered under an appropriate open source License
    and I have the right under that license to submit that work with
    modifications, whether created in whole or in part by me, under
    the same open source license (unless I am permitted to submit
    under a different license), as indicated in the file; or
 
(c) The contribution was provided directly to me by some other person
    who certified (a), (b) or (c) and I have not modified it.
 
(d) The contribution is made free of any other party's intellectual
    property claims or rights.
 
(e) I understand and agree that this project and the contribution are
    public and that a record of the contribution (including all
    personal information I submit with it, including my sign-off) is
    maintained indefinitely and may be redistributed consistent with
    this project or the open source license(s) involved.
 
 
then you just add a line saying
 
    Signed-off-by: Random J Developer <random@example.org>
 
using your real name (sorry, no pseudonyms or anonymous contributions.)