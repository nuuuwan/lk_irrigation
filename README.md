# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--21_15:07:07-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **103,489 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **42** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-21 15:07:07 | Rathnapura (Kalu Ganga) | 0.55 | 🟢 Normal | -0.012 |  |
| 2026-03-21 15:06:37 | Padiyathalawa (Maduru Oya) | 0.41 | 🟢 Normal | -0.009 |  |
| 2026-03-21 15:05:30 | Holombuwa (Kelani Ganga) | 0.23 | 🟢 Normal | -0.010 |  |
| 2026-03-21 15:05:23 | Galgamuwa (Mee Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-21 15:05:10 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-03-21 15:04:41 | Manampitiya (Mahaweli Ganga) | 0.50 | 🟢 Normal | -0.047 |  |
| 2026-03-21 15:04:09 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | -0.009 |  |
| 2026-03-21 15:04:02 | Wellawaya (Kirindi Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-03-21 15:03:55 | Deraniyagala (Kelani Ganga) | 0.21 | 🟢 Normal | -0.068 |  |
| 2026-03-21 15:03:54 | Magura (Kalu Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-03-21 15:03:39 | Pitabeddara (Nilwala Ganga) | 0.31 | 🟢 Normal | -0.015 |  |
| 2026-03-21 15:03:16 | Panadugama (Nilwala Ganga) | 2.02 | 🟢 Normal | 0.000 |  |
| 2026-03-21 15:03:07 | Peradeniya (Mahaweli Ganga) | 1.08 | 🟢 Normal | -0.118 |  |
| 2026-03-21 15:02:51 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-03-21 15:02:48 | Hanwella (Kelani Ganga) | 0.40 | 🟢 Normal | -0.010 |  |
| 2026-03-21 15:02:47 | Baddegama (Gin Ganga) | 1.15 | 🟢 Normal | -0.064 |  |
| 2026-03-21 15:02:33 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.36 | 🟢 Normal | -0.030 |  |
| 2026-03-21 15:02:33 | Putupaula (Kalu Ganga) | 0.80 | 🟢 Normal | 0.206 | 🔺 Rising |
| 2026-03-21 15:02:29 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-21 15:02:27 | Giriulla (Maha Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-03-21 15:02:24 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-03-21 15:02:12 | Thanamalwila (Kirindi Oya) | 0.60 | 🟢 Normal | -0.020 |  |
| 2026-03-21 15:02:09 | Glencourse (Kelani Ganga) | 8.43 | 🟢 Normal | 0.131 | 🔺 Rising |
| 2026-03-21 15:02:02 | Thaldena (Mahaweli Ganga) | 0.36 | 🟢 Normal | -0.022 |  |
| 2026-03-21 15:01:55 | Kithulgala (Kelani Ganga) | 1.39 | 🟢 Normal | -0.010 |  |
| 2026-03-21 15:01:54 | Weraganthota (Mahaweli Ganga) | -2.65 | 🟢 Normal | -0.079 |  |
| 2026-03-21 15:01:53 | Moraketiya (Walawe Ganga) | 0.82 | 🟢 Normal | -0.018 |  |
| 2026-03-21 15:01:53 | Thawalama (Gin Ganga) | 1.38 | 🟢 Normal | -0.032 |  |
| 2026-03-21 15:01:51 | Thanthirimale (Malwathu Oya) | 1.35 | 🟢 Normal | -0.010 |  |
| 2026-03-21 15:01:49 | Badalgama (Maha Oya) | 1.86 | 🟢 Normal | 0.000 |  |
| 2026-03-21 15:01:42 | Nawalapitiya (Mahaweli Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-21 15:01:42 | Norwood (Kelani Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-03-21 15:01:29 | Kuda Oya (Kirindi Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-03-21 15:01:12 | Ellagawa (Kalu Ganga) | 3.98 | 🟢 Normal | 0.000 |  |
| 2026-03-21 15:01:07 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-03-21 15:01:00 | Nakkala (Kumbukkan Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-03-21 15:00:45 | Dunamale (Aththanagalu Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-03-21 14:28:00 | Moraketiya (Walawe Ganga) | 0.83 | 🟢 Normal | -0.018 |  |
| 2026-03-21 14:23:25 | Pitabeddara (Nilwala Ganga) | 0.32 | 🟢 Normal | -0.015 |  |
| 2026-03-21 14:19:14 | Moraketiya (Walawe Ganga) | 0.83 | 🟢 Normal | -0.018 |  |
| 2026-03-21 14:18:20 | Rathnapura (Kalu Ganga) | 0.56 | 🟢 Normal | -0.012 |  |
| 2026-03-21 14:18:19 | Moraketiya (Walawe Ganga) | 0.83 | 🟢 Normal | -0.018 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-21 15:02:33 | Putupaula (Kalu Ganga) | 0.80 | 🟢 Normal | 0.206 | 🔺 Rising |
| 2026-03-21 14:03:57 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.162 | 🔺 Rising |
| 2026-03-21 15:02:09 | Glencourse (Kelani Ganga) | 8.43 | 🟢 Normal | 0.131 | 🔺 Rising |
| 2026-03-21 15:04:02 | Wellawaya (Kirindi Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-03-21 15:01:00 | Nakkala (Kumbukkan Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-03-21 15:01:42 | Nawalapitiya (Mahaweli Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-21 15:02:29 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-21 15:02:27 | Giriulla (Maha Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-03-21 14:02:53 | Horowpothana (Yan Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-03-21 15:05:23 | Galgamuwa (Mee Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-21 15:03:54 | Magura (Kalu Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-03-21 15:01:42 | Norwood (Kelani Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-03-21 15:01:12 | Ellagawa (Kalu Ganga) | 3.98 | 🟢 Normal | 0.000 |  |
| 2026-03-21 15:03:16 | Panadugama (Nilwala Ganga) | 2.02 | 🟢 Normal | 0.000 |  |
| 2026-03-21 15:01:07 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-03-21 15:00:45 | Dunamale (Aththanagalu Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-03-21 15:02:51 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-03-21 15:01:49 | Badalgama (Maha Oya) | 1.86 | 🟢 Normal | 0.000 |  |
| 2026-03-21 15:05:10 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-03-21 15:01:29 | Kuda Oya (Kirindi Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-03-21 15:06:37 | Padiyathalawa (Maduru Oya) | 0.41 | 🟢 Normal | -0.009 |  |
| 2026-03-21 15:04:09 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | -0.009 |  |
| 2026-03-21 15:05:30 | Holombuwa (Kelani Ganga) | 0.23 | 🟢 Normal | -0.010 |  |
| 2026-03-21 15:01:51 | Thanthirimale (Malwathu Oya) | 1.35 | 🟢 Normal | -0.010 |  |
| 2026-03-21 15:02:48 | Hanwella (Kelani Ganga) | 0.40 | 🟢 Normal | -0.010 |  |
| 2026-03-21 15:01:55 | Kithulgala (Kelani Ganga) | 1.39 | 🟢 Normal | -0.010 |  |
| 2026-03-21 15:07:07 | Rathnapura (Kalu Ganga) | 0.55 | 🟢 Normal | -0.012 |  |
| 2026-03-21 15:03:39 | Pitabeddara (Nilwala Ganga) | 0.31 | 🟢 Normal | -0.015 |  |
| 2026-03-21 15:01:53 | Moraketiya (Walawe Ganga) | 0.82 | 🟢 Normal | -0.018 |  |
| 2026-03-21 15:02:12 | Thanamalwila (Kirindi Oya) | 0.60 | 🟢 Normal | -0.020 |  |
| 2026-03-21 15:02:02 | Thaldena (Mahaweli Ganga) | 0.36 | 🟢 Normal | -0.022 |  |
| 2026-03-21 15:02:33 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.36 | 🟢 Normal | -0.030 |  |
| 2026-03-21 15:01:53 | Thawalama (Gin Ganga) | 1.38 | 🟢 Normal | -0.032 |  |
| 2026-03-21 14:03:56 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | -0.044 |  |
| 2026-03-21 15:04:41 | Manampitiya (Mahaweli Ganga) | 0.50 | 🟢 Normal | -0.047 |  |
| 2026-03-21 15:02:47 | Baddegama (Gin Ganga) | 1.15 | 🟢 Normal | -0.064 |  |
| 2026-03-21 15:03:55 | Deraniyagala (Kelani Ganga) | 0.21 | 🟢 Normal | -0.068 |  |
| 2026-03-21 15:01:54 | Weraganthota (Mahaweli Ganga) | -2.65 | 🟢 Normal | -0.079 |  |
| 2026-03-21 15:03:07 | Peradeniya (Mahaweli Ganga) | 1.08 | 🟢 Normal | -0.118 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)