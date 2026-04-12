# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--13_04:39:36-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **123,610 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **15** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-13 04:39:36 | Urawa (Nilwala Ganga) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-04-13 04:39:00 | Urawa (Nilwala Ganga) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-04-13 04:31:56 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-13 04:26:49 | Wellawaya (Kirindi Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-04-13 04:23:50 | Magura (Kalu Ganga) | 3.95 | 🟢 Normal | -18.000 |  |
| 2026-04-13 04:23:48 | Magura (Kalu Ganga) | 3.96 | 🟢 Normal | -18.000 |  |
| 2026-04-13 04:15:22 | Putupaula (Kalu Ganga) | 0.57 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-04-13 04:13:05 | Thanamalwila (Kirindi Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-04-13 04:11:20 | Holombuwa (Kelani Ganga) | 0.48 | 🟢 Normal | -0.091 |  |
| 2026-04-13 04:10:20 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-04-13 04:06:58 | Thalgahagoda (Nilwala Ganga) | 0.39 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-04-13 04:06:34 | Badalgama (Maha Oya) | 1.79 | 🟢 Normal | -0.009 |  |
| 2026-04-13 04:06:29 | Baddegama (Gin Ganga) | 1.33 | 🟢 Normal | 0.075 | 🔺 Rising |
| 2026-04-13 04:06:11 | Thawalama (Gin Ganga) | 1.60 | 🟢 Normal | -0.089 |  |
| 2026-04-13 04:06:03 | Moragaswewa (Deduru Oya) | 0.06 | 🟢 Normal | 0.018 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-13 04:02:55 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.74 | 🟢 Normal | 9.290 | 🔺 Rising |
| 2026-04-13 04:05:06 | Panadugama (Nilwala Ganga) | 4.25 | 🟢 Normal | 2.135 | 🔺 Rising |
| 2026-04-13 04:03:59 | Ellagawa (Kalu Ganga) | 4.88 | 🟢 Normal | 0.832 | 🔺 Rising |
| 2026-04-13 04:02:55 | Glencourse (Kelani Ganga) | 8.70 | 🟢 Normal | 0.148 | 🔺 Rising |
| 2026-04-13 04:04:15 | Giriulla (Maha Oya) | 1.29 | 🟢 Normal | 0.130 | 🔺 Rising |
| 2026-04-12 18:07:41 | Galgamuwa (Mee Oya) | 0.27 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2026-04-13 04:06:29 | Baddegama (Gin Ganga) | 1.33 | 🟢 Normal | 0.075 | 🔺 Rising |
| 2026-04-13 04:02:18 | Hanwella (Kelani Ganga) | 0.38 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-04-13 04:06:58 | Thalgahagoda (Nilwala Ganga) | 0.39 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-04-13 04:15:22 | Putupaula (Kalu Ganga) | 0.57 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-04-13 04:03:12 | Manampitiya (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-13 04:06:03 | Moragaswewa (Deduru Oya) | 0.06 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-04-13 04:01:09 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-04-13 04:04:29 | Rathnapura (Kalu Ganga) | 3.66 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-04-13 04:10:20 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-04-13 04:26:49 | Wellawaya (Kirindi Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-04-13 04:02:53 | Nakkala (Kumbukkan Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-04-13 04:01:35 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-13 04:02:13 | Horowpothana (Yan Oya) | 1.48 | 🟢 Normal | 0.000 |  |
| 2026-04-13 04:04:13 | Pitabeddara (Nilwala Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-13 04:03:37 | Norwood (Kelani Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-04-13 03:01:17 | Padiyathalawa (Maduru Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-04-13 03:03:50 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-04-13 04:31:56 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-12 18:02:49 | Thanthirimale (Malwathu Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-04-13 04:39:36 | Urawa (Nilwala Ganga) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-04-13 04:13:05 | Thanamalwila (Kirindi Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-04-13 04:04:47 | Kuda Oya (Kirindi Oya) | 1.24 | 🟢 Normal | -0.005 |  |
| 2026-04-13 04:06:34 | Badalgama (Maha Oya) | 1.79 | 🟢 Normal | -0.009 |  |
| 2026-04-13 04:04:55 | Nawalapitiya (Mahaweli Ganga) | 0.63 | 🟢 Normal | -0.009 |  |
| 2026-04-13 04:04:37 | Thaldena (Mahaweli Ganga) | 0.39 | 🟢 Normal | -0.030 |  |
| 2026-04-13 03:12:58 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.031 |  |
| 2026-04-12 18:12:59 | Weraganthota (Mahaweli Ganga) | -3.20 | 🟢 Normal | -0.033 |  |
| 2026-04-13 04:06:11 | Thawalama (Gin Ganga) | 1.60 | 🟢 Normal | -0.089 |  |
| 2026-04-13 04:11:20 | Holombuwa (Kelani Ganga) | 0.48 | 🟢 Normal | -0.091 |  |
| 2026-04-13 04:03:27 | Deraniyagala (Kelani Ganga) | 0.74 | 🟢 Normal | -0.103 |  |
| 2026-04-13 04:01:19 | Peradeniya (Mahaweli Ganga) | 1.62 | 🟢 Normal | -0.127 |  |
| 2026-04-13 03:15:28 | Kithulgala (Kelani Ganga) | 1.37 | 🟢 Normal | -0.145 |  |
| 2026-04-13 04:23:50 | Magura (Kalu Ganga) | 3.95 | 🟢 Normal | -18.000 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)