<script>
  import { onMount, onDestroy, createEventDispatcher } from "svelte";
  import { insertItem } from "../utils/Api";
  import { itemStore } from "../utils/Store";

  let item = "";
  let items = [];
  const dispatch = createEventDispatcher();

  onMount(async () => {
    itemStore.subscribe((value) => {
      items = value;
    });

    document.addEventListener("keyup", closeHandler);
  });

  onDestroy(() => {
    document.removeEventListener("keyup", closeHandler);
  });

  function closeHandler({ key }) {
    if (key === "Escape") dispatch("close");
  }

  async function addItem() {
    if (
      item &&
      !items.map((i) => i.toLowerCase()).includes(item.toLowerCase())
    ) {
      if (await insertItem(item)) {
        itemStore.update((value) => [item, ...value]);
        item = "";
      }
    }
  }
</script>

<div class="container">
  <article>
    <h4>
      New Item<span on:click={() => dispatch("close")}>&#10006;</span>
    </h4>
    <div>
      <form on:submit|preventDefault={addItem}>
        <input type="text" placeholder="Item name" required bind:value={item} />
        <button type="submit"
          ><i class="fas fa-plus-square" />&nbsp;&nbsp;Add</button
        >
      </form>
      <ul>
        {#each items as i}
          <li>{i}</li>
        {/each}
      </ul>
    </div>
  </article>
</div>

<style>
  .container {
    top: 0;
    left: 0;
    position: absolute;
    width: 100%;
    height: 100%;
    background: rgba(0, 0, 0, 0.25);
    z-index: 1;
    display: flex;
  }
  article {
    width: auto;
    margin: auto;
    border-radius: 4px;
    background: var(--bg);
    box-shadow: 1px 1px 20px 2px grey;
    /* max-height: 85%;
    overflow-y: scroll; */
  }
  h4 {
    background: var(--primary);
    color: white;
    margin: 0;
    padding: 1rem;
  }
  span {
    float: right;
    color: red;
    cursor: pointer;
  }
  ul {
    list-style: none;
    padding: 0;
    margin-bottom: 1rem;
    display: grid;
    grid-template-columns: 1fr 1fr;
  }
  li {
    padding: 0.5rem;
    margin: 0.25rem 0.5rem;
    color: var(--heading);
    width: 81%;
    background: white;
    border-radius: 4px;
    border: 1px solid lightgrey;
    border-left: 5px solid lightgrey;
    text-indent: 0.5rem;
  }
  form {
    padding: 0.5rem;
    display: flex;
  }
  input {
    margin-left: 0;
    width: 80%;
  }
  button {
    color: white;
    background: rgb(172, 170, 170);
    font-weight: bold;
  }
  button:hover {
    background: grey;
  }
</style>
