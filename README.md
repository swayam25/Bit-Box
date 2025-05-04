<div align="center">

![Bit Box](./assets/bitbox.png)

Elevate your coding skills with Bit Box

</div>

> [!IMPORTANT]
> This project is outdated and no longer maintained. Dependencies may be broken and the code may not work as expected.

## 🎬️ Preview

- **Main Page**

    ![Main Page](./assets/main.png)

- **Share Box**

    ![Share Box](./assets/share.gif)

## 🚀 Installation

1. Clone this repository
    ```sh
    git clone https://github.com/swayam25/Bit-Box bit_box
    cd bit_box
    ```

2. Configure the [`config.json`](./config.json) file

   <details>

    <summary>Configuration</summary>

    - `server`: Backend server url

    - `donateURL`: Donation url

    </details>

3. For backend
   - Install dependencies
        ```sh
        cd server
        python -m venv .venv
        source .venv/bin/activate
        pip install -r requirements.txt
        ```
   - Start the server
        ```sh
        fastapi dev --port 2501
        ```

4. For frontend
   - Install dependencies
        ```sh
        cd client
        npm i
        ```
   - Start the client
        ```sh
        npm run dev -- --port 2500
        ```

## 🌐 Production

1. Follow steps 1 & 2 from the [installation guide](#-installation). *Ignore if already done.*

2. For backend
   - Install dependencies (*Ignore if already done*)
   - Start the server
        ```sh
        fastapi run --port 2501
        ```

3. For frontend
    - Install dependencies (*Ignore if already done*)
    - Build the client
        ```sh
        npm run build
        ```
    - Preview the client
        ```sh
        npm run preview -- --port 2500
        ```

> [!TIP]
> Checkout the [deployment guide](https://svelte.dev/docs/kit/adapter-node) for more information.
