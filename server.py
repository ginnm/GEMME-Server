import pandas as pd
from typing import AnyStr, List
import tempfile
import os
from pathlib import Path
import shutil
import subprocess


def exec_command(command: str) -> List[AnyStr]:
    process = subprocess.Popen(
        command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE
    )
    stdout, stderr = process.communicate()
    return stdout.decode(), stderr.decode()


def search_a3m(fasta_file, output_dir=None):
    raise NotImplementedError("search_a3m is not implemented")


def handle(fasta_file, mutant_file, a3m_file=None):
    # 创建一个临时文件夹
    with tempfile.TemporaryDirectory() as temp_dir:
        source_file = fasta_file
        fasta = os.path.join(temp_dir, Path(source_file).name)
        # 将fasta文件复制到临时文件夹
        shutil.copy(source_file, fasta)

        # a3m
        if a3m_file is None:
            a3m = search_a3m(fasta)
        else:
            source_file = a3m_file
            a3m = os.path.join(temp_dir, Path(source_file).name)
        
        # 
    print("临时文件夹已删除")


if __name__ == "__main__":
    handle("exmples/GFP.fasta", "test.mutant", "exmples/GFP.a3m")


# Load the a3m

# Load the mutant_file

# Convert the muant_file to a temporary txt file

# Convert the a3m file to a fasta file

# Score the fasta file

# Extract Score
