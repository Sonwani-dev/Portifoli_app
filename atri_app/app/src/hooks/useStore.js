import create from "zustand";

// unsafe merge state
// and mew properties will added or existing properties will be changed
// but the type of value of the property must not change
function mergeState(baseState, newState) {
  if (
    typeof newState === "object" &&
    !Array.isArray(newState) &&
    newState !== null
  ) {
    const keys = Object.keys(newState);
    keys.forEach((key) => {
      // create a new key in base if not exists
      if (!(key in baseState)) {
        baseState[key] = {};
      }
      if (typeof newState[key] === "object" && !Array.isArray(newState[key]))
        mergeState(baseState[key], newState[key]);
      else baseState[key] = newState[key];
    });
  }
}

const useStore = create((set) => {
  return {
    setPage: (pageName, newState) =>
      set((state) => {
        const pageState = JSON.parse(JSON.stringify(state[pageName]));
        mergeState(pageState, newState);
        return { [pageName]: pageState };
      }),
  };
});

export function updateStoreStateFromController(pageName, newState) {
  useStore.getState().setPage(pageName, newState);
}

const desktopModeProps = {
  ...{
  "Home": {
    "nav_container": {
      "callbacks": {}
    },
    "nav_bar_div": {
      "callbacks": {}
    },
    "side_nav": {
      "callbacks": {}
    },
    "hero_main": {
      "callbacks": {}
    },
    "hero_flex": {
      "callbacks": {}
    },
    "heading_paragraph": {
      "callbacks": {}
    },
    "hero_button_link": {
      "callbacks": {}
    },
    "call_button_div": {
      "callbacks": {}
    },
    "companies": {
      "callbacks": {}
    },
    "services_div": {
      "callbacks": {}
    },
    "services_main": {
      "callbacks": {}
    },
    "sevices_head_main": {
      "callbacks": {}
    },
    "head_2": {
      "callbacks": {}
    },
    "services_flex": {
      "callbacks": {}
    },
    "sub_service_1": {
      "callbacks": {}
    },
    "services_heading_1": {
      "callbacks": {}
    },
    "services_1_paragraph1": {
      "callbacks": {}
    },
    "services_list_1": {
      "callbacks": {}
    },
    "services_pointer_1": {
      "callbacks": {}
    },
    "services_list_item_1": {
      "callbacks": {}
    },
    "Flex36": {
      "callbacks": {}
    },
    "list_pointer_head_3": {
      "callbacks": {}
    },
    "Flex92": {
      "callbacks": {}
    },
    "Flex91": {
      "callbacks": {}
    },
    "list_ponter_head_9ac": {
      "callbacks": {}
    },
    "Flex90": {
      "callbacks": {}
    },
    "Div111": {
      "callbacks": {}
    },
    "list_pointer_head_7": {
      "callbacks": {}
    },
    "Div112": {
      "callbacks": {}
    },
    "Div113": {
      "callbacks": {}
    },
    "sub_service_2": {
      "callbacks": {}
    },
    "Div118": {
      "callbacks": {}
    },
    "Div119": {
      "callbacks": {}
    },
    "Flex96": {
      "callbacks": {}
    },
    "Div117": {
      "callbacks": {}
    },
    "list_pointer_head_4": {
      "callbacks": {}
    },
    "Flex94": {
      "callbacks": {}
    },
    "Flex95": {
      "callbacks": {}
    },
    "projects_head_paragraph_1": {
      "callbacks": {}
    },
    "projects_heading_1": {
      "callbacks": {}
    },
    "heading_2_3_div": {
      "callbacks": {}
    },
    "view_projects_button_div": {
      "callbacks": {}
    },
    "projects_slider_flex": {
      "callbacks": {}
    },
    "projects_slider_3": {
      "callbacks": {}
    },
    "project_slider_3_paragraph_head": {
      "callbacks": {}
    },
    "slider_3_link_flex": {
      "callbacks": {}
    },
    "slider_item_2": {
      "callbacks": {}
    },
    "slider_item_2_head": {
      "callbacks": {}
    },
    "slider_item_2_link_2": {
      "callbacks": {}
    },
    "slider_item_1": {
      "callbacks": {}
    },
    "slider_item1_head_flex": {
      "callbacks": {}
    },
    "Flex136": {
      "callbacks": {}
    },
    "slider_button_left": {
      "callbacks": {}
    },
    "sliderbutton_right": {
      "callbacks": {}
    },
    "blogs_main_div": {
      "callbacks": {}
    },
    "blogs_main_flex": {
      "callbacks": {}
    },
    "blogs_heading_div": {
      "callbacks": {}
    },
    "blogs_view_all_link_flex": {
      "callbacks": {}
    },
    "blog_list_div_main": {
      "callbacks": {}
    },
    "list_item_1_flex": {
      "callbacks": {}
    },
    "list_item_1_date_time": {
      "callbacks": {}
    },
    "heading_date_time_flex": {
      "callbacks": {}
    },
    "list_heading_2_div": {
      "callbacks": {}
    },
    "list_item_1_read_link_flex": {
      "callbacks": {}
    },
    "list_item_2_flex": {
      "callbacks": {}
    },
    "list_item_2_link_flex": {
      "callbacks": {}
    },
    "list_item_2_heading_div": {
      "callbacks": {}
    },
    "Div166": {
      "callbacks": {}
    },
    "Flex158": {
      "callbacks": {}
    },
    "list_item_3_flex": {
      "callbacks": {}
    },
    "Div168": {
      "callbacks": {}
    },
    "point_div_3": {
      "callbacks": {}
    },
    "list_3_heading_div": {
      "callbacks": {}
    },
    "list_3_link": {
      "callbacks": {}
    },
    "list_item_4_flex": {
      "callbacks": {}
    },
    "list_4_link_flex": {
      "callbacks": {}
    },
    "list_4_heading_div": {
      "callbacks": {}
    },
    "Div172": {
      "callbacks": {}
    },
    "Flex164": {
      "callbacks": {}
    },
    "list_item_5_flex": {
      "callbacks": {}
    },
    "Div174": {
      "callbacks": {}
    },
    "Flex167": {
      "callbacks": {}
    },
    "vlist_5_heading_div": {
      "callbacks": {}
    },
    "list_5_link_flex": {
      "callbacks": {}
    },
    "pro_designer_main": {
      "callbacks": {}
    },
    "designer_details_flex": {
      "callbacks": {}
    },
    "designer_deatails_div": {
      "callbacks": {}
    },
    "designer_about_paragraph_div": {
      "callbacks": {}
    },
    "designer_image_flex": {
      "callbacks": {}
    },
    "designer_2_image_flex": {
      "callbacks": {}
    },
    "experience_main_div": {
      "callbacks": {}
    },
    "experience_flex": {
      "callbacks": {}
    },
    "experience_left_div": {
      "callbacks": {}
    },
    "experience_heading_div": {
      "callbacks": {}
    },
    "experience_list": {
      "callbacks": {}
    },
    "experience_list_item_1": {
      "callbacks": {}
    },
    "list_item_1_heading_div": {
      "callbacks": {}
    },
    "experience_list_item_1_year_1_flex": {
      "callbacks": {}
    },
    "experience_list_item_2": {
      "callbacks": {}
    },
    "experience_list_item_2_year_2_flex": {
      "callbacks": {}
    },
    "list_item__heading_div": {
      "callbacks": {}
    },
    "experience_list_item_3": {
      "callbacks": {}
    },
    "experience_list_item__year_3_flex": {
      "callbacks": {}
    },
    "list_item_3_heading_div": {
      "callbacks": {}
    },
    "experience_right_div": {
      "callbacks": {}
    },
    "Div200": {
      "callbacks": {}
    },
    "experience_right_list_item_3": {
      "callbacks": {}
    },
    "right_list_item_3_heading_div": {
      "callbacks": {}
    },
    "experience_right_ist_item_3_year_3_flex": {
      "callbacks": {}
    },
    "experience_right_list_item_2": {
      "callbacks": {}
    },
    "right_list_item_2_heading_div": {
      "callbacks": {}
    },
    "experience_right_ist_item_2_year_2_flex": {
      "callbacks": {}
    },
    "experience_right_list_item_1": {
      "callbacks": {}
    },
    "experience_right_ist_item_1_year_1_flex": {
      "callbacks": {}
    },
    "right_list_item_1_heading_div": {
      "callbacks": {}
    },
    "Div201": {
      "callbacks": {}
    },
    "testimonials_main": {
      "callbacks": {}
    },
    "testimonials_headings_flex": {
      "callbacks": {}
    },
    "testimonial_1_flex": {
      "callbacks": {}
    },
    "testimonial_details": {
      "callbacks": {}
    },
    "detail_div": {
      "callbacks": {}
    },
    "testimonial_name_div": {
      "callbacks": {}
    },
    "left_arrow_button": {
      "callbacks": {}
    },
    "right_arrow_div": {
      "callbacks": {}
    },
    "faq_main": {
      "callbacks": {}
    },
    "faq_heading_div": {
      "callbacks": {}
    },
    "faq_list_main_flex": {
      "callbacks": {}
    },
    "faq_left_list": {
      "callbacks": {}
    },
    "faq_list_item_1": {
      "callbacks": {}
    },
    "faq_list_heading_flex_1": {
      "callbacks": {}
    },
    "faq_list_item_4": {
      "callbacks": {}
    },
    "faq_list_item_2": {
      "callbacks": {}
    },
    "faq_list_item_3": {
      "callbacks": {}
    },
    "faq_right_list": {
      "callbacks": {}
    },
    "faq_right_list_item_3": {
      "callbacks": {}
    },
    "faq_right_list_item_2": {
      "callbacks": {}
    },
    "faq_right_list_item_4": {
      "callbacks": {}
    },
    "faq_right_list_item_1": {
      "callbacks": {}
    },
    "faq_right_list_heading_flex_1": {
      "callbacks": {}
    },
    "footer_main_div": {
      "callbacks": {}
    },
    "footer_headings_flex": {
      "callbacks": {}
    },
    "footer_heading_div": {
      "callbacks": {}
    },
    "footer_links_flex": {
      "callbacks": {}
    },
    "website_details_div": {
      "callbacks": {}
    },
    "mail_flex": {
      "callbacks": {}
    },
    "links_grid": {
      "callbacks": {}
    },
    "copyright_div": {
      "callbacks": {}
    },
    "webflow_div": {
      "callbacks": {}
    },
    "trust_heading": {
      "custom": {
        "text": "Trusted By"
      },
      "callbacks": {
        "onClick": [
          {
            "sendEventData": true
          }
        ]
      }
    },
    "projects_view_button_back": {
      "callbacks": {}
    },
    "logo_img": {
      "custom": {
        "alt": "No preview available",
        "src": "/app-assets/6078ab3cfa1bca879adb93d1_Group%2070.svg"
      },
      "callbacks": {
        "onClick": [
          {
            "sendEventData": true
          }
        ]
      }
    },
    "call_link": {
      "custom": {
        "text": "Book a Call",
        "url": "/"
      },
      "callbacks": {
        "onClick": [
          {
            "sendEventData": true
          }
        ]
      }
    },
    "about_link": {
      "custom": {
        "text": "About",
        "url": "/"
      },
      "callbacks": {
        "onClick": [
          {
            "sendEventData": true
          }
        ]
      }
    },
    "blog_link": {
      "custom": {
        "text": "Blog",
        "url": "/"
      },
      "callbacks": {
        "onClick": [
          {
            "sendEventData": true
          }
        ]
      }
    },
    "project_link": {
      "custom": {
        "text": "Project",
        "url": "/"
      },
      "callbacks": {
        "onClick": [
          {
            "sendEventData": true
          }
        ]
      }
    },
    "services_link": {
      "custom": {
        "text": "Services",
        "url": "/"
      },
      "callbacks": {
        "onClick": [
          {
            "sendEventData": true
          }
        ]
      }
    },
    "nav_call_arrow": {
      "custom": {
        "alt": "arrow",
        "src": "/app-assets/5ff019fc559a4200eda62273_Vector.svg"
      },
      "callbacks": {
        "onClick": [
          {
            "sendEventData": true
          }
        ]
      }
    },
    "trusted_div_main": {
      "callbacks": {}
    },
    "hero_image": {
      "custom": {
        "alt": "No preview available",
        "src": "/app-assets/hero-image.jpeg"
      },
      "callbacks": {
        "onClick": [
          {
            "sendEventData": true
          }
        ]
      }
    },
    "heading_1": {
      "custom": {
        "text": "I design products "
      },
      "callbacks": {
        "onClick": [
          {
            "sendEventData": true
          }
        ]
      }
    },
    "heading_2": {
      "custom": {
        "text": "that delight and"
      },
      "callbacks": {
        "onClick": [
          {
            "sendEventData": true
          }
        ]
      }
    },
    "heading_3": {
      "custom": {
        "text": "inspire people."
      },
      "callbacks": {
        "onClick": [
          {
            "sendEventData": true
          }
        ]
      }
    },
    "paragraph": {
      "custom": {
        "text": "Hi! I’m Jake, a product designer based in Berlin. I create user-friendly interfaces for fast-growing startups."
      },
      "callbacks": {
        "onClick": [
          {
            "sendEventData": true
          }
        ]
      }
    },
    "button_background": {
      "callbacks": {}
    },
    "CV_link": {
      "custom": {
        "text": "Download CV",
        "url": "/"
      },
      "callbacks": {
        "onClick": [
          {
            "sendEventData": true
          }
        ]
      }
    },
    "call_button": {
      "custom": {
        "text": "Book a Call"
      },
      "callbacks": {
        "onClick": [
          {
            "sendEventData": true
          }
        ]
      }
    },
    "company_1": {
      "custom": {
        "alt": "No preview available",
        "src": "/app-assets/logoipsum.png"
      },
      "callbacks": {
        "onClick": [
          {
            "sendEventData": true
          }
        ]
      }
    },
    "company_2": {
      "custom": {
        "alt": "No preview available",
        "src": "/app-assets/logoipsum1.png"
      },
      "callbacks": {
        "onClick": [
          {
            "sendEventData": true
          }
        ]
      }
    },
    "company_3": {
      "custom": {
        "alt": "No preview available",
        "src": "/app-assets/logoipsum2.png"
      },
      "callbacks": {
        "onClick": [
          {
            "sendEventData": true
          }
        ]
      }
    },
    "company_4": {
      "custom": {
        "alt": "No preview available",
        "src": "/app-assets/logoipsum4.png"
      },
      "callbacks": {
        "onClick": [
          {
            "sendEventData": true
          }
        ]
      }
    },
    "projects_main": {
      "callbacks": {}
    },
    "services_heading": {
      "custom": {
        "text": "SERVICES"
      },
      "callbacks": {
        "onClick": [
          {
            "sendEventData": true
          }
        ]
      }
    },
    "serices_paragraph": {
      "custom": {
        "text": "Design that solves problems, one product at a time."
      },
      "callbacks": {
        "onClick": [
          {
            "sendEventData": true
          }
        ]
      }
    },
    "services_image_1": {
      "custom": {
        "alt": "No preview available",
        "src": "/app-assets/5fef584362e74acfa6b75398_Group%2051.svg"
      },
      "callbacks": {
        "onClick": [
          {
            "sendEventData": true
          }
        ]
      }
    },
    "list_heading_1": {
      "custom": {
        "text": "What can I do for you"
      },
      "callbacks": {
        "onClick": [
          {
            "sendEventData": true
          }
        ]
      }
    },
    "list_paragraph_1": {
      "custom": {
        "text": "Faster, better products that your users love. Here's all the services I provide:"
      },
      "callbacks": {
        "onClick": [
          {
            "sendEventData": true
          }
        ]
      }
    },
    "services_bullet_point_1": {
      "callbacks": {}
    },
    "list_pointer_heading": {
      "custom": {
        "text": "Design Strategy"
      },
      "callbacks": {
        "onClick": [
          {
            "sendEventData": true
          }
        ]
      }
    },
    "list_pointer_head_2": {
      "custom": {
        "text": "Web and Mobile App Design"
      },
      "callbacks": {
        "onClick": [
          {
            "sendEventData": true
          }
        ]
      }
    },
    "Div46": {
      "callbacks": {}
    },
    "pointer_list_heading_3": {
      "custom": {
        "text": "Front-end Development"
      },
      "callbacks": {
        "onClick": [
          {
            "sendEventData": true
          }
        ]
      }
    },
    "Div47": {
      "callbacks": {}
    },
    "services_image_3": {
      "custom": {
        "alt": "No preview available",
        "src": "/app-assets/svg%205.svg"
      },
      "callbacks": {
        "onClick": [
          {
            "sendEventData": true
          }
        ]
      }
    },
    "Div109": {
      "callbacks": {}
    },
    "list_pointer_heading_9": {
      "custom": {
        "text": "Efficient and maintianable"
      },
      "callbacks": {
        "onClick": [
          {
            "sendEventData": true
          }
        ]
      }
    },
    "Div110": {
      "callbacks": {}
    },
    "list_pointer_heading_8": {
      "custom": {
        "text": "Device and user friendly"
      },
      "callbacks": {
        "onClick": [
          {
            "sendEventData": true
          }
        ]
      }
    },
    "TextBox78": {
      "custom": {
        "text": "Design Strategy"
      },
      "callbacks": {
        "onClick": [
          {
            "sendEventData": true
          }
        ]
      }
    },
    "Div108": {
      "callbacks": {}
    },
    "list_paragraph_3": {
      "custom": {
        "text": "I design products that are more than pretty. I make them shippable and usable."
      },
      "callbacks": {
        "onClick": [
          {
            "sendEventData": true
          }
        ]
      }
    },
    "list_heading_3": {
      "custom": {
        "text": "What you can expect"
      },
      "callbacks": {
        "onClick": [
          {
            "sendEventData": true
          }
        ]
      }
    },
    "services_image_2": {
      "custom": {
        "alt": "No preview available",
        "src": "/app-assets/svg2.svg"
      },
      "callbacks": {
        "onClick": [
          {
            "sendEventData": true
          }
        ]
      }
    },
    "list_heading_2": {
      "custom": {
        "text": "Applications I'm fluent in"
      },
      "callbacks": {
        "onClick": [
          {
            "sendEventData": true
          }
        ]
      }
    },
    "list_paragraph_2": {
      "custom": {
        "text": "Every designer needs the right tools to do the perfect job. Thankfully, I'm multilingual."
      },
      "callbacks": {
        "onClick": [
          {
            "sendEventData": true
          }
        ]
      }
    },
    "Div114": {
      "callbacks": {}
    },
    "list_pointer_heading_2": {
      "custom": {
        "text": "Sketch"
      },
      "callbacks": {
        "onClick": [
          {
            "sendEventData": true
          }
        ]
      }
    },
    "list_pointer_head_5": {
      "custom": {
        "text": "Webflow"
      },
      "callbacks": {
        "onClick": [
          {
            "sendEventData": true
          }
        ]
      }
    },
    "Div115": {
      "callbacks": {}
    },
    "list_pointer_heading_6": {
      "custom": {
        "text": "Figma"
      },
      "callbacks": {
        "onClick": [
          {
            "sendEventData": true
          }
        ]
      }
    },
    "Div116": {
      "callbacks": {}
    },
    "projects_head_1": {
      "custom": {
        "text": "PROJECTS"
      },
      "callbacks": {
        "onClick": [
          {
            "sendEventData": true
          }
        ]
      }
    },
    "projects_heading_2": {
      "custom": {
        "text": "I bring results. "
      },
      "callbacks": {
        "onClick": [
          {
            "sendEventData": true
          }
        ]
      }
    },
    "projeccts_heading_3": {
      "custom": {
        "text": "My clients are proof."
      },
      "callbacks": {
        "onClick": [
          {
            "sendEventData": true
          }
        ]
      }
    },
    "view_projects_button": {
      "custom": {
        "text": "View All Projects"
      },
      "callbacks": {
        "onClick": [
          {
            "sendEventData": true
          }
        ]
      }
    },
    "slider_3_image": {
      "custom": {
        "alt": "project slider 3 image",
        "src": "/app-assets/web%20design.png"
      },
      "callbacks": {
        "onClick": [
          {
            "sendEventData": true
          }
        ]
      }
    },
    "slider_3_head_1": {
      "custom": {
        "text": "WEB DESIGN"
      },
      "callbacks": {
        "onClick": [
          {
            "sendEventData": true
          }
        ]
      }
    },
    "slider_3_head_2": {
      "custom": {
        "text": "Maize Website Design"
      },
      "callbacks": {
        "onClick": [
          {
            "sendEventData": true
          }
        ]
      }
    },
    "slider_3_flex_head_3": {
      "custom": {
        "text": "View Project"
      },
      "callbacks": {
        "onClick": [
          {
            "sendEventData": true
          }
        ]
      }
    },
    "slider_3_head_image": {
      "custom": {
        "alt": "arrow",
        "src": "/app-assets/5ff019fc559a4200eda62273_Vector.svg"
      },
      "callbacks": {
        "onClick": [
          {
            "sendEventData": true
          }
        ]
      }
    },
    "slider_item_1_image_2": {
      "custom": {
        "alt": "Random Image 2 ",
        "src": "/app-assets/prod%20desingn%20image.png"
      },
      "callbacks": {
        "onClick": [
          {
            "sendEventData": true
          }
        ]
      }
    },
    "slider_item_2_head_2": {
      "custom": {
        "text": "Datadash Product Design"
      },
      "callbacks": {
        "onClick": [
          {
            "sendEventData": true
          }
        ]
      }
    },
    "slider_item_2_product": {
      "custom": {
        "text": "PRODUCT DESIGN"
      },
      "callbacks": {
        "onClick": [
          {
            "sendEventData": true
          }
        ]
      }
    },
    "Image44": {
      "custom": {
        "alt": "arrow",
        "src": "/app-assets/5ff019fc559a4200eda62273_Vector.svg"
      },
      "callbacks": {
        "onClick": [
          {
            "sendEventData": true
          }
        ]
      }
    },
    "TextBox116": {
      "custom": {
        "text": "View Project"
      },
      "callbacks": {
        "onClick": [
          {
            "sendEventData": true
          }
        ]
      }
    },
    "slider_image_1": {
      "custom": {
        "alt": "random image 1 ",
        "src": "/app-assets/branding%20img.png"
      },
      "callbacks": {
        "onClick": [
          {
            "sendEventData": true
          }
        ]
      }
    },
    "slider_item_1_head_2": {
      "custom": {
        "text": "Soulful Rebrand"
      },
      "callbacks": {
        "onClick": [
          {
            "sendEventData": true
          }
        ]
      }
    },
    "slider_branding_head": {
      "custom": {
        "text": "BRANDING"
      },
      "callbacks": {
        "onClick": [
          {
            "sendEventData": true
          }
        ]
      }
    },
    "arrow_image_1": {
      "custom": {
        "alt": "arrow",
        "src": "/app-assets/5ff019fc559a4200eda62273_Vector.svg"
      },
      "callbacks": {
        "onClick": [
          {
            "sendEventData": true
          }
        ]
      }
    },
    "slider_view_link_1": {
      "custom": {
        "text": "View Project"
      },
      "callbacks": {
        "onClick": [
          {
            "sendEventData": true
          }
        ]
      }
    },
    "blog_left_arrow_image": {
      "custom": {
        "alt": "left",
        "src": "/app-assets/left%20arrow.svg"
      },
      "callbacks": {
        "onClick": [
          {
            "sendEventData": true
          }
        ]
      }
    },
    "blogs_right_arrow_image": {
      "custom": {
        "alt": "right",
        "src": "/app-assets/right%20arrow.svg"
      },
      "callbacks": {
        "onClick": [
          {
            "sendEventData": true
          }
        ]
      }
    },
    "heading_blogs": {
      "custom": {
        "text": "BLOGS"
      },
      "callbacks": {
        "onClick": [
          {
            "sendEventData": true
          }
        ]
      }
    },
    "latest_blogs_heading": {
      "custom": {
        "text": "Latest Blogs"
      },
      "callbacks": {
        "onClick": [
          {
            "sendEventData": true
          }
        ]
      }
    },
    "view_all_link": {
      "custom": {
        "text": "View all"
      },
      "callbacks": {
        "onClick": [
          {
            "sendEventData": true
          }
        ]
      }
    },
    "arrow_image": {
      "custom": {
        "alt": "arrow",
        "src": "/app-assets/link_arrow.svg"
      },
      "callbacks": {
        "onClick": [
          {
            "sendEventData": true
          }
        ]
      }
    },
    "heading_time": {
      "custom": {
        "text": "6 mins"
      },
      "callbacks": {
        "onClick": [
          {
            "sendEventData": true
          }
        ]
      }
    },
    "point_div1": {
      "callbacks": {}
    },
    "heading_date": {
      "custom": {
        "text": "April 16, 2021"
      },
      "callbacks": {
        "onClick": [
          {
            "sendEventData": true
          }
        ]
      }
    },
    "list_item_1_heading_2": {
      "custom": {
        "text": "Design tips for designers, that cover everything you need"
      },
      "callbacks": {
        "onClick": [
          {
            "sendEventData": true
          }
        ]
      }
    },
    "list_1_read_link": {
      "custom": {
        "text": "Read this Article "
      },
      "callbacks": {
        "onClick": [
          {
            "sendEventData": true
          }
        ]
      }
    },
    "list_link_arrow_image": {
      "custom": {
        "alt": "arrow",
        "src": "/app-assets/link_arrow.svg"
      },
      "callbacks": {
        "onClick": [
          {
            "sendEventData": true
          }
        ]
      }
    },
    "list_arrow_image": {
      "custom": {
        "alt": "arrow",
        "src": "/app-assets/link_arrow.svg"
      },
      "callbacks": {
        "onClick": [
          {
            "sendEventData": true
          }
        ]
      }
    },
    "list_2_link": {
      "custom": {
        "text": "Read this Article "
      },
      "callbacks": {
        "onClick": [
          {
            "sendEventData": true
          }
        ]
      }
    },
    "list_item_heading_2": {
      "custom": {
        "text": "How to build rapport with your web design clients"
      },
      "callbacks": {
        "onClick": [
          {
            "sendEventData": true
          }
        ]
      }
    },
    "list_item_2_date": {
      "custom": {
        "text": "April 16, 2021"
      },
      "callbacks": {
        "onClick": [
          {
            "sendEventData": true
          }
        ]
      }
    },
    "point_div_2": {
      "callbacks": {}
    },
    "list_item_2_time": {
      "custom": {
        "text": "5 mins"
      },
      "callbacks": {
        "onClick": [
          {
            "sendEventData": true
          }
        ]
      }
    },
    "list_3_time": {
      "custom": {
        "text": "5 mins"
      },
      "callbacks": {
        "onClick": [
          {
            "sendEventData": true
          }
        ]
      }
    },
    "point_div3": {
      "callbacks": {}
    },
    "list_3_date": {
      "custom": {
        "text": "April 16, 2021"
      },
      "callbacks": {
        "onClick": [
          {
            "sendEventData": true
          }
        ]
      }
    },
    "list_3_heading": {
      "custom": {
        "text": "Top 6 free website mockup tools 2021"
      },
      "callbacks": {
        "onClick": [
          {
            "sendEventData": true
          }
        ]
      }
    },
    "list_3_link_3": {
      "custom": {
        "text": "Read this Article "
      },
      "callbacks": {
        "onClick": [
          {
            "sendEventData": true
          }
        ]
      }
    },
    "arrow_image_3": {
      "custom": {
        "alt": "arrow",
        "src": "/app-assets/link_arrow.svg"
      },
      "callbacks": {
        "onClick": [
          {
            "sendEventData": true
          }
        ]
      }
    },
    "arrow_image_4": {
      "custom": {
        "alt": "arrow",
        "src": "/app-assets/link_arrow.svg"
      },
      "callbacks": {
        "onClick": [
          {
            "sendEventData": true
          }
        ]
      }
    },
    "list_4_link": {
      "custom": {
        "text": "Read this Article "
      },
      "callbacks": {
        "onClick": [
          {
            "sendEventData": true
          }
        ]
      }
    },
    "list_4_heading": {
      "custom": {
        "text": "Logo design trends to avoid in 2021"
      },
      "callbacks": {
        "onClick": [
          {
            "sendEventData": true
          }
        ]
      }
    },
    "list_4_date": {
      "custom": {
        "text": "April 16, 2021"
      },
      "callbacks": {
        "onClick": [
          {
            "sendEventData": true
          }
        ]
      }
    },
    "point_div_4": {
      "callbacks": {}
    },
    "list_4_time": {
      "custom": {
        "text": "7 mins"
      },
      "callbacks": {
        "onClick": [
          {
            "sendEventData": true
          }
        ]
      }
    },
    "list_5_time": {
      "custom": {
        "text": "7 mins"
      },
      "callbacks": {
        "onClick": [
          {
            "sendEventData": true
          }
        ]
      }
    },
    "point_div_5": {
      "callbacks": {}
    },
    "list_5_date_": {
      "custom": {
        "text": "April 16, 2021"
      },
      "callbacks": {
        "onClick": [
          {
            "sendEventData": true
          }
        ]
      }
    },
    "list_5_heading": {
      "custom": {
        "text": "22 best UI design tools"
      },
      "callbacks": {
        "onClick": [
          {
            "sendEventData": true
          }
        ]
      }
    },
    "list_5_link": {
      "custom": {
        "text": "Read this Article "
      },
      "callbacks": {
        "onClick": [
          {
            "sendEventData": true
          }
        ]
      }
    },
    "arrow_image_5": {
      "custom": {
        "alt": "arrow",
        "src": "/app-assets/link_arrow.svg"
      },
      "callbacks": {
        "onClick": [
          {
            "sendEventData": true
          }
        ]
      }
    },
    "designer_heading_main": {
      "custom": {
        "text": "PRODUCT DESIGNER"
      },
      "callbacks": {
        "onClick": [
          {
            "sendEventData": true
          }
        ]
      }
    },
    "designer_about_heading_2": {
      "custom": {
        "text": "That's me!"
      },
      "callbacks": {
        "onClick": [
          {
            "sendEventData": true
          }
        ]
      }
    },
    "designer_about_paragraph": {
      "custom": {
        "text": "Over the past 12 years, I've worked with a diverse range of clients, from startups to Fortune 500 companies. I love crafting interfaces that delight users and help businesses grow."
      },
      "callbacks": {
        "onClick": [
          {
            "sendEventData": true
          }
        ]
      }
    },
    "designer_image_2": {
      "custom": {
        "alt": "office image",
        "src": "/app-assets/designer_image%20_2.png"
      },
      "callbacks": {
        "onClick": [
          {
            "sendEventData": true
          }
        ]
      }
    },
    "designer_image_1": {
      "custom": {
        "alt": "phone image",
        "src": "/app-assets/designer_image%20_1.png"
      },
      "callbacks": {
        "onClick": [
          {
            "sendEventData": true
          }
        ]
      }
    },
    "designer_image_3": {
      "custom": {
        "alt": "laptop image",
        "src": "/app-assets/designer_image%20_3.png"
      },
      "callbacks": {
        "onClick": [
          {
            "sendEventData": true
          }
        ]
      }
    },
    "designer_image_4": {
      "custom": {
        "alt": "office image ",
        "src": "/app-assets/designer_image%20_4.png"
      },
      "callbacks": {
        "onClick": [
          {
            "sendEventData": true
          }
        ]
      }
    },
    "education_heading": {
      "custom": {
        "text": "📚  Education"
      },
      "callbacks": {
        "onClick": [
          {
            "sendEventData": true
          }
        ]
      }
    },
    "list_border_div_1": {
      "callbacks": {}
    },
    "experience_list_item_1_link_1": {
      "custom": {
        "text": "Stanford University",
        "url": "/"
      },
      "callbacks": {
        "onClick": [
          {
            "sendEventData": true
          }
        ]
      }
    },
    "experience_list_item_1_heading": {
      "custom": {
        "text": "MSc (Human Computer Interaction)"
      },
      "callbacks": {
        "onClick": [
          {
            "sendEventData": true
          }
        ]
      }
    },
    "list_item_1_date": {
      "custom": {
        "text": "• 2013-2015"
      },
      "callbacks": {
        "onClick": [
          {
            "sendEventData": true
          }
        ]
      }
    },
    "up_right_arrow_1": {
      "custom": {
        "alt": "arrow",
        "src": "/app-assets/up_right_arrow.svg"
      },
      "callbacks": {
        "onClick": [
          {
            "sendEventData": true
          }
        ]
      }
    },
    "list_border_div_2": {
      "callbacks": {}
    },
    "up_right_arrow_2": {
      "custom": {
        "alt": "arrow",
        "src": "/app-assets/up_right_arrow.svg"
      },
      "callbacks": {
        "onClick": [
          {
            "sendEventData": true
          }
        ]
      }
    },
    "list_item__date": {
      "custom": {
        "text": "• 2013-2014"
      },
      "callbacks": {
        "onClick": [
          {
            "sendEventData": true
          }
        ]
      }
    },
    "list_item_2_link": {
      "custom": {
        "text": "MIT Summer School",
        "url": "/"
      },
      "callbacks": {
        "onClick": [
          {
            "sendEventData": true
          }
        ]
      }
    },
    "experience_list_item_2_heading": {
      "custom": {
        "text": "UX Training Bootcamp"
      },
      "callbacks": {
        "onClick": [
          {
            "sendEventData": true
          }
        ]
      }
    },
    "list_border_div_3": {
      "callbacks": {}
    },
    "up_right_arrow_3": {
      "custom": {
        "alt": "arrow",
        "src": "/app-assets/up_right_arrow.svg"
      },
      "callbacks": {
        "onClick": [
          {
            "sendEventData": true
          }
        ]
      }
    },
    "list_item_3_date": {
      "custom": {
        "text": "• 2009-2012"
      },
      "callbacks": {
        "onClick": [
          {
            "sendEventData": true
          }
        ]
      }
    },
    "experience_list_item_3_heading": {
      "custom": {
        "text": "BSc in Software Engineering"
      },
      "callbacks": {
        "onClick": [
          {
            "sendEventData": true
          }
        ]
      }
    },
    "experience_list_item_3_link_3": {
      "custom": {
        "text": "Stanford University",
        "url": "/"
      },
      "callbacks": {
        "onClick": [
          {
            "sendEventData": true
          }
        ]
      }
    },
    "list_border_div_6": {
      "callbacks": {}
    },
    "right_list_item_3_image_3": {
      "custom": {
        "alt": "",
        "src": "/app-assets/crown.svg"
      },
      "callbacks": {
        "onClick": [
          {
            "sendEventData": true
          }
        ]
      }
    },
    "experience_right_list_item_3_link_3": {
      "custom": {
        "text": " Kingdom",
        "url": "/"
      },
      "callbacks": {
        "onClick": [
          {
            "sendEventData": true
          }
        ]
      }
    },
    "experience_right_list_item_3_heading": {
      "custom": {
        "text": "UI Designer"
      },
      "callbacks": {
        "onClick": [
          {
            "sendEventData": true
          }
        ]
      }
    },
    "right_list_item_3_date": {
      "custom": {
        "text": "• April 2016 - May 2017"
      },
      "callbacks": {
        "onClick": [
          {
            "sendEventData": true
          }
        ]
      }
    },
    "up_right_arrow_6": {
      "custom": {
        "alt": "arrow",
        "src": "/app-assets/up_right_arrow.svg"
      },
      "callbacks": {
        "onClick": [
          {
            "sendEventData": true
          }
        ]
      }
    },
    "list_border_div_5": {
      "callbacks": {}
    },
    "right_list_item_2_image_2": {
      "custom": {
        "alt": "song ",
        "src": "/app-assets/music.svg"
      },
      "callbacks": {
        "onClick": [
          {
            "sendEventData": true
          }
        ]
      }
    },
    "experience_right_list_item_2_heading": {
      "custom": {
        "text": " Information Architect"
      },
      "callbacks": {
        "onClick": [
          {
            "sendEventData": true
          }
        ]
      }
    },
    "experience_right_list_item_2_link_2": {
      "custom": {
        "text": " Music Mash",
        "url": "/"
      },
      "callbacks": {
        "onClick": [
          {
            "sendEventData": true
          }
        ]
      }
    },
    "right_list_item_2_date": {
      "custom": {
        "text": "• April 2016 - May 2017"
      },
      "callbacks": {
        "onClick": [
          {
            "sendEventData": true
          }
        ]
      }
    },
    "up_right_arrow_5": {
      "custom": {
        "alt": "arrow",
        "src": "/app-assets/up_right_arrow.svg"
      },
      "callbacks": {
        "onClick": [
          {
            "sendEventData": true
          }
        ]
      }
    },
    "list_border_div_4": {
      "callbacks": {}
    },
    "right_list_item_1_image_1": {
      "custom": {
        "alt": "rocket",
        "src": "/app-assets/rocket.svg"
      },
      "callbacks": {
        "onClick": [
          {
            "sendEventData": true
          }
        ]
      }
    },
    "up_right_arrow_4": {
      "custom": {
        "alt": "arrow",
        "src": "/app-assets/up_right_arrow.svg"
      },
      "callbacks": {
        "onClick": [
          {
            "sendEventData": true
          }
        ]
      }
    },
    "right_list_item_1_date": {
      "custom": {
        "text": "April 2019 - Current"
      },
      "callbacks": {
        "onClick": [
          {
            "sendEventData": true
          }
        ]
      }
    },
    "experience_right_list_item_1_heading": {
      "custom": {
        "text": "Senior Product Designer"
      },
      "callbacks": {
        "onClick": [
          {
            "sendEventData": true
          }
        ]
      }
    },
    "experience_right_list_item_1_link_1": {
      "custom": {
        "text": "SpaceFleet",
        "url": "/"
      },
      "callbacks": {
        "onClick": [
          {
            "sendEventData": true
          }
        ]
      }
    },
    "work_experience_heading": {
      "custom": {
        "text": "💼  Work Experience"
      },
      "callbacks": {
        "onClick": [
          {
            "sendEventData": true
          }
        ]
      }
    },
    "testimonials_heading_1": {
      "custom": {
        "text": "TESTIMONIALS"
      },
      "callbacks": {
        "onClick": [
          {
            "sendEventData": true
          }
        ]
      }
    },
    "testimonials_heading_2": {
      "custom": {
        "text": "Word on the street"
      },
      "callbacks": {
        "onClick": [
          {
            "sendEventData": true
          }
        ]
      }
    },
    "testimonial_1_image": {
      "custom": {
        "alt": "person",
        "src": "/app-assets/person.jpeg"
      },
      "callbacks": {
        "onClick": [
          {
            "sendEventData": true
          }
        ]
      }
    },
    "double_quotes_image": {
      "custom": {
        "alt": "double quotes",
        "src": "/app-assets/double%20quots.svg"
      },
      "callbacks": {
        "onClick": [
          {
            "sendEventData": true
          }
        ]
      }
    },
    "detail": {
      "custom": {
        "text": "Jade helped us build a software so intuitive that it didn't need a walkthrough. He solved complex problems with brilliant design."
      },
      "callbacks": {
        "onClick": [
          {
            "sendEventData": true
          }
        ]
      }
    },
    "testimonial_name": {
      "custom": {
        "text": "John Frankin"
      },
      "callbacks": {
        "onClick": [
          {
            "sendEventData": true
          }
        ]
      }
    },
    "testimonial_designation": {
      "custom": {
        "text": "Founder, Double Bunch"
      },
      "callbacks": {
        "onClick": [
          {
            "sendEventData": true
          }
        ]
      }
    },
    "left_arrow": {
      "custom": {
        "alt": "a",
        "src": "/app-assets/white%20left%20arrow.svg"
      },
      "callbacks": {
        "onClick": [
          {
            "sendEventData": true
          }
        ]
      }
    },
    "right_arrow": {
      "custom": {
        "alt": "arrow",
        "src": "/app-assets/white%20right%20arrow.svg"
      },
      "callbacks": {
        "onClick": [
          {
            "sendEventData": true
          }
        ]
      }
    },
    "faq_heading": {
      "custom": {
        "text": "FAQ"
      },
      "callbacks": {
        "onClick": [
          {
            "sendEventData": true
          }
        ]
      }
    },
    "faq_heading_2": {
      "custom": {
        "text": "Frequently asked questions"
      },
      "callbacks": {
        "onClick": [
          {
            "sendEventData": true
          }
        ]
      }
    },
    "list_question_1": {
      "custom": {
        "text": "What type of projects do you take on?"
      },
      "callbacks": {
        "onClick": [
          {
            "sendEventData": true
          }
        ]
      }
    },
    "list_down_arrow_1": {
      "custom": {
        "alt": "arrow",
        "src": "/app-assets/white%20down%20arrow.svg"
      },
      "callbacks": {
        "onClick": [
          {
            "sendEventData": true
          }
        ]
      }
    },
    "list_down_arrow_4": {
      "custom": {
        "alt": "arrow",
        "src": "/app-assets/white%20down%20arrow.svg"
      },
      "callbacks": {
        "onClick": [
          {
            "sendEventData": true
          }
        ]
      }
    },
    "list_question_4": {
      "custom": {
        "text": "What is the typical timeline for a project?"
      },
      "callbacks": {
        "onClick": [
          {
            "sendEventData": true
          }
        ]
      }
    },
    "list_down_arrow_2": {
      "custom": {
        "alt": "arrow",
        "src": "/app-assets/white%20down%20arrow.svg"
      },
      "callbacks": {
        "onClick": [
          {
            "sendEventData": true
          }
        ]
      }
    },
    "list_question_2": {
      "custom": {
        "text": "What is your hourly rate?"
      },
      "callbacks": {
        "onClick": [
          {
            "sendEventData": true
          }
        ]
      }
    },
    "list_down_arrow_3": {
      "custom": {
        "alt": "arrow",
        "src": "/app-assets/white%20down%20arrow.svg"
      },
      "callbacks": {
        "onClick": [
          {
            "sendEventData": true
          }
        ]
      }
    },
    "list_question_3": {
      "custom": {
        "text": "What time-zone do you work in?"
      },
      "callbacks": {
        "onClick": [
          {
            "sendEventData": true
          }
        ]
      }
    },
    "right_list_question_3": {
      "custom": {
        "text": "What metrics do you use to measure success?"
      },
      "callbacks": {
        "onClick": [
          {
            "sendEventData": true
          }
        ]
      }
    },
    "right_list_down_arrow_3": {
      "custom": {
        "alt": "arrow",
        "src": "/app-assets/white%20down%20arrow.svg"
      },
      "callbacks": {
        "onClick": [
          {
            "sendEventData": true
          }
        ]
      }
    },
    "right_list_question_2": {
      "custom": {
        "text": "What does your design process look like?"
      },
      "callbacks": {
        "onClick": [
          {
            "sendEventData": true
          }
        ]
      }
    },
    "list_down_arrow_6": {
      "custom": {
        "alt": "arrow",
        "src": "/app-assets/white%20down%20arrow.svg"
      },
      "callbacks": {
        "onClick": [
          {
            "sendEventData": true
          }
        ]
      }
    },
    "right_list_question_4": {
      "custom": {
        "text": "What if I need help after the project is complete?"
      },
      "callbacks": {
        "onClick": [
          {
            "sendEventData": true
          }
        ]
      }
    },
    "right_list_down_arrow_4": {
      "custom": {
        "alt": "arrow",
        "src": "/app-assets/white%20down%20arrow.svg"
      },
      "callbacks": {
        "onClick": [
          {
            "sendEventData": true
          }
        ]
      }
    },
    "list_down_arrow_5": {
      "custom": {
        "alt": "arrow",
        "src": "/app-assets/white%20down%20arrow.svg"
      },
      "callbacks": {
        "onClick": [
          {
            "sendEventData": true
          }
        ]
      }
    },
    "right_list_question_1": {
      "custom": {
        "text": "How do you charge for projects ?"
      },
      "callbacks": {
        "onClick": [
          {
            "sendEventData": true
          }
        ]
      }
    },
    "footer_heading_1": {
      "custom": {
        "text": "Ready to make something kickass?"
      },
      "callbacks": {
        "onClick": [
          {
            "sendEventData": true
          }
        ]
      }
    },
    "footer_heading_2": {
      "custom": {
        "text": "Let's get on a call."
      },
      "callbacks": {
        "onClick": [
          {
            "sendEventData": true
          }
        ]
      }
    },
    "logo_link_image": {
      "custom": {
        "alt": "logo",
        "src": "/app-assets/white%20link.svg"
      },
      "callbacks": {
        "onClick": [
          {
            "sendEventData": true
          }
        ]
      }
    },
    "address_text": {
      "custom": {
        "text": "4353 Delaware Avenue, San Francisco, USA"
      },
      "callbacks": {
        "onClick": [
          {
            "sendEventData": true
          }
        ]
      }
    },
    "mail_icon_image": {
      "custom": {
        "alt": "mail",
        "src": "/app-assets/mail.svg"
      },
      "callbacks": {
        "onClick": [
          {
            "sendEventData": true
          }
        ]
      }
    },
    "mail_link": {
      "custom": {
        "text": "hi@thefolio.com",
        "url": "/"
      },
      "callbacks": {
        "onClick": [
          {
            "sendEventData": true
          }
        ]
      }
    },
    "footer_link_9": {
      "custom": {
        "text": "Twitter",
        "url": "/"
      },
      "callbacks": {
        "onClick": [
          {
            "sendEventData": true
          }
        ]
      }
    },
    "footer_link_1": {
      "custom": {
        "text": "About",
        "url": "/"
      },
      "callbacks": {
        "onClick": [
          {
            "sendEventData": true
          }
        ]
      }
    },
    "footer_link_2": {
      "custom": {
        "text": "Services",
        "url": "/"
      },
      "callbacks": {
        "onClick": [
          {
            "sendEventData": true
          }
        ]
      }
    },
    "footer_link_7": {
      "custom": {
        "text": "Dribbble",
        "url": "/"
      },
      "callbacks": {
        "onClick": [
          {
            "sendEventData": true
          }
        ]
      }
    },
    "footer_link_6": {
      "custom": {
        "text": "Projects",
        "url": "/"
      },
      "callbacks": {
        "onClick": [
          {
            "sendEventData": true
          }
        ]
      }
    },
    "footer_link_3": {
      "custom": {
        "text": "Experience",
        "url": "/"
      },
      "callbacks": {
        "onClick": [
          {
            "sendEventData": true
          }
        ]
      }
    },
    "footer_link_5": {
      "custom": {
        "text": "Blog",
        "url": "/"
      },
      "callbacks": {
        "onClick": []
      }
    },
    "footer_link_4": {
      "custom": {
        "text": "Contact",
        "url": "/"
      },
      "callbacks": {
        "onClick": [
          {
            "sendEventData": true
          }
        ]
      }
    },
    "footer_link_8": {
      "custom": {
        "text": "Instagram",
        "url": "/"
      },
      "callbacks": {
        "onClick": [
          {
            "sendEventData": true
          }
        ]
      }
    },
    "rights_text": {
      "custom": {
        "text": "© All rights reserved."
      },
      "callbacks": {
        "onClick": [
          {
            "sendEventData": true
          }
        ]
      }
    },
    "Conversionflow_link": {
      "custom": {
        "text": "Conversionflow.",
        "url": "/"
      },
      "callbacks": {
        "onClick": [
          {
            "sendEventData": true
          }
        ]
      }
    },
    "powered_rext": {
      "custom": {
        "text": "powered by"
      },
      "callbacks": {
        "onClick": [
          {
            "sendEventData": true
          }
        ]
      }
    },
    "Webflow_link": {
      "custom": {
        "text": " Webflow /",
        "url": "/"
      },
      "callbacks": {
        "onClick": [
          {
            "sendEventData": true
          }
        ]
      }
    },
    "image_text_link": {
      "custom": {
        "text": "Image License Info",
        "url": "/"
      },
      "callbacks": {
        "onClick": [
          {
            "sendEventData": true
          }
        ]
      }
    },
    "instructions_link": {
      "custom": {
        "text": "/ Instructions",
        "url": "/"
      },
      "callbacks": {
        "onClick": [
          {
            "sendEventData": true
          }
        ]
      }
    },
    "Changelog_link": {
      "custom": {
        "text": "/ Changelog",
        "url": "/"
      },
      "callbacks": {
        "onClick": [
          {
            "sendEventData": true
          }
        ]
      }
    },
    "last_link": {
      "custom": {
        "text": "/ Style Guide",
        "url": "/"
      },
      "callbacks": {
        "onClick": [
          {
            "sendEventData": true
          }
        ]
      }
    },
    "webflow_logo": {
      "custom": {
        "alt": "webflow",
        "src": "/app-assets/webflow.svg"
      },
      "callbacks": {
        "onClick": [
          {
            "sendEventData": true
          }
        ]
      }
    },
    "webflow_text_image": {
      "custom": {
        "alt": "made in webflow",
        "src": "/app-assets/made%20in%20webflow.svg"
      },
      "callbacks": {
        "onClick": [
          {
            "sendEventData": true
          }
        ]
      }
    }
  }
}};

useStore.setState(desktopModeProps);

export default useStore;
