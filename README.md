# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--30_12:25:43-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **111,432 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-30 12:25:43 | Nakkala (Kumbukkan Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-03-30 12:12:11 | Panadugama (Nilwala Ganga) | 2.01 | 🟢 Normal | 0.000 |  |
| 2026-03-30 12:09:14 | Magura (Kalu Ganga) | 0.64 | 🟢 Normal | -0.010 |  |
| 2026-03-30 12:08:23 | Thalgahagoda (Nilwala Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-03-30 12:07:20 | Thawalama (Gin Ganga) | 1.05 | 🟢 Normal | -0.137 |  |
| 2026-03-30 12:06:59 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.086 | 🔺 Rising |
| 2026-03-30 12:05:56 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-03-30 12:05:19 | Urawa (Nilwala Ganga) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-30 12:04:54 | Badalgama (Maha Oya) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-03-30 12:04:44 | Galgamuwa (Mee Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-03-30 12:04:22 | Baddegama (Gin Ganga) | 1.22 | 🟢 Normal | -0.031 |  |
| 2026-03-30 12:04:21 | Giriulla (Maha Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-03-30 12:04:07 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | -0.010 |  |
| 2026-03-30 12:04:04 | Holombuwa (Kelani Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-03-30 12:03:59 | Padiyathalawa (Maduru Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-03-30 12:03:46 | Ellagawa (Kalu Ganga) | 3.68 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-03-30 12:03:37 | Glencourse (Kelani Ganga) | 8.33 | 🟢 Normal | -0.043 |  |
| 2026-03-30 12:03:23 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-03-30 12:03:07 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-03-30 12:02:57 | Wellawaya (Kirindi Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-30 12:02:55 | Hanwella (Kelani Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-03-30 12:02:51 | Putupaula (Kalu Ganga) | 0.67 | 🟢 Normal | 0.127 | 🔺 Rising |
| 2026-03-30 12:02:50 | Deraniyagala (Kelani Ganga) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-03-30 12:02:49 | Rathnapura (Kalu Ganga) | 0.42 | 🟢 Normal | -0.020 |  |
| 2026-03-30 12:02:40 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-03-30 12:02:27 | Manampitiya (Mahaweli Ganga) | 0.22 | 🟢 Normal | -0.034 |  |
| 2026-03-30 12:02:21 | Peradeniya (Mahaweli Ganga) | 1.25 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-03-30 12:02:16 | Moragaswewa (Deduru Oya) | -0.23 | 🟢 Normal | -0.011 |  |
| 2026-03-30 12:02:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.28 | 🟢 Normal | -0.020 |  |
| 2026-03-30 12:01:58 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-03-30 12:01:53 | Weraganthota (Mahaweli Ganga) | -2.27 | 🟢 Normal | -0.228 |  |
| 2026-03-30 12:01:53 | Thanamalwila (Kirindi Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-03-30 12:01:49 | Pitabeddara (Nilwala Ganga) | 0.30 | 🟢 Normal | -0.076 |  |
| 2026-03-30 12:01:48 | Horowpothana (Yan Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-03-30 12:01:48 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-30 12:01:24 | Thaldena (Mahaweli Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-30 12:00:47 | Thanthirimale (Malwathu Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-03-30 12:00:14 | Kuda Oya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-03-30 12:00:11 | Nawalapitiya (Mahaweli Ganga) | 0.47 | 🟢 Normal | 0.010 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-30 12:02:51 | Putupaula (Kalu Ganga) | 0.67 | 🟢 Normal | 0.127 | 🔺 Rising |
| 2026-03-30 12:06:59 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.086 | 🔺 Rising |
| 2026-03-30 12:02:21 | Peradeniya (Mahaweli Ganga) | 1.25 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-03-30 12:03:46 | Ellagawa (Kalu Ganga) | 3.68 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-03-30 12:00:11 | Nawalapitiya (Mahaweli Ganga) | 0.47 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-30 12:05:56 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-03-30 12:02:57 | Wellawaya (Kirindi Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-30 12:25:43 | Nakkala (Kumbukkan Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-03-30 12:01:48 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-30 12:04:21 | Giriulla (Maha Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-03-30 12:01:48 | Horowpothana (Yan Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-03-30 12:04:44 | Galgamuwa (Mee Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-03-30 12:02:55 | Hanwella (Kelani Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-03-30 12:02:50 | Deraniyagala (Kelani Ganga) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-03-30 12:12:11 | Panadugama (Nilwala Ganga) | 2.01 | 🟢 Normal | 0.000 |  |
| 2026-03-30 12:03:59 | Padiyathalawa (Maduru Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-03-30 12:02:40 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-03-30 12:03:23 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-03-30 12:01:58 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-03-30 12:01:24 | Thaldena (Mahaweli Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-30 12:03:07 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-03-30 12:04:54 | Badalgama (Maha Oya) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-03-30 12:04:04 | Holombuwa (Kelani Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-03-30 12:00:47 | Thanthirimale (Malwathu Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-03-30 12:05:19 | Urawa (Nilwala Ganga) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-30 12:08:23 | Thalgahagoda (Nilwala Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-03-30 12:00:14 | Kuda Oya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-03-30 12:01:53 | Thanamalwila (Kirindi Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-03-30 12:09:14 | Magura (Kalu Ganga) | 0.64 | 🟢 Normal | -0.010 |  |
| 2026-03-30 12:04:07 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | -0.010 |  |
| 2026-03-30 12:02:16 | Moragaswewa (Deduru Oya) | -0.23 | 🟢 Normal | -0.011 |  |
| 2026-03-30 12:02:49 | Rathnapura (Kalu Ganga) | 0.42 | 🟢 Normal | -0.020 |  |
| 2026-03-30 12:02:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.28 | 🟢 Normal | -0.020 |  |
| 2026-03-30 12:04:22 | Baddegama (Gin Ganga) | 1.22 | 🟢 Normal | -0.031 |  |
| 2026-03-30 12:02:27 | Manampitiya (Mahaweli Ganga) | 0.22 | 🟢 Normal | -0.034 |  |
| 2026-03-30 12:03:37 | Glencourse (Kelani Ganga) | 8.33 | 🟢 Normal | -0.043 |  |
| 2026-03-30 12:01:49 | Pitabeddara (Nilwala Ganga) | 0.30 | 🟢 Normal | -0.076 |  |
| 2026-03-30 12:07:20 | Thawalama (Gin Ganga) | 1.05 | 🟢 Normal | -0.137 |  |
| 2026-03-30 12:01:53 | Weraganthota (Mahaweli Ganga) | -2.27 | 🟢 Normal | -0.228 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

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

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)