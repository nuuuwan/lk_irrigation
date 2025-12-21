# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--21_17:02:05-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **24,080 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **30** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-21 17:02:05 | Badalgama (Maha Oya) | 2.30 | 🟢 Normal | -0.011 |  |
| 2025-12-21 17:01:49 | Thanamalwila (Kirindi Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2025-12-21 17:01:36 | Katharagama (Menik Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2025-12-21 17:01:30 | Wellawaya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2025-12-21 17:01:17 | Panadugama (Nilwala Ganga) | 3.36 | 🟢 Normal | -0.086 |  |
| 2025-12-21 17:01:17 | Thanthirimale (Malwathu Oya) | 5.00 | 🟡 Alert | -0.032 |  |
| 2025-12-21 17:01:09 | Nawalapitiya (Mahaweli Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2025-12-21 17:01:09 | Ellagawa (Kalu Ganga) | 4.99 | 🟢 Normal | -0.051 |  |
| 2025-12-21 17:00:57 | Thaldena (Mahaweli Ganga) | 0.88 | 🟢 Normal | -0.030 |  |
| 2025-12-21 17:00:16 | Magura (Kalu Ganga) | 1.48 | 🟢 Normal | -0.010 |  |
| 2025-12-21 17:00:13 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | -0.010 |  |
| 2025-12-21 16:13:51 | Peradeniya (Mahaweli Ganga) | 2.60 | 🟢 Normal | -0.083 |  |
| 2025-12-21 16:12:58 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2025-12-21 16:12:45 | Holombuwa (Kelani Ganga) | 0.55 | 🟢 Normal | -0.009 |  |
| 2025-12-21 16:11:28 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.35 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2025-12-21 16:10:54 | Urawa (Nilwala Ganga) | 0.44 | 🟢 Normal | -0.019 |  |
| 2025-12-21 16:08:16 | Pitabeddara (Nilwala Ganga) | 0.92 | 🟢 Normal | -0.009 |  |
| 2025-12-21 16:08:07 | Thawalama (Gin Ganga) | 1.56 | 🟢 Normal | -0.018 |  |
| 2025-12-21 16:07:46 | Dunamale (Aththanagalu Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2025-12-21 16:07:21 | Yaka Wewa (Ma Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2025-12-21 16:07:06 | Katharagama (Menik Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2025-12-21 16:05:47 | Galgamuwa (Mee Oya) | 1.69 | 🟢 Normal | -0.030 |  |
| 2025-12-21 16:05:30 | Weraganthota (Mahaweli Ganga) | -1.00 | 🟢 Normal | -0.305 |  |
| 2025-12-21 16:05:24 | Panadugama (Nilwala Ganga) | 3.44 | 🟢 Normal | -0.086 |  |
| 2025-12-21 16:05:00 | Badalgama (Maha Oya) | 2.31 | 🟢 Normal | -0.011 |  |
| 2025-12-21 16:04:48 | Thanthirimale (Malwathu Oya) | 5.03 | 🟡 Alert | -0.032 |  |
| 2025-12-21 16:04:30 | Giriulla (Maha Oya) | 1.16 | 🟢 Normal | -0.010 |  |
| 2025-12-21 16:04:11 | Glencourse (Kelani Ganga) | 8.94 | 🟢 Normal | -0.010 |  |
| 2025-12-21 16:03:51 | Padiyathalawa (Maduru Oya) | 1.31 | 🟢 Normal | -0.012 |  |
| 2025-12-21 16:03:41 | Kithulgala (Kelani Ganga) | 1.73 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-21 17:01:17 | Thanthirimale (Malwathu Oya) | 5.00 | 🟡 Alert | -0.032 |  |
| 2025-12-21 16:03:12 | Siyambalanduwa (Heda Oya) | 1.25 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2025-12-21 16:12:58 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2025-12-21 16:11:28 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.35 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2025-12-21 16:02:50 | Kuda Oya (Kirindi Oya) | 1.36 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-21 16:02:23 | Putupaula (Kalu Ganga) | 0.83 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-21 16:02:27 | Norwood (Kelani Ganga) | 0.67 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-21 17:01:30 | Wellawaya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2025-12-21 16:01:23 | Moragaswewa (Deduru Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2025-12-21 17:01:09 | Nawalapitiya (Mahaweli Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2025-12-21 16:07:21 | Yaka Wewa (Ma Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2025-12-21 16:02:36 | Hanwella (Kelani Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2025-12-21 16:02:09 | Deraniyagala (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2025-12-21 16:01:09 | Baddegama (Gin Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2025-12-21 16:07:46 | Dunamale (Aththanagalu Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2025-12-21 17:01:36 | Katharagama (Menik Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2025-12-21 15:16:26 | Thalgahagoda (Nilwala Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-21 17:01:49 | Thanamalwila (Kirindi Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2025-12-21 16:12:45 | Holombuwa (Kelani Ganga) | 0.55 | 🟢 Normal | -0.009 |  |
| 2025-12-21 16:08:16 | Pitabeddara (Nilwala Ganga) | 0.92 | 🟢 Normal | -0.009 |  |
| 2025-12-21 16:04:30 | Giriulla (Maha Oya) | 1.16 | 🟢 Normal | -0.010 |  |
| 2025-12-21 16:03:41 | Kithulgala (Kelani Ganga) | 1.73 | 🟢 Normal | -0.010 |  |
| 2025-12-21 17:00:13 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | -0.010 |  |
| 2025-12-21 16:04:11 | Glencourse (Kelani Ganga) | 8.94 | 🟢 Normal | -0.010 |  |
| 2025-12-21 17:00:16 | Magura (Kalu Ganga) | 1.48 | 🟢 Normal | -0.010 |  |
| 2025-12-21 17:02:05 | Badalgama (Maha Oya) | 2.30 | 🟢 Normal | -0.011 |  |
| 2025-12-21 16:02:59 | Nakkala (Kumbukkan Oya) | 1.29 | 🟢 Normal | -0.011 |  |
| 2025-12-21 16:03:51 | Padiyathalawa (Maduru Oya) | 1.31 | 🟢 Normal | -0.012 |  |
| 2025-12-21 16:08:07 | Thawalama (Gin Ganga) | 1.56 | 🟢 Normal | -0.018 |  |
| 2025-12-21 16:10:54 | Urawa (Nilwala Ganga) | 0.44 | 🟢 Normal | -0.019 |  |
| 2025-12-21 16:02:42 | Rathnapura (Kalu Ganga) | 1.26 | 🟢 Normal | -0.022 |  |
| 2025-12-21 16:05:47 | Galgamuwa (Mee Oya) | 1.69 | 🟢 Normal | -0.030 |  |
| 2025-12-21 17:00:57 | Thaldena (Mahaweli Ganga) | 0.88 | 🟢 Normal | -0.030 |  |
| 2025-12-21 16:01:15 | Manampitiya (Mahaweli Ganga) | 2.70 | 🟢 Normal | -0.031 |  |
| 2025-12-21 17:01:09 | Ellagawa (Kalu Ganga) | 4.99 | 🟢 Normal | -0.051 |  |
| 2025-12-21 16:01:04 | Horowpothana (Yan Oya) | 4.78 | 🟢 Normal | -0.052 |  |
| 2025-12-21 16:13:51 | Peradeniya (Mahaweli Ganga) | 2.60 | 🟢 Normal | -0.083 |  |
| 2025-12-21 17:01:17 | Panadugama (Nilwala Ganga) | 3.36 | 🟢 Normal | -0.086 |  |
| 2025-12-21 16:05:30 | Weraganthota (Mahaweli Ganga) | -1.00 | 🟢 Normal | -0.305 |  |

## River Water Level Charts by Station

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)