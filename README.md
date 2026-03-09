# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--09_11:27:53-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **93,393 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **42** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-09 11:27:53 | Moraketiya (Walawe Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-03-09 11:20:17 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-09 11:19:59 | Dunamale (Aththanagalu Oya) | 0.31 | 🟢 Normal | -0.009 |  |
| 2026-03-09 11:16:47 | Panadugama (Nilwala Ganga) | 2.02 | 🟢 Normal | 0.000 |  |
| 2026-03-09 11:10:43 | Thalgahagoda (Nilwala Ganga) | 0.22 | 🟢 Normal | -0.010 |  |
| 2026-03-09 11:10:38 | Urawa (Nilwala Ganga) | -0.01 | 🟢 Normal | -0.010 |  |
| 2026-03-09 11:10:36 | Ellagawa (Kalu Ganga) | 3.94 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-03-09 11:08:35 | Panadugama (Nilwala Ganga) | 2.02 | 🟢 Normal | 0.000 |  |
| 2026-03-09 11:07:43 | Kuda Oya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-03-09 11:07:27 | Thanamalwila (Kirindi Oya) | 0.36 | 🟢 Normal | -0.009 |  |
| 2026-03-09 11:07:10 | Magura (Kalu Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-09 11:06:25 | Holombuwa (Kelani Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-03-09 11:06:10 | Pitabeddara (Nilwala Ganga) | 0.21 | 🟢 Normal | -0.009 |  |
| 2026-03-09 11:05:29 | Moragaswewa (Deduru Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-09 11:05:24 | Nagalagam Street (Kelani Ganga) | 0.15 | 🟢 Normal | -0.031 |  |
| 2026-03-09 11:05:12 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-09 11:04:55 | Peradeniya (Mahaweli Ganga) | 1.83 | 🟢 Normal | 0.077 | 🔺 Rising |
| 2026-03-09 11:04:47 | Thawalama (Gin Ganga) | 1.05 | 🟢 Normal | -0.042 |  |
| 2026-03-09 11:04:02 | Giriulla (Maha Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-03-09 11:04:01 | Thaldena (Mahaweli Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-03-09 11:03:58 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-09 11:03:50 | Norwood (Kelani Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-03-09 11:03:46 | Deraniyagala (Kelani Ganga) | 0.39 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-03-09 11:03:34 | Hanwella (Kelani Ganga) | 0.40 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-09 11:03:31 | Rathnapura (Kalu Ganga) | 0.82 | 🟢 Normal | -0.088 |  |
| 2026-03-09 11:03:13 | Putupaula (Kalu Ganga) | 0.15 | 🟢 Normal | -0.050 |  |
| 2026-03-09 11:03:06 | Glencourse (Kelani Ganga) | 8.53 | 🟢 Normal | -0.019 |  |
| 2026-03-09 11:02:38 | Badalgama (Maha Oya) | 1.72 | 🟢 Normal | 0.000 |  |
| 2026-03-09 11:02:22 | Nawalapitiya (Mahaweli Ganga) | 0.53 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-03-09 11:02:15 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-09 11:02:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.34 | 🟢 Normal | -0.040 |  |
| 2026-03-09 11:02:06 | Baddegama (Gin Ganga) | 1.11 | 🟢 Normal | -0.010 |  |
| 2026-03-09 11:01:54 | Wellawaya (Kirindi Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-03-09 11:01:46 | Kithulgala (Kelani Ganga) | 1.42 | 🟢 Normal | 0.336 | 🔺 Rising |
| 2026-03-09 11:01:37 | Padiyathalawa (Maduru Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-03-09 11:01:28 | Weraganthota (Mahaweli Ganga) | -2.32 | 🟢 Normal | 0.142 | 🔺 Rising |
| 2026-03-09 11:01:22 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-03-09 11:01:21 | Thanthirimale (Malwathu Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-03-09 11:01:08 | Galgamuwa (Mee Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-09 11:00:59 | Horowpothana (Yan Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-03-09 11:00:15 | Nakkala (Kumbukkan Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-03-09 11:00:11 | Manampitiya (Mahaweli Ganga) | 1.14 | 🟢 Normal | 0.021 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-09 11:01:46 | Kithulgala (Kelani Ganga) | 1.42 | 🟢 Normal | 0.336 | 🔺 Rising |
| 2026-03-09 11:01:28 | Weraganthota (Mahaweli Ganga) | -2.32 | 🟢 Normal | 0.142 | 🔺 Rising |
| 2026-03-09 11:03:46 | Deraniyagala (Kelani Ganga) | 0.39 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-03-09 11:04:55 | Peradeniya (Mahaweli Ganga) | 1.83 | 🟢 Normal | 0.077 | 🔺 Rising |
| 2026-03-09 11:02:22 | Nawalapitiya (Mahaweli Ganga) | 0.53 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-03-09 11:10:36 | Ellagawa (Kalu Ganga) | 3.94 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-03-09 11:00:11 | Manampitiya (Mahaweli Ganga) | 1.14 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-03-09 11:03:34 | Hanwella (Kelani Ganga) | 0.40 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-09 11:01:54 | Wellawaya (Kirindi Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-03-09 11:00:15 | Nakkala (Kumbukkan Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-03-09 11:05:29 | Moragaswewa (Deduru Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-09 11:05:12 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-09 11:04:02 | Giriulla (Maha Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-03-09 11:00:59 | Horowpothana (Yan Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-03-09 11:01:08 | Galgamuwa (Mee Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-09 11:07:10 | Magura (Kalu Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-09 11:03:50 | Norwood (Kelani Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-03-09 11:16:47 | Panadugama (Nilwala Ganga) | 2.02 | 🟢 Normal | 0.000 |  |
| 2026-03-09 11:01:37 | Padiyathalawa (Maduru Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-03-09 11:27:53 | Moraketiya (Walawe Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-03-09 11:01:22 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-03-09 11:04:01 | Thaldena (Mahaweli Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-03-09 11:20:17 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-09 11:02:38 | Badalgama (Maha Oya) | 1.72 | 🟢 Normal | 0.000 |  |
| 2026-03-09 11:06:25 | Holombuwa (Kelani Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-03-09 11:01:21 | Thanthirimale (Malwathu Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-03-09 11:07:43 | Kuda Oya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-03-09 11:19:59 | Dunamale (Aththanagalu Oya) | 0.31 | 🟢 Normal | -0.009 |  |
| 2026-03-09 11:07:27 | Thanamalwila (Kirindi Oya) | 0.36 | 🟢 Normal | -0.009 |  |
| 2026-03-09 11:06:10 | Pitabeddara (Nilwala Ganga) | 0.21 | 🟢 Normal | -0.009 |  |
| 2026-03-09 11:10:43 | Thalgahagoda (Nilwala Ganga) | 0.22 | 🟢 Normal | -0.010 |  |
| 2026-03-09 11:02:06 | Baddegama (Gin Ganga) | 1.11 | 🟢 Normal | -0.010 |  |
| 2026-03-09 11:10:38 | Urawa (Nilwala Ganga) | -0.01 | 🟢 Normal | -0.010 |  |
| 2026-03-09 11:03:06 | Glencourse (Kelani Ganga) | 8.53 | 🟢 Normal | -0.019 |  |
| 2026-03-09 11:05:24 | Nagalagam Street (Kelani Ganga) | 0.15 | 🟢 Normal | -0.031 |  |
| 2026-03-09 11:02:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.34 | 🟢 Normal | -0.040 |  |
| 2026-03-09 11:04:47 | Thawalama (Gin Ganga) | 1.05 | 🟢 Normal | -0.042 |  |
| 2026-03-09 11:03:13 | Putupaula (Kalu Ganga) | 0.15 | 🟢 Normal | -0.050 |  |
| 2026-03-09 11:03:31 | Rathnapura (Kalu Ganga) | 0.82 | 🟢 Normal | -0.088 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)