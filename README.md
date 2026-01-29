# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--29_16:13:23-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **58,968 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-29 16:13:23 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-01-29 16:09:47 | Baddegama (Gin Ganga) | 0.80 | 🟢 Normal | -0.020 |  |
| 2026-01-29 16:08:20 | Rathnapura (Kalu Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-01-29 16:07:25 | Badalgama (Maha Oya) | 1.83 | 🟢 Normal | 0.000 |  |
| 2026-01-29 16:06:08 | Kuda Oya (Kirindi Oya) | 1.21 | 🟢 Normal | -0.009 |  |
| 2026-01-29 16:05:58 | Thalgahagoda (Nilwala Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-01-29 16:05:36 | Wellawaya (Kirindi Oya) | 0.82 | 🟢 Normal | -0.009 |  |
| 2026-01-29 16:05:18 | Weraganthota (Mahaweli Ganga) | -2.35 | 🟢 Normal | -0.019 |  |
| 2026-01-29 16:05:11 | Katharagama (Menik Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-01-29 16:04:46 | Giriulla (Maha Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-01-29 16:04:36 | Panadugama (Nilwala Ganga) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-01-29 16:04:34 | Dunamale (Aththanagalu Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-01-29 16:04:22 | Peradeniya (Mahaweli Ganga) | 1.15 | 🟢 Normal | -0.047 |  |
| 2026-01-29 16:04:06 | Putupaula (Kalu Ganga) | 0.40 | 🟢 Normal | -0.040 |  |
| 2026-01-29 16:04:01 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.20 | 🟢 Normal | -0.010 |  |
| 2026-01-29 16:03:48 | Hanwella (Kelani Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-01-29 16:03:34 | Deraniyagala (Kelani Ganga) | 0.19 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-01-29 16:03:14 | Thawalama (Gin Ganga) | 0.96 | 🟢 Normal | -0.010 |  |
| 2026-01-29 16:03:11 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.015 |  |
| 2026-01-29 16:03:06 | Nakkala (Kumbukkan Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-01-29 16:03:03 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-01-29 16:03:02 | Galgamuwa (Mee Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-01-29 16:02:59 | Ellagawa (Kalu Ganga) | 3.80 | 🟢 Normal | 0.000 |  |
| 2026-01-29 16:02:46 | Moraketiya (Walawe Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-01-29 16:02:45 | Holombuwa (Kelani Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-01-29 16:02:33 | Glencourse (Kelani Ganga) | 8.31 | 🟢 Normal | -0.030 |  |
| 2026-01-29 16:02:32 | Pitabeddara (Nilwala Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-01-29 16:02:30 | Norwood (Kelani Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-01-29 16:02:07 | Thanamalwila (Kirindi Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-01-29 16:01:39 | Padiyathalawa (Maduru Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-01-29 16:01:33 | Thaldena (Mahaweli Ganga) | 0.44 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-29 16:01:19 | Siyambalanduwa (Heda Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-01-29 16:01:16 | Thanthirimale (Malwathu Oya) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-01-29 16:01:08 | Nawalapitiya (Mahaweli Ganga) | 0.63 | 🟢 Normal | -0.010 |  |
| 2026-01-29 16:00:54 | Moragaswewa (Deduru Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-01-29 16:00:21 | Manampitiya (Mahaweli Ganga) | 0.97 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-01-29 15:58:00 | Norwood (Kelani Ganga) | 0.39 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-29 16:03:34 | Deraniyagala (Kelani Ganga) | 0.19 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-01-29 16:13:23 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-01-29 16:00:21 | Manampitiya (Mahaweli Ganga) | 0.97 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-01-29 16:03:03 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-01-29 16:01:33 | Thaldena (Mahaweli Ganga) | 0.44 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-29 16:03:06 | Nakkala (Kumbukkan Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-01-29 16:00:54 | Moragaswewa (Deduru Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-01-29 15:02:41 | Yaka Wewa (Ma Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-01-29 16:04:46 | Giriulla (Maha Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-01-29 16:03:02 | Galgamuwa (Mee Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-01-29 16:02:32 | Pitabeddara (Nilwala Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-01-29 16:02:30 | Norwood (Kelani Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-01-29 16:03:48 | Hanwella (Kelani Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-01-29 16:02:59 | Ellagawa (Kalu Ganga) | 3.80 | 🟢 Normal | 0.000 |  |
| 2026-01-29 16:04:36 | Panadugama (Nilwala Ganga) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-01-29 16:01:39 | Padiyathalawa (Maduru Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-01-29 16:02:46 | Moraketiya (Walawe Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-01-29 16:01:19 | Siyambalanduwa (Heda Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-01-29 16:04:34 | Dunamale (Aththanagalu Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-01-29 16:05:11 | Katharagama (Menik Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-01-29 16:07:25 | Badalgama (Maha Oya) | 1.83 | 🟢 Normal | 0.000 |  |
| 2026-01-29 16:02:45 | Holombuwa (Kelani Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-01-29 16:08:20 | Rathnapura (Kalu Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-01-29 16:01:16 | Thanthirimale (Malwathu Oya) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-01-29 15:11:22 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-01-29 16:05:58 | Thalgahagoda (Nilwala Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-01-29 16:02:07 | Thanamalwila (Kirindi Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-01-29 16:05:36 | Wellawaya (Kirindi Oya) | 0.82 | 🟢 Normal | -0.009 |  |
| 2026-01-29 16:06:08 | Kuda Oya (Kirindi Oya) | 1.21 | 🟢 Normal | -0.009 |  |
| 2026-01-29 16:01:08 | Nawalapitiya (Mahaweli Ganga) | 0.63 | 🟢 Normal | -0.010 |  |
| 2026-01-29 15:08:24 | Magura (Kalu Ganga) | 0.63 | 🟢 Normal | -0.010 |  |
| 2026-01-29 16:04:01 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.20 | 🟢 Normal | -0.010 |  |
| 2026-01-29 16:03:14 | Thawalama (Gin Ganga) | 0.96 | 🟢 Normal | -0.010 |  |
| 2026-01-29 16:03:11 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.015 |  |
| 2026-01-29 16:05:18 | Weraganthota (Mahaweli Ganga) | -2.35 | 🟢 Normal | -0.019 |  |
| 2026-01-29 16:09:47 | Baddegama (Gin Ganga) | 0.80 | 🟢 Normal | -0.020 |  |
| 2026-01-29 16:02:33 | Glencourse (Kelani Ganga) | 8.31 | 🟢 Normal | -0.030 |  |
| 2026-01-29 16:04:06 | Putupaula (Kalu Ganga) | 0.40 | 🟢 Normal | -0.040 |  |
| 2026-01-29 16:04:22 | Peradeniya (Mahaweli Ganga) | 1.15 | 🟢 Normal | -0.047 |  |

## River Water Level Charts by Station

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

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

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)