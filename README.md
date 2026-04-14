# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--14_16:19:13-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **124,977 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-14 16:19:13 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | -0.008 |  |
| 2026-04-14 16:18:59 | Rathnapura (Kalu Ganga) | 0.98 | 🟢 Normal | -0.008 |  |
| 2026-04-14 16:11:25 | Magura (Kalu Ganga) | 1.43 | 🟢 Normal | -0.010 |  |
| 2026-04-14 16:10:35 | Baddegama (Gin Ganga) | 1.02 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-04-14 16:09:45 | Thalgahagoda (Nilwala Ganga) | 0.42 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-04-14 16:09:03 | Norwood (Kelani Ganga) | 0.66 | 🟢 Normal | 0.084 | 🔺 Rising |
| 2026-04-14 16:08:17 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-04-14 16:08:16 | Panadugama (Nilwala Ganga) | 1.99 | 🟢 Normal | -0.007 |  |
| 2026-04-14 16:07:41 | Wellawaya (Kirindi Oya) | 0.89 | 🟢 Normal | -0.018 |  |
| 2026-04-14 16:07:18 | Putupaula (Kalu Ganga) | 0.92 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-04-14 16:06:20 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | -0.010 |  |
| 2026-04-14 16:05:54 | Ellagawa (Kalu Ganga) | 4.40 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-14 16:05:01 | Thanamalwila (Kirindi Oya) | 1.36 | 🟢 Normal | -0.060 |  |
| 2026-04-14 16:04:37 | Holombuwa (Kelani Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-04-14 16:04:31 | Thawalama (Gin Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-04-14 16:04:24 | Giriulla (Maha Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-04-14 16:03:49 | Badalgama (Maha Oya) | 2.04 | 🟢 Normal | 0.000 |  |
| 2026-04-14 16:03:32 | Peradeniya (Mahaweli Ganga) | 1.08 | 🟢 Normal | -0.020 |  |
| 2026-04-14 16:03:16 | Padiyathalawa (Maduru Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-04-14 16:03:06 | Glencourse (Kelani Ganga) | 8.49 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-04-14 16:03:03 | Pitabeddara (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-04-14 16:02:50 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-14 16:02:49 | Deraniyagala (Kelani Ganga) | 0.13 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-14 16:02:44 | Hanwella (Kelani Ganga) | 0.44 | 🟢 Normal | -0.010 |  |
| 2026-04-14 16:02:38 | Siyambalanduwa (Heda Oya) | 0.51 | 🟢 Normal | -0.010 |  |
| 2026-04-14 16:02:19 | Katharagama (Menik Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-04-14 16:02:06 | Galgamuwa (Mee Oya) | 0.28 | 🟢 Normal | -0.010 |  |
| 2026-04-14 16:01:17 | Nawalapitiya (Mahaweli Ganga) | 0.73 | 🟢 Normal | -0.020 |  |
| 2026-04-14 16:01:10 | Kuda Oya (Kirindi Oya) | 1.48 | 🟢 Normal | -0.010 |  |
| 2026-04-14 16:01:09 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-04-14 16:01:06 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.18 | 🟢 Normal | -0.062 |  |
| 2026-04-14 16:00:58 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | -0.010 |  |
| 2026-04-14 16:00:58 | Moragaswewa (Deduru Oya) | 0.96 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-04-14 16:00:51 | Thanthirimale (Malwathu Oya) | 3.93 | 🟢 Normal | -0.050 |  |
| 2026-04-14 16:00:44 | Nakkala (Kumbukkan Oya) | 0.74 | 🟢 Normal | -0.011 |  |
| 2026-04-14 16:00:23 | Manampitiya (Mahaweli Ganga) | 0.08 | 🟢 Normal | -0.010 |  |
| 2026-04-14 15:33:09 | Giriulla (Maha Oya) | 0.98 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-14 16:09:03 | Norwood (Kelani Ganga) | 0.66 | 🟢 Normal | 0.084 | 🔺 Rising |
| 2026-04-14 16:00:58 | Moragaswewa (Deduru Oya) | 0.96 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-04-14 16:09:45 | Thalgahagoda (Nilwala Ganga) | 0.42 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-04-14 15:00:22 | Weraganthota (Mahaweli Ganga) | -2.79 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-04-14 16:10:35 | Baddegama (Gin Ganga) | 1.02 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-04-14 16:07:18 | Putupaula (Kalu Ganga) | 0.92 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-04-14 16:03:06 | Glencourse (Kelani Ganga) | 8.49 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-04-14 16:05:54 | Ellagawa (Kalu Ganga) | 4.40 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-14 16:02:49 | Deraniyagala (Kelani Ganga) | 0.13 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-14 16:01:09 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-04-14 16:02:50 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-14 16:04:24 | Giriulla (Maha Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-04-14 15:03:10 | Horowpothana (Yan Oya) | 1.53 | 🟢 Normal | 0.000 |  |
| 2026-04-14 16:03:03 | Pitabeddara (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-04-14 16:03:16 | Padiyathalawa (Maduru Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-04-14 16:08:17 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-04-14 15:03:27 | Dunamale (Aththanagalu Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-04-14 16:02:19 | Katharagama (Menik Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-04-14 16:03:49 | Badalgama (Maha Oya) | 2.04 | 🟢 Normal | 0.000 |  |
| 2026-04-14 16:04:37 | Holombuwa (Kelani Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-04-14 16:04:31 | Thawalama (Gin Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-04-14 16:08:16 | Panadugama (Nilwala Ganga) | 1.99 | 🟢 Normal | -0.007 |  |
| 2026-04-14 16:18:59 | Rathnapura (Kalu Ganga) | 0.98 | 🟢 Normal | -0.008 |  |
| 2026-04-14 16:19:13 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | -0.008 |  |
| 2026-04-14 16:06:20 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | -0.010 |  |
| 2026-04-14 16:00:58 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | -0.010 |  |
| 2026-04-14 16:11:25 | Magura (Kalu Ganga) | 1.43 | 🟢 Normal | -0.010 |  |
| 2026-04-14 16:02:38 | Siyambalanduwa (Heda Oya) | 0.51 | 🟢 Normal | -0.010 |  |
| 2026-04-14 16:00:23 | Manampitiya (Mahaweli Ganga) | 0.08 | 🟢 Normal | -0.010 |  |
| 2026-04-14 16:02:44 | Hanwella (Kelani Ganga) | 0.44 | 🟢 Normal | -0.010 |  |
| 2026-04-14 16:01:10 | Kuda Oya (Kirindi Oya) | 1.48 | 🟢 Normal | -0.010 |  |
| 2026-04-14 16:02:06 | Galgamuwa (Mee Oya) | 0.28 | 🟢 Normal | -0.010 |  |
| 2026-04-14 16:00:44 | Nakkala (Kumbukkan Oya) | 0.74 | 🟢 Normal | -0.011 |  |
| 2026-04-14 16:07:41 | Wellawaya (Kirindi Oya) | 0.89 | 🟢 Normal | -0.018 |  |
| 2026-04-14 16:01:17 | Nawalapitiya (Mahaweli Ganga) | 0.73 | 🟢 Normal | -0.020 |  |
| 2026-04-14 16:03:32 | Peradeniya (Mahaweli Ganga) | 1.08 | 🟢 Normal | -0.020 |  |
| 2026-04-14 16:00:51 | Thanthirimale (Malwathu Oya) | 3.93 | 🟢 Normal | -0.050 |  |
| 2026-04-14 16:05:01 | Thanamalwila (Kirindi Oya) | 1.36 | 🟢 Normal | -0.060 |  |
| 2026-04-14 16:01:06 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.18 | 🟢 Normal | -0.062 |  |

## River Water Level Charts by Station

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)