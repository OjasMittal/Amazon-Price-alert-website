mkdir -p ~/.streamlit/
echo "
[theme]
primaryColor='#b11212'
backgroundColor='#171818'
secondaryBackgroundColor='#f9ca06'
textColor='#eff7f7'
[server]\n\
headless = true\n\
port = $PORT\n\
enableCORS = false\n\
\n\
" > ~/.streamlit/config.toml
