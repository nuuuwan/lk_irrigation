# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--22_08:06:01-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **79,798 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-22 08:06:01 | Badalgama (Maha Oya) | 1.81 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-22 08:05:56 | Holombuwa (Kelani Ganga) | 1.08 | 🟢 Normal | -0.020 |  |
| 2026-02-22 08:05:47 | Thawalama (Gin Ganga) | 3.00 | 🟢 Normal | -0.103 |  |
| 2026-02-22 08:05:37 | Kuda Oya (Kirindi Oya) | 2.42 | 🟢 Normal | 0.000 |  |
| 2026-02-22 08:05:25 | Pitabeddara (Nilwala Ganga) | 2.07 | 🟢 Normal | -0.111 |  |
| 2026-02-22 08:05:19 | Thanamalwila (Kirindi Oya) | 1.84 | 🟢 Normal | -0.084 |  |
| 2026-02-22 08:05:03 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.128 |  |
| 2026-02-22 08:04:50 | Peradeniya (Mahaweli Ganga) | 2.68 | 🟢 Normal | -0.020 |  |
| 2026-02-22 08:04:05 | Urawa (Nilwala Ganga) | 0.88 | 🟢 Normal | -0.068 |  |
| 2026-02-22 08:04:02 | Katharagama (Menik Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-02-22 08:03:54 | Panadugama (Nilwala Ganga) | 4.47 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-02-22 08:03:45 | Hanwella (Kelani Ganga) | 2.94 | 🟢 Normal | -0.041 |  |
| 2026-02-22 08:03:36 | Thaldena (Mahaweli Ganga) | 0.90 | 🟢 Normal | -0.021 |  |
| 2026-02-22 08:03:34 | Horowpothana (Yan Oya) | 1.78 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-02-22 08:03:32 | Siyambalanduwa (Heda Oya) | 0.87 | 🟢 Normal | -0.030 |  |
| 2026-02-22 08:03:15 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.72 | 🟢 Normal | 0.810 | 🔺 Rising |
| 2026-02-22 08:03:11 | Kithulgala (Kelani Ganga) | 1.36 | 🟢 Normal | -0.185 |  |
| 2026-02-22 08:03:08 | Thanthirimale (Malwathu Oya) | 1.28 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-22 08:02:53 | Deraniyagala (Kelani Ganga) | 0.83 | 🟢 Normal | -0.081 |  |
| 2026-02-22 08:02:43 | Manampitiya (Mahaweli Ganga) | 4.45 | 🟠 Minor Flood | 0.000 |  |
| 2026-02-22 08:02:31 | Giriulla (Maha Oya) | 2.55 | 🟢 Normal | -0.181 |  |
| 2026-02-22 08:02:28 | Baddegama (Gin Ganga) | 2.54 | 🟢 Normal | 0.112 | 🔺 Rising |
| 2026-02-22 08:02:24 | Wellawaya (Kirindi Oya) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-02-22 08:01:58 | Galgamuwa (Mee Oya) | 0.06 | 🟢 Normal | 36.000 | 🔺 Rising |
| 2026-02-22 08:01:57 | Galgamuwa (Mee Oya) | 0.05 | 🟢 Normal | 36.000 | 🔺 Rising |
| 2026-02-22 08:01:52 | Weraganthota (Mahaweli Ganga) | -0.86 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-02-22 08:01:44 | Glencourse (Kelani Ganga) | 10.86 | 🟢 Normal | -0.219 |  |
| 2026-02-22 08:01:23 | Magura (Kalu Ganga) | 3.60 | 🟢 Normal | -0.055 |  |
| 2026-02-22 08:01:11 | Ellagawa (Kalu Ganga) | 7.60 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-02-22 08:01:04 | Padiyathalawa (Maduru Oya) | 1.50 | 🟢 Normal | -0.030 |  |
| 2026-02-22 08:00:58 | Nawalapitiya (Mahaweli Ganga) | 1.27 | 🟢 Normal | -0.020 |  |
| 2026-02-22 08:00:55 | Nakkala (Kumbukkan Oya) | 1.53 | 🟢 Normal | -0.030 |  |
| 2026-02-22 08:00:48 | Moraketiya (Walawe Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-02-22 08:00:44 | Moragaswewa (Deduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-02-22 07:58:04 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.65 | 🟢 Normal | 0.810 | 🔺 Rising |
| 2026-02-22 07:49:16 | Pitabeddara (Nilwala Ganga) | 2.10 | 🟢 Normal | -0.111 |  |
| 2026-02-22 07:24:29 | Horowpothana (Yan Oya) | 1.72 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-02-22 07:24:25 | Yaka Wewa (Ma Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-02-22 07:24:14 | Horowpothana (Yan Oya) | 1.72 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-02-22 07:19:47 | Urawa (Nilwala Ganga) | 0.93 | 🟢 Normal | -0.068 |  |
| 2026-02-22 07:19:31 | Baddegama (Gin Ganga) | 2.46 | 🟢 Normal | 0.112 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-22 08:02:43 | Manampitiya (Mahaweli Ganga) | 4.45 | 🟠 Minor Flood | 0.000 |  |
| 2026-02-22 08:01:58 | Galgamuwa (Mee Oya) | 0.06 | 🟢 Normal | 36.000 | 🔺 Rising |
| 2026-02-22 08:03:15 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.72 | 🟢 Normal | 0.810 | 🔺 Rising |
| 2026-02-22 07:00:36 | Thalgahagoda (Nilwala Ganga) | 0.95 | 🟢 Normal | 0.156 | 🔺 Rising |
| 2026-02-22 08:02:28 | Baddegama (Gin Ganga) | 2.54 | 🟢 Normal | 0.112 | 🔺 Rising |
| 2026-02-22 08:03:34 | Horowpothana (Yan Oya) | 1.78 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-02-22 08:03:54 | Panadugama (Nilwala Ganga) | 4.47 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-02-22 08:01:11 | Ellagawa (Kalu Ganga) | 7.60 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-02-22 07:07:30 | Putupaula (Kalu Ganga) | 1.30 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-02-22 08:01:52 | Weraganthota (Mahaweli Ganga) | -0.86 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-02-22 08:03:08 | Thanthirimale (Malwathu Oya) | 1.28 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-22 08:06:01 | Badalgama (Maha Oya) | 1.81 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-22 08:02:24 | Wellawaya (Kirindi Oya) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-02-22 08:00:44 | Moragaswewa (Deduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-02-22 07:24:25 | Yaka Wewa (Ma Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-02-22 08:00:48 | Moraketiya (Walawe Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-02-22 08:04:02 | Katharagama (Menik Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-02-22 08:05:37 | Kuda Oya (Kirindi Oya) | 2.42 | 🟢 Normal | 0.000 |  |
| 2026-02-22 07:08:41 | Dunamale (Aththanagalu Oya) | 1.48 | 🟢 Normal | -0.018 |  |
| 2026-02-22 08:00:58 | Nawalapitiya (Mahaweli Ganga) | 1.27 | 🟢 Normal | -0.020 |  |
| 2026-02-22 08:05:56 | Holombuwa (Kelani Ganga) | 1.08 | 🟢 Normal | -0.020 |  |
| 2026-02-22 08:04:50 | Peradeniya (Mahaweli Ganga) | 2.68 | 🟢 Normal | -0.020 |  |
| 2026-02-22 08:03:36 | Thaldena (Mahaweli Ganga) | 0.90 | 🟢 Normal | -0.021 |  |
| 2026-02-22 08:01:04 | Padiyathalawa (Maduru Oya) | 1.50 | 🟢 Normal | -0.030 |  |
| 2026-02-22 08:00:55 | Nakkala (Kumbukkan Oya) | 1.53 | 🟢 Normal | -0.030 |  |
| 2026-02-22 08:03:32 | Siyambalanduwa (Heda Oya) | 0.87 | 🟢 Normal | -0.030 |  |
| 2026-02-22 08:03:45 | Hanwella (Kelani Ganga) | 2.94 | 🟢 Normal | -0.041 |  |
| 2026-02-22 07:01:56 | Norwood (Kelani Ganga) | 1.05 | 🟢 Normal | -0.052 |  |
| 2026-02-22 08:01:23 | Magura (Kalu Ganga) | 3.60 | 🟢 Normal | -0.055 |  |
| 2026-02-22 08:04:05 | Urawa (Nilwala Ganga) | 0.88 | 🟢 Normal | -0.068 |  |
| 2026-02-22 08:02:53 | Deraniyagala (Kelani Ganga) | 0.83 | 🟢 Normal | -0.081 |  |
| 2026-02-22 08:05:19 | Thanamalwila (Kirindi Oya) | 1.84 | 🟢 Normal | -0.084 |  |
| 2026-02-22 08:05:47 | Thawalama (Gin Ganga) | 3.00 | 🟢 Normal | -0.103 |  |
| 2026-02-22 08:05:25 | Pitabeddara (Nilwala Ganga) | 2.07 | 🟢 Normal | -0.111 |  |
| 2026-02-22 07:04:36 | Rathnapura (Kalu Ganga) | 4.54 | 🟢 Normal | -0.119 |  |
| 2026-02-22 08:05:03 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.128 |  |
| 2026-02-22 08:02:31 | Giriulla (Maha Oya) | 2.55 | 🟢 Normal | -0.181 |  |
| 2026-02-22 08:03:11 | Kithulgala (Kelani Ganga) | 1.36 | 🟢 Normal | -0.185 |  |
| 2026-02-22 08:01:44 | Glencourse (Kelani Ganga) | 10.86 | 🟢 Normal | -0.219 |  |

## River Water Level Charts by Station

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)