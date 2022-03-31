BEGIN TRANSACTION;
CREATE TABLE audit(
    id integer primary key autoincrement,
    createdon datetime default current_timestamp,
    user varchar(20),
    cpu decimal,
    memory decimal,
    storage decimal
);
INSERT INTO "audit" VALUES(1,'2022-03-27 11:53:30','alexis',19,63,0);
INSERT INTO "audit" VALUES(2,'2022-03-27 11:53:30','root',0,2,0);
INSERT INTO "audit" VALUES(3,'2022-03-27 11:53:30','whoopsie',0,0,0);
INSERT INTO "audit" VALUES(4,'2022-03-27 11:53:30','uuidd',0,0,0);
INSERT INTO "audit" VALUES(5,'2022-03-27 11:53:30','systemd+',0,0,0);
INSERT INTO "audit" VALUES(6,'2022-03-27 11:53:31','syslog',0,0,0);
INSERT INTO "audit" VALUES(7,'2022-03-27 11:53:31','rtkit',0,0,0);
INSERT INTO "audit" VALUES(8,'2022-03-27 11:53:31','message+',0,0,0);
INSERT INTO "audit" VALUES(9,'2022-03-27 11:53:31','kernoops',0,0,0);
INSERT INTO "audit" VALUES(10,'2022-03-27 11:53:31','colord',0,0,0);
INSERT INTO "audit" VALUES(11,'2022-03-27 16:47:08','alexis',19,63,0);
INSERT INTO "audit" VALUES(12,'2022-03-27 16:47:08','root',0,2,0);
INSERT INTO "audit" VALUES(13,'2022-03-27 16:47:08','whoopsie',0,0,0);
INSERT INTO "audit" VALUES(14,'2022-03-27 16:47:08','uuidd',0,0,0);
INSERT INTO "audit" VALUES(15,'2022-03-27 16:47:08','systemd+',0,0,0);
INSERT INTO "audit" VALUES(16,'2022-03-27 16:47:08','syslog',0,0,0);
INSERT INTO "audit" VALUES(17,'2022-03-27 16:47:08','rtkit',0,0,0);
INSERT INTO "audit" VALUES(18,'2022-03-27 16:47:08','message+',0,0,0);
INSERT INTO "audit" VALUES(19,'2022-03-27 16:47:08','kernoops',0,0,0);
INSERT INTO "audit" VALUES(20,'2022-03-27 16:47:08','colord',0,0,0);
INSERT INTO "audit" VALUES(21,'2022-03-30 17:49:42','alexis',19,63,0);
INSERT INTO "audit" VALUES(22,'2022-03-30 17:49:42','root',0,2,0);
INSERT INTO "audit" VALUES(23,'2022-03-30 17:49:42','whoopsie',0,0,0);
INSERT INTO "audit" VALUES(24,'2022-03-30 17:49:42','uuidd',0,0,0);
INSERT INTO "audit" VALUES(25,'2022-03-30 17:49:42','systemd+',0,0,0);
INSERT INTO "audit" VALUES(26,'2022-03-30 17:49:42','syslog',0,0,0);
INSERT INTO "audit" VALUES(27,'2022-03-30 17:49:42','rtkit',0,0,0);
INSERT INTO "audit" VALUES(28,'2022-03-30 17:49:42','message+',0,0,0);
INSERT INTO "audit" VALUES(29,'2022-03-30 17:49:42','kernoops',0,0,0);
INSERT INTO "audit" VALUES(30,'2022-03-30 17:49:42','colord',0,0,0);
INSERT INTO "audit" VALUES(31,'2022-03-30 17:52:50','alexis',22,67,0);
INSERT INTO "audit" VALUES(32,'2022-03-30 17:52:50','whoopsie',0,0,0);
INSERT INTO "audit" VALUES(33,'2022-03-30 17:52:50','uuidd',0,0,0);
INSERT INTO "audit" VALUES(34,'2022-03-30 17:52:50','systemd+',0,0,0);
INSERT INTO "audit" VALUES(35,'2022-03-30 17:52:50','syslog',0,0,0);
INSERT INTO "audit" VALUES(36,'2022-03-30 17:52:50','rtkit',0,0,0);
INSERT INTO "audit" VALUES(37,'2022-03-30 17:52:51','root',0,0,0);
INSERT INTO "audit" VALUES(38,'2022-03-30 17:52:51','message+',0,0,0);
INSERT INTO "audit" VALUES(39,'2022-03-30 17:52:51','kernoops',0,0,0);
INSERT INTO "audit" VALUES(40,'2022-03-30 17:52:51','colord',0,0,0);
CREATE TABLE settings(
    id integer primary key autoincrement,
    createdon datetime default current_timestamp,
    threshold_cpu integer default 5,
    threshold_memory integer default 5 ,
    threshold_storage integer default 5,
    max_backups integer default 10
);
INSERT INTO "settings" VALUES(1,'2022-03-27 12:17:37',5,5,5,10);
DELETE FROM "sqlite_sequence";
INSERT INTO "sqlite_sequence" VALUES('audit',40);
INSERT INTO "sqlite_sequence" VALUES('settings',1);
COMMIT;
