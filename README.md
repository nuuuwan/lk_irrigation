# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--07_01:17:18-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **38,642 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **24** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-07 01:17:18 | Thawalama (Gin Ganga) | 1.52 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-01-07 01:08:43 | Katharagama (Menik Ganga) | 0.57 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-01-07 01:07:49 | Thanamalwila (Kirindi Oya) | 1.32 | 🟢 Normal | -0.009 |  |
| 2026-01-07 01:07:24 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-01-07 01:07:22 | Nakkala (Kumbukkan Oya) | 1.60 | 🟢 Normal | -0.009 |  |
| 2026-01-07 01:06:25 | Badalgama (Maha Oya) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-01-07 01:04:45 | Deraniyagala (Kelani Ganga) | 0.31 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-01-07 01:04:34 | Padiyathalawa (Maduru Oya) | 1.40 | 🟢 Normal | -0.104 |  |
| 2026-01-07 01:04:22 | Rathnapura (Kalu Ganga) | 0.86 | 🟢 Normal | -0.010 |  |
| 2026-01-07 01:04:19 | Ellagawa (Kalu Ganga) | 4.36 | 🟢 Normal | -0.012 |  |
| 2026-01-07 01:04:18 | Manampitiya (Mahaweli Ganga) | 3.59 | 🟡 Alert | -0.060 |  |
| 2026-01-07 01:04:17 | Giriulla (Maha Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-01-07 01:03:54 | Siyambalanduwa (Heda Oya) | 2.29 | 🟢 Normal | -0.109 |  |
| 2026-01-07 01:03:36 | Baddegama (Gin Ganga) | 1.41 | 🟢 Normal | 0.000 |  |
| 2026-01-07 01:03:16 | Norwood (Kelani Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-01-07 01:03:11 | Moragaswewa (Deduru Oya) | 0.60 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-07 01:03:01 | Hanwella (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-01-07 01:02:38 | Peradeniya (Mahaweli Ganga) | 2.40 | 🟢 Normal | -0.275 |  |
| 2026-01-07 01:02:33 | Moraketiya (Walawe Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-01-07 01:02:18 | Kuda Oya (Kirindi Oya) | 1.41 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-07 01:00:37 | Horowpothana (Yan Oya) | 2.89 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-01-07 01:00:11 | Kithulgala (Kelani Ganga) | 1.50 | 🟢 Normal | -0.062 |  |
| 2026-01-07 00:54:48 | Urawa (Nilwala Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-01-07 00:29:39 | Thalgahagoda (Nilwala Ganga) | 0.43 | 🟢 Normal | -0.015 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-07 01:04:18 | Manampitiya (Mahaweli Ganga) | 3.59 | 🟡 Alert | -0.060 |  |
| 2026-01-07 01:08:43 | Katharagama (Menik Ganga) | 0.57 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-01-07 01:04:45 | Deraniyagala (Kelani Ganga) | 0.31 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-01-07 00:04:23 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-01-07 01:00:37 | Horowpothana (Yan Oya) | 2.89 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-01-07 01:17:18 | Thawalama (Gin Ganga) | 1.52 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-01-06 18:00:39 | Thanthirimale (Malwathu Oya) | 1.73 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-07 01:03:11 | Moragaswewa (Deduru Oya) | 0.60 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-07 01:02:18 | Kuda Oya (Kirindi Oya) | 1.41 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-06 18:02:01 | Weraganthota (Mahaweli Ganga) | -0.56 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-07 00:03:49 | Thaldena (Mahaweli Ganga) | 0.99 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-07 00:18:35 | Wellawaya (Kirindi Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-01-07 00:03:12 | Nawalapitiya (Mahaweli Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-01-07 00:03:26 | Yaka Wewa (Ma Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-01-07 01:04:17 | Giriulla (Maha Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-01-06 18:03:13 | Galgamuwa (Mee Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-01-07 01:03:16 | Norwood (Kelani Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-01-07 01:03:01 | Hanwella (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-01-07 01:03:36 | Baddegama (Gin Ganga) | 1.41 | 🟢 Normal | 0.000 |  |
| 2026-01-07 00:08:40 | Glencourse (Kelani Ganga) | 8.68 | 🟢 Normal | 0.000 |  |
| 2026-01-07 01:02:33 | Moraketiya (Walawe Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-01-07 00:03:09 | Dunamale (Aththanagalu Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-01-07 01:06:25 | Badalgama (Maha Oya) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-01-07 01:07:24 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-01-07 00:54:48 | Urawa (Nilwala Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-01-06 22:26:10 | Pitabeddara (Nilwala Ganga) | 0.75 | 🟢 Normal | -0.008 |  |
| 2026-01-07 01:07:22 | Nakkala (Kumbukkan Oya) | 1.60 | 🟢 Normal | -0.009 |  |
| 2026-01-07 01:07:49 | Thanamalwila (Kirindi Oya) | 1.32 | 🟢 Normal | -0.009 |  |
| 2026-01-06 22:08:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.68 | 🟢 Normal | -0.010 |  |
| 2026-01-07 00:06:15 | Magura (Kalu Ganga) | 0.82 | 🟢 Normal | -0.010 |  |
| 2026-01-07 01:04:22 | Rathnapura (Kalu Ganga) | 0.86 | 🟢 Normal | -0.010 |  |
| 2026-01-07 01:04:19 | Ellagawa (Kalu Ganga) | 4.36 | 🟢 Normal | -0.012 |  |
| 2026-01-07 00:29:39 | Thalgahagoda (Nilwala Ganga) | 0.43 | 🟢 Normal | -0.015 |  |
| 2026-01-07 00:06:21 | Panadugama (Nilwala Ganga) | 2.62 | 🟢 Normal | -0.031 |  |
| 2026-01-07 01:00:11 | Kithulgala (Kelani Ganga) | 1.50 | 🟢 Normal | -0.062 |  |
| 2026-01-07 00:05:18 | Putupaula (Kalu Ganga) | 0.43 | 🟢 Normal | -0.063 |  |
| 2026-01-07 01:04:34 | Padiyathalawa (Maduru Oya) | 1.40 | 🟢 Normal | -0.104 |  |
| 2026-01-07 01:03:54 | Siyambalanduwa (Heda Oya) | 2.29 | 🟢 Normal | -0.109 |  |
| 2026-01-07 01:02:38 | Peradeniya (Mahaweli Ganga) | 2.40 | 🟢 Normal | -0.275 |  |

## River Water Level Charts by Station

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)