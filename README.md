# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--15_02:04:59-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **45,828 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **21** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-15 02:04:59 | Hanwella (Kelani Ganga) | 0.71 | 🟢 Normal | -0.020 |  |
| 2026-01-15 02:04:39 | Rathnapura (Kalu Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-01-15 02:04:36 | Urawa (Nilwala Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-01-15 02:02:56 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-01-15 02:02:55 | Giriulla (Maha Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-01-15 02:02:35 | Padiyathalawa (Maduru Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-01-15 02:02:34 | Norwood (Kelani Ganga) | 0.48 | 🟢 Normal | -0.010 |  |
| 2026-01-15 02:02:21 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-01-15 02:02:17 | Moragaswewa (Deduru Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-01-15 02:01:54 | Peradeniya (Mahaweli Ganga) | 2.10 | 🟢 Normal | -0.102 |  |
| 2026-01-15 02:01:15 | Deraniyagala (Kelani Ganga) | 0.20 | 🟢 Normal | -0.020 |  |
| 2026-01-15 02:00:56 | Ellagawa (Kalu Ganga) | 4.12 | 🟢 Normal | 0.000 |  |
| 2026-01-15 02:00:48 | Thaldena (Mahaweli Ganga) | 0.66 | 🟢 Normal | -0.020 |  |
| 2026-01-15 02:00:29 | Manampitiya (Mahaweli Ganga) | 1.71 | 🟢 Normal | -0.005 |  |
| 2026-01-15 01:44:49 | Rathnapura (Kalu Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-01-15 01:44:22 | Nawalapitiya (Mahaweli Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-01-15 01:39:57 | Panadugama (Nilwala Ganga) | 3.38 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-01-15 01:29:02 | Putupaula (Kalu Ganga) | 0.69 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-01-15 01:16:45 | Siyambalanduwa (Heda Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-01-15 01:12:39 | Nakkala (Kumbukkan Oya) | 1.10 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-01-15 01:10:50 | Katharagama (Menik Ganga) | 0.07 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-15 01:06:49 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.12 | 🟢 Normal | 0.467 | 🔺 Rising |
| 2026-01-15 01:07:47 | Thalgahagoda (Nilwala Ganga) | 0.34 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-01-15 02:02:21 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-01-15 00:07:06 | Baddegama (Gin Ganga) | 1.34 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-01-15 01:12:39 | Nakkala (Kumbukkan Oya) | 1.10 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-01-15 01:29:02 | Putupaula (Kalu Ganga) | 0.69 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-01-15 01:39:57 | Panadugama (Nilwala Ganga) | 3.38 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-01-15 01:02:08 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-01-14 18:00:19 | Weraganthota (Mahaweli Ganga) | -1.52 | 🟢 Normal | 0.000 |  |
| 2026-01-15 02:02:17 | Moragaswewa (Deduru Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-01-15 01:44:22 | Nawalapitiya (Mahaweli Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-01-15 01:07:20 | Yaka Wewa (Ma Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-01-15 02:02:55 | Giriulla (Maha Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-01-14 18:02:43 | Galgamuwa (Mee Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-01-15 00:18:34 | Magura (Kalu Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-01-15 02:00:56 | Ellagawa (Kalu Ganga) | 4.12 | 🟢 Normal | 0.000 |  |
| 2026-01-15 02:02:35 | Padiyathalawa (Maduru Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-01-15 02:02:56 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-01-15 01:16:45 | Siyambalanduwa (Heda Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-01-15 01:03:37 | Dunamale (Aththanagalu Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-01-15 01:10:50 | Katharagama (Menik Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-01-15 00:05:27 | Badalgama (Maha Oya) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-01-15 01:07:06 | Holombuwa (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-01-15 02:04:39 | Rathnapura (Kalu Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-01-15 02:04:36 | Urawa (Nilwala Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-01-15 00:01:18 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-01-15 00:08:03 | Thanamalwila (Kirindi Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-01-15 02:00:29 | Manampitiya (Mahaweli Ganga) | 1.71 | 🟢 Normal | -0.005 |  |
| 2026-01-15 00:02:34 | Thawalama (Gin Ganga) | 1.21 | 🟢 Normal | -0.010 |  |
| 2026-01-15 02:02:34 | Norwood (Kelani Ganga) | 0.48 | 🟢 Normal | -0.010 |  |
| 2026-01-15 01:01:52 | Pitabeddara (Nilwala Ganga) | 0.89 | 🟢 Normal | -0.010 |  |
| 2026-01-14 23:03:29 | Glencourse (Kelani Ganga) | 8.63 | 🟢 Normal | -0.010 |  |
| 2026-01-15 01:01:28 | Wellawaya (Kirindi Oya) | 1.07 | 🟢 Normal | -0.010 |  |
| 2026-01-14 18:02:52 | Thanthirimale (Malwathu Oya) | 2.20 | 🟢 Normal | -0.020 |  |
| 2026-01-15 02:01:15 | Deraniyagala (Kelani Ganga) | 0.20 | 🟢 Normal | -0.020 |  |
| 2026-01-15 02:00:48 | Thaldena (Mahaweli Ganga) | 0.66 | 🟢 Normal | -0.020 |  |
| 2026-01-15 02:04:59 | Hanwella (Kelani Ganga) | 0.71 | 🟢 Normal | -0.020 |  |
| 2026-01-15 01:01:14 | Horowpothana (Yan Oya) | 2.62 | 🟢 Normal | -0.034 |  |
| 2026-01-15 02:01:54 | Peradeniya (Mahaweli Ganga) | 2.10 | 🟢 Normal | -0.102 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

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

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)