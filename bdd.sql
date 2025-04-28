SET FOREIGN_KEY_CHECKS = 0;

DROP TABLE IF EXISTS sales_method;
DROP TABLE IF EXISTS region;
DROP TABLE IF EXISTS property_type;
DROP TABLE IF EXISTS seller;
DROP TABLE IF EXISTS suburb;
DROP TABLE IF EXISTS property;

CREATE TABLE region ( 
	id_region           INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
	label               VARCHAR(255)
);

CREATE TABLE suburb ( 
	id_suburb          INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
	label               VARCHAR(255) NOT NULL,
	distance_to_city_center INT UNSIGNED NOT NULL,
	property_count		INT UNSIGNED,
	id_region          INT UNSIGNED,
	CONSTRAINT fk_suburb_region FOREIGN KEY (id_region) REFERENCES region(id_region) ON DELETE RESTRICT
);

CREATE TABLE sales_method ( 
	id_sales_method      INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
	label               VARCHAR(255)       
);

CREATE TABLE property_type ( 
	id_property_type    INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
	label               VARCHAR(255) NOT NULL   
);

CREATE TABLE seller ( 
	id_seller          INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
	label              VARCHAR(255)       
);

CREATE TABLE property (
	id                   INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
	sale_date            DATE,
	price                INT UNSIGNED,
	bedroom_count        INT UNSIGNED,
	bathroom_count       INT UNSIGNED,
	parking_count        INT UNSIGNED,
	land_area            INT UNSIGNED,
	living_area          INT UNSIGNED,
	construction_year    YEAR,
	latitude             FLOAT,
	longitude            FLOAT,
	property_address     VARCHAR(255),
	id_seller            INT UNSIGNED,
	id_property_type     INT UNSIGNED,
	id_sales_method      INT UNSIGNED,
	id_suburb            INT UNSIGNED,
	CONSTRAINT fk_property_suburb FOREIGN KEY (id_suburb) REFERENCES suburb(id_suburb) ON DELETE RESTRICT,
	CONSTRAINT fk_property_sales_method FOREIGN KEY (id_sales_method) REFERENCES sales_method(id_sales_method) ON DELETE RESTRICT,
	CONSTRAINT fk_property_type FOREIGN KEY (id_property_type) REFERENCES property_type(id_property_type) ON DELETE RESTRICT,
	CONSTRAINT fk_property_seller FOREIGN KEY (id_seller) REFERENCES seller(id_seller) ON DELETE RESTRICT
);
