# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--29_03:15:02-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **164,455 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-29 03:15:02 | Holombuwa (Kelani Ganga) | 1.05 | 🟢 Normal | -0.156 |  |
| 2026-05-29 03:11:34 | Thawalama (Gin Ganga) | 3.14 | 🟢 Normal | -0.081 |  |
| 2026-05-29 03:09:05 | Hanwella (Kelani Ganga) | 3.90 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-05-29 03:07:03 | Panadugama (Nilwala Ganga) | 5.11 | 🟡 Alert | 0.013 | 🔺 Rising |
| 2026-05-29 03:06:35 | Rathnapura (Kalu Ganga) | 5.01 | 🟢 Normal | -0.185 |  |
| 2026-05-29 03:06:25 | Thalgahagoda (Nilwala Ganga) | 0.76 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-05-29 03:06:01 | Thanamalwila (Kirindi Oya) | 0.74 | 🟢 Normal | 0.065 | 🔺 Rising |
| 2026-05-29 03:05:57 | Baddegama (Gin Ganga) | 3.10 | 🟢 Normal | -1.800 |  |
| 2026-05-29 03:05:41 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | -0.031 |  |
| 2026-05-29 03:05:39 | Kithulgala (Kelani Ganga) | 1.84 | 🟢 Normal | -0.010 |  |
| 2026-05-29 03:05:37 | Baddegama (Gin Ganga) | 3.11 | 🟢 Normal | -1.800 |  |
| 2026-05-29 03:05:36 | Urawa (Nilwala Ganga) | 1.10 | 🟢 Normal | -0.087 |  |
| 2026-05-29 03:05:34 | Badalgama (Maha Oya) | 2.36 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-29 03:05:26 | Wellawaya (Kirindi Oya) | 1.08 | 🟢 Normal | -0.028 |  |
| 2026-05-29 03:04:31 | Deraniyagala (Kelani Ganga) | 1.83 | 🟢 Normal | -0.304 |  |
| 2026-05-29 03:04:01 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-05-29 03:03:58 | Thaldena (Mahaweli Ganga) | 0.38 | 🟢 Normal | -54.000 |  |
| 2026-05-29 03:03:56 | Thaldena (Mahaweli Ganga) | 0.41 | 🟢 Normal | -54.000 |  |
| 2026-05-29 03:03:43 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-05-29 03:03:39 | Padiyathalawa (Maduru Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-05-29 03:03:27 | Magura (Kalu Ganga) | 4.78 | 🟡 Alert | -0.079 |  |
| 2026-05-29 03:03:24 | Ellagawa (Kalu Ganga) | 8.50 | 🟢 Normal | 0.000 |  |
| 2026-05-29 03:03:17 | Norwood (Kelani Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-05-29 03:03:14 | Moragaswewa (Deduru Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-05-29 03:03:02 | Manampitiya (Mahaweli Ganga) | 0.01 | 🟢 Normal | -0.010 |  |
| 2026-05-29 03:02:44 | Nawalapitiya (Mahaweli Ganga) | 1.92 | 🟢 Normal | -0.288 |  |
| 2026-05-29 03:02:39 | Glencourse (Kelani Ganga) | 12.12 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-05-29 03:02:33 | Giriulla (Maha Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-05-29 03:02:25 | Dunamale (Aththanagalu Oya) | 1.76 | 🟢 Normal | 0.000 |  |
| 2026-05-29 03:02:14 | Pitabeddara (Nilwala Ganga) | 2.51 | 🟢 Normal | -0.194 |  |
| 2026-05-29 03:01:31 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-05-29 03:01:12 | Peradeniya (Mahaweli Ganga) | 2.20 | 🟢 Normal | -0.032 |  |
| 2026-05-29 03:00:54 | Moraketiya (Walawe Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-05-29 03:00:49 | Nakkala (Kumbukkan Oya) | 0.67 | 🟢 Normal | -0.010 |  |
| 2026-05-29 03:00:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.54 | 🟠 Minor Flood | 0.036 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-29 03:00:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.54 | 🟠 Minor Flood | 0.036 | 🔺 Rising |
| 2026-05-29 03:07:03 | Panadugama (Nilwala Ganga) | 5.11 | 🟡 Alert | 0.013 | 🔺 Rising |
| 2026-05-29 03:03:27 | Magura (Kalu Ganga) | 4.78 | 🟡 Alert | -0.079 |  |
| 2026-05-29 03:06:01 | Thanamalwila (Kirindi Oya) | 0.74 | 🟢 Normal | 0.065 | 🔺 Rising |
| 2026-05-29 02:02:16 | Kuda Oya (Kirindi Oya) | 1.41 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-05-29 03:09:05 | Hanwella (Kelani Ganga) | 3.90 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-05-29 03:02:39 | Glencourse (Kelani Ganga) | 12.12 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-05-29 03:06:25 | Thalgahagoda (Nilwala Ganga) | 0.76 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-05-29 03:05:34 | Badalgama (Maha Oya) | 2.36 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-29 03:03:14 | Moragaswewa (Deduru Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-05-29 00:02:53 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-05-29 03:02:33 | Giriulla (Maha Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-05-29 03:04:01 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-05-28 18:03:10 | Galgamuwa (Mee Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-05-29 03:03:17 | Norwood (Kelani Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-05-29 03:03:24 | Ellagawa (Kalu Ganga) | 8.50 | 🟢 Normal | 0.000 |  |
| 2026-05-29 03:03:39 | Padiyathalawa (Maduru Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-05-29 03:00:54 | Moraketiya (Walawe Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-05-29 03:01:31 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-05-29 03:02:25 | Dunamale (Aththanagalu Oya) | 1.76 | 🟢 Normal | 0.000 |  |
| 2026-05-29 03:03:43 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-05-29 02:06:29 | Putupaula (Kalu Ganga) | 2.59 | 🟢 Normal | 0.000 |  |
| 2026-05-28 18:02:12 | Thanthirimale (Malwathu Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-05-29 03:03:02 | Manampitiya (Mahaweli Ganga) | 0.01 | 🟢 Normal | -0.010 |  |
| 2026-05-29 03:05:39 | Kithulgala (Kelani Ganga) | 1.84 | 🟢 Normal | -0.010 |  |
| 2026-05-29 03:00:49 | Nakkala (Kumbukkan Oya) | 0.67 | 🟢 Normal | -0.010 |  |
| 2026-05-28 18:32:56 | Weraganthota (Mahaweli Ganga) | -3.27 | 🟢 Normal | -0.013 |  |
| 2026-05-29 03:05:26 | Wellawaya (Kirindi Oya) | 1.08 | 🟢 Normal | -0.028 |  |
| 2026-05-29 03:05:41 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | -0.031 |  |
| 2026-05-29 03:01:12 | Peradeniya (Mahaweli Ganga) | 2.20 | 🟢 Normal | -0.032 |  |
| 2026-05-29 03:11:34 | Thawalama (Gin Ganga) | 3.14 | 🟢 Normal | -0.081 |  |
| 2026-05-29 03:05:36 | Urawa (Nilwala Ganga) | 1.10 | 🟢 Normal | -0.087 |  |
| 2026-05-29 03:15:02 | Holombuwa (Kelani Ganga) | 1.05 | 🟢 Normal | -0.156 |  |
| 2026-05-29 03:06:35 | Rathnapura (Kalu Ganga) | 5.01 | 🟢 Normal | -0.185 |  |
| 2026-05-29 03:02:14 | Pitabeddara (Nilwala Ganga) | 2.51 | 🟢 Normal | -0.194 |  |
| 2026-05-29 03:02:44 | Nawalapitiya (Mahaweli Ganga) | 1.92 | 🟢 Normal | -0.288 |  |
| 2026-05-29 03:04:31 | Deraniyagala (Kelani Ganga) | 1.83 | 🟢 Normal | -0.304 |  |
| 2026-05-29 03:05:57 | Baddegama (Gin Ganga) | 3.10 | 🟢 Normal | -1.800 |  |
| 2026-05-29 03:03:58 | Thaldena (Mahaweli Ganga) | 0.38 | 🟢 Normal | -54.000 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

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

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)