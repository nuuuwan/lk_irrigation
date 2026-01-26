# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--26_05:24:25-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **55,845 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **42** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-26 05:24:25 | Thawalama (Gin Ganga) | 0.96 | 🟢 Normal | -0.010 |  |
| 2026-01-26 05:17:56 | Pitabeddara (Nilwala Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-01-26 05:17:45 | Glencourse (Kelani Ganga) | 8.54 | 🟢 Normal | 0.075 | 🔺 Rising |
| 2026-01-26 05:06:37 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.065 | 🔺 Rising |
| 2026-01-26 05:06:11 | Deraniyagala (Kelani Ganga) | 0.07 | 🟢 Normal | -0.027 |  |
| 2026-01-26 05:06:08 | Magura (Kalu Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-01-26 05:05:59 | Baddegama (Gin Ganga) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-01-26 05:05:57 | Panadugama (Nilwala Ganga) | 1.97 | 🟢 Normal | 0.000 |  |
| 2026-01-26 05:04:47 | Giriulla (Maha Oya) | 0.80 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-26 05:04:44 | Rathnapura (Kalu Ganga) | 0.75 | 🟢 Normal | -0.021 |  |
| 2026-01-26 05:04:43 | Urawa (Nilwala Ganga) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-01-26 05:04:41 | Hanwella (Kelani Ganga) | 0.29 | 🟢 Normal | -0.040 |  |
| 2026-01-26 05:04:28 | Ellagawa (Kalu Ganga) | 0.76 | 🟢 Normal | -101.271 |  |
| 2026-01-26 05:04:11 | Padiyathalawa (Maduru Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-01-26 05:04:00 | Dunamale (Aththanagalu Oya) | 0.38 | 🟢 Normal | -0.010 |  |
| 2026-01-26 05:03:56 | Nakkala (Kumbukkan Oya) | 0.86 | 🟢 Normal | -0.011 |  |
| 2026-01-26 05:03:32 | Moraketiya (Walawe Ganga) | 0.85 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-01-26 05:03:31 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | -0.042 |  |
| 2026-01-26 05:02:56 | Horowpothana (Yan Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-01-26 05:02:52 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-01-26 05:02:42 | Manampitiya (Mahaweli Ganga) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-01-26 05:02:41 | Ellagawa (Kalu Ganga) | 3.77 | 🟢 Normal | -101.271 |  |
| 2026-01-26 05:02:40 | Manampitiya (Mahaweli Ganga) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-01-26 05:02:36 | Katharagama (Menik Ganga) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-01-26 05:02:33 | Manampitiya (Mahaweli Ganga) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-01-26 05:02:32 | Manampitiya (Mahaweli Ganga) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-01-26 05:02:20 | Yaka Wewa (Ma Oya) | 0.96 | 🟢 Normal | -0.020 |  |
| 2026-01-26 05:01:59 | Kithulgala (Kelani Ganga) | 1.52 | 🟢 Normal | -0.012 |  |
| 2026-01-26 05:01:46 | Moragaswewa (Deduru Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-01-26 05:01:43 | Siyambalanduwa (Heda Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-01-26 05:01:41 | Peradeniya (Mahaweli Ganga) | 1.60 | 🟢 Normal | -0.111 |  |
| 2026-01-26 05:01:12 | Manampitiya (Mahaweli Ganga) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-01-26 05:01:08 | Nawalapitiya (Mahaweli Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-01-26 05:00:50 | Thaldena (Mahaweli Ganga) | 0.47 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-01-26 05:00:30 | Thanamalwila (Kirindi Oya) | 0.58 | 🟢 Normal | -0.003 |  |
| 2026-01-26 05:00:26 | Wellawaya (Kirindi Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-01-26 04:58:18 | Padiyathalawa (Maduru Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-01-26 04:53:32 | Holombuwa (Kelani Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-01-26 04:51:38 | Magura (Kalu Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-01-26 04:49:49 | Urawa (Nilwala Ganga) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-01-26 04:48:23 | Putupaula (Kalu Ganga) | 0.73 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-01-26 04:43:17 | Pitabeddara (Nilwala Ganga) | 0.27 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-26 03:11:07 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.62 | 🟢 Normal | 0.277 | 🔺 Rising |
| 2026-01-26 04:48:23 | Putupaula (Kalu Ganga) | 0.73 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-01-26 05:17:45 | Glencourse (Kelani Ganga) | 8.54 | 🟢 Normal | 0.075 | 🔺 Rising |
| 2026-01-26 05:06:37 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.065 | 🔺 Rising |
| 2026-01-25 18:00:27 | Thanthirimale (Malwathu Oya) | 1.80 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-01-26 05:00:50 | Thaldena (Mahaweli Ganga) | 0.47 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-01-26 05:03:32 | Moraketiya (Walawe Ganga) | 0.85 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-01-26 03:00:36 | Thalgahagoda (Nilwala Ganga) | 0.36 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-26 05:04:47 | Giriulla (Maha Oya) | 0.80 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-26 05:00:26 | Wellawaya (Kirindi Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-01-26 05:01:46 | Moragaswewa (Deduru Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-01-26 05:01:08 | Nawalapitiya (Mahaweli Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-01-26 05:02:56 | Horowpothana (Yan Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-01-25 18:04:15 | Galgamuwa (Mee Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-01-26 05:06:08 | Magura (Kalu Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-01-26 05:17:56 | Pitabeddara (Nilwala Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-01-26 05:02:52 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-01-26 05:05:59 | Baddegama (Gin Ganga) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-01-26 05:05:57 | Panadugama (Nilwala Ganga) | 1.97 | 🟢 Normal | 0.000 |  |
| 2026-01-26 05:04:11 | Padiyathalawa (Maduru Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-01-26 05:01:43 | Siyambalanduwa (Heda Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-01-26 05:02:36 | Katharagama (Menik Ganga) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-01-26 02:10:49 | Badalgama (Maha Oya) | 1.86 | 🟢 Normal | 0.000 |  |
| 2026-01-26 04:53:32 | Holombuwa (Kelani Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-01-26 05:02:42 | Manampitiya (Mahaweli Ganga) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-01-26 05:04:43 | Urawa (Nilwala Ganga) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-01-26 05:00:30 | Thanamalwila (Kirindi Oya) | 0.58 | 🟢 Normal | -0.003 |  |
| 2026-01-26 05:04:00 | Dunamale (Aththanagalu Oya) | 0.38 | 🟢 Normal | -0.010 |  |
| 2026-01-26 05:24:25 | Thawalama (Gin Ganga) | 0.96 | 🟢 Normal | -0.010 |  |
| 2026-01-26 05:03:56 | Nakkala (Kumbukkan Oya) | 0.86 | 🟢 Normal | -0.011 |  |
| 2026-01-26 05:01:59 | Kithulgala (Kelani Ganga) | 1.52 | 🟢 Normal | -0.012 |  |
| 2026-01-26 05:02:20 | Yaka Wewa (Ma Oya) | 0.96 | 🟢 Normal | -0.020 |  |
| 2026-01-25 18:01:26 | Weraganthota (Mahaweli Ganga) | -2.35 | 🟢 Normal | -0.020 |  |
| 2026-01-26 05:04:44 | Rathnapura (Kalu Ganga) | 0.75 | 🟢 Normal | -0.021 |  |
| 2026-01-26 05:06:11 | Deraniyagala (Kelani Ganga) | 0.07 | 🟢 Normal | -0.027 |  |
| 2026-01-26 05:04:41 | Hanwella (Kelani Ganga) | 0.29 | 🟢 Normal | -0.040 |  |
| 2026-01-26 05:03:31 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | -0.042 |  |
| 2026-01-26 05:01:41 | Peradeniya (Mahaweli Ganga) | 1.60 | 🟢 Normal | -0.111 |  |
| 2026-01-26 05:04:28 | Ellagawa (Kalu Ganga) | 0.76 | 🟢 Normal | -101.271 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)