# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--13_14:19:23-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **44,528 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-13 14:19:23 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-01-13 14:18:48 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-01-13 14:16:07 | Horowpothana (Yan Oya) | 3.84 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-01-13 14:14:45 | Manampitiya (Mahaweli Ganga) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-01-13 14:14:30 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-01-13 14:13:46 | Pitabeddara (Nilwala Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-01-13 14:11:16 | Urawa (Nilwala Ganga) | 0.24 | 🟢 Normal | -0.009 |  |
| 2026-01-13 14:09:35 | Magura (Kalu Ganga) | 1.02 | 🟢 Normal | -0.009 |  |
| 2026-01-13 14:08:13 | Peradeniya (Mahaweli Ganga) | 1.50 | 🟢 Normal | -0.148 |  |
| 2026-01-13 14:08:11 | Badalgama (Maha Oya) | 2.18 | 🟢 Normal | 0.000 |  |
| 2026-01-13 14:05:34 | Holombuwa (Kelani Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-01-13 14:05:07 | Galgamuwa (Mee Oya) | 0.18 | 🟢 Normal | -0.032 |  |
| 2026-01-13 14:04:56 | Dunamale (Aththanagalu Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-01-13 14:04:55 | Putupaula (Kalu Ganga) | 0.40 | 🟢 Normal | -0.052 |  |
| 2026-01-13 14:04:52 | Panadugama (Nilwala Ganga) | 2.23 | 🟢 Normal | 0.000 |  |
| 2026-01-13 14:04:44 | Katharagama (Menik Ganga) | 0.12 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-01-13 14:04:37 | Kuda Oya (Kirindi Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-01-13 14:03:36 | Hanwella (Kelani Ganga) | 0.76 | 🟢 Normal | -0.020 |  |
| 2026-01-13 14:03:31 | Deraniyagala (Kelani Ganga) | 0.26 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-01-13 14:03:01 | Norwood (Kelani Ganga) | 0.51 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-13 14:02:47 | Padiyathalawa (Maduru Oya) | 1.02 | 🟢 Normal | -0.019 |  |
| 2026-01-13 14:02:40 | Siyambalanduwa (Heda Oya) | 1.05 | 🟢 Normal | -0.010 |  |
| 2026-01-13 14:02:26 | Wellawaya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-01-13 14:02:21 | Rathnapura (Kalu Ganga) | 0.61 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-01-13 14:02:20 | Thaldena (Mahaweli Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-01-13 14:02:20 | Baddegama (Gin Ganga) | 0.90 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-01-13 14:02:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.76 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-01-13 14:02:15 | Nawalapitiya (Mahaweli Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-01-13 14:01:59 | Thanthirimale (Malwathu Oya) | 2.64 | 🟢 Normal | -0.010 |  |
| 2026-01-13 14:01:44 | Yaka Wewa (Ma Oya) | 1.28 | 🟢 Normal | -0.025 |  |
| 2026-01-13 14:01:44 | Glencourse (Kelani Ganga) | 8.89 | 🟢 Normal | 0.000 |  |
| 2026-01-13 14:01:42 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-01-13 14:01:41 | Giriulla (Maha Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-01-13 14:01:38 | Kithulgala (Kelani Ganga) | 1.49 | 🟢 Normal | 0.000 |  |
| 2026-01-13 14:01:31 | Ellagawa (Kalu Ganga) | 4.07 | 🟢 Normal | 0.000 |  |
| 2026-01-13 14:01:13 | Weraganthota (Mahaweli Ganga) | -1.47 | 🟢 Normal | -0.010 |  |
| 2026-01-13 14:01:06 | Thawalama (Gin Ganga) | 1.12 | 🟢 Normal | -0.032 |  |
| 2026-01-13 14:01:03 | Thanamalwila (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-01-13 14:00:48 | Moragaswewa (Deduru Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-01-13 14:00:09 | Nakkala (Kumbukkan Oya) | 1.16 | 🟢 Normal | -0.021 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-13 14:02:20 | Baddegama (Gin Ganga) | 0.90 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-01-13 14:02:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.76 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-01-13 14:03:31 | Deraniyagala (Kelani Ganga) | 0.26 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-01-13 14:18:48 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-01-13 14:14:30 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-01-13 14:16:07 | Horowpothana (Yan Oya) | 3.84 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-01-13 14:04:44 | Katharagama (Menik Ganga) | 0.12 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-01-13 14:02:21 | Rathnapura (Kalu Ganga) | 0.61 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-01-13 14:03:01 | Norwood (Kelani Ganga) | 0.51 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-13 14:01:38 | Kithulgala (Kelani Ganga) | 1.49 | 🟢 Normal | 0.000 |  |
| 2026-01-13 14:02:26 | Wellawaya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-01-13 14:00:48 | Moragaswewa (Deduru Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-01-13 14:02:15 | Nawalapitiya (Mahaweli Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-01-13 14:01:41 | Giriulla (Maha Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-01-13 14:13:46 | Pitabeddara (Nilwala Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-01-13 14:01:31 | Ellagawa (Kalu Ganga) | 4.07 | 🟢 Normal | 0.000 |  |
| 2026-01-13 14:04:52 | Panadugama (Nilwala Ganga) | 2.23 | 🟢 Normal | 0.000 |  |
| 2026-01-13 14:01:44 | Glencourse (Kelani Ganga) | 8.89 | 🟢 Normal | 0.000 |  |
| 2026-01-13 14:19:23 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-01-13 14:04:56 | Dunamale (Aththanagalu Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-01-13 14:02:20 | Thaldena (Mahaweli Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-01-13 14:08:11 | Badalgama (Maha Oya) | 2.18 | 🟢 Normal | 0.000 |  |
| 2026-01-13 14:05:34 | Holombuwa (Kelani Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-01-13 14:14:45 | Manampitiya (Mahaweli Ganga) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-01-13 14:04:37 | Kuda Oya (Kirindi Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-01-13 14:01:03 | Thanamalwila (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-01-13 14:09:35 | Magura (Kalu Ganga) | 1.02 | 🟢 Normal | -0.009 |  |
| 2026-01-13 14:11:16 | Urawa (Nilwala Ganga) | 0.24 | 🟢 Normal | -0.009 |  |
| 2026-01-13 14:02:40 | Siyambalanduwa (Heda Oya) | 1.05 | 🟢 Normal | -0.010 |  |
| 2026-01-13 14:01:59 | Thanthirimale (Malwathu Oya) | 2.64 | 🟢 Normal | -0.010 |  |
| 2026-01-13 14:01:13 | Weraganthota (Mahaweli Ganga) | -1.47 | 🟢 Normal | -0.010 |  |
| 2026-01-13 14:02:47 | Padiyathalawa (Maduru Oya) | 1.02 | 🟢 Normal | -0.019 |  |
| 2026-01-13 14:03:36 | Hanwella (Kelani Ganga) | 0.76 | 🟢 Normal | -0.020 |  |
| 2026-01-13 14:00:09 | Nakkala (Kumbukkan Oya) | 1.16 | 🟢 Normal | -0.021 |  |
| 2026-01-13 14:01:44 | Yaka Wewa (Ma Oya) | 1.28 | 🟢 Normal | -0.025 |  |
| 2026-01-13 14:01:06 | Thawalama (Gin Ganga) | 1.12 | 🟢 Normal | -0.032 |  |
| 2026-01-13 14:05:07 | Galgamuwa (Mee Oya) | 0.18 | 🟢 Normal | -0.032 |  |
| 2026-01-13 14:04:55 | Putupaula (Kalu Ganga) | 0.40 | 🟢 Normal | -0.052 |  |
| 2026-01-13 14:08:13 | Peradeniya (Mahaweli Ganga) | 1.50 | 🟢 Normal | -0.148 |  |

## River Water Level Charts by Station

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)