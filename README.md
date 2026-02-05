# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--05_18:08:44-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **64,978 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-05 18:08:44 | Panadugama (Nilwala Ganga) | 2.40 | 🟢 Normal | -0.027 |  |
| 2026-02-05 18:07:58 | Moragaswewa (Deduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-02-05 18:06:38 | Thaldena (Mahaweli Ganga) | 0.52 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-05 18:06:32 | Urawa (Nilwala Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-02-05 18:05:52 | Glencourse (Kelani Ganga) | 8.42 | 🟢 Normal | 0.111 | 🔺 Rising |
| 2026-02-05 18:05:48 | Yaka Wewa (Ma Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-02-05 18:05:46 | Galgamuwa (Mee Oya) | 0.27 | 🟢 Normal | -0.010 |  |
| 2026-02-05 18:05:45 | Weraganthota (Mahaweli Ganga) | -2.55 | 🟢 Normal | -0.046 |  |
| 2026-02-05 18:05:40 | Moraketiya (Walawe Ganga) | 0.81 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-02-05 18:05:30 | Katharagama (Menik Ganga) | 0.06 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-05 18:05:21 | Padiyathalawa (Maduru Oya) | 1.56 | 🟢 Normal | 0.547 | 🔺 Rising |
| 2026-02-05 18:05:15 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-02-05 18:05:15 | Rathnapura (Kalu Ganga) | 0.77 | 🟢 Normal | -0.010 |  |
| 2026-02-05 18:05:00 | Deraniyagala (Kelani Ganga) | 0.16 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-05 18:04:44 | Hanwella (Kelani Ganga) | 0.61 | 🟢 Normal | -0.021 |  |
| 2026-02-05 18:04:30 | Giriulla (Maha Oya) | 0.75 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-05 18:04:23 | Thalgahagoda (Nilwala Ganga) | 0.60 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-02-05 18:04:15 | Dunamale (Aththanagalu Oya) | 0.19 | 🟢 Normal | -0.010 |  |
| 2026-02-05 18:04:13 | Thanthirimale (Malwathu Oya) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-02-05 18:03:43 | Kithulgala (Kelani Ganga) | 1.40 | 🟢 Normal | -0.324 |  |
| 2026-02-05 18:03:38 | Thawalama (Gin Ganga) | 1.23 | 🟢 Normal | -0.032 |  |
| 2026-02-05 18:03:36 | Holombuwa (Kelani Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-02-05 18:03:25 | Peradeniya (Mahaweli Ganga) | 1.35 | 🟢 Normal | 0.178 | 🔺 Rising |
| 2026-02-05 18:03:08 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.157 |  |
| 2026-02-05 18:02:52 | Nakkala (Kumbukkan Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-02-05 18:02:09 | Siyambalanduwa (Heda Oya) | 1.31 | 🟢 Normal | 0.234 | 🔺 Rising |
| 2026-02-05 18:02:08 | Badalgama (Maha Oya) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-02-05 18:01:57 | Putupaula (Kalu Ganga) | 0.85 | 🟢 Normal | -0.051 |  |
| 2026-02-05 18:01:27 | Kuda Oya (Kirindi Oya) | 1.25 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-02-05 18:01:24 | Thanamalwila (Kirindi Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-02-05 18:01:23 | Manampitiya (Mahaweli Ganga) | 0.35 | 🟢 Normal | -1.036 |  |
| 2026-02-05 18:00:50 | Wellawaya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-05 18:00:40 | Pitabeddara (Nilwala Ganga) | 0.44 | 🟢 Normal | -0.032 |  |
| 2026-02-05 18:00:37 | Nawalapitiya (Mahaweli Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-02-05 17:52:46 | Thanthirimale (Malwathu Oya) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-02-05 17:52:45 | Thanthirimale (Malwathu Oya) | 1.59 | 🟢 Normal | 0.000 |  |
| 2026-02-05 17:52:44 | Thanthirimale (Malwathu Oya) | 1.59 | 🟢 Normal | 0.000 |  |
| 2026-02-05 17:52:43 | Thanthirimale (Malwathu Oya) | 1.59 | 🟢 Normal | 0.000 |  |
| 2026-02-05 17:52:41 | Thanthirimale (Malwathu Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-02-05 17:42:20 | Padiyathalawa (Maduru Oya) | 1.35 | 🟢 Normal | 0.547 | 🔺 Rising |
| 2026-02-05 17:42:16 | Padiyathalawa (Maduru Oya) | 0.65 | 🟢 Normal | 0.547 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-05 18:05:21 | Padiyathalawa (Maduru Oya) | 1.56 | 🟢 Normal | 0.547 | 🔺 Rising |
| 2026-02-05 18:02:09 | Siyambalanduwa (Heda Oya) | 1.31 | 🟢 Normal | 0.234 | 🔺 Rising |
| 2026-02-05 18:03:25 | Peradeniya (Mahaweli Ganga) | 1.35 | 🟢 Normal | 0.178 | 🔺 Rising |
| 2026-02-05 18:05:52 | Glencourse (Kelani Ganga) | 8.42 | 🟢 Normal | 0.111 | 🔺 Rising |
| 2026-02-03 05:18:55⌛ | Magura (Kalu Ganga) | 0.88 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2026-02-05 06:07:34 | Baddegama (Gin Ganga) | 1.41 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-02-05 18:04:23 | Thalgahagoda (Nilwala Ganga) | 0.60 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-02-05 18:01:27 | Kuda Oya (Kirindi Oya) | 1.25 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-02-05 18:06:38 | Thaldena (Mahaweli Ganga) | 0.52 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-05 18:00:50 | Wellawaya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-05 18:05:00 | Deraniyagala (Kelani Ganga) | 0.16 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-05 18:04:30 | Giriulla (Maha Oya) | 0.75 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-05 18:05:30 | Katharagama (Menik Ganga) | 0.06 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-05 18:05:40 | Moraketiya (Walawe Ganga) | 0.81 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-02-05 18:02:52 | Nakkala (Kumbukkan Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-02-05 18:07:58 | Moragaswewa (Deduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-02-05 18:00:37 | Nawalapitiya (Mahaweli Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-02-05 18:05:48 | Yaka Wewa (Ma Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-02-03 07:40:09⌛ | Horowpothana (Yan Oya) | 1.76 | 🟢 Normal | 0.000 |  |
| 2026-02-05 18:05:15 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-02-03 06:07:19⌛ | Ellagawa (Kalu Ganga) | 4.23 | 🟢 Normal | 0.000 |  |
| 2026-02-05 18:02:08 | Badalgama (Maha Oya) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-02-05 18:03:36 | Holombuwa (Kelani Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-02-05 18:04:13 | Thanthirimale (Malwathu Oya) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-02-05 18:06:32 | Urawa (Nilwala Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-02-05 18:01:24 | Thanamalwila (Kirindi Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-02-05 18:04:15 | Dunamale (Aththanagalu Oya) | 0.19 | 🟢 Normal | -0.010 |  |
| 2026-02-05 18:05:15 | Rathnapura (Kalu Ganga) | 0.77 | 🟢 Normal | -0.010 |  |
| 2026-02-05 18:05:46 | Galgamuwa (Mee Oya) | 0.27 | 🟢 Normal | -0.010 |  |
| 2026-02-05 18:04:44 | Hanwella (Kelani Ganga) | 0.61 | 🟢 Normal | -0.021 |  |
| 2026-02-05 18:08:44 | Panadugama (Nilwala Ganga) | 2.40 | 🟢 Normal | -0.027 |  |
| 2026-02-05 18:03:38 | Thawalama (Gin Ganga) | 1.23 | 🟢 Normal | -0.032 |  |
| 2026-02-05 18:00:40 | Pitabeddara (Nilwala Ganga) | 0.44 | 🟢 Normal | -0.032 |  |
| 2026-02-05 18:05:45 | Weraganthota (Mahaweli Ganga) | -2.55 | 🟢 Normal | -0.046 |  |
| 2026-02-05 18:01:57 | Putupaula (Kalu Ganga) | 0.85 | 🟢 Normal | -0.051 |  |
| 2026-02-03 05:02:29⌛ | Kalawellawa (Millakanda) (Kalu Ganga) | 2.30 | 🟢 Normal | -0.069 |  |
| 2026-02-05 18:03:08 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.157 |  |
| 2026-02-05 18:03:43 | Kithulgala (Kelani Ganga) | 1.40 | 🟢 Normal | -0.324 |  |
| 2026-02-05 18:01:23 | Manampitiya (Mahaweli Ganga) | 0.35 | 🟢 Normal | -1.036 |  |

## River Water Level Charts by Station

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)