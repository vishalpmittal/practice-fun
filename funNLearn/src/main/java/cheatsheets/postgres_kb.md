======================================================================
Postgres DB
======================================================================
postgres (postgres)
scotzilla (ca$hc0w)

DB_DATE=`date '+%Y%m%d'`

/desk/PostgreSQL/9.6/bin/

cd /desk/osstp/stage/dbs
scp scotzilla@osstp-admin:mnt/backup/scotzilla/db/LATEST `date '+%Y%m%d'`_scotzilla.dmp


dropdb --host=localhost --username=postgres --port=5432 scotzilla --password=postgres

createuser --host=localhost --username=postgres --port=5432 --createdb --pwprompt scotzilla

role password (cashcow)


createdb  --host=localhost --username=postgres --port=5432 --owner=scotzilla scotzilla

cd /desk/osstp/stage/dbs
pg_restore -x --verbose --host=localhost --username=postgres --port=5432 --dbname=scotzilla 2018012_scotzilla.dmp >20180129_osstp_pg_restore_logs_1.txt 2>&1


pg_restore -x --verbose --host=localhost --username=postgres --port=5432 --dbname=scotzilla `date '+%Y%m%d'`_scotzilla.dmp > `date '+%Y%m%d'`_osstp_pg_restore_logs_1.txt 2>&1


Rename DB:
Disconnect all the clients and then

ALTER DATABASE "name of database" RENAME TO "new name of database";

