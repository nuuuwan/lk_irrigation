# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--29_03:13:32-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **219,028 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-29 03:13:32 | Rathnapura (Kalu Ganga) | 0.98 | 🟢 Normal | -0.026 |  |
| 2026-07-29 03:12:36 | Holombuwa (Kelani Ganga) | 0.24 | 🟢 Normal | -0.029 |  |
| 2026-07-29 03:11:37 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.027 |  |
| 2026-07-29 03:09:08 | Moragaswewa (Deduru Oya) | 0.03 | 🟢 Normal | 0.125 | 🔺 Rising |
| 2026-07-29 03:06:57 | Badalgama (Maha Oya) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-07-29 03:06:51 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | -0.009 |  |
| 2026-07-29 03:06:46 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-07-29 03:06:00 | Panadugama (Nilwala Ganga) | 1.98 | 🟢 Normal | 0.000 |  |
| 2026-07-29 03:05:38 | Glencourse (Kelani Ganga) | 9.05 | 🟢 Normal | 0.151 | 🔺 Rising |
| 2026-07-29 03:05:32 | Thaldena (Mahaweli Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-07-29 03:05:30 | Thaldena (Mahaweli Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-07-29 03:05:14 | Deraniyagala (Kelani Ganga) | 0.45 | 🟢 Normal | -0.059 |  |
| 2026-07-29 03:04:59 | Peradeniya (Mahaweli Ganga) | 1.86 | 🟢 Normal | -0.215 |  |
| 2026-07-29 03:04:45 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-07-29 03:04:36 | Thawalama (Gin Ganga) | 1.26 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-29 03:04:32 | Giriulla (Maha Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-07-29 03:04:19 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.125 | 🔺 Rising |
| 2026-07-29 03:04:10 | Pitabeddara (Nilwala Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-07-29 03:04:05 | Ellagawa (Kalu Ganga) | 4.21 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-29 03:03:38 | Kithulgala (Kelani Ganga) | 1.66 | 🟢 Normal | 0.000 |  |
| 2026-07-29 03:03:09 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | -0.010 |  |
| 2026-07-29 03:02:57 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-07-29 03:02:39 | Thanamalwila (Kirindi Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-07-29 03:02:29 | Moraketiya (Walawe Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-07-29 03:02:25 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-07-29 03:02:18 | Manampitiya (Mahaweli Ganga) | -0.17 | 🟢 Normal | -0.180 |  |
| 2026-07-29 03:02:12 | Hanwella (Kelani Ganga) | 0.48 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-07-29 03:01:47 | Nawalapitiya (Mahaweli Ganga) | 1.04 | 🟢 Normal | -0.011 |  |
| 2026-07-29 03:01:46 | Siyambalanduwa (Heda Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-07-29 03:01:15 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-29 03:01:13 | Baddegama (Gin Ganga) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-07-29 02:55:38 | Manampitiya (Mahaweli Ganga) | -0.15 | 🟢 Normal | -0.180 |  |
| 2026-07-29 02:55:04 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.125 | 🔺 Rising |
| 2026-07-29 02:49:25 | Badalgama (Maha Oya) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-07-29 02:34:10 | Pitabeddara (Nilwala Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-07-29 02:34:09 | Pitabeddara (Nilwala Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-07-29 02:34:07 | Pitabeddara (Nilwala Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-07-29 02:33:16 | Magura (Kalu Ganga) | 0.88 | 🟢 Normal | -0.025 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-29 03:05:38 | Glencourse (Kelani Ganga) | 9.05 | 🟢 Normal | 0.151 | 🔺 Rising |
| 2026-07-29 03:09:08 | Moragaswewa (Deduru Oya) | 0.03 | 🟢 Normal | 0.125 | 🔺 Rising |
| 2026-07-29 02:04:59 | Putupaula (Kalu Ganga) | 0.55 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-07-29 03:02:12 | Hanwella (Kelani Ganga) | 0.48 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-07-29 03:04:36 | Thawalama (Gin Ganga) | 1.26 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-29 03:04:05 | Ellagawa (Kalu Ganga) | 4.21 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-29 03:03:38 | Kithulgala (Kelani Ganga) | 1.66 | 🟢 Normal | 0.000 |  |
| 2026-07-29 03:02:57 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-07-29 03:06:46 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-07-29 03:02:25 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-07-29 03:04:32 | Giriulla (Maha Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-07-28 23:01:04 | Horowpothana (Yan Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-07-28 18:03:13 | Galgamuwa (Mee Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-07-29 03:04:10 | Pitabeddara (Nilwala Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-07-29 03:01:13 | Baddegama (Gin Ganga) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-07-29 03:06:00 | Panadugama (Nilwala Ganga) | 1.98 | 🟢 Normal | 0.000 |  |
| 2026-07-29 03:01:15 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-29 03:02:29 | Moraketiya (Walawe Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-07-29 03:01:46 | Siyambalanduwa (Heda Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-07-29 01:07:30 | Dunamale (Aththanagalu Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-07-29 03:05:32 | Thaldena (Mahaweli Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-07-29 03:06:57 | Badalgama (Maha Oya) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-07-28 18:00:50 | Thanthirimale (Malwathu Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-07-29 01:47:14 | Urawa (Nilwala Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-07-29 00:03:01 | Kuda Oya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-07-29 03:02:39 | Thanamalwila (Kirindi Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-07-28 22:06:35 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-07-29 03:06:51 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | -0.009 |  |
| 2026-07-29 03:03:09 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | -0.010 |  |
| 2026-07-29 03:01:47 | Nawalapitiya (Mahaweli Ganga) | 1.04 | 🟢 Normal | -0.011 |  |
| 2026-07-29 01:10:40 | Thalgahagoda (Nilwala Ganga) | 0.14 | 🟢 Normal | -0.019 |  |
| 2026-07-29 02:33:16 | Magura (Kalu Ganga) | 0.88 | 🟢 Normal | -0.025 |  |
| 2026-07-29 03:13:32 | Rathnapura (Kalu Ganga) | 0.98 | 🟢 Normal | -0.026 |  |
| 2026-07-29 03:11:37 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.027 |  |
| 2026-07-29 03:12:36 | Holombuwa (Kelani Ganga) | 0.24 | 🟢 Normal | -0.029 |  |
| 2026-07-28 18:00:11 | Weraganthota (Mahaweli Ganga) | -3.26 | 🟢 Normal | -0.030 |  |
| 2026-07-29 03:05:14 | Deraniyagala (Kelani Ganga) | 0.45 | 🟢 Normal | -0.059 |  |
| 2026-07-29 03:02:18 | Manampitiya (Mahaweli Ganga) | -0.17 | 🟢 Normal | -0.180 |  |
| 2026-07-29 03:04:59 | Peradeniya (Mahaweli Ganga) | 1.86 | 🟢 Normal | -0.215 |  |

## River Water Level Charts by Station

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

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

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)