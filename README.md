# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--12_22:23:12-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **71,408 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-12 22:23:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.90 | 🟢 Normal | 0.163 | 🔺 Rising |
| 2026-02-12 22:22:53 | Urawa (Nilwala Ganga) | 0.04 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-02-12 22:18:25 | Thalgahagoda (Nilwala Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-02-12 22:17:05 | Dunamale (Aththanagalu Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-02-12 22:16:10 | Rathnapura (Kalu Ganga) | 0.63 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-02-12 22:13:16 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | -0.088 |  |
| 2026-02-12 22:10:11 | Glencourse (Kelani Ganga) | 8.30 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-02-12 22:09:35 | Pitabeddara (Nilwala Ganga) | 0.26 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-12 22:09:16 | Holombuwa (Kelani Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-02-12 22:08:03 | Baddegama (Gin Ganga) | 1.20 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-02-12 22:06:28 | Katharagama (Menik Ganga) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-02-12 22:06:00 | Badalgama (Maha Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-02-12 22:05:30 | Ellagawa (Kalu Ganga) | 3.93 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-02-12 22:05:00 | Thanamalwila (Kirindi Oya) | 0.43 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-12 22:04:51 | Manampitiya (Mahaweli Ganga) | 0.64 | 🟢 Normal | -0.029 |  |
| 2026-02-12 22:04:50 | Nawalapitiya (Mahaweli Ganga) | 0.76 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-02-12 22:04:44 | Rathnapura (Kalu Ganga) | 0.62 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-02-12 22:04:37 | Moragaswewa (Deduru Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-02-12 22:04:28 | Kuda Oya (Kirindi Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-02-12 22:04:21 | Padiyathalawa (Maduru Oya) | 1.40 | 🟢 Normal | 0.199 | 🔺 Rising |
| 2026-02-12 22:03:58 | Deraniyagala (Kelani Ganga) | 0.07 | 🟢 Normal | -0.020 |  |
| 2026-02-12 22:03:53 | Magura (Kalu Ganga) | 0.79 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-02-12 22:03:23 | Kithulgala (Kelani Ganga) | 1.60 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2026-02-12 22:02:59 | Wellawaya (Kirindi Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-02-12 22:02:48 | Giriulla (Maha Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-02-12 22:02:46 | Hanwella (Kelani Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-02-12 22:02:32 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-02-12 22:02:27 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-02-12 22:01:41 | Yaka Wewa (Ma Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-02-12 22:01:37 | Horowpothana (Yan Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-02-12 22:01:24 | Nakkala (Kumbukkan Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-02-12 22:01:22 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-02-12 22:00:54 | Peradeniya (Mahaweli Ganga) | 2.30 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-12 22:00:14 | Moraketiya (Walawe Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-02-12 21:59:39 | Thaldena (Mahaweli Ganga) | 0.82 | 🟢 Normal | -0.011 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-12 22:04:21 | Padiyathalawa (Maduru Oya) | 1.40 | 🟢 Normal | 0.199 | 🔺 Rising |
| 2026-02-12 22:23:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.90 | 🟢 Normal | 0.163 | 🔺 Rising |
| 2026-02-12 22:03:23 | Kithulgala (Kelani Ganga) | 1.60 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2026-02-12 22:16:10 | Rathnapura (Kalu Ganga) | 0.63 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-02-12 22:03:53 | Magura (Kalu Ganga) | 0.79 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-02-12 22:04:50 | Nawalapitiya (Mahaweli Ganga) | 0.76 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-02-12 22:02:27 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-02-12 22:05:30 | Ellagawa (Kalu Ganga) | 3.93 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-02-12 22:00:54 | Peradeniya (Mahaweli Ganga) | 2.30 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-12 22:10:11 | Glencourse (Kelani Ganga) | 8.30 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-02-12 22:22:53 | Urawa (Nilwala Ganga) | 0.04 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-02-12 18:00:26 | Galgamuwa (Mee Oya) | 0.15 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-02-12 22:08:03 | Baddegama (Gin Ganga) | 1.20 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-02-12 22:05:00 | Thanamalwila (Kirindi Oya) | 0.43 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-12 18:02:36 | Weraganthota (Mahaweli Ganga) | -2.83 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-12 22:09:35 | Pitabeddara (Nilwala Ganga) | 0.26 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-12 22:02:59 | Wellawaya (Kirindi Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-02-12 22:01:24 | Nakkala (Kumbukkan Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-02-12 22:04:37 | Moragaswewa (Deduru Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-02-12 22:01:41 | Yaka Wewa (Ma Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-02-12 22:02:48 | Giriulla (Maha Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-02-12 22:01:37 | Horowpothana (Yan Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-02-12 22:02:32 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-02-12 22:02:46 | Hanwella (Kelani Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-02-12 21:05:26 | Panadugama (Nilwala Ganga) | 1.96 | 🟢 Normal | 0.000 |  |
| 2026-02-12 22:00:14 | Moraketiya (Walawe Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-02-12 22:01:22 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-02-12 22:17:05 | Dunamale (Aththanagalu Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-02-12 22:06:28 | Katharagama (Menik Ganga) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-02-12 22:06:00 | Badalgama (Maha Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-02-12 22:09:16 | Holombuwa (Kelani Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-02-12 18:01:34 | Thanthirimale (Malwathu Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-02-12 22:18:25 | Thalgahagoda (Nilwala Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-02-12 22:04:28 | Kuda Oya (Kirindi Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-02-12 21:59:39 | Thaldena (Mahaweli Ganga) | 0.82 | 🟢 Normal | -0.011 |  |
| 2026-02-12 22:03:58 | Deraniyagala (Kelani Ganga) | 0.07 | 🟢 Normal | -0.020 |  |
| 2026-02-12 21:10:40 | Thawalama (Gin Ganga) | 1.03 | 🟢 Normal | -0.021 |  |
| 2026-02-12 22:04:51 | Manampitiya (Mahaweli Ganga) | 0.64 | 🟢 Normal | -0.029 |  |
| 2026-02-12 22:13:16 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | -0.088 |  |

## River Water Level Charts by Station

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

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

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)