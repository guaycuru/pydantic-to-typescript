/* tslint:disable */
/* eslint-disable */
/**
/* This file was automatically generated from pydantic models by running pydantic2ts.
/* Do not modify it by hand - just update the pydantic models and then re-run the script
*/

export interface AnimalShelter {
  address: string;
  cats: Cat[];
  dogs: Dog[];
  owner: Dog | null;
  master: Cat;
}
export interface Cat {
  name: string;
  age: number;
  declawed: boolean;
}
export interface Dog {
  name: string;
  age: number;
}
