# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--27_18:08:46-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **136,650 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-27 18:08:46 | Kithulgala (Kelani Ganga) | 1.64 | 🟢 Normal | -0.089 |  |
| 2026-04-27 18:06:51 | Holombuwa (Kelani Ganga) | 1.30 | 🟢 Normal | 0.713 | 🔺 Rising |
| 2026-04-27 18:06:06 | Dunamale (Aththanagalu Oya) | 1.04 | 🟢 Normal | 0.097 | 🔺 Rising |
| 2026-04-27 18:05:40 | Peradeniya (Mahaweli Ganga) | 1.45 | 🟢 Normal | -0.039 |  |
| 2026-04-27 18:05:39 | Rathnapura (Kalu Ganga) | 1.20 | 🟢 Normal | -0.031 |  |
| 2026-04-27 18:05:31 | Padiyathalawa (Maduru Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-04-27 18:05:30 | Galgamuwa (Mee Oya) | 0.15 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-27 18:05:04 | Thawalama (Gin Ganga) | 1.42 | 🟢 Normal | 0.174 | 🔺 Rising |
| 2026-04-27 18:05:02 | Baddegama (Gin Ganga) | 1.68 | 🟢 Normal | -0.019 |  |
| 2026-04-27 18:04:49 | Magura (Kalu Ganga) | 1.28 | 🟢 Normal | -0.019 |  |
| 2026-04-27 18:04:48 | Katharagama (Menik Ganga) | 0.10 | 🟢 Normal | -0.021 |  |
| 2026-04-27 18:04:32 | Urawa (Nilwala Ganga) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-04-27 18:04:29 | Glencourse (Kelani Ganga) | 8.75 | 🟢 Normal | -0.030 |  |
| 2026-04-27 18:04:01 | Deraniyagala (Kelani Ganga) | 0.31 | 🟢 Normal | -0.020 |  |
| 2026-04-27 18:03:47 | Wellawaya (Kirindi Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-04-27 18:03:10 | Norwood (Kelani Ganga) | 0.74 | 🟢 Normal | -0.020 |  |
| 2026-04-27 18:03:09 | Hanwella (Kelani Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-04-27 18:03:08 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-27 18:03:04 | Thanthirimale (Malwathu Oya) | 1.84 | 🟢 Normal | 0.000 |  |
| 2026-04-27 18:02:57 | Moragaswewa (Deduru Oya) | 0.45 | 🟢 Normal | -0.010 |  |
| 2026-04-27 18:02:43 | Badalgama (Maha Oya) | 2.50 | 🟢 Normal | -0.022 |  |
| 2026-04-27 18:02:33 | Giriulla (Maha Oya) | 1.53 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-04-27 18:02:24 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.54 | 🟢 Normal | 0.000 |  |
| 2026-04-27 18:02:17 | Thanamalwila (Kirindi Oya) | 0.74 | 🟢 Normal | -0.010 |  |
| 2026-04-27 18:01:58 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | -0.010 |  |
| 2026-04-27 18:01:58 | Ellagawa (Kalu Ganga) | 5.08 | 🟢 Normal | 0.117 | 🔺 Rising |
| 2026-04-27 18:01:41 | Weraganthota (Mahaweli Ganga) | -3.25 | 🟢 Normal | 0.000 |  |
| 2026-04-27 18:01:31 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.030 |  |
| 2026-04-27 18:01:27 | Thaldena (Mahaweli Ganga) | 0.27 | 🟢 Normal | -0.010 |  |
| 2026-04-27 18:01:21 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | -0.010 |  |
| 2026-04-27 18:01:13 | Kuda Oya (Kirindi Oya) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-04-27 18:01:10 | Manampitiya (Mahaweli Ganga) | -0.02 | 🟢 Normal | -0.013 |  |
| 2026-04-27 18:01:09 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-27 18:00:57 | Pitabeddara (Nilwala Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-04-27 18:00:50 | Putupaula (Kalu Ganga) | 0.68 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-04-27 18:00:28 | Nawalapitiya (Mahaweli Ganga) | 0.78 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-27 18:00:10 | Thalgahagoda (Nilwala Ganga) | 0.48 | 🟢 Normal | -0.011 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-27 18:06:51 | Holombuwa (Kelani Ganga) | 1.30 | 🟢 Normal | 0.713 | 🔺 Rising |
| 2026-04-27 18:05:04 | Thawalama (Gin Ganga) | 1.42 | 🟢 Normal | 0.174 | 🔺 Rising |
| 2026-04-27 18:01:58 | Ellagawa (Kalu Ganga) | 5.08 | 🟢 Normal | 0.117 | 🔺 Rising |
| 2026-04-27 18:06:06 | Dunamale (Aththanagalu Oya) | 1.04 | 🟢 Normal | 0.097 | 🔺 Rising |
| 2026-04-27 18:02:33 | Giriulla (Maha Oya) | 1.53 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-04-27 18:00:50 | Putupaula (Kalu Ganga) | 0.68 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-04-27 18:03:08 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-27 18:00:28 | Nawalapitiya (Mahaweli Ganga) | 0.78 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-27 18:05:30 | Galgamuwa (Mee Oya) | 0.15 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-27 18:01:41 | Weraganthota (Mahaweli Ganga) | -3.25 | 🟢 Normal | 0.000 |  |
| 2026-04-27 18:03:47 | Wellawaya (Kirindi Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-04-27 18:01:09 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-27 17:01:18 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-27 18:00:57 | Pitabeddara (Nilwala Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-04-27 18:03:09 | Hanwella (Kelani Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-04-27 17:28:25 | Panadugama (Nilwala Ganga) | 2.84 | 🟢 Normal | 0.000 |  |
| 2026-04-27 18:05:31 | Padiyathalawa (Maduru Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-04-27 18:03:04 | Thanthirimale (Malwathu Oya) | 1.84 | 🟢 Normal | 0.000 |  |
| 2026-04-27 18:04:32 | Urawa (Nilwala Ganga) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-04-27 18:01:13 | Kuda Oya (Kirindi Oya) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-04-27 18:02:24 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.54 | 🟢 Normal | 0.000 |  |
| 2026-04-27 18:01:21 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | -0.010 |  |
| 2026-04-27 18:02:57 | Moragaswewa (Deduru Oya) | 0.45 | 🟢 Normal | -0.010 |  |
| 2026-04-27 18:02:17 | Thanamalwila (Kirindi Oya) | 0.74 | 🟢 Normal | -0.010 |  |
| 2026-04-27 18:01:58 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | -0.010 |  |
| 2026-04-27 18:01:27 | Thaldena (Mahaweli Ganga) | 0.27 | 🟢 Normal | -0.010 |  |
| 2026-04-27 18:00:10 | Thalgahagoda (Nilwala Ganga) | 0.48 | 🟢 Normal | -0.011 |  |
| 2026-04-27 18:01:10 | Manampitiya (Mahaweli Ganga) | -0.02 | 🟢 Normal | -0.013 |  |
| 2026-04-27 18:04:49 | Magura (Kalu Ganga) | 1.28 | 🟢 Normal | -0.019 |  |
| 2026-04-27 18:05:02 | Baddegama (Gin Ganga) | 1.68 | 🟢 Normal | -0.019 |  |
| 2026-04-27 18:04:01 | Deraniyagala (Kelani Ganga) | 0.31 | 🟢 Normal | -0.020 |  |
| 2026-04-27 18:03:10 | Norwood (Kelani Ganga) | 0.74 | 🟢 Normal | -0.020 |  |
| 2026-04-27 18:04:48 | Katharagama (Menik Ganga) | 0.10 | 🟢 Normal | -0.021 |  |
| 2026-04-27 18:02:43 | Badalgama (Maha Oya) | 2.50 | 🟢 Normal | -0.022 |  |
| 2026-04-27 18:01:31 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.030 |  |
| 2026-04-27 18:04:29 | Glencourse (Kelani Ganga) | 8.75 | 🟢 Normal | -0.030 |  |
| 2026-04-27 18:05:39 | Rathnapura (Kalu Ganga) | 1.20 | 🟢 Normal | -0.031 |  |
| 2026-04-27 18:05:40 | Peradeniya (Mahaweli Ganga) | 1.45 | 🟢 Normal | -0.039 |  |
| 2026-04-27 18:08:46 | Kithulgala (Kelani Ganga) | 1.64 | 🟢 Normal | -0.089 |  |

## River Water Level Charts by Station

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)