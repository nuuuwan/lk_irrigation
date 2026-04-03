# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--04_03:13:11-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **115,564 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **44** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-04 03:13:11 | Deraniyagala (Kelani Ganga) | 0.16 | 🟢 Normal | -0.025 |  |
| 2026-04-04 03:13:01 | Magura (Kalu Ganga) | 2.42 | 🟢 Normal | 0.075 | 🔺 Rising |
| 2026-04-04 03:09:36 | Thaldena (Mahaweli Ganga) | 0.50 | 🟢 Normal | -10.286 |  |
| 2026-04-04 03:09:29 | Thaldena (Mahaweli Ganga) | 0.52 | 🟢 Normal | -10.286 |  |
| 2026-04-04 03:09:27 | Urawa (Nilwala Ganga) | 0.02 | 🟢 Normal | -0.009 |  |
| 2026-04-04 03:09:25 | Thaldena (Mahaweli Ganga) | 0.37 | 🟢 Normal | -10.286 |  |
| 2026-04-04 03:09:21 | Thaldena (Mahaweli Ganga) | 0.37 | 🟢 Normal | -10.286 |  |
| 2026-04-04 03:09:21 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-04-04 03:09:17 | Thaldena (Mahaweli Ganga) | 0.38 | 🟢 Normal | -10.286 |  |
| 2026-04-04 03:09:13 | Thaldena (Mahaweli Ganga) | 0.38 | 🟢 Normal | -10.286 |  |
| 2026-04-04 03:09:08 | Thaldena (Mahaweli Ganga) | 0.39 | 🟢 Normal | -10.286 |  |
| 2026-04-04 03:09:04 | Thaldena (Mahaweli Ganga) | 0.45 | 🟢 Normal | -10.286 |  |
| 2026-04-04 03:07:56 | Rathnapura (Kalu Ganga) | 0.66 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-04-04 03:07:34 | Hanwella (Kelani Ganga) | 0.29 | 🟢 Normal | -0.011 |  |
| 2026-04-04 03:07:28 | Siyambalanduwa (Heda Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-04 03:06:43 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.28 | 🟢 Normal | 4.500 | 🔺 Rising |
| 2026-04-04 03:06:33 | Wellawaya (Kirindi Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-04-04 03:06:23 | Nagalagam Street (Kelani Ganga) | 0.79 | 🟢 Normal | 0.074 | 🔺 Rising |
| 2026-04-04 03:05:47 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.21 | 🟢 Normal | 4.500 | 🔺 Rising |
| 2026-04-04 03:04:47 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-04-04 03:04:46 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.11 | 🟢 Normal | 4.500 | 🔺 Rising |
| 2026-04-04 03:04:40 | Baddegama (Gin Ganga) | 1.33 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-04-04 03:03:50 | Holombuwa (Kelani Ganga) | 0.44 | 🟢 Normal | -0.031 |  |
| 2026-04-04 03:03:38 | Nawalapitiya (Mahaweli Ganga) | 0.57 | 🟢 Normal | -0.017 |  |
| 2026-04-04 03:03:32 | Badalgama (Maha Oya) | 2.06 | 🟢 Normal | -0.010 |  |
| 2026-04-04 03:03:11 | Nakkala (Kumbukkan Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-04-04 03:03:03 | Peradeniya (Mahaweli Ganga) | 1.36 | 🟢 Normal | -0.068 |  |
| 2026-04-04 03:02:39 | Norwood (Kelani Ganga) | 0.55 | 🟢 Normal | -0.055 |  |
| 2026-04-04 03:02:38 | Ellagawa (Kalu Ganga) | 3.98 | 🟢 Normal | 0.000 |  |
| 2026-04-04 03:02:32 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-04-04 03:02:32 | Giriulla (Maha Oya) | 0.96 | 🟢 Normal | -0.020 |  |
| 2026-04-04 03:02:31 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-04 03:02:12 | Thanamalwila (Kirindi Oya) | 0.23 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-04 03:02:01 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | 0.271 | 🔺 Rising |
| 2026-04-04 03:01:48 | Horowpothana (Yan Oya) | 1.68 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-04-04 03:01:43 | Yaka Wewa (Ma Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-04-04 03:01:31 | Thawalama (Gin Ganga) | 1.37 | 🟢 Normal | -0.031 |  |
| 2026-04-04 03:01:23 | Kuda Oya (Kirindi Oya) | 1.14 | 🟢 Normal | 0.005 |  |
| 2026-04-04 03:01:11 | Moragaswewa (Deduru Oya) | 0.07 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-04-04 03:01:09 | Manampitiya (Mahaweli Ganga) | 0.93 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-04-04 03:00:40 | Glencourse (Kelani Ganga) | 8.58 | 🟢 Normal | -0.010 |  |
| 2026-04-04 02:48:27 | Horowpothana (Yan Oya) | 1.66 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-04-04 02:40:56 | Norwood (Kelani Ganga) | 0.57 | 🟢 Normal | -0.055 |  |
| 2026-04-04 02:28:07 | Nawalapitiya (Mahaweli Ganga) | 0.58 | 🟢 Normal | -0.017 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-04 03:06:43 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.28 | 🟢 Normal | 4.500 | 🔺 Rising |
| 2026-04-04 03:02:01 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | 0.271 | 🔺 Rising |
| 2026-04-04 03:01:48 | Horowpothana (Yan Oya) | 1.68 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-04-04 03:01:09 | Manampitiya (Mahaweli Ganga) | 0.93 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-04-04 03:13:01 | Magura (Kalu Ganga) | 2.42 | 🟢 Normal | 0.075 | 🔺 Rising |
| 2026-04-04 03:06:23 | Nagalagam Street (Kelani Ganga) | 0.79 | 🟢 Normal | 0.074 | 🔺 Rising |
| 2026-04-04 03:01:11 | Moragaswewa (Deduru Oya) | 0.07 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-04-03 18:05:32 | Thanthirimale (Malwathu Oya) | 3.43 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-04-04 03:04:40 | Baddegama (Gin Ganga) | 1.33 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-04-04 03:07:56 | Rathnapura (Kalu Ganga) | 0.66 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-04-04 03:02:12 | Thanamalwila (Kirindi Oya) | 0.23 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-03 18:02:55 | Galgamuwa (Mee Oya) | 0.31 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-04 03:01:23 | Kuda Oya (Kirindi Oya) | 1.14 | 🟢 Normal | 0.005 |  |
| 2026-04-04 03:09:21 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-04-04 03:06:33 | Wellawaya (Kirindi Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-04-04 03:03:11 | Nakkala (Kumbukkan Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-04-04 03:01:43 | Yaka Wewa (Ma Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-04-04 00:32:26 | Pitabeddara (Nilwala Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-04-04 03:02:38 | Ellagawa (Kalu Ganga) | 3.98 | 🟢 Normal | 0.000 |  |
| 2026-04-04 01:22:11 | Panadugama (Nilwala Ganga) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-04-04 03:02:32 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-04-04 03:07:28 | Siyambalanduwa (Heda Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-04 03:02:31 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-04 03:04:47 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-04-04 03:09:27 | Urawa (Nilwala Ganga) | 0.02 | 🟢 Normal | -0.009 |  |
| 2026-04-04 03:03:32 | Badalgama (Maha Oya) | 2.06 | 🟢 Normal | -0.010 |  |
| 2026-04-04 03:00:40 | Glencourse (Kelani Ganga) | 8.58 | 🟢 Normal | -0.010 |  |
| 2026-04-04 03:07:34 | Hanwella (Kelani Ganga) | 0.29 | 🟢 Normal | -0.011 |  |
| 2026-04-04 03:03:38 | Nawalapitiya (Mahaweli Ganga) | 0.57 | 🟢 Normal | -0.017 |  |
| 2026-04-04 00:04:26 | Padiyathalawa (Maduru Oya) | 0.73 | 🟢 Normal | -0.019 |  |
| 2026-04-04 03:02:32 | Giriulla (Maha Oya) | 0.96 | 🟢 Normal | -0.020 |  |
| 2026-04-04 02:03:15 | Thalgahagoda (Nilwala Ganga) | 0.28 | 🟢 Normal | -0.022 |  |
| 2026-04-04 03:13:11 | Deraniyagala (Kelani Ganga) | 0.16 | 🟢 Normal | -0.025 |  |
| 2026-04-04 03:03:50 | Holombuwa (Kelani Ganga) | 0.44 | 🟢 Normal | -0.031 |  |
| 2026-04-04 03:01:31 | Thawalama (Gin Ganga) | 1.37 | 🟢 Normal | -0.031 |  |
| 2026-04-04 03:02:39 | Norwood (Kelani Ganga) | 0.55 | 🟢 Normal | -0.055 |  |
| 2026-04-03 18:00:27 | Weraganthota (Mahaweli Ganga) | -3.08 | 🟢 Normal | -0.060 |  |
| 2026-04-04 03:03:03 | Peradeniya (Mahaweli Ganga) | 1.36 | 🟢 Normal | -0.068 |  |
| 2026-04-04 03:09:36 | Thaldena (Mahaweli Ganga) | 0.50 | 🟢 Normal | -10.286 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)