# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--01_06:31:09-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **112,976 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **43** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-01 06:31:09 | Galgamuwa (Mee Oya) | 0.12 | 🟢 Normal | -0.007 |  |
| 2026-04-01 06:19:20 | Panadugama (Nilwala Ganga) | 1.81 | 🟢 Normal | 0.000 |  |
| 2026-04-01 06:10:07 | Panadugama (Nilwala Ganga) | 1.81 | 🟢 Normal | 0.000 |  |
| 2026-04-01 06:09:55 | Manampitiya (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-04-01 06:08:16 | Dunamale (Aththanagalu Oya) | 0.40 | 🟢 Normal | -0.250 |  |
| 2026-04-01 06:08:03 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.029 |  |
| 2026-04-01 06:07:25 | Holombuwa (Kelani Ganga) | 0.35 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-04-01 06:07:22 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-04-01 06:06:37 | Hanwella (Kelani Ganga) | 0.17 | 🟢 Normal | -0.009 |  |
| 2026-04-01 06:06:28 | Thalgahagoda (Nilwala Ganga) | 0.47 | 🟢 Normal | -0.057 |  |
| 2026-04-01 06:06:04 | Weraganthota (Mahaweli Ganga) | -2.10 | 🟢 Normal | 0.083 | 🔺 Rising |
| 2026-04-01 06:05:51 | Rathnapura (Kalu Ganga) | 0.47 | 🟢 Normal | -0.031 |  |
| 2026-04-01 06:05:51 | Moragaswewa (Deduru Oya) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-04-01 06:05:15 | Thaldena (Mahaweli Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-04-01 06:05:12 | Urawa (Nilwala Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-04-01 06:05:01 | Yaka Wewa (Ma Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-04-01 06:04:46 | Pitabeddara (Nilwala Ganga) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-04-01 06:04:29 | Wellawaya (Kirindi Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-04-01 06:04:20 | Baddegama (Gin Ganga) | 1.06 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-01 06:04:17 | Moraketiya (Walawe Ganga) | 0.96 | 🟢 Normal | -0.103 |  |
| 2026-04-01 06:04:14 | Giriulla (Maha Oya) | 0.61 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-01 06:04:14 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-01 06:03:46 | Putupaula (Kalu Ganga) | 0.45 | 🟢 Normal | -0.098 |  |
| 2026-04-01 06:03:11 | Ellagawa (Kalu Ganga) | 3.75 | 🟢 Normal | 0.000 |  |
| 2026-04-01 06:02:58 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-04-01 06:02:48 | Norwood (Kelani Ganga) | 0.50 | 🟢 Normal | -0.020 |  |
| 2026-04-01 06:02:33 | Thawalama (Gin Ganga) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-04-01 06:02:32 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.46 | 🟢 Normal | -0.024 |  |
| 2026-04-01 06:02:26 | Deraniyagala (Kelani Ganga) | 0.10 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-04-01 06:02:24 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | -0.011 |  |
| 2026-04-01 06:02:15 | Manampitiya (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-04-01 06:02:07 | Peradeniya (Mahaweli Ganga) | 1.12 | 🟢 Normal | -0.084 |  |
| 2026-04-01 06:02:06 | Glencourse (Kelani Ganga) | 8.60 | 🟢 Normal | 0.210 | 🔺 Rising |
| 2026-04-01 06:02:00 | Nawalapitiya (Mahaweli Ganga) | 0.49 | 🟢 Normal | -0.033 |  |
| 2026-04-01 06:01:40 | Badalgama (Maha Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-04-01 06:01:13 | Kuda Oya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-04-01 06:00:30 | Magura (Kalu Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-04-01 06:00:10 | Padiyathalawa (Maduru Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-04-01 06:00:07 | Padiyathalawa (Maduru Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-04-01 05:58:26 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | -0.103 |  |
| 2026-04-01 05:49:06 | Dunamale (Aththanagalu Oya) | 0.48 | 🟢 Normal | -0.250 |  |
| 2026-04-01 05:46:11 | Rathnapura (Kalu Ganga) | 0.48 | 🟢 Normal | -0.031 |  |
| 2026-04-01 05:39:52 | Thaldena (Mahaweli Ganga) | 0.23 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-01 06:02:06 | Glencourse (Kelani Ganga) | 8.60 | 🟢 Normal | 0.210 | 🔺 Rising |
| 2026-04-01 06:06:04 | Weraganthota (Mahaweli Ganga) | -2.10 | 🟢 Normal | 0.083 | 🔺 Rising |
| 2026-04-01 06:02:26 | Deraniyagala (Kelani Ganga) | 0.10 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-04-01 06:07:25 | Holombuwa (Kelani Ganga) | 0.35 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-04-01 06:04:14 | Giriulla (Maha Oya) | 0.61 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-01 06:04:14 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-01 06:04:20 | Baddegama (Gin Ganga) | 1.06 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-01 06:07:22 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-04-01 06:04:29 | Wellawaya (Kirindi Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-04-01 06:02:58 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-04-01 06:05:51 | Moragaswewa (Deduru Oya) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-04-01 06:05:01 | Yaka Wewa (Ma Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-04-01 05:02:54 | Horowpothana (Yan Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-04-01 06:00:30 | Magura (Kalu Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-04-01 06:04:46 | Pitabeddara (Nilwala Ganga) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-04-01 06:03:11 | Ellagawa (Kalu Ganga) | 3.75 | 🟢 Normal | 0.000 |  |
| 2026-04-01 06:19:20 | Panadugama (Nilwala Ganga) | 1.81 | 🟢 Normal | 0.000 |  |
| 2026-04-01 06:00:10 | Padiyathalawa (Maduru Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-04-01 06:05:15 | Thaldena (Mahaweli Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-04-01 06:01:40 | Badalgama (Maha Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-04-01 06:09:55 | Manampitiya (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-04-01 06:02:33 | Thawalama (Gin Ganga) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-04-01 06:05:12 | Urawa (Nilwala Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-04-01 06:01:13 | Kuda Oya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-04-01 05:09:35 | Thanamalwila (Kirindi Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-04-01 06:31:09 | Galgamuwa (Mee Oya) | 0.12 | 🟢 Normal | -0.007 |  |
| 2026-04-01 06:06:37 | Hanwella (Kelani Ganga) | 0.17 | 🟢 Normal | -0.009 |  |
| 2026-03-31 18:01:49 | Thanthirimale (Malwathu Oya) | 1.28 | 🟢 Normal | -0.010 |  |
| 2026-04-01 06:02:24 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | -0.011 |  |
| 2026-04-01 06:02:48 | Norwood (Kelani Ganga) | 0.50 | 🟢 Normal | -0.020 |  |
| 2026-04-01 06:02:32 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.46 | 🟢 Normal | -0.024 |  |
| 2026-04-01 06:08:03 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.029 |  |
| 2026-04-01 06:05:51 | Rathnapura (Kalu Ganga) | 0.47 | 🟢 Normal | -0.031 |  |
| 2026-04-01 06:02:00 | Nawalapitiya (Mahaweli Ganga) | 0.49 | 🟢 Normal | -0.033 |  |
| 2026-04-01 06:06:28 | Thalgahagoda (Nilwala Ganga) | 0.47 | 🟢 Normal | -0.057 |  |
| 2026-04-01 06:02:07 | Peradeniya (Mahaweli Ganga) | 1.12 | 🟢 Normal | -0.084 |  |
| 2026-04-01 06:03:46 | Putupaula (Kalu Ganga) | 0.45 | 🟢 Normal | -0.098 |  |
| 2026-04-01 06:04:17 | Moraketiya (Walawe Ganga) | 0.96 | 🟢 Normal | -0.103 |  |
| 2026-04-01 06:08:16 | Dunamale (Aththanagalu Oya) | 0.40 | 🟢 Normal | -0.250 |  |

## River Water Level Charts by Station

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)