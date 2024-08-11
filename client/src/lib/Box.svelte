<script>
    import { onMount } from "svelte";

    export let type;
    export let msg;

    let div;

    setTimeout(() => {
        if (div) {
            div.remove();
        }
    }, 5000);
</script>

<div bind:this={div} class="{type == "success" ? "bg-green-800" : "bg-red-800"} m-2 p-4 rounded-md text-sm overflow-hidden">
    {msg}
</div>