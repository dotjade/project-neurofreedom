# Cloudflare deployment through GitHub Actions

Pushes to `main` validate the source and deploy the tested revision to the existing Cloudflare Worker. Pull requests validate without deploying or receiving Cloudflare credentials. Manual runs are available from Actions, on `main` only. Workflow: [GitHub Actions](https://github.com/dotjade/project-neurofreedom/actions/workflows/deploy-cloudflare.yml).

## Required repository Actions secrets

- `CLOUDFLARE_API_TOKEN`: a Cloudflare API token restricted to the existing account and appropriate zone, with Workers Scripts Edit and Zone Workers Routes Edit. Include Account Settings Read / Zone Read for account and route discovery by Wrangler. Cloudflare’s Edit Cloudflare Workers API-token template is a suitable starting point; restrict its account and zone resources. Existing Worker runtime secrets stay in Cloudflare; do not put them in this workflow.
- `CLOUDFLARE_ACCOUNT_ID`: the existing Cloudflare account ID, `db397fe15559d29b5980cfdf828feb1d`.

Set these under [Settings → Secrets and variables → Actions](https://github.com/dotjade/project-neurofreedom/settings/secrets/actions). Do not paste credentials into chat, commits, logs or issues. A secret already configured in another personal repository cannot be read back or automatically inherited here. The current GitHub integration cannot administer Actions secrets.

The workflow fails clearly if credentials are missing. Once configured, rerun the failed deployment job or use Run workflow. Confirm the deployment job and public-site check succeeded before reporting publication. A commit or green validation job alone does not establish deployment success.

## Scheduled cloud agents

Commit validated changes to `main` using the connected GitHub tools or CLI; Actions handles deployment without the PC or Cloudflare credentials in the agent workspace. Inspect the Actions run for that exact commit. If it fails, record the real error and leave deployment pending. Do not make a second direct Wrangler deployment while Actions is deploying.

Deployments are serialized. Database migrations, account/billing changes and new infrastructure are not run by this workflow. Apply separately reviewed migrations before deploying code that requires them. Check the existing Wrangler configuration before changing target names, bindings or routes.

The workflow runs from `public/journal-source/`. The build uses an explicit public-asset allowlist and the current `public/research-feed.json` as its saved fallback; research files and the disabled feedback service are excluded. Existing GET-only repository feed publication remains available. Feed and journal-source changes trigger the workflow; ordinary research notes do not. Shared voting stays disabled.
