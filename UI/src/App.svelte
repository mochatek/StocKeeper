<script>
  import Header from "./components/Header.svelte";
  import Sidebar from "./components/Sidebar.svelte";
  import Purchase from "./components/Purchase.svelte";
  import Sale from "./components/Sale.svelte";

  const router = { Purchase, Sale };
  let page = "Purchase";
</script>

<svelte:head>
  <link
    rel="stylesheet"
    href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css"
  />
</svelte:head>

<Header />
<main>
  <Sidebar on:change={({ detail: { tab } }) => (page = tab)} />
  <div>
    <svelte:component this={router[page]} />
  </div>
</main>

<style>
  main {
    display: flex;
    height: 88vh;
  }
  div {
    background: var(--bg);
    padding: 1rem;
    width: 92%;
  }
</style>
