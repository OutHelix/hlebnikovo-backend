CREATE TABLE IF NOT EXISTS public.datetable
(
    date_id integer NOT NULL DEFAULT nextval('datetable_date_id_seq'::regclass),
    date_value date NOT NULL,
    CONSTRAINT datetable_pkey PRIMARY KEY (date_id)
)

CREATE TABLE IF NOT EXISTS public.horsesinfo
(
    horse_id integer NOT NULL DEFAULT nextval('horsesinfo_horse_id_seq'::regclass),
    horsename character varying(50) COLLATE pg_catalog."default" NOT NULL,
    text1 character varying(1500) COLLATE pg_catalog."default" NOT NULL,
    text2 character varying(400) COLLATE pg_catalog."default" NOT NULL,
    text3 character varying(300) COLLATE pg_catalog."default" NOT NULL,
    pic_url character varying(200) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT horsesinfo_pkey PRIMARY KEY (horse_id)
)

CREATE TABLE IF NOT EXISTS public.questions
(
    questions_id integer NOT NULL DEFAULT nextval('questions_questions_id_seq'::regclass),
    username character varying(150) COLLATE pg_catalog."default" NOT NULL,
    phone character varying(50) COLLATE pg_catalog."default" NOT NULL,
    question character varying(2000) COLLATE pg_catalog."default" NOT NULL
)

CREATE TABLE IF NOT EXISTS public.timetable
(
    time_id integer NOT NULL DEFAULT nextval('timetable_time_id_seq'::regclass),
    time_value character varying(25) COLLATE pg_catalog."default",
    CONSTRAINT timetable_pkey PRIMARY KEY (time_id)
)

CREATE TABLE IF NOT EXISTS public.userinfo
(
    user_id integer NOT NULL DEFAULT nextval('userinfo_user_id_seq'::regclass),
    fullname character varying(150) COLLATE pg_catalog."default" NOT NULL,
    phone character varying(20) COLLATE pg_catalog."default" NOT NULL,
    numofpeople character varying(3) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT userinfo_pkey PRIMARY KEY (user_id),
    CONSTRAINT fullname UNIQUE (fullname)
        INCLUDE(fullname)
)


CREATE TABLE IF NOT EXISTS public.orders
(
    order_id integer NOT NULL DEFAULT nextval('orders_order_id_seq'::regclass),
    horse integer,
    dateoforder integer,
    timeoforder integer,
    orderuser integer,
    CONSTRAINT orders_dateoforder_fkey FOREIGN KEY (dateoforder)
        REFERENCES public.datetable (date_id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT orders_horse_fkey FOREIGN KEY (horse)
        REFERENCES public.horsesinfo (horse_id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT orders_orderuser_fkey FOREIGN KEY (orderuser)
        REFERENCES public.userinfo (user_id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT orders_timeoforder_fkey FOREIGN KEY (timeoforder)
        REFERENCES public.timetable (time_id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)


CREATE SEQUENCE IF NOT EXISTS datetable_date_id_seq;
CREATE SEQUENCE IF NOT EXISTS horsesinfo_horse_id_seq;
CREATE SEQUENCE IF NOT EXISTS questions_questions_id_seq;
CREATE SEQUENCE IF NOT EXISTS timetable_time_id_seq;
CREATE SEQUENCE IF NOT EXISTS userinfo_user_id_seq;
CREATE SEQUENCE IF NOT EXISTS orders_order_id_seq;

CREATE TABLE IF NOT EXISTS public.datetable
(
    date_id integer NOT NULL DEFAULT nextval('datetable_date_id_seq'::regclass),
    date_value date NOT NULL,
    CONSTRAINT datetable_pkey PRIMARY KEY (date_id)
);

CREATE TABLE IF NOT EXISTS public.horsesinfo
(
    horse_id integer NOT NULL DEFAULT nextval('horsesinfo_horse_id_seq'::regclass),
    horsename character varying(50) COLLATE pg_catalog."default" NOT NULL,
    text1 character varying(1500) COLLATE pg_catalog."default" NOT NULL,
    text2 character varying(400) COLLATE pg_catalog."default" NOT NULL,
    text3 character varying(300) COLLATE pg_catalog."default" NOT NULL,
    pic_url character varying(200) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT horsesinfo_pkey PRIMARY KEY (horse_id)
);

CREATE TABLE IF NOT EXISTS public.questions
(
    questions_id integer NOT NULL DEFAULT nextval('questions_questions_id_seq'::regclass),
    username character varying(150) COLLATE pg_catalog."default" NOT NULL,
    phone character varying(50) COLLATE pg_catalog."default" NOT NULL,
    question character varying(2000) COLLATE pg_catalog."default" NOT NULL
);

CREATE TABLE IF NOT EXISTS public.timetable
(
    time_id integer NOT NULL DEFAULT nextval('timetable_time_id_seq'::regclass),
    time_value character varying(25) COLLATE pg_catalog."default",
    CONSTRAINT timetable_pkey PRIMARY KEY (time_id)
);

CREATE TABLE IF NOT EXISTS public.userinfo
(
    user_id integer NOT NULL DEFAULT nextval('userinfo_user_id_seq'::regclass),
    fullname character varying(150) COLLATE pg_catalog."default" NOT NULL,
    phone character varying(20) COLLATE pg_catalog."default" NOT NULL,
    numofpeople character varying(3) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT userinfo_pkey PRIMARY KEY (user_id),
    CONSTRAINT fullname UNIQUE (fullname)
        INCLUDE(fullname)
);

CREATE TABLE IF NOT EXISTS public.orders
(
    order_id integer NOT NULL DEFAULT nextval('orders_order_id_seq'::regclass),
    horse integer,
    dateoforder integer,
    timeoforder integer,
    orderuser integer,
    CONSTRAINT orders_dateoforder_fkey FOREIGN KEY (dateoforder)
        REFERENCES public.datetable (date_id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT orders_horse_fkey FOREIGN KEY (horse)
        REFERENCES public.horsesinfo (horse_id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT orders_orderuser_fkey FOREIGN KEY (orderuser)
        REFERENCES public.userinfo (user_id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT orders_timeoforder_fkey FOREIGN KEY (timeoforder)
        REFERENCES public.timetable (time_id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
);
