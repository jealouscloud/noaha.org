# Data
The purpose of this module is to effectively separate all conversations with
data sources into its own little isolated module.

The goal of this purpose is to
* Allow easy swapping of data sources when you need to scale to the next one
* Setup performant and bespoke methods to speak to data in its native language

## store module
The store is what any other part of the application speaks to. It's what handles
speaking to any adapters for any kinds of data.

## SQLAlchemy

In this project, we recommend using SQLAlchemy in **Core** mode.

Data can be queried using **ORM models**, which we do. However, when execuuting
in ORM mode, SQLAlchemy copies the results into the ORM models.

These ORM models have secret gotchas like accidentally triggering a query for a
field that you did not originally query.

Often they must be marshalled into a more appropriate type anyhow-

So my recommendation is to parse your query into a namedtuple matching your
exact query.

You can validate the correct columns via `adapters.param_check`

You can alias any params you query so they match your NamedTuple arg names.