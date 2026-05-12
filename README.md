# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--12_14:07:01-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **149,847 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **32** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-12 14:07:01 | Rathnapura (Kalu Ganga) | 1.65 | 🟢 Normal | -0.022 |  |
| 2026-05-12 14:06:39 | Thanthirimale (Malwathu Oya) | 3.40 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-12 14:06:30 | Siyambalanduwa (Heda Oya) | 0.69 | 🟢 Normal | -0.019 |  |
| 2026-05-12 14:05:59 | Galgamuwa (Mee Oya) | 1.56 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-05-12 14:05:53 | Horowpothana (Yan Oya) | 2.15 | 🟢 Normal | 0.000 |  |
| 2026-05-12 14:05:20 | Manampitiya (Mahaweli Ganga) | 0.87 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-05-12 14:05:17 | Thalgahagoda (Nilwala Ganga) | 0.66 | 🟢 Normal | -0.010 |  |
| 2026-05-12 14:04:57 | Putupaula (Kalu Ganga) | 1.10 | 🟢 Normal | -0.020 |  |
| 2026-05-12 14:04:55 | Thanamalwila (Kirindi Oya) | 1.97 | 🟢 Normal | -0.019 |  |
| 2026-05-12 14:04:35 | Hanwella (Kelani Ganga) | 1.82 | 🟢 Normal | -0.052 |  |
| 2026-05-12 14:04:21 | Moragaswewa (Deduru Oya) | 2.29 | 🟢 Normal | -0.031 |  |
| 2026-05-12 14:04:03 | Panadugama (Nilwala Ganga) | 3.03 | 🟢 Normal | 0.187 | 🔺 Rising |
| 2026-05-12 14:03:58 | Norwood (Kelani Ganga) | 0.73 | 🟢 Normal | -0.010 |  |
| 2026-05-12 14:03:29 | Giriulla (Maha Oya) | 1.53 | 🟢 Normal | -0.020 |  |
| 2026-05-12 14:03:22 | Deraniyagala (Kelani Ganga) | 0.71 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-12 14:03:22 | Baddegama (Gin Ganga) | 1.72 | 🟢 Normal | -0.011 |  |
| 2026-05-12 14:02:58 | Katharagama (Menik Ganga) | 2.03 | 🟢 Normal | -0.029 |  |
| 2026-05-12 14:02:33 | Dunamale (Aththanagalu Oya) | 1.44 | 🟢 Normal | 0.000 |  |
| 2026-05-12 14:01:51 | Moraketiya (Walawe Ganga) | 1.10 | 🟢 Normal | -0.021 |  |
| 2026-05-12 14:01:49 | Yaka Wewa (Ma Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-05-12 14:01:41 | Ellagawa (Kalu Ganga) | 5.65 | 🟢 Normal | -0.070 |  |
| 2026-05-12 14:01:31 | Peradeniya (Mahaweli Ganga) | 1.52 | 🟢 Normal | -0.032 |  |
| 2026-05-12 14:01:31 | Nawalapitiya (Mahaweli Ganga) | 0.93 | 🟢 Normal | -0.031 |  |
| 2026-05-12 14:01:27 | Kuda Oya (Kirindi Oya) | 1.97 | 🟢 Normal | -0.020 |  |
| 2026-05-12 14:01:25 | Weraganthota (Mahaweli Ganga) | -2.74 | 🟢 Normal | -0.140 |  |
| 2026-05-12 14:01:21 | Thaldena (Mahaweli Ganga) | 0.69 | 🟢 Normal | -0.045 |  |
| 2026-05-12 14:00:42 | Wellawaya (Kirindi Oya) | 1.63 | 🟢 Normal | 0.000 |  |
| 2026-05-12 14:00:41 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.092 |  |
| 2026-05-12 14:00:06 | Nakkala (Kumbukkan Oya) | 1.10 | 🟢 Normal | -0.020 |  |
| 2026-05-12 13:59:14 | Padiyathalawa (Maduru Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-05-12 13:22:15 | Katharagama (Menik Ganga) | 2.05 | 🟢 Normal | -0.029 |  |
| 2026-05-12 13:21:29 | Thaldena (Mahaweli Ganga) | 0.72 | 🟢 Normal | -0.045 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-12 13:01:11 | Pitabeddara (Nilwala Ganga) | 1.30 | 🟢 Normal | 0.309 | 🔺 Rising |
| 2026-05-12 13:08:22 | Kithulgala (Kelani Ganga) | 1.72 | 🟢 Normal | 0.239 | 🔺 Rising |
| 2026-05-12 14:04:03 | Panadugama (Nilwala Ganga) | 3.03 | 🟢 Normal | 0.187 | 🔺 Rising |
| 2026-05-12 14:05:20 | Manampitiya (Mahaweli Ganga) | 0.87 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-05-12 14:06:39 | Thanthirimale (Malwathu Oya) | 3.40 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-12 14:05:59 | Galgamuwa (Mee Oya) | 1.56 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-05-12 13:06:59 | Badalgama (Maha Oya) | 2.78 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-12 14:03:22 | Deraniyagala (Kelani Ganga) | 0.71 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-12 14:00:42 | Wellawaya (Kirindi Oya) | 1.63 | 🟢 Normal | 0.000 |  |
| 2026-05-12 14:01:49 | Yaka Wewa (Ma Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-05-12 14:05:53 | Horowpothana (Yan Oya) | 2.15 | 🟢 Normal | 0.000 |  |
| 2026-05-12 13:59:14 | Padiyathalawa (Maduru Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-05-12 14:02:33 | Dunamale (Aththanagalu Oya) | 1.44 | 🟢 Normal | 0.000 |  |
| 2026-05-12 13:10:59 | Urawa (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-05-12 14:03:58 | Norwood (Kelani Ganga) | 0.73 | 🟢 Normal | -0.010 |  |
| 2026-05-12 14:05:17 | Thalgahagoda (Nilwala Ganga) | 0.66 | 🟢 Normal | -0.010 |  |
| 2026-05-12 14:03:22 | Baddegama (Gin Ganga) | 1.72 | 🟢 Normal | -0.011 |  |
| 2026-05-12 14:06:30 | Siyambalanduwa (Heda Oya) | 0.69 | 🟢 Normal | -0.019 |  |
| 2026-05-12 14:04:55 | Thanamalwila (Kirindi Oya) | 1.97 | 🟢 Normal | -0.019 |  |
| 2026-05-12 14:04:57 | Putupaula (Kalu Ganga) | 1.10 | 🟢 Normal | -0.020 |  |
| 2026-05-12 14:00:06 | Nakkala (Kumbukkan Oya) | 1.10 | 🟢 Normal | -0.020 |  |
| 2026-05-12 14:01:27 | Kuda Oya (Kirindi Oya) | 1.97 | 🟢 Normal | -0.020 |  |
| 2026-05-12 14:03:29 | Giriulla (Maha Oya) | 1.53 | 🟢 Normal | -0.020 |  |
| 2026-05-12 13:04:30 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.90 | 🟢 Normal | -0.021 |  |
| 2026-05-12 13:02:17 | Holombuwa (Kelani Ganga) | 0.78 | 🟢 Normal | -0.021 |  |
| 2026-05-12 14:01:51 | Moraketiya (Walawe Ganga) | 1.10 | 🟢 Normal | -0.021 |  |
| 2026-05-12 14:07:01 | Rathnapura (Kalu Ganga) | 1.65 | 🟢 Normal | -0.022 |  |
| 2026-05-12 14:02:58 | Katharagama (Menik Ganga) | 2.03 | 🟢 Normal | -0.029 |  |
| 2026-05-12 13:02:22 | Glencourse (Kelani Ganga) | 9.87 | 🟢 Normal | -0.030 |  |
| 2026-05-12 14:01:31 | Nawalapitiya (Mahaweli Ganga) | 0.93 | 🟢 Normal | -0.031 |  |
| 2026-05-12 14:04:21 | Moragaswewa (Deduru Oya) | 2.29 | 🟢 Normal | -0.031 |  |
| 2026-05-12 14:01:31 | Peradeniya (Mahaweli Ganga) | 1.52 | 🟢 Normal | -0.032 |  |
| 2026-05-12 13:09:28 | Magura (Kalu Ganga) | 2.36 | 🟢 Normal | -0.039 |  |
| 2026-05-12 14:01:21 | Thaldena (Mahaweli Ganga) | 0.69 | 🟢 Normal | -0.045 |  |
| 2026-05-12 14:04:35 | Hanwella (Kelani Ganga) | 1.82 | 🟢 Normal | -0.052 |  |
| 2026-05-12 14:01:41 | Ellagawa (Kalu Ganga) | 5.65 | 🟢 Normal | -0.070 |  |
| 2026-05-12 14:00:41 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.092 |  |
| 2026-05-12 13:04:55 | Thawalama (Gin Ganga) | 2.04 | 🟢 Normal | -0.094 |  |
| 2026-05-12 14:01:25 | Weraganthota (Mahaweli Ganga) | -2.74 | 🟢 Normal | -0.140 |  |

## River Water Level Charts by Station

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)