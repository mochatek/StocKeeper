<script>
  export let invoices, loading;
  import Loading from "./Loading.svelte";

  $: total = Array.isArray(invoices)
    ? invoices.reduce((sum, { quantity }) => sum + quantity, 0)
    : 0;
</script>

{#if loading}
  <Loading />
{:else if invoices.length}
  <div>
    <table cellspacing="0" cellpadding="0">
      <thead>
        <tr>
          <th>Date</th>
          <th>#Invoice</th>
          <th>Item</th>
          <th>Quantity</th>
        </tr>
      </thead>
      <tbody>
        {#each invoices as { date, invoiceID, item, quantity }}
          <tr>
            <td>{date}</td>
            <td>{invoiceID}</td>
            <td>{item}</td>
            <td>{quantity}</td>
          </tr>
        {/each}
      </tbody>
      <tfoot>
        <tr>
          <th colspan="3" style="text-align: right" class="freeze">Total</th>
          <th class="freeze"><span>{total}</span></th>
        </tr>
      </tfoot>
    </table>
  </div>
{:else}
  <h6 class="alert"><i class="fas fa-info-circle" />&nbsp;&nbsp;No records!</h6>
{/if}

<style>
  div {
    max-height: 40%;
    overflow-y: scroll;
  }
  span {
    color: red;
    font-weight: bolder;
  }
  .freeze {
    bottom: 0;
    font-weight: bold;
  }
</style>
