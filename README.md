# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--18_09:17:24-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **48,818 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-18 09:17:24 | Horowpothana (Yan Oya) | 1.31 | 🟢 Normal | -0.041 |  |
| 2026-01-18 09:16:27 | Moragaswewa (Deduru Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-01-18 09:10:39 | Ellagawa (Kalu Ganga) | 3.96 | 🟢 Normal | 0.000 |  |
| 2026-01-18 09:10:21 | Panadugama (Nilwala Ganga) | 2.15 | 🟢 Normal | -0.011 |  |
| 2026-01-18 09:09:33 | Glencourse (Kelani Ganga) | 8.61 | 🟢 Normal | -0.009 |  |
| 2026-01-18 09:08:04 | Pitabeddara (Nilwala Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-01-18 09:07:45 | Baddegama (Gin Ganga) | 1.18 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-18 09:07:42 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-01-18 09:06:10 | Thawalama (Gin Ganga) | 1.08 | 🟢 Normal | -0.010 |  |
| 2026-01-18 09:05:09 | Galgamuwa (Mee Oya) | 0.10 | 🟢 Normal | -0.010 |  |
| 2026-01-18 09:04:59 | Siyambalanduwa (Heda Oya) | 0.70 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-18 09:04:52 | Thanamalwila (Kirindi Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-01-18 09:04:29 | Putupaula (Kalu Ganga) | 0.40 | 🟢 Normal | -0.066 |  |
| 2026-01-18 09:04:28 | Padiyathalawa (Maduru Oya) | 0.73 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-01-18 09:04:25 | Dunamale (Aththanagalu Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-01-18 09:04:18 | Rathnapura (Kalu Ganga) | 0.56 | 🟢 Normal | -0.010 |  |
| 2026-01-18 09:04:15 | Giriulla (Maha Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-01-18 09:03:36 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-01-18 09:03:26 | Deraniyagala (Kelani Ganga) | 0.27 | 🟢 Normal | 0.097 | 🔺 Rising |
| 2026-01-18 09:03:20 | Norwood (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-01-18 09:03:14 | Hanwella (Kelani Ganga) | 0.47 | 🟢 Normal | -0.010 |  |
| 2026-01-18 09:03:13 | Kithulgala (Kelani Ganga) | 1.20 | 🟢 Normal | -0.299 |  |
| 2026-01-18 09:03:09 | Urawa (Nilwala Ganga) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-01-18 09:02:39 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.50 | 🟢 Normal | -0.046 |  |
| 2026-01-18 09:02:34 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-01-18 09:02:21 | Badalgama (Maha Oya) | 1.91 | 🟢 Normal | 0.000 |  |
| 2026-01-18 09:02:16 | Katharagama (Menik Ganga) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-01-18 09:02:15 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-01-18 09:02:06 | Peradeniya (Mahaweli Ganga) | 1.42 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2026-01-18 09:01:52 | Yaka Wewa (Ma Oya) | 0.68 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-18 09:01:49 | Manampitiya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-01-18 09:01:35 | Thanthirimale (Malwathu Oya) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-01-18 09:01:25 | Magura (Kalu Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-01-18 09:01:10 | Kuda Oya (Kirindi Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-01-18 09:01:04 | Nakkala (Kumbukkan Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-01-18 09:01:02 | Thaldena (Mahaweli Ganga) | 0.60 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-01-18 09:01:01 | Weraganthota (Mahaweli Ganga) | -1.80 | 🟢 Normal | 0.000 |  |
| 2026-01-18 09:00:46 | Nawalapitiya (Mahaweli Ganga) | 0.69 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-18 08:32:33 | Moragaswewa (Deduru Oya) | 0.46 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-18 09:03:26 | Deraniyagala (Kelani Ganga) | 0.27 | 🟢 Normal | 0.097 | 🔺 Rising |
| 2026-01-18 09:02:06 | Peradeniya (Mahaweli Ganga) | 1.42 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2026-01-18 09:01:02 | Thaldena (Mahaweli Ganga) | 0.60 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-01-18 09:01:49 | Manampitiya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-01-18 09:01:52 | Yaka Wewa (Ma Oya) | 0.68 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-18 09:00:46 | Nawalapitiya (Mahaweli Ganga) | 0.69 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-18 09:04:28 | Padiyathalawa (Maduru Oya) | 0.73 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-01-18 09:07:45 | Baddegama (Gin Ganga) | 1.18 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-18 09:04:59 | Siyambalanduwa (Heda Oya) | 0.70 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-18 09:01:01 | Weraganthota (Mahaweli Ganga) | -1.80 | 🟢 Normal | 0.000 |  |
| 2026-01-18 09:02:15 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-01-18 09:01:04 | Nakkala (Kumbukkan Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-01-18 09:16:27 | Moragaswewa (Deduru Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-01-18 09:04:15 | Giriulla (Maha Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-01-18 09:01:25 | Magura (Kalu Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-01-18 09:08:04 | Pitabeddara (Nilwala Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-01-18 09:03:20 | Norwood (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-01-18 09:10:39 | Ellagawa (Kalu Ganga) | 3.96 | 🟢 Normal | 0.000 |  |
| 2026-01-18 09:03:36 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-01-18 09:02:34 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-01-18 09:04:25 | Dunamale (Aththanagalu Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-01-18 09:02:16 | Katharagama (Menik Ganga) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-01-18 09:02:21 | Badalgama (Maha Oya) | 1.91 | 🟢 Normal | 0.000 |  |
| 2026-01-18 09:07:42 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-01-18 09:01:35 | Thanthirimale (Malwathu Oya) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-01-18 09:03:09 | Urawa (Nilwala Ganga) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-01-18 09:01:10 | Kuda Oya (Kirindi Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-01-18 09:04:52 | Thanamalwila (Kirindi Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-01-18 09:09:33 | Glencourse (Kelani Ganga) | 8.61 | 🟢 Normal | -0.009 |  |
| 2026-01-18 09:06:10 | Thawalama (Gin Ganga) | 1.08 | 🟢 Normal | -0.010 |  |
| 2026-01-18 09:05:09 | Galgamuwa (Mee Oya) | 0.10 | 🟢 Normal | -0.010 |  |
| 2026-01-18 09:03:14 | Hanwella (Kelani Ganga) | 0.47 | 🟢 Normal | -0.010 |  |
| 2026-01-18 09:04:18 | Rathnapura (Kalu Ganga) | 0.56 | 🟢 Normal | -0.010 |  |
| 2026-01-18 09:10:21 | Panadugama (Nilwala Ganga) | 2.15 | 🟢 Normal | -0.011 |  |
| 2026-01-18 09:17:24 | Horowpothana (Yan Oya) | 1.31 | 🟢 Normal | -0.041 |  |
| 2026-01-18 09:02:39 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.50 | 🟢 Normal | -0.046 |  |
| 2026-01-18 09:04:29 | Putupaula (Kalu Ganga) | 0.40 | 🟢 Normal | -0.066 |  |
| 2026-01-18 08:21:45 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | -0.075 |  |
| 2026-01-18 09:03:13 | Kithulgala (Kelani Ganga) | 1.20 | 🟢 Normal | -0.299 |  |

## River Water Level Charts by Station

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

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

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)