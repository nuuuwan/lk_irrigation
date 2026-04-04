# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--04_09:06:11-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **115,793 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-04 09:06:11 | Horowpothana (Yan Oya) | 1.72 | 🟢 Normal | -0.012 |  |
| 2026-04-04 09:05:38 | Badalgama (Maha Oya) | 2.02 | 🟢 Normal | 0.000 |  |
| 2026-04-04 09:05:15 | Urawa (Nilwala Ganga) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-04-04 09:05:03 | Glencourse (Kelani Ganga) | 8.72 | 🟢 Normal | -0.020 |  |
| 2026-04-04 09:04:46 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | -0.009 |  |
| 2026-04-04 09:04:28 | Moragaswewa (Deduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-04-04 09:04:19 | Thanamalwila (Kirindi Oya) | 0.27 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-04 09:04:00 | Panadugama (Nilwala Ganga) | 2.02 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-04-04 09:04:00 | Siyambalanduwa (Heda Oya) | 0.57 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-04 09:03:54 | Kithulgala (Kelani Ganga) | 1.29 | 🟢 Normal | -0.229 |  |
| 2026-04-04 09:03:43 | Giriulla (Maha Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-04-04 09:03:43 | Nagalagam Street (Kelani Ganga) | 0.18 | 🟢 Normal | -0.031 |  |
| 2026-04-04 09:03:34 | Thawalama (Gin Ganga) | 1.70 | 🟢 Normal | -0.041 |  |
| 2026-04-04 09:03:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.23 | 🟢 Normal | -0.010 |  |
| 2026-04-04 09:03:12 | Putupaula (Kalu Ganga) | 0.28 | 🟢 Normal | -0.147 |  |
| 2026-04-04 09:03:03 | Magura (Kalu Ganga) | 1.96 | 🟢 Normal | -0.299 |  |
| 2026-04-04 09:03:00 | Norwood (Kelani Ganga) | 0.47 | 🟢 Normal | -0.021 |  |
| 2026-04-04 09:02:54 | Hanwella (Kelani Ganga) | 0.49 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-04-04 09:02:53 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-04 09:02:42 | Deraniyagala (Kelani Ganga) | 0.33 | 🟢 Normal | 0.130 | 🔺 Rising |
| 2026-04-04 09:02:41 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-04 09:02:39 | Pitabeddara (Nilwala Ganga) | 0.38 | 🟢 Normal | -0.011 |  |
| 2026-04-04 09:02:24 | Manampitiya (Mahaweli Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-04-04 09:02:23 | Manampitiya (Mahaweli Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-04-04 09:01:48 | Ellagawa (Kalu Ganga) | 3.99 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-04 09:01:32 | Thaldena (Mahaweli Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-04-04 09:01:15 | Yaka Wewa (Ma Oya) | 0.64 | 🟢 Normal | -0.010 |  |
| 2026-04-04 09:01:08 | Kuda Oya (Kirindi Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-04-04 09:01:08 | Wellawaya (Kirindi Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-04-04 09:00:45 | Padiyathalawa (Maduru Oya) | 0.62 | 🟢 Normal | 0.169 | 🔺 Rising |
| 2026-04-04 09:00:39 | Thanthirimale (Malwathu Oya) | 2.50 | 🟢 Normal | -0.010 |  |
| 2026-04-04 09:00:24 | Nawalapitiya (Mahaweli Ganga) | 0.50 | 🟢 Normal | -0.010 |  |
| 2026-04-04 09:00:15 | Weraganthota (Mahaweli Ganga) | -1.81 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-04 09:00:13 | Nakkala (Kumbukkan Oya) | 0.78 | 🟢 Normal | -0.010 |  |
| 2026-04-04 08:16:56 | Magura (Kalu Ganga) | 2.19 | 🟢 Normal | -0.299 |  |
| 2026-04-04 08:15:38 | Galgamuwa (Mee Oya) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-04-04 08:14:12 | Urawa (Nilwala Ganga) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-04-04 08:14:09 | Horowpothana (Yan Oya) | 1.73 | 🟢 Normal | -0.012 |  |
| 2026-04-04 08:14:02 | Thalgahagoda (Nilwala Ganga) | 0.38 | 🟢 Normal | -0.054 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-04 09:00:45 | Padiyathalawa (Maduru Oya) | 0.62 | 🟢 Normal | 0.169 | 🔺 Rising |
| 2026-04-04 09:02:42 | Deraniyagala (Kelani Ganga) | 0.33 | 🟢 Normal | 0.130 | 🔺 Rising |
| 2026-04-04 08:03:59 | Baddegama (Gin Ganga) | 1.59 | 🟢 Normal | 0.065 | 🔺 Rising |
| 2026-04-04 09:04:00 | Panadugama (Nilwala Ganga) | 2.02 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-04-04 09:02:54 | Hanwella (Kelani Ganga) | 0.49 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-04-04 08:11:27 | Rathnapura (Kalu Ganga) | 0.88 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-04-04 09:04:00 | Siyambalanduwa (Heda Oya) | 0.57 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-04 09:01:48 | Ellagawa (Kalu Ganga) | 3.99 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-04 09:00:15 | Weraganthota (Mahaweli Ganga) | -1.81 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-04 09:02:41 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-04 09:04:19 | Thanamalwila (Kirindi Oya) | 0.27 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-04 09:01:08 | Wellawaya (Kirindi Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-04-04 09:04:28 | Moragaswewa (Deduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-04-04 09:03:43 | Giriulla (Maha Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-04-04 08:15:38 | Galgamuwa (Mee Oya) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-04-04 09:02:53 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-04 09:01:32 | Thaldena (Mahaweli Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-04-04 09:05:38 | Badalgama (Maha Oya) | 2.02 | 🟢 Normal | 0.000 |  |
| 2026-04-04 09:02:24 | Manampitiya (Mahaweli Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-04-04 08:05:32 | Peradeniya (Mahaweli Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-04-04 09:05:15 | Urawa (Nilwala Ganga) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-04-04 09:01:08 | Kuda Oya (Kirindi Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-04-04 09:04:46 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | -0.009 |  |
| 2026-04-04 09:03:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.23 | 🟢 Normal | -0.010 |  |
| 2026-04-04 09:01:15 | Yaka Wewa (Ma Oya) | 0.64 | 🟢 Normal | -0.010 |  |
| 2026-04-04 09:00:39 | Thanthirimale (Malwathu Oya) | 2.50 | 🟢 Normal | -0.010 |  |
| 2026-04-04 09:00:13 | Nakkala (Kumbukkan Oya) | 0.78 | 🟢 Normal | -0.010 |  |
| 2026-04-04 09:00:24 | Nawalapitiya (Mahaweli Ganga) | 0.50 | 🟢 Normal | -0.010 |  |
| 2026-04-04 08:07:39 | Holombuwa (Kelani Ganga) | 0.32 | 🟢 Normal | -0.010 |  |
| 2026-04-04 09:02:39 | Pitabeddara (Nilwala Ganga) | 0.38 | 🟢 Normal | -0.011 |  |
| 2026-04-04 09:06:11 | Horowpothana (Yan Oya) | 1.72 | 🟢 Normal | -0.012 |  |
| 2026-04-04 09:05:03 | Glencourse (Kelani Ganga) | 8.72 | 🟢 Normal | -0.020 |  |
| 2026-04-04 09:03:00 | Norwood (Kelani Ganga) | 0.47 | 🟢 Normal | -0.021 |  |
| 2026-04-04 09:03:43 | Nagalagam Street (Kelani Ganga) | 0.18 | 🟢 Normal | -0.031 |  |
| 2026-04-04 09:03:34 | Thawalama (Gin Ganga) | 1.70 | 🟢 Normal | -0.041 |  |
| 2026-04-04 08:14:02 | Thalgahagoda (Nilwala Ganga) | 0.38 | 🟢 Normal | -0.054 |  |
| 2026-04-04 09:03:12 | Putupaula (Kalu Ganga) | 0.28 | 🟢 Normal | -0.147 |  |
| 2026-04-04 09:03:54 | Kithulgala (Kelani Ganga) | 1.29 | 🟢 Normal | -0.229 |  |
| 2026-04-04 09:03:03 | Magura (Kalu Ganga) | 1.96 | 🟢 Normal | -0.299 |  |

## River Water Level Charts by Station

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)