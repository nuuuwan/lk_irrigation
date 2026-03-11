# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--12_02:30:59-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **94,954 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-12 02:30:59 | Putupaula (Kalu Ganga) | 0.42 | 🟢 Normal | 0.112 | 🔺 Rising |
| 2026-03-12 02:26:56 | Thawalama (Gin Ganga) | 0.77 | 🟢 Normal | -36.000 |  |
| 2026-03-12 02:26:55 | Thawalama (Gin Ganga) | 0.78 | 🟢 Normal | -36.000 |  |
| 2026-03-12 02:26:54 | Thawalama (Gin Ganga) | 0.78 | 🟢 Normal | -36.000 |  |
| 2026-03-12 02:26:52 | Thawalama (Gin Ganga) | 0.78 | 🟢 Normal | -36.000 |  |
| 2026-03-12 02:26:51 | Thawalama (Gin Ganga) | 0.79 | 🟢 Normal | -36.000 |  |
| 2026-03-12 02:17:48 | Manampitiya (Mahaweli Ganga) | 0.65 | 🟢 Normal | -0.004 |  |
| 2026-03-12 02:10:28 | Thalgahagoda (Nilwala Ganga) | 0.24 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-03-12 02:09:27 | Holombuwa (Kelani Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-03-12 02:07:39 | Padiyathalawa (Maduru Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-03-12 02:06:41 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-03-12 02:06:02 | Pitabeddara (Nilwala Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-03-12 02:05:04 | Kuda Oya (Kirindi Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-03-12 02:05:03 | Rathnapura (Kalu Ganga) | 0.38 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-12 02:04:49 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | 0.094 | 🔺 Rising |
| 2026-03-12 02:04:21 | Thanamalwila (Kirindi Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-03-12 02:04:15 | Giriulla (Maha Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-03-12 02:04:09 | Norwood (Kelani Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-03-12 02:03:52 | Thaldena (Mahaweli Ganga) | 0.36 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-03-12 02:03:08 | Panadugama (Nilwala Ganga) | 1.86 | 🟢 Normal | 0.000 |  |
| 2026-03-12 02:03:03 | Glencourse (Kelani Ganga) | 8.40 | 🟢 Normal | 0.000 |  |
| 2026-03-12 02:02:50 | Baddegama (Gin Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-03-12 02:02:48 | Dunamale (Aththanagalu Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-03-12 02:02:43 | Moragaswewa (Deduru Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-12 02:02:36 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-03-12 02:01:52 | Ellagawa (Kalu Ganga) | 3.76 | 🟢 Normal | 0.000 |  |
| 2026-03-12 02:01:19 | Deraniyagala (Kelani Ganga) | 0.11 | 🟢 Normal | -0.021 |  |
| 2026-03-12 02:01:16 | Nawalapitiya (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-03-12 02:01:15 | Badalgama (Maha Oya) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-03-12 02:01:01 | Nakkala (Kumbukkan Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-03-12 02:00:54 | Kithulgala (Kelani Ganga) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-03-12 02:00:50 | Moraketiya (Walawe Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-03-12 01:59:24 | Glencourse (Kelani Ganga) | 8.40 | 🟢 Normal | 0.000 |  |
| 2026-03-12 01:45:55 | Nakkala (Kumbukkan Oya) | 0.75 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-12 02:30:59 | Putupaula (Kalu Ganga) | 0.42 | 🟢 Normal | 0.112 | 🔺 Rising |
| 2026-03-12 02:04:49 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | 0.094 | 🔺 Rising |
| 2026-03-12 02:10:28 | Thalgahagoda (Nilwala Ganga) | 0.24 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-03-12 01:03:25 | Urawa (Nilwala Ganga) | 0.21 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-03-12 02:05:03 | Rathnapura (Kalu Ganga) | 0.38 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-12 02:03:52 | Thaldena (Mahaweli Ganga) | 0.36 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-03-12 02:00:54 | Kithulgala (Kelani Ganga) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-03-12 00:07:51 | Wellawaya (Kirindi Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-03-12 02:01:01 | Nakkala (Kumbukkan Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-03-12 02:02:43 | Moragaswewa (Deduru Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-12 02:01:16 | Nawalapitiya (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-03-12 00:04:12 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-12 02:04:15 | Giriulla (Maha Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-03-11 23:22:30 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-03-10 18:02:23⌛ | Galgamuwa (Mee Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-12 01:11:17 | Magura (Kalu Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-03-12 02:06:02 | Pitabeddara (Nilwala Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-03-12 02:04:09 | Norwood (Kelani Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-03-12 02:01:52 | Ellagawa (Kalu Ganga) | 3.76 | 🟢 Normal | 0.000 |  |
| 2026-03-12 02:02:50 | Baddegama (Gin Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-03-12 02:03:08 | Panadugama (Nilwala Ganga) | 1.86 | 🟢 Normal | 0.000 |  |
| 2026-03-12 02:07:39 | Padiyathalawa (Maduru Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-03-12 02:03:03 | Glencourse (Kelani Ganga) | 8.40 | 🟢 Normal | 0.000 |  |
| 2026-03-12 02:00:50 | Moraketiya (Walawe Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-03-12 02:02:36 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-03-12 02:02:48 | Dunamale (Aththanagalu Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-03-12 02:06:41 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-03-12 02:01:15 | Badalgama (Maha Oya) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-03-12 02:09:27 | Holombuwa (Kelani Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-03-10 18:00:47⌛ | Thanthirimale (Malwathu Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-03-12 02:05:04 | Kuda Oya (Kirindi Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-03-12 02:04:21 | Thanamalwila (Kirindi Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-03-11 21:05:07 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-03-12 02:17:48 | Manampitiya (Mahaweli Ganga) | 0.65 | 🟢 Normal | -0.004 |  |
| 2026-03-12 01:04:16 | Hanwella (Kelani Ganga) | 0.43 | 🟢 Normal | -0.019 |  |
| 2026-03-12 02:01:19 | Deraniyagala (Kelani Ganga) | 0.11 | 🟢 Normal | -0.021 |  |
| 2026-03-10 18:02:53⌛ | Weraganthota (Mahaweli Ganga) | -2.89 | 🟢 Normal | -0.088 |  |
| 2026-03-12 01:00:44 | Peradeniya (Mahaweli Ganga) | 1.71 | 🟢 Normal | -0.231 |  |
| 2026-03-12 02:26:56 | Thawalama (Gin Ganga) | 0.77 | 🟢 Normal | -36.000 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

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

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)