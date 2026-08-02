# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--03_05:03:33-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **223,473 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **16** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
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
| 2026-08-03 04:34:43 | Putupaula (Kalu Ganga) | 0.92 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-08-03 04:31:17 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | -0.028 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-03 04:03:21 | Nawalapitiya (Mahaweli Ganga) | 6.02 | 🔴 Major Flood | -0.464 |  |
| 2026-08-03 05:01:36 | Peradeniya (Mahaweli Ganga) | 7.28 | 🟠 Minor Flood | 0.684 | 🔺 Rising |
| 2026-08-03 04:03:30 | Rathnapura (Kalu Ganga) | 6.55 | 🟡 Alert | 0.314 | 🔺 Rising |
| 2026-08-03 04:06:40 | Norwood (Kelani Ganga) | 2.21 | 🟡 Alert | 0.130 | 🔺 Rising |
| 2026-08-03 05:01:12 | Kithulgala (Kelani Ganga) | 3.45 | 🟡 Alert | -0.053 |  |
| 2026-08-03 04:10:35 | Glencourse (Kelani Ganga) | 13.52 | 🟢 Normal | 1.078 | 🔺 Rising |
| 2026-08-03 05:03:18 | Hanwella (Kelani Ganga) | 2.21 | 🟢 Normal | 0.334 | 🔺 Rising |
| 2026-08-03 05:02:24 | Ellagawa (Kalu Ganga) | 6.52 | 🟢 Normal | 0.334 | 🔺 Rising |
| 2026-08-03 04:07:11 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.230 | 🔺 Rising |
| 2026-08-03 04:06:27 | Holombuwa (Kelani Ganga) | 1.80 | 🟢 Normal | 0.160 | 🔺 Rising |
| 2026-08-03 05:03:33 | Thawalama (Gin Ganga) | 2.93 | 🟢 Normal | 0.116 | 🔺 Rising |
| 2026-08-03 04:03:20 | Panadugama (Nilwala Ganga) | 3.66 | 🟢 Normal | 0.110 | 🔺 Rising |
| 2026-08-03 04:04:09 | Baddegama (Gin Ganga) | 1.92 | 🟢 Normal | 0.083 | 🔺 Rising |
| 2026-08-03 04:02:53 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.90 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-08-03 03:00:51 | Pitabeddara (Nilwala Ganga) | 2.38 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-08-03 03:06:52 | Urawa (Nilwala Ganga) | 0.33 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-08-03 04:00:45 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-08-03 04:34:43 | Putupaula (Kalu Ganga) | 0.92 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-08-03 05:01:16 | Nakkala (Kumbukkan Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-08-03 04:00:56 | Moragaswewa (Deduru Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-03 05:01:56 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-03 05:02:54 | Giriulla (Maha Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-08-03 05:01:36 | Horowpothana (Yan Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-08-02 18:03:49 | Galgamuwa (Mee Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-08-03 00:02:21 | Padiyathalawa (Maduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-03 03:12:33 | Moraketiya (Walawe Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-08-03 05:02:32 | Siyambalanduwa (Heda Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-08-03 04:03:34 | Thaldena (Mahaweli Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-08-03 04:06:19 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-08-03 05:00:50 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-08-02 18:00:59 | Thanthirimale (Malwathu Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-08-03 04:01:54 | Kuda Oya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-08-03 05:02:12 | Thanamalwila (Kirindi Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-03 05:03:29 | Badalgama (Maha Oya) | 2.19 | 🟢 Normal | -0.010 |  |
| 2026-08-03 05:01:58 | Dunamale (Aththanagalu Oya) | 1.14 | 🟢 Normal | -0.010 |  |
| 2026-08-02 18:00:54 | Weraganthota (Mahaweli Ganga) | -3.31 | 🟢 Normal | -0.020 |  |
| 2026-08-03 04:31:17 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | -0.028 |  |
| 2026-08-03 03:05:07 | Deraniyagala (Kelani Ganga) | 3.47 | 🟢 Normal | -0.378 |  |
| 2026-08-03 03:07:19 | Magura (Kalu Ganga) | 2.12 | 🟢 Normal | -1008.000 |  |

## River Water Level Charts by Station

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

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

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)