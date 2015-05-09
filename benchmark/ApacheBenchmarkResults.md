#First Test 1 Request with 1 concurrent
```sh
ab -n 1 -c 1 localhost:5000/fallout
```

######Over here We can clearly see that this is the baseline first experiment to be done in order to understand if your code is working right. Everything else will be tested against this so then i can observe how -n and -c react to this one.


>This is ApacheBench, Version 2.3 <$Revision: 1554214 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient).....done

* [AngularJS] - HTML enhanced for web apps!
- Server Software:       Werkzeug/0.9.6
- Server Hostname:        localhost
- Server Port:            5000

* Document Path:          /fallout
* Document Length:        267 bytes

* Concurrency Level:      1
- Time taken for tests:   0.004 seconds
- Complete requests:      1
- Failed requests:        0
- Non-2xx responses:      1
- Total transferred:      478 bytes
- HTML transferred:       267 bytes
- Requests per second:    238.95 [#/sec] (mean)
- Time per request:       4.185 [ms] (mean)
- Time per request:       4.185 [ms] (mean, across all concurrent requests)
- Transfer rate:          111.54 [Kbytes/sec] received

###Connection Times (ms)
min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       0
Processing:     4    4   0.0      4       4
Waiting:        4    4   0.0      4       4
Total:          4    4   0.0      4       4

#Second Test 200 Requests 1 Concurrent
```sh
ab -n 200 -c 1 localhost:5000/fallout
```

######This test is clearly fitted for testing concurrent requests. Although I have 100requests, its processing these requests 15 at a time. This is important into understanding how my computer will handle heavy loads. As you can see, there is clearly a big difference in processing time when compared to the last two results. Thankfully my CPU can handle this load quite well. 

>This is ApacheBench, Version 2.3 <$Revision: 1554214 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient)


- Server Software:        Werkzeug/0.9.6
- Server Hostname:        localhost
- Server Port:            5000

- Document Path:          /fallout
- Document Length:        267 bytes

- Concurrency Level:      1
- Time taken for tests:   0.543 seconds
- Complete requests:      200
- Failed requests:        0
- Non-2xx responses:      200
- Total transferred:      95600 bytes
- HTML transferred:       53400 bytes
- Requests per second:    368.11 [#/sec] (mean)
- Time per request:       2.717 [ms] (mean)
- Time per request:       2.717 [ms] (mean, across all concurrent requests)
- Transfer rate:          171.83 [Kbytes/sec] received

Connection Times (ms)
min  mean[+/-sd] median   max
Connect:        0    0   0.1      0       1
Processing:     2    3   1.1      2      16
Waiting:        0    2   0.8      2       6
Total:          2    3   1.1      2      16

###Percentage of the requests served within a certain time (ms)
- 50%      2
- 66%      3
- 75%      3
- 80%      3
- 90%      3
- 95%      4
- 98%      5
- 99%      7
- 100% 16 (longest request)

#Thirst Test 100 Requests 1 Concurrent


```sh
ab -n 100 -c 15 localhost:5000/fallout
```
######This is a follow up to the previous test. Just an easier load to compare time and understand. 
>This is ApacheBench, Version 2.3 <$Revision: 1554214 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/


Benchmarking localhost (be patient).....done


- Server Software:        Werkzeug/0.9.6
- Server Hostname:        localhost
- Server Port:            5000

- Document Path:          /fallout
- Document Length:        267 bytes

- Concurrency Level:      15
- Time taken for tests:   0.232 seconds
- Complete requests:      100
- Failed requests:        0
- Non-2xx responses:      100
- Total transferred:      47800 bytes
- HTML transferred:       26700 bytes
- Requests per second:    430.84 [#/sec] (mean)
- Time per request:       34.816 [ms] (mean)
- Time per request:       2.321 [ms] (mean, across all concurrent requests)
- Transfer rate:          201.11 [Kbytes/sec] received

Connection Times (ms)
min  mean[+/-sd] median   max
- Connect:        0    0   0.2      0       1
- Processing:    11   32   4.7     33      43
- Waiting:       10   32   4.8     32      42
- Total:         11   33   4.6     33      43

Percentage of the requests served within a certain time (ms)
- 50%     33
- 66%     34
- 75%     35
- 80%     35
- 90%     36
- 95%     37
- 98%     41
- 99%     43
- 100%     43 (longest request)

######This is my last test where I really put my computer to the test. It took quite a while for this to process comapred to the others. Overall im glad with how the computer 

>This is ApacheBench, Version 2.3 <$Revision: 1554214 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient)
> - Completed 1000 requests
> - Completed 2000 requests
> - Completed 3000 requests
> - Completed 4000 requests
> - Completed 5000 requests
> - Completed 6000 requests
> - Completed 7000 requests
> - Completed 8000 requests
> - Completed 9000 requests
> - Completed 10000 requests
> - Finished 10000 requests


- Server Software:        Werkzeug/0.9.6
- Server Hostname:        localhost
- Server Port:            5000

Document Path:          /fallout
Document Length:        267 bytes

- Concurrency Level:      100
- Time taken for tests:   24.042 seconds
Complete requests:      10000
- Failed requests:        0
- Non-2xx responses:      10000
- Total transferred:      4780000 bytes
- HTML transferred:       2670000 bytes
- Requests per second:    415.94 [#/sec] (mean)
- Time per request:       240.419 [ms] (mean)
- Time per request:       2.404 [ms] (mean, across all concurrent requests)
- Transfer rate:          194.16 [Kbytes/sec] received

Connection Times (ms)
min  mean[+/-sd] median   max
- Connect:        0    0   0.4      0       5
- Processing:     4  239  47.8    229     586
- Waiting:        4  239  47.8    229     586
- Total:          8  239  47.7    229     586

Percentage of the requests served within a certain time (ms)
- 50%    229
- 66%    232
- 75%    236
- 80%    239
- 90%    254
- 95%    331
- 98%    415
- 99%    485
- 100%    586 (longest request)