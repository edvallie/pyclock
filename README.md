A simple timeclock display written for use on a Raspberry Pi via framebuffer

Reads an ID card through keyboard wedge interface (most barcode and magstripe readers)

![screen shot](https://github.com/edvallie/pyclock/raw/master/screenshot.png)

Written in python
Uses pygame module for graphics, psycopg for database routines

Collaborators: edvallie, chris0x00, s6moberg

Should work out of the box on Raspbian after installing psycopg:

apt-get install python-psycopg2

Needs a postgres backend either on the Pi or remote server.

Database scheme as follows:
```
timeclock=# \d+ employees
                    Table "public.employees"
   Column    |          Type          | Modifiers | Description
-------------+------------------------+-----------+-------------
 id          | integer                | not null  |
 employee_id | character varying(12)  |           |
 full_name   | character varying(200) |           |
Indexes:
    "employees_pkey" PRIMARY KEY, btree (id)
Has OIDs: no


timeclock=# \d+ timestamps
                                              Table "public.timestamps"
    Column     |            Type             |                        Modifiers                        | Description
---------------+-----------------------------+---------------------------------------------------------+-------------
 id            | integer                     | not null default nextval('timestamps_id_seq'::regclass) |
 employee_id   | character varying(12)       |                                                         |
 timestamp     | timestamp without time zone |                                                         |
 user_modified | character varying(30)       |                                                         |
Indexes:
    "timestamps_pkey" PRIMARY KEY, btree (id)
    "timestamp_record" UNIQUE, btree ("timestamp", employee_id)
Has OIDs: no
```
