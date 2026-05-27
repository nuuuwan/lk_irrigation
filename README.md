# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--27_23:25:36-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **163,427 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-27 23:25:36 | Rathnapura (Kalu Ganga) | 4.88 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2026-05-27 23:20:47 | Urawa (Nilwala Ganga) | 0.19 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-05-27 23:16:31 | Panadugama (Nilwala Ganga) | 2.78 | 🟢 Normal | 0.000 |  |
| 2026-05-27 23:10:37 | Hanwella (Kelani Ganga) | 4.30 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-05-27 23:10:33 | Wellawaya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-05-27 23:08:48 | Putupaula (Kalu Ganga) | 2.45 | 🟢 Normal | 0.000 |  |
| 2026-05-27 23:08:06 | Holombuwa (Kelani Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-05-27 23:07:15 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-05-27 23:06:50 | Kithulgala (Kelani Ganga) | 1.97 | 🟢 Normal | -0.120 |  |
| 2026-05-27 23:06:38 | Baddegama (Gin Ganga) | 2.30 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-05-27 23:06:18 | Panadugama (Nilwala Ganga) | 2.78 | 🟢 Normal | 0.000 |  |
| 2026-05-27 23:05:23 | Badalgama (Maha Oya) | 2.45 | 🟢 Normal | 0.000 |  |
| 2026-05-27 23:04:57 | Thawalama (Gin Ganga) | 3.18 | 🟢 Normal | 0.127 | 🔺 Rising |
| 2026-05-27 23:04:34 | Thanamalwila (Kirindi Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-05-27 23:04:29 | Magura (Kalu Ganga) | 4.51 | 🟡 Alert | 0.208 | 🔺 Rising |
| 2026-05-27 23:04:20 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-05-27 23:03:56 | Giriulla (Maha Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-05-27 23:03:48 | Panadugama (Nilwala Ganga) | 2.78 | 🟢 Normal | 0.000 |  |
| 2026-05-27 23:03:34 | Norwood (Kelani Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-05-27 23:03:28 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-05-27 23:03:15 | Thaldena (Mahaweli Ganga) | 0.28 | 🟢 Normal | -0.010 |  |
| 2026-05-27 23:03:00 | Dunamale (Aththanagalu Oya) | 2.39 | 🟢 Normal | -0.021 |  |
| 2026-05-27 23:02:56 | Deraniyagala (Kelani Ganga) | 2.25 | 🟢 Normal | -0.181 |  |
| 2026-05-27 23:02:10 | Kuda Oya (Kirindi Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-05-27 23:02:06 | Peradeniya (Mahaweli Ganga) | 2.05 | 🟢 Normal | 0.148 | 🔺 Rising |
| 2026-05-27 23:02:05 | Ellagawa (Kalu Ganga) | 8.58 | 🟢 Normal | 0.000 |  |
| 2026-05-27 23:01:23 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-05-27 23:01:21 | Padiyathalawa (Maduru Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-05-27 23:01:19 | Nakkala (Kumbukkan Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-05-27 23:01:11 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-05-27 23:01:10 | Moraketiya (Walawe Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-05-27 23:01:09 | Nawalapitiya (Mahaweli Ganga) | 2.03 | 🟢 Normal | -0.021 |  |
| 2026-05-27 23:00:58 | Glencourse (Kelani Ganga) | 12.49 | 🟢 Normal | 0.141 | 🔺 Rising |
| 2026-05-27 23:00:31 | Pitabeddara (Nilwala Ganga) | 0.78 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-27 23:04:29 | Magura (Kalu Ganga) | 4.51 | 🟡 Alert | 0.208 | 🔺 Rising |
| 2026-05-27 22:08:28 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.47 | 🟡 Alert | 0.018 | 🔺 Rising |
| 2026-05-27 23:02:06 | Peradeniya (Mahaweli Ganga) | 2.05 | 🟢 Normal | 0.148 | 🔺 Rising |
| 2026-05-27 23:00:58 | Glencourse (Kelani Ganga) | 12.49 | 🟢 Normal | 0.141 | 🔺 Rising |
| 2026-05-27 23:04:57 | Thawalama (Gin Ganga) | 3.18 | 🟢 Normal | 0.127 | 🔺 Rising |
| 2026-05-27 23:25:36 | Rathnapura (Kalu Ganga) | 4.88 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2026-05-27 23:10:37 | Hanwella (Kelani Ganga) | 4.30 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-05-27 18:00:23 | Thanthirimale (Malwathu Oya) | 1.18 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-05-27 22:04:02 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-05-27 23:06:38 | Baddegama (Gin Ganga) | 2.30 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-05-27 23:20:47 | Urawa (Nilwala Ganga) | 0.19 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-05-27 23:10:33 | Wellawaya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-05-27 23:01:19 | Nakkala (Kumbukkan Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-05-27 22:03:59 | Moragaswewa (Deduru Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-05-27 23:01:23 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-05-27 23:03:56 | Giriulla (Maha Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-05-27 23:03:28 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-05-27 18:02:35 | Galgamuwa (Mee Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-05-27 23:00:31 | Pitabeddara (Nilwala Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-05-27 23:03:34 | Norwood (Kelani Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-05-27 23:02:05 | Ellagawa (Kalu Ganga) | 8.58 | 🟢 Normal | 0.000 |  |
| 2026-05-27 23:16:31 | Panadugama (Nilwala Ganga) | 2.78 | 🟢 Normal | 0.000 |  |
| 2026-05-27 23:01:21 | Padiyathalawa (Maduru Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-05-27 23:01:10 | Moraketiya (Walawe Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-05-27 23:04:20 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-05-27 23:07:15 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-05-27 23:08:48 | Putupaula (Kalu Ganga) | 2.45 | 🟢 Normal | 0.000 |  |
| 2026-05-27 23:05:23 | Badalgama (Maha Oya) | 2.45 | 🟢 Normal | 0.000 |  |
| 2026-05-27 23:08:06 | Holombuwa (Kelani Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-05-27 23:01:11 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-05-27 23:02:10 | Kuda Oya (Kirindi Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-05-27 23:04:34 | Thanamalwila (Kirindi Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-05-27 18:05:39 | Weraganthota (Mahaweli Ganga) | -3.28 | 🟢 Normal | -0.009 |  |
| 2026-05-27 23:03:15 | Thaldena (Mahaweli Ganga) | 0.28 | 🟢 Normal | -0.010 |  |
| 2026-05-27 23:01:09 | Nawalapitiya (Mahaweli Ganga) | 2.03 | 🟢 Normal | -0.021 |  |
| 2026-05-27 23:03:00 | Dunamale (Aththanagalu Oya) | 2.39 | 🟢 Normal | -0.021 |  |
| 2026-05-27 21:04:16 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | -0.029 |  |
| 2026-05-27 23:06:50 | Kithulgala (Kelani Ganga) | 1.97 | 🟢 Normal | -0.120 |  |
| 2026-05-27 23:02:56 | Deraniyagala (Kelani Ganga) | 2.25 | 🟢 Normal | -0.181 |  |

## River Water Level Charts by Station

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

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

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

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

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)