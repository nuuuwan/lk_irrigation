# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--09_11:41:24-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **40,834 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **43** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-09 11:41:24 | Badalgama (Maha Oya) | 1.99 | 🟢 Normal | 0.000 |  |
| 2026-01-09 11:26:07 | Thalgahagoda (Nilwala Ganga) | 0.48 | 🟢 Normal | -0.027 |  |
| 2026-01-09 11:17:13 | Panadugama (Nilwala Ganga) | 2.52 | 🟢 Normal | -0.009 |  |
| 2026-01-09 11:12:02 | Giriulla (Maha Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-01-09 11:10:49 | Hanwella (Kelani Ganga) | 0.44 | 🟢 Normal | 0.965 | 🔺 Rising |
| 2026-01-09 11:10:10 | Pitabeddara (Nilwala Ganga) | 0.78 | 🟢 Normal | -0.023 |  |
| 2026-01-09 11:09:20 | Magura (Kalu Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-01-09 11:06:51 | Peradeniya (Mahaweli Ganga) | 2.03 | 🟢 Normal | -0.068 |  |
| 2026-01-09 11:06:41 | Baddegama (Gin Ganga) | 0.94 | 🟢 Normal | -0.019 |  |
| 2026-01-09 11:06:34 | Putupaula (Kalu Ganga) | 0.37 | 🟢 Normal | -0.112 |  |
| 2026-01-09 11:06:14 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-01-09 11:05:53 | Dunamale (Aththanagalu Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-01-09 11:05:16 | Kuda Oya (Kirindi Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-01-09 11:05:10 | Badalgama (Maha Oya) | 1.99 | 🟢 Normal | 0.000 |  |
| 2026-01-09 11:04:49 | Norwood (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-01-09 11:04:39 | Rathnapura (Kalu Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-01-09 11:04:36 | Hanwella (Kelani Ganga) | 0.34 | 🟢 Normal | 0.965 | 🔺 Rising |
| 2026-01-09 11:04:24 | Urawa (Nilwala Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-01-09 11:04:08 | Deraniyagala (Kelani Ganga) | 0.28 | 🟢 Normal | -0.069 |  |
| 2026-01-09 11:03:48 | Padiyathalawa (Maduru Oya) | 1.29 | 🟢 Normal | -0.010 |  |
| 2026-01-09 11:03:33 | Horowpothana (Yan Oya) | 2.27 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-09 11:03:26 | Glencourse (Kelani Ganga) | 8.53 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-01-09 11:03:06 | Nakkala (Kumbukkan Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-01-09 11:02:47 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | 0.131 | 🔺 Rising |
| 2026-01-09 11:02:46 | Thaldena (Mahaweli Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-01-09 11:02:45 | Katharagama (Menik Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-01-09 11:02:45 | Galgamuwa (Mee Oya) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-01-09 11:02:36 | Manampitiya (Mahaweli Ganga) | 2.53 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-01-09 11:02:20 | Yaka Wewa (Ma Oya) | 0.85 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-09 11:02:08 | Thanthirimale (Malwathu Oya) | 1.48 | 🟢 Normal | 0.000 |  |
| 2026-01-09 11:02:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.40 | 🟢 Normal | -0.051 |  |
| 2026-01-09 11:01:39 | Thanamalwila (Kirindi Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-01-09 11:01:29 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-01-09 11:01:18 | Ellagawa (Kalu Ganga) | 4.11 | 🟢 Normal | 0.000 |  |
| 2026-01-09 11:01:15 | Moragaswewa (Deduru Oya) | 1.99 | 🟢 Normal | -0.509 |  |
| 2026-01-09 11:01:13 | Thawalama (Gin Ganga) | 1.23 | 🟢 Normal | -1.500 |  |
| 2026-01-09 11:01:10 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.031 |  |
| 2026-01-09 11:01:07 | Wellawaya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-01-09 11:00:49 | Thawalama (Gin Ganga) | 1.24 | 🟢 Normal | -1.500 |  |
| 2026-01-09 11:00:45 | Nawalapitiya (Mahaweli Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-01-09 11:00:24 | Nakkala (Kumbukkan Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-01-09 11:00:09 | Weraganthota (Mahaweli Ganga) | -1.14 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-09 11:00:08 | Siyambalanduwa (Heda Oya) | 1.14 | 🟢 Normal | -0.011 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-09 11:10:49 | Hanwella (Kelani Ganga) | 0.44 | 🟢 Normal | 0.965 | 🔺 Rising |
| 2026-01-09 11:02:47 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | 0.131 | 🔺 Rising |
| 2026-01-09 11:02:36 | Manampitiya (Mahaweli Ganga) | 2.53 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-01-09 11:03:26 | Glencourse (Kelani Ganga) | 8.53 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-01-09 11:03:33 | Horowpothana (Yan Oya) | 2.27 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-09 11:02:20 | Yaka Wewa (Ma Oya) | 0.85 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-09 11:00:09 | Weraganthota (Mahaweli Ganga) | -1.14 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-09 11:01:07 | Wellawaya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-01-09 11:03:06 | Nakkala (Kumbukkan Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-01-09 11:00:45 | Nawalapitiya (Mahaweli Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-01-09 11:12:02 | Giriulla (Maha Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-01-09 11:02:45 | Galgamuwa (Mee Oya) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-01-09 11:09:20 | Magura (Kalu Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-01-09 11:04:49 | Norwood (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-01-09 11:01:18 | Ellagawa (Kalu Ganga) | 4.11 | 🟢 Normal | 0.000 |  |
| 2026-01-09 11:01:29 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-01-09 11:05:53 | Dunamale (Aththanagalu Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-01-09 11:02:46 | Thaldena (Mahaweli Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-01-09 11:02:45 | Katharagama (Menik Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-01-09 11:41:24 | Badalgama (Maha Oya) | 1.99 | 🟢 Normal | 0.000 |  |
| 2026-01-09 11:06:14 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-01-09 11:04:39 | Rathnapura (Kalu Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-01-09 11:02:08 | Thanthirimale (Malwathu Oya) | 1.48 | 🟢 Normal | 0.000 |  |
| 2026-01-09 11:04:24 | Urawa (Nilwala Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-01-09 11:05:16 | Kuda Oya (Kirindi Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-01-09 11:01:39 | Thanamalwila (Kirindi Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-01-09 11:17:13 | Panadugama (Nilwala Ganga) | 2.52 | 🟢 Normal | -0.009 |  |
| 2026-01-09 11:03:48 | Padiyathalawa (Maduru Oya) | 1.29 | 🟢 Normal | -0.010 |  |
| 2026-01-09 11:00:08 | Siyambalanduwa (Heda Oya) | 1.14 | 🟢 Normal | -0.011 |  |
| 2026-01-09 11:06:41 | Baddegama (Gin Ganga) | 0.94 | 🟢 Normal | -0.019 |  |
| 2026-01-09 11:10:10 | Pitabeddara (Nilwala Ganga) | 0.78 | 🟢 Normal | -0.023 |  |
| 2026-01-09 11:26:07 | Thalgahagoda (Nilwala Ganga) | 0.48 | 🟢 Normal | -0.027 |  |
| 2026-01-09 11:01:10 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.031 |  |
| 2026-01-09 11:02:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.40 | 🟢 Normal | -0.051 |  |
| 2026-01-09 11:06:51 | Peradeniya (Mahaweli Ganga) | 2.03 | 🟢 Normal | -0.068 |  |
| 2026-01-09 11:04:08 | Deraniyagala (Kelani Ganga) | 0.28 | 🟢 Normal | -0.069 |  |
| 2026-01-09 11:06:34 | Putupaula (Kalu Ganga) | 0.37 | 🟢 Normal | -0.112 |  |
| 2026-01-09 11:01:15 | Moragaswewa (Deduru Oya) | 1.99 | 🟢 Normal | -0.509 |  |
| 2026-01-09 11:01:13 | Thawalama (Gin Ganga) | 1.23 | 🟢 Normal | -1.500 |  |

## River Water Level Charts by Station

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

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

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)