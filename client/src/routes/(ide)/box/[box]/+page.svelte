<script>
    import { onMount } from "svelte";
    import { page } from "$app/stores";
    import config from "../../../../../../config.json";

    import Box from "$lib/Box.svelte";
    import Editor from "$lib/Editor.svelte";

    let boxKey = $page.params.box;
    let isConnected = false;
    let disabled = true;
    let boxName = "New Box";
    let boxCode = "";
    let theme = "dark";
    let notifBox;

    // set params
    onMount(async() => {
        // server ping
        try {
            await fetch(config.server);
            isConnected = true;
            // check
            if (boxKey == "new") {
                disabled = false;
            } else {
                disabled = true;
                const resp = await fetch(`${config.server}/get/${boxKey}`);
                const data = await resp.json();
                if(data.name) {
                    boxName = data.name;
                    boxCode = data.code;
                } else {
                    disabled = false;
                    history.pushState({}, "", "/box/new");
                    const notifMsg = new Box({
                        target: notifBox,
                        props: {
                            type: "error",
                            msg: "Box not found"
                        }
                    });
                    $page.params.box = "new";
                }
            }
        } catch (error) {
            isConnected == false;
        }
    });

    // download file
    function downloadFile(txt, filename) {
        var element = document.createElement("a");
        element.setAttribute("href", "data:text/plain;charset=utf-8," + encodeURIComponent(txt));
        element.setAttribute("download", `${filename}.txt`);
        element.style.display = "none";
        document.body.appendChild(element);
        element.click();
        document.body.removeChild(element);
    }

    // save box
    async function saveBox() {
        try {
            if(boxKey == "new") {
                const options = {
                    method: "POST",
                    headers: { "Content-Type": "application/json" },
                    body: JSON.stringify({ name: boxName, code: boxCode })
                };
                const resp = await fetch(`${config.server}/save`, options);
                const data = await resp.json();
                if (data.key != undefined || data.key != "") {
                    navigator.clipboard.writeText(`${$page.url.origin}/box/${data.key}`);
                } else {
                    const notifMsg = new Box({
                        target: notifBox,
                        props: {
                            type: "error",
                            msg: "Currently storage is full"
                        }
                    });
                }
            } else {
                navigator.clipboard.writeText($page.url.href);
            }
            const notifMsg = new Box({
                target: notifBox,
                props: {
                    type: "success",
                    msg: "Copied share link to clipboard"
                }
            });
        } catch (error) {
            const notifMsg = new Box({
                target: notifBox,
                props: {
                    type: "error",
                    msg: "Server is offline"
                }
            });
        }
    }

    // download box
    async function downloadBox() {
        try {
            if(boxKey == "new") {
                downloadFile(boxCode, boxName)
            } else {
                const resp = await fetch(`${config.server}/get/${boxKey}`);
                const data = await resp.json();
                downloadFile(data.code, data.name);
            }
            const notifMsg = new Box({
                target: notifBox,
                props: {
                    type: "success",
                    msg: "Download started"
                }
            });
        } catch (error) {
            const notifMsg = new Box({
                target: notifBox,
                props: {
                    type: "error",
                    msg: "Server is offline"
                }
            });
        }
    }

    // Add event listener for ctrl+s
    function handleKeyDown(event) {
        if (event.ctrlKey && event.key === 's') {
            event.preventDefault();
            downloadBox();
        }
    }

    onMount(() => {
        window.addEventListener('keydown', handleKeyDown);
        return () => {
            window.removeEventListener('keydown', handleKeyDown);
        };
    });

    // change theme
    function changeTheme() {
        let themes = ["dark", "light"];
        theme = themes[(themes.indexOf(theme) + 1) >= themes.length ? 0 : (themes.indexOf(theme) + 1)];
    }
</script>

{#if isConnected == null}
    <div class="h-screen flex items-center -mt-11">
        <div class="block mx-auto text-center">
            <img src="/bitbox.webp" class="h-32 animate-pulse" alt="Bit Box Logo" />
            <p class="mt-4">Loading Box...</p>
        </div>
    </div>
{:else if !isConnected}
    <div class="h-screen flex items-center md:-mt-11">
        <div class="block mx-auto text-center bg-orange-rust border-4 border-dashed border-orange-rust-lite rounded-xl p-4 md:w-3/4">
            <p class="text-gray-400">
            We're sorry, but it seems that the server for our <span class="text-orange-bright">Bit Box</span> is <span class="text-orange-bright">currently offline</span>. This means that you <span class="text-orange-bright">won't be able to code or share the box</span> until the server comes back online.
            We understand that this can be frustrating and we're working hard to get the server back up as soon as possible. We apologize for any inconvenience this may have caused you and we appreciate your patience while we work on resolving the issue.
            In the meantime, we recommend that you try accessing the <span class="text-orange-bright">Bit Box</span> again later. Once the server is back online, you should be able to resume your work without any issues.
            Thank you for using our <span class="text-orange-bright">Bit Box</span>, and we apologize again for the inconvenience.
            </p>
        </div>
    </div>
{:else}
    <!-- Top Navbar -->
    <nav class="bg-orange-rust sticky h-14 w-screen rounded-b-xl md:rounded-b-none inset-x-0 top-0 flex flex-row items-center align-middle justify-center md:justify-start pl-20">
        <div class="flex flex-row items-center py-2">
            <img src="/bitbox.webp" class="h-10 w-10" alt="Bit Box Logo" />
        </div>
        <input bind:value={boxName} class="bg-orange-rust focus:outline-none pl-4 w-48" {disabled} title="Box Name"/>
    </nav>

    <!-- Editor -->
    <Editor bind:code={boxCode} {theme} {disabled} />

    <!-- Bottom Navbar / Sidebar -->
    <nav class="bg-orange-rust h-14 md:h-full w-full md:w-14 py-4 px-11 md:px-4 md:pt-16 space-x-8 md:space-x-0 fixed flex md:flex-col items-center justify-between md:justify-start inset-x-0 md:inset-y-0 bottom-0 md:left-0 rounded-t-xl md:rounded-t-none">
        <a href="/" title="Close Editor">
            <button class="fill-gray-200 hover:fill-orange-bright py-4">
                <svg class="h-6 w-auto" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16">
                    <path d="M2.146 2.854a.5.5 0 1 1 .708-.708L8 7.293l5.146-5.147a.5.5 0 0 1 .708.708L8.707 8l5.147 5.146a.5.5 0 0 1-.708.708L8 8.707l-5.146 5.147a.5.5 0 0 1-.708-.708L7.293 8 2.146 2.854Z"/>
                </svg>
            </button>
        </a>
        <button on:click={changeTheme} class="fill-gray-200 hover:fill-orange-bright py-4" title="Change Theme">
            <svg class="h-6 w-auto" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16">
                <path d="M8 5a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3zm4 3a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3zM5.5 7a1.5 1.5 0 1 1-3 0 1.5 1.5 0 0 1 3 0zm.5 6a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3z"/>
                <path d="M16 8c0 3.15-1.866 2.585-3.567 2.07C11.42 9.763 10.465 9.473 10 10c-.603.683-.475 1.819-.351 2.92C9.826 14.495 9.996 16 8 16a8 8 0 1 1 8-8zm-8 7c.611 0 .654-.171.655-.176.078-.146.124-.464.07-1.119-.014-.168-.037-.37-.061-.591-.052-.464-.112-1.005-.118-1.462-.01-.707.083-1.61.704-2.314.369-.417.845-.578 1.272-.618.404-.038.812.026 1.16.104.343.077.702.186 1.025.284l.028.008c.346.105.658.199.953.266.653.148.904.083.991.024C14.717 9.38 15 9.161 15 8a7 7 0 1 0-7 7z"/>
            </svg>
        </button>
        <button on:click={saveBox} class="fill-gray-200 hover:fill-orange-bright py-4" title="Save Box">
            <svg class="h-6 w-auto" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16">
                <path d="M13.5 1a1.5 1.5 0 1 0 0 3 1.5 1.5 0 0 0 0-3zM11 2.5a2.5 2.5 0 1 1 .603 1.628l-6.718 3.12a2.499 2.499 0 0 1 0 1.504l6.718 3.12a2.5 2.5 0 1 1-.488.876l-6.718-3.12a2.5 2.5 0 1 1 0-3.256l6.718-3.12A2.5 2.5 0 0 1 11 2.5zm-8.5 4a1.5 1.5 0 1 0 0 3 1.5 1.5 0 0 0 0-3zm11 5.5a1.5 1.5 0 1 0 0 3 1.5 1.5 0 0 0 0-3z"/>
            </svg>
        </button>
        <button on:click={downloadBox} class="fill-gray-200 hover:fill-orange-bright py-4" title="Download Box">
            <svg class="h-6 w-auto"  xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16">
                <path d="M4.406 1.342A5.53 5.53 0 0 1 8 0c2.69 0 4.923 2 5.166 4.579C14.758 4.804 16 6.137 16 7.773 16 9.569 14.502 11 12.687 11H10a.5.5 0 0 1 0-1h2.688C13.979 10 15 8.988 15 7.773c0-1.216-1.02-2.228-2.313-2.228h-.5v-.5C12.188 2.825 10.328 1 8 1a4.53 4.53 0 0 0-2.941 1.1c-.757.652-1.153 1.438-1.153 2.055v.448l-.445.049C2.064 4.805 1 5.952 1 7.318 1 8.785 2.23 10 3.781 10H6a.5.5 0 0 1 0 1H3.781C1.708 11 0 9.366 0 7.318c0-1.763 1.266-3.223 2.942-3.593.143-.863.698-1.723 1.464-2.383z"/>
                <path d="M7.646 15.854a.5.5 0 0 0 .708 0l3-3a.5.5 0 0 0-.708-.708L8.5 14.293V5.5a.5.5 0 0 0-1 0v8.793l-2.146-2.147a.5.5 0 0 0-.708.708l3 3z"/>
            </svg>
        </button>
    </nav>

    <!-- Notification -->
    <div bind:this={notifBox} class="flex flex-col h-auto w-full md:w-64 bottom-0 right-0 absolute mb-5 overflow-hidden"></div>
{/if}
