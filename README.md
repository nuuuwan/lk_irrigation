# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--20_19:20:38-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **157,223 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-20 19:20:38 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.22 | 🟢 Normal | 0.000 |  |
| 2026-05-20 19:16:32 | Ellagawa (Kalu Ganga) | 5.30 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-05-20 19:14:49 | Kithulgala (Kelani Ganga) | 1.81 | 🟢 Normal | -0.034 |  |
| 2026-05-20 19:13:46 | Magura (Kalu Ganga) | 1.73 | 🟢 Normal | 0.000 |  |
| 2026-05-20 19:13:12 | Urawa (Nilwala Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-05-20 19:09:00 | Moragaswewa (Deduru Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-05-20 19:08:35 | Giriulla (Maha Oya) | 1.36 | 🟢 Normal | -0.093 |  |
| 2026-05-20 19:08:09 | Holombuwa (Kelani Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-05-20 19:06:57 | Padiyathalawa (Maduru Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-05-20 19:06:49 | Badalgama (Maha Oya) | 2.71 | 🟢 Normal | 0.000 |  |
| 2026-05-20 19:06:38 | Thalgahagoda (Nilwala Ganga) | 0.48 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-05-20 19:06:23 | Pitabeddara (Nilwala Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-05-20 19:06:03 | Baddegama (Gin Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-05-20 19:05:37 | Rathnapura (Kalu Ganga) | 1.61 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-05-20 19:05:05 | Norwood (Kelani Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-20 19:04:51 | Putupaula (Kalu Ganga) | 0.92 | 🟢 Normal | -0.028 |  |
| 2026-05-20 19:04:29 | Deraniyagala (Kelani Ganga) | 1.03 | 🟢 Normal | 0.176 | 🔺 Rising |
| 2026-05-20 19:04:12 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-05-20 19:03:43 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-05-20 19:03:39 | Peradeniya (Mahaweli Ganga) | 1.35 | 🟢 Normal | -0.022 |  |
| 2026-05-20 19:03:20 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.117 |  |
| 2026-05-20 19:03:16 | Moragaswewa (Deduru Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-05-20 19:03:14 | Nakkala (Kumbukkan Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-05-20 19:03:11 | Kuda Oya (Kirindi Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-05-20 19:03:11 | Hanwella (Kelani Ganga) | 1.68 | 🟢 Normal | -0.010 |  |
| 2026-05-20 19:02:47 | Yaka Wewa (Ma Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-05-20 19:02:25 | Thawalama (Gin Ganga) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-05-20 19:02:22 | Thaldena (Mahaweli Ganga) | 0.34 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-20 19:01:59 | Dunamale (Aththanagalu Oya) | 2.34 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-05-20 19:01:29 | Glencourse (Kelani Ganga) | 9.61 | 🟢 Normal | -0.062 |  |
| 2026-05-20 19:01:21 | Manampitiya (Mahaweli Ganga) | 0.23 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-05-20 19:01:15 | Nawalapitiya (Mahaweli Ganga) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-05-20 19:00:58 | Thanamalwila (Kirindi Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-05-20 19:00:47 | Horowpothana (Yan Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-05-20 19:00:35 | Wellawaya (Kirindi Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-05-20 19:00:26 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-20 19:04:29 | Deraniyagala (Kelani Ganga) | 1.03 | 🟢 Normal | 0.176 | 🔺 Rising |
| 2026-05-20 19:05:37 | Rathnapura (Kalu Ganga) | 1.61 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-05-20 19:06:38 | Thalgahagoda (Nilwala Ganga) | 0.48 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-05-20 19:01:21 | Manampitiya (Mahaweli Ganga) | 0.23 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-05-20 19:01:59 | Dunamale (Aththanagalu Oya) | 2.34 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-05-20 19:16:32 | Ellagawa (Kalu Ganga) | 5.30 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-05-20 19:02:22 | Thaldena (Mahaweli Ganga) | 0.34 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-20 18:01:24 | Weraganthota (Mahaweli Ganga) | -3.34 | 🟢 Normal | 0.000 |  |
| 2026-05-20 19:00:35 | Wellawaya (Kirindi Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-05-20 19:03:14 | Nakkala (Kumbukkan Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-05-20 19:09:00 | Moragaswewa (Deduru Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-05-20 19:01:15 | Nawalapitiya (Mahaweli Ganga) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-05-20 19:02:47 | Yaka Wewa (Ma Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-05-20 19:00:47 | Horowpothana (Yan Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-05-20 19:13:46 | Magura (Kalu Ganga) | 1.73 | 🟢 Normal | 0.000 |  |
| 2026-05-20 19:06:23 | Pitabeddara (Nilwala Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-05-20 19:05:05 | Norwood (Kelani Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-20 19:06:03 | Baddegama (Gin Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-05-20 18:06:16 | Panadugama (Nilwala Ganga) | 2.43 | 🟢 Normal | 0.000 |  |
| 2026-05-20 19:06:57 | Padiyathalawa (Maduru Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-05-20 19:03:43 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-05-20 19:00:26 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-05-20 19:04:12 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-05-20 19:06:49 | Badalgama (Maha Oya) | 2.71 | 🟢 Normal | 0.000 |  |
| 2026-05-20 19:08:09 | Holombuwa (Kelani Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-05-20 19:02:25 | Thawalama (Gin Ganga) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-05-20 19:13:12 | Urawa (Nilwala Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-05-20 19:03:11 | Kuda Oya (Kirindi Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-05-20 19:00:58 | Thanamalwila (Kirindi Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-05-20 19:20:38 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.22 | 🟢 Normal | 0.000 |  |
| 2026-05-20 19:03:11 | Hanwella (Kelani Ganga) | 1.68 | 🟢 Normal | -0.010 |  |
| 2026-05-20 18:01:19 | Galgamuwa (Mee Oya) | 0.76 | 🟢 Normal | -0.011 |  |
| 2026-05-20 19:03:39 | Peradeniya (Mahaweli Ganga) | 1.35 | 🟢 Normal | -0.022 |  |
| 2026-05-20 19:04:51 | Putupaula (Kalu Ganga) | 0.92 | 🟢 Normal | -0.028 |  |
| 2026-05-20 18:02:19 | Thanthirimale (Malwathu Oya) | 1.98 | 🟢 Normal | -0.030 |  |
| 2026-05-20 19:14:49 | Kithulgala (Kelani Ganga) | 1.81 | 🟢 Normal | -0.034 |  |
| 2026-05-20 19:01:29 | Glencourse (Kelani Ganga) | 9.61 | 🟢 Normal | -0.062 |  |
| 2026-05-20 19:08:35 | Giriulla (Maha Oya) | 1.36 | 🟢 Normal | -0.093 |  |
| 2026-05-20 19:03:20 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.117 |  |

## River Water Level Charts by Station

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)