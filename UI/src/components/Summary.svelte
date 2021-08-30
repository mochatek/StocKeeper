<script>
  import { createEventDispatcher } from "svelte";

  const dispatch = createEventDispatcher();
  export let invoices;

  $: summary = invoices.reduce((summary, { item, quantity }) => {
    if (item in summary) {
      summary[item] += quantity;
    } else {
      summary[item] = quantity;
    }
    return summary;
  }, {});
</script>

{#if invoices && invoices.length}
  <h5>
    <i class="fas fa-list" />
    <span>Summary</span>
    <i
      class="fas fa-download export"
      on:click={() => dispatch("export", summary)}
    />
  </h5>
  <div>
    <table cellspacing="0" cellpadding="0">
      <thead>
        <tr>
          <th>#</th>
          <th>Item</th>
          <th>Total</th>
        </tr>
      </thead>
      <tbody>
        {#each Object.entries(summary) as [item, total], index}
          <tr>
            <td>{index + 1}</td>
            <td>{item}</td>
            <td>{total}</td>
          </tr>
        {/each}
      </tbody>
    </table>
  </div>
{/if}

<style>
  div {
    max-height: 40%;
    overflow-y: scroll;
  }
  h5 {
    color: var(--heading);
    margin: 0;
    padding: 1rem;
  }
  h5 > span {
    margin-right: 1rem;
  }
</style>
