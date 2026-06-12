# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--13_03:10:50-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **177,893 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-13 03:10:50 | Hanwella (Kelani Ganga) | 4.19 | 🟢 Normal | 0.084 | 🔺 Rising |
| 2026-06-13 03:09:35 | Putupaula (Kalu Ganga) | 2.29 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-06-13 03:09:13 | Holombuwa (Kelani Ganga) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-06-13 03:08:57 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.24 | 🟡 Alert | 0.000 |  |
| 2026-06-13 03:07:35 | Kithulgala (Kelani Ganga) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-06-13 03:07:06 | Glencourse (Kelani Ganga) | 12.18 | 🟢 Normal | -0.069 |  |
| 2026-06-13 03:07:02 | Thanamalwila (Kirindi Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-06-13 03:06:48 | Horowpothana (Yan Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-06-13 03:06:45 | Yaka Wewa (Ma Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-06-13 03:06:04 | Thaldena (Mahaweli Ganga) | 0.29 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2026-06-13 03:05:57 | Urawa (Nilwala Ganga) | 1.46 | 🟢 Normal | -0.086 |  |
| 2026-06-13 03:05:44 | Norwood (Kelani Ganga) | 1.36 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-13 03:05:28 | Giriulla (Maha Oya) | 2.30 | 🟢 Normal | 0.000 |  |
| 2026-06-13 03:05:18 | Thawalama (Gin Ganga) | 3.67 | 🟢 Normal | 0.000 |  |
| 2026-06-13 03:05:17 | Rathnapura (Kalu Ganga) | 6.26 | 🟡 Alert | -0.055 |  |
| 2026-06-13 03:04:57 | Ellagawa (Kalu Ganga) | 8.43 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-06-13 03:04:32 | Thalgahagoda (Nilwala Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-06-13 03:04:11 | Badalgama (Maha Oya) | 3.41 | 🟢 Normal | -0.011 |  |
| 2026-06-13 03:04:08 | Nawalapitiya (Mahaweli Ganga) | 1.90 | 🟢 Normal | -0.169 |  |
| 2026-06-13 03:03:57 | Deraniyagala (Kelani Ganga) | 1.39 | 🟢 Normal | -0.020 |  |
| 2026-06-13 03:03:53 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-06-13 03:03:53 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-06-13 03:03:50 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | -0.059 |  |
| 2026-06-13 03:03:31 | Katharagama (Menik Ganga) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-06-13 03:03:08 | Panadugama (Nilwala Ganga) | 4.82 | 🟢 Normal | 0.087 | 🔺 Rising |
| 2026-06-13 03:03:06 | Moraketiya (Walawe Ganga) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-06-13 03:03:03 | Baddegama (Gin Ganga) | 3.09 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-13 03:02:57 | Peradeniya (Mahaweli Ganga) | 2.51 | 🟢 Normal | -0.273 |  |
| 2026-06-13 03:02:43 | Magura (Kalu Ganga) | 4.72 | 🟡 Alert | 0.000 |  |
| 2026-06-13 03:02:38 | Padiyathalawa (Maduru Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-06-13 03:02:35 | Pitabeddara (Nilwala Ganga) | 2.20 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-06-13 03:02:35 | Padiyathalawa (Maduru Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-06-13 03:02:19 | Dunamale (Aththanagalu Oya) | 3.17 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-06-13 03:02:13 | Moragaswewa (Deduru Oya) | 0.66 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-13 03:01:25 | Moraketiya (Walawe Ganga) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-06-13 03:00:37 | Nakkala (Kumbukkan Oya) | 0.78 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-06-13 03:00:33 | Wellawaya (Kirindi Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-06-13 02:49:55 | Nawalapitiya (Mahaweli Ganga) | 1.94 | 🟢 Normal | -0.169 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-13 03:02:43 | Magura (Kalu Ganga) | 4.72 | 🟡 Alert | 0.000 |  |
| 2026-06-13 03:08:57 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.24 | 🟡 Alert | 0.000 |  |
| 2026-06-13 03:05:17 | Rathnapura (Kalu Ganga) | 6.26 | 🟡 Alert | -0.055 |  |
| 2026-06-13 03:03:08 | Panadugama (Nilwala Ganga) | 4.82 | 🟢 Normal | 0.087 | 🔺 Rising |
| 2026-06-13 03:10:50 | Hanwella (Kelani Ganga) | 4.19 | 🟢 Normal | 0.084 | 🔺 Rising |
| 2026-06-13 03:06:04 | Thaldena (Mahaweli Ganga) | 0.29 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2026-06-13 03:02:35 | Pitabeddara (Nilwala Ganga) | 2.20 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-06-13 03:02:19 | Dunamale (Aththanagalu Oya) | 3.17 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-06-13 03:03:53 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-06-13 03:04:57 | Ellagawa (Kalu Ganga) | 8.43 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-06-12 18:04:11 | Galgamuwa (Mee Oya) | 0.51 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-06-13 03:00:37 | Nakkala (Kumbukkan Oya) | 0.78 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-06-13 03:09:35 | Putupaula (Kalu Ganga) | 2.29 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-06-13 03:03:03 | Baddegama (Gin Ganga) | 3.09 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-13 03:02:13 | Moragaswewa (Deduru Oya) | 0.66 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-13 03:05:44 | Norwood (Kelani Ganga) | 1.36 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-13 03:07:35 | Kithulgala (Kelani Ganga) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-06-12 18:02:22 | Weraganthota (Mahaweli Ganga) | -3.36 | 🟢 Normal | 0.000 |  |
| 2026-06-13 03:00:33 | Wellawaya (Kirindi Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-06-13 03:06:45 | Yaka Wewa (Ma Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-06-13 03:05:28 | Giriulla (Maha Oya) | 2.30 | 🟢 Normal | 0.000 |  |
| 2026-06-13 03:06:48 | Horowpothana (Yan Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-06-13 03:02:38 | Padiyathalawa (Maduru Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-06-13 03:03:06 | Moraketiya (Walawe Ganga) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-06-13 03:03:53 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-06-13 03:03:31 | Katharagama (Menik Ganga) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-06-13 03:09:13 | Holombuwa (Kelani Ganga) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-06-12 19:19:51 | Thanthirimale (Malwathu Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-06-13 03:05:18 | Thawalama (Gin Ganga) | 3.67 | 🟢 Normal | 0.000 |  |
| 2026-06-13 03:04:32 | Thalgahagoda (Nilwala Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-06-13 00:01:19 | Kuda Oya (Kirindi Oya) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-06-13 03:07:02 | Thanamalwila (Kirindi Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-06-13 03:04:11 | Badalgama (Maha Oya) | 3.41 | 🟢 Normal | -0.011 |  |
| 2026-06-13 03:03:57 | Deraniyagala (Kelani Ganga) | 1.39 | 🟢 Normal | -0.020 |  |
| 2026-06-13 03:03:50 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | -0.059 |  |
| 2026-06-13 03:07:06 | Glencourse (Kelani Ganga) | 12.18 | 🟢 Normal | -0.069 |  |
| 2026-06-13 03:05:57 | Urawa (Nilwala Ganga) | 1.46 | 🟢 Normal | -0.086 |  |
| 2026-06-13 03:04:08 | Nawalapitiya (Mahaweli Ganga) | 1.90 | 🟢 Normal | -0.169 |  |
| 2026-06-13 03:02:57 | Peradeniya (Mahaweli Ganga) | 2.51 | 🟢 Normal | -0.273 |  |

## River Water Level Charts by Station

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)