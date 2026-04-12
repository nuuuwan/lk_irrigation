# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--12_23:13:34-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **123,434 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **29** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-12 23:13:34 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | -0.043 |  |
| 2026-04-12 23:11:59 | Horowpothana (Yan Oya) | 1.47 | 🟢 Normal | 0.000 |  |
| 2026-04-12 23:09:36 | Magura (Kalu Ganga) | 3.76 | 🟢 Normal | 0.323 | 🔺 Rising |
| 2026-04-12 23:09:31 | Thawalama (Gin Ganga) | 1.89 | 🟢 Normal | 0.084 | 🔺 Rising |
| 2026-04-12 23:08:45 | Badalgama (Maha Oya) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-04-12 23:06:41 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-12 23:06:22 | Holombuwa (Kelani Ganga) | 0.30 | 🟢 Normal | 0.149 | 🔺 Rising |
| 2026-04-12 23:05:23 | Rathnapura (Kalu Ganga) | 3.57 | 🟢 Normal | 0.682 | 🔺 Rising |
| 2026-04-12 23:05:15 | Kuda Oya (Kirindi Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-04-12 23:05:12 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-04-12 23:05:11 | Panadugama (Nilwala Ganga) | 2.31 | 🟢 Normal | -0.015 |  |
| 2026-04-12 23:04:27 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-04-12 23:03:51 | Nawalapitiya (Mahaweli Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-04-12 23:03:30 | Giriulla (Maha Oya) | 0.75 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-12 23:03:10 | Thanamalwila (Kirindi Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-04-12 23:02:59 | Nawalapitiya (Mahaweli Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-04-12 23:02:59 | Norwood (Kelani Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-04-12 23:02:46 | Pitabeddara (Nilwala Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-04-12 23:02:27 | Ellagawa (Kalu Ganga) | 3.89 | 🟢 Normal | 0.000 |  |
| 2026-04-12 23:02:19 | Deraniyagala (Kelani Ganga) | 0.53 | 🟢 Normal | 0.160 | 🔺 Rising |
| 2026-04-12 23:02:17 | Manampitiya (Mahaweli Ganga) | 0.20 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-04-12 23:02:14 | Glencourse (Kelani Ganga) | 8.45 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-04-12 23:02:13 | Hanwella (Kelani Ganga) | 0.31 | 🟢 Normal | -0.020 |  |
| 2026-04-12 23:02:07 | Thalgahagoda (Nilwala Ganga) | 0.28 | 🟢 Normal | -0.011 |  |
| 2026-04-12 23:01:38 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.098 | 🔺 Rising |
| 2026-04-12 23:01:38 | Moragaswewa (Deduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-04-12 23:01:12 | Thaldena (Mahaweli Ganga) | 0.55 | 🟢 Normal | 0.316 | 🔺 Rising |
| 2026-04-12 23:00:57 | Nakkala (Kumbukkan Oya) | 0.69 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-12 23:00:56 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.010 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-12 23:05:23 | Rathnapura (Kalu Ganga) | 3.57 | 🟢 Normal | 0.682 | 🔺 Rising |
| 2026-04-12 23:09:36 | Magura (Kalu Ganga) | 3.76 | 🟢 Normal | 0.323 | 🔺 Rising |
| 2026-04-12 23:01:12 | Thaldena (Mahaweli Ganga) | 0.55 | 🟢 Normal | 0.316 | 🔺 Rising |
| 2026-04-12 23:02:19 | Deraniyagala (Kelani Ganga) | 0.53 | 🟢 Normal | 0.160 | 🔺 Rising |
| 2026-04-12 23:06:22 | Holombuwa (Kelani Ganga) | 0.30 | 🟢 Normal | 0.149 | 🔺 Rising |
| 2026-04-12 21:07:46 | Peradeniya (Mahaweli Ganga) | 1.32 | 🟢 Normal | 0.116 | 🔺 Rising |
| 2026-04-12 23:01:38 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.098 | 🔺 Rising |
| 2026-04-12 23:09:31 | Thawalama (Gin Ganga) | 1.89 | 🟢 Normal | 0.084 | 🔺 Rising |
| 2026-04-12 18:07:41 | Galgamuwa (Mee Oya) | 0.27 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2026-04-12 23:02:14 | Glencourse (Kelani Ganga) | 8.45 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-04-12 23:02:17 | Manampitiya (Mahaweli Ganga) | 0.20 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-04-12 23:03:30 | Giriulla (Maha Oya) | 0.75 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-12 22:04:24 | Baddegama (Gin Ganga) | 1.12 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-12 23:00:56 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-12 23:00:57 | Nakkala (Kumbukkan Oya) | 0.69 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-12 21:02:30 | Wellawaya (Kirindi Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-04-12 23:01:38 | Moragaswewa (Deduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-04-12 23:03:51 | Nawalapitiya (Mahaweli Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-04-12 22:01:43 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-12 23:11:59 | Horowpothana (Yan Oya) | 1.47 | 🟢 Normal | 0.000 |  |
| 2026-04-12 23:02:46 | Pitabeddara (Nilwala Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-04-12 23:02:59 | Norwood (Kelani Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-04-12 23:02:27 | Ellagawa (Kalu Ganga) | 3.89 | 🟢 Normal | 0.000 |  |
| 2026-04-12 22:01:15 | Padiyathalawa (Maduru Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-04-12 23:04:27 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-04-12 23:06:41 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-12 23:05:12 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-04-12 23:08:45 | Badalgama (Maha Oya) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-04-12 18:02:49 | Thanthirimale (Malwathu Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-04-12 21:05:18 | Urawa (Nilwala Ganga) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-04-12 23:05:15 | Kuda Oya (Kirindi Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-04-12 23:03:10 | Thanamalwila (Kirindi Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-04-12 23:02:07 | Thalgahagoda (Nilwala Ganga) | 0.28 | 🟢 Normal | -0.011 |  |
| 2026-04-12 23:05:11 | Panadugama (Nilwala Ganga) | 2.31 | 🟢 Normal | -0.015 |  |
| 2026-04-12 23:02:13 | Hanwella (Kelani Ganga) | 0.31 | 🟢 Normal | -0.020 |  |
| 2026-04-12 18:12:59 | Weraganthota (Mahaweli Ganga) | -3.20 | 🟢 Normal | -0.033 |  |
| 2026-04-12 23:13:34 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | -0.043 |  |
| 2026-04-12 21:19:02 | Putupaula (Kalu Ganga) | 0.43 | 🟢 Normal | -0.051 |  |
| 2026-04-12 20:40:15 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.47 | 🟢 Normal | -0.167 |  |

## River Water Level Charts by Station

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

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

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)