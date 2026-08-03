# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--03_05:20:10-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **223,492 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **33** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-03 05:20:10 | Putupaula (Kalu Ganga) | 0.94 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-08-03 05:18:49 | Magura (Kalu Ganga) | 2.56 | 🟢 Normal | -288.000 |  |
| 2026-08-03 05:18:48 | Magura (Kalu Ganga) | 2.64 | 🟢 Normal | -288.000 |  |
| 2026-08-03 05:12:00 | Holombuwa (Kelani Ganga) | 1.54 | 🟢 Normal | -0.238 |  |
| 2026-08-03 05:10:32 | Rathnapura (Kalu Ganga) | 6.63 | 🟡 Alert | 0.072 | 🔺 Rising |
| 2026-08-03 05:10:05 | Panadugama (Nilwala Ganga) | 3.73 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-08-03 05:09:00 | Pitabeddara (Nilwala Ganga) | 2.40 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-08-03 05:08:13 | Glencourse (Kelani Ganga) | 14.05 | 🟢 Normal | 0.552 | 🔺 Rising |
| 2026-08-03 05:07:54 | Urawa (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.574 | 🔺 Rising |
| 2026-08-03 05:07:41 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-08-03 05:07:29 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-08-03 05:06:55 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-08-03 05:05:53 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-08-03 05:05:52 | Norwood (Kelani Ganga) | 2.14 | 🟡 Alert | -0.071 |  |
| 2026-08-03 05:04:50 | Deraniyagala (Kelani Ganga) | 2.87 | 🟢 Normal | -0.301 |  |
| 2026-08-03 05:04:46 | Urawa (Nilwala Ganga) | 0.37 | 🟢 Normal | 0.574 | 🔺 Rising |
| 2026-08-03 05:04:31 | Baddegama (Gin Ganga) | 1.01 | 🟢 Normal | -0.904 |  |
| 2026-08-03 05:04:04 | Wellawaya (Kirindi Oya) | 0.52 | 🟢 Normal | -0.009 |  |
| 2026-08-03 05:03:48 | Moragaswewa (Deduru Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-03 05:03:33 | Thawalama (Gin Ganga) | 2.93 | 🟢 Normal | 0.116 | 🔺 Rising |
| 2026-08-03 05:03:29 | Badalgama (Maha Oya) | 2.19 | 🟢 Normal | -0.010 |  |
| 2026-08-03 05:03:18 | Hanwella (Kelani Ganga) | 2.21 | 🟢 Normal | 0.334 | 🔺 Rising |
| 2026-08-03 05:02:54 | Giriulla (Maha Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-08-03 05:02:32 | Siyambalanduwa (Heda Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-08-03 05:02:24 | Ellagawa (Kalu Ganga) | 6.52 | 🟢 Normal | 0.334 | 🔺 Rising |
| 2026-08-03 05:02:12 | Thanamalwila (Kirindi Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-03 05:01:58 | Dunamale (Aththanagalu Oya) | 1.14 | 🟢 Normal | -0.010 |  |
| 2026-08-03 05:01:56 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-03 05:01:36 | Horowpothana (Yan Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-08-03 05:01:36 | Peradeniya (Mahaweli Ganga) | 7.28 | 🟠 Minor Flood | 0.684 | 🔺 Rising |
| 2026-08-03 05:01:16 | Nakkala (Kumbukkan Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-08-03 05:01:12 | Kithulgala (Kelani Ganga) | 3.45 | 🟡 Alert | -0.053 |  |
| 2026-08-03 05:00:50 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-03 04:03:21 | Nawalapitiya (Mahaweli Ganga) | 6.02 | 🔴 Major Flood | -0.464 |  |
| 2026-08-03 05:01:36 | Peradeniya (Mahaweli Ganga) | 7.28 | 🟠 Minor Flood | 0.684 | 🔺 Rising |
| 2026-08-03 05:10:32 | Rathnapura (Kalu Ganga) | 6.63 | 🟡 Alert | 0.072 | 🔺 Rising |
| 2026-08-03 05:01:12 | Kithulgala (Kelani Ganga) | 3.45 | 🟡 Alert | -0.053 |  |
| 2026-08-03 05:05:52 | Norwood (Kelani Ganga) | 2.14 | 🟡 Alert | -0.071 |  |
| 2026-08-03 05:07:54 | Urawa (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.574 | 🔺 Rising |
| 2026-08-03 05:08:13 | Glencourse (Kelani Ganga) | 14.05 | 🟢 Normal | 0.552 | 🔺 Rising |
| 2026-08-03 05:03:18 | Hanwella (Kelani Ganga) | 2.21 | 🟢 Normal | 0.334 | 🔺 Rising |
| 2026-08-03 05:02:24 | Ellagawa (Kalu Ganga) | 6.52 | 🟢 Normal | 0.334 | 🔺 Rising |
| 2026-08-03 05:03:33 | Thawalama (Gin Ganga) | 2.93 | 🟢 Normal | 0.116 | 🔺 Rising |
| 2026-08-03 05:10:05 | Panadugama (Nilwala Ganga) | 3.73 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-08-03 04:02:53 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.90 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-08-03 05:07:41 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-08-03 05:20:10 | Putupaula (Kalu Ganga) | 0.94 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-08-03 05:09:00 | Pitabeddara (Nilwala Ganga) | 2.40 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-08-03 05:01:16 | Nakkala (Kumbukkan Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-08-03 05:03:48 | Moragaswewa (Deduru Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-03 05:01:56 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-03 05:02:54 | Giriulla (Maha Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-08-03 05:01:36 | Horowpothana (Yan Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-08-02 18:03:49 | Galgamuwa (Mee Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-08-03 00:02:21 | Padiyathalawa (Maduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-03 03:12:33 | Moraketiya (Walawe Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-08-03 05:02:32 | Siyambalanduwa (Heda Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-08-03 04:03:34 | Thaldena (Mahaweli Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-08-03 05:07:29 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-08-03 05:00:50 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-08-02 18:00:59 | Thanthirimale (Malwathu Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-08-03 05:05:53 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-08-03 04:01:54 | Kuda Oya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-08-03 05:02:12 | Thanamalwila (Kirindi Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-03 05:04:04 | Wellawaya (Kirindi Oya) | 0.52 | 🟢 Normal | -0.009 |  |
| 2026-08-03 05:03:29 | Badalgama (Maha Oya) | 2.19 | 🟢 Normal | -0.010 |  |
| 2026-08-03 05:01:58 | Dunamale (Aththanagalu Oya) | 1.14 | 🟢 Normal | -0.010 |  |
| 2026-08-02 18:00:54 | Weraganthota (Mahaweli Ganga) | -3.31 | 🟢 Normal | -0.020 |  |
| 2026-08-03 05:12:00 | Holombuwa (Kelani Ganga) | 1.54 | 🟢 Normal | -0.238 |  |
| 2026-08-03 05:04:50 | Deraniyagala (Kelani Ganga) | 2.87 | 🟢 Normal | -0.301 |  |
| 2026-08-03 05:04:31 | Baddegama (Gin Ganga) | 1.01 | 🟢 Normal | -0.904 |  |
| 2026-08-03 05:18:49 | Magura (Kalu Ganga) | 2.56 | 🟢 Normal | -288.000 |  |

## River Water Level Charts by Station

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

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

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

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

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)