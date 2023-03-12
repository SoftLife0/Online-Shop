--
-- PostgreSQL database dump
--

-- Dumped from database version 14.5 (Ubuntu 14.5-2.pgdg20.04+2)
-- Dumped by pg_dump version 14.4

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: heroku_ext; Type: SCHEMA; Schema: -; Owner: postgres
--

GRANT postgres TO postgres;

CREATE SCHEMA IF NOT EXISTS heroku_ext;


ALTER SCHEMA heroku_ext OWNER TO postgres;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: alembic_version; Type: TABLE; Schema: public; Owner: hgikcuqfytwhhw
--

CREATE TABLE public.alembic_version (
    version_num character varying(32) NOT NULL
);


ALTER TABLE public.alembic_version OWNER TO hgikcuqfytwhhw;

--
-- Name: categories; Type: TABLE; Schema: public; Owner: hgikcuqfytwhhw
--

CREATE TABLE public.categories (
    id integer NOT NULL,
    name character varying(50) NOT NULL
);


ALTER TABLE public.categories OWNER TO hgikcuqfytwhhw;

--
-- Name: categories_id_seq; Type: SEQUENCE; Schema: public; Owner: hgikcuqfytwhhw
--

CREATE SEQUENCE public.categories_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.categories_id_seq OWNER TO hgikcuqfytwhhw;

--
-- Name: categories_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: hgikcuqfytwhhw
--

ALTER SEQUENCE public.categories_id_seq OWNED BY public.categories.id;


--
-- Name: item; Type: TABLE; Schema: public; Owner: hgikcuqfytwhhw
--

CREATE TABLE public.item (
    id integer NOT NULL,
    name character varying(50) NOT NULL,
    price character varying(10),
    description character varying NOT NULL,
    image character varying,
    trending boolean,
    category character varying NOT NULL,
    vendor integer NOT NULL
);


ALTER TABLE public.item OWNER TO hgikcuqfytwhhw;

--
-- Name: item_id_seq; Type: SEQUENCE; Schema: public; Owner: hgikcuqfytwhhw
--

CREATE SEQUENCE public.item_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.item_id_seq OWNER TO hgikcuqfytwhhw;

--
-- Name: item_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: hgikcuqfytwhhw
--

ALTER SEQUENCE public.item_id_seq OWNED BY public.item.id;


--
-- Name: movies; Type: TABLE; Schema: public; Owner: hgikcuqfytwhhw
--

CREATE TABLE public.movies (
    id integer NOT NULL,
    name character varying(50) NOT NULL,
    count character varying(50) NOT NULL
);


ALTER TABLE public.movies OWNER TO hgikcuqfytwhhw;

--
-- Name: movies_id_seq; Type: SEQUENCE; Schema: public; Owner: hgikcuqfytwhhw
--

CREATE SEQUENCE public.movies_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.movies_id_seq OWNER TO hgikcuqfytwhhw;

--
-- Name: movies_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: hgikcuqfytwhhw
--

ALTER SEQUENCE public.movies_id_seq OWNED BY public.movies.id;


--
-- Name: order; Type: TABLE; Schema: public; Owner: hgikcuqfytwhhw
--

CREATE TABLE public."order" (
    id integer NOT NULL,
    name character varying NOT NULL,
    phone character varying NOT NULL,
    price character varying,
    location character varying,
    items character varying
);


ALTER TABLE public."order" OWNER TO hgikcuqfytwhhw;

--
-- Name: order_id_seq; Type: SEQUENCE; Schema: public; Owner: hgikcuqfytwhhw
--

CREATE SEQUENCE public.order_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.order_id_seq OWNER TO hgikcuqfytwhhw;

--
-- Name: order_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: hgikcuqfytwhhw
--

ALTER SEQUENCE public.order_id_seq OWNED BY public."order".id;


--
-- Name: poll; Type: TABLE; Schema: public; Owner: hgikcuqfytwhhw
--

CREATE TABLE public.poll (
    id integer NOT NULL,
    "sessionId" character varying NOT NULL,
    name character varying,
    "phoneNumber" character varying,
    movie character varying,
    "movieConfirm" character varying,
    tlk boolean,
    probability character varying,
    "startDate" character varying,
    event character varying
);


ALTER TABLE public.poll OWNER TO hgikcuqfytwhhw;

--
-- Name: poll_id_seq; Type: SEQUENCE; Schema: public; Owner: hgikcuqfytwhhw
--

CREATE SEQUENCE public.poll_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.poll_id_seq OWNER TO hgikcuqfytwhhw;

--
-- Name: poll_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: hgikcuqfytwhhw
--

ALTER SEQUENCE public.poll_id_seq OWNED BY public.poll.id;


--
-- Name: user; Type: TABLE; Schema: public; Owner: hgikcuqfytwhhw
--

CREATE TABLE public."user" (
    id integer NOT NULL,
    username character varying(10) NOT NULL,
    phone character varying(15) NOT NULL,
    password character varying(15)
);


ALTER TABLE public."user" OWNER TO hgikcuqfytwhhw;

--
-- Name: user_id_seq; Type: SEQUENCE; Schema: public; Owner: hgikcuqfytwhhw
--

CREATE SEQUENCE public.user_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.user_id_seq OWNER TO hgikcuqfytwhhw;

--
-- Name: user_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: hgikcuqfytwhhw
--

ALTER SEQUENCE public.user_id_seq OWNED BY public."user".id;


--
-- Name: categories id; Type: DEFAULT; Schema: public; Owner: hgikcuqfytwhhw
--

ALTER TABLE ONLY public.categories ALTER COLUMN id SET DEFAULT nextval('public.categories_id_seq'::regclass);


--
-- Name: item id; Type: DEFAULT; Schema: public; Owner: hgikcuqfytwhhw
--

ALTER TABLE ONLY public.item ALTER COLUMN id SET DEFAULT nextval('public.item_id_seq'::regclass);


--
-- Name: movies id; Type: DEFAULT; Schema: public; Owner: hgikcuqfytwhhw
--

ALTER TABLE ONLY public.movies ALTER COLUMN id SET DEFAULT nextval('public.movies_id_seq'::regclass);


--
-- Name: order id; Type: DEFAULT; Schema: public; Owner: hgikcuqfytwhhw
--

ALTER TABLE ONLY public."order" ALTER COLUMN id SET DEFAULT nextval('public.order_id_seq'::regclass);


--
-- Name: poll id; Type: DEFAULT; Schema: public; Owner: hgikcuqfytwhhw
--

ALTER TABLE ONLY public.poll ALTER COLUMN id SET DEFAULT nextval('public.poll_id_seq'::regclass);


--
-- Name: user id; Type: DEFAULT; Schema: public; Owner: hgikcuqfytwhhw
--

ALTER TABLE ONLY public."user" ALTER COLUMN id SET DEFAULT nextval('public.user_id_seq'::regclass);


--
-- Data for Name: alembic_version; Type: TABLE DATA; Schema: public; Owner: hgikcuqfytwhhw
--

COPY public.alembic_version (version_num) FROM stdin;
522e4f95ecce
\.


--
-- Data for Name: categories; Type: TABLE DATA; Schema: public; Owner: hgikcuqfytwhhw
--

COPY public.categories (id, name) FROM stdin;
\.


--
-- Data for Name: item; Type: TABLE DATA; Schema: public; Owner: hgikcuqfytwhhw
--

COPY public.item (id, name, price, description, image, trending, category, vendor) FROM stdin;
1	Levon 2	15	None	https://firebasestorage.googleapis.com/v0/b/ineruu-142dc.appspot.com/o/ineruu-142dc-default-rtdb%2Fineruu%2F19142965_1774749906148866_2752128699301437068_o%202.JPG.jpg?alt=media&token=c15e81cc-0a18-4413-80b3-57f3e1148657	f	Post Pill	1
2	Postinor 2	60	None	https://firebasestorage.googleapis.com/v0/b/ineruu-142dc.appspot.com/o/ineruu-142dc-default-rtdb%2Fineruu%2FIMG_1651.jpg.jpg?alt=media&token=73771556-e088-4b29-837a-6d9132ca961a	f	Post Pill	1
3	Lydia	20	None	https://firebasestorage.googleapis.com/v0/b/ineruu-142dc.appspot.com/o/ineruu-142dc-default-rtdb%2Fineruu%2FIMG_1652.JPG.jpg?alt=media&token=445fe275-878a-4a2c-a932-7f935cc0491b	f	Post Pill	1
6	Kiss	8	None	https://firebasestorage.googleapis.com/v0/b/ineruu-142dc.appspot.com/o/ineruu-142dc-default-rtdb%2Fineruu%2FIMG_1648.PNG.jpg?alt=media&token=44077f8f-d739-4eb7-b938-ec15f841269a	f	Protection	1
7	Fiesta	12	None	https://firebasestorage.googleapis.com/v0/b/ineruu-142dc.appspot.com/o/ineruu-142dc-default-rtdb%2Fineruu%2FIMG_1650.PNG.jpg?alt=media&token=e7c75233-b5fe-4706-b5f2-78946a3f8474	f	Protection	1
8	Ky Lube	60	None	https://firebasestorage.googleapis.com/v0/b/ineruu-142dc.appspot.com/o/ineruu-142dc-default-rtdb%2Fineruu%2Fimage_8633cd93-dca2-4d4d-a789-4e794a938fb0.jpg.jpg?alt=media&token=83a51dc2-3f73-43d9-9fb5-9fa6a6abd2bf	f	Lubrication	1
9	Fiesta Lube	30	None	https://firebasestorage.googleapis.com/v0/b/ineruu-142dc.appspot.com/o/ineruu-142dc-default-rtdb%2Fineruu%2Fimage_a0fe5acb-bafe-4c0b-a93f-6e7bb9798300.jpg.jpg?alt=media&token=db69a31c-0b6f-4a0e-a1bc-12b75c89d4dc	f	Post Pill	1
10	Pregnancy Test Kit	13	None	https://firebasestorage.googleapis.com/v0/b/ineruu-142dc.appspot.com/o/ineruu-142dc-default-rtdb%2Fineruu%2F114445086_1006522923152275_159744739896315391_n.jpg.jpg?alt=media&token=0834768f-d71b-4da1-a4dd-be4312201d11	f	Test Kits	1
11	Dragon Delay Spray	48	Dragon Delay Spray	https://firebasestorage.googleapis.com/v0/b/ineruu-142dc.appspot.com/o/ineruu-142dc-default-rtdb%2Fineruu%2F11446874_super-dragon-6000-12ml-delay-spray_1600x1710.jpg.jpg?alt=media&token=d0c7d5d5-a59a-46d9-86f1-d2ca70ebbb11	f	Delay	1
\.


--
-- Data for Name: movies; Type: TABLE DATA; Schema: public; Owner: hgikcuqfytwhhw
--

COPY public.movies (id, name, count) FROM stdin;
3	This Lady Called Life	0
5	Fatherhood	5
4	Black Widow	12
2	Cruella	8
1	Black Panther	31
\.


--
-- Data for Name: order; Type: TABLE DATA; Schema: public; Owner: hgikcuqfytwhhw
--

COPY public."order" (id, name, phone, price, location, items) FROM stdin;
1	Kkk	0208047371	13	J and j	Pregnancy Test Kit * 1 = 13,Total = 13
2	Kkk	0208043714	13	J and j	Pregnancy Test Kit * 1 = 13,Total = 13
3	Giv	0545977791	28	Da	Pregnancy Test Kit * 1 = 13,Levon 2 * 1 = 15,Total = 28
4	nk	0545977791	103	ghana	Pregnancy Test Kit * 1 = 13,Fiesta Lube * 1 = 30,Ky Lube * 1 = 60,Total = 103
5	sd	0545977791	90	ghana	Fiesta Lube * 1 = 30,Ky Lube * 1 = 60,Total = 90
6	jg	0545977791	150	ghana	Fiesta Lube * 5 = 150,Total = 150
7	nm	0545977791	28	gh	Pregnancy Test Kit * 1 = 13,Levon 2 * 1 = 15,Total = 28
8	nk	0545977791	8	gh	Kiss * 1 = 8,Total = 8
9	Thxg	0244332212	13	Cdr	Pregnancy Test Kit * 1 = 13,Total = 13
10	Ggg	0546401277	13	J and J	Pregnancy Test Kit * 1 = 13,Total = 13
11	Nk	0545977791	25	Ghana	Pregnancy Test Kit * 1 = 13,Fiesta * 1 = 12,Total = 25
12	Hgh	0554766889	38	Valerie 	Fiesta Lube * 1 = 30,Kiss * 1 = 8,Total = 38
13	Okayyyy	0264167630	33	Accra	Pregnancy Test Kit * 1 = 13,Lydia * 1 = 20,Total = 33
14	Gvjv	0545977787	90	Ghg	Fiesta Lube * 1 = 30,Ky Lube * 1 = 60,Total = 90
15	Kwame1	0201403402	30	J&j	Fiesta Lube * 1 = 30,Total = 30
16	Eben	0245595389	12	Silver state	Fiesta * 1 = 12,Total = 12
17	Softlife	+233508495	8	Old Girls E307	Kiss * 1 = 8,Total = 8
18	reginald	0240592667	32	cape coast	Lydia * 1 = 20,Fiesta * 1 = 12,Total = 32
19	37837	0256249333	35	Test	Lydia * 1 = 20,Levon 2 * 1 = 15,Total = 35
20	me	0241348011	13	silver state	Pregnancy Test Kit * 1 = 13,Total = 13
21	nk	0545977791	38	Accra, Ghana	Kiss * 1 = 8,Fiesta Lube * 1 = 30,Total = 38
22	ama	0240556123	15	Cape Coast	Levon 2 * 1 = 15,Total = 15
23	Test	0545977791	30	Accra	Fiesta Lube * 1 = 30,Total = 30
24	Ferguson	0544261165	20	Beam court 303	Lydia * 1 = 20,Total = 20
25	Bree	0208372280	13	Pronto block 4 room 14 	Pregnancy Test Kit * 1 = 13,Total = 13
26	Raph	0200242202	20	Starkey hostel	Lydia * 1 = 20,Total = 20
27	Kwaku	020*******	8	Location 	Kiss * 1 = 8,Total = 8
28	Esther	0203409976	12	pronto block 5 room 17	Fiesta * 1 = 12,Total = 12
29	Ama	0571234568	13	JnJ	Pregnancy Test Kit * 1 = 13,Total = 13
30	Naa	0572491480	15	Old girls tv room 3rd floor 	Levon 2 * 1 = 15,Total = 15
31	Naa	0572491480	15	Old girls tv room 3rd floor 	Levon 2 * 1 = 15,Total = 15
32	1real_rena	0547691327	20	Pronto Block 3 Room 8	Fiesta * 1 = 12,Kiss * 1 = 8,Total = 20
33	1real_rena	0547691327	20	Pronto Block 3 Room 8	Fiesta * 1 = 12,Kiss * 1 = 8,Total = 20
34	1real_rena	0547691327	20	Block E	Lydia * 1 = 20,Total = 20
35	1real_rena	0547691327	20	Block E	Lydia * 1 = 20,Total = 20
36	None	0549001905	0	F block 201	Total = 0
37	Kweku-Test	0545977791	13	Accra	Pregnancy Test Kit * 1 = 13,Total = 13
38	1real_rena	0547691327	12	Pronto Block 3 Room 8	Fiesta * 1 = 12,Total = 12
39	Ayele	0500178941	20	Aseda 	Lydia * 1 = 20,Total = 20
40	Ayele	0500178941	20	Aseda 	Lydia * 1 = 20,Total = 20
41	Shev	0592958353	12	Queenscourt	Fiesta * 1 = 12,Total = 12
42	Ella	0554911625	13	Pimag 	Pregnancy Test Kit * 1 = 13,Total = 13
43	mcskorlah	0597236129	0	Pronto Potters Lodge 	Total = 0
44	Zoziii	0545977791	48	Accra, Near labadi	Dragon Delay Spray * 1 = 48,Total = 48
45	Kwame	45677889hg	20	Fagagagaha	Lydia * 1 = 20,Total = 20
46	Evelyn	0241667886	145	Pronto	Lydia * 4 = 80,Pregnancy Test Kit * 5 = 65,Total = 145
47	Testing	0545977791	13	Testin!	Pregnancy Test Kit * 1 = 13,Total = 13
48	Love	0544036047	15	Pronto block 5 room 28	Levon 2 * 1 = 15,Total = 15
49	Love	0502552544	15	Pronto block 5 room 28	Levon 2 * 1 = 15,Total = 15
50	SB	0597236129	0	Pronto potters 	Total = 0
51	Serwaah	0544036047	15	Pronto Block 5 Room 28	Levon 2 * 1 = 15,Total = 15
52	Nana	0549322598	48	Dansoman	Dragon Delay Spray * 1 = 48,Total = 48
53	Yaa	0592904697	20	Fortress hostel. Room 2	Lydia * 1 = 20,Total = 20
54	Yaa	0592904697	20	Fortress hostel. Room 2	Lydia * 1 = 20,Total = 20
55	Yaa	0592904697	20	Fortress room 2	Lydia * 1 = 20,Total = 20
56	Koti	0205596108	60	Pent block B	Ky Lube * 1 = 60,Total = 60
57	asdf	0545977791	12	asdf	Fiesta * 1 = 12,Total = 12
58	Test	0570136459	48	Pronto block 6 room 12	Dragon Delay Spray * 1 = 48,Total = 48
59	asdf	0545977791	48	Accra	Dragon Delay Spray * 1 = 48,Total = 48
60	Test	0545977791	20	Ghana	Lydia * 1 = 20,Total = 20
61	SJ	0264121190	20	Pronto block 1 Room28	Lydia * 1 = 20,Total = 20
62	flow	0545977791	48	test-flow	Dragon Delay Spray * 1 = 48,Total = 48
63	asdf	0545977791	96	asdf	Dragon Delay Spray * 2 = 96,Total = 96
64	Ghana	0545977791	480	Ghana	Dragon Delay Spray * 10 = 480,Total = 480
65	asdf	0545977791	48	asdf	Dragon Delay Spray * 1 = 48,Total = 48
66	asdf	0545977791	48	asdf	Dragon Delay Spray * 1 = 48,Total = 48
67	asdf	0545977791	48	asdf	Dragon Delay Spray * 1 = 48,Total = 48
68	Enidpepper	0552814942	93	Block 3 room 12	Pregnancy Test Kit * 1 = 13,Ky Lube * 1 = 60,Lydia * 1 = 20,Total = 93
69	Naa	0264230549	15	Adedwua hostel	Levon 2 * 1 = 15,Total = 15
70	pinkmimosa	0504229002	20	pronto block 2 room 16	Lydia * 1 = 20,Total = 20
71	pdf	0545966691	48	sdf	Dragon Delay Spray * 1 = 48,Total = 48
72	sss	0545977791	48	qdf	Dragon Delay Spray * 1 = 48,Total = 48
73	Love	0544036047	20	Pronto Block 5 Room 28	Lydia * 1 = 20,Total = 20
74	Mac	0541761355	28	Queens court	Lydia * 1 = 20,Kiss * 1 = 8,Total = 28
\.


--
-- Data for Name: poll; Type: TABLE DATA; Schema: public; Owner: hgikcuqfytwhhw
--

COPY public.poll (id, "sessionId", name, "phoneNumber", movie, "movieConfirm", tlk, probability, "startDate", event) FROM stdin;
1	16686508931592598	\N	\N	\N	\N	\N	\N	\N	A Night Under The Stars
38	16687749211514504	\N	233550381395	Black Panther	\N	f	0	2022-11-18 12:35:33.721905	A Night Under The Stars
15	16687005621521339	\N	\N	Black Panther	\N	t	10	2022-11-17 15:56:12.212967	A Night Under The Stars
25	16687088371569635	\N	\N	Black Panther	\N	f	0	2022-11-17 18:14:05.771386	A Night Under The Stars
2	16686510801777393	\N	\N	1	\N	t	5	2022-11-17 02:11:25.03034	A Night Under The Stars
3	16686525502497257	\N	\N	\N	\N	\N	\N	2022-11-17 02:35:54.260083	A Night Under The Stars
33	16687705721549467	\N	233552878489	Black Panther	\N	f	0	2022-11-18 11:23:04.411932	A Night Under The Stars
16	16687009152473588	\N	\N	Black Panther	\N	t	10	2022-11-17 16:02:02.220746	A Night Under The Stars
4	16686526191594049	\N	\N	Black Panther	\N	t	7	2022-11-17 02:37:04.331105	A Night Under The Stars
26	5006258333	\N	\N	Black Panther	\N	t	72912$$2 shwkq	2022-11-17 18:42:58.182771	A Night Under The Stars
5	16686526512497371	\N	\N	Black Panther	\N	t	4	2022-11-17 02:37:35.156793	A Night Under The Stars
17	16687010221529722	\N	\N	Cruella	\N	t	10	2022-11-17 16:03:48.971426	A Night Under The Stars
6	16686528262497564	\N	\N	Black Widow	\N	f	0	2022-11-17 02:40:32.36703	A Night Under The Stars
27	5006270520	\N	\N	\N	\N	\N	\N	2022-11-17 18:48:51.008541	A Night Under The Stars
7	16686528671594252	\N	\N	Fatherhood	\N	f	0	2022-11-17 02:41:12.2277	A Night Under The Stars
34	16687723221571546	\N	233550934289	Black Panther	\N	\N	\N	2022-11-18 11:52:12.042871	A Night Under The Stars
43	5008225637	\N	233507959777	Black Panther	\N	\N	User timeout	2022-11-18 18:05:38.995974	A Night Under The Stars
28	16687365162485572	\N	\N	Cruella	\N	f	0	2022-11-18 01:55:20.725217	A Night Under The Stars
8	16686530852497834	\N	\N	Black Widow	\N	t	3	2022-11-17 02:44:49.037188	A Night Under The Stars
19	16687033261776694	\N	\N	Black Panther	\N	t	7	2022-11-17 16:42:12.923079	A Night Under The Stars
18	16687033031576508	\N	\N	Black Panther	\N	t	10	2022-11-17 16:41:52.520922	A Night Under The Stars
9	16686547181595756	\N	\N	Cruella	\N	t	5	2022-11-17 03:12:02.675396	A Night Under The Stars
39	828017323	\N	233205596308	Black Panther	\N	t	100	2022-11-18 13:08:43.780331	A Night Under The Stars
35	16687723941789828	\N	233550934289	Black Panther	\N	f	0	2022-11-18 11:53:22.645556	A Night Under The Stars
10	16686567622411946	\N	\N	Black Panther	\N	t	6	2022-11-17 03:46:08.010889	A Night Under The Stars
29	3000000007866373	\N	\N	Cruella	\N	t	4	2022-11-18 07:22:50.087998	A Night Under The Stars
20	16687054591768669	\N	\N	Black Panther	\N	f	0	2022-11-17 17:17:52.048944	A Night Under The Stars
11	16686569651597733	\N	\N	Black Widow	\N	f	0	2022-11-17 03:49:29.923154	A Night Under The Stars
21	5006066862	\N	\N	Black Panther	\N	f	0	2022-11-17 17:17:57.614737	A Night Under The Stars
12	16686694541754530	\N	\N	Black Panther	\N	f	0	2022-11-17 07:17:45.12955	A Night Under The Stars
13	826005449	\N	\N	\N	\N	\N	\N	2022-11-17 13:42:13.291299	A Night Under The Stars
46	16688428621548928	\N	233245399024	Black Panther	\N	t	8	2022-11-19 07:27:53.498365	A Night Under The Stars
22	16687055321771666	\N	\N	Black Panther	\N	t	10	2022-11-17 17:19:00.299808	A Night Under The Stars
14	16687005341520820	\N	\N	Black Panther	\N	t	10	2022-11-17 15:55:45.249308	A Night Under The Stars
30	16687657651763829	\N	\N	Black Panther	\N	t	4	2022-11-18 10:02:49.341291	A Night Under The Stars
23	826402788	\N	\N	\N	\N	\N	\N	2022-11-17 17:25:15.833279	A Night Under The Stars
36	16687736751588614	\N	233245182064	Black Panther	\N	t	7	2022-11-18 12:14:41.84543	A Night Under The Stars
40	5007696125	\N	233501098468	Black Panther	\N	f	0	2022-11-18 13:16:08.19467	A Night Under The Stars
24	826434362	\N	\N	Black Panther	\N	t	10	2022-11-17 17:39:39.710933	A Night Under The Stars
31	16687659402434277	\N	233545977791	Black Panther	\N	t	4	2022-11-18 10:05:44.514498	A Night Under The Stars
44	5008704853	\N	233208674182	Black Panther	\N	f	0	2022-11-18 20:51:29.574219	A Night Under The Stars
41	828032447	\N	233501098468	\N	\N	\N	\N	2022-11-18 13:18:06.630589	A Night Under The Stars
37	16687745862449103	\N	233544036047	Black Panther	\N	t	8	2022-11-18 12:29:58.570624	A Night Under The Stars
32	827750057	\N	233508935217	Black Panther	\N	f	0	2022-11-18 10:35:47.454307	A Night Under The Stars
47	16688604251787007	\N	233245595389	\N	\N	\N	\N	\N	A Night Under The Stars
42	2005497566600497	\N	233264121190	Black Panther	\N	t	10	2022-11-18 15:27:11.20949	A Night Under The Stars
45	829229316	\N	233205344689	Black Panther	\N	t	7	2022-11-18 22:46:11.229204	A Night Under The Stars
\.


--
-- Data for Name: user; Type: TABLE DATA; Schema: public; Owner: hgikcuqfytwhhw
--

COPY public."user" (id, username, phone, password) FROM stdin;
1	admin	0545977791	password
\.


--
-- Name: categories_id_seq; Type: SEQUENCE SET; Schema: public; Owner: hgikcuqfytwhhw
--

SELECT pg_catalog.setval('public.categories_id_seq', 1, false);


--
-- Name: item_id_seq; Type: SEQUENCE SET; Schema: public; Owner: hgikcuqfytwhhw
--

SELECT pg_catalog.setval('public.item_id_seq', 11, true);


--
-- Name: movies_id_seq; Type: SEQUENCE SET; Schema: public; Owner: hgikcuqfytwhhw
--

SELECT pg_catalog.setval('public.movies_id_seq', 5, true);


--
-- Name: order_id_seq; Type: SEQUENCE SET; Schema: public; Owner: hgikcuqfytwhhw
--

SELECT pg_catalog.setval('public.order_id_seq', 74, true);


--
-- Name: poll_id_seq; Type: SEQUENCE SET; Schema: public; Owner: hgikcuqfytwhhw
--

SELECT pg_catalog.setval('public.poll_id_seq', 47, true);


--
-- Name: user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: hgikcuqfytwhhw
--

SELECT pg_catalog.setval('public.user_id_seq', 1, true);


--
-- Name: alembic_version alembic_version_pkc; Type: CONSTRAINT; Schema: public; Owner: hgikcuqfytwhhw
--

ALTER TABLE ONLY public.alembic_version
    ADD CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num);


--
-- Name: categories categories_pkey; Type: CONSTRAINT; Schema: public; Owner: hgikcuqfytwhhw
--

ALTER TABLE ONLY public.categories
    ADD CONSTRAINT categories_pkey PRIMARY KEY (id);


--
-- Name: item item_pkey; Type: CONSTRAINT; Schema: public; Owner: hgikcuqfytwhhw
--

ALTER TABLE ONLY public.item
    ADD CONSTRAINT item_pkey PRIMARY KEY (id);


--
-- Name: movies movies_pkey; Type: CONSTRAINT; Schema: public; Owner: hgikcuqfytwhhw
--

ALTER TABLE ONLY public.movies
    ADD CONSTRAINT movies_pkey PRIMARY KEY (id);


--
-- Name: order order_pkey; Type: CONSTRAINT; Schema: public; Owner: hgikcuqfytwhhw
--

ALTER TABLE ONLY public."order"
    ADD CONSTRAINT order_pkey PRIMARY KEY (id);


--
-- Name: poll poll_pkey; Type: CONSTRAINT; Schema: public; Owner: hgikcuqfytwhhw
--

ALTER TABLE ONLY public.poll
    ADD CONSTRAINT poll_pkey PRIMARY KEY (id);


--
-- Name: user user_pkey; Type: CONSTRAINT; Schema: public; Owner: hgikcuqfytwhhw
--

ALTER TABLE ONLY public."user"
    ADD CONSTRAINT user_pkey PRIMARY KEY (id);


--
-- Name: item item_vendor_fkey; Type: FK CONSTRAINT; Schema: public; Owner: hgikcuqfytwhhw
--

ALTER TABLE ONLY public.item
    ADD CONSTRAINT item_vendor_fkey FOREIGN KEY (vendor) REFERENCES public."user"(id) ON DELETE CASCADE;


--
-- Name: SCHEMA heroku_ext; Type: ACL; Schema: -; Owner: postgres
--

GRANT USAGE ON SCHEMA heroku_ext TO hgikcuqfytwhhw;


--
-- Name: SCHEMA public; Type: ACL; Schema: -; Owner: hgikcuqfytwhhw
--

REVOKE ALL ON SCHEMA public FROM postgres;
REVOKE ALL ON SCHEMA public FROM PUBLIC;
GRANT ALL ON SCHEMA public TO hgikcuqfytwhhw;
GRANT ALL ON SCHEMA public TO PUBLIC;


--
-- Name: LANGUAGE plpgsql; Type: ACL; Schema: -; Owner: postgres
--

GRANT ALL ON LANGUAGE plpgsql TO hgikcuqfytwhhw;


--
-- PostgreSQL database dump complete
--

