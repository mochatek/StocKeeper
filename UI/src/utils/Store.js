import { writable } from "svelte/store";
import { getItems } from "./Api";

export const itemStore = writable([], async (set) => {
  set(await getItems());
});
