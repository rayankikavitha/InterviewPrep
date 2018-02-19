"""
I was able to answer 2 out of 4 questions successfully and execute them. Rest, I had a  of which 3 python and 1 SQL.

1. Find the GCF of given a list of numbers. Example [12,36,72] = 6
2. Find the number that is repeating the most. Example [0,0,3,4,5,4,4,4 ] , output :4
3. Find the sum of numbers that are divisible by 3 and 5 in 1000. So for sumup(10) = 23
4. Given a schema : Products, Customers, Sales
   Find  very old customer, very young customer by gender who purchases atleast 1 item

Output table should look like
         gender |     very early customer birthday   |   very last customer birthday  |
----------------------------------------------------------------------------------------------------
        F                      1960-01-01                                  2001 -01-01
         M
 //Schema

CREATE TABLE product (
    category INT NOT NULL, id INT NOT NULL,
    price DECIMAL,
    PRIMARY KEY(category, id)
)   ENGINE=INNODB;

CREATE TABLE customer (
    id INT NOT NULL,
    CUS_DOB DATE,
    CUS_GENDER VARCHAR(1),
    CUS_ADDR VARCHAR(128),
    CUS_EMAIL VARCHAR(64),
    CUS_TEL VARCHAR(16),
    CUS_PW VARCHAR(32),
    CUS_JOINDATE DATETIME,
    CUS_LASTACCESS DATE,
    PRIMARY KEY (id)
)   ENGINE=INNODB;

CREATE TABLE product_order (
    no INT NOT NULL AUTO_INCREMENT,
    product_category INT NOT NULL,
    product_id INT NOT NULL,
    customer_id INT NOT NULL,

    PRIMARY KEY(no),
    INDEX (product_category, product_id),
    INDEX (customer_id),

    FOREIGN KEY (product_category, product_id)
      REFERENCES product(category, id)
      ON UPDATE CASCADE ON DELETE RESTRICT,

    FOREIGN KEY (customer_id)
      REFERENCES customer(id)
)   ENGINE=INNODB;
"""