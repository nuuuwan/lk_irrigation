# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--29_12:10:51-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **219,383 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-29 12:10:51 | Baddegama (Gin Ganga) | 1.28 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-07-29 12:09:54 | Holombuwa (Kelani Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-07-29 12:07:53 | Glencourse (Kelani Ganga) | 8.98 | 🟢 Normal | -0.020 |  |
| 2026-07-29 12:07:48 | Ellagawa (Kalu Ganga) | 4.61 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-07-29 12:07:44 | Urawa (Nilwala Ganga) | -0.06 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-07-29 12:07:09 | Panadugama (Nilwala Ganga) | 1.98 | 🟢 Normal | 0.000 |  |
| 2026-07-29 12:06:57 | Kuda Oya (Kirindi Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-07-29 12:06:52 | Wellawaya (Kirindi Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-07-29 12:06:12 | Deraniyagala (Kelani Ganga) | 0.44 | 🟢 Normal | -0.040 |  |
| 2026-07-29 12:06:10 | Peradeniya (Mahaweli Ganga) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-07-29 12:05:39 | Thalgahagoda (Nilwala Ganga) | 0.12 | 🟢 Normal | -0.031 |  |
| 2026-07-29 12:04:48 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.30 | 🟢 Normal | 0.108 | 🔺 Rising |
| 2026-07-29 12:04:47 | Thawalama (Gin Ganga) | 1.35 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-07-29 12:03:54 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-29 12:03:49 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-07-29 12:03:46 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-07-29 12:03:40 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.128 | 🔺 Rising |
| 2026-07-29 12:03:33 | Giriulla (Maha Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-07-29 12:03:26 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-07-29 12:03:19 | Hanwella (Kelani Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-07-29 12:03:06 | Nawalapitiya (Mahaweli Ganga) | 1.26 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-07-29 12:03:00 | Norwood (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-07-29 12:02:55 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-07-29 12:02:54 | Dunamale (Aththanagalu Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-07-29 12:02:48 | Thaldena (Mahaweli Ganga) | 0.09 | 🟢 Normal | -0.010 |  |
| 2026-07-29 12:02:21 | Thanamalwila (Kirindi Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-07-29 12:02:12 | Putupaula (Kalu Ganga) | 0.50 | 🟢 Normal | 0.191 | 🔺 Rising |
| 2026-07-29 12:01:51 | Magura (Kalu Ganga) | 1.22 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-07-29 12:01:49 | Weraganthota (Mahaweli Ganga) | -3.19 | 🟢 Normal | -0.010 |  |
| 2026-07-29 12:01:45 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-07-29 12:01:42 | Galgamuwa (Mee Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-29 12:01:30 | Rathnapura (Kalu Ganga) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-07-29 12:01:25 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-07-29 12:01:15 | Thanthirimale (Malwathu Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-07-29 12:01:05 | Moraketiya (Walawe Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-07-29 12:00:45 | Pitabeddara (Nilwala Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-07-29 12:00:40 | Manampitiya (Mahaweli Ganga) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-07-29 12:00:32 | Siyambalanduwa (Heda Oya) | 0.18 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-29 12:02:12 | Putupaula (Kalu Ganga) | 0.50 | 🟢 Normal | 0.191 | 🔺 Rising |
| 2026-07-29 12:03:40 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.128 | 🔺 Rising |
| 2026-07-29 12:04:48 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.30 | 🟢 Normal | 0.108 | 🔺 Rising |
| 2026-07-29 12:01:51 | Magura (Kalu Ganga) | 1.22 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-07-29 12:03:06 | Nawalapitiya (Mahaweli Ganga) | 1.26 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-07-29 12:04:47 | Thawalama (Gin Ganga) | 1.35 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-07-29 12:07:48 | Ellagawa (Kalu Ganga) | 4.61 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-07-29 12:03:46 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-07-29 12:07:44 | Urawa (Nilwala Ganga) | -0.06 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-07-29 12:10:51 | Baddegama (Gin Ganga) | 1.28 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-07-29 12:06:52 | Wellawaya (Kirindi Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-07-29 12:03:26 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-07-29 12:01:45 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-07-29 12:01:25 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-07-29 12:03:33 | Giriulla (Maha Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-07-29 11:10:09 | Horowpothana (Yan Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-07-29 12:01:42 | Galgamuwa (Mee Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-29 12:00:45 | Pitabeddara (Nilwala Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-07-29 12:03:00 | Norwood (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-07-29 12:03:19 | Hanwella (Kelani Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-07-29 12:07:09 | Panadugama (Nilwala Ganga) | 1.98 | 🟢 Normal | 0.000 |  |
| 2026-07-29 12:03:54 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-29 12:01:05 | Moraketiya (Walawe Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-07-29 12:00:32 | Siyambalanduwa (Heda Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-07-29 12:02:54 | Dunamale (Aththanagalu Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-07-29 12:02:55 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-07-29 12:03:49 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-07-29 12:09:54 | Holombuwa (Kelani Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-07-29 12:00:40 | Manampitiya (Mahaweli Ganga) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-07-29 12:01:30 | Rathnapura (Kalu Ganga) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-07-29 12:01:15 | Thanthirimale (Malwathu Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-07-29 12:06:10 | Peradeniya (Mahaweli Ganga) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-07-29 12:06:57 | Kuda Oya (Kirindi Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-07-29 12:02:21 | Thanamalwila (Kirindi Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-07-29 12:02:48 | Thaldena (Mahaweli Ganga) | 0.09 | 🟢 Normal | -0.010 |  |
| 2026-07-29 12:01:49 | Weraganthota (Mahaweli Ganga) | -3.19 | 🟢 Normal | -0.010 |  |
| 2026-07-29 12:07:53 | Glencourse (Kelani Ganga) | 8.98 | 🟢 Normal | -0.020 |  |
| 2026-07-29 12:05:39 | Thalgahagoda (Nilwala Ganga) | 0.12 | 🟢 Normal | -0.031 |  |
| 2026-07-29 12:06:12 | Deraniyagala (Kelani Ganga) | 0.44 | 🟢 Normal | -0.040 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

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

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

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

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)