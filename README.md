# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--01_12:16:14-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **61,534 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-01 12:16:14 | Yaka Wewa (Ma Oya) | 1.16 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-02-01 12:12:06 | Peradeniya (Mahaweli Ganga) | 1.47 | 🟢 Normal | -0.026 |  |
| 2026-02-01 12:11:27 | Pitabeddara (Nilwala Ganga) | 0.82 | 🟢 Normal | -0.022 |  |
| 2026-02-01 12:11:26 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.54 | 🟢 Normal | 0.000 |  |
| 2026-02-01 12:10:12 | Galgamuwa (Mee Oya) | 0.43 | 🟢 Normal | -0.010 |  |
| 2026-02-01 12:09:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.54 | 🟢 Normal | 0.000 |  |
| 2026-02-01 12:07:43 | Baddegama (Gin Ganga) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-02-01 12:06:32 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-02-01 12:05:59 | Panadugama (Nilwala Ganga) | 2.47 | 🟢 Normal | 0.088 | 🔺 Rising |
| 2026-02-01 12:05:58 | Urawa (Nilwala Ganga) | 0.47 | 🟢 Normal | -0.010 |  |
| 2026-02-01 12:05:56 | Padiyathalawa (Maduru Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-02-01 12:05:27 | Glencourse (Kelani Ganga) | 8.50 | 🟢 Normal | -0.010 |  |
| 2026-02-01 12:05:19 | Badalgama (Maha Oya) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-02-01 12:05:13 | Hanwella (Kelani Ganga) | 0.49 | 🟢 Normal | -0.010 |  |
| 2026-02-01 12:05:11 | Dunamale (Aththanagalu Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-02-01 12:05:09 | Thanthirimale (Malwathu Oya) | 2.02 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-02-01 12:05:08 | Magura (Kalu Ganga) | 0.74 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-02-01 12:04:59 | Thaldena (Mahaweli Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-02-01 12:04:57 | Deraniyagala (Kelani Ganga) | 0.13 | 🟢 Normal | -0.040 |  |
| 2026-02-01 12:04:43 | Thanamalwila (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-02-01 12:04:36 | Ellagawa (Kalu Ganga) | 4.24 | 🟢 Normal | -0.010 |  |
| 2026-02-01 12:04:29 | Holombuwa (Kelani Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-02-01 12:03:57 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-02-01 12:03:45 | Thawalama (Gin Ganga) | 1.07 | 🟢 Normal | -0.100 |  |
| 2026-02-01 12:03:42 | Rathnapura (Kalu Ganga) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-02-01 12:03:39 | Moragaswewa (Deduru Oya) | 0.24 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-01 12:03:05 | Putupaula (Kalu Ganga) | 0.51 | 🟢 Normal | 0.107 | 🔺 Rising |
| 2026-02-01 12:02:45 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-02-01 12:02:37 | Giriulla (Maha Oya) | 0.89 | 🟢 Normal | -0.022 |  |
| 2026-02-01 12:02:34 | Kuda Oya (Kirindi Oya) | 1.24 | 🟢 Normal | -0.011 |  |
| 2026-02-01 12:02:21 | Manampitiya (Mahaweli Ganga) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-02-01 12:02:19 | Katharagama (Menik Ganga) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-02-01 12:02:17 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-02-01 12:01:52 | Siyambalanduwa (Heda Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-02-01 12:01:36 | Weraganthota (Mahaweli Ganga) | -1.90 | 🟢 Normal | -0.115 |  |
| 2026-02-01 12:01:21 | Nakkala (Kumbukkan Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-02-01 12:01:18 | Thalgahagoda (Nilwala Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-02-01 12:01:16 | Wellawaya (Kirindi Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-02-01 12:01:15 | Nawalapitiya (Mahaweli Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-02-01 11:59:50 | Horowpothana (Yan Oya) | 1.57 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-02-01 11:26:49 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.60 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-01 12:03:05 | Putupaula (Kalu Ganga) | 0.51 | 🟢 Normal | 0.107 | 🔺 Rising |
| 2026-02-01 12:03:57 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-02-01 12:05:59 | Panadugama (Nilwala Ganga) | 2.47 | 🟢 Normal | 0.088 | 🔺 Rising |
| 2026-02-01 12:05:09 | Thanthirimale (Malwathu Oya) | 2.02 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-02-01 12:16:14 | Yaka Wewa (Ma Oya) | 1.16 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-02-01 11:59:50 | Horowpothana (Yan Oya) | 1.57 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-02-01 12:05:08 | Magura (Kalu Ganga) | 0.74 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-02-01 12:03:39 | Moragaswewa (Deduru Oya) | 0.24 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-01 12:02:17 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-02-01 12:01:16 | Wellawaya (Kirindi Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-02-01 12:01:21 | Nakkala (Kumbukkan Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-02-01 12:01:15 | Nawalapitiya (Mahaweli Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-02-01 12:02:45 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-02-01 12:07:43 | Baddegama (Gin Ganga) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-02-01 12:05:56 | Padiyathalawa (Maduru Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-02-01 12:06:32 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-02-01 12:01:52 | Siyambalanduwa (Heda Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-02-01 12:05:11 | Dunamale (Aththanagalu Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-02-01 12:04:59 | Thaldena (Mahaweli Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-02-01 12:02:19 | Katharagama (Menik Ganga) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-02-01 12:05:19 | Badalgama (Maha Oya) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-02-01 12:04:29 | Holombuwa (Kelani Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-02-01 12:02:21 | Manampitiya (Mahaweli Ganga) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-02-01 12:03:42 | Rathnapura (Kalu Ganga) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-02-01 12:01:18 | Thalgahagoda (Nilwala Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-02-01 12:04:43 | Thanamalwila (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-02-01 12:11:26 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.54 | 🟢 Normal | 0.000 |  |
| 2026-02-01 12:05:27 | Glencourse (Kelani Ganga) | 8.50 | 🟢 Normal | -0.010 |  |
| 2026-02-01 12:05:13 | Hanwella (Kelani Ganga) | 0.49 | 🟢 Normal | -0.010 |  |
| 2026-02-01 12:10:12 | Galgamuwa (Mee Oya) | 0.43 | 🟢 Normal | -0.010 |  |
| 2026-02-01 12:04:36 | Ellagawa (Kalu Ganga) | 4.24 | 🟢 Normal | -0.010 |  |
| 2026-02-01 12:05:58 | Urawa (Nilwala Ganga) | 0.47 | 🟢 Normal | -0.010 |  |
| 2026-02-01 12:02:34 | Kuda Oya (Kirindi Oya) | 1.24 | 🟢 Normal | -0.011 |  |
| 2026-02-01 12:02:37 | Giriulla (Maha Oya) | 0.89 | 🟢 Normal | -0.022 |  |
| 2026-02-01 12:11:27 | Pitabeddara (Nilwala Ganga) | 0.82 | 🟢 Normal | -0.022 |  |
| 2026-02-01 12:12:06 | Peradeniya (Mahaweli Ganga) | 1.47 | 🟢 Normal | -0.026 |  |
| 2026-02-01 12:04:57 | Deraniyagala (Kelani Ganga) | 0.13 | 🟢 Normal | -0.040 |  |
| 2026-02-01 12:03:45 | Thawalama (Gin Ganga) | 1.07 | 🟢 Normal | -0.100 |  |
| 2026-02-01 12:01:36 | Weraganthota (Mahaweli Ganga) | -1.90 | 🟢 Normal | -0.115 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)