import pathlib
import subprocess
import sys

dir = pathlib.Path(__file__).parent

output_dir = dir / "build"
if not output_dir.exists():
    output_dir.mkdir()
for file in output_dir.glob("*.json"):
    file.unlink()

for notebook in dir.glob("*.ipynb"):
    print(f"Building {notebook.name}...")
    output = notebook.with_suffix(".py")
    if output.exists():
        output.unlink()
    cmd = [
        "python", "-m", "jupyter", "nbconvert", "-y",
        "--to", "python", str(notebook),
        "--output", output.stem
    ]
    print(" ".join(cmd))
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        sys.stderr.write(result.stderr)
        raise RuntimeError(f"Failed to convert {notebook} to script.")
    print(f"Successfully built {output.name}.")
    # Execute the generated script
    print(f"Executing {output.name}...")
    cmd = ["python", str(output)]
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        sys.stderr.write(result.stderr)
        sys.stdout.write(result.stdout)
        raise RuntimeError(f"Failed to execute {output}.")
    output.unlink()