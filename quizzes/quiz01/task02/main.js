// 2.A. Define statusToHTML here:

const statusToHTML = () => {
  document.querySelector('h1').innerHTML;
  }

// 2.B. Define userToHTML here:

const userToHTML = () => {
document.querySelector('h1').innerHTML;
}







/****************/
/* Testing Code */
/****************/

const statusObj = {
  id: 1631622250167423000,
  image_url: "http://pbs.twimg.com/media/FqSYD9MaYAAsXve.jpg",
  retweet_count: 3,
  screen_name: "YayukMulawati91",
  text: "RT @mynameisvanss: i see two cats https://t.co/CNu81DwnDB",
};


const userObj = {
  id: 19397785,
  id_str: "19397785",
  name: "Oprah Winfrey",
  screen_name: "Oprah",
  location: "",
  profile_location: null,
  description: "",
  url: "https://t.co/IKOnfAha8E",
  entities: {
    url: {
      urls: [
        {
          url: "https://t.co/IKOnfAha8E",
          expanded_url: "http://www.oprah.com",
          display_url: "oprah.com",
          indices: [0, 23],
        },
      ],
    },
    description: { urls: [] },
  },
  protected: false,
  followers_count: 42952464,
  friends_count: 317,
  listed_count: 82274,
  created_at: "Fri Jan 23 15:18:34 +0000 2009",
  favourites_count: 292,
  utc_offset: null,
  time_zone: null,
  geo_enabled: false,
  verified: true,
  statuses_count: 13654,
  lang: null,
  status: {
    created_at: "Wed Jan 18 23:22:25 +0000 2023",
    id: 1615852138063618048,
    id_str: "1615852138063618048",
    text: "@ChelseaClinton @iamwesmoore Yes and I\u2019m still laughing out LoUD for real \ud83d\ude02 cause I thought at first it was some cr\u2026 https://t.co/OqPyAMOLLC",
    truncated: true,
    entities: {
      hashtags: [],
      symbols: [],
      user_mentions: [
        {
          screen_name: "ChelseaClinton",
          name: "Chelsea Clinton",
          id: 757303975,
          id_str: "757303975",
          indices: [0, 15],
        },
        {
          screen_name: "iamwesmoore",
          name: "Gov. Wes Moore",
          id: 42535683,
          id_str: "42535683",
          indices: [16, 28],
        },
      ],
      urls: [
        {
          url: "https://t.co/OqPyAMOLLC",
          expanded_url: "https://twitter.com/i/web/status/1615852138063618048",
          display_url: "twitter.com/i/web/status/1\u2026",
          indices: [117, 140],
        },
      ],
    },
    source:
      '\u003ca href="http://twitter.com/download/iphone" rel="nofollow"\u003eTwitter for iPhone\u003c/a\u003e',
    in_reply_to_status_id: 1615813620746620930,
    in_reply_to_status_id_str: "1615813620746620930",
    in_reply_to_user_id: 757303975,
    in_reply_to_user_id_str: "757303975",
    in_reply_to_screen_name: "ChelseaClinton",
    geo: null,
    coordinates: null,
    place: null,
    contributors: null,
    is_quote_status: false,
    retweet_count: 144,
    favorite_count: 7476,
    favorited: false,
    retweeted: false,
    lang: "en",
  },
  contributors_enabled: false,
  is_translator: false,
  is_translation_enabled: true,
  profile_background_color: "131516",
  profile_background_image_url:
    "http://abs.twimg.com/images/themes/theme14/bg.gif",
  profile_background_image_url_https:
    "https://abs.twimg.com/images/themes/theme14/bg.gif",
  profile_background_tile: true,
  profile_image_url:
    "http://pbs.twimg.com/profile_images/1123359369570148353/Mh-Rf4Sk_normal.jpg",
  profile_image_url_https:
    "https://pbs.twimg.com/profile_images/1123359369570148353/Mh-Rf4Sk_normal.jpg",
  profile_banner_url:
    "https://pbs.twimg.com/profile_banners/19397785/1419227197",
  profile_link_color: "009999",
  profile_sidebar_border_color: "EEEEEE",
  profile_sidebar_fill_color: "EFEFEF",
  profile_text_color: "333333",
  profile_use_background_image: true,
  has_extended_profile: false,
  default_profile: false,
  default_profile_image: false,
  following: null,
  follow_request_sent: null,
  notifications: null,
  translator_type: "none",
  withheld_in_countries: [],
};



// uncomment this line when you've finished with Q2A:
 console.log("HTML representation of a status:", statusToHTML(statusObj));

// uncomment this line when you've finished with Q2B:
 console.log("HTML representation of a verified user:", userToHTML(userObj));
 userObj.verified = false;
 console.log("HTML representation of an unverified user:", userToHTML(userObj));