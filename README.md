# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--28_01:20:40-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **163,492 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **28** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-28 01:20:40 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-05-28 01:18:05 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-05-28 01:17:27 | Rathnapura (Kalu Ganga) | 4.93 | 🟢 Normal | -0.009 |  |
| 2026-05-28 01:08:08 | Holombuwa (Kelani Ganga) | 0.60 | 🟢 Normal | -0.038 |  |
| 2026-05-28 01:07:57 | Dunamale (Aththanagalu Oya) | 2.32 | 🟢 Normal | -0.037 |  |
| 2026-05-28 01:07:48 | Glencourse (Kelani Ganga) | 12.55 | 🟢 Normal | 0.000 |  |
| 2026-05-28 01:07:37 | Baddegama (Gin Ganga) | 2.37 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-05-28 01:07:21 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | -0.030 |  |
| 2026-05-28 01:05:52 | Wellawaya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-05-28 01:05:36 | Kuda Oya (Kirindi Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-05-28 01:03:56 | Hanwella (Kelani Ganga) | 4.48 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-05-28 01:03:50 | Badalgama (Maha Oya) | 2.44 | 🟢 Normal | 0.000 |  |
| 2026-05-28 01:03:45 | Thawalama (Gin Ganga) | 3.40 | 🟢 Normal | 0.130 | 🔺 Rising |
| 2026-05-28 01:03:26 | Moraketiya (Walawe Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-05-28 01:03:20 | Thaldena (Mahaweli Ganga) | 0.40 | 🟢 Normal | 0.107 | 🔺 Rising |
| 2026-05-28 01:03:16 | Kithulgala (Kelani Ganga) | 1.93 | 🟢 Normal | -0.031 |  |
| 2026-05-28 01:03:11 | Peradeniya (Mahaweli Ganga) | 2.08 | 🟢 Normal | -0.030 |  |
| 2026-05-28 01:03:10 | Giriulla (Maha Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-05-28 01:03:00 | Thanamalwila (Kirindi Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-05-28 01:02:53 | Norwood (Kelani Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-05-28 01:02:42 | Urawa (Nilwala Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-05-28 01:02:37 | Deraniyagala (Kelani Ganga) | 1.97 | 🟢 Normal | -0.131 |  |
| 2026-05-28 01:02:26 | Moragaswewa (Deduru Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-05-28 01:02:21 | Padiyathalawa (Maduru Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-05-28 01:02:13 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-05-28 01:01:48 | Ellagawa (Kalu Ganga) | 8.56 | 🟢 Normal | 0.000 |  |
| 2026-05-28 01:01:19 | Nawalapitiya (Mahaweli Ganga) | 1.83 | 🟢 Normal | -0.021 |  |
| 2026-05-28 01:00:49 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-28 00:01:15 | Magura (Kalu Ganga) | 4.65 | 🟡 Alert | 0.148 | 🔺 Rising |
| 2026-05-28 00:10:51 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.50 | 🟡 Alert | 0.015 | 🔺 Rising |
| 2026-05-28 00:02:23 | Nakkala (Kumbukkan Oya) | 0.88 | 🟢 Normal | 0.206 | 🔺 Rising |
| 2026-05-28 01:03:45 | Thawalama (Gin Ganga) | 3.40 | 🟢 Normal | 0.130 | 🔺 Rising |
| 2026-05-28 01:03:20 | Thaldena (Mahaweli Ganga) | 0.40 | 🟢 Normal | 0.107 | 🔺 Rising |
| 2026-05-28 01:03:56 | Hanwella (Kelani Ganga) | 4.48 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-05-27 18:00:23 | Thanthirimale (Malwathu Oya) | 1.18 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-05-28 01:07:37 | Baddegama (Gin Ganga) | 2.37 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-05-28 00:07:50 | Panadugama (Nilwala Ganga) | 2.80 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-05-28 00:02:26 | Manampitiya (Mahaweli Ganga) | -0.08 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-28 01:05:52 | Wellawaya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-05-28 01:02:26 | Moragaswewa (Deduru Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-05-28 00:01:21 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-05-28 01:03:10 | Giriulla (Maha Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-05-28 01:18:05 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-05-27 18:02:35 | Galgamuwa (Mee Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-05-28 00:06:13 | Pitabeddara (Nilwala Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-05-28 01:02:53 | Norwood (Kelani Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-05-28 01:01:48 | Ellagawa (Kalu Ganga) | 8.56 | 🟢 Normal | 0.000 |  |
| 2026-05-28 01:02:21 | Padiyathalawa (Maduru Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-05-28 01:07:48 | Glencourse (Kelani Ganga) | 12.55 | 🟢 Normal | 0.000 |  |
| 2026-05-28 01:03:26 | Moraketiya (Walawe Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-05-28 01:20:40 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-05-28 01:02:13 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-05-28 00:20:09 | Putupaula (Kalu Ganga) | 2.45 | 🟢 Normal | 0.000 |  |
| 2026-05-28 01:03:50 | Badalgama (Maha Oya) | 2.44 | 🟢 Normal | 0.000 |  |
| 2026-05-28 01:02:42 | Urawa (Nilwala Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-05-28 01:00:49 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-05-28 01:05:36 | Kuda Oya (Kirindi Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-05-28 01:03:00 | Thanamalwila (Kirindi Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-05-28 01:17:27 | Rathnapura (Kalu Ganga) | 4.93 | 🟢 Normal | -0.009 |  |
| 2026-05-27 18:05:39 | Weraganthota (Mahaweli Ganga) | -3.28 | 🟢 Normal | -0.009 |  |
| 2026-05-28 01:01:19 | Nawalapitiya (Mahaweli Ganga) | 1.83 | 🟢 Normal | -0.021 |  |
| 2026-05-28 01:03:11 | Peradeniya (Mahaweli Ganga) | 2.08 | 🟢 Normal | -0.030 |  |
| 2026-05-28 01:07:21 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | -0.030 |  |
| 2026-05-28 01:03:16 | Kithulgala (Kelani Ganga) | 1.93 | 🟢 Normal | -0.031 |  |
| 2026-05-28 01:07:57 | Dunamale (Aththanagalu Oya) | 2.32 | 🟢 Normal | -0.037 |  |
| 2026-05-28 01:08:08 | Holombuwa (Kelani Ganga) | 0.60 | 🟢 Normal | -0.038 |  |
| 2026-05-28 01:02:37 | Deraniyagala (Kelani Ganga) | 1.97 | 🟢 Normal | -0.131 |  |

## River Water Level Charts by Station

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

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

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

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

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)