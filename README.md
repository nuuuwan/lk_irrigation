# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--07_18:12:47-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **39,297 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-07 18:12:47 | Urawa (Nilwala Ganga) | 1.22 | 🟢 Normal | 0.218 | 🔺 Rising |
| 2026-01-07 18:09:01 | Padiyathalawa (Maduru Oya) | 1.22 | 🟢 Normal | -0.009 |  |
| 2026-01-07 18:08:59 | Manampitiya (Mahaweli Ganga) | 2.61 | 🟢 Normal | -0.041 |  |
| 2026-01-07 18:07:46 | Ellagawa (Kalu Ganga) | 4.20 | 🟢 Normal | 0.000 |  |
| 2026-01-07 18:06:48 | Rathnapura (Kalu Ganga) | 0.74 | 🟢 Normal | -0.010 |  |
| 2026-01-07 18:06:39 | Baddegama (Gin Ganga) | 1.18 | 🟢 Normal | -0.020 |  |
| 2026-01-07 18:06:25 | Badalgama (Maha Oya) | 2.04 | 🟢 Normal | 0.000 |  |
| 2026-01-07 18:05:50 | Horowpothana (Yan Oya) | 2.50 | 🟢 Normal | -0.009 |  |
| 2026-01-07 18:05:18 | Magura (Kalu Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-01-07 18:04:10 | Kithulgala (Kelani Ganga) | 1.65 | 🟢 Normal | -0.106 |  |
| 2026-01-07 18:04:02 | Siyambalanduwa (Heda Oya) | 1.53 | 🟢 Normal | -0.019 |  |
| 2026-01-07 18:04:01 | Katharagama (Menik Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-01-07 18:03:54 | Thanamalwila (Kirindi Oya) | 1.12 | 🟢 Normal | -0.011 |  |
| 2026-01-07 18:03:54 | Holombuwa (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-01-07 18:03:33 | Glencourse (Kelani Ganga) | 8.61 | 🟢 Normal | -0.010 |  |
| 2026-01-07 18:03:29 | Moragaswewa (Deduru Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-01-07 18:03:25 | Thanthirimale (Malwathu Oya) | 1.77 | 🟢 Normal | -0.023 |  |
| 2026-01-07 18:02:57 | Deraniyagala (Kelani Ganga) | 0.22 | 🟢 Normal | -0.110 |  |
| 2026-01-07 18:02:51 | Pitabeddara (Nilwala Ganga) | 0.88 | 🟢 Normal | 0.172 | 🔺 Rising |
| 2026-01-07 18:02:45 | Giriulla (Maha Oya) | 0.98 | 🟢 Normal | -0.011 |  |
| 2026-01-07 18:02:40 | Dunamale (Aththanagalu Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-01-07 18:02:39 | Wellawaya (Kirindi Oya) | 1.05 | 🟢 Normal | -0.039 |  |
| 2026-01-07 18:02:22 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.46 | 🟢 Normal | -0.010 |  |
| 2026-01-07 18:02:15 | Hanwella (Kelani Ganga) | 0.51 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-01-07 18:02:09 | Peradeniya (Mahaweli Ganga) | 1.63 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-01-07 18:02:09 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | -0.033 |  |
| 2026-01-07 18:02:08 | Thaldena (Mahaweli Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-01-07 18:02:00 | Putupaula (Kalu Ganga) | 0.85 | 🟢 Normal | -0.031 |  |
| 2026-01-07 18:01:49 | Weraganthota (Mahaweli Ganga) | -1.15 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-07 18:01:44 | Yaka Wewa (Ma Oya) | 0.83 | 🟢 Normal | -0.010 |  |
| 2026-01-07 18:01:32 | Thawalama (Gin Ganga) | 1.36 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-01-07 18:01:21 | Galgamuwa (Mee Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-01-07 18:01:19 | Kuda Oya (Kirindi Oya) | 1.37 | 🟢 Normal | -0.010 |  |
| 2026-01-07 18:00:57 | Norwood (Kelani Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-01-07 18:00:56 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-01-07 18:00:18 | Thalgahagoda (Nilwala Ganga) | 0.55 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-01-07 18:00:12 | Nakkala (Kumbukkan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-01-07 18:00:11 | Nawalapitiya (Mahaweli Ganga) | 0.74 | 🟢 Normal | -0.020 |  |
| 2026-01-07 17:55:17 | Moragaswewa (Deduru Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-01-07 17:37:24 | Panadugama (Nilwala Ganga) | 2.50 | 🟢 Normal | -0.007 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-07 18:12:47 | Urawa (Nilwala Ganga) | 1.22 | 🟢 Normal | 0.218 | 🔺 Rising |
| 2026-01-07 18:02:51 | Pitabeddara (Nilwala Ganga) | 0.88 | 🟢 Normal | 0.172 | 🔺 Rising |
| 2026-01-07 18:00:18 | Thalgahagoda (Nilwala Ganga) | 0.55 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-01-07 18:02:15 | Hanwella (Kelani Ganga) | 0.51 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-01-07 18:01:32 | Thawalama (Gin Ganga) | 1.36 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-01-07 18:02:09 | Peradeniya (Mahaweli Ganga) | 1.63 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-01-07 18:01:49 | Weraganthota (Mahaweli Ganga) | -1.15 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-07 18:00:12 | Nakkala (Kumbukkan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-01-07 18:03:29 | Moragaswewa (Deduru Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-01-07 18:01:21 | Galgamuwa (Mee Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-01-07 18:05:18 | Magura (Kalu Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-01-07 18:00:57 | Norwood (Kelani Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-01-07 18:07:46 | Ellagawa (Kalu Ganga) | 4.20 | 🟢 Normal | 0.000 |  |
| 2026-01-07 18:00:56 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-01-07 18:02:40 | Dunamale (Aththanagalu Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-01-07 18:02:08 | Thaldena (Mahaweli Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-01-07 18:04:01 | Katharagama (Menik Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-01-07 18:06:25 | Badalgama (Maha Oya) | 2.04 | 🟢 Normal | 0.000 |  |
| 2026-01-07 18:03:54 | Holombuwa (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-01-07 17:37:24 | Panadugama (Nilwala Ganga) | 2.50 | 🟢 Normal | -0.007 |  |
| 2026-01-07 18:09:01 | Padiyathalawa (Maduru Oya) | 1.22 | 🟢 Normal | -0.009 |  |
| 2026-01-07 18:05:50 | Horowpothana (Yan Oya) | 2.50 | 🟢 Normal | -0.009 |  |
| 2026-01-07 18:03:33 | Glencourse (Kelani Ganga) | 8.61 | 🟢 Normal | -0.010 |  |
| 2026-01-07 18:02:22 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.46 | 🟢 Normal | -0.010 |  |
| 2026-01-07 18:06:48 | Rathnapura (Kalu Ganga) | 0.74 | 🟢 Normal | -0.010 |  |
| 2026-01-07 18:01:19 | Kuda Oya (Kirindi Oya) | 1.37 | 🟢 Normal | -0.010 |  |
| 2026-01-07 18:01:44 | Yaka Wewa (Ma Oya) | 0.83 | 🟢 Normal | -0.010 |  |
| 2026-01-07 18:02:45 | Giriulla (Maha Oya) | 0.98 | 🟢 Normal | -0.011 |  |
| 2026-01-07 18:03:54 | Thanamalwila (Kirindi Oya) | 1.12 | 🟢 Normal | -0.011 |  |
| 2026-01-07 18:04:02 | Siyambalanduwa (Heda Oya) | 1.53 | 🟢 Normal | -0.019 |  |
| 2026-01-07 18:06:39 | Baddegama (Gin Ganga) | 1.18 | 🟢 Normal | -0.020 |  |
| 2026-01-07 18:00:11 | Nawalapitiya (Mahaweli Ganga) | 0.74 | 🟢 Normal | -0.020 |  |
| 2026-01-07 18:03:25 | Thanthirimale (Malwathu Oya) | 1.77 | 🟢 Normal | -0.023 |  |
| 2026-01-07 18:02:00 | Putupaula (Kalu Ganga) | 0.85 | 🟢 Normal | -0.031 |  |
| 2026-01-07 18:02:09 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | -0.033 |  |
| 2026-01-07 18:02:39 | Wellawaya (Kirindi Oya) | 1.05 | 🟢 Normal | -0.039 |  |
| 2026-01-07 18:08:59 | Manampitiya (Mahaweli Ganga) | 2.61 | 🟢 Normal | -0.041 |  |
| 2026-01-07 18:04:10 | Kithulgala (Kelani Ganga) | 1.65 | 🟢 Normal | -0.106 |  |
| 2026-01-07 18:02:57 | Deraniyagala (Kelani Ganga) | 0.22 | 🟢 Normal | -0.110 |  |

## River Water Level Charts by Station

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)