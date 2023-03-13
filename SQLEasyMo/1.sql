create table workshops_shifts
(
    id          serial
        primary key,
    name    varchar
);

alter table workshops_shifts_content
    owner to easymo_db_user;