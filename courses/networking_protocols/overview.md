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

# application layer
the application layer protocols are implemented within the application software

## protocol general proparties of the protocols
- data delivery reliability
  - lossless
  - lossy
- transfer time reliability
  - consistent delay
  - varying delay
- security
- privacy

## client-server architecture
- server:
  - the server process is reachable using the following network layer protocols:
    - TCP via ip-address and port number
    - UDP
  - always-on (waiting for incoming requests from clients)
- client:
  - initiate the connection to the server
  
### HTTP API protocol
HTTP is stateless (the server does not retain previous requests from the client)

#### universal resource locator (URL):
`http://www.someschool.edu:port#/someDept/pic.gif?key,foo#bar`
- protocol: `http`
- hosting: `www.someschool.edu:port#`
- path name: `someDept/pic.gif`
- query: `?foo`
  - the de facto format is delimited key-value pairs
- fragment: `#bar`
  - denotes a sub-component of the received resource
- when a server socket listens for connection requests and accepts a connection, it creates a new socket that is connected to the socket which sent the connection request (the main server socket continues to listen for more connection requests).

#### HTTP 1.0: non-persistent
- every HTTP/1.0 request must first send a request to stablish a TCP connection before sending the HTTP request, thus the response time is $2*RTT+\text{transfer time}$

#### HTTP 1.1: persistent connection
- without pipelining - each request is processed individually
- with pipelining - requests are responded to using multiplexing (this decreases the total response delay)
- processes requests sequentially, which can lead to head-of-line-blocking of important requests
- sequential requests can have redundant headers 

#### HTTP 2.0: binary framing
- the client and the server keep a header table until the TCP connection closes
- messages are sent in binary encoding
- layers:
  - the connection is defined by a set of streams.
    - requests and responses are defined by a message
      - the request line, header lines are defined by the HEADERS frame and the response payload is defined by the DATA frame. dig messages are broken down into smaller frames. frames can be interleaved. 
- note: this version still suffers from head-of-line blocking and congestion control from TCP; it requires a separate security layer (TLS). each connection must negotiate security parameters.

#### HTTP 3.0: QUIC and UDP
- uses UDP for it networking layer.
- reuses security parameters from previous connections
- app-managed congestion control
- uses `streams` for multiplexing without head-of-line blocking
- forward error connection
- connection migration
- compresses headers
- servers can predict a client's request and "push" a response without receiving a request
- requests have prioritization levels
- uses connection identifiers

#### HTTPS: secure HTTP
certificate authority (CA) checks the right of the applicant to use a specific domain name and conducts a vetting of the organization
states of TLS certificates:
- valid
- expired
- wrong host
- untrusted root
- revoked
- pinned
- etc.

#### HTTP requests
- GET
  - requests information from the server
- POST
  - sends data, located in the message body, to the server
- HEAD
  - requests metadata of a resource from the server
- PUT
  - uploads a file, specified by a path in the message body, to the path specified in the URL of the request line.
- DELETE
  - deletes a file specified in the URL of the request line from the server
- and others (from the protocol RFC2616)

request example:
- GET /index.html HTTP/1.1\r\n
- Host: www-net.cs.umass.edu\r\n
- User-Agent: Firefox/3.6.10\r\n
- Accept: text/html, application/xhtml+xml\r\n
- Accept-Language: en-us, en;q=0.5\r\n
- Accept-Encoding: gzip, deflate\r\n
- Accept-Charset: ISO-8859-1, utf-8;q=0.7\r\n
- Keep-Alive: 115\r\n
- Connection: keep-alive\r\n
- \r\n
- <request body (optional)>

note: all lines of the request message end with the return character. the first line is the request line. it contains the request method, the URL, and the protocol version, in that sequential order. the subsequent lines are header lines in the format `atribute`:[`value`]. the body of the request ends with a line that only contains the return character.

note: the url of the request line could include the full url and remove the host header and the protocol would still work, but that is not how HTTP is specified.

#### HTTP responses
response example:
- HTTP/1.1 200 OK/r/n
- Date: Sun, 27 Sep 2010 20:09:20 GMT/r/n
- Server: Apach/2.0.52 (CentOS) \r\n
- Last-Modified: Tue, 30 Oct 2007 17:00:02 GMT\r\n
- ETag: "17dc6-a5c-bf716880"\r\n
- Accept-Ranges: bytes\r\n
- Content-Length: 2652\r\n
- Keep-Alive: timeout=10, ma= 100\r\n
- Connection: Keep-Alive\r\n
- Content-Type: text/html; charset=ISO-8859-1\r\n
- \r\n
- <response body (optional)>


##### HTTP response status codes

- 200 OK
  - request succeeded, requested object later in this message
- 301 Moved Permanently
  - requested object moved, new location specified later in this message (Location:)
- 400 Bad Request
  - request message not understood by server
- 404 Not Found
  - requested document not found on this server
- HTTP Version Not Supported
  - Something is wrong with the server (authorization error, etc.)

##### HTTP cookie headers
- Set-cookie:
  - fields:
    - \<key-value pairs\>
    - \<domain path\>
    - \<Expires, Max-Age\>
    - \<Secure, HttpOnly\>
- cookies: <ID>

servers can preserve state of HTTP messages from clients with the cookie header ID defined and tracked by the server. the server sends an ID for the client to store. the client cannot create cookies for subdomains (e.g. bar.www.foobar.com). some public domains (like .com) are also restricted. the client sends requests with this header so the server can identify the client if the request path includes (/docs). the client can keep some data linked to the client ID, which could be used to generate unique responses.

advertising companies (e.g. ad.foxy-tracking.com) get HTTP messages when a client visits websites. the advertising company can build a profile of the user.

#### HTTP proxy cache servers
a proxy server acts as an intermediate client and server node in the requests sent to the server and the responses sent to the client

### SMTP API protocol
the protocol has three phases of transfer (handshaking to check capabilities, start TLS session, transfer of messages, close SMTP). 

the messages specification is very similar to HTTP. every phase has a command (ASCII text) and a response (status code and phrase). uses `(\r\n.\r\n)` to determine end of message.

use an empty line to separate the header and body of a message.

the messages must be encoded in 7-bit ASCII.

#### message format
- header lines
  - To:
  - From:
  - Subject:
  - Other headers
- empty line to separate header and body
- body

#### user agents
compose, edit, read mail messages.

#### mail servers
contains incoming messages for user agents and has a message queue of outgoing mail messages

#### mail access protocols
- SMTP

add more features to how the data as retrieved:
- IMAP
- Exchange
- etc.

#### reply status codes
- 1st digit: whether response is good/bad/incomplete
  - 2 - positive completion
  - 5 - negative completion
- 2nd digit: encodes responses in categories
  - 2 - connections
  - 5 - mail server system
- 3rd digit: a finer gradation of meaning in each category specified by the second digit

common code meanings
- 220 - service ready
- 221 - I'm closing too
- 250 - requested action OK
- 500 error, command not recognized
- 550 no such mbox, no action taken

#### multipurpose internet mail extensions (MIME)
- adds header information or text in non-ASCII character set
- adds message bodies with multiple parts
- adds support for non-text attachments
  
additional MINE header lines (with examples):
- MINE-Version: 1.0
- Content-Transfer-Encoding: base64
- Content-Type: image/jpeg

the body can be encoded data.

### BSD sockets API protocol

## peer-to-peer architecture
- peers are both servers and clients
- the peer servers are not always on
- the list of servers in the network can change
- peers request messages from other peers
  - peers exchange ip-address tables via complex protocols

## hybrid architecture
- some communication happens over server-client connections
- some communication happens over peer-to-peer connections

## publish-subscriber architecture
- potentially built using client-server architectures
  - the server is the publish-subscriber central server 
  - the clients are the publishers and subscribers
- publishers publish messages to a topic on the publish-subscriber server
- subscribers subscribe to the set of desired topics
  - subscribers are sent messages published to their subscribed topics

## multicast architecture
- publish-subscriber architecture implemented at the networking layer
- subscribers subscribe to all the packets sent to the publishing address (all the provider messages sent to the subscribed address)
- AJAX
- SMTP
- DNS
- CDNs

## TCP/IP addressing
each device component can have its own IP address

IPv4 specification:
- network address: [0-9]{1,4}[.][0-9]{1,4}[.][0-9]{1,4}[.][0-9]{1,4}
- device port: [0-65536]
  - note: ports after 1024 usage require super user authorization