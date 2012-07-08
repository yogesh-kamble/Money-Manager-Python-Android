drop table if exists default_items;
-- create default items table
create table default_items (id integer primary key,itemname text);
-- default values
-- g REFERENCES parent(a)
insert into default_items (itemname) 
      select "Petrol"
        union
      select "Internet"
       union
      select "Dish Recharge"
      union
      select "Mobile"
      union
      select "Shopping";

drop table if exists date_table;

-- Table to maintain 1:n Relationship

create table date_table(
    id integer primary key,
    entered_date date unique on conflict ignore
);

drop table if exists items;
create table items(
        id integer primary key,
        item_name text,
        amount integer,
        entered_date REFERENCES date_table(id)
);
create unique index test_idx on date_table(id);

create trigger before_insert_items before insert on items
begin
  insert into date_table(entered_date) values(strftime('%Y-%m-%d','now'));
end; 

create trigger after_insert_items after insert on items
begin
   update items set entered_date=(select max(id) from date_table);
end; 





