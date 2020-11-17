" == General Congiguartion ==
set nocompatible                    " Disable vi compatibility

set number                          " Always show line numbers
set backspace=indent,eol,start      " Allow backspace in insert mode
set showmode                        " Always show the mode

syntax on                           " Enable syntax highlighting

if has("autocmd")                   " Open at the same place we left off
  au BufReadPost * if line("'\"") > 0 && line("'\"") <= line("$") | exe "normal! g`\"" | endif
endif

" ======== Indentation =======
set autoindent                      " Copy indenation from previous line
"set smartindent                     " Automatically inserts one extra indentation in special cases
set shiftwidth=4                    " Set the number of spaces when using >> or <<
set tabstop=4                       " Set the width of TAB to 4
set expandtab                       " TABs are spaces
set softtabstop=4                   " Backspace deltes entire TABs
set nowrap                          " Don't wrap lines

" ========== Search ==========
set incsearch                       " Find the next match as we type
set hlsearch                        " Highlight searches by default
set ignorecase                      " Ignore case while searching...
set smartcase                       " ... unless we type a captial
