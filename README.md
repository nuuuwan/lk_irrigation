# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--08_21:12:21-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **146,510 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-08 21:12:21 | Magura (Kalu Ganga) | 2.97 | 🟢 Normal | 0.215 | 🔺 Rising |
| 2026-05-08 21:11:27 | Horowpothana (Yan Oya) | 1.76 | 🟢 Normal | 0.000 |  |
| 2026-05-08 21:11:23 | Pitabeddara (Nilwala Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-05-08 21:10:04 | Panadugama (Nilwala Ganga) | 3.57 | 🟢 Normal | -0.018 |  |
| 2026-05-08 21:08:41 | Holombuwa (Kelani Ganga) | 1.59 | 🟢 Normal | 0.086 | 🔺 Rising |
| 2026-05-08 21:07:41 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.91 | 🟢 Normal | 0.171 | 🔺 Rising |
| 2026-05-08 21:07:32 | Thanamalwila (Kirindi Oya) | 4.10 | 🟡 Alert | 0.577 | 🔺 Rising |
| 2026-05-08 21:07:30 | Rathnapura (Kalu Ganga) | 2.21 | 🟢 Normal | 0.427 | 🔺 Rising |
| 2026-05-08 21:07:30 | Putupaula (Kalu Ganga) | 0.90 | 🟢 Normal | -0.040 |  |
| 2026-05-08 21:06:49 | Peradeniya (Mahaweli Ganga) | 2.20 | 🟢 Normal | 0.076 | 🔺 Rising |
| 2026-05-08 21:06:25 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-05-08 21:06:17 | Dunamale (Aththanagalu Oya) | 1.04 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-08 21:05:58 | Katharagama (Menik Ganga) | 0.45 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-05-08 21:05:47 | Norwood (Kelani Ganga) | 1.45 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-05-08 21:04:40 | Padiyathalawa (Maduru Oya) | 0.27 | 🟢 Normal | -0.011 |  |
| 2026-05-08 21:04:34 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.059 |  |
| 2026-05-08 21:04:17 | Kithulgala (Kelani Ganga) | 1.61 | 🟢 Normal | -0.081 |  |
| 2026-05-08 21:04:01 | Baddegama (Gin Ganga) | 2.22 | 🟢 Normal | 0.120 | 🔺 Rising |
| 2026-05-08 21:03:54 | Giriulla (Maha Oya) | 1.75 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-05-08 21:03:34 | Urawa (Nilwala Ganga) | 0.39 | 🟢 Normal | -0.010 |  |
| 2026-05-08 21:03:12 | Deraniyagala (Kelani Ganga) | 0.90 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-05-08 21:03:05 | Moragaswewa (Deduru Oya) | 1.78 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-05-08 21:03:02 | Glencourse (Kelani Ganga) | 9.50 | 🟢 Normal | 0.000 |  |
| 2026-05-08 21:03:00 | Badalgama (Maha Oya) | 2.71 | 🟢 Normal | -0.022 |  |
| 2026-05-08 21:02:50 | Thalgahagoda (Nilwala Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-05-08 21:02:40 | Wellawaya (Kirindi Oya) | 3.62 | 🟢 Normal | -1.688 |  |
| 2026-05-08 21:02:32 | Manampitiya (Mahaweli Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-05-08 21:02:29 | Hanwella (Kelani Ganga) | 1.47 | 🟢 Normal | -0.030 |  |
| 2026-05-08 21:02:05 | Nawalapitiya (Mahaweli Ganga) | 1.53 | 🟢 Normal | -0.010 |  |
| 2026-05-08 21:01:50 | Thawalama (Gin Ganga) | 1.74 | 🟢 Normal | 0.111 | 🔺 Rising |
| 2026-05-08 21:01:47 | Ellagawa (Kalu Ganga) | 5.66 | 🟢 Normal | 0.000 |  |
| 2026-05-08 21:01:44 | Kuda Oya (Kirindi Oya) | 6.21 | 🟢 Normal | 0.869 | 🔺 Rising |
| 2026-05-08 21:01:35 | Yaka Wewa (Ma Oya) | 0.62 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-08 21:01:22 | Thaldena (Mahaweli Ganga) | 1.45 | 🟢 Normal | 0.589 | 🔺 Rising |
| 2026-05-08 21:01:21 | Moraketiya (Walawe Ganga) | 1.59 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-08 21:01:14 | Nakkala (Kumbukkan Oya) | 0.94 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-05-08 20:26:46 | Wellawaya (Kirindi Oya) | 4.63 | 🟡 Alert | -1.688 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-08 21:07:32 | Thanamalwila (Kirindi Oya) | 4.10 | 🟡 Alert | 0.577 | 🔺 Rising |
| 2026-05-08 18:13:42 | Galgamuwa (Mee Oya) | 2.48 | 🟢 Normal | 1.954 | 🔺 Rising |
| 2026-05-08 21:01:44 | Kuda Oya (Kirindi Oya) | 6.21 | 🟢 Normal | 0.869 | 🔺 Rising |
| 2026-05-08 21:01:22 | Thaldena (Mahaweli Ganga) | 1.45 | 🟢 Normal | 0.589 | 🔺 Rising |
| 2026-05-08 21:07:30 | Rathnapura (Kalu Ganga) | 2.21 | 🟢 Normal | 0.427 | 🔺 Rising |
| 2026-05-08 21:12:21 | Magura (Kalu Ganga) | 2.97 | 🟢 Normal | 0.215 | 🔺 Rising |
| 2026-05-08 21:07:41 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.91 | 🟢 Normal | 0.171 | 🔺 Rising |
| 2026-05-08 21:04:01 | Baddegama (Gin Ganga) | 2.22 | 🟢 Normal | 0.120 | 🔺 Rising |
| 2026-05-08 21:01:50 | Thawalama (Gin Ganga) | 1.74 | 🟢 Normal | 0.111 | 🔺 Rising |
| 2026-05-08 21:03:12 | Deraniyagala (Kelani Ganga) | 0.90 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-05-08 21:08:41 | Holombuwa (Kelani Ganga) | 1.59 | 🟢 Normal | 0.086 | 🔺 Rising |
| 2026-05-08 21:06:49 | Peradeniya (Mahaweli Ganga) | 2.20 | 🟢 Normal | 0.076 | 🔺 Rising |
| 2026-05-08 21:03:05 | Moragaswewa (Deduru Oya) | 1.78 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-05-08 21:05:58 | Katharagama (Menik Ganga) | 0.45 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-05-08 21:03:54 | Giriulla (Maha Oya) | 1.75 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-05-08 21:01:14 | Nakkala (Kumbukkan Oya) | 0.94 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-05-08 18:01:43 | Thanthirimale (Malwathu Oya) | 2.10 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-05-08 21:05:47 | Norwood (Kelani Ganga) | 1.45 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-05-08 21:01:21 | Moraketiya (Walawe Ganga) | 1.59 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-08 21:06:17 | Dunamale (Aththanagalu Oya) | 1.04 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-08 21:01:35 | Yaka Wewa (Ma Oya) | 0.62 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-08 21:11:27 | Horowpothana (Yan Oya) | 1.76 | 🟢 Normal | 0.000 |  |
| 2026-05-08 21:11:23 | Pitabeddara (Nilwala Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-05-08 21:01:47 | Ellagawa (Kalu Ganga) | 5.66 | 🟢 Normal | 0.000 |  |
| 2026-05-08 21:03:02 | Glencourse (Kelani Ganga) | 9.50 | 🟢 Normal | 0.000 |  |
| 2026-05-08 21:06:25 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-05-08 21:02:32 | Manampitiya (Mahaweli Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-05-08 21:02:50 | Thalgahagoda (Nilwala Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-05-08 21:03:34 | Urawa (Nilwala Ganga) | 0.39 | 🟢 Normal | -0.010 |  |
| 2026-05-08 21:02:05 | Nawalapitiya (Mahaweli Ganga) | 1.53 | 🟢 Normal | -0.010 |  |
| 2026-05-08 21:04:40 | Padiyathalawa (Maduru Oya) | 0.27 | 🟢 Normal | -0.011 |  |
| 2026-05-08 21:10:04 | Panadugama (Nilwala Ganga) | 3.57 | 🟢 Normal | -0.018 |  |
| 2026-05-08 21:03:00 | Badalgama (Maha Oya) | 2.71 | 🟢 Normal | -0.022 |  |
| 2026-05-08 21:02:29 | Hanwella (Kelani Ganga) | 1.47 | 🟢 Normal | -0.030 |  |
| 2026-05-08 18:01:19 | Weraganthota (Mahaweli Ganga) | -2.95 | 🟢 Normal | -0.040 |  |
| 2026-05-08 21:07:30 | Putupaula (Kalu Ganga) | 0.90 | 🟢 Normal | -0.040 |  |
| 2026-05-08 21:04:34 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.059 |  |
| 2026-05-08 21:04:17 | Kithulgala (Kelani Ganga) | 1.61 | 🟢 Normal | -0.081 |  |
| 2026-05-08 21:02:40 | Wellawaya (Kirindi Oya) | 3.62 | 🟢 Normal | -1.688 |  |

## River Water Level Charts by Station

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)