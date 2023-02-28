drop database if exists dns_database;
create schema dns_database;

drop table if exists dns_database.resource_record;
create table dns_database.resource_record (
    NAME bit(64) not null , # entity name
    TYPE bit(16) not null , # type of record in bit form (A, AAAA, NS, SOA, MX, etc.)
    CLASS bit(16) not null , # type of network (IN, CH, HS, etc.)
    TTL bit(32) not null , # counts up the expiration of the record entry
    RDLENGTH bit(16) , # length of `RDATA` field
    RDATA bit , # additional data to be stored (IPv4/IPv6/mail_server_full_path)

    primary key (NAME)

    # TODO: autoincrement `TTL` and delete the record when it reaches 2^16 - 1
    # TODO: set `RDLENGTH` to the length of `RDATA`
);
