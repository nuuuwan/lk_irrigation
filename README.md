# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--12_05:29:57-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **43,283 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-12 05:29:57 | Magura (Kalu Ganga) | 1.18 | 🟢 Normal | -0.087 |  |
| 2026-01-12 05:22:53 | Dunamale (Aththanagalu Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-01-12 05:21:03 | Holombuwa (Kelani Ganga) | 0.85 | 🟢 Normal | -0.016 |  |
| 2026-01-12 05:20:20 | Rathnapura (Kalu Ganga) | 0.70 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-01-12 05:15:53 | Pitabeddara (Nilwala Ganga) | 0.25 | 🟢 Normal | -418.605 |  |
| 2026-01-12 05:15:10 | Pitabeddara (Nilwala Ganga) | 5.25 | 🟠 Minor Flood | -418.605 |  |
| 2026-01-12 05:11:32 | Panadugama (Nilwala Ganga) | 2.28 | 🟢 Normal | 0.000 |  |
| 2026-01-12 05:10:57 | Urawa (Nilwala Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-01-12 05:10:08 | Thalgahagoda (Nilwala Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-01-12 05:08:03 | Glencourse (Kelani Ganga) | 10.24 | 🟢 Normal | -0.369 |  |
| 2026-01-12 05:06:40 | Thanamalwila (Kirindi Oya) | 1.09 | 🟢 Normal | -0.010 |  |
| 2026-01-12 05:06:08 | Nakkala (Kumbukkan Oya) | 1.15 | 🟢 Normal | -0.005 |  |
| 2026-01-12 05:06:08 | Baddegama (Gin Ganga) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-01-12 05:05:42 | Yaka Wewa (Ma Oya) | 0.85 | 🟢 Normal | -0.019 |  |
| 2026-01-12 05:04:56 | Moragaswewa (Deduru Oya) | 0.62 | 🟢 Normal | -0.024 |  |
| 2026-01-12 05:04:26 | Hanwella (Kelani Ganga) | 0.97 | 🟢 Normal | 0.229 | 🔺 Rising |
| 2026-01-12 05:04:08 | Dunamale (Aththanagalu Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-01-12 05:04:06 | Badalgama (Maha Oya) | 2.15 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-01-12 05:03:50 | Horowpothana (Yan Oya) | 2.28 | 🟢 Normal | -0.027 |  |
| 2026-01-12 05:03:41 | Norwood (Kelani Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-01-12 05:03:38 | Padiyathalawa (Maduru Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-01-12 05:03:14 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-01-12 05:03:09 | Giriulla (Maha Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-01-12 05:03:06 | Thawalama (Gin Ganga) | 1.30 | 🟢 Normal | -0.010 |  |
| 2026-01-12 05:02:55 | Kuda Oya (Kirindi Oya) | 1.37 | 🟢 Normal | -0.018 |  |
| 2026-01-12 05:02:20 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | -0.010 |  |
| 2026-01-12 05:01:58 | Peradeniya (Mahaweli Ganga) | 1.50 | 🟢 Normal | -0.109 |  |
| 2026-01-12 05:01:48 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-01-12 05:01:23 | Manampitiya (Mahaweli Ganga) | 1.98 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2026-01-12 05:01:01 | Ellagawa (Kalu Ganga) | 4.18 | 🟢 Normal | -0.010 |  |
| 2026-01-12 05:00:12 | Wellawaya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-01-12 04:55:52 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | 0.096 | 🔺 Rising |
| 2026-01-12 04:50:09 | Glencourse (Kelani Ganga) | 10.35 | 🟢 Normal | -0.369 |  |
| 2026-01-12 04:39:51 | Moragaswewa (Deduru Oya) | 0.63 | 🟢 Normal | -0.024 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-12 05:04:26 | Hanwella (Kelani Ganga) | 0.97 | 🟢 Normal | 0.229 | 🔺 Rising |
| 2026-01-12 04:55:52 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | 0.096 | 🔺 Rising |
| 2026-01-12 00:11:30 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.60 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2026-01-12 05:01:48 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-01-12 05:01:23 | Manampitiya (Mahaweli Ganga) | 1.98 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2026-01-12 05:04:06 | Badalgama (Maha Oya) | 2.15 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-01-11 18:00:33 | Thanthirimale (Malwathu Oya) | 1.82 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-01-12 05:20:20 | Rathnapura (Kalu Ganga) | 0.70 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-01-12 03:04:23 | Katharagama (Menik Ganga) | 0.01 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-11 18:01:30 | Weraganthota (Mahaweli Ganga) | -1.51 | 🟢 Normal | 0.000 |  |
| 2026-01-12 05:00:12 | Wellawaya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-01-12 03:02:08 | Nawalapitiya (Mahaweli Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-01-12 05:03:09 | Giriulla (Maha Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-01-11 18:02:19 | Galgamuwa (Mee Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-01-12 05:03:41 | Norwood (Kelani Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-01-12 05:06:08 | Baddegama (Gin Ganga) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-01-12 05:11:32 | Panadugama (Nilwala Ganga) | 2.28 | 🟢 Normal | 0.000 |  |
| 2026-01-12 05:03:38 | Padiyathalawa (Maduru Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-01-12 05:03:14 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-01-12 05:22:53 | Dunamale (Aththanagalu Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-01-12 02:10:41 | Thaldena (Mahaweli Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-01-12 05:10:57 | Urawa (Nilwala Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-01-12 05:10:08 | Thalgahagoda (Nilwala Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-01-12 05:06:08 | Nakkala (Kumbukkan Oya) | 1.15 | 🟢 Normal | -0.005 |  |
| 2026-01-12 05:06:40 | Thanamalwila (Kirindi Oya) | 1.09 | 🟢 Normal | -0.010 |  |
| 2026-01-12 05:02:20 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | -0.010 |  |
| 2026-01-12 05:01:01 | Ellagawa (Kalu Ganga) | 4.18 | 🟢 Normal | -0.010 |  |
| 2026-01-12 05:03:06 | Thawalama (Gin Ganga) | 1.30 | 🟢 Normal | -0.010 |  |
| 2026-01-12 05:21:03 | Holombuwa (Kelani Ganga) | 0.85 | 🟢 Normal | -0.016 |  |
| 2026-01-12 05:02:55 | Kuda Oya (Kirindi Oya) | 1.37 | 🟢 Normal | -0.018 |  |
| 2026-01-12 05:05:42 | Yaka Wewa (Ma Oya) | 0.85 | 🟢 Normal | -0.019 |  |
| 2026-01-12 05:04:56 | Moragaswewa (Deduru Oya) | 0.62 | 🟢 Normal | -0.024 |  |
| 2026-01-12 05:03:50 | Horowpothana (Yan Oya) | 2.28 | 🟢 Normal | -0.027 |  |
| 2026-01-12 04:03:46 | Siyambalanduwa (Heda Oya) | 1.14 | 🟢 Normal | -0.029 |  |
| 2026-01-12 04:15:08 | Deraniyagala (Kelani Ganga) | 0.19 | 🟢 Normal | -0.049 |  |
| 2026-01-12 05:29:57 | Magura (Kalu Ganga) | 1.18 | 🟢 Normal | -0.087 |  |
| 2026-01-12 05:01:58 | Peradeniya (Mahaweli Ganga) | 1.50 | 🟢 Normal | -0.109 |  |
| 2026-01-12 05:08:03 | Glencourse (Kelani Ganga) | 10.24 | 🟢 Normal | -0.369 |  |
| 2026-01-12 05:15:53 | Pitabeddara (Nilwala Ganga) | 0.25 | 🟢 Normal | -418.605 |  |

## River Water Level Charts by Station

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)