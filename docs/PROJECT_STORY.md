# Project Story

## Problem

Public Puerto Rico data is useful but often fragmented across agency websites and APIs. A recruiter or business stakeholder should not need to understand Census variable codes just to compare municipalities.

## Solution

This project creates a reproducible analytics layer that:

1. extracts municipality-level ACS data,
2. validates the raw dataset,
3. creates understandable KPI names,
4. calculates unemployment rate and rankings,
5. stores the results in CSV and SQLite,
6. prepares a dashboard-ready export,
7. documents how to extend the project into Power BI.

## Analytics questions

The first version focuses on questions that are easy to communicate in a portfolio interview:

- Where are Puerto Rico's most populated municipalities?
- How does median household income vary across municipalities?
- Which municipalities show the highest unemployment rates?
- Which large municipalities also show above-average unemployment?
- How can municipality rankings support prioritization and comparison?

## Next extensions

Potential future data domains:

- housing
- tourism
- electricity / energy
- education
- business activity
- healthcare access
- transportation

The goal is to add them as separate source modules rather than mixing unrelated extraction logic into one script.
