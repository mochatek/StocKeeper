<script>
  import { createEventDispatcher } from "svelte";

  let current = "Purchase";
  const dispatch = createEventDispatcher();

  $: changeTab(current);

  function changeTab() {
    dispatch("change", { tab: current });
  }
</script>

<nav>
  <li
    on:click={() => (current = "Purchase")}
    class={current === "Purchase" ? "active" : ""}
  >
    <i class="fas fa-box-open" /><span>Purchases</span>
  </li>
  <li
    on:click={() => (current = "Sale")}
    class={current === "Sale" ? "active" : ""}
  >
    <i class="fas fa-shopping-cart" /><span>Sales</span>
  </li>
</nav>

<style>
  nav {
    display: flex;
    flex-direction: column;
    align-items: center;
    background: var(--primary);
    color: white;
    width: 8%;
  }
  li {
    display: flex;
    flex-direction: column;
    align-items: center;
    cursor: pointer;
    width: 100%;
    padding: 1.5rem 0rem;
    font-size: small;
  }
  i {
    font-size: 30px;
  }
  li:hover {
    background: var(--secondary);
  }
  .active {
    background: var(--secondary);
    border: 1px solid white;
  }
</style>
