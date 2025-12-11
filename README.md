# Rainbow Table Hash Cracker

## Overview

The Rainbow Table Hash Cracker is a command-line tool designed to crack hashed passwords using precomputed rainbow tables. This tool leverages the efficiency of rainbow tables to quickly find the original password corresponding to a given hash.

## Features

- Supports cracking of hexadecimal formatted hashes
- Loads rainbow tables generated from `rainbowgen.py`
- Displays detailed information about the loaded rainbow table
- Provides human-readable execution time for operations
- Handles errors gracefully with informative messages
- Supports multiple hash algorithms: SHA1, MD5, and SHA256
- Includes a powerful table generation system with configurable parameters
- Utilizes GomuhryTree optimization for efficient lookup operations
- Comprehensive logging and progress tracking

## Supported Algorithms

- **SHA1** - 160-bit secure hash algorithm
- **MD5** - 128-bit cryptographic hash function
- **SHA256** - 256-bit secure hash algorithm

## Requirements

- Python 3.x
- Required libraries:
  - `argparse`
  - `os`
  - `sys`
  - `time`
  - `datetime`
  - `hashlib`
  - `configparser`
  - `logging`
  - `pickle`
  - `random`
  - `rainbowtable` (custom module)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/rainbow-table-hash-cracker.git
   cd rainbow-table-hash-cracker
   ```

2. Ensure you have the required libraries installed. You may need to install the rainbowtable module if it's not included in your environment.

3. Create the required directories:
   ```bash
   mkdir -p config logs
   ```

## Configuration

The tool uses `config/config.ini` to define character sets for password generation. Available character sets include:

- `lower_alphanumeric` - lowercase letters and numbers
- `alphanumeric` - uppercase, lowercase letters and numbers
- `ascii` - full ASCII printable character set
- `numeric` - numbers only

## Usage

### Generating Rainbow Tables

To generate a rainbow table, use the `rainbowgen.py` script:

```bash
python3 rainbowgen.py <algorithm> <charset> <min_length> <max_length> <chain_length> <number_of_chains> <output_file>
```

**Example - SHA256 Table:**

```bash
python3 rainbowgen.py sha256 alphanumeric 4 6 1000 5000 my_sha256_table.rt
```

**Example - MD5 Table:**

```bash
python3 rainbowgen.py md5 lower_alphanumeric 3 5 800 3000 my_md5_table.rt
```

**Example - SHA1 Table:**

```bash
python3 rainbowgen.py sha1 numeric 4 4 500 2000 my_sha1_table.rt
```

### Cracking Hashes

To crack a hash using a precomputed rainbow table:

```bash
python3 rainbowcrack.py <hash_value> <rainbow_file>
```

**Example - Cracking SHA256 Hash:**

```bash
python3 rainbowcrack.py 5d41402abc4b2a76b9719d911017c592 my_sha256_table.rt
```

**Example - Cracking MD5 Hash:**

```bash
python3 rainbowcrack.py c44b066a89bb2ba78d6b8e5e81194d596 my_md5_table.rt
```

**Example - Cracking SHA1 Hash:**

```bash
python3 rainbowcrack.py e4815b09a6fdc84943f727b1611bd704899864ca my_sha1_table.rt
```

### Migrating Table Files

To rebuild internal structures in older table files:

```bash
python3 scripts/migrate_table.py <input_file> [-o <output_file>]
```

## Parameter Details

- **algorithm**: Hash algorithm (sha1, md5, sha256)
- **charset**: Character set name from config.ini
- **min_length**: Minimum password length
- **max_length**: Maximum password length
- **chain_length**: Length of each chain in the rainbow table
- **number_of_chains**: Number of chains to generate
- **output_file**: Output filename for the generated table

## Examples

### Complete Workflow

1. Generate a SHA256 rainbow table:

   ```bash
   python3 rainbowgen.py sha256 alphanumeric 3 5 1000 1000 test_table.rt
   ```

2. Hash a test password:

   ```bash
   # Using Python to hash "abc123" with SHA256
   python3 -c "import hashlib; print(hashlib.sha256(b'abc123').hexdigest())"
   # Output: 240be518fabd2724ddb6f04eeb1da5967448d7e831c08c8fa822809f74c720a9
   ```

3. Crack the hash:
   ```bash
   python3 rainbowcrack.py 240be518fabd2724ddb6f04eeb1da5967448d7e831c08c8fa822809f74c720a9 test_table.rt
   ```

## Performance Considerations

- Larger chain lengths increase lookup time but reduce storage requirements
- More chains increase storage but improve success rate
- Memory usage scales with the number of chains
- Algorithm choice affects both generation time and storage size

## Troubleshooting

- Ensure rainbow table file exists and is readable
- Verify hash format is hexadecimal
- Check that the hash algorithm matches the table's algorithm
- For large tables, ensure sufficient disk space is available
