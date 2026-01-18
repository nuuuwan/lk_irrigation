# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--18_07:29:30-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **48,740 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-18 07:29:30 | Urawa (Nilwala Ganga) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-01-18 07:24:08 | Magura (Kalu Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-01-18 07:17:46 | Glencourse (Kelani Ganga) | 8.64 | 🟢 Normal | -0.024 |  |
| 2026-01-18 07:15:01 | Baddegama (Gin Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-01-18 07:13:12 | Pitabeddara (Nilwala Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-01-18 07:12:24 | Dunamale (Aththanagalu Oya) | 0.65 | 🟢 Normal | -0.009 |  |
| 2026-01-18 07:12:04 | Ellagawa (Kalu Ganga) | 3.97 | 🟢 Normal | 0.000 |  |
| 2026-01-18 07:11:13 | Manampitiya (Mahaweli Ganga) | 1.15 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-01-18 07:10:34 | Putupaula (Kalu Ganga) | 0.53 | 🟢 Normal | -0.035 |  |
| 2026-01-18 07:08:55 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.60 | 🟢 Normal | -0.097 |  |
| 2026-01-18 07:08:41 | Giriulla (Maha Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-01-18 07:08:40 | Moragaswewa (Deduru Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-01-18 07:07:24 | Ellagawa (Kalu Ganga) | 3.97 | 🟢 Normal | 0.000 |  |
| 2026-01-18 07:06:51 | Thanamalwila (Kirindi Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-01-18 07:06:29 | Thaldena (Mahaweli Ganga) | 0.59 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-01-18 07:05:56 | Thawalama (Gin Ganga) | 1.09 | 🟢 Normal | -0.010 |  |
| 2026-01-18 07:05:15 | Panadugama (Nilwala Ganga) | 2.16 | 🟢 Normal | -0.011 |  |
| 2026-01-18 07:04:45 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-01-18 07:04:11 | Badalgama (Maha Oya) | 1.91 | 🟢 Normal | 0.000 |  |
| 2026-01-18 07:04:06 | Galgamuwa (Mee Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-01-18 07:03:54 | Rathnapura (Kalu Ganga) | 0.58 | 🟢 Normal | -0.010 |  |
| 2026-01-18 07:03:33 | Hanwella (Kelani Ganga) | 0.47 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-18 07:03:32 | Padiyathalawa (Maduru Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-01-18 07:03:18 | Katharagama (Menik Ganga) | -0.02 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-18 07:03:09 | Peradeniya (Mahaweli Ganga) | 1.29 | 🟢 Normal | -0.119 |  |
| 2026-01-18 07:03:07 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-01-18 07:02:58 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.100 |  |
| 2026-01-18 07:02:48 | Norwood (Kelani Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-01-18 07:02:22 | Siyambalanduwa (Heda Oya) | 0.71 | 🟢 Normal | -0.020 |  |
| 2026-01-18 07:02:17 | Weraganthota (Mahaweli Ganga) | -1.79 | 🟢 Normal | 0.000 |  |
| 2026-01-18 07:01:51 | Thanthirimale (Malwathu Oya) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-01-18 07:01:47 | Yaka Wewa (Ma Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-01-18 07:01:34 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-01-18 07:01:32 | Deraniyagala (Kelani Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-01-18 07:01:27 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-01-18 07:01:19 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-01-18 07:01:10 | Kuda Oya (Kirindi Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-01-18 07:01:01 | Horowpothana (Yan Oya) | 1.39 | 🟢 Normal | -0.034 |  |
| 2026-01-18 07:00:54 | Nawalapitiya (Mahaweli Ganga) | 0.68 | 🟢 Normal | -0.020 |  |
| 2026-01-18 07:00:06 | Nakkala (Kumbukkan Oya) | 0.97 | 🟢 Normal | 0.011 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-18 07:01:34 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-01-18 07:11:13 | Manampitiya (Mahaweli Ganga) | 1.15 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-01-18 07:03:18 | Katharagama (Menik Ganga) | -0.02 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-18 07:00:06 | Nakkala (Kumbukkan Oya) | 0.97 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-01-18 07:03:33 | Hanwella (Kelani Ganga) | 0.47 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-18 07:06:29 | Thaldena (Mahaweli Ganga) | 0.59 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-01-18 07:03:07 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-01-18 07:02:17 | Weraganthota (Mahaweli Ganga) | -1.79 | 🟢 Normal | 0.000 |  |
| 2026-01-18 07:01:27 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-01-18 07:08:40 | Moragaswewa (Deduru Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-01-18 07:01:47 | Yaka Wewa (Ma Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-01-18 07:08:41 | Giriulla (Maha Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-01-18 07:04:06 | Galgamuwa (Mee Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-01-18 07:24:08 | Magura (Kalu Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-01-18 07:13:12 | Pitabeddara (Nilwala Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-01-18 07:02:48 | Norwood (Kelani Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-01-18 07:01:32 | Deraniyagala (Kelani Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-01-18 07:12:04 | Ellagawa (Kalu Ganga) | 3.97 | 🟢 Normal | 0.000 |  |
| 2026-01-18 07:15:01 | Baddegama (Gin Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-01-18 07:03:32 | Padiyathalawa (Maduru Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-01-18 07:01:19 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-01-18 07:04:11 | Badalgama (Maha Oya) | 1.91 | 🟢 Normal | 0.000 |  |
| 2026-01-18 07:04:45 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-01-18 07:01:51 | Thanthirimale (Malwathu Oya) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-01-18 07:29:30 | Urawa (Nilwala Ganga) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-01-18 07:01:10 | Kuda Oya (Kirindi Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-01-18 07:06:51 | Thanamalwila (Kirindi Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-01-18 07:12:24 | Dunamale (Aththanagalu Oya) | 0.65 | 🟢 Normal | -0.009 |  |
| 2026-01-18 07:05:56 | Thawalama (Gin Ganga) | 1.09 | 🟢 Normal | -0.010 |  |
| 2026-01-18 07:03:54 | Rathnapura (Kalu Ganga) | 0.58 | 🟢 Normal | -0.010 |  |
| 2026-01-18 07:05:15 | Panadugama (Nilwala Ganga) | 2.16 | 🟢 Normal | -0.011 |  |
| 2026-01-18 07:02:22 | Siyambalanduwa (Heda Oya) | 0.71 | 🟢 Normal | -0.020 |  |
| 2026-01-18 07:00:54 | Nawalapitiya (Mahaweli Ganga) | 0.68 | 🟢 Normal | -0.020 |  |
| 2026-01-18 07:17:46 | Glencourse (Kelani Ganga) | 8.64 | 🟢 Normal | -0.024 |  |
| 2026-01-18 07:01:01 | Horowpothana (Yan Oya) | 1.39 | 🟢 Normal | -0.034 |  |
| 2026-01-18 07:10:34 | Putupaula (Kalu Ganga) | 0.53 | 🟢 Normal | -0.035 |  |
| 2026-01-18 07:08:55 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.60 | 🟢 Normal | -0.097 |  |
| 2026-01-18 07:02:58 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.100 |  |
| 2026-01-18 07:03:09 | Peradeniya (Mahaweli Ganga) | 1.29 | 🟢 Normal | -0.119 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)