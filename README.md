# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--07_16:16:38-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **66,725 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-07 16:16:38 | Manampitiya (Mahaweli Ganga) | 2.12 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-02-07 16:14:50 | Yaka Wewa (Ma Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-02-07 16:14:36 | Urawa (Nilwala Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-02-07 16:12:30 | Panadugama (Nilwala Ganga) | 2.16 | 🟢 Normal | 0.000 |  |
| 2026-02-07 16:11:32 | Pitabeddara (Nilwala Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-02-07 16:10:56 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-02-07 16:09:18 | Galgamuwa (Mee Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-02-07 16:08:24 | Peradeniya (Mahaweli Ganga) | 1.18 | 🟢 Normal | -0.018 |  |
| 2026-02-07 16:06:37 | Padiyathalawa (Maduru Oya) | 1.16 | 🟢 Normal | -0.039 |  |
| 2026-02-07 16:06:26 | Baddegama (Gin Ganga) | 1.33 | 🟢 Normal | -0.072 |  |
| 2026-02-07 16:06:21 | Thawalama (Gin Ganga) | 1.16 | 🟢 Normal | -0.010 |  |
| 2026-02-07 16:06:11 | Magura (Kalu Ganga) | 1.21 | 🟢 Normal | -0.047 |  |
| 2026-02-07 16:05:44 | Putupaula (Kalu Ganga) | 0.78 | 🟢 Normal | 0.171 | 🔺 Rising |
| 2026-02-07 16:05:30 | Holombuwa (Kelani Ganga) | 0.33 | 🟢 Normal | -0.010 |  |
| 2026-02-07 16:04:31 | Dunamale (Aththanagalu Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-02-07 16:04:14 | Thanamalwila (Kirindi Oya) | 0.51 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-07 16:04:08 | Thaldena (Mahaweli Ganga) | 0.78 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-02-07 16:03:57 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.07 | 🟢 Normal | -0.069 |  |
| 2026-02-07 16:03:56 | Ellagawa (Kalu Ganga) | 4.26 | 🟢 Normal | -0.019 |  |
| 2026-02-07 16:03:54 | Siyambalanduwa (Heda Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-02-07 16:03:43 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-02-07 16:03:20 | Hanwella (Kelani Ganga) | 0.60 | 🟢 Normal | -0.010 |  |
| 2026-02-07 16:03:08 | Kithulgala (Kelani Ganga) | 1.49 | 🟢 Normal | 0.000 |  |
| 2026-02-07 16:02:54 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-02-07 16:02:51 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-02-07 16:02:47 | Horowpothana (Yan Oya) | 2.52 | 🟢 Normal | -0.037 |  |
| 2026-02-07 16:02:47 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-07 16:02:43 | Glencourse (Kelani Ganga) | 8.51 | 🟢 Normal | -0.030 |  |
| 2026-02-07 16:02:42 | Deraniyagala (Kelani Ganga) | 0.08 | 🟢 Normal | -0.010 |  |
| 2026-02-07 16:02:35 | Moraketiya (Walawe Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-02-07 16:02:23 | Nakkala (Kumbukkan Oya) | 1.07 | 🟢 Normal | -0.010 |  |
| 2026-02-07 16:02:13 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-02-07 16:01:18 | Moragaswewa (Deduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-02-07 16:00:58 | Weraganthota (Mahaweli Ganga) | -2.05 | 🟢 Normal | -0.010 |  |
| 2026-02-07 16:00:57 | Thanthirimale (Malwathu Oya) | 1.86 | 🟢 Normal | -0.010 |  |
| 2026-02-07 16:00:52 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-02-07 16:00:40 | Nawalapitiya (Mahaweli Ganga) | 0.68 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-07 16:05:44 | Putupaula (Kalu Ganga) | 0.78 | 🟢 Normal | 0.171 | 🔺 Rising |
| 2026-02-07 16:10:56 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-02-07 16:04:14 | Thanamalwila (Kirindi Oya) | 0.51 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-07 16:04:08 | Thaldena (Mahaweli Ganga) | 0.78 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-02-07 16:16:38 | Manampitiya (Mahaweli Ganga) | 2.12 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-02-07 16:03:08 | Kithulgala (Kelani Ganga) | 1.49 | 🟢 Normal | 0.000 |  |
| 2026-02-07 16:00:52 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-02-07 16:01:18 | Moragaswewa (Deduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-02-07 16:00:40 | Nawalapitiya (Mahaweli Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-02-07 16:14:50 | Yaka Wewa (Ma Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-02-07 16:03:43 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-02-07 16:09:18 | Galgamuwa (Mee Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-02-07 16:11:32 | Pitabeddara (Nilwala Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-02-07 16:02:51 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-02-07 16:12:30 | Panadugama (Nilwala Ganga) | 2.16 | 🟢 Normal | 0.000 |  |
| 2026-02-07 16:02:35 | Moraketiya (Walawe Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-02-07 16:03:54 | Siyambalanduwa (Heda Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-02-07 16:04:31 | Dunamale (Aththanagalu Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-02-07 16:02:54 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-02-07 16:02:47 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-07 16:14:36 | Urawa (Nilwala Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-02-07 16:02:13 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-02-07 16:02:23 | Nakkala (Kumbukkan Oya) | 1.07 | 🟢 Normal | -0.010 |  |
| 2026-02-07 16:05:30 | Holombuwa (Kelani Ganga) | 0.33 | 🟢 Normal | -0.010 |  |
| 2026-02-07 16:03:20 | Hanwella (Kelani Ganga) | 0.60 | 🟢 Normal | -0.010 |  |
| 2026-02-07 16:02:42 | Deraniyagala (Kelani Ganga) | 0.08 | 🟢 Normal | -0.010 |  |
| 2026-02-07 16:06:21 | Thawalama (Gin Ganga) | 1.16 | 🟢 Normal | -0.010 |  |
| 2026-02-07 16:00:58 | Weraganthota (Mahaweli Ganga) | -2.05 | 🟢 Normal | -0.010 |  |
| 2026-02-07 16:00:57 | Thanthirimale (Malwathu Oya) | 1.86 | 🟢 Normal | -0.010 |  |
| 2026-02-07 16:08:24 | Peradeniya (Mahaweli Ganga) | 1.18 | 🟢 Normal | -0.018 |  |
| 2026-02-07 16:03:56 | Ellagawa (Kalu Ganga) | 4.26 | 🟢 Normal | -0.019 |  |
| 2026-02-07 15:03:28 | Rathnapura (Kalu Ganga) | 0.89 | 🟢 Normal | -0.022 |  |
| 2026-02-07 13:11:30 | Thalgahagoda (Nilwala Ganga) | 0.24 | 🟢 Normal | -0.026 |  |
| 2026-02-07 16:02:43 | Glencourse (Kelani Ganga) | 8.51 | 🟢 Normal | -0.030 |  |
| 2026-02-07 16:02:47 | Horowpothana (Yan Oya) | 2.52 | 🟢 Normal | -0.037 |  |
| 2026-02-07 16:06:37 | Padiyathalawa (Maduru Oya) | 1.16 | 🟢 Normal | -0.039 |  |
| 2026-02-07 16:06:11 | Magura (Kalu Ganga) | 1.21 | 🟢 Normal | -0.047 |  |
| 2026-02-07 16:03:57 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.07 | 🟢 Normal | -0.069 |  |
| 2026-02-07 16:06:26 | Baddegama (Gin Ganga) | 1.33 | 🟢 Normal | -0.072 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

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

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)