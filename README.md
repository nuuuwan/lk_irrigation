# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--12_05:16:18-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **149,495 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-12 05:16:18 | Pitabeddara (Nilwala Ganga) | 0.78 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-05-12 05:14:32 | Peradeniya (Mahaweli Ganga) | 1.47 | 🟢 Normal | -0.034 |  |
| 2026-05-12 05:14:02 | Rathnapura (Kalu Ganga) | 2.02 | 🟢 Normal | -0.042 |  |
| 2026-05-12 05:12:51 | Baddegama (Gin Ganga) | 1.69 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-05-12 05:11:56 | Padiyathalawa (Maduru Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-05-12 05:10:10 | Holombuwa (Kelani Ganga) | 0.90 | 🟢 Normal | 0.133 | 🔺 Rising |
| 2026-05-12 05:07:04 | Katharagama (Menik Ganga) | 2.25 | 🟢 Normal | -0.048 |  |
| 2026-05-12 05:06:46 | Magura (Kalu Ganga) | 2.70 | 🟢 Normal | 0.111 | 🔺 Rising |
| 2026-05-12 05:06:30 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-05-12 05:05:50 | Siyambalanduwa (Heda Oya) | 0.99 | 🟢 Normal | -0.049 |  |
| 2026-05-12 05:05:08 | Moraketiya (Walawe Ganga) | 1.32 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-05-12 05:04:59 | Horowpothana (Yan Oya) | 2.15 | 🟢 Normal | 0.000 |  |
| 2026-05-12 05:04:47 | Moragaswewa (Deduru Oya) | 2.25 | 🟢 Normal | 0.000 |  |
| 2026-05-12 05:04:36 | Thaldena (Mahaweli Ganga) | 0.78 | 🟢 Normal | -0.020 |  |
| 2026-05-12 05:04:22 | Giriulla (Maha Oya) | 1.74 | 🟢 Normal | -0.019 |  |
| 2026-05-12 05:03:38 | Kithulgala (Kelani Ganga) | 1.53 | 🟢 Normal | -0.020 |  |
| 2026-05-12 05:03:22 | Yaka Wewa (Ma Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-05-12 05:02:57 | Manampitiya (Mahaweli Ganga) | 0.82 | 🟢 Normal | -0.020 |  |
| 2026-05-12 05:02:47 | Deraniyagala (Kelani Ganga) | 0.90 | 🟢 Normal | -0.010 |  |
| 2026-05-12 05:02:47 | Norwood (Kelani Ganga) | 0.78 | 🟢 Normal | -0.010 |  |
| 2026-05-12 05:02:46 | Thanamalwila (Kirindi Oya) | 2.20 | 🟢 Normal | -0.030 |  |
| 2026-05-12 05:02:28 | Dunamale (Aththanagalu Oya) | 1.57 | 🟢 Normal | -0.030 |  |
| 2026-05-12 05:02:18 | Thawalama (Gin Ganga) | 1.76 | 🟢 Normal | -0.011 |  |
| 2026-05-12 05:02:16 | Moragaswewa (Deduru Oya) | 2.25 | 🟢 Normal | 0.000 |  |
| 2026-05-12 05:02:03 | Nakkala (Kumbukkan Oya) | 1.26 | 🟢 Normal | -0.031 |  |
| 2026-05-12 05:02:02 | Thalgahagoda (Nilwala Ganga) | 0.44 | 🟢 Normal | -0.011 |  |
| 2026-05-12 05:01:46 | Nawalapitiya (Mahaweli Ganga) | 1.03 | 🟢 Normal | -0.061 |  |
| 2026-05-12 05:01:30 | Ellagawa (Kalu Ganga) | 5.88 | 🟢 Normal | 0.000 |  |
| 2026-05-12 05:01:29 | Kuda Oya (Kirindi Oya) | 2.30 | 🟢 Normal | -0.060 |  |
| 2026-05-12 05:01:06 | Badalgama (Maha Oya) | 2.76 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-05-12 05:00:30 | Wellawaya (Kirindi Oya) | 1.80 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2026-05-12 04:42:35 | Putupaula (Kalu Ganga) | 0.95 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-05-12 04:39:44 | Magura (Kalu Ganga) | 2.65 | 🟢 Normal | 0.111 | 🔺 Rising |
| 2026-05-12 04:36:58 | Baddegama (Gin Ganga) | 1.67 | 🟢 Normal | 0.033 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-12 04:02:21 | Hanwella (Kelani Ganga) | 1.92 | 🟢 Normal | 0.151 | 🔺 Rising |
| 2026-05-12 05:10:10 | Holombuwa (Kelani Ganga) | 0.90 | 🟢 Normal | 0.133 | 🔺 Rising |
| 2026-05-12 05:06:46 | Magura (Kalu Ganga) | 2.70 | 🟢 Normal | 0.111 | 🔺 Rising |
| 2026-05-12 05:00:30 | Wellawaya (Kirindi Oya) | 1.80 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2026-05-11 18:01:53 | Thanthirimale (Malwathu Oya) | 3.12 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-05-12 03:06:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.88 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-05-12 05:01:06 | Badalgama (Maha Oya) | 2.76 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-05-12 05:12:51 | Baddegama (Gin Ganga) | 1.69 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-05-12 05:05:08 | Moraketiya (Walawe Ganga) | 1.32 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-05-12 05:16:18 | Pitabeddara (Nilwala Ganga) | 0.78 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-05-12 04:42:35 | Putupaula (Kalu Ganga) | 0.95 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-05-12 05:04:47 | Moragaswewa (Deduru Oya) | 2.25 | 🟢 Normal | 0.000 |  |
| 2026-05-12 05:03:22 | Yaka Wewa (Ma Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-05-12 05:04:59 | Horowpothana (Yan Oya) | 2.15 | 🟢 Normal | 0.000 |  |
| 2026-05-12 05:01:30 | Ellagawa (Kalu Ganga) | 5.88 | 🟢 Normal | 0.000 |  |
| 2026-05-12 05:11:56 | Padiyathalawa (Maduru Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-05-12 05:06:30 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-05-12 04:05:36 | Urawa (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-05-12 05:02:47 | Norwood (Kelani Ganga) | 0.78 | 🟢 Normal | -0.010 |  |
| 2026-05-12 05:02:47 | Deraniyagala (Kelani Ganga) | 0.90 | 🟢 Normal | -0.010 |  |
| 2026-05-12 05:02:18 | Thawalama (Gin Ganga) | 1.76 | 🟢 Normal | -0.011 |  |
| 2026-05-12 05:02:02 | Thalgahagoda (Nilwala Ganga) | 0.44 | 🟢 Normal | -0.011 |  |
| 2026-05-12 05:04:22 | Giriulla (Maha Oya) | 1.74 | 🟢 Normal | -0.019 |  |
| 2026-05-12 05:04:36 | Thaldena (Mahaweli Ganga) | 0.78 | 🟢 Normal | -0.020 |  |
| 2026-05-12 05:03:38 | Kithulgala (Kelani Ganga) | 1.53 | 🟢 Normal | -0.020 |  |
| 2026-05-12 05:02:57 | Manampitiya (Mahaweli Ganga) | 0.82 | 🟢 Normal | -0.020 |  |
| 2026-05-12 03:06:54 | Panadugama (Nilwala Ganga) | 2.59 | 🟢 Normal | -0.021 |  |
| 2026-05-12 05:02:46 | Thanamalwila (Kirindi Oya) | 2.20 | 🟢 Normal | -0.030 |  |
| 2026-05-12 05:02:28 | Dunamale (Aththanagalu Oya) | 1.57 | 🟢 Normal | -0.030 |  |
| 2026-05-12 05:02:03 | Nakkala (Kumbukkan Oya) | 1.26 | 🟢 Normal | -0.031 |  |
| 2026-05-12 05:14:32 | Peradeniya (Mahaweli Ganga) | 1.47 | 🟢 Normal | -0.034 |  |
| 2026-05-12 05:14:02 | Rathnapura (Kalu Ganga) | 2.02 | 🟢 Normal | -0.042 |  |
| 2026-05-12 05:07:04 | Katharagama (Menik Ganga) | 2.25 | 🟢 Normal | -0.048 |  |
| 2026-05-12 05:05:50 | Siyambalanduwa (Heda Oya) | 0.99 | 🟢 Normal | -0.049 |  |
| 2026-05-11 18:02:56 | Weraganthota (Mahaweli Ganga) | -2.75 | 🟢 Normal | -0.049 |  |
| 2026-05-12 05:01:29 | Kuda Oya (Kirindi Oya) | 2.30 | 🟢 Normal | -0.060 |  |
| 2026-05-12 05:01:46 | Nawalapitiya (Mahaweli Ganga) | 1.03 | 🟢 Normal | -0.061 |  |
| 2026-05-12 04:18:37 | Glencourse (Kelani Ganga) | 10.53 | 🟢 Normal | -0.073 |  |
| 2026-05-11 18:06:15 | Galgamuwa (Mee Oya) | 1.40 | 🟢 Normal | -0.074 |  |

## River Water Level Charts by Station

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)