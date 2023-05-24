CREATE TABLE IF NOT EXISTS "User" (
	"Id" serial NOT NULL,
	"UserName" varchar(255) NOT NULL,
	"UserEmail" varchar(255) NOT NULL UNIQUE,
	"UserPassword" varchar(255) NOT NULL,
	CONSTRAINT "User_pk" PRIMARY KEY ("Id")
) WITH (
  OIDS=FALSE
);



CREATE TABLE IF NOT EXISTS "Car" (
	"Id" serial NOT NULL,
	"User" bigint NOT NULL,
	"Driver" varchar(255) NOT NULL,
	"Contact" varchar(255) NOT NULL,
	"Date" DATE NOT NULL,
	"LicencePlate" varchar(255) NOT NULL,
	CONSTRAINT "Car_pk" PRIMARY KEY ("Id")
) WITH (
  OIDS=FALSE
);



CREATE TABLE IF NOT EXISTS "Expense" (
	"Id" serial NOT NULL,
	"User" bigint NOT NULL,
	"Car" bigserial NOT NULL,
	"Sum" bigint NOT NULL,
	"Date" DATE NOT NULL,
	"IsCash" bool NOT NULL,
	"Description" varchar(255) NOT NULL,
	CONSTRAINT "Expense_pk" PRIMARY KEY ("Id")
) WITH (
  OIDS=FALSE
);



CREATE TABLE IF NOT EXISTS "Income" (
	"Id" serial NOT NULL,
	"User" bigint NOT NULL,
	"Car" bigint NOT NULL,
	"Deal" bigint NOT NULL,
	"Sender" varchar(255) NOT NULL,
	"Sum" bigint NOT NULL,
	"Date" DATE NOT NULL,
	"IsCash" bool NOT NULL,
	CONSTRAINT "Income_pk" PRIMARY KEY ("Id")
) WITH (
  OIDS=FALSE
);



CREATE TABLE IF NOT EXISTS "Deal" (
	"Id" serial NOT NULL,
	"Car" bigint NOT NULL,
	"User" bigint NOT NULL,
	"From" varchar(255) NOT NULL,
	"To" varchar(255) NOT NULL,
	"Company" varchar(255) NOT NULL,
	"Sum" bigint NOT NULL,
	"Date" DATE NOT NULL,
	CONSTRAINT "Deal_pk" PRIMARY KEY ("Id")
) WITH (
  OIDS=FALSE
);



ALTER TABLE "Car" DROP CONSTRAINT IF EXISTS "Car_fk0";
ALTER TABLE "Car" ADD CONSTRAINT "Car_fk0" FOREIGN KEY ("User") REFERENCES "User"("Id");

ALTER TABLE "Expense" DROP CONSTRAINT IF EXISTS "Expense_fk0";
ALTER TABLE "Expense" DROP CONSTRAINT IF EXISTS "Expense_fk1";

ALTER TABLE "Expense" ADD CONSTRAINT "Expense_fk0" FOREIGN KEY ("User") REFERENCES "User"("Id");
ALTER TABLE "Expense" ADD CONSTRAINT "Expense_fk1" FOREIGN KEY ("Car") REFERENCES "Car"("Id");

ALTER TABLE "Income" DROP CONSTRAINT IF EXISTS "Income_fk0";
ALTER TABLE "Income" DROP CONSTRAINT IF EXISTS "Income_fk1";
ALTER TABLE "Income" DROP CONSTRAINT IF EXISTS "Income_fk2";

ALTER TABLE "Income" ADD CONSTRAINT "Income_fk0" FOREIGN KEY ("User") REFERENCES "User"("Id");
ALTER TABLE "Income" ADD CONSTRAINT "Income_fk1" FOREIGN KEY ("Car") REFERENCES "Car"("Id");
ALTER TABLE "Income" ADD CONSTRAINT "Income_fk2" FOREIGN KEY ("Deal") REFERENCES "Deal"("Id");

ALTER TABLE "Deal" DROP CONSTRAINT IF EXISTS "Deal_fk0";
ALTER TABLE "Deal" DROP CONSTRAINT IF EXISTS "Deal_fk1";
ALTER TABLE "Deal" ADD CONSTRAINT "Deal_fk0" FOREIGN KEY ("Car") REFERENCES "Car"("Id");
ALTER TABLE "Deal" ADD CONSTRAINT "Deal_fk1" FOREIGN KEY ("User") REFERENCES "User"("Id");






