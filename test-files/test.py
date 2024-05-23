#!/usr/bin/env python
import os, sys
import subprocess
this_dir = os.path.dirname(__file__)

projects_dir = os.path.join(os.path.dirname(this_dir), "project", "assignments")
test_file    = os.path.join(this_dir,  "test.fa")
if not os.path.exists(projects_dir):
    print(f"Error: {projects_dir} not found")
    sys.exit(1)

passed, total = 0, 0
for py_file in os.listdir(projects_dir):
    if py_file.endswith(".py"):
        print(f"Processing {py_file}")
        total += 1
        py_file_path = os.path.join(projects_dir, py_file)
        command = ["python", py_file_path, test_file]
        output = subprocess.run(command, capture_output=True, text=True)
        ok = 0
        # Check if the command was successful
        if output.returncode != 0:
            print(f"\tError running {py_file_path}")
        else:
            ok += 1

        # Check if the output is as expected
        lines_count = len(output.stdout.strip().split("\n"))

        lines_starting_with_gt = [line for line in output.stdout.strip().split("\n") if line.startswith(">")]
        if len(lines_starting_with_gt) == 3:
            ok += 1

        non_empty_lines = [line for line in output.stdout.strip().split("\n") if len(line.strip()) > 0]
        if len(non_empty_lines) == 6:
            ok += 1

        match = "QIDTP"
        lines_matching = [line for line in output.stdout.strip().split("\n") if match in line]
        if len(lines_matching) == 1:
            ok += 1
        print("\t"ok, "/4 tests passed", sep="")
        passed += 1 if ok == 4 else 0


print(f"-----------------\n{passed}/{total} tests passed")
if passed == total:
    exit(0)
else:
    exit(1)