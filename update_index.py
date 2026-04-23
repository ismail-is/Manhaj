import sys

with open("index.html", "r", encoding="utf-8") as f:
    lines = f.readlines()

new_lines = []
for i, line in enumerate(lines):
    if i == 11:
        new_lines.append('  <link href="assets/css/bootstrap.css" rel="stylesheet">\n')
        new_lines.append('  <link href="assets/css/style.css" rel="stylesheet">\n')
        new_lines.append('  <link href="assets/css/responsive.css" rel="stylesheet">\n')
        new_lines.append('  <link href="https://fonts.googleapis.com/css2?family=Lexend:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet">\n')
        new_lines.append(line) # styles.css
    elif i == 14:
        new_lines.append('<body>\n<div class="page-wrapper">\n\t<div class="preloader"></div>\n')
    elif 15 <= i <= 163:
        pass # Skip original nav and hero
    elif i == 164:
        # Add our new header and hero
        new_html = r'''
	<!-- Main Header / Style Five -->
	<header class="main-header header-style-five">
		<!-- Header Top -->
		<div class="header-top style-two">
			<div class="auto-container">
				<div class="inner-container">
					<div class="d-flex justify-content-between align-items-center flex-wrap">
						<div class="left-box d-flex align-items-center flex-wrap">
							<ul class="header-top_list">
								<li><span class="icon fa-solid fa-envelope fa-fw"></span>info@manhajalambiya.org</li>
								<li><span class="icon fa-solid fa-location-dot fa-fw"></span>Mangaluru, Karnataka, India</li>
							</ul>
						</div>
						<ul class="header-top_list-two">
                            <li><span>The Methodology of Ahlu Sunnah wal Jama'ah</span></li>
							<li><span class="icon fa-solid fa-phone fa-fw"></span>Contact Us +91 XXXXXXXXXX</li>
						</ul>
					</div>
				</div>
			</div>
		</div>
		
		<!-- Header Upper -->
		<div class="header-upper">
			<div class="auto-container">
				<div class="inner-container">
					<div class="d-flex justify-content-between align-items-center flex-wrap">
						
						<div class="logo-box">
							<div class="logo"><a href="index.html"><img src="logo.png" alt="Manhaj Al Ambiya Logo" style="height:48px;"></a></div>
						</div>
						
						<div class="nav-outer">
							<!-- Main Menu -->
							<nav class="main-menu navbar-expand-md">
								<div class="navbar-header">
									<!-- Toggle Button -->    	
									<button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
										<span class="icon-bar"></span>
										<span class="icon-bar"></span>
										<span class="icon-bar"></span>
									</button>
								</div>
								
								<div class="navbar-collapse collapse clearfix" id="navbarSupportedContent">
									<ul class="navigation clearfix">
										<li class="active"><a href="index.html">Home</a></li>
										<li><a href="about.html">About Us</a></li>
										<li class="dropdown"><a href="education.html">Education</a>
											<ul>
                                                <li><a href="education.html#arabic-academy">Arabic Academy</a></li>
                                                <li><a href="education.html#quran-tajweed">Quran Tajweed & Hifz</a></li>
                                                <li><a href="education.html#madrasah">Madrasah & Islamic Studies</a></li>
                                                <li><a href="education.html#teen-series">Teen Series</a></li>
                                                <li><a href="education.html#pre-school">Islamic Pre School</a></li>
											</ul>
										</li>
										<li class="dropdown"><a href="dawa.html">Da'wah</a>
											<ul>
                                                <li><a href="dawa.html#tasfiyah">Tasfiyah & Tarbiyah</a></li>
                                                <li><a href="dawa.html#workshops">Islamic Workshops</a></li>
                                                <li><a href="dawa.html#library">Multi Language Library</a></li>
                                                <li><a href="dawa.html#studio">Islamic Studio</a></li>
                                                <li><a href="dawa.html#radio">Online Islamic Radio</a></li>
											</ul>
										</li>
										<li class="dropdown"><a href="publications.html">Publications</a>
											<ul>
                                                <li><a href="publications.html#quran-printing">Quran Printing Project</a></li>
                                                <li><a href="publications.html#books">Kannada Islamic Books</a></li>
                                                <li><a href="publications.html#pamphlets-muslims">Pamphlets for Muslims</a></li>
                                                <li><a href="publications.html#pamphlets-nonmuslims">Pamphlets for Non-Muslims</a></li>
											</ul>
										</li>
										<li><a href="social-service.html">Social Service</a></li>
										<li><a href="blog.html">Blog</a></li>
										<li><a href="contact.html">Contact</a></li>
									</ul>
								</div>
							</nav>
						</div>
						
						<div class="outer-box d-flex align-items-center flex-wrap">
							<div class="header_button-box">
								<a href="#donation" class="theme-btn btn-style-five">
									<span class="btn-wrap">
										<span class="text-one">Donate Now</span>
										<span class="text-two">Donate Now</span>
									</span>
								</a>
							</div>
							<!-- Mobile Navigation Toggler -->
							<div class="mobile-nav-toggler"><span class="icon flaticon-menu"></span></div>
						</div>

					</div>
				</div>
			</div>
		</div>
		
		<!-- Mobile Menu  -->
		<div class="mobile-menu">
			<div class="menu-backdrop"></div>
			<div class="close-btn"><span class="icon flaticon-close-1"></span></div>
			
			<nav class="menu-box">
				<div class="nav-logo"><a href="index.html"><img src="logo.png" alt="Manhaj Al Ambiya Logo" style="height:48px;"></a></div>
				<div class="menu-outer"><!--Here Menu Will Come Automatically Via Javascript / Same Menu as in Header--></div>
			</nav>
		</div>
	</header>
	<!-- End Header Five -->

	<!-- Slider Four -->
	<section class="slider-five">
		<div class="slider-five_bg" style="background-image:url(assets/main-img/main-slider/8.jpg)"></div>
		<div class="slider-five_circle" style="background-image:url(assets/main-img/main-slider/vector-4.png)"></div>
		<div class="main-slider_two swiper-container">
			<div class="swiper-wrapper">

				<!-- Slide -->
				<div class="swiper-slide">
					<div class="auto-container">
						<div class="row clearfix">
							<!-- Content Column -->
							<div class="slider-five_content col-xl-8 col-lg-12 col-md-12 col-sm-12">
								<div class="slider-five_content-inner">
									<div class="slider-five_vector-1" style="background-image:url(assets/main-img/main-slider/vector-5.png)"></div>
									<div class="slider-five_vector-2" style="background-image:url(assets/main-img/main-slider/vector-6.png)"></div>
									<div class="slider-five_vector-4" style="background-image:url(assets/main-img/main-slider/vector-7.png)"></div>
									<div class="slider-five_title" style="font-family: var(--font-arabic); direction: rtl; font-size: 1.5rem; letter-spacing: 0;">منهج الأنبياء للدعوة والإرشاد</div>
									<h1 class="slider-five_heading">Guiding the Community Through Knowledge & Da'wah</h1>
									<div class="slider-five_text" style="font-weight: 500;">Manhaj-Al-Ambiya, Mangaluru — Non-Profit Islamic Education & Da'wah Trust</div>
									<div class="slider-five_button mt-4">
										<a href="education.html" class="theme-btn btn-style-five">
											<span class="btn-wrap">
												<span class="text-one">Explore Programs</span>
												<span class="text-two">Explore Programs</span>
											</span>
										</a>
										<a href="about.html" class="theme-btn btn-style-six" style="margin-left: 15px;">
											<span class="btn-wrap">
												<span class="text-one">About Us</span>
												<span class="text-two">About Us</span>
											</span>
										</a>
									</div>
								</div>
							</div>

							<!-- Images Column -->
							<div class="slider-five_images-column col-xl-4 col-lg-12 col-md-12 col-sm-12">
								<div class="slider-five_images-outer">
									<div class="slider-five_vector" style="background-image:url(assets/main-img/main-slider/vector-3.png)"></div>
									<div class="slider-five_vector-3" style="background-image:url(assets/main-img/main-slider/vector-6.png)"></div>
									<div class="image">
										<img src="assets/main-img/main-slider/image-6.png" alt=""/>
									</div>
								</div>
							</div>
						</div>
					</div>
				</div>

				<!-- Slide -->
				<div class="swiper-slide">
					<div class="auto-container">
						<div class="row clearfix">
							<!-- Content Column -->
							<div class="slider-five_content col-xl-8 col-lg-12 col-md-12 col-sm-12">
								<div class="slider-five_content-inner">
									<div class="slider-five_vector-1" style="background-image:url(assets/main-img/main-slider/vector-5.png)"></div>
									<div class="slider-five_vector-2" style="background-image:url(assets/main-img/main-slider/vector-6.png)"></div>
									<div class="slider-five_vector-4" style="background-image:url(assets/main-img/main-slider/vector-7.png)"></div>
									<div class="slider-five_title" style="font-family: var(--font-arabic); direction: rtl; font-size: 1.5rem; letter-spacing: 0;">وَتَعَاوَنُوا عَلَى الْبِرِّ وَالتَّقْوَىٰ</div>
									<h1 class="slider-five_heading">Methodology of Ahlu Sunnah</h1>
									<div class="slider-five_text" style="font-weight: 500;">Learning and spreading correct Islam in Mangaluru based on Quran & Sunnah</div>
									<div class="slider-five_button mt-4">
										<a href="#donation" class="theme-btn btn-style-five">
											<span class="btn-wrap">
												<span class="text-one">Support Mission</span>
												<span class="text-two">Support Mission</span>
											</span>
										</a>
									</div>
								</div>
							</div>

							<!-- Images Column -->
							<div class="slider-five_images-column col-xl-4 col-lg-12 col-md-12 col-sm-12">
								<div class="slider-five_images-outer">
									<div class="slider-five_vector" style="background-image:url(assets/main-img/main-slider/vector-3.png)"></div>
									<div class="slider-five_vector-3" style="background-image:url(assets/main-img/main-slider/vector-6.png)"></div>
									<div class="image">
										<img src="assets/main-img/main-slider/image-5.png" alt=""/>
									</div>
								</div>
							</div>
						</div>
					</div>
				</div>

			</div>
		</div>
	</section>
	<!-- End Slider Four -->
'''
        new_lines.append(new_html)
    elif i == 831:
        new_lines.append(line)
        new_lines.append('</div><!-- End PageWrapper -->\n')
        end_stuff = r'''
	<!-- Search Popup -->
	<div class="search-popup">
		<div class="color-layer"></div>
		<button class="close-search"><span class="flaticon-close-1"></span></button>
		<form method="post" action="blog.html">
			<div class="form-group">
				<input type="search" name="search-field" value="" placeholder="Search Here" required="">
				<button class="fa fa-solid fa-magnifying-glass fa-fw" type="submit"></button>
			</div>
		</form>
	</div>
	<!-- End Search Popup -->

<div class="progress-wrap">
	<svg class="progress-circle svg-content" width="100%" height="100%" viewBox="-1 -1 102 102">
		<path d="M50,1 a49,49 0 0,1 0,98 a49,49 0 0,1 0,-98"/>
	</svg>
</div>

<script src="assets/js/jquery.js"></script>
<script src="assets/js/popper.min.js"></script>
<script src="assets/js/bootstrap.min.js"></script>
<script src="assets/js/appear.js"></script>
<script src="assets/js/parallax.min.js"></script>
<script src="assets/js/tilt.jquery.min.js"></script>
<script src="assets/js/jquery.paroller.min.js"></script>
<script src="assets/js/wow.js"></script>
<script src="assets/js/jarallax.js"></script>
<script src="assets/js/swiper.min.js"></script>
<script src="assets/js/backtotop.js"></script>
<script src="assets/js/odometer.js"></script>
<script src="assets/js/parallax-scroll.js"></script>
<script src="assets/js/gsap.min.js"></script>
<script src="assets/js/SplitText.min.js"></script>
<script src="assets/js/ScrollTrigger.min.js"></script>
<script src="assets/js/ScrollToPlugin.min.js"></script>
<script src="assets/js/ScrollSmoother.min.js"></script>
<script src="assets/js/magnific-popup.min.js"></script>
<script src="assets/js/nav-tool.js"></script>
<script src="assets/js/jquery-ui.js"></script>
<script src="assets/js/element-in-view.js"></script>
<script src="assets/js/script.js"></script>
'''
        new_lines.append(end_stuff)
    else:
        new_lines.append(line)

with open("index.html", "w", encoding="utf-8") as f:
    f.writelines(new_lines)

print("Successfully modified index.html")
