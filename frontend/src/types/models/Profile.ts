/* generated using openapi-typescript-codegen -- do not edit */
/* istanbul ignore file */
/* tslint:disable */
 
import type { Avatar } from './Avatar';
import type { Control } from './Control';
import type { Summary } from './Summary';
/**
 * Adds nested create feature
 */
export type Profile = {
  avatar: Avatar;
  summary: Summary;
  controls: Array<Control>;
  color?: string;
};

