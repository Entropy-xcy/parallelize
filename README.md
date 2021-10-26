# Parallelize

## Usage
Very simple:
```bash
python parallelize.py target.sh > Makefile

make -j$(nproc)
```
