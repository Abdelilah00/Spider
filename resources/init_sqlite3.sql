create table if not exists audit(
    id integer primary key autoincrement,
    createdon datetime default current_timestamp,
    user varchar(20),
    cpu decimal,
    memory decimal,
    storage decimal
);
create table if not exists settings(
    id integer primary key autoincrement,
    createdon datetime default current_timestamp,
    threshold_cpu integer default 5,
    threshold_memory integer default 5 ,
    threshold_storage integer default 5,
    max_backups integer default 10
);
drop table settings;

insert into settings(threshold_cpu) values(5);


select * from audit a,settings s where a.cpu>s.threshold_cpu or a.memory>s.threshold_memory or a.storage>s.threshold_storage;

commit;
rollback;

select user,cpu,memory,storage from audit;
select threshold_storage,threshold_memory,threshold_cpu,max_backups  from settings;