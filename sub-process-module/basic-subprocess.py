import subprocess

result = subprocess.run(
    ["dir"],
    capture_output=True,
    text=True,
    shell=True   # IMPORTANT on Windows
)

print(result.stdout)
