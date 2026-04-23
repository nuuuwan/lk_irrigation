# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--24_05:02:34-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **133,441 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **16** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-24 05:02:34 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-24 05:02:24 | Dunamale (Aththanagalu Oya) | 1.90 | 🟢 Normal | 0.000 |  |
| 2026-04-24 05:01:33 | Thanamalwila (Kirindi Oya) | 1.90 | 🟢 Normal | -0.155 |  |
| 2026-04-24 05:01:20 | Thaldena (Mahaweli Ganga) | 0.43 | 🟢 Normal | -0.010 |  |
| 2026-04-24 05:01:13 | Peradeniya (Mahaweli Ganga) | 1.66 | 🟢 Normal | -0.090 |  |
| 2026-04-24 05:01:08 | Kuda Oya (Kirindi Oya) | 2.20 | 🟢 Normal | -0.071 |  |
| 2026-04-24 05:00:54 | Glencourse (Kelani Ganga) | 9.70 | 🟢 Normal | -0.010 |  |
| 2026-04-24 05:00:44 | Magura (Kalu Ganga) | 2.32 | 🟢 Normal | -0.214 |  |
| 2026-04-24 05:00:38 | Thalgahagoda (Nilwala Ganga) | 0.54 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-04-24 05:00:34 | Wellawaya (Kirindi Oya) | 1.19 | 🟢 Normal | -0.020 |  |
| 2026-04-24 04:51:17 | Urawa (Nilwala Ganga) | 0.26 | 🟢 Normal | -2.919 |  |
| 2026-04-24 04:50:40 | Urawa (Nilwala Ganga) | 0.29 | 🟢 Normal | -2.919 |  |
| 2026-04-24 04:25:50 | Deraniyagala (Kelani Ganga) | 0.61 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-04-24 04:22:33 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-04-24 04:14:06 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-24 04:10:21 | Magura (Kalu Ganga) | 2.50 | 🟢 Normal | -0.214 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-24 04:00:34 | Moraketiya (Walawe Ganga) | 1.30 | 🟢 Normal | 0.211 | 🔺 Rising |
| 2026-04-24 04:07:25 | Katharagama (Menik Ganga) | 2.00 | 🟢 Normal | 0.210 | 🔺 Rising |
| 2026-04-24 04:07:46 | Putupaula (Kalu Ganga) | 0.55 | 🟢 Normal | 0.088 | 🔺 Rising |
| 2026-04-24 04:05:54 | Badalgama (Maha Oya) | 2.48 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2026-04-24 01:00:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.90 | 🟢 Normal | 0.075 | 🔺 Rising |
| 2026-04-24 05:00:38 | Thalgahagoda (Nilwala Ganga) | 0.54 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-04-24 04:25:50 | Deraniyagala (Kelani Ganga) | 0.61 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-04-24 02:04:52 | Pitabeddara (Nilwala Ganga) | 0.69 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-04-24 04:01:41 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-04-24 04:02:37 | Moragaswewa (Deduru Oya) | 0.62 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-24 04:04:49 | Rathnapura (Kalu Ganga) | 1.06 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-04-24 04:04:45 | Kithulgala (Kelani Ganga) | 1.53 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-04-23 18:03:04 | Thanthirimale (Malwathu Oya) | 1.55 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-23 18:01:09 | Weraganthota (Mahaweli Ganga) | -3.05 | 🟢 Normal | 0.000 |  |
| 2026-04-24 05:02:34 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-24 02:02:02 | Horowpothana (Yan Oya) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-04-24 04:05:07 | Hanwella (Kelani Ganga) | 1.47 | 🟢 Normal | 0.000 |  |
| 2026-04-24 04:01:38 | Padiyathalawa (Maduru Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-04-24 04:22:33 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-04-24 05:02:24 | Dunamale (Aththanagalu Oya) | 1.90 | 🟢 Normal | 0.000 |  |
| 2026-04-24 04:03:05 | Giriulla (Maha Oya) | 1.39 | 🟢 Normal | -0.010 |  |
| 2026-04-24 05:01:20 | Thaldena (Mahaweli Ganga) | 0.43 | 🟢 Normal | -0.010 |  |
| 2026-04-23 18:03:04 | Galgamuwa (Mee Oya) | 0.12 | 🟢 Normal | -0.010 |  |
| 2026-04-24 05:00:54 | Glencourse (Kelani Ganga) | 9.70 | 🟢 Normal | -0.010 |  |
| 2026-04-24 05:00:34 | Wellawaya (Kirindi Oya) | 1.19 | 🟢 Normal | -0.020 |  |
| 2026-04-24 04:03:39 | Baddegama (Gin Ganga) | 1.90 | 🟢 Normal | -0.020 |  |
| 2026-04-24 04:00:36 | Thawalama (Gin Ganga) | 1.59 | 🟢 Normal | -0.021 |  |
| 2026-04-24 04:00:40 | Manampitiya (Mahaweli Ganga) | 0.17 | 🟢 Normal | -0.021 |  |
| 2026-04-24 04:01:46 | Nakkala (Kumbukkan Oya) | 0.88 | 🟢 Normal | -0.021 |  |
| 2026-04-24 03:02:36 | Norwood (Kelani Ganga) | 0.94 | 🟢 Normal | -0.021 |  |
| 2026-04-24 04:03:24 | Nawalapitiya (Mahaweli Ganga) | 0.96 | 🟢 Normal | -0.029 |  |
| 2026-04-24 04:07:44 | Panadugama (Nilwala Ganga) | 3.24 | 🟢 Normal | -0.032 |  |
| 2026-04-24 04:05:50 | Ellagawa (Kalu Ganga) | 5.46 | 🟢 Normal | -0.058 |  |
| 2026-04-24 05:01:08 | Kuda Oya (Kirindi Oya) | 2.20 | 🟢 Normal | -0.071 |  |
| 2026-04-24 04:06:45 | Holombuwa (Kelani Ganga) | 0.41 | 🟢 Normal | -0.078 |  |
| 2026-04-24 05:01:13 | Peradeniya (Mahaweli Ganga) | 1.66 | 🟢 Normal | -0.090 |  |
| 2026-04-24 05:01:33 | Thanamalwila (Kirindi Oya) | 1.90 | 🟢 Normal | -0.155 |  |
| 2026-04-24 05:00:44 | Magura (Kalu Ganga) | 2.32 | 🟢 Normal | -0.214 |  |
| 2026-04-24 04:51:17 | Urawa (Nilwala Ganga) | 0.26 | 🟢 Normal | -2.919 |  |

## River Water Level Charts by Station

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)