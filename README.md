# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--03_06:15:05-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **223,534 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **42** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-03 06:15:05 | Dunamale (Aththanagalu Oya) | 1.13 | 🟢 Normal | -0.008 |  |
| 2026-08-03 06:14:38 | Moraketiya (Walawe Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-08-03 06:12:42 | Pitabeddara (Nilwala Ganga) | 2.40 | 🟢 Normal | 0.000 |  |
| 2026-08-03 06:12:24 | Thaldena (Mahaweli Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-08-03 06:12:23 | Thaldena (Mahaweli Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-08-03 06:12:19 | Thanamalwila (Kirindi Oya) | 0.05 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-08-03 06:12:02 | Magura (Kalu Ganga) | 2.43 | 🟢 Normal | -0.147 |  |
| 2026-08-03 06:11:46 | Peradeniya (Mahaweli Ganga) | 7.50 | 🟠 Minor Flood | 0.188 | 🔺 Rising |
| 2026-08-03 06:08:38 | Baddegama (Gin Ganga) | 2.09 | 🟢 Normal | 15.385 | 🔺 Rising |
| 2026-08-03 06:07:47 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-08-03 06:07:35 | Padiyathalawa (Maduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-03 06:06:30 | Deraniyagala (Kelani Ganga) | 2.42 | 🟢 Normal | -0.438 |  |
| 2026-08-03 06:06:28 | Panadugama (Nilwala Ganga) | 3.79 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-08-03 06:06:26 | Norwood (Kelani Ganga) | 2.13 | 🟡 Alert | -0.010 |  |
| 2026-08-03 06:06:07 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.031 |  |
| 2026-08-03 06:05:38 | Moragaswewa (Deduru Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-03 06:05:22 | Glencourse (Kelani Ganga) | 14.31 | 🟢 Normal | 0.273 | 🔺 Rising |
| 2026-08-03 06:05:14 | Urawa (Nilwala Ganga) | 0.42 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-08-03 06:05:04 | Badalgama (Maha Oya) | 2.18 | 🟢 Normal | -0.010 |  |
| 2026-08-03 06:04:58 | Holombuwa (Kelani Ganga) | 1.34 | 🟢 Normal | -0.227 |  |
| 2026-08-03 06:04:44 | Baddegama (Gin Ganga) | 1.09 | 🟢 Normal | 15.385 | 🔺 Rising |
| 2026-08-03 06:04:31 | Kuda Oya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-08-03 06:04:22 | Siyambalanduwa (Heda Oya) | 0.20 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-03 06:04:02 | Horowpothana (Yan Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-08-03 06:03:14 | Thawalama (Gin Ganga) | 2.79 | 🟢 Normal | -0.141 |  |
| 2026-08-03 06:03:02 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.86 | 🟢 Normal | -0.189 |  |
| 2026-08-03 06:02:55 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-08-03 06:02:54 | Nakkala (Kumbukkan Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-08-03 06:02:23 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-08-03 06:02:21 | Hanwella (Kelani Ganga) | 3.40 | 🟢 Normal | 1.209 | 🔺 Rising |
| 2026-08-03 06:02:12 | Ellagawa (Kalu Ganga) | 6.75 | 🟢 Normal | 0.231 | 🔺 Rising |
| 2026-08-03 06:02:08 | Weraganthota (Mahaweli Ganga) | -3.30 | 🟢 Normal | 0.001 |  |
| 2026-08-03 06:02:07 | Nawalapitiya (Mahaweli Ganga) | 4.89 | 🟡 Alert | -2.172 |  |
| 2026-08-03 06:01:58 | Wellawaya (Kirindi Oya) | 0.51 | 🟢 Normal | -0.010 |  |
| 2026-08-03 06:01:40 | Kithulgala (Kelani Ganga) | 3.20 | 🟡 Alert | -0.248 |  |
| 2026-08-03 06:01:30 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-03 06:01:28 | Rathnapura (Kalu Ganga) | 6.63 | 🟡 Alert | 0.000 |  |
| 2026-08-03 06:01:06 | Giriulla (Maha Oya) | 1.08 | 🟢 Normal | -0.010 |  |
| 2026-08-03 06:00:47 | Putupaula (Kalu Ganga) | 0.95 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-08-03 05:56:42 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.88 | 🟢 Normal | -0.189 |  |
| 2026-08-03 05:41:24 | Nawalapitiya (Mahaweli Ganga) | 5.64 | 🟠 Minor Flood | -2.172 |  |
| 2026-08-03 05:39:49 | Moraketiya (Walawe Ganga) | 0.83 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-03 06:11:46 | Peradeniya (Mahaweli Ganga) | 7.50 | 🟠 Minor Flood | 0.188 | 🔺 Rising |
| 2026-08-03 06:01:28 | Rathnapura (Kalu Ganga) | 6.63 | 🟡 Alert | 0.000 |  |
| 2026-08-03 06:06:26 | Norwood (Kelani Ganga) | 2.13 | 🟡 Alert | -0.010 |  |
| 2026-08-03 06:01:40 | Kithulgala (Kelani Ganga) | 3.20 | 🟡 Alert | -0.248 |  |
| 2026-08-03 06:02:07 | Nawalapitiya (Mahaweli Ganga) | 4.89 | 🟡 Alert | -2.172 |  |
| 2026-08-03 06:08:38 | Baddegama (Gin Ganga) | 2.09 | 🟢 Normal | 15.385 | 🔺 Rising |
| 2026-08-03 06:02:21 | Hanwella (Kelani Ganga) | 3.40 | 🟢 Normal | 1.209 | 🔺 Rising |
| 2026-08-03 06:05:22 | Glencourse (Kelani Ganga) | 14.31 | 🟢 Normal | 0.273 | 🔺 Rising |
| 2026-08-03 06:02:12 | Ellagawa (Kalu Ganga) | 6.75 | 🟢 Normal | 0.231 | 🔺 Rising |
| 2026-08-03 06:06:28 | Panadugama (Nilwala Ganga) | 3.79 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-08-03 06:05:14 | Urawa (Nilwala Ganga) | 0.42 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-08-03 06:12:19 | Thanamalwila (Kirindi Oya) | 0.05 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-08-03 06:00:47 | Putupaula (Kalu Ganga) | 0.95 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-08-03 06:04:22 | Siyambalanduwa (Heda Oya) | 0.20 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-03 06:02:08 | Weraganthota (Mahaweli Ganga) | -3.30 | 🟢 Normal | 0.001 |  |
| 2026-08-03 06:02:54 | Nakkala (Kumbukkan Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-08-03 06:05:38 | Moragaswewa (Deduru Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-03 06:01:30 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-03 06:04:02 | Horowpothana (Yan Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-08-02 18:03:49 | Galgamuwa (Mee Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-08-03 06:12:42 | Pitabeddara (Nilwala Ganga) | 2.40 | 🟢 Normal | 0.000 |  |
| 2026-08-03 06:07:35 | Padiyathalawa (Maduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-03 06:14:38 | Moraketiya (Walawe Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-08-03 06:12:24 | Thaldena (Mahaweli Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-08-03 06:02:55 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-08-03 06:02:23 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-08-02 18:00:59 | Thanthirimale (Malwathu Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-08-03 06:07:47 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-08-03 06:04:31 | Kuda Oya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-08-03 06:15:05 | Dunamale (Aththanagalu Oya) | 1.13 | 🟢 Normal | -0.008 |  |
| 2026-08-03 06:05:04 | Badalgama (Maha Oya) | 2.18 | 🟢 Normal | -0.010 |  |
| 2026-08-03 06:01:06 | Giriulla (Maha Oya) | 1.08 | 🟢 Normal | -0.010 |  |
| 2026-08-03 06:01:58 | Wellawaya (Kirindi Oya) | 0.51 | 🟢 Normal | -0.010 |  |
| 2026-08-03 06:06:07 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.031 |  |
| 2026-08-03 06:03:14 | Thawalama (Gin Ganga) | 2.79 | 🟢 Normal | -0.141 |  |
| 2026-08-03 06:12:02 | Magura (Kalu Ganga) | 2.43 | 🟢 Normal | -0.147 |  |
| 2026-08-03 06:03:02 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.86 | 🟢 Normal | -0.189 |  |
| 2026-08-03 06:04:58 | Holombuwa (Kelani Ganga) | 1.34 | 🟢 Normal | -0.227 |  |
| 2026-08-03 06:06:30 | Deraniyagala (Kelani Ganga) | 2.42 | 🟢 Normal | -0.438 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)