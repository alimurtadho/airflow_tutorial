CREATE TABLE IF NOT EXISTS dl.test (
id BIGINT,
name TEXT,
created_at timestamp without time zone,
updated_at timestamp without time zone,
deleted_at timestamp without time zone,
data_updated_at timestamp without time zone,
PRIMARY KEY (id)
);