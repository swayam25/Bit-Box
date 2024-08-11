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

<div class="remove-body-margin h-[90.2vh] w-screen pt-8 pb-[68px] md:pb-[0.1px] pl-[35px] md:pl-[95px] pr-[35px]">
    <textarea bind:value={code} class="{themeColor} text-[20px] pl-2 focus:outline-none font-mono h-full w-full rounded-md resize-none" {disabled} />
</div>
