# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--13_05:05:37-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **150,375 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **27** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-13 05:05:37 | Wellawaya (Kirindi Oya) | 1.56 | 🟢 Normal | 0.000 |  |
| 2026-05-13 05:05:37 | Norwood (Kelani Ganga) | 0.71 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-13 05:05:20 | Giriulla (Maha Oya) | 1.43 | 🟢 Normal | -0.020 |  |
| 2026-05-13 05:05:02 | Rathnapura (Kalu Ganga) | 4.09 | 🟢 Normal | 0.517 | 🔺 Rising |
| 2026-05-13 05:03:43 | Glencourse (Kelani Ganga) | 10.37 | 🟢 Normal | -0.041 |  |
| 2026-05-13 05:03:32 | Urawa (Nilwala Ganga) | 0.16 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-05-13 05:03:32 | Thalgahagoda (Nilwala Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-05-13 05:03:14 | Horowpothana (Yan Oya) | 2.12 | 🟢 Normal | 0.000 |  |
| 2026-05-13 05:03:11 | Thaldena (Mahaweli Ganga) | 0.86 | 🟢 Normal | -0.050 |  |
| 2026-05-13 05:03:00 | Pitabeddara (Nilwala Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-05-13 05:02:36 | Thanamalwila (Kirindi Oya) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-05-13 05:02:07 | Badalgama (Maha Oya) | 2.69 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-13 05:01:46 | Yaka Wewa (Ma Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-05-13 05:01:46 | Holombuwa (Kelani Ganga) | 0.58 | 🟢 Normal | -0.040 |  |
| 2026-05-13 05:01:44 | Moragaswewa (Deduru Oya) | 1.56 | 🟢 Normal | 0.262 | 🔺 Rising |
| 2026-05-13 05:01:25 | Thawalama (Gin Ganga) | 2.05 | 🟢 Normal | -0.225 |  |
| 2026-05-13 05:01:15 | Moraketiya (Walawe Ganga) | 1.05 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-13 05:00:19 | Siyambalanduwa (Heda Oya) | 1.16 | 🟢 Normal | -0.110 |  |
| 2026-05-13 05:00:02 | Thalgahagoda (Nilwala Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-05-13 04:48:35 | Deraniyagala (Kelani Ganga) | 0.73 | 🟢 Normal | -0.024 |  |
| 2026-05-13 04:35:50 | Nawalapitiya (Mahaweli Ganga) | 1.08 | 🟢 Normal | -0.006 |  |
| 2026-05-13 04:33:56 | Magura (Kalu Ganga) | 2.54 | 🟢 Normal | -0.108 |  |
| 2026-05-13 04:32:50 | Urawa (Nilwala Ganga) | 0.14 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-05-13 04:32:30 | Hanwella (Kelani Ganga) | 2.27 | 🟢 Normal | -0.014 |  |
| 2026-05-13 04:25:22 | Katharagama (Menik Ganga) | 1.05 | 🟢 Normal | -0.256 |  |
| 2026-05-13 04:24:08 | Thawalama (Gin Ganga) | 2.19 | 🟢 Normal | -0.225 |  |
| 2026-05-13 04:17:16 | Panadugama (Nilwala Ganga) | 3.56 | 🟢 Normal | -0.056 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-13 05:05:02 | Rathnapura (Kalu Ganga) | 4.09 | 🟢 Normal | 0.517 | 🔺 Rising |
| 2026-05-13 04:09:48 | Kithulgala (Kelani Ganga) | 1.63 | 🟢 Normal | 0.369 | 🔺 Rising |
| 2026-05-13 05:01:44 | Moragaswewa (Deduru Oya) | 1.56 | 🟢 Normal | 0.262 | 🔺 Rising |
| 2026-05-13 04:04:22 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.68 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-05-13 04:06:25 | Baddegama (Gin Ganga) | 2.12 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-05-13 05:03:32 | Urawa (Nilwala Ganga) | 0.16 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-05-13 04:00:35 | Peradeniya (Mahaweli Ganga) | 1.62 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-05-13 04:01:57 | Manampitiya (Mahaweli Ganga) | 1.16 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-13 04:06:51 | Putupaula (Kalu Ganga) | 1.09 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-12 18:00:31 | Galgamuwa (Mee Oya) | 1.68 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-13 05:05:37 | Norwood (Kelani Ganga) | 0.71 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-13 05:02:07 | Badalgama (Maha Oya) | 2.69 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-13 05:01:15 | Moraketiya (Walawe Ganga) | 1.05 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-13 05:05:37 | Wellawaya (Kirindi Oya) | 1.56 | 🟢 Normal | 0.000 |  |
| 2026-05-13 05:01:46 | Yaka Wewa (Ma Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-05-13 05:03:14 | Horowpothana (Yan Oya) | 2.12 | 🟢 Normal | 0.000 |  |
| 2026-05-13 05:03:00 | Pitabeddara (Nilwala Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-05-13 03:00:55 | Padiyathalawa (Maduru Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-05-13 04:03:43 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-05-13 05:03:32 | Thalgahagoda (Nilwala Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-05-13 04:01:21 | Kuda Oya (Kirindi Oya) | 1.87 | 🟢 Normal | 0.000 |  |
| 2026-05-13 05:02:36 | Thanamalwila (Kirindi Oya) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-05-13 04:35:50 | Nawalapitiya (Mahaweli Ganga) | 1.08 | 🟢 Normal | -0.006 |  |
| 2026-05-13 04:32:30 | Hanwella (Kelani Ganga) | 2.27 | 🟢 Normal | -0.014 |  |
| 2026-05-13 04:05:44 | Dunamale (Aththanagalu Oya) | 2.88 | 🟢 Normal | -0.019 |  |
| 2026-05-13 05:05:20 | Giriulla (Maha Oya) | 1.43 | 🟢 Normal | -0.020 |  |
| 2026-05-13 04:01:24 | Ellagawa (Kalu Ganga) | 6.17 | 🟢 Normal | -0.020 |  |
| 2026-05-12 18:01:07 | Thanthirimale (Malwathu Oya) | 3.38 | 🟢 Normal | -0.020 |  |
| 2026-05-13 04:48:35 | Deraniyagala (Kelani Ganga) | 0.73 | 🟢 Normal | -0.024 |  |
| 2026-05-12 18:02:40 | Weraganthota (Mahaweli Ganga) | -2.95 | 🟢 Normal | -0.031 |  |
| 2026-05-13 05:01:46 | Holombuwa (Kelani Ganga) | 0.58 | 🟢 Normal | -0.040 |  |
| 2026-05-13 05:03:43 | Glencourse (Kelani Ganga) | 10.37 | 🟢 Normal | -0.041 |  |
| 2026-05-13 05:03:11 | Thaldena (Mahaweli Ganga) | 0.86 | 🟢 Normal | -0.050 |  |
| 2026-05-13 04:17:16 | Panadugama (Nilwala Ganga) | 3.56 | 🟢 Normal | -0.056 |  |
| 2026-05-13 04:01:02 | Nakkala (Kumbukkan Oya) | 1.60 | 🟢 Normal | -0.104 |  |
| 2026-05-13 04:33:56 | Magura (Kalu Ganga) | 2.54 | 🟢 Normal | -0.108 |  |
| 2026-05-13 05:00:19 | Siyambalanduwa (Heda Oya) | 1.16 | 🟢 Normal | -0.110 |  |
| 2026-05-13 05:01:25 | Thawalama (Gin Ganga) | 2.05 | 🟢 Normal | -0.225 |  |
| 2026-05-13 04:25:22 | Katharagama (Menik Ganga) | 1.05 | 🟢 Normal | -0.256 |  |

## River Water Level Charts by Station

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)