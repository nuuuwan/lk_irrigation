# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--11_01:09:04-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **14,580 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **21** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-11 01:09:04 | Pitabeddara (Nilwala Ganga) | 0.95 | 🟢 Normal | -0.009 |  |
| 2025-12-11 01:08:44 | Baddegama (Gin Ganga) | 1.46 | 🟢 Normal | -0.019 |  |
| 2025-12-11 01:07:25 | Giriulla (Maha Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2025-12-11 01:05:29 | Thalgahagoda (Nilwala Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2025-12-11 01:05:14 | Rathnapura (Kalu Ganga) | 1.59 | 🟢 Normal | -0.010 |  |
| 2025-12-11 01:04:54 | Katharagama (Menik Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2025-12-11 01:04:18 | Deraniyagala (Kelani Ganga) | 0.62 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2025-12-11 01:03:40 | Siyambalanduwa (Heda Oya) | 0.83 | 🟢 Normal | -0.010 |  |
| 2025-12-11 01:03:16 | Norwood (Kelani Ganga) | 0.81 | 🟢 Normal | -0.010 |  |
| 2025-12-11 01:03:14 | Urawa (Nilwala Ganga) | 0.62 | 🟢 Normal | -0.010 |  |
| 2025-12-11 01:03:14 | Ellagawa (Kalu Ganga) | 5.09 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-11 01:03:14 | Thawalama (Gin Ganga) | 1.72 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2025-12-11 01:03:00 | Nakkala (Kumbukkan Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2025-12-11 01:02:57 | Moraketiya (Walawe Ganga) | 1.01 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-11 01:02:56 | Padiyathalawa (Maduru Oya) | 0.91 | 🟢 Normal | -0.011 |  |
| 2025-12-11 01:02:11 | Badalgama (Maha Oya) | 2.58 | 🟢 Normal | -0.012 |  |
| 2025-12-11 01:02:10 | Glencourse (Kelani Ganga) | 9.85 | 🟢 Normal | 0.108 | 🔺 Rising |
| 2025-12-11 01:02:04 | Yaka Wewa (Ma Oya) | 1.53 | 🟢 Normal | 0.000 |  |
| 2025-12-11 01:01:16 | Nawalapitiya (Mahaweli Ganga) | 1.15 | 🟢 Normal | -0.010 |  |
| 2025-12-11 01:00:46 | Horowpothana (Yan Oya) | 5.10 | 🟢 Normal | -0.031 |  |
| 2025-12-11 01:00:20 | Wellawaya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-11-28 06:04:09⌛ | Moragaswewa (Deduru Oya) | 8.33 | 🔴 Major Flood | 0.051 | 🔺 Rising |
| 2025-12-11 00:15:35 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.10 | 🟢 Normal | 0.113 | 🔺 Rising |
| 2025-12-11 01:02:10 | Glencourse (Kelani Ganga) | 9.85 | 🟢 Normal | 0.108 | 🔺 Rising |
| 2025-12-11 00:14:59 | Magura (Kalu Ganga) | 2.25 | 🟢 Normal | 0.076 | 🔺 Rising |
| 2025-12-11 01:03:14 | Thawalama (Gin Ganga) | 1.72 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2025-12-11 01:04:18 | Deraniyagala (Kelani Ganga) | 0.62 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2025-12-10 18:02:01 | Thanthirimale (Malwathu Oya) | 3.88 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-11 01:03:14 | Ellagawa (Kalu Ganga) | 5.09 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-10 18:04:22 | Galgamuwa (Mee Oya) | 0.83 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2025-12-11 01:02:57 | Moraketiya (Walawe Ganga) | 1.01 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-11 00:10:16 | Kithulgala (Kelani Ganga) | 1.82 | 🟢 Normal | 0.000 |  |
| 2025-12-11 01:00:20 | Wellawaya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2025-12-11 01:03:00 | Nakkala (Kumbukkan Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2025-12-11 01:02:04 | Yaka Wewa (Ma Oya) | 1.53 | 🟢 Normal | 0.000 |  |
| 2025-12-11 01:07:25 | Giriulla (Maha Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2025-12-11 00:03:14 | Hanwella (Kelani Ganga) | 1.77 | 🟢 Normal | 0.000 |  |
| 2025-12-11 00:03:44 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2025-12-11 00:02:19 | Dunamale (Aththanagalu Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2025-12-11 00:03:20 | Thaldena (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-11 01:04:54 | Katharagama (Menik Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2025-12-10 21:09:04 | Manampitiya (Mahaweli Ganga) | 2.58 | 🟢 Normal | 0.000 |  |
| 2025-12-10 18:00:11 | Peradeniya (Mahaweli Ganga) | 2.58 | 🟢 Normal | 0.000 |  |
| 2025-12-11 01:05:29 | Thalgahagoda (Nilwala Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2025-12-11 00:08:14 | Kuda Oya (Kirindi Oya) | 1.50 | 🟢 Normal | 0.000 |  |
| 2025-12-11 00:07:02 | Thanamalwila (Kirindi Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2025-12-11 01:09:04 | Pitabeddara (Nilwala Ganga) | 0.95 | 🟢 Normal | -0.009 |  |
| 2025-12-11 01:03:40 | Siyambalanduwa (Heda Oya) | 0.83 | 🟢 Normal | -0.010 |  |
| 2025-12-11 00:03:12 | Holombuwa (Kelani Ganga) | 0.72 | 🟢 Normal | -0.010 |  |
| 2025-12-11 01:03:14 | Urawa (Nilwala Ganga) | 0.62 | 🟢 Normal | -0.010 |  |
| 2025-12-11 01:03:16 | Norwood (Kelani Ganga) | 0.81 | 🟢 Normal | -0.010 |  |
| 2025-12-11 01:05:14 | Rathnapura (Kalu Ganga) | 1.59 | 🟢 Normal | -0.010 |  |
| 2025-12-11 01:01:16 | Nawalapitiya (Mahaweli Ganga) | 1.15 | 🟢 Normal | -0.010 |  |
| 2025-12-11 01:02:56 | Padiyathalawa (Maduru Oya) | 0.91 | 🟢 Normal | -0.011 |  |
| 2025-12-11 01:02:11 | Badalgama (Maha Oya) | 2.58 | 🟢 Normal | -0.012 |  |
| 2025-12-11 01:08:44 | Baddegama (Gin Ganga) | 1.46 | 🟢 Normal | -0.019 |  |
| 2025-12-11 01:00:46 | Horowpothana (Yan Oya) | 5.10 | 🟢 Normal | -0.031 |  |
| 2025-12-11 00:12:32 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | -0.081 |  |
| 2025-12-11 00:02:59 | Panadugama (Nilwala Ganga) | 3.27 | 🟢 Normal | -0.099 |  |
| 2025-12-10 17:02:38 | Weraganthota (Mahaweli Ganga) | -1.40 | 🟢 Normal | -0.337 |  |

## River Water Level Charts by Station

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

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

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)