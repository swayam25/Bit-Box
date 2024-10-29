<script>
    export let code, theme, disabled;

    let themeColor = "";

    $: {
        if(theme == "dark") {
            themeColor = "bg-orange-rust text-white";
        } else if(theme == "light") {
            themeColor = "bg-white text-orange-rust";
        }
    }
</script>

<div class="h-[90.2vh] w-screen pt-8 pb-[68px] md:pb-[0.1px] pl-[35px] md:pl-[95px] pr-[35px]">
    <div class="relative h-full w-full">
        <textarea bind:value={code} class="{themeColor} text-[20px] pl-8 focus:outline-none font-mono h-full w-full rounded-md resize-none absolute top-0 left-0" {disabled} />
        <div class="absolute top-0 left-0 h-full w-full pointer-events-none">
            {#each code.split("\n") as _, i}
                <div class="text-left px-2 text-gray-500">{i + 1}</div>
            {/each}
        </div>
    </div>
</div>
