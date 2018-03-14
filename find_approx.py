import approximable
import sys

#Initialize
approx = approximable.Approximable()

# Change paths accordingly in config.txt before running
#config_path = 'config.txt'
config_path = '/home/himeshi/Projects/workspace/SORScimark/config.txt'

with open(config_path, 'r') as infile:
    result_path = infile.readline().split()[2].strip()
    source_path = infile.readline().split()[2].strip()
    ktest_tool_path = infile.readline().split()[2].strip()
    input_path = infile.readline().split()[2].strip()

if(len(sys.argv) < 2):
    print("Usage: python find_approx.py [--single-path-approximation|--all-path-approximation|--approximate-path-by-probability=<N>|--approximate-path-by-pathcount=<N>]")
elif(sys.argv[1] == "--single-path-approximation"):
    approx.approximate_for_single_path(result_path, source_path, input_path, ktest_tool_path)
elif (sys.argv[1] == "--all-path-approximation"):
    approx.approximate_for_all_paths(result_path, source_path, ktest_tool_path)
elif (sys.argv[1] == "--all-path-approximation-summary"):
    approx.approximate_for_all_paths_summary(result_path, source_path, ktest_tool_path)
elif ("--approximate-path-by-probability" in sys.argv[1]):
    approx.approximate_path_by_probability(sys.argv[1], result_path, source_path, ktest_tool_path)
elif ("--approximate-path-by-pathcount" in sys.argv[1]):
    approx.approximate_path_by_pathcount(sys.argv[1], result_path, source_path, ktest_tool_path)
else:
    print("Usage: python find_approx.py [--single-path-approximation|--all-path-approximation|--approximate-path-by-probability=<N>|--approximate-path-by-pathcount=<N>]")
