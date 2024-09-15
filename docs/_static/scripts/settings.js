
function setRootTheme(mode) {
    document.documentElement.setAttribute("data-theme", mode)
}


function cycleThemeOnce() {
    const currentTheme = localStorage.getItem("theme") || "auto"
    const prefersDark = window.matchMedia("(prefers-color-scheme: dark)").matches

    if (prefersDark) {
        // Auto (dark) -> Light -> Dark
        if (currentTheme === "auto") {
            setRootTheme("light")
        } else {
            setRootTheme("dark")
        }
    } else {
        // Auto (light) -> Dark -> Light
        if (currentTheme === "auto") {
            setRootTheme("dark")
        } else {
            setRootTheme("light")
        }
    }
}


function setupRootTheme() {
    const currentTheme = localStorage.getItem("theme") || "auto"
    const prefersDark = window.matchMedia("(prefers-color-scheme: dark)").matches

    if (currentTheme === "auto") {
        if (prefersDark) {
            setRootTheme("dark")
        }
        else {
            setRootTheme("light")
        }
    }
    else {
        setRootTheme(currentTheme)
    }
}


function insertAttributetables() {
    const tables = document.querySelectorAll(".py-attribute-table[data-move-to-id]")

    tables.forEach(table => {
        let element = document.getElementById(table.getAttribute("data-move-to-id"))
        element.parentNode.insertBefore(table, element.nextSibling)
    })
}


function editSigParenStyle() {
    let elems = document.getElementsByClassName("sig-paren")
    for (let elem of elems) {
        if (elem.textContent === "(") {
            elem.classList.add("sig-paren-open")
        }
        else if (elem.textContent === ")") {
            elem.classList.add("sig-paren-close")
        }
    }
}


function replaceAsyncWithAwait() {
    let elems = document.getElementsByClassName("pre")
    for (let elem of elems) {
        if (elem.textContent === "async") {
            elem.textContent = "await"
        }
    }
}


function removeParent(parent) {
    // recursively remove parent
    let parentParent = parent.parentNode
    parentParent.remove(parent)

    if (parentParent.childElementCount == 0) {
        removeParent(parentParent)
    }
}

function adjustAPIReferenceToc() {
    let tocTree = document.getElementsByClassName("toc-tree")[0]
    let codeElements = tocTree.getElementsByTagName("code")

    let parents = []
    for (let codeElem of codeElements) {
        parents.push(codeElem.parentNode)
    }

    for (let parent of parents) {
        for (let child of parent.childNodes) {
            parent.removeChild(child)
            // clean up empty parent elements (li, ul)
            removeParent(parent)
        }
    }

    let tocTitle = document.getElementsByClassName("toc-title")[0]
    tocTitle.textContent = ""
    let tocTitleAnchor = document.createElement("a")
    tocTitleAnchor.textContent = "API Reference"
    tocTitleAnchor.href = "#api-reference"
    tocTitle.appendChild(tocTitleAnchor)

    let liElemensRemaining = tocTree.getElementsByTagName("li")
    for (let li of liElemensRemaining) {
        if (li.childElementCount === 1) {
            li.classList.add("toc-tree-list")
        }
        else {
            li.children[0].classList.add("toc-tree-list-title")
        }
    }

}

function adjustChangelogToc() {
    let tocTree = document.getElementsByClassName("toc-tree")[0]
    let refElements = tocTree.getElementsByClassName("reference")

    let parents = []
    for (let refElem of refElements) {
        if (["New Features", "Bug Fixes", "Misc"].includes(refElem.textContent)) {
            parents.push(refElem.parentNode)
        }
    }

    for (let parent of parents) {
        for (let child of parent.childNodes) {
            parent.removeChild(child)
            // clean up empty parent elements (li, ul)
            removeParent(parent)
        }
    }
}

themeToggles = document.getElementsByClassName("theme-toggle")
for (let elem of themeToggles) {
    elem.addEventListener("click", cycleThemeOnce)
}

document.addEventListener("DOMContentLoaded", () => {
    let path = window.location.pathname
    let page = path.split("/").pop()
    if (page === "api.html") {
        insertAttributetables()
        editSigParenStyle()
        replaceAsyncWithAwait()
        adjustAPIReferenceToc()
    }
    else if (page === "changelog.html") {
        adjustChangelogToc()
    }

    setupRootTheme()
})
