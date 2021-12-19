create schema phone_models;
-- ----------------------------
-- Table structure for brands
-- ----------------------------
DROP TABLE IF EXISTS phone_models.brands;
CREATE TABLE phone_models.brands
(
    id         serial       NOT NULL,
    name       varchar(255) NOT NULL,
    logo       varchar(255)      DEFAULT NULL,
    deleted_at timestamp    NULL DEFAULT NULL,
    created_at timestamp    NULL DEFAULT NULL,
    updated_at timestamp    NULL DEFAULT NULL,
    PRIMARY KEY (id)
);

-- ----------------------------
-- Table structure for devices
-- ----------------------------
DROP TABLE IF EXISTS phone_models.devices;
CREATE TABLE if not exists phone_models.devices
(
    id                 serial,
    url_hash           varchar(255) NOT NULL,
    brand_id           int          NOT NULL,
    name               varchar(255) NOT NULL,
    picture            varchar(255)      DEFAULT NULL,
    released_at        varchar(255)      DEFAULT NULL,
    body               varchar(255)      DEFAULT NULL,
    os                 varchar(255)      DEFAULT NULL,
    storage            varchar(255)      DEFAULT NULL,
    display_size       varchar(255)      DEFAULT NULL,
    display_resolution varchar(255)      DEFAULT NULL,
    camera_pixels      varchar(255)      DEFAULT NULL,
    video_pixels       varchar(255)      DEFAULT NULL,
    ram                varchar(255)      DEFAULT NULL,
    chipset            varchar(255)      DEFAULT NULL,
    battery_size       varchar(255)      DEFAULT NULL,
    battery_type       varchar(255)      DEFAULT NULL,
    specifications     text         NOT NULL,
    deleted_at         timestamp    NULL DEFAULT NULL,
    created_at         timestamp    NULL DEFAULT NULL,
    updated_at         timestamp    NULL DEFAULT NULL,
    PRIMARY KEY (id)
);

-- ----------------------------
-- Table structure for models
-- ----------------------------
DROP TABLE IF EXISTS phone_models.models;
CREATE TABLE phone_models.models
(
    id         serial,
    shop_id    int          NOT NULL,
    brand_id   int          NOT NULL,
    name       varchar(255) NOT NULL,
    created_at timestamp(0) NOT NULL DEFAULT current_timestamp(0),
    deleted_at timestamp(0) NULL     DEFAULT NULL,
    updated_at timestamp(0) NULL     DEFAULT NULL,
    PRIMARY KEY (id)
);

select count('*')
from phone_models.devices;

copy
    (select m.name || ' --- ' || b.name
     from phone_models.brands b
              join phone_models.models m on b.id = m.brand_id

     limit 2000)
    to '/home/phones_data/phone_models_dict.csv'
    csv delimiter ',' header;
