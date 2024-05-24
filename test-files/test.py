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
        for path in [test_file, test_file + ".gz"]:
            file = os.path.basename(path)
            command = ["python", py_file_path, path]
            output = subprocess.run(command, capture_output=True, text=True)
            ok = 0
            # Check if the command was successful
            if output.returncode != 0:
                print(f"\tERR {file}: Error running {py_file_path}")
            else:
                print(f"\tOK {file}: Command ran successfully")
                ok += 1
            

            # Check if the output is as expected
            lines_count = len(output.stdout.strip().split("\n"))

            lines_starting_with_gt = [line for line in output.stdout.strip().split("\n") if line.startswith(">")]
            if len(lines_starting_with_gt) == 3:
                ok += 1
                print(f"\tOK {file}: there are 3 lines starting with '>'")
            else:
                print(f"\tERR {file}: there are", len(lines_starting_with_gt), "lines starting with '>'")

            non_empty_lines = [line for line in output.stdout.strip().split("\n") if len(line.strip()) > 0]
            if len(non_empty_lines) == 6:
                ok += 1
                print(f"\tOK {file}: there are 6 non-empty lines")
            else:
                print(f"\tERR {file}: there are", len(non_empty_lines), "non-empty lines")

            match = "QIDTP"
            lines_matching = [line for line in output.stdout.strip().split("\n") if match in line]
            if len(lines_matching) == 1:
                ok += 1
                print(f"\tOK {file}: there is 1 line matching", match)
            else:
                print(f"\tERR {file}: there are", len(lines_matching), "lines matching", match)
        print("\t", ok, "/4 tests passed", sep="")

        #==== OPTIONAL TESTS ====
        passed += 1 if ok >= 4 else 0


print(f"-----------------\n{passed}/{total} tests passed")
if passed == total:
    exit(0)
else:
    exit(1)
