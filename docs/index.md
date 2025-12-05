<style>
  .align {
    /* This uses flexbox to center items horizontally. */
    display: flex;
    justify-content: center;
    flex-wrap: wrap;
    text-align: center;
  }

  .md-typeset .img-fluid {
    max-width: 100%;
    height: auto;
  }

  /* Each item in a row takes up 1/3 of the width on large screens */
  .col-3 {
    flex: 0 0 33%;
    box-sizing: border-box;
  }

  /* Adjust for medium/small screens as needed */
  @media (max-width: 768px) {
    .col-md-6 {
      flex: 0 0 50%;
    }
  }
  @media (max-width: 576px) {
    .col-sm-12 {
      flex: 0 0 100%;
    }
  }
</style>

<div class="md-content" data-md-component="content">
  <article class="md-content__inner md-typeset">
    <h1 id="documentation">Documentation</h1>
    <h3 id="select-your-device">Select your device</h3>
    <!-- ROW 1: 3D Sonar, DVL A125, DVL A50 -->
    <div class="grid align">
      <div class="col-3 col-md-6 col-sm-12">
        <a href="./sonar-3d/sonar-3d-15/">
          <img class="img-fluid"
               src="https://www.waterlinked.com/web/image/product.product/919/image_1024/%5BWL-21045-2%5D%20Sonar%203D-15?unique=6f5242e" />
          <br />
          <h4>Sonar 3D-15</h4>
        </a>
      </div>
      <div class="col-3 col-md-6 col-sm-12">
        <a href="./dvl/dvl-a125/">
          <img class="img-fluid"
               src="https://www.waterlinked.com/web/image/product.product/221/image_512/%5BWL-21037-2-S-600%5D%20DVL%20A125%20%28Standard%2C%20600m%29"/>
          <br />
          <h4>DVL A125</h4>
        </a>
      </div>
      <div class="col-3 col-md-6 col-sm-12">
        <a href="./dvl/dvl-a50/">
          <img class="img-fluid"
               src="https://www.waterlinked.com/web/image/product.product/1516/image_512/%5BWL-21035-4-S-300-SIDE-IO%5D%20DVL%20A50%20%28Standard%2C%20300m%2C%203m%20c-w%20Interface%20PCB%29"/>
          <br />
          <h4>DVL A50</h4>
        </a>
      </div>
    </div>
    <!-- ROW 2: Modem M16, Underwater GPS G2, Locator-A1 -->
    <div class="grid align">
      <div class="col-3 col-md-6 col-sm-12">
        <a href="./modem-m16/modem-m16">
          <img class="img-fluid"
               src="https://www.waterlinked.com/web/image/product.product/240/image_1024/%5BWL-21048-1-S%5D%20Modem%20M16%20%28Standard%29?unique=f736508"/>
          <br />
          <h4>Modem M16</h4>
        </a>
      </div>
      <div class="col-3 col-md-6 col-sm-12">
        <a href="./underwater-gps/introduction/">
          <img class="img-fluid"
               src="https://www.waterlinked.com/web/image/product.product/152/image_512/%5BWL-11001-2-R100-U1-ANT%5D%20Underwater%20GPS%20G2%20Standard%20Kit%20%28100m%29"/>
          <br />
          <h4>Underwater GPS G2</h4>
        </a>
      </div>
      <div class="col-3 col-md-6 col-sm-12">
        <a href="./underwater-gps/locators/locator-a1/">
          <img class="img-fluid"
               src="https://www.waterlinked.com/web/image/product.product/120/image_512/%5BWL-21009-1-N001%5D%20Locator%20A1"/>
          <br />
          <h4>Locator-A1</h4>
        </a>
      </div>
    </div>
    <!-- ROW 3: Remaining locators: U1, D1, Receiver-D1 -->
    <div class="grid align">
      <div class="col-3 col-md-6 col-sm-12">
        <a href="./underwater-gps/locators/locator-u1/">
          <img class="img-fluid"
               src="https://www.waterlinked.com/web/image/product.product/122/image_512/%5BWL-21018-1%5D%20Locator%20U1"/>
          <br />
          <h4>Locator-U1</h4>
        </a>
      </div>
      <div class="col-3 col-md-6 col-sm-12">
        <a href="./underwater-gps/locators/locator-d1/">
          <img class="img-fluid"
               src="https://www.waterlinked.com/web/image/product.product/143/image_512/%5BWL-21016-1-B050%5D%20Locator%20D1%20%2850m%29"/>
          <br />
          <h4>Locator-D1</h4>
        </a>
      </div>
      <div class="col-3 col-md-6 col-sm-12">
        <a href="./underwater-gps/receiver-d1/">
          <img class="img-fluid"
               src="https://www.waterlinked.com/web/image/product.product/145/image_512/%5BWL-21005-4-010%5D%20Receiver%20D1%20%2810m%29"/>
          <br />
          <h4>Receiver-D1</h4>
        </a>
      </div>
    </div>
  </article>
</div>
