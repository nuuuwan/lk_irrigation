# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--04_15:00:09-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **197,091 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **7** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-04 15:00:09 | Thalgahagoda (Nilwala Ganga) | 0.23 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-07-04 14:28:40 | Panadugama (Nilwala Ganga) | 2.39 | 🟢 Normal | 0.000 |  |
| 2026-07-04 14:27:58 | Pitabeddara (Nilwala Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-07-04 14:25:58 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-07-04 14:22:17 | Urawa (Nilwala Ganga) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-04 14:21:49 | Magura (Kalu Ganga) | 1.25 | 🟢 Normal | -0.008 |  |
| 2026-07-04 14:12:46 | Baddegama (Gin Ganga) | 1.16 | 🟢 Normal | -0.019 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-04 14:08:50 | Holombuwa (Kelani Ganga) | 1.31 | 🟢 Normal | 0.212 | 🔺 Rising |
| 2026-07-04 14:05:17 | Peradeniya (Mahaweli Ganga) | 2.30 | 🟢 Normal | 0.200 | 🔺 Rising |
| 2026-07-04 14:04:23 | Hanwella (Kelani Ganga) | 2.26 | 🟢 Normal | 0.157 | 🔺 Rising |
| 2026-07-04 14:06:22 | Glencourse (Kelani Ganga) | 11.28 | 🟢 Normal | 0.127 | 🔺 Rising |
| 2026-07-04 14:04:15 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.121 | 🔺 Rising |
| 2026-07-04 14:02:26 | Putupaula (Kalu Ganga) | 0.56 | 🟢 Normal | 0.119 | 🔺 Rising |
| 2026-07-04 14:02:50 | Ellagawa (Kalu Ganga) | 5.50 | 🟢 Normal | 0.088 | 🔺 Rising |
| 2026-07-04 15:00:09 | Thalgahagoda (Nilwala Ganga) | 0.23 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-07-04 14:08:15 | Dunamale (Aththanagalu Oya) | 1.64 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-07-04 14:09:28 | Giriulla (Maha Oya) | 1.12 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-07-04 14:02:38 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.37 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-04 14:00:47 | Thanthirimale (Malwathu Oya) | 1.28 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-04 14:10:16 | Badalgama (Maha Oya) | 2.14 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-04 14:02:51 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-07-04 14:02:25 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-07-04 14:07:06 | Moragaswewa (Deduru Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-07-04 14:25:58 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-07-04 14:00:44 | Horowpothana (Yan Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-07-04 14:03:30 | Galgamuwa (Mee Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-07-04 14:27:58 | Pitabeddara (Nilwala Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-07-04 14:28:40 | Panadugama (Nilwala Ganga) | 2.39 | 🟢 Normal | 0.000 |  |
| 2026-07-04 14:01:15 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-07-04 14:01:10 | Moraketiya (Walawe Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-07-04 14:03:31 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-07-04 14:01:32 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-07-04 14:22:17 | Urawa (Nilwala Ganga) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-04 14:01:44 | Kuda Oya (Kirindi Oya) | 1.10 | 🟢 Normal | -0.005 |  |
| 2026-07-04 14:21:49 | Magura (Kalu Ganga) | 1.25 | 🟢 Normal | -0.008 |  |
| 2026-07-04 14:09:47 | Weraganthota (Mahaweli Ganga) | -3.41 | 🟢 Normal | -0.009 |  |
| 2026-07-04 14:04:15 | Thanamalwila (Kirindi Oya) | 0.32 | 🟢 Normal | -0.010 |  |
| 2026-07-04 14:01:44 | Thaldena (Mahaweli Ganga) | 0.12 | 🟢 Normal | -0.010 |  |
| 2026-07-04 14:01:24 | Manampitiya (Mahaweli Ganga) | -0.17 | 🟢 Normal | -0.010 |  |
| 2026-07-04 14:12:46 | Baddegama (Gin Ganga) | 1.16 | 🟢 Normal | -0.019 |  |
| 2026-07-04 14:05:47 | Norwood (Kelani Ganga) | 0.70 | 🟢 Normal | -0.020 |  |
| 2026-07-04 14:06:21 | Thawalama (Gin Ganga) | 1.37 | 🟢 Normal | -0.022 |  |
| 2026-07-04 14:02:37 | Deraniyagala (Kelani Ganga) | 1.30 | 🟢 Normal | -0.040 |  |
| 2026-07-04 14:03:55 | Nawalapitiya (Mahaweli Ganga) | 1.87 | 🟢 Normal | -0.080 |  |
| 2026-07-04 14:04:47 | Rathnapura (Kalu Ganga) | 2.51 | 🟢 Normal | -0.088 |  |
| 2026-07-04 14:05:15 | Kithulgala (Kelani Ganga) | 1.73 | 🟢 Normal | -0.136 |  |

## River Water Level Charts by Station

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

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

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)