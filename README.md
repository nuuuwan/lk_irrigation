# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--06_22:18:45-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **38,553 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-06 22:18:45 | Urawa (Nilwala Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-01-06 22:16:25 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.075 |  |
| 2026-01-06 22:08:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.68 | 🟢 Normal | -0.010 |  |
| 2026-01-06 22:08:00 | Panadugama (Nilwala Ganga) | 2.66 | 🟢 Normal | 0.000 |  |
| 2026-01-06 22:06:46 | Katharagama (Menik Ganga) | 0.49 | 🟢 Normal | -0.031 |  |
| 2026-01-06 22:06:38 | Thawalama (Gin Ganga) | 1.45 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-01-06 22:05:33 | Rathnapura (Kalu Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-01-06 22:04:59 | Kithulgala (Kelani Ganga) | 1.60 | 🟢 Normal | -0.086 |  |
| 2026-01-06 22:04:54 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-01-06 22:04:54 | Badalgama (Maha Oya) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-01-06 22:04:51 | Wellawaya (Kirindi Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-01-06 22:04:41 | Thalgahagoda (Nilwala Ganga) | 0.47 | 🟢 Normal | -0.031 |  |
| 2026-01-06 22:04:41 | Thanamalwila (Kirindi Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-01-06 22:04:36 | Nakkala (Kumbukkan Oya) | 1.63 | 🟢 Normal | -0.066 |  |
| 2026-01-06 22:04:25 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | -0.010 |  |
| 2026-01-06 22:04:11 | Ellagawa (Kalu Ganga) | 4.38 | 🟢 Normal | -0.010 |  |
| 2026-01-06 22:04:08 | Baddegama (Gin Ganga) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-01-06 22:03:44 | Thaldena (Mahaweli Ganga) | 1.05 | 🟢 Normal | -0.058 |  |
| 2026-01-06 22:03:40 | Deraniyagala (Kelani Ganga) | 0.22 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-01-06 22:03:36 | Nawalapitiya (Mahaweli Ganga) | 0.86 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-06 22:03:14 | Giriulla (Maha Oya) | 0.96 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-06 22:03:04 | Putupaula (Kalu Ganga) | 0.56 | 🟢 Normal | -0.088 |  |
| 2026-01-06 22:03:01 | Norwood (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-01-06 22:02:54 | Hanwella (Kelani Ganga) | 0.45 | 🟢 Normal | -0.010 |  |
| 2026-01-06 22:02:49 | Peradeniya (Mahaweli Ganga) | 2.68 | 🟢 Normal | 0.093 | 🔺 Rising |
| 2026-01-06 22:02:45 | Dunamale (Aththanagalu Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-01-06 22:02:23 | Siyambalanduwa (Heda Oya) | 2.63 | 🟢 Normal | -0.282 |  |
| 2026-01-06 22:02:21 | Moragaswewa (Deduru Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-01-06 22:02:09 | Magura (Kalu Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-01-06 22:02:08 | Manampitiya (Mahaweli Ganga) | 3.75 | 🟡 Alert | -0.048 |  |
| 2026-01-06 22:01:50 | Yaka Wewa (Ma Oya) | 0.90 | 🟢 Normal | -0.010 |  |
| 2026-01-06 22:01:47 | Kuda Oya (Kirindi Oya) | 1.39 | 🟢 Normal | 0.000 |  |
| 2026-01-06 22:01:21 | Horowpothana (Yan Oya) | 2.79 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-01-06 22:01:14 | Padiyathalawa (Maduru Oya) | 1.60 | 🟢 Normal | -0.053 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-06 22:02:08 | Manampitiya (Mahaweli Ganga) | 3.75 | 🟡 Alert | -0.048 |  |
| 2026-01-06 22:02:49 | Peradeniya (Mahaweli Ganga) | 2.68 | 🟢 Normal | 0.093 | 🔺 Rising |
| 2026-01-06 22:01:21 | Horowpothana (Yan Oya) | 2.79 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-01-06 22:06:38 | Thawalama (Gin Ganga) | 1.45 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-01-06 22:03:40 | Deraniyagala (Kelani Ganga) | 0.22 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-01-06 18:00:39 | Thanthirimale (Malwathu Oya) | 1.73 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-06 22:03:14 | Giriulla (Maha Oya) | 0.96 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-06 22:03:36 | Nawalapitiya (Mahaweli Ganga) | 0.86 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-06 18:02:01 | Weraganthota (Mahaweli Ganga) | -0.56 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-06 22:04:51 | Wellawaya (Kirindi Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-01-06 22:02:21 | Moragaswewa (Deduru Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-01-06 18:03:13 | Galgamuwa (Mee Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-01-06 22:02:09 | Magura (Kalu Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-01-06 22:03:01 | Norwood (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-01-06 22:04:08 | Baddegama (Gin Ganga) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-01-06 22:08:00 | Panadugama (Nilwala Ganga) | 2.66 | 🟢 Normal | 0.000 |  |
| 2026-01-06 21:07:21 | Glencourse (Kelani Ganga) | 8.65 | 🟢 Normal | 0.000 |  |
| 2026-01-06 22:04:54 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-01-06 22:02:45 | Dunamale (Aththanagalu Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-01-06 22:04:54 | Badalgama (Maha Oya) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-01-06 22:05:33 | Rathnapura (Kalu Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-01-06 22:18:45 | Urawa (Nilwala Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-01-06 22:01:47 | Kuda Oya (Kirindi Oya) | 1.39 | 🟢 Normal | 0.000 |  |
| 2026-01-06 22:04:41 | Thanamalwila (Kirindi Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-01-06 22:04:11 | Ellagawa (Kalu Ganga) | 4.38 | 🟢 Normal | -0.010 |  |
| 2026-01-06 22:04:25 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | -0.010 |  |
| 2026-01-06 22:08:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.68 | 🟢 Normal | -0.010 |  |
| 2026-01-06 22:02:54 | Hanwella (Kelani Ganga) | 0.45 | 🟢 Normal | -0.010 |  |
| 2026-01-06 22:01:50 | Yaka Wewa (Ma Oya) | 0.90 | 🟢 Normal | -0.010 |  |
| 2026-01-06 21:10:02 | Pitabeddara (Nilwala Ganga) | 0.76 | 🟢 Normal | -0.026 |  |
| 2026-01-06 22:06:46 | Katharagama (Menik Ganga) | 0.49 | 🟢 Normal | -0.031 |  |
| 2026-01-06 22:04:41 | Thalgahagoda (Nilwala Ganga) | 0.47 | 🟢 Normal | -0.031 |  |
| 2026-01-06 22:01:14 | Padiyathalawa (Maduru Oya) | 1.60 | 🟢 Normal | -0.053 |  |
| 2026-01-06 22:03:44 | Thaldena (Mahaweli Ganga) | 1.05 | 🟢 Normal | -0.058 |  |
| 2026-01-06 22:04:36 | Nakkala (Kumbukkan Oya) | 1.63 | 🟢 Normal | -0.066 |  |
| 2026-01-06 22:16:25 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.075 |  |
| 2026-01-06 22:04:59 | Kithulgala (Kelani Ganga) | 1.60 | 🟢 Normal | -0.086 |  |
| 2026-01-06 22:03:04 | Putupaula (Kalu Ganga) | 0.56 | 🟢 Normal | -0.088 |  |
| 2026-01-06 22:02:23 | Siyambalanduwa (Heda Oya) | 2.63 | 🟢 Normal | -0.282 |  |

## River Water Level Charts by Station

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)