<script>
  import { createEventDispatcher, onMount } from "svelte";
  import { itemStore } from "../utils/Store";

  const dispatch = createEventDispatcher();
  let invoiceID = "";
  let item = "";
  let quantity = "";
  let items = [];

  onMount(async () => {
    itemStore.subscribe((value) => {
      items = value;
    });
  });

  function addInvoice() {
    if ([invoiceID, quantity, item].some((value) => value.trim())) {
      const date = new Date().toLocaleDateString("en-GB");
      dispatch("newInvoice", { date, invoiceID, item, quantity });
      reset();
    }
  }

  export function reset() {
    invoiceID = "";
    item = "";
    quantity = "";
  }
</script>

<form autocomplete="off" on:submit|preventDefault={addInvoice}>
  <slot name="newItemButton" />

  <input
    type="text"
    name="invoice"
    placeholder="Invoice ID"
    required
    bind:value={invoiceID}
  />

  <select name="item" required bind:value={item}>
    <option value="">-- SELECT ITEM --</option>
    {#each items as item}
      <option value={item}>{item}</option>
    {/each}
  </select>

  <input
    type="number"
    name="quantity"
    placeholder="Quantity"
    min="1"
    required
    bind:value={quantity}
  />

  <button type="submit">
    <i class="fas fa-plus-square" />&nbsp;&nbsp;Add
  </button>
</form>

<style>
  form {
    display: flex;
    align-items: center;
    justify-content: space-evenly;
  }
  button {
    color: white;
    background: var(--primary);
    font-weight: bold;
    width: 10%;
  }
  button:hover {
    background: var(--secondary);
  }
</style>
