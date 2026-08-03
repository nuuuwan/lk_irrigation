# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--04_04:34:26-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **224,361 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-04 04:34:26 | Thaldena (Mahaweli Ganga) | 0.23 | 🟢 Normal | -0.007 |  |
| 2026-08-04 04:34:22 | Kithulgala (Kelani Ganga) | 2.75 | 🟢 Normal | -0.014 |  |
| 2026-08-04 04:20:38 | Thanamalwila (Kirindi Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-08-04 04:18:37 | Magura (Kalu Ganga) | 2.88 | 🟢 Normal | -576.000 |  |
| 2026-08-04 04:18:36 | Magura (Kalu Ganga) | 3.04 | 🟢 Normal | -576.000 |  |
| 2026-08-04 04:18:35 | Magura (Kalu Ganga) | 3.11 | 🟢 Normal | -576.000 |  |
| 2026-08-04 04:18:34 | Magura (Kalu Ganga) | 3.17 | 🟢 Normal | -576.000 |  |
| 2026-08-04 04:18:32 | Magura (Kalu Ganga) | 3.21 | 🟢 Normal | -576.000 |  |
| 2026-08-04 04:17:30 | Horowpothana (Yan Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-08-04 04:14:48 | Putupaula (Kalu Ganga) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-08-04 04:13:25 | Urawa (Nilwala Ganga) | 0.70 | 🟢 Normal | -0.094 |  |
| 2026-08-04 04:11:29 | Holombuwa (Kelani Ganga) | 1.32 | 🟢 Normal | -0.094 |  |
| 2026-08-04 04:06:52 | Kuda Oya (Kirindi Oya) | 0.96 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-08-04 04:06:36 | Glencourse (Kelani Ganga) | 15.41 | 🟡 Alert | -0.423 |  |
| 2026-08-04 04:06:18 | Nagalagam Street (Kelani Ganga) | 1.19 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-08-04 04:05:50 | Katharagama (Menik Ganga) | -0.21 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-04 04:05:47 | Deraniyagala (Kelani Ganga) | 1.60 | 🟢 Normal | -0.027 |  |
| 2026-08-04 04:05:06 | Badalgama (Maha Oya) | 4.82 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-08-04 04:04:37 | Peradeniya (Mahaweli Ganga) | 5.98 | 🟡 Alert | -0.214 |  |
| 2026-08-04 04:04:37 | Hanwella (Kelani Ganga) | 7.15 | 🟡 Alert | -0.023 |  |
| 2026-08-04 04:04:30 | Ellagawa (Kalu Ganga) | 8.45 | 🟢 Normal | 0.097 | 🔺 Rising |
| 2026-08-04 04:04:29 | Nawalapitiya (Mahaweli Ganga) | 2.70 | 🟢 Normal | -0.081 |  |
| 2026-08-04 04:04:28 | Panadugama (Nilwala Ganga) | 4.68 | 🟢 Normal | -0.075 |  |
| 2026-08-04 04:04:27 | Norwood (Kelani Ganga) | 1.43 | 🟢 Normal | -0.020 |  |
| 2026-08-04 04:03:33 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-08-04 04:03:26 | Wellawaya (Kirindi Oya) | 0.49 | 🟢 Normal | -0.021 |  |
| 2026-08-04 04:02:49 | Thalgahagoda (Nilwala Ganga) | 0.84 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-04 04:02:45 | Moragaswewa (Deduru Oya) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-08-04 04:02:19 | Giriulla (Maha Oya) | 2.80 | 🟢 Normal | -0.400 |  |
| 2026-08-04 04:02:16 | Dunamale (Aththanagalu Oya) | 1.66 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-08-04 04:02:07 | Pitabeddara (Nilwala Ganga) | 1.28 | 🟢 Normal | -0.610 |  |
| 2026-08-04 04:01:58 | Manampitiya (Mahaweli Ganga) | -0.03 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-08-04 04:01:48 | Siyambalanduwa (Heda Oya) | 0.18 | 🟢 Normal | -0.010 |  |
| 2026-08-04 04:01:38 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-08-04 04:01:29 | Moraketiya (Walawe Ganga) | 1.23 | 🟢 Normal | -0.023 |  |
| 2026-08-04 04:01:17 | Nakkala (Kumbukkan Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-08-04 04:00:59 | Thawalama (Gin Ganga) | 2.88 | 🟢 Normal | -0.186 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-04 03:07:45 | Rathnapura (Kalu Ganga) | 7.65 | 🟠 Minor Flood | -0.083 |  |
| 2026-08-04 03:02:40 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.10 | 🟡 Alert | 0.020 | 🔺 Rising |
| 2026-08-04 04:04:37 | Hanwella (Kelani Ganga) | 7.15 | 🟡 Alert | -0.023 |  |
| 2026-08-04 04:04:37 | Peradeniya (Mahaweli Ganga) | 5.98 | 🟡 Alert | -0.214 |  |
| 2026-08-04 04:06:36 | Glencourse (Kelani Ganga) | 15.41 | 🟡 Alert | -0.423 |  |
| 2026-08-04 04:04:30 | Ellagawa (Kalu Ganga) | 8.45 | 🟢 Normal | 0.097 | 🔺 Rising |
| 2026-08-04 04:06:18 | Nagalagam Street (Kelani Ganga) | 1.19 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-08-04 04:05:06 | Badalgama (Maha Oya) | 4.82 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-08-04 04:01:58 | Manampitiya (Mahaweli Ganga) | -0.03 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-08-04 03:07:18 | Baddegama (Gin Ganga) | 2.48 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-08-04 04:06:52 | Kuda Oya (Kirindi Oya) | 0.96 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-08-04 04:02:16 | Dunamale (Aththanagalu Oya) | 1.66 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-08-04 04:02:49 | Thalgahagoda (Nilwala Ganga) | 0.84 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-04 04:05:50 | Katharagama (Menik Ganga) | -0.21 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-04 04:01:17 | Nakkala (Kumbukkan Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-08-04 04:02:45 | Moragaswewa (Deduru Oya) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-08-04 03:03:47 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-04 04:17:30 | Horowpothana (Yan Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-08-03 18:03:52 | Galgamuwa (Mee Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-08-04 04:03:33 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-08-04 04:14:48 | Putupaula (Kalu Ganga) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-08-03 18:03:22 | Thanthirimale (Malwathu Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-08-04 04:20:38 | Thanamalwila (Kirindi Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-08-04 04:34:26 | Thaldena (Mahaweli Ganga) | 0.23 | 🟢 Normal | -0.007 |  |
| 2026-08-04 04:01:48 | Siyambalanduwa (Heda Oya) | 0.18 | 🟢 Normal | -0.010 |  |
| 2026-08-04 04:34:22 | Kithulgala (Kelani Ganga) | 2.75 | 🟢 Normal | -0.014 |  |
| 2026-08-04 04:04:27 | Norwood (Kelani Ganga) | 1.43 | 🟢 Normal | -0.020 |  |
| 2026-08-04 04:03:26 | Wellawaya (Kirindi Oya) | 0.49 | 🟢 Normal | -0.021 |  |
| 2026-08-04 04:01:29 | Moraketiya (Walawe Ganga) | 1.23 | 🟢 Normal | -0.023 |  |
| 2026-08-04 04:05:47 | Deraniyagala (Kelani Ganga) | 1.60 | 🟢 Normal | -0.027 |  |
| 2026-08-03 18:00:23 | Weraganthota (Mahaweli Ganga) | -3.29 | 🟢 Normal | -0.070 |  |
| 2026-08-04 04:04:28 | Panadugama (Nilwala Ganga) | 4.68 | 🟢 Normal | -0.075 |  |
| 2026-08-04 04:04:29 | Nawalapitiya (Mahaweli Ganga) | 2.70 | 🟢 Normal | -0.081 |  |
| 2026-08-04 04:11:29 | Holombuwa (Kelani Ganga) | 1.32 | 🟢 Normal | -0.094 |  |
| 2026-08-04 04:13:25 | Urawa (Nilwala Ganga) | 0.70 | 🟢 Normal | -0.094 |  |
| 2026-08-04 04:00:59 | Thawalama (Gin Ganga) | 2.88 | 🟢 Normal | -0.186 |  |
| 2026-08-04 04:02:19 | Giriulla (Maha Oya) | 2.80 | 🟢 Normal | -0.400 |  |
| 2026-08-04 04:02:07 | Pitabeddara (Nilwala Ganga) | 1.28 | 🟢 Normal | -0.610 |  |
| 2026-08-04 04:18:37 | Magura (Kalu Ganga) | 2.88 | 🟢 Normal | -576.000 |  |

## River Water Level Charts by Station

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

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

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)