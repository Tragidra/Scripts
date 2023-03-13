create table senler_groups
(
    id          integer default nextval('attacks_id_seq'::regclass) not null
        constraint id
            primary key,
    vk_group_id integer,
    api_token   text,
    name        text
);

alter table senler_groups
    owner to current_user
