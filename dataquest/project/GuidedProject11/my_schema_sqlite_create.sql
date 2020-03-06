CREATE TABLE Players (
	id string,
	Last string,
	First string,
	Position integer
);

CREATE TABLE Positions (
	Position integer
);

CREATE TABLE "Team Location" (
	team_id string,
	league string,
	city string,
	franch_id string
);

CREATE TABLE "Team Nickname" (
	nickname string,
	franch_id string
);

CREATE TABLE "Park Location" (
	park_id string,
	city string,
	state string
);

CREATE TABLE "Park Info" (
	park_id string,
	name string,
	league string
);

CREATE TABLE Visitors (
	game_id string,
	V1 string,
	V2 string,
	V3 string,
	V4 string,
	V5 string,
	V6 string,
	V7 string,
	V8 string,
	V9 string
);

CREATE TABLE Games (
	game_id string,
	v_name string,
	h_name string,
	v_score string,
	h_score string,
	park_id string,
	h_manager string,
	v_manager string
);

CREATE TABLE Home (
	game_id string,
	H1 string,
	H2 string,
	H3 string,
	H4 string,
	H5 string,
	H6 string,
	H7 string,
	H8 string,
	H9 string
);

CREATE TABLE "Umpires Info" (
	id string,
	Name string
);

CREATE TABLE Umpires (
	game_id string,
	hp_umpire string,
	1b_umpire string,
	2b_umpire string,
	3b_umpire string,
	lf_umpire string,
	rf_umpire string
);

