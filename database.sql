-- database_name: "pet-hotel"

CREATE TABLE "Pets" (
	"id" serial NOT NULL,
	"name" varchar(255) NOT NULL,
	"owner_id" integer NOT NULL,
	"breed" varchar(255) NOT NULL,
	"color" varchar(255) NOT NULL,
	"checked_in" BOOLEAN NOT NULL,
	"checked_in_date" DATE NOT NULL,
	CONSTRAINT "Pets_pk" PRIMARY KEY ("id")
) WITH (
  OIDS=FALSE
);

CREATE TABLE "Owner" (
	"id" serial NOT NULL,
	"name" varchar(255) NOT NULL,
	CONSTRAINT "Owner_pk" PRIMARY KEY ("id")
) WITH (
  OIDS=FALSE
);

ALTER TABLE "Pets" ADD CONSTRAINT "Pets_fk0" FOREIGN KEY ("owner_id") REFERENCES "Owner"("id");

INSERT INTO "Pets" ("name", "breed", "color", "checked_in", "checked_in_date", "owner_id")
VALUES ('Joe', 'Z-Pet', 'Black', 'TRUE', '12/4/2020', 1);

INSERT INTO "Owner" ("name")
VALUES ('Franz');