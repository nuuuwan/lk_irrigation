# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--29_00:07:00-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **164,348 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **30** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-29 00:07:00 | Kithulgala (Kelani Ganga) | 1.98 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-29 00:06:04 | Glencourse (Kelani Ganga) | 11.84 | 🟢 Normal | 0.093 | 🔺 Rising |
| 2026-05-29 00:06:00 | Rathnapura (Kalu Ganga) | 5.41 | 🟡 Alert | 0.032 | 🔺 Rising |
| 2026-05-29 00:05:57 | Thanamalwila (Kirindi Oya) | 0.68 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-05-29 00:05:44 | Pitabeddara (Nilwala Ganga) | 2.82 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-05-29 00:05:44 | Thawalama (Gin Ganga) | 3.35 | 🟢 Normal | -0.083 |  |
| 2026-05-29 00:05:39 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-05-29 00:05:28 | Baddegama (Gin Ganga) | 3.09 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-05-29 00:04:14 | Badalgama (Maha Oya) | 2.35 | 🟢 Normal | 0.000 |  |
| 2026-05-29 00:04:11 | Norwood (Kelani Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-05-29 00:03:45 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-29 00:03:37 | Hanwella (Kelani Ganga) | 3.76 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-05-29 00:03:16 | Putupaula (Kalu Ganga) | 2.59 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-29 00:03:13 | Thaldena (Mahaweli Ganga) | 0.47 | 🟢 Normal | -0.011 |  |
| 2026-05-29 00:02:53 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-05-29 00:02:50 | Ellagawa (Kalu Ganga) | 8.52 | 🟢 Normal | -0.020 |  |
| 2026-05-29 00:02:42 | Giriulla (Maha Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-05-29 00:02:37 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-05-29 00:02:36 | Kuda Oya (Kirindi Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-05-29 00:02:17 | Urawa (Nilwala Ganga) | 1.30 | 🟢 Normal | -0.226 |  |
| 2026-05-29 00:02:10 | Magura (Kalu Ganga) | 4.92 | 🟡 Alert | -0.032 |  |
| 2026-05-29 00:02:09 | Padiyathalawa (Maduru Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-05-29 00:01:59 | Moragaswewa (Deduru Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-05-29 00:01:58 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-29 00:01:48 | Peradeniya (Mahaweli Ganga) | 2.15 | 🟢 Normal | 0.130 | 🔺 Rising |
| 2026-05-29 00:01:31 | Deraniyagala (Kelani Ganga) | 2.45 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-05-29 00:00:58 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-29 00:00:33 | Wellawaya (Kirindi Oya) | 1.18 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-28 23:16:39 | Padiyathalawa (Maduru Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-05-28 23:16:38 | Padiyathalawa (Maduru Oya) | 0.09 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-28 21:06:25 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.38 | 🟡 Alert | 0.065 | 🔺 Rising |
| 2026-05-29 00:06:00 | Rathnapura (Kalu Ganga) | 5.41 | 🟡 Alert | 0.032 | 🔺 Rising |
| 2026-05-29 00:02:10 | Magura (Kalu Ganga) | 4.92 | 🟡 Alert | -0.032 |  |
| 2026-05-29 00:01:48 | Peradeniya (Mahaweli Ganga) | 2.15 | 🟢 Normal | 0.130 | 🔺 Rising |
| 2026-05-29 00:06:04 | Glencourse (Kelani Ganga) | 11.84 | 🟢 Normal | 0.093 | 🔺 Rising |
| 2026-05-28 23:09:42 | Panadugama (Nilwala Ganga) | 4.97 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-05-28 23:04:05 | Nawalapitiya (Mahaweli Ganga) | 2.38 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2026-05-29 00:01:31 | Deraniyagala (Kelani Ganga) | 2.45 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-05-28 23:09:16 | Thalgahagoda (Nilwala Ganga) | 0.68 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-05-28 23:01:48 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-05-28 23:02:08 | Manampitiya (Mahaweli Ganga) | -0.05 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-29 00:00:33 | Wellawaya (Kirindi Oya) | 1.18 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-29 00:05:28 | Baddegama (Gin Ganga) | 3.09 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-05-29 00:05:44 | Pitabeddara (Nilwala Ganga) | 2.82 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-05-28 23:05:36 | Holombuwa (Kelani Ganga) | 1.10 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-05-29 00:03:37 | Hanwella (Kelani Ganga) | 3.76 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-05-29 00:07:00 | Kithulgala (Kelani Ganga) | 1.98 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-29 00:05:57 | Thanamalwila (Kirindi Oya) | 0.68 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-05-29 00:03:45 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-29 00:03:16 | Putupaula (Kalu Ganga) | 2.59 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-29 00:01:58 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-29 00:01:59 | Moragaswewa (Deduru Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-05-29 00:02:53 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-05-29 00:02:42 | Giriulla (Maha Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-05-29 00:05:39 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-05-28 18:03:10 | Galgamuwa (Mee Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-05-29 00:04:11 | Norwood (Kelani Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-05-29 00:02:09 | Padiyathalawa (Maduru Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-05-28 23:01:35 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-05-29 00:02:37 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-05-29 00:04:14 | Badalgama (Maha Oya) | 2.35 | 🟢 Normal | 0.000 |  |
| 2026-05-28 18:02:12 | Thanthirimale (Malwathu Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-05-29 00:02:36 | Kuda Oya (Kirindi Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-05-29 00:03:13 | Thaldena (Mahaweli Ganga) | 0.47 | 🟢 Normal | -0.011 |  |
| 2026-05-28 18:32:56 | Weraganthota (Mahaweli Ganga) | -3.27 | 🟢 Normal | -0.013 |  |
| 2026-05-29 00:02:50 | Ellagawa (Kalu Ganga) | 8.52 | 🟢 Normal | -0.020 |  |
| 2026-05-28 23:03:04 | Dunamale (Aththanagalu Oya) | 1.82 | 🟢 Normal | -0.030 |  |
| 2026-05-29 00:05:44 | Thawalama (Gin Ganga) | 3.35 | 🟢 Normal | -0.083 |  |
| 2026-05-29 00:02:17 | Urawa (Nilwala Ganga) | 1.30 | 🟢 Normal | -0.226 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)