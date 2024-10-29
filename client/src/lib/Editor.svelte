<script>
    export let code, theme, disabled;

    let themeColor = "";
    let lineNumbersDiv;

    $: {
        if(theme == "dark") {
            themeColor = "bg-orange-rust text-white";
        } else if(theme == "light") {
            themeColor = "bg-white text-orange-rust";
        }
    }

    function handleScroll(event) {
        lineNumbersDiv.scrollTop = event.target.scrollTop;
    }
</script>

<div class="h-[90.2vh] w-screen pt-8 pb-[68px] md:pb-[0.1px] pl-[35px] md:pl-[95px] pr-[35px]">
    <div class="relative h-full w-full">
        <div class="relative h-full w-full overflow-hidden {themeColor} rounded-md top-0 left-0 flex flex-row-reverse gap-x-2 p-5">
            <textarea bind:value={code} class="text-[20px] bg-transparent focus:outline-none font-mono h-full w-full resize-none overflow-auto text-nowrap" {disabled} on:scroll={handleScroll} />
            <div class="h-full pointer-events-none overflow-hidden" bind:this={lineNumbersDiv} style="width: {`${String(code.split("\n").length).length + 1}ch`}">
                <div class="h-full w-full">
                    {#each code.split("\n") as _, i}
                        <p class="text-left text-gray-500 overflow-hidden">{i + 1}</p>
                    {/each}
                </div>
            </div>
        </div>
    </div>
</div>
