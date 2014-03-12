create table users (
  id varchar(10) not null unique,
  G  boolean not null default 1,
  F  boolean not null default 0,
  T  boolean not null default 0,
  H  boolean not null default 0
);
insert into users values ('G',1,0,0,0);
insert into users values ('GF',1,1,0,0);
insert into users values ('GT',1,0,1,0);
insert into users values ('GH',1,0,0,1);
insert into users values ('GFT',1,1,1,0);
insert into users values ('GFH',1,1,0,1);
insert into users values ('GTH',1,0,1,1);
insert into users values ('GFTH',1,1,1,1);

alter table actors add column G boolean not null default 1;
alter table actors add column F boolean not null default 0;
alter table actors add column T boolean not null default 0;
alter table actors add column H boolean not null default 0;
update actors set G=1;

