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
export interface ImportedSubModule {
  sub: SubModel;
}
export interface SubModel {
  bar: Bar;
}
export interface ModelOne {
  foo: Foo;
}
export interface ModelTwo {
  foo: Foo1;
}

export const enum Bar {
  ONE = "one",
  TWO = "two"
}
export const enum Foo {
  ONE_A = "one_a",
  ONE_B = "one_b"
}
export const enum Foo1 {
  TWO_A = "two_a",
  TWO_B = "two_b"
}
