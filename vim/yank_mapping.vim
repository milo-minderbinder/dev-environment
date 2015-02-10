" Remaps yank line (yy) for NERDTree window to copy full path of node into the
" default register
" To install: copy into .vim/bundle/The-NERD-tree/nerdtree_plugin

call NERDTreeAddKeyMap({
        \ 'key': 'yy',
        \ 'callback': 'NERDTreeYankCurrentNode',
        \ 'quickhelpText': 'put full path of current node into the default register' })

function! NERDTreeYankCurrentNode()
    let n = g:NERDTreeFileNode.GetSelected()
    if n != {}
        call setreg('"', n.path.str())
    endif
endfunction
