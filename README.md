# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--29_03:17:10-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **137,838 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-29 03:17:10 | Wellawaya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-04-29 03:16:11 | Rathnapura (Kalu Ganga) | 0.90 | 🟢 Normal | -0.017 |  |
| 2026-04-29 03:14:58 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.46 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-04-29 03:14:52 | Magura (Kalu Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-04-29 03:13:38 | Baddegama (Gin Ganga) | 1.28 | 🟢 Normal | -0.036 |  |
| 2026-04-29 03:09:54 | Badalgama (Maha Oya) | 2.41 | 🟢 Normal | -0.027 |  |
| 2026-04-29 03:08:18 | Thaldena (Mahaweli Ganga) | 0.27 | 🟢 Normal | -36.000 |  |
| 2026-04-29 03:08:17 | Thaldena (Mahaweli Ganga) | 0.28 | 🟢 Normal | -36.000 |  |
| 2026-04-29 03:08:16 | Thaldena (Mahaweli Ganga) | 0.29 | 🟢 Normal | -36.000 |  |
| 2026-04-29 03:07:50 | Holombuwa (Kelani Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-04-29 03:07:40 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.095 |  |
| 2026-04-29 03:06:27 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | -0.008 |  |
| 2026-04-29 03:06:17 | Urawa (Nilwala Ganga) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-04-29 03:04:32 | Pitabeddara (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-04-29 03:04:12 | Hanwella (Kelani Ganga) | 0.68 | 🟢 Normal | -0.024 |  |
| 2026-04-29 03:04:04 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-04-29 03:03:31 | Norwood (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-04-29 03:03:18 | Moragaswewa (Deduru Oya) | 0.26 | 🟢 Normal | -0.010 |  |
| 2026-04-29 03:02:45 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-04-29 03:02:27 | Dunamale (Aththanagalu Oya) | 1.20 | 🟢 Normal | -0.030 |  |
| 2026-04-29 03:02:26 | Manampitiya (Mahaweli Ganga) | 0.35 | 🟢 Normal | -0.010 |  |
| 2026-04-29 03:02:25 | Thanamalwila (Kirindi Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-04-29 03:02:16 | Glencourse (Kelani Ganga) | 9.10 | 🟢 Normal | 0.129 | 🔺 Rising |
| 2026-04-29 03:02:13 | Ellagawa (Kalu Ganga) | 4.52 | 🟢 Normal | -0.020 |  |
| 2026-04-29 03:02:05 | Giriulla (Maha Oya) | 1.20 | 🟢 Normal | -0.010 |  |
| 2026-04-29 03:01:59 | Deraniyagala (Kelani Ganga) | 0.37 | 🟢 Normal | -0.020 |  |
| 2026-04-29 03:01:55 | Panadugama (Nilwala Ganga) | 2.24 | 🟢 Normal | -0.010 |  |
| 2026-04-29 03:01:49 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-29 03:01:47 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-29 03:01:40 | Kuda Oya (Kirindi Oya) | 1.58 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-04-29 03:01:39 | Peradeniya (Mahaweli Ganga) | 1.60 | 🟢 Normal | -0.020 |  |
| 2026-04-29 03:01:37 | Nawalapitiya (Mahaweli Ganga) | 1.11 | 🟢 Normal | -0.045 |  |
| 2026-04-29 03:00:57 | Thalgahagoda (Nilwala Ganga) | 0.38 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-04-29 03:00:29 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-04-29 03:00:17 | Padiyathalawa (Maduru Oya) | 0.15 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-29 03:02:16 | Glencourse (Kelani Ganga) | 9.10 | 🟢 Normal | 0.129 | 🔺 Rising |
| 2026-04-29 03:14:58 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.46 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-04-29 03:00:57 | Thalgahagoda (Nilwala Ganga) | 0.38 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-04-28 18:04:58 | Galgamuwa (Mee Oya) | 0.40 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-29 03:01:40 | Kuda Oya (Kirindi Oya) | 1.58 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-04-28 17:02:52 | Weraganthota (Mahaweli Ganga) | -3.20 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-29 03:04:04 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-04-29 03:17:10 | Wellawaya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-04-29 03:01:49 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-29 00:08:33 | Yaka Wewa (Ma Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-04-29 03:14:52 | Magura (Kalu Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-04-29 03:04:32 | Pitabeddara (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-04-29 03:03:31 | Norwood (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-04-29 03:02:45 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-04-29 03:07:50 | Holombuwa (Kelani Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-04-29 03:06:17 | Urawa (Nilwala Ganga) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-04-29 03:02:25 | Thanamalwila (Kirindi Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-04-29 03:06:27 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | -0.008 |  |
| 2026-04-29 02:10:15 | Thawalama (Gin Ganga) | 1.53 | 🟢 Normal | -0.009 |  |
| 2026-04-29 01:06:16 | Katharagama (Menik Ganga) | -0.02 | 🟢 Normal | -0.009 |  |
| 2026-04-29 00:03:00 | Horowpothana (Yan Oya) | 1.37 | 🟢 Normal | -0.010 |  |
| 2026-04-29 03:03:18 | Moragaswewa (Deduru Oya) | 0.26 | 🟢 Normal | -0.010 |  |
| 2026-04-28 18:04:12 | Thanthirimale (Malwathu Oya) | 2.12 | 🟢 Normal | -0.010 |  |
| 2026-04-29 03:02:26 | Manampitiya (Mahaweli Ganga) | 0.35 | 🟢 Normal | -0.010 |  |
| 2026-04-29 03:02:05 | Giriulla (Maha Oya) | 1.20 | 🟢 Normal | -0.010 |  |
| 2026-04-29 03:01:55 | Panadugama (Nilwala Ganga) | 2.24 | 🟢 Normal | -0.010 |  |
| 2026-04-29 03:00:17 | Padiyathalawa (Maduru Oya) | 0.15 | 🟢 Normal | -0.010 |  |
| 2026-04-29 03:16:11 | Rathnapura (Kalu Ganga) | 0.90 | 🟢 Normal | -0.017 |  |
| 2026-04-29 03:01:39 | Peradeniya (Mahaweli Ganga) | 1.60 | 🟢 Normal | -0.020 |  |
| 2026-04-29 03:02:13 | Ellagawa (Kalu Ganga) | 4.52 | 🟢 Normal | -0.020 |  |
| 2026-04-29 03:01:59 | Deraniyagala (Kelani Ganga) | 0.37 | 🟢 Normal | -0.020 |  |
| 2026-04-29 03:04:12 | Hanwella (Kelani Ganga) | 0.68 | 🟢 Normal | -0.024 |  |
| 2026-04-29 03:09:54 | Badalgama (Maha Oya) | 2.41 | 🟢 Normal | -0.027 |  |
| 2026-04-29 03:02:27 | Dunamale (Aththanagalu Oya) | 1.20 | 🟢 Normal | -0.030 |  |
| 2026-04-29 03:13:38 | Baddegama (Gin Ganga) | 1.28 | 🟢 Normal | -0.036 |  |
| 2026-04-29 03:01:37 | Nawalapitiya (Mahaweli Ganga) | 1.11 | 🟢 Normal | -0.045 |  |
| 2026-04-29 02:08:44 | Putupaula (Kalu Ganga) | 0.61 | 🟢 Normal | -0.093 |  |
| 2026-04-29 03:07:40 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.095 |  |
| 2026-04-29 03:08:18 | Thaldena (Mahaweli Ganga) | 0.27 | 🟢 Normal | -36.000 |  |

## River Water Level Charts by Station

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)