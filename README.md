# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--07_14:20:23-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **118,667 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-07 14:20:23 | Baddegama (Gin Ganga) | 0.85 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-04-07 14:14:41 | Dunamale (Aththanagalu Oya) | 0.66 | 🟢 Normal | -0.009 |  |
| 2026-04-07 14:13:14 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-04-07 14:12:46 | Panadugama (Nilwala Ganga) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-04-07 14:10:29 | Rathnapura (Kalu Ganga) | 0.39 | 🟢 Normal | -0.035 |  |
| 2026-04-07 14:09:32 | Glencourse (Kelani Ganga) | 8.48 | 🟢 Normal | -0.027 |  |
| 2026-04-07 14:08:46 | Urawa (Nilwala Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-04-07 14:08:28 | Peradeniya (Mahaweli Ganga) | 1.02 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-04-07 14:07:41 | Galgamuwa (Mee Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-04-07 14:07:31 | Kithulgala (Kelani Ganga) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-04-07 14:05:31 | Kuda Oya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-04-07 14:05:05 | Holombuwa (Kelani Ganga) | 0.34 | 🟢 Normal | -0.010 |  |
| 2026-04-07 14:04:57 | Badalgama (Maha Oya) | 2.18 | 🟢 Normal | -0.021 |  |
| 2026-04-07 14:04:45 | Magura (Kalu Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-04-07 14:04:42 | Thaldena (Mahaweli Ganga) | 0.23 | 🟢 Normal | -0.010 |  |
| 2026-04-07 14:04:04 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-04-07 14:03:48 | Pitabeddara (Nilwala Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-04-07 14:03:47 | Thanamalwila (Kirindi Oya) | 0.40 | 🟢 Normal | -0.010 |  |
| 2026-04-07 14:03:01 | Hanwella (Kelani Ganga) | 0.59 | 🟢 Normal | -0.050 |  |
| 2026-04-07 14:02:55 | Padiyathalawa (Maduru Oya) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-04-07 14:02:53 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.167 | 🔺 Rising |
| 2026-04-07 14:02:40 | Putupaula (Kalu Ganga) | 0.53 | 🟢 Normal | 0.179 | 🔺 Rising |
| 2026-04-07 14:02:39 | Giriulla (Maha Oya) | 1.02 | 🟢 Normal | -0.021 |  |
| 2026-04-07 14:02:20 | Deraniyagala (Kelani Ganga) | 0.07 | 🟢 Normal | -0.020 |  |
| 2026-04-07 14:02:15 | Nawalapitiya (Mahaweli Ganga) | 0.55 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-07 14:02:15 | Ellagawa (Kalu Ganga) | 4.10 | 🟢 Normal | -0.020 |  |
| 2026-04-07 14:02:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.29 | 🟢 Normal | -0.020 |  |
| 2026-04-07 14:01:59 | Norwood (Kelani Ganga) | 0.44 | 🟢 Normal | -0.010 |  |
| 2026-04-07 14:01:54 | Weraganthota (Mahaweli Ganga) | -2.73 | 🟢 Normal | -0.180 |  |
| 2026-04-07 14:01:53 | Thawalama (Gin Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-04-07 14:01:51 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-04-07 14:01:36 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-07 14:01:23 | Thanthirimale (Malwathu Oya) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-04-07 14:01:16 | Moragaswewa (Deduru Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-04-07 14:00:42 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-04-07 14:00:14 | Wellawaya (Kirindi Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-04-07 14:00:13 | Manampitiya (Mahaweli Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-04-07 14:00:12 | Nakkala (Kumbukkan Oya) | 0.70 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-07 14:02:40 | Putupaula (Kalu Ganga) | 0.53 | 🟢 Normal | 0.179 | 🔺 Rising |
| 2026-04-07 14:02:53 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.167 | 🔺 Rising |
| 2026-04-07 14:02:15 | Nawalapitiya (Mahaweli Ganga) | 0.55 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-07 14:08:28 | Peradeniya (Mahaweli Ganga) | 1.02 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-04-07 14:20:23 | Baddegama (Gin Ganga) | 0.85 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-04-07 14:07:31 | Kithulgala (Kelani Ganga) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-04-07 14:00:14 | Wellawaya (Kirindi Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-04-07 14:00:12 | Nakkala (Kumbukkan Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-04-07 14:01:16 | Moragaswewa (Deduru Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-04-07 14:01:36 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-07 14:00:42 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-04-07 14:07:41 | Galgamuwa (Mee Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-04-07 14:04:45 | Magura (Kalu Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-04-07 14:03:48 | Pitabeddara (Nilwala Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-04-07 14:12:46 | Panadugama (Nilwala Ganga) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-04-07 14:02:55 | Padiyathalawa (Maduru Oya) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-04-07 14:01:51 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-04-07 14:04:04 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-04-07 14:13:14 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-04-07 14:00:13 | Manampitiya (Mahaweli Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-04-07 14:01:23 | Thanthirimale (Malwathu Oya) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-04-07 14:01:53 | Thawalama (Gin Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-04-07 14:08:46 | Urawa (Nilwala Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-04-07 14:05:31 | Kuda Oya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-04-07 14:14:41 | Dunamale (Aththanagalu Oya) | 0.66 | 🟢 Normal | -0.009 |  |
| 2026-04-07 14:03:47 | Thanamalwila (Kirindi Oya) | 0.40 | 🟢 Normal | -0.010 |  |
| 2026-04-07 14:01:59 | Norwood (Kelani Ganga) | 0.44 | 🟢 Normal | -0.010 |  |
| 2026-04-07 14:04:42 | Thaldena (Mahaweli Ganga) | 0.23 | 🟢 Normal | -0.010 |  |
| 2026-04-07 14:05:05 | Holombuwa (Kelani Ganga) | 0.34 | 🟢 Normal | -0.010 |  |
| 2026-04-07 14:02:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.29 | 🟢 Normal | -0.020 |  |
| 2026-04-07 14:02:15 | Ellagawa (Kalu Ganga) | 4.10 | 🟢 Normal | -0.020 |  |
| 2026-04-07 14:02:20 | Deraniyagala (Kelani Ganga) | 0.07 | 🟢 Normal | -0.020 |  |
| 2026-04-07 14:04:57 | Badalgama (Maha Oya) | 2.18 | 🟢 Normal | -0.021 |  |
| 2026-04-07 14:02:39 | Giriulla (Maha Oya) | 1.02 | 🟢 Normal | -0.021 |  |
| 2026-04-07 12:54:27 | Thalgahagoda (Nilwala Ganga) | 0.18 | 🟢 Normal | -0.026 |  |
| 2026-04-07 14:09:32 | Glencourse (Kelani Ganga) | 8.48 | 🟢 Normal | -0.027 |  |
| 2026-04-07 14:10:29 | Rathnapura (Kalu Ganga) | 0.39 | 🟢 Normal | -0.035 |  |
| 2026-04-07 14:03:01 | Hanwella (Kelani Ganga) | 0.59 | 🟢 Normal | -0.050 |  |
| 2026-04-07 14:01:54 | Weraganthota (Mahaweli Ganga) | -2.73 | 🟢 Normal | -0.180 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)