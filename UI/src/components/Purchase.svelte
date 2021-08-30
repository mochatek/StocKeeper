<script>
  import { onMount } from "svelte";
  import { getInvoices, insertInvoice, saveToPDF } from "../utils/Api";
  import Filters from "./Filters.svelte";
  import Controls from "./Controls.svelte";
  import Invoices from "./Invoices.svelte";
  import Summary from "./Summary.svelte";
  import NewItem from "./NewItem.svelte";

  let invoices;
  let loading = false;
  let search;
  let duration;
  let showModal = false;

  onMount(async () => {
    loading = true;
    invoices = await getInvoices("purchase");
    loading = false;
    duration = "today";
    search = "";
  });

  $: filteredInvoices = filterOnDuration(invoices, duration);

  $: filteredInvoices = filterOnSearch(search);

  function filterOnDuration(invoices, duration) {
    if (duration === "today") {
      return invoices.filter(
        ({ date }) => date === new Date().toLocaleDateString("en-GB")
      );
    } else if (duration === "month") {
      const thisMonth = new Date().getMonth() + 1;
      const thisYear = new Date().getFullYear();

      return invoices.filter(({ date }) => {
        const [_, month, year] = date.split("/");
        return +year === thisYear && +month === thisMonth;
      });
    } else {
      return invoices;
    }
  }

  function filterOnSearch(search) {
    return search
      ? filteredInvoices.filter(({ date, invoiceID, item, quantity }) =>
          [date, invoiceID, item, quantity].some((value) =>
            `${value}`.toLocaleLowerCase().includes(search.toLocaleLowerCase())
          )
        )
      : filterOnDuration(invoices, duration);
  }

  async function addInvoice({ detail: newInvoice }) {
    if (await insertInvoice(newInvoice, "Purchase")) {
      invoices = [newInvoice, ...invoices];
    }
  }

  function exportInvoices({ detail: summary }) {
    if (filteredInvoices && filteredInvoices.length) {
      const category = "Sale";
      let period = new Date();
      switch (duration) {
        case "today":
          period = period.toLocaleDateString("en-GB");
          break;
        case "month":
          period = period.toLocaleString("default", {
            month: "long",
            year: "numeric",
          });
          break;
        case "year":
          period = period.getFullYear();
          break;
      }

      saveToPDF(
        category,
        period,
        search,
        summary || filteredInvoices,
        summary ? true : false
      );
    }
  }
</script>

{#if showModal}
  <NewItem on:close={() => (showModal = false)} />
{/if}

<div>
  <h4>
    <i class="fas fa-shopping-cart" /><span>New Purchase</span>
  </h4>
  <Controls on:newInvoice={addInvoice}>
    <button
      slot="newItemButton"
      type="button"
      on:click={() => (showModal = true)}
    >
      <i class="fas fa-plus-square" />&nbsp;&nbsp;New Item</button
    >
  </Controls>
</div>

<article>
  <div>
    <Filters bind:duration on:export={exportInvoices} />
    <input
      type="search"
      placeholder="Search"
      autocomplete="off"
      bind:value={search}
    />
  </div>
  <Invoices invoices={filteredInvoices || []} {loading} />
  <Summary invoices={filteredInvoices || []} on:export={exportInvoices} />
</article>

<style>
  input[type="search"] {
    padding: 0.5rem;
    width: 13rem;
    border: none;
    background: var(--bg);
  }
  article {
    background: white;
    border: 1px solid lightgrey;
    color: grey;
    border-radius: 5px;
    padding: 0.5rem 1rem;
    height: 88%;
  }
  input {
    margin: 0;
    padding: 0;
    width: 10px;
  }
  div {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 0.5rem;
  }
  h4 {
    display: flex;
    align-items: center;
    color: var(--heading);
    margin-top: 0;
  }
  h4 > i {
    margin-right: 1rem;
    padding-bottom: 0.25rem;
    cursor: pointer;
    font-size: 28px;
  }
  input {
    margin: 0;
    padding: 0;
    width: 10px;
  }
  div {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 0.5rem;
  }
  button {
    color: white;
    background: rgb(172, 170, 170);
    font-weight: bold;
    width: 15%;
  }
  button:hover {
    background: grey;
  }
</style>
