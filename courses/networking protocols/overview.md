# network sharing and delays
- packets cannot hop more than 255 nodes (this a protocol limit)

## sharing
**circuit sharing** - switches must be manually changed to alter the path of a connection

**packet sharing** - packets of data must be analized by the router to determine where to send the packet to:
- multiplexing - multiple inputs from multiple senders to the same router
- queuing - when the input throughput exceeds the output throughput, new packets are added to a queue to be sent
- packet drop - when the router queue is full new packets are dropped and not registered.


## delays

the four sources of delay in packet-switched networks:
  - **nodal  ($D_{nodal}$)** - cpu processing
    - delay contribution:
      - packet generation, copying, etc.
      - checking for bit errors
      - determining which link the packet should be sent to
    - not easy to estimate:
      - depends on the host type, available cpu and memory resources, how much other traffic is being processed.
  - **queuing ($D_{queue}$)**
    - describes the time the packet is witing in the queue to be transmitted
    - can be estimated:
      - number of packets in the queue, including the packet (N)
      - transmission time of a packet ($D_{trans}$ transmission delay)
      - $D_{queue} = (N -1) \times D_{trans}$
        - $D_{queue} = \sum_{n=1}^{N-1} D_{trans}^{n}$ when packet sizes significantly differ
  - **transmission ($D_{trans}$)**
    - time the bits of the packet being transmitted to the link 
      - sending packets is not instantanaous (packet bits need to be properly modulated and transmitted one-by-one or in groups (depending on link layer))
    - the entire packet must be received before it can be transmitted
    - can be estimated using:
      - packet size in bits ($L$ bits)
      - link bandwidth ($B$ bits per second)
      - $D_{trans} = L/B$
  - **propagation ($D_{prop}$)** 
    - time the packets take to reach the next destination after being transmitted 
    - can be estimated using:
      - length of physical link ($d$ in $meters$)
      - propagation speed in the medium ($velocity$ in $meters/second$):
        - in copper and fiber $\sim 2 \times 10^8 \ m/s$
        - in wireless $\sim 3 \times 10^8 \ m/s$
    - $D_{prop} = \frac{d}{v}$

time to send a single packet from source IP address to destination address:
- sum of delays across each hop along the path
- one way:
  - $Delay_{A \text{ to } B} = Delay_{A \text{ to } 1} + Delay_{1 \text{ to } 2} + Delay_{3 \text{ to } B}$
- RTT (round trip time):
  - $RTT_{A \text{ to } B} = Delay_{A \text{ to } B} + Delay_{B \text{ to } A}$

packets are extensively delayed when they don't make it to their destination on the first traversal

reasons for packet loss:
- errors in the transmission links (this is rare)
- packet reached a router with a full queue
- wireless links:
  - limited transmission rate
  - higher bit error rate
  - high variance in the number of hosts being served

## packet delivery performance
- throughput (bits/sec)
  - over a single link:
    - point to point
      - router output to router input
    - multi-access
  - throughput between two end hosts
- loss rate (% of packets loss)
- delay (seconds for the packet to transmit)