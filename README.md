# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--31_04:31:06-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **166,274 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-31 04:31:06 | Ellagawa (Kalu Ganga) | 6.40 | 🟢 Normal | -0.035 |  |
| 2026-05-31 04:25:51 | Thawalama (Gin Ganga) | 1.87 | 🟢 Normal | -0.024 |  |
| 2026-05-31 04:25:03 | Moraketiya (Walawe Ganga) | 0.89 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-05-31 04:13:30 | Deraniyagala (Kelani Ganga) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-05-31 04:12:55 | Thalgahagoda (Nilwala Ganga) | 0.52 | 🟢 Normal | -0.085 |  |
| 2026-05-31 04:11:39 | Baddegama (Gin Ganga) | 2.39 | 🟢 Normal | -0.018 |  |
| 2026-05-31 04:10:09 | Kithulgala (Kelani Ganga) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-05-31 04:06:21 | Panadugama (Nilwala Ganga) | 3.06 | 🟢 Normal | -0.034 |  |
| 2026-05-31 04:05:42 | Rathnapura (Kalu Ganga) | 2.04 | 🟢 Normal | 0.000 |  |
| 2026-05-31 04:04:51 | Thaldena (Mahaweli Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-05-31 04:04:46 | Giriulla (Maha Oya) | 1.06 | 🟢 Normal | -0.010 |  |
| 2026-05-31 04:04:42 | Thaldena (Mahaweli Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-05-31 04:04:41 | Badalgama (Maha Oya) | 2.25 | 🟢 Normal | -0.011 |  |
| 2026-05-31 04:03:58 | Hanwella (Kelani Ganga) | 2.28 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-05-31 04:03:58 | Magura (Kalu Ganga) | 2.45 | 🟢 Normal | -0.020 |  |
| 2026-05-31 04:03:52 | Thaldena (Mahaweli Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-05-31 04:03:40 | Putupaula (Kalu Ganga) | 2.20 | 🟢 Normal | -0.052 |  |
| 2026-05-31 04:03:37 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-05-31 04:03:23 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-05-31 04:03:13 | Nawalapitiya (Mahaweli Ganga) | 1.40 | 🟢 Normal | -0.010 |  |
| 2026-05-31 04:03:04 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-05-31 04:03:00 | Manampitiya (Mahaweli Ganga) | 0.03 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-05-31 04:02:53 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.032 |  |
| 2026-05-31 04:02:50 | Rathnapura (Kalu Ganga) | 2.04 | 🟢 Normal | 0.000 |  |
| 2026-05-31 04:02:28 | Norwood (Kelani Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-05-31 04:02:20 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-05-31 04:02:16 | Thanamalwila (Kirindi Oya) | 0.65 | 🟢 Normal | -0.010 |  |
| 2026-05-31 04:02:05 | Moragaswewa (Deduru Oya) | 0.36 | 🟢 Normal | -0.010 |  |
| 2026-05-31 04:01:57 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.85 | 🟡 Alert | -0.030 |  |
| 2026-05-31 04:01:52 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-05-31 04:01:45 | Thaldena (Mahaweli Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-05-31 04:01:39 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-05-31 04:01:24 | Glencourse (Kelani Ganga) | 10.47 | 🟢 Normal | -0.041 |  |
| 2026-05-31 04:00:57 | Peradeniya (Mahaweli Ganga) | 1.75 | 🟢 Normal | -0.044 |  |
| 2026-05-31 04:00:49 | Wellawaya (Kirindi Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-05-31 04:00:44 | Dunamale (Aththanagalu Oya) | 1.54 | 🟢 Normal | -0.018 |  |
| 2026-05-31 04:00:22 | Wellawaya (Kirindi Oya) | 0.97 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-31 04:01:57 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.85 | 🟡 Alert | -0.030 |  |
| 2026-05-31 04:03:58 | Hanwella (Kelani Ganga) | 2.28 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-05-31 04:03:00 | Manampitiya (Mahaweli Ganga) | 0.03 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-05-31 04:25:03 | Moraketiya (Walawe Ganga) | 0.89 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-05-31 04:10:09 | Kithulgala (Kelani Ganga) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-05-30 18:00:56 | Weraganthota (Mahaweli Ganga) | -3.32 | 🟢 Normal | 0.000 |  |
| 2026-05-31 04:00:49 | Wellawaya (Kirindi Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-05-31 04:02:20 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-05-31 04:01:52 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-05-31 04:01:39 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-05-30 18:04:48 | Galgamuwa (Mee Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-05-31 03:10:43 | Pitabeddara (Nilwala Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-05-31 04:02:28 | Norwood (Kelani Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-05-31 04:13:30 | Deraniyagala (Kelani Ganga) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-05-31 03:02:33 | Padiyathalawa (Maduru Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-05-31 04:03:37 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-05-31 04:04:51 | Thaldena (Mahaweli Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-05-31 04:03:23 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-05-31 03:13:23 | Holombuwa (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-05-31 04:05:42 | Rathnapura (Kalu Ganga) | 2.04 | 🟢 Normal | 0.000 |  |
| 2026-05-30 18:03:31 | Thanthirimale (Malwathu Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-05-31 03:08:34 | Kuda Oya (Kirindi Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-05-31 04:03:13 | Nawalapitiya (Mahaweli Ganga) | 1.40 | 🟢 Normal | -0.010 |  |
| 2026-05-31 04:04:46 | Giriulla (Maha Oya) | 1.06 | 🟢 Normal | -0.010 |  |
| 2026-05-31 04:02:05 | Moragaswewa (Deduru Oya) | 0.36 | 🟢 Normal | -0.010 |  |
| 2026-05-31 04:02:16 | Thanamalwila (Kirindi Oya) | 0.65 | 🟢 Normal | -0.010 |  |
| 2026-05-31 04:04:41 | Badalgama (Maha Oya) | 2.25 | 🟢 Normal | -0.011 |  |
| 2026-05-31 04:11:39 | Baddegama (Gin Ganga) | 2.39 | 🟢 Normal | -0.018 |  |
| 2026-05-31 04:00:44 | Dunamale (Aththanagalu Oya) | 1.54 | 🟢 Normal | -0.018 |  |
| 2026-05-31 04:03:58 | Magura (Kalu Ganga) | 2.45 | 🟢 Normal | -0.020 |  |
| 2026-05-31 04:25:51 | Thawalama (Gin Ganga) | 1.87 | 🟢 Normal | -0.024 |  |
| 2026-05-31 03:03:50 | Urawa (Nilwala Ganga) | 0.23 | 🟢 Normal | -0.025 |  |
| 2026-05-31 04:02:53 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.032 |  |
| 2026-05-31 04:06:21 | Panadugama (Nilwala Ganga) | 3.06 | 🟢 Normal | -0.034 |  |
| 2026-05-31 04:31:06 | Ellagawa (Kalu Ganga) | 6.40 | 🟢 Normal | -0.035 |  |
| 2026-05-31 04:01:24 | Glencourse (Kelani Ganga) | 10.47 | 🟢 Normal | -0.041 |  |
| 2026-05-31 04:00:57 | Peradeniya (Mahaweli Ganga) | 1.75 | 🟢 Normal | -0.044 |  |
| 2026-05-31 04:03:40 | Putupaula (Kalu Ganga) | 2.20 | 🟢 Normal | -0.052 |  |
| 2026-05-31 04:12:55 | Thalgahagoda (Nilwala Ganga) | 0.52 | 🟢 Normal | -0.085 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)