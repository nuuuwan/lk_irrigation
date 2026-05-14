# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--14_17:15:46-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **151,764 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-14 17:15:46 | Magura (Kalu Ganga) | 4.95 | 🟡 Alert | 0.035 | 🔺 Rising |
| 2026-05-14 17:15:03 | Thaldena (Mahaweli Ganga) | 0.57 | 🟢 Normal | -0.008 |  |
| 2026-05-14 17:13:39 | Yaka Wewa (Ma Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-05-14 17:08:15 | Moragaswewa (Deduru Oya) | 1.35 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-05-14 17:08:13 | Kithulgala (Kelani Ganga) | 2.18 | 🟢 Normal | 0.251 | 🔺 Rising |
| 2026-05-14 17:06:35 | Holombuwa (Kelani Ganga) | 1.71 | 🟢 Normal | 0.300 | 🔺 Rising |
| 2026-05-14 17:06:16 | Rathnapura (Kalu Ganga) | 4.75 | 🟢 Normal | 1.312 | 🔺 Rising |
| 2026-05-14 17:06:05 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.090 |  |
| 2026-05-14 17:05:42 | Badalgama (Maha Oya) | 3.38 | 🟢 Normal | 0.268 | 🔺 Rising |
| 2026-05-14 17:05:29 | Urawa (Nilwala Ganga) | 0.39 | 🟢 Normal | -0.015 |  |
| 2026-05-14 17:04:24 | Katharagama (Menik Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-05-14 17:04:14 | Dunamale (Aththanagalu Oya) | 3.30 | 🟡 Alert | 0.254 | 🔺 Rising |
| 2026-05-14 17:04:11 | Hanwella (Kelani Ganga) | 2.82 | 🟢 Normal | 0.300 | 🔺 Rising |
| 2026-05-14 17:04:00 | Glencourse (Kelani Ganga) | 12.02 | 🟢 Normal | 0.577 | 🔺 Rising |
| 2026-05-14 17:03:58 | Galgamuwa (Mee Oya) | 1.49 | 🟢 Normal | -0.186 |  |
| 2026-05-14 17:03:49 | Pitabeddara (Nilwala Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-05-14 17:03:27 | Baddegama (Gin Ganga) | 3.14 | 🟢 Normal | -0.010 |  |
| 2026-05-14 17:03:26 | Nawalapitiya (Mahaweli Ganga) | 2.01 | 🟢 Normal | 0.234 | 🔺 Rising |
| 2026-05-14 17:03:26 | Ellagawa (Kalu Ganga) | 8.34 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-05-14 17:03:21 | Panadugama (Nilwala Ganga) | 3.88 | 🟢 Normal | -0.032 |  |
| 2026-05-14 17:02:44 | Putupaula (Kalu Ganga) | 2.62 | 🟢 Normal | -0.010 |  |
| 2026-05-14 17:02:25 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.50 | 🟠 Minor Flood | 0.040 | 🔺 Rising |
| 2026-05-14 17:02:24 | Siyambalanduwa (Heda Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-05-14 17:02:17 | Thawalama (Gin Ganga) | 2.28 | 🟢 Normal | 0.162 | 🔺 Rising |
| 2026-05-14 17:02:12 | Padiyathalawa (Maduru Oya) | 0.29 | 🟢 Normal | -0.010 |  |
| 2026-05-14 17:02:11 | Nakkala (Kumbukkan Oya) | 0.99 | 🟢 Normal | -0.010 |  |
| 2026-05-14 17:02:08 | Thanamalwila (Kirindi Oya) | 1.46 | 🟢 Normal | 0.000 |  |
| 2026-05-14 17:02:03 | Peradeniya (Mahaweli Ganga) | 2.10 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-05-14 17:02:01 | Kuda Oya (Kirindi Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-05-14 17:01:59 | Norwood (Kelani Ganga) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-05-14 17:01:57 | Weraganthota (Mahaweli Ganga) | -3.08 | 🟢 Normal | 0.000 |  |
| 2026-05-14 17:01:50 | Giriulla (Maha Oya) | 3.04 | 🟢 Normal | 0.136 | 🔺 Rising |
| 2026-05-14 17:01:25 | Manampitiya (Mahaweli Ganga) | 0.57 | 🟢 Normal | -0.010 |  |
| 2026-05-14 17:01:05 | Moraketiya (Walawe Ganga) | 1.17 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-14 17:00:55 | Thanthirimale (Malwathu Oya) | 3.25 | 🟢 Normal | 0.000 |  |
| 2026-05-14 17:00:28 | Wellawaya (Kirindi Oya) | 1.32 | 🟢 Normal | -0.030 |  |
| 2026-05-14 17:00:06 | Horowpothana (Yan Oya) | 2.54 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-05-14 16:59:25 | Thalgahagoda (Nilwala Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-05-14 16:58:57 | Rathnapura (Kalu Ganga) | 4.59 | 🟢 Normal | 1.312 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-14 17:02:25 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.50 | 🟠 Minor Flood | 0.040 | 🔺 Rising |
| 2026-05-14 17:04:14 | Dunamale (Aththanagalu Oya) | 3.30 | 🟡 Alert | 0.254 | 🔺 Rising |
| 2026-05-14 17:15:46 | Magura (Kalu Ganga) | 4.95 | 🟡 Alert | 0.035 | 🔺 Rising |
| 2026-05-14 17:06:16 | Rathnapura (Kalu Ganga) | 4.75 | 🟢 Normal | 1.312 | 🔺 Rising |
| 2026-05-14 17:04:00 | Glencourse (Kelani Ganga) | 12.02 | 🟢 Normal | 0.577 | 🔺 Rising |
| 2026-05-14 17:06:35 | Holombuwa (Kelani Ganga) | 1.71 | 🟢 Normal | 0.300 | 🔺 Rising |
| 2026-05-14 17:04:11 | Hanwella (Kelani Ganga) | 2.82 | 🟢 Normal | 0.300 | 🔺 Rising |
| 2026-05-14 17:05:42 | Badalgama (Maha Oya) | 3.38 | 🟢 Normal | 0.268 | 🔺 Rising |
| 2026-05-14 16:04:04 | Deraniyagala (Kelani Ganga) | 3.81 | 🟢 Normal | 0.252 | 🔺 Rising |
| 2026-05-14 17:08:13 | Kithulgala (Kelani Ganga) | 2.18 | 🟢 Normal | 0.251 | 🔺 Rising |
| 2026-05-14 17:03:26 | Nawalapitiya (Mahaweli Ganga) | 2.01 | 🟢 Normal | 0.234 | 🔺 Rising |
| 2026-05-14 17:02:17 | Thawalama (Gin Ganga) | 2.28 | 🟢 Normal | 0.162 | 🔺 Rising |
| 2026-05-14 17:01:50 | Giriulla (Maha Oya) | 3.04 | 🟢 Normal | 0.136 | 🔺 Rising |
| 2026-05-14 17:03:26 | Ellagawa (Kalu Ganga) | 8.34 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-05-14 17:00:06 | Horowpothana (Yan Oya) | 2.54 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-05-14 17:02:03 | Peradeniya (Mahaweli Ganga) | 2.10 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-05-14 17:01:05 | Moraketiya (Walawe Ganga) | 1.17 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-14 17:08:15 | Moragaswewa (Deduru Oya) | 1.35 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-05-14 17:01:57 | Weraganthota (Mahaweli Ganga) | -3.08 | 🟢 Normal | 0.000 |  |
| 2026-05-14 17:13:39 | Yaka Wewa (Ma Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-05-14 17:03:49 | Pitabeddara (Nilwala Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-05-14 17:01:59 | Norwood (Kelani Ganga) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-05-14 17:02:24 | Siyambalanduwa (Heda Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-05-14 17:04:24 | Katharagama (Menik Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-05-14 17:00:55 | Thanthirimale (Malwathu Oya) | 3.25 | 🟢 Normal | 0.000 |  |
| 2026-05-14 16:59:25 | Thalgahagoda (Nilwala Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-05-14 17:02:01 | Kuda Oya (Kirindi Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-05-14 17:02:08 | Thanamalwila (Kirindi Oya) | 1.46 | 🟢 Normal | 0.000 |  |
| 2026-05-14 17:15:03 | Thaldena (Mahaweli Ganga) | 0.57 | 🟢 Normal | -0.008 |  |
| 2026-05-14 17:02:12 | Padiyathalawa (Maduru Oya) | 0.29 | 🟢 Normal | -0.010 |  |
| 2026-05-14 17:02:11 | Nakkala (Kumbukkan Oya) | 0.99 | 🟢 Normal | -0.010 |  |
| 2026-05-14 17:01:25 | Manampitiya (Mahaweli Ganga) | 0.57 | 🟢 Normal | -0.010 |  |
| 2026-05-14 17:03:27 | Baddegama (Gin Ganga) | 3.14 | 🟢 Normal | -0.010 |  |
| 2026-05-14 17:02:44 | Putupaula (Kalu Ganga) | 2.62 | 🟢 Normal | -0.010 |  |
| 2026-05-14 17:05:29 | Urawa (Nilwala Ganga) | 0.39 | 🟢 Normal | -0.015 |  |
| 2026-05-14 17:00:28 | Wellawaya (Kirindi Oya) | 1.32 | 🟢 Normal | -0.030 |  |
| 2026-05-14 17:03:21 | Panadugama (Nilwala Ganga) | 3.88 | 🟢 Normal | -0.032 |  |
| 2026-05-14 17:06:05 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.090 |  |
| 2026-05-14 17:03:58 | Galgamuwa (Mee Oya) | 1.49 | 🟢 Normal | -0.186 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)