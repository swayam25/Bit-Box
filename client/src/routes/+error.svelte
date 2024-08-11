<script>
    import { page } from "$app/stores";
</script>

<!-- Error -->
<div class="mt-[50%] md:mt-[20%] text-center space-y-2">
    <h1 class="text-orange-bright font-bold text-4xl md:text-5xl font-mono">{$page.status}</h1>
    <p class="text-grey-200 text-2xl">{$page.error.message}</p>
    <br>
    <a href="/">
        <button class="text-orange-bright rounded-xl px-16 py-4 bg-orange-rust hover:bg-orange-rust-lite duration-500">Return Home</button>
    </a>
</div>