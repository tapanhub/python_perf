# python_perf
DONOT Always have measurable  perf goals before optimizing code
Dont .. Yet: Developer time is expensive - sometimes the best solution is to upgrade hardware
Profile before optimizing: profiling measures where code spend time

General tips for profiling:

- Use real data
- Turn off antivirus/similar programs
- test suite ready, as optimization can add bug
- know when to measure, many program may have warmup time like db access


Measuring Time
- time module
- timeit module


may get -ve time if ntp is enabled
measument of elapsed time include the time processes spend sleeping
In python ppl usually use time function, Python 3 includes the monolithic and perf_counter func for
high-resolution monolithic timer.

Ipython timeit:
ipython
In [1]: %run -n using_timeit.py # -n is to just load , dont run __main__
In [2]: %timeit use_catch('a')
In [2]: %timeit use_get('a')

CPU Profiling:
-------------
cProfile is recommended by Python
- Deterministic profilers record every function call, return , and exception
- statistical profilers record where the program is at small intervals
- pstat module displays profiler-generated statistics file

cProfile usage:
--------------
python -m cProfile using_time.py # profiling whole code
only a function:
import cProfile
cProfile.run('use_catch("x")')
cProfile.run('use_catch("x")', filename="prof.out")
python -m pstats prof.out
perf.out% stats 10
perf.out% sort cumtime
perf.out% stats 10
pip/conda install snakeviz
snakeviz prof.out

ipython cpuprofiling:
--------------------
%run -n prof.py
%prun bench_login(1000)
%prun?
%prun -s cumulative bench_login(cases)

Line profiler:
-------------
line_profiler can be used to measure with finer granurality than just function
line_profiler is not in the standard  library
includes a commandline program called "kernprof"
install: conda install line_profiler
use @profile decorators to select which parts of the code to profile
kernprof -l  using_time.py
python -m line_profiler using_time.py.lprof
ipython:
remove @profile decorator if any
%run -n using_time.py
%load_ext line_profiler
%lprun -f login bench_login(cases)

Tracing memory allocations:
--------------------------
In 3.0 tracemalloc is introduced
import tracemalloc
tracemalloc.start()
for event in events:
    encode_event(event, stream)
snapshot = tracemalloc.take_snapshot()
for stat in snapshot.statistics('lineno')[:10]
    print(stat)

memory_profiler (also works with python2)
---------------
 conda install memory_profiler
use @profile decorators to select which parts of the code to profile
 python -m memory_profiler sum_of_differences.py
mprof tool
---------
remove @profile
mprof run sum_of_differences.py
mprof plot mprofile_20200829011814.dat


