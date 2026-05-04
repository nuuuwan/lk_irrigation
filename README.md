# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--04_21:09:09-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **142,976 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-04 21:09:09 | Urawa (Nilwala Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-05-04 21:08:10 | Panadugama (Nilwala Ganga) | 2.06 | 🟢 Normal | 0.000 |  |
| 2026-05-04 21:07:44 | Hanwella (Kelani Ganga) | 0.43 | 🟢 Normal | -0.010 |  |
| 2026-05-04 21:07:26 | Ellagawa (Kalu Ganga) | 4.30 | 🟢 Normal | 0.000 |  |
| 2026-05-04 21:06:40 | Magura (Kalu Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-05-04 21:06:06 | Thanamalwila (Kirindi Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-05-04 21:06:00 | Peradeniya (Mahaweli Ganga) | 1.30 | 🟢 Normal | 0.227 | 🔺 Rising |
| 2026-05-04 21:05:58 | Padiyathalawa (Maduru Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-05-04 21:05:11 | Baddegama (Gin Ganga) | 1.07 | 🟢 Normal | -0.041 |  |
| 2026-05-04 21:05:01 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.070 |  |
| 2026-05-04 21:04:53 | Holombuwa (Kelani Ganga) | 0.34 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2026-05-04 21:04:41 | Badalgama (Maha Oya) | 1.86 | 🟢 Normal | -0.011 |  |
| 2026-05-04 21:04:38 | Deraniyagala (Kelani Ganga) | 0.43 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-05-04 21:04:24 | Thawalama (Gin Ganga) | 1.29 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-05-04 21:04:16 | Wellawaya (Kirindi Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-05-04 21:03:58 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-05-04 21:03:57 | Thalgahagoda (Nilwala Ganga) | 0.31 | 🟢 Normal | -0.048 |  |
| 2026-05-04 21:03:55 | Giriulla (Maha Oya) | 0.81 | 🟢 Normal | -0.010 |  |
| 2026-05-04 21:03:38 | Manampitiya (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-04 21:02:48 | Thaldena (Mahaweli Ganga) | 0.50 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-04 21:02:47 | Glencourse (Kelani Ganga) | 8.45 | 🟢 Normal | -0.053 |  |
| 2026-05-04 21:02:46 | Pitabeddara (Nilwala Ganga) | 0.30 | 🟢 Normal | -0.010 |  |
| 2026-05-04 21:02:44 | Nawalapitiya (Mahaweli Ganga) | 0.78 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-05-04 21:02:36 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-04 21:02:36 | Rathnapura (Kalu Ganga) | 2.25 | 🟢 Normal | 0.409 | 🔺 Rising |
| 2026-05-04 21:02:20 | Moragaswewa (Deduru Oya) | 0.26 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-05-04 21:02:19 | Kithulgala (Kelani Ganga) | 1.40 | 🟢 Normal | -0.462 |  |
| 2026-05-04 21:02:19 | Dunamale (Aththanagalu Oya) | 0.49 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-04 21:01:41 | Norwood (Kelani Ganga) | 1.20 | 🟢 Normal | -0.061 |  |
| 2026-05-04 21:01:38 | Horowpothana (Yan Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-05-04 21:01:25 | Yaka Wewa (Ma Oya) | 1.05 | 🟢 Normal | 0.462 | 🔺 Rising |
| 2026-05-04 21:01:22 | Putupaula (Kalu Ganga) | 0.44 | 🟢 Normal | -0.133 |  |
| 2026-05-04 21:01:20 | Kuda Oya (Kirindi Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-05-04 21:01:15 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-05-04 21:00:23 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-04 21:01:25 | Yaka Wewa (Ma Oya) | 1.05 | 🟢 Normal | 0.462 | 🔺 Rising |
| 2026-05-04 21:02:36 | Rathnapura (Kalu Ganga) | 2.25 | 🟢 Normal | 0.409 | 🔺 Rising |
| 2026-05-04 21:06:00 | Peradeniya (Mahaweli Ganga) | 1.30 | 🟢 Normal | 0.227 | 🔺 Rising |
| 2026-05-04 21:02:44 | Nawalapitiya (Mahaweli Ganga) | 0.78 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-05-04 21:04:53 | Holombuwa (Kelani Ganga) | 0.34 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2026-05-04 21:04:24 | Thawalama (Gin Ganga) | 1.29 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-05-04 21:03:58 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-05-04 21:04:38 | Deraniyagala (Kelani Ganga) | 0.43 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-05-04 21:02:20 | Moragaswewa (Deduru Oya) | 0.26 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-05-04 21:02:19 | Dunamale (Aththanagalu Oya) | 0.49 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-04 21:02:36 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-04 21:02:48 | Thaldena (Mahaweli Ganga) | 0.50 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-04 21:03:38 | Manampitiya (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-04 18:02:41 | Weraganthota (Mahaweli Ganga) | -3.10 | 🟢 Normal | 0.000 |  |
| 2026-05-04 21:04:16 | Wellawaya (Kirindi Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-05-04 21:00:23 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-05-04 21:01:38 | Horowpothana (Yan Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-05-04 18:01:37 | Galgamuwa (Mee Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-05-04 21:06:40 | Magura (Kalu Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-05-04 21:07:26 | Ellagawa (Kalu Ganga) | 4.30 | 🟢 Normal | 0.000 |  |
| 2026-05-04 21:08:10 | Panadugama (Nilwala Ganga) | 2.06 | 🟢 Normal | 0.000 |  |
| 2026-05-04 21:05:58 | Padiyathalawa (Maduru Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-05-04 21:01:15 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-05-04 18:03:48 | Thanthirimale (Malwathu Oya) | 1.56 | 🟢 Normal | 0.000 |  |
| 2026-05-04 21:09:09 | Urawa (Nilwala Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-05-04 21:01:20 | Kuda Oya (Kirindi Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-05-04 21:06:06 | Thanamalwila (Kirindi Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-05-04 21:07:44 | Hanwella (Kelani Ganga) | 0.43 | 🟢 Normal | -0.010 |  |
| 2026-05-04 21:03:55 | Giriulla (Maha Oya) | 0.81 | 🟢 Normal | -0.010 |  |
| 2026-05-04 21:02:46 | Pitabeddara (Nilwala Ganga) | 0.30 | 🟢 Normal | -0.010 |  |
| 2026-05-04 21:04:41 | Badalgama (Maha Oya) | 1.86 | 🟢 Normal | -0.011 |  |
| 2026-05-04 20:09:32 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.56 | 🟢 Normal | -0.024 |  |
| 2026-05-04 21:05:11 | Baddegama (Gin Ganga) | 1.07 | 🟢 Normal | -0.041 |  |
| 2026-05-04 21:03:57 | Thalgahagoda (Nilwala Ganga) | 0.31 | 🟢 Normal | -0.048 |  |
| 2026-05-04 21:02:47 | Glencourse (Kelani Ganga) | 8.45 | 🟢 Normal | -0.053 |  |
| 2026-05-04 21:01:41 | Norwood (Kelani Ganga) | 1.20 | 🟢 Normal | -0.061 |  |
| 2026-05-04 21:05:01 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.070 |  |
| 2026-05-04 21:01:22 | Putupaula (Kalu Ganga) | 0.44 | 🟢 Normal | -0.133 |  |
| 2026-05-04 21:02:19 | Kithulgala (Kelani Ganga) | 1.40 | 🟢 Normal | -0.462 |  |

## River Water Level Charts by Station

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)