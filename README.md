# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--11_19:42:19-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **149,149 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-11 19:42:19 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.70 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-05-11 19:14:07 | Giriulla (Maha Oya) | 1.51 | 🟢 Normal | 0.000 |  |
| 2026-05-11 19:12:25 | Rathnapura (Kalu Ganga) | 2.13 | 🟢 Normal | -0.009 |  |
| 2026-05-11 19:11:10 | Magura (Kalu Ganga) | 1.85 | 🟢 Normal | -0.035 |  |
| 2026-05-11 19:10:23 | Urawa (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-05-11 19:09:04 | Baddegama (Gin Ganga) | 1.56 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-05-11 19:08:37 | Panadugama (Nilwala Ganga) | 2.67 | 🟢 Normal | -0.010 |  |
| 2026-05-11 19:07:55 | Putupaula (Kalu Ganga) | 0.97 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-05-11 19:06:43 | Glencourse (Kelani Ganga) | 9.60 | 🟢 Normal | -0.038 |  |
| 2026-05-11 19:06:22 | Peradeniya (Mahaweli Ganga) | 2.69 | 🟢 Normal | 0.274 | 🔺 Rising |
| 2026-05-11 19:06:18 | Kuda Oya (Kirindi Oya) | 2.35 | 🟢 Normal | -0.009 |  |
| 2026-05-11 19:06:06 | Holombuwa (Kelani Ganga) | 1.21 | 🟢 Normal | -0.134 |  |
| 2026-05-11 19:05:49 | Norwood (Kelani Ganga) | 0.78 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-11 19:05:38 | Nawalapitiya (Mahaweli Ganga) | 1.01 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-11 19:05:18 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-05-11 19:04:58 | Kithulgala (Kelani Ganga) | 1.85 | 🟢 Normal | 0.201 | 🔺 Rising |
| 2026-05-11 19:04:49 | Moragaswewa (Deduru Oya) | 2.34 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-05-11 19:04:11 | Ellagawa (Kalu Ganga) | 5.54 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-11 19:04:09 | Katharagama (Menik Ganga) | 2.44 | 🟢 Normal | 0.000 |  |
| 2026-05-11 19:04:03 | Thawalama (Gin Ganga) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-05-11 19:03:47 | Badalgama (Maha Oya) | 2.61 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-05-11 19:03:36 | Nakkala (Kumbukkan Oya) | 2.58 | 🟢 Normal | 0.908 | 🔺 Rising |
| 2026-05-11 19:03:25 | Deraniyagala (Kelani Ganga) | 0.90 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-11 19:03:17 | Siyambalanduwa (Heda Oya) | 2.18 | 🟢 Normal | 0.558 | 🔺 Rising |
| 2026-05-11 19:03:03 | Pitabeddara (Nilwala Ganga) | 0.75 | 🟢 Normal | -0.021 |  |
| 2026-05-11 19:02:57 | Thaldena (Mahaweli Ganga) | 1.70 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-05-11 19:02:41 | Manampitiya (Mahaweli Ganga) | 1.20 | 🟢 Normal | -0.061 |  |
| 2026-05-11 19:02:39 | Thalgahagoda (Nilwala Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-05-11 19:02:30 | Yaka Wewa (Ma Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-05-11 19:02:30 | Hanwella (Kelani Ganga) | 1.51 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-05-11 19:02:19 | Dunamale (Aththanagalu Oya) | 1.48 | 🟢 Normal | 0.000 |  |
| 2026-05-11 19:02:08 | Thanamalwila (Kirindi Oya) | 2.15 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-11 19:01:21 | Moraketiya (Walawe Ganga) | 1.35 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-11 19:01:20 | Horowpothana (Yan Oya) | 2.15 | 🟢 Normal | 0.000 |  |
| 2026-05-11 19:00:44 | Wellawaya (Kirindi Oya) | 2.20 | 🟢 Normal | 0.149 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-11 19:03:36 | Nakkala (Kumbukkan Oya) | 2.58 | 🟢 Normal | 0.908 | 🔺 Rising |
| 2026-05-11 19:03:17 | Siyambalanduwa (Heda Oya) | 2.18 | 🟢 Normal | 0.558 | 🔺 Rising |
| 2026-05-11 19:06:22 | Peradeniya (Mahaweli Ganga) | 2.69 | 🟢 Normal | 0.274 | 🔺 Rising |
| 2026-05-11 19:04:58 | Kithulgala (Kelani Ganga) | 1.85 | 🟢 Normal | 0.201 | 🔺 Rising |
| 2026-05-11 19:00:44 | Wellawaya (Kirindi Oya) | 2.20 | 🟢 Normal | 0.149 | 🔺 Rising |
| 2026-05-11 18:01:53 | Thanthirimale (Malwathu Oya) | 3.12 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-05-11 19:02:57 | Thaldena (Mahaweli Ganga) | 1.70 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-05-11 19:04:49 | Moragaswewa (Deduru Oya) | 2.34 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-05-11 19:09:04 | Baddegama (Gin Ganga) | 1.56 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-05-11 19:05:18 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-05-11 19:03:47 | Badalgama (Maha Oya) | 2.61 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-05-11 19:03:25 | Deraniyagala (Kelani Ganga) | 0.90 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-11 19:01:21 | Moraketiya (Walawe Ganga) | 1.35 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-11 19:02:30 | Hanwella (Kelani Ganga) | 1.51 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-05-11 19:04:11 | Ellagawa (Kalu Ganga) | 5.54 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-11 19:07:55 | Putupaula (Kalu Ganga) | 0.97 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-05-11 19:42:19 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.70 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-05-11 19:00:24 | Padiyathalawa (Maduru Oya) | 0.30 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-05-11 19:02:08 | Thanamalwila (Kirindi Oya) | 2.15 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-11 19:05:38 | Nawalapitiya (Mahaweli Ganga) | 1.01 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-11 19:05:49 | Norwood (Kelani Ganga) | 0.78 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-11 19:10:23 | Urawa (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-05-11 19:02:30 | Yaka Wewa (Ma Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-05-11 19:14:07 | Giriulla (Maha Oya) | 1.51 | 🟢 Normal | 0.000 |  |
| 2026-05-11 19:01:20 | Horowpothana (Yan Oya) | 2.15 | 🟢 Normal | 0.000 |  |
| 2026-05-11 19:02:19 | Dunamale (Aththanagalu Oya) | 1.48 | 🟢 Normal | 0.000 |  |
| 2026-05-11 19:04:09 | Katharagama (Menik Ganga) | 2.44 | 🟢 Normal | 0.000 |  |
| 2026-05-11 19:04:03 | Thawalama (Gin Ganga) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-05-11 19:02:39 | Thalgahagoda (Nilwala Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-05-11 19:12:25 | Rathnapura (Kalu Ganga) | 2.13 | 🟢 Normal | -0.009 |  |
| 2026-05-11 19:06:18 | Kuda Oya (Kirindi Oya) | 2.35 | 🟢 Normal | -0.009 |  |
| 2026-05-11 19:08:37 | Panadugama (Nilwala Ganga) | 2.67 | 🟢 Normal | -0.010 |  |
| 2026-05-11 19:03:03 | Pitabeddara (Nilwala Ganga) | 0.75 | 🟢 Normal | -0.021 |  |
| 2026-05-11 19:11:10 | Magura (Kalu Ganga) | 1.85 | 🟢 Normal | -0.035 |  |
| 2026-05-11 19:06:43 | Glencourse (Kelani Ganga) | 9.60 | 🟢 Normal | -0.038 |  |
| 2026-05-11 18:02:56 | Weraganthota (Mahaweli Ganga) | -2.75 | 🟢 Normal | -0.049 |  |
| 2026-05-11 19:02:41 | Manampitiya (Mahaweli Ganga) | 1.20 | 🟢 Normal | -0.061 |  |
| 2026-05-11 18:06:15 | Galgamuwa (Mee Oya) | 1.40 | 🟢 Normal | -0.074 |  |
| 2026-05-11 19:06:06 | Holombuwa (Kelani Ganga) | 1.21 | 🟢 Normal | -0.134 |  |

## River Water Level Charts by Station

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)