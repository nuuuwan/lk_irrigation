# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--21_01:07:45-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **130,631 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **26** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-21 01:07:45 | Thaldena (Mahaweli Ganga) | 0.98 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-04-21 01:07:30 | Glencourse (Kelani Ganga) | 9.97 | 🟢 Normal | 0.719 | 🔺 Rising |
| 2026-04-21 01:07:30 | Baddegama (Gin Ganga) | 1.26 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-04-21 01:06:53 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-04-21 01:05:32 | Magura (Kalu Ganga) | 1.58 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-04-21 01:04:10 | Deraniyagala (Kelani Ganga) | 0.67 | 🟢 Normal | -0.113 |  |
| 2026-04-21 01:04:00 | Thanamalwila (Kirindi Oya) | 4.50 | 🟡 Alert | -0.101 |  |
| 2026-04-21 01:03:58 | Thawalama (Gin Ganga) | 1.66 | 🟢 Normal | -0.029 |  |
| 2026-04-21 01:03:54 | Panadugama (Nilwala Ganga) | 2.61 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-04-21 01:03:53 | Urawa (Nilwala Ganga) | 0.38 | 🟢 Normal | -0.039 |  |
| 2026-04-21 01:03:25 | Hanwella (Kelani Ganga) | 0.66 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-04-21 01:03:25 | Ellagawa (Kalu Ganga) | 4.80 | 🟢 Normal | 0.098 | 🔺 Rising |
| 2026-04-21 01:03:20 | Giriulla (Maha Oya) | 1.13 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-04-21 01:03:11 | Nakkala (Kumbukkan Oya) | 0.88 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-21 01:03:06 | Kithulgala (Kelani Ganga) | 1.52 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-04-21 01:02:52 | Moragaswewa (Deduru Oya) | -0.02 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-21 01:02:27 | Norwood (Kelani Ganga) | 0.90 | 🟢 Normal | -0.021 |  |
| 2026-04-21 01:02:22 | Wellawaya (Kirindi Oya) | 1.04 | 🟢 Normal | -0.039 |  |
| 2026-04-21 01:02:07 | Badalgama (Maha Oya) | 1.78 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-21 01:02:02 | Kuda Oya (Kirindi Oya) | 4.73 | 🟢 Normal | -0.118 |  |
| 2026-04-21 01:01:56 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | -0.010 |  |
| 2026-04-21 01:01:34 | Nawalapitiya (Mahaweli Ganga) | 0.87 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-21 01:01:31 | Manampitiya (Mahaweli Ganga) | 0.38 | 🟢 Normal | -0.020 |  |
| 2026-04-21 01:00:50 | Horowpothana (Yan Oya) | 1.41 | 🟢 Normal | 0.000 |  |
| 2026-04-21 01:00:11 | Peradeniya (Mahaweli Ganga) | 2.90 | 🟢 Normal | -0.086 |  |
| 2026-04-21 00:33:54 | Katharagama (Menik Ganga) | 0.05 | 🟢 Normal | 0.028 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-21 01:04:00 | Thanamalwila (Kirindi Oya) | 4.50 | 🟡 Alert | -0.101 |  |
| 2026-04-21 01:07:30 | Glencourse (Kelani Ganga) | 9.97 | 🟢 Normal | 0.719 | 🔺 Rising |
| 2026-04-21 00:10:18 | Rathnapura (Kalu Ganga) | 1.72 | 🟢 Normal | 0.624 | 🔺 Rising |
| 2026-04-21 00:05:55 | Holombuwa (Kelani Ganga) | 1.10 | 🟢 Normal | 0.322 | 🔺 Rising |
| 2026-04-20 18:03:54 | Weraganthota (Mahaweli Ganga) | -2.98 | 🟢 Normal | 0.129 | 🔺 Rising |
| 2026-04-21 01:03:25 | Ellagawa (Kalu Ganga) | 4.80 | 🟢 Normal | 0.098 | 🔺 Rising |
| 2026-04-21 01:03:20 | Giriulla (Maha Oya) | 1.13 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-04-21 01:03:06 | Kithulgala (Kelani Ganga) | 1.52 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-04-21 00:05:45 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.10 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2026-04-21 01:03:54 | Panadugama (Nilwala Ganga) | 2.61 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-04-21 01:05:32 | Magura (Kalu Ganga) | 1.58 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-04-21 01:03:25 | Hanwella (Kelani Ganga) | 0.66 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-04-21 01:06:53 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-04-21 01:03:11 | Nakkala (Kumbukkan Oya) | 0.88 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-21 00:33:54 | Katharagama (Menik Ganga) | 0.05 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-04-20 18:11:39 | Galgamuwa (Mee Oya) | 0.28 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-04-21 00:02:36 | Dunamale (Aththanagalu Oya) | 0.62 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-21 01:01:34 | Nawalapitiya (Mahaweli Ganga) | 0.87 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-21 01:02:07 | Badalgama (Maha Oya) | 1.78 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-21 01:02:52 | Moragaswewa (Deduru Oya) | -0.02 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-21 01:07:45 | Thaldena (Mahaweli Ganga) | 0.98 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-04-21 01:07:30 | Baddegama (Gin Ganga) | 1.26 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-04-21 00:02:00 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-21 01:00:50 | Horowpothana (Yan Oya) | 1.41 | 🟢 Normal | 0.000 |  |
| 2026-04-20 23:02:37 | Pitabeddara (Nilwala Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-04-21 00:01:15 | Padiyathalawa (Maduru Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-04-21 00:02:21 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-04-21 01:01:56 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | -0.010 |  |
| 2026-04-20 18:01:44 | Thanthirimale (Malwathu Oya) | 1.25 | 🟢 Normal | -0.010 |  |
| 2026-04-21 01:01:31 | Manampitiya (Mahaweli Ganga) | 0.38 | 🟢 Normal | -0.020 |  |
| 2026-04-21 01:02:27 | Norwood (Kelani Ganga) | 0.90 | 🟢 Normal | -0.021 |  |
| 2026-04-21 01:03:58 | Thawalama (Gin Ganga) | 1.66 | 🟢 Normal | -0.029 |  |
| 2026-04-21 01:02:22 | Wellawaya (Kirindi Oya) | 1.04 | 🟢 Normal | -0.039 |  |
| 2026-04-21 01:03:53 | Urawa (Nilwala Ganga) | 0.38 | 🟢 Normal | -0.039 |  |
| 2026-04-20 23:02:34 | Moraketiya (Walawe Ganga) | 1.90 | 🟢 Normal | -0.050 |  |
| 2026-04-20 23:33:11 | Putupaula (Kalu Ganga) | 0.29 | 🟢 Normal | -0.077 |  |
| 2026-04-21 01:00:11 | Peradeniya (Mahaweli Ganga) | 2.90 | 🟢 Normal | -0.086 |  |
| 2026-04-21 01:04:10 | Deraniyagala (Kelani Ganga) | 0.67 | 🟢 Normal | -0.113 |  |
| 2026-04-21 01:02:02 | Kuda Oya (Kirindi Oya) | 4.73 | 🟢 Normal | -0.118 |  |

## River Water Level Charts by Station

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)