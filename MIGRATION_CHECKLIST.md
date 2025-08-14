# Repo Rename & Migration Checklist (A10WIRE → corepath-a10)

This guide keeps your links working and your local clone clean.

## 1) Rename the GitHub repo
- Open the GitHub repo settings for `cdracars/A10WIRE`
- Change the name to **`corepath-a10`**
- GitHub auto-creates HTTP redirects for old links, but you should still update references below.

## 2) Update your local git remote
```bash
# from an existing clone that still points to A10WIRE
git remote -v
git remote set-url origin git@github.com:cdracars/corepath-a10.git
# or HTTPS
git remote set-url origin https://github.com/cdracars/corepath-a10.git
```

## 3) Update internal references
Search/replace in the repo:
- `A10WIRE` → `CorePath – A10 Build` (or `CorePath-A10` where a filename/slug is required)
- `a10wire/` paths → `corepath-a10/`
- Badges, shields, and CI references (if used): repository name and URLs

Common places:
- `README.md`
- `docs/*.md`
- Any GitHub Actions badges or workflow names
- Issue templates / PR templates (if repo name appears)

## 4) Repo settings sanity check
- **Branches & protection rules:** still point to `corepath-a10`
- **Actions/Workflows:** still run under the new name
- **Pages (if any):** update the publish source and custom domain/CNAME references
- **Environments/Secrets:** remain intact but review names that include the old repo

## 5) External links you control
- Update links in Discord pins, forum posts, and any project pages that you can edit.
- If you have package metadata (e.g., `package.json`, `pyproject.toml`) with repo fields, update them.

## 6) Local housekeeping
```bash
# optional: clean old branches or tags that used A10WIRE naming
git fetch --all --prune
```

## 7) Verify redirects
- Visit an old `A10WIRE` link; ensure it redirects to `corepath-a10`
- Click badges inside README to ensure no 404s
