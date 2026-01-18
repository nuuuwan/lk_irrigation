# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--18_12:11:59-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **48,942 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-18 12:11:59 | Thalgahagoda (Nilwala Ganga) | 0.28 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-01-18 12:09:43 | Moragaswewa (Deduru Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-01-18 12:09:21 | Panadugama (Nilwala Ganga) | 2.14 | 🟢 Normal | 0.000 |  |
| 2026-01-18 12:08:10 | Hanwella (Kelani Ganga) | 0.44 | 🟢 Normal | -0.019 |  |
| 2026-01-18 12:07:15 | Padiyathalawa (Maduru Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-01-18 12:06:58 | Thanamalwila (Kirindi Oya) | 0.77 | 🟢 Normal | -0.010 |  |
| 2026-01-18 12:06:47 | Kuda Oya (Kirindi Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-01-18 12:06:07 | Urawa (Nilwala Ganga) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-01-18 12:06:03 | Glencourse (Kelani Ganga) | 8.57 | 🟢 Normal | 0.000 |  |
| 2026-01-18 12:05:34 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | -0.009 |  |
| 2026-01-18 12:04:59 | Baddegama (Gin Ganga) | 1.14 | 🟢 Normal | -0.064 |  |
| 2026-01-18 12:04:57 | Putupaula (Kalu Ganga) | 0.50 | 🟢 Normal | 0.077 | 🔺 Rising |
| 2026-01-18 12:04:45 | Thawalama (Gin Ganga) | 1.04 | 🟢 Normal | -0.021 |  |
| 2026-01-18 12:04:41 | Dunamale (Aththanagalu Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-01-18 12:04:26 | Magura (Kalu Ganga) | 0.83 | 🟢 Normal | -0.010 |  |
| 2026-01-18 12:04:22 | Rathnapura (Kalu Ganga) | 0.50 | 🟢 Normal | -0.031 |  |
| 2026-01-18 12:04:19 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.40 | 🟢 Normal | -0.032 |  |
| 2026-01-18 12:04:18 | Norwood (Kelani Ganga) | 0.46 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-18 12:04:17 | Galgamuwa (Mee Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-01-18 12:04:02 | Yaka Wewa (Ma Oya) | 0.70 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-18 12:03:50 | Holombuwa (Kelani Ganga) | 0.39 | 🟢 Normal | -0.010 |  |
| 2026-01-18 12:03:41 | Siyambalanduwa (Heda Oya) | 0.72 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-18 12:03:28 | Giriulla (Maha Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-01-18 12:03:12 | Deraniyagala (Kelani Ganga) | 0.22 | 🟢 Normal | -0.079 |  |
| 2026-01-18 12:02:38 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-01-18 12:02:37 | Ellagawa (Kalu Ganga) | 3.95 | 🟢 Normal | 0.000 |  |
| 2026-01-18 12:02:35 | Thaldena (Mahaweli Ganga) | 0.57 | 🟢 Normal | -0.011 |  |
| 2026-01-18 12:02:26 | Weraganthota (Mahaweli Ganga) | -2.00 | 🟢 Normal | -0.146 |  |
| 2026-01-18 12:02:17 | Katharagama (Menik Ganga) | 0.02 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-18 12:02:11 | Badalgama (Maha Oya) | 1.91 | 🟢 Normal | 0.000 |  |
| 2026-01-18 12:02:11 | Moragaswewa (Deduru Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-01-18 12:01:48 | Kithulgala (Kelani Ganga) | 1.48 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-01-18 12:01:41 | Thanthirimale (Malwathu Oya) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-01-18 12:01:35 | Nawalapitiya (Mahaweli Ganga) | 0.71 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-18 12:01:13 | Pitabeddara (Nilwala Ganga) | 0.37 | 🟢 Normal | -0.358 |  |
| 2026-01-18 12:01:10 | Peradeniya (Mahaweli Ganga) | 1.52 | 🟢 Normal | -0.010 |  |
| 2026-01-18 12:01:09 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.083 | 🔺 Rising |
| 2026-01-18 12:00:31 | Nakkala (Kumbukkan Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-01-18 12:00:13 | Manampitiya (Mahaweli Ganga) | 1.26 | 🟢 Normal | 0.012 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-18 12:01:09 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.083 | 🔺 Rising |
| 2026-01-18 12:04:57 | Putupaula (Kalu Ganga) | 0.50 | 🟢 Normal | 0.077 | 🔺 Rising |
| 2026-01-18 12:01:48 | Kithulgala (Kelani Ganga) | 1.48 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-01-18 12:11:59 | Thalgahagoda (Nilwala Ganga) | 0.28 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-01-18 12:00:13 | Manampitiya (Mahaweli Ganga) | 1.26 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-01-18 12:02:17 | Katharagama (Menik Ganga) | 0.02 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-18 12:01:35 | Nawalapitiya (Mahaweli Ganga) | 0.71 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-18 12:04:18 | Norwood (Kelani Ganga) | 0.46 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-18 12:03:41 | Siyambalanduwa (Heda Oya) | 0.72 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-18 12:04:02 | Yaka Wewa (Ma Oya) | 0.70 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-18 12:02:38 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-01-18 12:00:31 | Nakkala (Kumbukkan Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-01-18 12:09:43 | Moragaswewa (Deduru Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-01-18 12:03:28 | Giriulla (Maha Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-01-18 12:04:17 | Galgamuwa (Mee Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-01-18 12:02:37 | Ellagawa (Kalu Ganga) | 3.95 | 🟢 Normal | 0.000 |  |
| 2026-01-18 12:09:21 | Panadugama (Nilwala Ganga) | 2.14 | 🟢 Normal | 0.000 |  |
| 2026-01-18 12:07:15 | Padiyathalawa (Maduru Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-01-18 12:06:03 | Glencourse (Kelani Ganga) | 8.57 | 🟢 Normal | 0.000 |  |
| 2026-01-18 12:04:41 | Dunamale (Aththanagalu Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-01-18 12:02:11 | Badalgama (Maha Oya) | 1.91 | 🟢 Normal | 0.000 |  |
| 2026-01-18 12:01:41 | Thanthirimale (Malwathu Oya) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-01-18 12:06:07 | Urawa (Nilwala Ganga) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-01-18 12:06:47 | Kuda Oya (Kirindi Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-01-18 12:05:34 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | -0.009 |  |
| 2026-01-18 12:06:58 | Thanamalwila (Kirindi Oya) | 0.77 | 🟢 Normal | -0.010 |  |
| 2026-01-18 12:04:26 | Magura (Kalu Ganga) | 0.83 | 🟢 Normal | -0.010 |  |
| 2026-01-18 12:03:50 | Holombuwa (Kelani Ganga) | 0.39 | 🟢 Normal | -0.010 |  |
| 2026-01-18 12:01:10 | Peradeniya (Mahaweli Ganga) | 1.52 | 🟢 Normal | -0.010 |  |
| 2026-01-18 12:02:35 | Thaldena (Mahaweli Ganga) | 0.57 | 🟢 Normal | -0.011 |  |
| 2026-01-18 11:01:05 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | -0.016 |  |
| 2026-01-18 12:08:10 | Hanwella (Kelani Ganga) | 0.44 | 🟢 Normal | -0.019 |  |
| 2026-01-18 12:04:45 | Thawalama (Gin Ganga) | 1.04 | 🟢 Normal | -0.021 |  |
| 2026-01-18 12:04:22 | Rathnapura (Kalu Ganga) | 0.50 | 🟢 Normal | -0.031 |  |
| 2026-01-18 12:04:19 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.40 | 🟢 Normal | -0.032 |  |
| 2026-01-18 12:04:59 | Baddegama (Gin Ganga) | 1.14 | 🟢 Normal | -0.064 |  |
| 2026-01-18 12:03:12 | Deraniyagala (Kelani Ganga) | 0.22 | 🟢 Normal | -0.079 |  |
| 2026-01-18 12:02:26 | Weraganthota (Mahaweli Ganga) | -2.00 | 🟢 Normal | -0.146 |  |
| 2026-01-18 12:01:13 | Pitabeddara (Nilwala Ganga) | 0.37 | 🟢 Normal | -0.358 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)