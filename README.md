# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--13_20:20:24-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **124,235 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-13 20:20:24 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.26 | 🟢 Normal | -0.016 |  |
| 2026-04-13 20:08:52 | Manampitiya (Mahaweli Ganga) | 0.19 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-04-13 20:08:36 | Rathnapura (Kalu Ganga) | 1.64 | 🟢 Normal | -0.068 |  |
| 2026-04-13 20:08:10 | Moragaswewa (Deduru Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-04-13 20:08:07 | Moragaswewa (Deduru Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-04-13 20:07:53 | Pitabeddara (Nilwala Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-04-13 20:07:47 | Urawa (Nilwala Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-04-13 20:07:13 | Baddegama (Gin Ganga) | 1.30 | 🟢 Normal | -0.049 |  |
| 2026-04-13 20:06:41 | Thawalama (Gin Ganga) | 1.59 | 🟢 Normal | 0.075 | 🔺 Rising |
| 2026-04-13 20:06:37 | Moraketiya (Walawe Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-04-13 20:05:42 | Magura (Kalu Ganga) | 1.56 | 🟢 Normal | -0.302 |  |
| 2026-04-13 20:05:18 | Giriulla (Maha Oya) | 1.09 | 🟢 Normal | -0.010 |  |
| 2026-04-13 20:04:51 | Holombuwa (Kelani Ganga) | 0.30 | 🟢 Normal | -0.010 |  |
| 2026-04-13 20:04:48 | Hanwella (Kelani Ganga) | 0.64 | 🟢 Normal | -0.047 |  |
| 2026-04-13 20:04:29 | Panadugama (Nilwala Ganga) | 2.03 | 🟢 Normal | 0.000 |  |
| 2026-04-13 20:04:16 | Deraniyagala (Kelani Ganga) | 0.42 | 🟢 Normal | -0.020 |  |
| 2026-04-13 20:04:12 | Badalgama (Maha Oya) | 2.25 | 🟢 Normal | -0.052 |  |
| 2026-04-13 20:04:10 | Peradeniya (Mahaweli Ganga) | 1.21 | 🟢 Normal | 0.088 | 🔺 Rising |
| 2026-04-13 20:04:09 | Siyambalanduwa (Heda Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-04-13 20:03:45 | Horowpothana (Yan Oya) | 1.53 | 🟢 Normal | 0.000 |  |
| 2026-04-13 20:03:34 | Panadugama (Nilwala Ganga) | 2.03 | 🟢 Normal | 0.000 |  |
| 2026-04-13 20:03:32 | Padiyathalawa (Maduru Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-04-13 20:03:16 | Norwood (Kelani Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-04-13 20:03:02 | Katharagama (Menik Ganga) | -0.70 | 🟢 Normal | -0.101 |  |
| 2026-04-13 20:02:56 | Putupaula (Kalu Ganga) | 0.63 | 🟢 Normal | -0.077 |  |
| 2026-04-13 20:02:52 | Ellagawa (Kalu Ganga) | 5.56 | 🟢 Normal | 0.000 |  |
| 2026-04-13 20:02:46 | Kuda Oya (Kirindi Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-04-13 20:02:30 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | -0.134 |  |
| 2026-04-13 20:02:27 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | -0.030 |  |
| 2026-04-13 20:02:25 | Dunamale (Aththanagalu Oya) | 0.45 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-13 20:02:11 | Thaldena (Mahaweli Ganga) | 0.86 | 🟢 Normal | 0.375 | 🔺 Rising |
| 2026-04-13 20:02:01 | Glencourse (Kelani Ganga) | 8.59 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-13 20:01:54 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | -0.031 |  |
| 2026-04-13 20:01:53 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-13 20:01:24 | Nawalapitiya (Mahaweli Ganga) | 1.13 | 🟢 Normal | -0.038 |  |
| 2026-04-13 20:01:05 | Thanamalwila (Kirindi Oya) | 1.07 | 🟢 Normal | 0.097 | 🔺 Rising |
| 2026-04-13 20:00:46 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-04-13 20:00:34 | Wellawaya (Kirindi Oya) | 1.85 | 🟢 Normal | 0.810 | 🔺 Rising |
| 2026-04-13 19:32:04 | Panadugama (Nilwala Ganga) | 2.04 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-13 20:00:34 | Wellawaya (Kirindi Oya) | 1.85 | 🟢 Normal | 0.810 | 🔺 Rising |
| 2026-04-13 20:02:11 | Thaldena (Mahaweli Ganga) | 0.86 | 🟢 Normal | 0.375 | 🔺 Rising |
| 2026-04-13 20:01:05 | Thanamalwila (Kirindi Oya) | 1.07 | 🟢 Normal | 0.097 | 🔺 Rising |
| 2026-04-13 20:04:10 | Peradeniya (Mahaweli Ganga) | 1.21 | 🟢 Normal | 0.088 | 🔺 Rising |
| 2026-04-13 20:06:41 | Thawalama (Gin Ganga) | 1.59 | 🟢 Normal | 0.075 | 🔺 Rising |
| 2026-04-13 20:08:52 | Manampitiya (Mahaweli Ganga) | 0.19 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-04-13 20:02:25 | Dunamale (Aththanagalu Oya) | 0.45 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-13 20:02:01 | Glencourse (Kelani Ganga) | 8.59 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-13 18:01:02 | Thanthirimale (Malwathu Oya) | 1.16 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-13 20:00:46 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-04-13 20:08:10 | Moragaswewa (Deduru Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-04-13 20:01:53 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-13 20:03:45 | Horowpothana (Yan Oya) | 1.53 | 🟢 Normal | 0.000 |  |
| 2026-04-13 18:01:19 | Galgamuwa (Mee Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-04-13 20:07:53 | Pitabeddara (Nilwala Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-04-13 20:03:16 | Norwood (Kelani Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-04-13 20:02:52 | Ellagawa (Kalu Ganga) | 5.56 | 🟢 Normal | 0.000 |  |
| 2026-04-13 20:04:29 | Panadugama (Nilwala Ganga) | 2.03 | 🟢 Normal | 0.000 |  |
| 2026-04-13 20:03:32 | Padiyathalawa (Maduru Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-04-13 20:06:37 | Moraketiya (Walawe Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-04-13 20:04:09 | Siyambalanduwa (Heda Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-04-13 20:07:47 | Urawa (Nilwala Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-04-13 20:02:46 | Kuda Oya (Kirindi Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-04-13 18:03:40 | Weraganthota (Mahaweli Ganga) | -3.02 | 🟢 Normal | -0.010 |  |
| 2026-04-13 20:04:51 | Holombuwa (Kelani Ganga) | 0.30 | 🟢 Normal | -0.010 |  |
| 2026-04-13 20:05:18 | Giriulla (Maha Oya) | 1.09 | 🟢 Normal | -0.010 |  |
| 2026-04-13 20:20:24 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.26 | 🟢 Normal | -0.016 |  |
| 2026-04-13 20:04:16 | Deraniyagala (Kelani Ganga) | 0.42 | 🟢 Normal | -0.020 |  |
| 2026-04-13 20:02:27 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | -0.030 |  |
| 2026-04-13 20:01:54 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | -0.031 |  |
| 2026-04-13 20:01:24 | Nawalapitiya (Mahaweli Ganga) | 1.13 | 🟢 Normal | -0.038 |  |
| 2026-04-13 20:04:48 | Hanwella (Kelani Ganga) | 0.64 | 🟢 Normal | -0.047 |  |
| 2026-04-13 20:07:13 | Baddegama (Gin Ganga) | 1.30 | 🟢 Normal | -0.049 |  |
| 2026-04-13 20:04:12 | Badalgama (Maha Oya) | 2.25 | 🟢 Normal | -0.052 |  |
| 2026-04-13 20:08:36 | Rathnapura (Kalu Ganga) | 1.64 | 🟢 Normal | -0.068 |  |
| 2026-04-13 20:02:56 | Putupaula (Kalu Ganga) | 0.63 | 🟢 Normal | -0.077 |  |
| 2026-04-13 20:03:02 | Katharagama (Menik Ganga) | -0.70 | 🟢 Normal | -0.101 |  |
| 2026-04-13 20:02:30 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | -0.134 |  |
| 2026-04-13 20:05:42 | Magura (Kalu Ganga) | 1.56 | 🟢 Normal | -0.302 |  |

## River Water Level Charts by Station

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)