# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--05_15:10:41-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **143,626 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-05 15:10:41 | Urawa (Nilwala Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-05-05 15:09:23 | Thalgahagoda (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-05-05 15:09:21 | Rathnapura (Kalu Ganga) | 1.09 | 🟢 Normal | -0.025 |  |
| 2026-05-05 15:08:42 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2026-05-05 15:06:27 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | -0.019 |  |
| 2026-05-05 15:06:14 | Norwood (Kelani Ganga) | 0.68 | 🟢 Normal | -0.019 |  |
| 2026-05-05 15:05:46 | Dunamale (Aththanagalu Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-05-05 15:05:37 | Thanamalwila (Kirindi Oya) | 0.66 | 🟢 Normal | -0.009 |  |
| 2026-05-05 15:05:28 | Magura (Kalu Ganga) | 0.87 | 🟢 Normal | -0.011 |  |
| 2026-05-05 15:05:26 | Padiyathalawa (Maduru Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-05-05 15:05:20 | Nakkala (Kumbukkan Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-05-05 15:05:10 | Glencourse (Kelani Ganga) | 9.08 | 🟢 Normal | -0.054 |  |
| 2026-05-05 15:05:04 | Galgamuwa (Mee Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-05-05 15:04:47 | Thawalama (Gin Ganga) | 1.30 | 🟢 Normal | -0.011 |  |
| 2026-05-05 15:04:38 | Giriulla (Maha Oya) | 0.94 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-05-05 15:04:37 | Putupaula (Kalu Ganga) | 0.72 | 🟢 Normal | 0.122 | 🔺 Rising |
| 2026-05-05 15:04:20 | Thanthirimale (Malwathu Oya) | 1.48 | 🟢 Normal | 0.000 |  |
| 2026-05-05 15:04:14 | Badalgama (Maha Oya) | 1.83 | 🟢 Normal | 0.000 |  |
| 2026-05-05 15:04:10 | Panadugama (Nilwala Ganga) | 2.01 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-05 15:03:26 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-05-05 15:03:09 | Hanwella (Kelani Ganga) | 1.11 | 🟢 Normal | -0.080 |  |
| 2026-05-05 15:03:02 | Deraniyagala (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-05-05 15:02:56 | Wellawaya (Kirindi Oya) | 0.83 | 🟢 Normal | -0.010 |  |
| 2026-05-05 15:02:41 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | -0.030 |  |
| 2026-05-05 15:02:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.88 | 🟢 Normal | -0.030 |  |
| 2026-05-05 15:02:15 | Peradeniya (Mahaweli Ganga) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-05-05 15:01:57 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | -0.032 |  |
| 2026-05-05 15:01:41 | Pitabeddara (Nilwala Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-05-05 15:01:38 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-05-05 15:01:22 | Yaka Wewa (Ma Oya) | 0.62 | 🟢 Normal | -0.010 |  |
| 2026-05-05 15:01:19 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-05-05 15:01:15 | Kuda Oya (Kirindi Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-05-05 15:01:15 | Ellagawa (Kalu Ganga) | 4.63 | 🟢 Normal | -0.062 |  |
| 2026-05-05 15:01:14 | Nawalapitiya (Mahaweli Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-05-05 15:00:36 | Manampitiya (Mahaweli Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-05-05 15:00:15 | Horowpothana (Yan Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-05-05 15:00:09 | Weraganthota (Mahaweli Ganga) | -3.11 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-05 15:04:37 | Putupaula (Kalu Ganga) | 0.72 | 🟢 Normal | 0.122 | 🔺 Rising |
| 2026-05-05 15:08:42 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2026-05-05 15:09:23 | Thalgahagoda (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-05-05 15:04:38 | Giriulla (Maha Oya) | 0.94 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-05-05 15:04:10 | Panadugama (Nilwala Ganga) | 2.01 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-05 15:01:19 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-05-05 15:05:20 | Nakkala (Kumbukkan Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-05-05 14:03:13 | Moragaswewa (Deduru Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-05-05 15:01:14 | Nawalapitiya (Mahaweli Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-05-05 15:00:15 | Horowpothana (Yan Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-05-05 15:05:04 | Galgamuwa (Mee Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-05-05 15:01:41 | Pitabeddara (Nilwala Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-05-05 15:03:02 | Deraniyagala (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-05-05 14:11:36 | Baddegama (Gin Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-05-05 15:05:26 | Padiyathalawa (Maduru Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-05-05 15:03:26 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-05-05 15:05:46 | Dunamale (Aththanagalu Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-05-05 15:01:38 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-05-05 15:04:14 | Badalgama (Maha Oya) | 1.83 | 🟢 Normal | 0.000 |  |
| 2026-05-05 15:00:36 | Manampitiya (Mahaweli Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-05-05 15:04:20 | Thanthirimale (Malwathu Oya) | 1.48 | 🟢 Normal | 0.000 |  |
| 2026-05-05 15:02:15 | Peradeniya (Mahaweli Ganga) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-05-05 15:10:41 | Urawa (Nilwala Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-05-05 15:01:15 | Kuda Oya (Kirindi Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-05-05 15:05:37 | Thanamalwila (Kirindi Oya) | 0.66 | 🟢 Normal | -0.009 |  |
| 2026-05-05 15:02:56 | Wellawaya (Kirindi Oya) | 0.83 | 🟢 Normal | -0.010 |  |
| 2026-05-05 15:00:09 | Weraganthota (Mahaweli Ganga) | -3.11 | 🟢 Normal | -0.010 |  |
| 2026-05-05 15:01:22 | Yaka Wewa (Ma Oya) | 0.62 | 🟢 Normal | -0.010 |  |
| 2026-05-05 15:04:47 | Thawalama (Gin Ganga) | 1.30 | 🟢 Normal | -0.011 |  |
| 2026-05-05 15:05:28 | Magura (Kalu Ganga) | 0.87 | 🟢 Normal | -0.011 |  |
| 2026-05-05 15:06:27 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | -0.019 |  |
| 2026-05-05 15:06:14 | Norwood (Kelani Ganga) | 0.68 | 🟢 Normal | -0.019 |  |
| 2026-05-05 15:09:21 | Rathnapura (Kalu Ganga) | 1.09 | 🟢 Normal | -0.025 |  |
| 2026-05-05 15:02:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.88 | 🟢 Normal | -0.030 |  |
| 2026-05-05 15:02:41 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | -0.030 |  |
| 2026-05-05 15:01:57 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | -0.032 |  |
| 2026-05-05 15:05:10 | Glencourse (Kelani Ganga) | 9.08 | 🟢 Normal | -0.054 |  |
| 2026-05-05 15:01:15 | Ellagawa (Kalu Ganga) | 4.63 | 🟢 Normal | -0.062 |  |
| 2026-05-05 15:03:09 | Hanwella (Kelani Ganga) | 1.11 | 🟢 Normal | -0.080 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)