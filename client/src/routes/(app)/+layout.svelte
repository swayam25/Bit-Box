<script>
    import config from "../../../../config.json";

    // Navbar button
    let isHidden = true;
    let navCls = "hidden";
    function onNavBtn() {
        isHidden = !isHidden;
        if(isHidden) {
            navCls = "hidden";
        } else {
            navCls = "justify-center items-center"
        }
    }
</script>

<!-- Navbar -->
<nav class="py-1 sticky remove-body-margin inset-x-0 z-50 top-0 bg-cover bg-orange-dark bg-opacity-80 rounded-b-xl {isHidden ? '' : 'h-32'} md:h-auto">
    <div class="container flex flex-wrap items-center justify-between justify mx-auto">
        <a href="/" class="flex items-center pt-2 mx-5 md:-mx-5">
            <img src="/bitbox.webp" class="h-14 w-14 antialised rounded-md" alt="Bit Box Logo" />
        </a>
        <button on:click={onNavBtn} class="mx-5 md:-mx-5 inline-flex items-center rounded-lg md:hidden">
            <svg class="h-6 w-6 fill-white hover:fill-orange-bright" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16">
                <path d="M9.5 13a1.5 1.5 0 1 1-3 0 1.5 1.5 0 0 1 3 0zm0-5a1.5 1.5 0 1 1-3 0 1.5 1.5 0 0 1 3 0zm0-5a1.5 1.5 0 1 1-3 0 1.5 1.5 0 0 1 3 0z"/>
            </svg>
        </button>
        <div class="{navCls} md:block w-full md:w-auto text-base">
            <ul class="flex absolute space-x-4 md:relative rounded-md md:flex-row justify-evenly w-full">
                <a href={config.donateURL} class="px-3 py-2 rounded-md text-md font-medium hover:text-orange-bright">Donate</a>
                <a href="/#features" class="px-3 py-2 rounded-md text-md font-medium hover:text-orange-bright">Features</a>
                <a href="/box/new" class="px-3 py-2 rounded-md text-md font-medium bg-orange-rust hover:bg-orange-rust-lite flex items-center duration-300 pr-4">
                    <svg class="h-6 md:h-7 pr-2" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16">
                        <path fill-rule="evenodd" d="M8 2a.5.5 0 0 1 .5.5v5h5a.5.5 0 0 1 0 1h-5v5a.5.5 0 0 1-1 0v-5h-5a.5.5 0 0 1 0-1h5v-5A.5.5 0 0 1 8 2Z"/>
                    </svg>
                    Create Box
                </a>
            </ul>
        </div>
    </div>
</nav>

<slot />