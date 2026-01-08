# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--08_20:13:25-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **40,271 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-08 20:13:25 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-01-08 20:12:55 | Norwood (Kelani Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-01-08 20:11:53 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.057 |  |
| 2026-01-08 20:11:24 | Padiyathalawa (Maduru Oya) | 1.40 | 🟢 Normal | -0.081 |  |
| 2026-01-08 20:10:56 | Ellagawa (Kalu Ganga) | 4.10 | 🟢 Normal | 0.000 |  |
| 2026-01-08 20:10:53 | Magura (Kalu Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-01-08 20:10:27 | Pitabeddara (Nilwala Ganga) | 0.90 | 🟢 Normal | -0.009 |  |
| 2026-01-08 20:09:27 | Katharagama (Menik Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-01-08 20:08:45 | Panadugama (Nilwala Ganga) | 2.90 | 🟢 Normal | -0.081 |  |
| 2026-01-08 20:08:27 | Norwood (Kelani Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-01-08 20:08:10 | Putupaula (Kalu Ganga) | 0.65 | 🟢 Normal | -0.096 |  |
| 2026-01-08 20:07:57 | Yaka Wewa (Ma Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-01-08 20:07:48 | Glencourse (Kelani Ganga) | 8.50 | 🟢 Normal | -0.009 |  |
| 2026-01-08 20:07:12 | Thaldena (Mahaweli Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-01-08 20:07:04 | Holombuwa (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-01-08 20:05:56 | Thawalama (Gin Ganga) | 1.32 | 🟢 Normal | -0.010 |  |
| 2026-01-08 20:05:24 | Badalgama (Maha Oya) | 2.01 | 🟢 Normal | 0.000 |  |
| 2026-01-08 20:04:54 | Hanwella (Kelani Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-01-08 20:04:36 | Moragaswewa (Deduru Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-01-08 20:04:32 | Deraniyagala (Kelani Ganga) | 0.17 | 🟢 Normal | -0.009 |  |
| 2026-01-08 20:04:17 | Dunamale (Aththanagalu Oya) | 0.85 | 🟢 Normal | -0.079 |  |
| 2026-01-08 20:04:11 | Giriulla (Maha Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-01-08 20:04:05 | Nawalapitiya (Mahaweli Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-01-08 20:03:55 | Thalgahagoda (Nilwala Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-01-08 20:03:48 | Urawa (Nilwala Ganga) | 0.33 | 🟢 Normal | -0.010 |  |
| 2026-01-08 20:03:17 | Kuda Oya (Kirindi Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-01-08 20:03:08 | Nakkala (Kumbukkan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-01-08 20:03:02 | Thanamalwila (Kirindi Oya) | 0.94 | 🟢 Normal | -0.010 |  |
| 2026-01-08 20:02:59 | Moragaswewa (Deduru Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-01-08 20:02:57 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-01-08 20:02:56 | Kithulgala (Kelani Ganga) | 1.58 | 🟢 Normal | -0.020 |  |
| 2026-01-08 20:02:44 | Rathnapura (Kalu Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-01-08 20:02:42 | Siyambalanduwa (Heda Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-01-08 20:02:25 | Peradeniya (Mahaweli Ganga) | 2.20 | 🟢 Normal | 0.353 | 🔺 Rising |
| 2026-01-08 20:01:54 | Horowpothana (Yan Oya) | 2.20 | 🟢 Normal | -0.014 |  |
| 2026-01-08 20:01:17 | Wellawaya (Kirindi Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-01-08 20:01:17 | Ellagawa (Kalu Ganga) | 4.10 | 🟢 Normal | 0.000 |  |
| 2026-01-08 20:01:14 | Manampitiya (Mahaweli Ganga) | 2.25 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-01-08 20:00:35 | Baddegama (Gin Ganga) | 1.02 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-01-08 19:36:29 | Badalgama (Maha Oya) | 2.01 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-08 20:02:25 | Peradeniya (Mahaweli Ganga) | 2.20 | 🟢 Normal | 0.353 | 🔺 Rising |
| 2026-01-08 20:01:14 | Manampitiya (Mahaweli Ganga) | 2.25 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-01-08 18:00:51 | Weraganthota (Mahaweli Ganga) | -1.15 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-01-08 20:00:35 | Baddegama (Gin Ganga) | 1.02 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-01-08 20:01:17 | Wellawaya (Kirindi Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-01-08 20:03:08 | Nakkala (Kumbukkan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-01-08 20:04:36 | Moragaswewa (Deduru Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-01-08 20:04:05 | Nawalapitiya (Mahaweli Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-01-08 20:07:57 | Yaka Wewa (Ma Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-01-08 20:04:11 | Giriulla (Maha Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-01-08 20:10:53 | Magura (Kalu Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-01-08 20:12:55 | Norwood (Kelani Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-01-08 20:04:54 | Hanwella (Kelani Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-01-08 20:10:56 | Ellagawa (Kalu Ganga) | 4.10 | 🟢 Normal | 0.000 |  |
| 2026-01-08 20:02:57 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-01-08 20:02:42 | Siyambalanduwa (Heda Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-01-08 20:07:12 | Thaldena (Mahaweli Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-01-08 20:09:27 | Katharagama (Menik Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-01-08 20:05:24 | Badalgama (Maha Oya) | 2.01 | 🟢 Normal | 0.000 |  |
| 2026-01-08 20:07:04 | Holombuwa (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-01-08 20:02:44 | Rathnapura (Kalu Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-01-08 20:03:55 | Thalgahagoda (Nilwala Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-01-08 20:03:17 | Kuda Oya (Kirindi Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-01-08 20:13:25 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-01-08 20:10:27 | Pitabeddara (Nilwala Ganga) | 0.90 | 🟢 Normal | -0.009 |  |
| 2026-01-08 20:04:32 | Deraniyagala (Kelani Ganga) | 0.17 | 🟢 Normal | -0.009 |  |
| 2026-01-08 20:07:48 | Glencourse (Kelani Ganga) | 8.50 | 🟢 Normal | -0.009 |  |
| 2026-01-08 20:05:56 | Thawalama (Gin Ganga) | 1.32 | 🟢 Normal | -0.010 |  |
| 2026-01-08 20:03:48 | Urawa (Nilwala Ganga) | 0.33 | 🟢 Normal | -0.010 |  |
| 2026-01-08 18:02:13 | Thanthirimale (Malwathu Oya) | 1.53 | 🟢 Normal | -0.010 |  |
| 2026-01-08 20:03:02 | Thanamalwila (Kirindi Oya) | 0.94 | 🟢 Normal | -0.010 |  |
| 2026-01-08 20:01:54 | Horowpothana (Yan Oya) | 2.20 | 🟢 Normal | -0.014 |  |
| 2026-01-08 20:02:56 | Kithulgala (Kelani Ganga) | 1.58 | 🟢 Normal | -0.020 |  |
| 2026-01-08 18:07:05 | Galgamuwa (Mee Oya) | 0.24 | 🟢 Normal | -0.038 |  |
| 2026-01-08 20:11:53 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.057 |  |
| 2026-01-08 20:04:17 | Dunamale (Aththanagalu Oya) | 0.85 | 🟢 Normal | -0.079 |  |
| 2026-01-08 20:08:45 | Panadugama (Nilwala Ganga) | 2.90 | 🟢 Normal | -0.081 |  |
| 2026-01-08 20:11:24 | Padiyathalawa (Maduru Oya) | 1.40 | 🟢 Normal | -0.081 |  |
| 2026-01-08 20:08:10 | Putupaula (Kalu Ganga) | 0.65 | 🟢 Normal | -0.096 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)