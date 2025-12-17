# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--18_04:17:47-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **20,943 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-18 04:17:47 | Putupaula (Kalu Ganga) | 0.95 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2025-12-18 04:16:47 | Thawalama (Gin Ganga) | 1.34 | 🟢 Normal | -0.015 |  |
| 2025-12-18 04:09:37 | Manampitiya (Mahaweli Ganga) | 2.86 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2025-12-18 04:07:21 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | -0.067 |  |
| 2025-12-18 04:06:23 | Nawalapitiya (Mahaweli Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-18 04:06:02 | Urawa (Nilwala Ganga) | 0.44 | 🟢 Normal | -1.059 |  |
| 2025-12-18 04:05:55 | Nawalapitiya (Mahaweli Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-18 04:05:28 | Urawa (Nilwala Ganga) | 0.45 | 🟢 Normal | -1.059 |  |
| 2025-12-18 04:05:25 | Nawalapitiya (Mahaweli Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-18 04:05:11 | Urawa (Nilwala Ganga) | 0.45 | 🟢 Normal | -1.059 |  |
| 2025-12-18 04:04:59 | Moragaswewa (Deduru Oya) | 1.50 | 🟢 Normal | 0.000 |  |
| 2025-12-18 04:04:58 | Peradeniya (Mahaweli Ganga) | 2.51 | 🟢 Normal | -0.040 |  |
| 2025-12-18 04:04:30 | Badalgama (Maha Oya) | 2.32 | 🟢 Normal | 0.000 |  |
| 2025-12-18 04:04:09 | Rathnapura (Kalu Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2025-12-18 04:04:07 | Siyambalanduwa (Heda Oya) | 1.21 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-18 04:03:58 | Baddegama (Gin Ganga) | 1.21 | 🟢 Normal | 72.000 | 🔺 Rising |
| 2025-12-18 04:03:57 | Baddegama (Gin Ganga) | 1.19 | 🟢 Normal | 72.000 | 🔺 Rising |
| 2025-12-18 04:03:55 | Baddegama (Gin Ganga) | 1.18 | 🟢 Normal | 72.000 | 🔺 Rising |
| 2025-12-18 04:03:54 | Baddegama (Gin Ganga) | 1.16 | 🟢 Normal | 72.000 | 🔺 Rising |
| 2025-12-18 04:03:29 | Yaka Wewa (Ma Oya) | 1.29 | 🟢 Normal | -0.022 |  |
| 2025-12-18 04:03:25 | Norwood (Kelani Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2025-12-18 04:03:19 | Thaldena (Mahaweli Ganga) | 1.43 | 🟢 Normal | -0.051 |  |
| 2025-12-18 04:03:10 | Giriulla (Maha Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2025-12-18 04:03:04 | Pitabeddara (Nilwala Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-18 04:02:56 | Nakkala (Kumbukkan Oya) | 2.11 | 🟢 Normal | 0.000 |  |
| 2025-12-18 04:02:47 | Moragaswewa (Deduru Oya) | 1.50 | 🟢 Normal | 0.000 |  |
| 2025-12-18 04:02:35 | Hanwella (Kelani Ganga) | 1.19 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2025-12-18 04:02:24 | Magura (Kalu Ganga) | 1.39 | 🟢 Normal | -0.012 |  |
| 2025-12-18 04:02:21 | Katharagama (Menik Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2025-12-18 04:02:12 | Thanamalwila (Kirindi Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-18 04:02:06 | Horowpothana (Yan Oya) | 3.63 | 🟢 Normal | -2.057 |  |
| 2025-12-18 04:01:45 | Holombuwa (Kelani Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2025-12-18 04:01:44 | Holombuwa (Kelani Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2025-12-18 04:01:25 | Kuda Oya (Kirindi Oya) | 1.45 | 🟢 Normal | 0.000 |  |
| 2025-12-18 04:01:17 | Ellagawa (Kalu Ganga) | 4.70 | 🟢 Normal | 0.000 |  |
| 2025-12-18 04:00:13 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-18 03:44:40 | Panadugama (Nilwala Ganga) | 2.70 | 🟢 Normal | 0.000 |  |
| 2025-12-18 03:37:21 | Thawalama (Gin Ganga) | 1.35 | 🟢 Normal | -0.015 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-18 04:03:58 | Baddegama (Gin Ganga) | 1.21 | 🟢 Normal | 72.000 | 🔺 Rising |
| 2025-12-18 03:03:19 | Thalgahagoda (Nilwala Ganga) | 0.57 | 🟢 Normal | 0.067 | 🔺 Rising |
| 2025-12-18 04:09:37 | Manampitiya (Mahaweli Ganga) | 2.86 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2025-12-17 18:01:03 | Thanthirimale (Malwathu Oya) | 4.15 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2025-12-18 04:02:35 | Hanwella (Kelani Ganga) | 1.19 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2025-12-18 04:17:47 | Putupaula (Kalu Ganga) | 0.95 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2025-12-17 18:04:33 | Galgamuwa (Mee Oya) | 0.63 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2025-12-18 04:04:07 | Siyambalanduwa (Heda Oya) | 1.21 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-18 03:04:44 | Wellawaya (Kirindi Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2025-12-18 04:02:56 | Nakkala (Kumbukkan Oya) | 2.11 | 🟢 Normal | 0.000 |  |
| 2025-12-18 04:04:59 | Moragaswewa (Deduru Oya) | 1.50 | 🟢 Normal | 0.000 |  |
| 2025-12-18 04:06:23 | Nawalapitiya (Mahaweli Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-18 04:03:10 | Giriulla (Maha Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2025-12-18 04:03:04 | Pitabeddara (Nilwala Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-18 04:03:25 | Norwood (Kelani Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2025-12-18 04:01:17 | Ellagawa (Kalu Ganga) | 4.70 | 🟢 Normal | 0.000 |  |
| 2025-12-18 03:44:40 | Panadugama (Nilwala Ganga) | 2.70 | 🟢 Normal | 0.000 |  |
| 2025-12-18 04:00:13 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-18 03:14:04 | Dunamale (Aththanagalu Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2025-12-18 04:02:21 | Katharagama (Menik Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2025-12-18 04:04:30 | Badalgama (Maha Oya) | 2.32 | 🟢 Normal | 0.000 |  |
| 2025-12-18 04:01:45 | Holombuwa (Kelani Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2025-12-18 04:04:09 | Rathnapura (Kalu Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2025-12-18 04:01:25 | Kuda Oya (Kirindi Oya) | 1.45 | 🟢 Normal | 0.000 |  |
| 2025-12-18 04:02:12 | Thanamalwila (Kirindi Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-18 02:02:13 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | -0.005 |  |
| 2025-12-18 04:02:24 | Magura (Kalu Ganga) | 1.39 | 🟢 Normal | -0.012 |  |
| 2025-12-18 04:16:47 | Thawalama (Gin Ganga) | 1.34 | 🟢 Normal | -0.015 |  |
| 2025-12-18 01:05:03 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.74 | 🟢 Normal | -0.019 |  |
| 2025-12-18 04:03:29 | Yaka Wewa (Ma Oya) | 1.29 | 🟢 Normal | -0.022 |  |
| 2025-12-18 03:05:39 | Deraniyagala (Kelani Ganga) | 0.45 | 🟢 Normal | -0.028 |  |
| 2025-12-18 04:04:58 | Peradeniya (Mahaweli Ganga) | 2.51 | 🟢 Normal | -0.040 |  |
| 2025-12-18 04:03:19 | Thaldena (Mahaweli Ganga) | 1.43 | 🟢 Normal | -0.051 |  |
| 2025-12-18 03:07:30 | Glencourse (Kelani Ganga) | 9.45 | 🟢 Normal | -0.054 |  |
| 2025-12-18 04:07:21 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | -0.067 |  |
| 2025-12-17 13:11:29 | Weraganthota (Mahaweli Ganga) | -1.43 | 🟢 Normal | -0.070 |  |
| 2025-12-18 03:04:54 | Padiyathalawa (Maduru Oya) | 3.00 | 🟢 Normal | -0.475 |  |
| 2025-12-18 04:06:02 | Urawa (Nilwala Ganga) | 0.44 | 🟢 Normal | -1.059 |  |
| 2025-12-18 04:02:06 | Horowpothana (Yan Oya) | 3.63 | 🟢 Normal | -2.057 |  |

## River Water Level Charts by Station

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)