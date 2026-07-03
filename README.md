# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--03_20:22:48-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **196,427 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-03 20:22:48 | Moragaswewa (Deduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-07-03 20:15:58 | Urawa (Nilwala Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-03 20:14:06 | Thawalama (Gin Ganga) | 1.59 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-07-03 20:13:07 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-07-03 20:12:34 | Holombuwa (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-07-03 20:12:00 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-07-03 20:10:51 | Peradeniya (Mahaweli Ganga) | 1.43 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-07-03 20:09:28 | Glencourse (Kelani Ganga) | 9.64 | 🟢 Normal | -0.009 |  |
| 2026-07-03 20:09:17 | Norwood (Kelani Ganga) | 0.54 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-03 20:08:41 | Baddegama (Gin Ganga) | 1.19 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-07-03 20:08:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.46 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-07-03 20:07:25 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-07-03 20:07:16 | Panadugama (Nilwala Ganga) | 2.40 | 🟢 Normal | -0.010 |  |
| 2026-07-03 20:06:00 | Moraketiya (Walawe Ganga) | 0.77 | 🟢 Normal | -0.010 |  |
| 2026-07-03 20:05:49 | Magura (Kalu Ganga) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-07-03 20:05:29 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-07-03 20:05:09 | Pitabeddara (Nilwala Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-07-03 20:04:52 | Rathnapura (Kalu Ganga) | 1.20 | 🟢 Normal | -0.011 |  |
| 2026-07-03 20:04:28 | Ellagawa (Kalu Ganga) | 4.90 | 🟢 Normal | -0.020 |  |
| 2026-07-03 20:03:40 | Moragaswewa (Deduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-07-03 20:03:29 | Giriulla (Maha Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-07-03 20:03:24 | Badalgama (Maha Oya) | 2.09 | 🟢 Normal | 0.000 |  |
| 2026-07-03 20:03:08 | Kithulgala (Kelani Ganga) | 1.69 | 🟢 Normal | 0.000 |  |
| 2026-07-03 20:02:46 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-07-03 20:02:45 | Dunamale (Aththanagalu Oya) | 1.08 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-07-03 20:02:30 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-07-03 20:02:21 | Hanwella (Kelani Ganga) | 1.42 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-07-03 20:02:16 | Deraniyagala (Kelani Ganga) | 0.77 | 🟢 Normal | -0.020 |  |
| 2026-07-03 20:02:13 | Nawalapitiya (Mahaweli Ganga) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-07-03 20:02:12 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-07-03 20:01:58 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-07-03 20:01:48 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-07-03 20:01:45 | Manampitiya (Mahaweli Ganga) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-07-03 20:01:43 | Thaldena (Mahaweli Ganga) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-07-03 20:01:43 | Thanamalwila (Kirindi Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-07-03 20:00:43 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.092 |  |
| 2026-07-03 20:00:08 | Wellawaya (Kirindi Oya) | 0.54 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-03 20:08:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.46 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-07-03 20:14:06 | Thawalama (Gin Ganga) | 1.59 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-07-03 20:02:45 | Dunamale (Aththanagalu Oya) | 1.08 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-07-03 20:02:21 | Hanwella (Kelani Ganga) | 1.42 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-07-03 20:08:41 | Baddegama (Gin Ganga) | 1.19 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-07-03 20:10:51 | Peradeniya (Mahaweli Ganga) | 1.43 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-07-03 20:09:17 | Norwood (Kelani Ganga) | 0.54 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-03 20:03:08 | Kithulgala (Kelani Ganga) | 1.69 | 🟢 Normal | 0.000 |  |
| 2026-07-03 20:00:08 | Wellawaya (Kirindi Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-07-03 20:02:30 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-07-03 20:22:48 | Moragaswewa (Deduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-07-03 20:02:13 | Nawalapitiya (Mahaweli Ganga) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-07-03 20:05:29 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-07-03 20:03:29 | Giriulla (Maha Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-07-03 20:01:48 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-07-03 20:05:49 | Magura (Kalu Ganga) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-07-03 20:05:09 | Pitabeddara (Nilwala Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-07-03 20:13:07 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-07-03 20:01:58 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-07-03 20:01:43 | Thaldena (Mahaweli Ganga) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-07-03 20:02:12 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-07-03 20:12:00 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-07-03 20:03:24 | Badalgama (Maha Oya) | 2.09 | 🟢 Normal | 0.000 |  |
| 2026-07-03 20:12:34 | Holombuwa (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-07-03 20:01:45 | Manampitiya (Mahaweli Ganga) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-07-03 18:47:16 | Thanthirimale (Malwathu Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-07-03 20:15:58 | Urawa (Nilwala Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-03 20:02:46 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-07-03 18:02:20 | Kuda Oya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-07-03 20:01:43 | Thanamalwila (Kirindi Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-07-03 18:09:47 | Galgamuwa (Mee Oya) | 0.21 | 🟢 Normal | -0.005 |  |
| 2026-07-03 20:09:28 | Glencourse (Kelani Ganga) | 9.64 | 🟢 Normal | -0.009 |  |
| 2026-07-03 20:06:00 | Moraketiya (Walawe Ganga) | 0.77 | 🟢 Normal | -0.010 |  |
| 2026-07-03 20:07:16 | Panadugama (Nilwala Ganga) | 2.40 | 🟢 Normal | -0.010 |  |
| 2026-07-03 18:00:18 | Weraganthota (Mahaweli Ganga) | -3.45 | 🟢 Normal | -0.010 |  |
| 2026-07-03 20:04:52 | Rathnapura (Kalu Ganga) | 1.20 | 🟢 Normal | -0.011 |  |
| 2026-07-03 20:04:28 | Ellagawa (Kalu Ganga) | 4.90 | 🟢 Normal | -0.020 |  |
| 2026-07-03 20:02:16 | Deraniyagala (Kelani Ganga) | 0.77 | 🟢 Normal | -0.020 |  |
| 2026-07-03 20:00:43 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.092 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

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

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)