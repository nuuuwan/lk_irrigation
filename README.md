# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--05_04:26:22-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **197,595 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **32** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-05 04:26:22 | Rathnapura (Kalu Ganga) | 1.80 | 🟢 Normal | -0.043 |  |
| 2026-07-05 04:26:17 | Magura (Kalu Ganga) | 1.32 | 🟢 Normal | -0.020 |  |
| 2026-07-05 04:24:44 | Dunamale (Aththanagalu Oya) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-07-05 04:22:44 | Moraketiya (Walawe Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-07-05 04:19:52 | Putupaula (Kalu Ganga) | 0.78 | 🟢 Normal | 0.125 | 🔺 Rising |
| 2026-07-05 04:18:47 | Dunamale (Aththanagalu Oya) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-07-05 04:18:07 | Thawalama (Gin Ganga) | 1.51 | 🟢 Normal | 0.000 |  |
| 2026-07-05 04:13:10 | Ellagawa (Kalu Ganga) | 5.87 | 🟢 Normal | -0.026 |  |
| 2026-07-05 04:12:46 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-07-05 04:09:00 | Thalgahagoda (Nilwala Ganga) | 0.14 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-07-05 04:08:16 | Baddegama (Gin Ganga) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-07-05 04:07:21 | Holombuwa (Kelani Ganga) | 1.08 | 🟢 Normal | -0.126 |  |
| 2026-07-05 04:05:51 | Pitabeddara (Nilwala Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-07-05 04:05:51 | Hanwella (Kelani Ganga) | 3.30 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-07-05 04:04:06 | Giriulla (Maha Oya) | 2.08 | 🟢 Normal | -0.020 |  |
| 2026-07-05 04:03:44 | Urawa (Nilwala Ganga) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-05 04:03:01 | Peradeniya (Mahaweli Ganga) | 2.60 | 🟢 Normal | -0.166 |  |
| 2026-07-05 04:02:55 | Badalgama (Maha Oya) | 3.14 | 🟢 Normal | 0.185 | 🔺 Rising |
| 2026-07-05 04:02:53 | Kithulgala (Kelani Ganga) | 1.82 | 🟢 Normal | -0.056 |  |
| 2026-07-05 04:02:50 | Deraniyagala (Kelani Ganga) | 1.24 | 🟢 Normal | -0.020 |  |
| 2026-07-05 04:02:44 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-07-05 04:02:43 | Norwood (Kelani Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-07-05 04:02:00 | Moragaswewa (Deduru Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-07-05 04:01:45 | Manampitiya (Mahaweli Ganga) | -0.15 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-05 04:01:32 | Nawalapitiya (Mahaweli Ganga) | 1.83 | 🟢 Normal | -0.070 |  |
| 2026-07-05 04:01:16 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | 0.000 |  |
| 2026-07-05 04:01:15 | Thaldena (Mahaweli Ganga) | 0.16 | 🟢 Normal | -0.011 |  |
| 2026-07-05 04:01:10 | Kuda Oya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-07-05 04:01:05 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-07-05 04:00:45 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-07-05 03:56:18 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-07-05 03:55:43 | Magura (Kalu Ganga) | 1.33 | 🟢 Normal | -0.020 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-05 04:02:55 | Badalgama (Maha Oya) | 3.14 | 🟢 Normal | 0.185 | 🔺 Rising |
| 2026-07-05 04:19:52 | Putupaula (Kalu Ganga) | 0.78 | 🟢 Normal | 0.125 | 🔺 Rising |
| 2026-07-05 04:09:00 | Thalgahagoda (Nilwala Ganga) | 0.14 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-07-05 04:05:51 | Hanwella (Kelani Ganga) | 3.30 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-07-05 04:02:44 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-07-04 23:01:40 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.48 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-07-05 04:01:45 | Manampitiya (Mahaweli Ganga) | -0.15 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-04 18:00:43 | Weraganthota (Mahaweli Ganga) | -3.41 | 🟢 Normal | 0.000 |  |
| 2026-07-05 04:01:05 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-07-05 04:00:45 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-07-05 04:02:00 | Moragaswewa (Deduru Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-07-05 02:03:47 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-07-05 04:12:46 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-07-04 18:04:06 | Galgamuwa (Mee Oya) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-07-05 04:05:51 | Pitabeddara (Nilwala Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-07-05 04:02:43 | Norwood (Kelani Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-07-05 04:08:16 | Baddegama (Gin Ganga) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-07-05 03:05:20 | Panadugama (Nilwala Ganga) | 2.39 | 🟢 Normal | 0.000 |  |
| 2026-07-05 03:04:17 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-07-05 04:22:44 | Moraketiya (Walawe Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-07-05 03:02:46 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-07-05 04:24:44 | Dunamale (Aththanagalu Oya) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-07-05 04:01:16 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | 0.000 |  |
| 2026-07-04 18:00:35 | Thanthirimale (Malwathu Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-07-05 04:18:07 | Thawalama (Gin Ganga) | 1.51 | 🟢 Normal | 0.000 |  |
| 2026-07-05 04:03:44 | Urawa (Nilwala Ganga) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-05 04:01:10 | Kuda Oya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-07-05 03:03:13 | Thanamalwila (Kirindi Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-07-05 04:01:15 | Thaldena (Mahaweli Ganga) | 0.16 | 🟢 Normal | -0.011 |  |
| 2026-07-05 03:07:40 | Glencourse (Kelani Ganga) | 11.69 | 🟢 Normal | -0.019 |  |
| 2026-07-05 04:26:17 | Magura (Kalu Ganga) | 1.32 | 🟢 Normal | -0.020 |  |
| 2026-07-05 04:04:06 | Giriulla (Maha Oya) | 2.08 | 🟢 Normal | -0.020 |  |
| 2026-07-05 04:02:50 | Deraniyagala (Kelani Ganga) | 1.24 | 🟢 Normal | -0.020 |  |
| 2026-07-05 04:13:10 | Ellagawa (Kalu Ganga) | 5.87 | 🟢 Normal | -0.026 |  |
| 2026-07-05 04:26:22 | Rathnapura (Kalu Ganga) | 1.80 | 🟢 Normal | -0.043 |  |
| 2026-07-05 04:02:53 | Kithulgala (Kelani Ganga) | 1.82 | 🟢 Normal | -0.056 |  |
| 2026-07-05 04:01:32 | Nawalapitiya (Mahaweli Ganga) | 1.83 | 🟢 Normal | -0.070 |  |
| 2026-07-05 04:07:21 | Holombuwa (Kelani Ganga) | 1.08 | 🟢 Normal | -0.126 |  |
| 2026-07-05 04:03:01 | Peradeniya (Mahaweli Ganga) | 2.60 | 🟢 Normal | -0.166 |  |

## River Water Level Charts by Station

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

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

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)