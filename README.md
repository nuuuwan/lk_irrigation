# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--25_00:17:39-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **160,786 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-25 00:17:39 | Urawa (Nilwala Ganga) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-05-25 00:17:08 | Rathnapura (Kalu Ganga) | 5.21 | 🟡 Alert | -0.050 |  |
| 2026-05-25 00:13:03 | Manampitiya (Mahaweli Ganga) | 0.11 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-05-25 00:09:00 | Glencourse (Kelani Ganga) | 10.75 | 🟢 Normal | -0.019 |  |
| 2026-05-25 00:08:52 | Magura (Kalu Ganga) | 2.05 | 🟢 Normal | -0.019 |  |
| 2026-05-25 00:07:54 | Baddegama (Gin Ganga) | 1.47 | 🟢 Normal | -0.010 |  |
| 2026-05-25 00:06:46 | Holombuwa (Kelani Ganga) | 1.35 | 🟢 Normal | 0.215 | 🔺 Rising |
| 2026-05-25 00:06:19 | Panadugama (Nilwala Ganga) | 2.41 | 🟢 Normal | -0.022 |  |
| 2026-05-25 00:05:55 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-05-25 00:05:45 | Putupaula (Kalu Ganga) | 3.24 | 🟡 Alert | -0.010 |  |
| 2026-05-25 00:05:44 | Moragaswewa (Deduru Oya) | 0.60 | 🟢 Normal | -0.010 |  |
| 2026-05-25 00:05:29 | Kithulgala (Kelani Ganga) | 2.08 | 🟢 Normal | 0.000 |  |
| 2026-05-25 00:05:18 | Badalgama (Maha Oya) | 2.66 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-25 00:04:59 | Norwood (Kelani Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-05-25 00:04:40 | Pitabeddara (Nilwala Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-05-25 00:04:39 | Hanwella (Kelani Ganga) | 4.10 | 🟢 Normal | 0.096 | 🔺 Rising |
| 2026-05-25 00:04:16 | Ellagawa (Kalu Ganga) | 9.37 | 🟢 Normal | -0.030 |  |
| 2026-05-25 00:03:49 | Peradeniya (Mahaweli Ganga) | 1.96 | 🟢 Normal | 0.145 | 🔺 Rising |
| 2026-05-25 00:03:47 | Thaldena (Mahaweli Ganga) | 0.28 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-25 00:03:14 | Deraniyagala (Kelani Ganga) | 2.60 | 🟢 Normal | -0.234 |  |
| 2026-05-25 00:02:51 | Thawalama (Gin Ganga) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-05-25 00:02:27 | Thanamalwila (Kirindi Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-05-25 00:02:27 | Dunamale (Aththanagalu Oya) | 2.68 | 🟢 Normal | -0.040 |  |
| 2026-05-25 00:02:16 | Giriulla (Maha Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-05-25 00:02:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.11 | 🟡 Alert | -0.010 |  |
| 2026-05-25 00:01:56 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-05-25 00:01:43 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-05-25 00:01:42 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | -0.010 |  |
| 2026-05-25 00:01:41 | Kuda Oya (Kirindi Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-05-25 00:01:36 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-05-25 00:01:25 | Thalgahagoda (Nilwala Ganga) | 0.26 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-25 00:01:21 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-25 00:01:19 | Nagalagam Street (Kelani Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-05-25 00:01:08 | Nawalapitiya (Mahaweli Ganga) | 1.85 | 🟢 Normal | -0.010 |  |
| 2026-05-25 00:00:15 | Wellawaya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-05-24 23:59:42 | Nagalagam Street (Kelani Ganga) | 0.79 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-25 00:05:45 | Putupaula (Kalu Ganga) | 3.24 | 🟡 Alert | -0.010 |  |
| 2026-05-25 00:02:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.11 | 🟡 Alert | -0.010 |  |
| 2026-05-25 00:17:08 | Rathnapura (Kalu Ganga) | 5.21 | 🟡 Alert | -0.050 |  |
| 2026-05-25 00:06:46 | Holombuwa (Kelani Ganga) | 1.35 | 🟢 Normal | 0.215 | 🔺 Rising |
| 2026-05-25 00:03:49 | Peradeniya (Mahaweli Ganga) | 1.96 | 🟢 Normal | 0.145 | 🔺 Rising |
| 2026-05-25 00:04:39 | Hanwella (Kelani Ganga) | 4.10 | 🟢 Normal | 0.096 | 🔺 Rising |
| 2026-05-25 00:13:03 | Manampitiya (Mahaweli Ganga) | 0.11 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-05-25 00:01:25 | Thalgahagoda (Nilwala Ganga) | 0.26 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-25 00:05:18 | Badalgama (Maha Oya) | 2.66 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-25 00:03:47 | Thaldena (Mahaweli Ganga) | 0.28 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-25 00:05:29 | Kithulgala (Kelani Ganga) | 2.08 | 🟢 Normal | 0.000 |  |
| 2026-05-24 18:00:57 | Weraganthota (Mahaweli Ganga) | -3.34 | 🟢 Normal | 0.000 |  |
| 2026-05-25 00:00:15 | Wellawaya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-05-25 00:01:21 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-24 23:01:56 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-05-25 00:02:16 | Giriulla (Maha Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-05-25 00:01:36 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-05-24 18:00:50 | Galgamuwa (Mee Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-05-25 00:04:40 | Pitabeddara (Nilwala Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-05-25 00:04:59 | Norwood (Kelani Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-05-25 00:01:43 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-05-25 00:01:19 | Nagalagam Street (Kelani Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-05-25 00:01:56 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-05-25 00:05:55 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-05-24 18:00:42 | Thanthirimale (Malwathu Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-05-25 00:02:51 | Thawalama (Gin Ganga) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-05-25 00:17:39 | Urawa (Nilwala Ganga) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-05-25 00:01:41 | Kuda Oya (Kirindi Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-05-25 00:02:27 | Thanamalwila (Kirindi Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-05-25 00:01:42 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | -0.010 |  |
| 2026-05-25 00:07:54 | Baddegama (Gin Ganga) | 1.47 | 🟢 Normal | -0.010 |  |
| 2026-05-25 00:05:44 | Moragaswewa (Deduru Oya) | 0.60 | 🟢 Normal | -0.010 |  |
| 2026-05-25 00:01:08 | Nawalapitiya (Mahaweli Ganga) | 1.85 | 🟢 Normal | -0.010 |  |
| 2026-05-25 00:08:52 | Magura (Kalu Ganga) | 2.05 | 🟢 Normal | -0.019 |  |
| 2026-05-25 00:09:00 | Glencourse (Kelani Ganga) | 10.75 | 🟢 Normal | -0.019 |  |
| 2026-05-25 00:06:19 | Panadugama (Nilwala Ganga) | 2.41 | 🟢 Normal | -0.022 |  |
| 2026-05-25 00:04:16 | Ellagawa (Kalu Ganga) | 9.37 | 🟢 Normal | -0.030 |  |
| 2026-05-25 00:02:27 | Dunamale (Aththanagalu Oya) | 2.68 | 🟢 Normal | -0.040 |  |
| 2026-05-25 00:03:14 | Deraniyagala (Kelani Ganga) | 2.60 | 🟢 Normal | -0.234 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

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

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)