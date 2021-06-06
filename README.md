# Personal Site powered by Jekyll 

I forked the theme from dark-poole with the goal of hosting a "simple" site that I can publish to and write using markdown files and hopefully as little fuss as possible. 

To serve locally use:
```bash
bundle exec jekyll serve
```

## Github Actions
On every change to the main branch the Github action should 🤞 run to deploy the latest version of the site to the `gh-pages` branch.

---

## Contents

- [Usage](#usage)
- [Development](#development)
- [Author](#author)
- [License](#license)

## Usage

### 0. Environment

* Install Homebrew
* Install `chruby`
* Install `ruby-install`
  * I've been using Ruby 2.7.3
* Use chruby for managing the local version of Ruby

### 1. Install dependencies

Poole is built on Jekyll and uses its built-in SCSS compiler to generate our CSS. Before getting started, you'll need to install the Jekyll gem and related dependencies:

```bash
$ gem install jekyll jekyll-gist jekyll-sitemap jekyll-seo-tag
```

### 2. Install bundler

You must have bundler installed. If you already have bundler installed, skip this step.

```bash
# Update Rubygems
$ gem update --system
# Update bundler
$ gem install bundler
```

Now install the bundle:

```bash
$ bundle install
```

### 3. Running locally

To see your Jekyll site with Poole applied, start a Jekyll server. In Terminal, from `/dark-poole` (or whatever your Jekyll site's root directory is named):

```bash
$ bundle exec jekyll serve
```

Open <http://localhost:4000> in your browser, and voilà.

### 4. Serving it up

You can use [GitHub Pages](https://pages.github.com) to host your project.

1. Fork this repo and switch to the `gh-pages` branch.
1. If you're [using a custom domain name](https://help.github.com/articles/setting-up-a-custom-domain-with-github-pages), modify the `CNAME` file to point to your new domain.
1. If you're not using a custom domain name, **modify the `url` in `_config.yml`** to point to your GitHub Pages URL. Example: for a site hosted at `username.github.io`, use `http://username.github.io`.
1. If you want to use your repo name as a base url, **set the `url`** to your repo link and **set the `baseurl`** to your repo name in **`_config.yml`**. Example: for site hosted on `https://username.github.io/dark-poole`, set `url` as `https://username.github.io/dark-poole` and `baseurl` as `/dark-poole`.
1. Done! Head to your GitHub Pages URL or custom domain.

No matter your production or hosting setup, be sure to verify the `baseurl` option file and `CNAME` settings. Not applying this correctly can mean broken styles on your site.

### 5. Pagination for sites with base urls

If you are using a base url for your site, (for example, hosted on `https://username.github.io/dark-poole`) you have to make some changes to get jekyll-pagination to work correctly:

In `_config.yml`, add this line:

```yaml
paginate_path: "/baseurl/page:num/"
```

In `archive.md`, add `{{ site.baseurl }}` before `{{ post.url }}`

```html
<!-- Add "{{ site.baseurl }}" -->
<li><a href="{{ site.baseurl }}{{ post.url }}">{{ post.title }}</a></li>
```

In `index.html`, remove the `prepend:`:

```html
<!-- Remove "prepend:" in "prepend: relative_url" -->
<a
  class="pagination-item newer"
  href="{{ paginator.previous_page_path | relative_url }}"
  >Newer</a
>
```

## Development

CSS is handled via Jeykll's built-in Sass compiler. Source Sass files are located in `_sass/`, included into `styles.scss`, and compile to `styles.css`.

### Customize Navbar

You can easily customize the navbar by tweaking the `_config.yml` file. Simply change the title and url of each of the nav elements, or add more. The order will be preserved in the site.

```yaml
nav:
  - title: Blog
    url: /posts

  - title: About
    url: /about
```

## Quotebacks

I love the intent behind [Quoteback](https://quotebacks.net) and my goal is to use them whenever I cite someone else. 

## Oops!

Something broke again. Did I / you / me remember to:

### Ruby version
Did you set the [version of ruby](https://stackoverflow.com/a/54873916/5499522) using `chruby`?

```bash
chruby 2.7.2
```

### M1 Processor
Did you try to install Ruby on an M1 iMac and read through several blog posts? Read this and update `ffi` https://www.moncefbelyamani.com/how-to-install-homebrew-and-ruby-on-a-mac-with-the-m1-apple-silicon-chip/

## License

Open sourced under the [MIT license](LICENSE.md).

<3
