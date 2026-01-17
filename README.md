# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--17_13:13:01-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **48,072 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-17 13:13:01 | Glencourse (Kelani Ganga) | 8.50 | 🟢 Normal | -0.009 |  |
| 2026-01-17 13:13:01 | Dunamale (Aththanagalu Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-01-17 13:11:44 | Panadugama (Nilwala Ganga) | 2.19 | 🟢 Normal | 0.000 |  |
| 2026-01-17 13:09:35 | Deraniyagala (Kelani Ganga) | 0.10 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-01-17 13:07:32 | Badalgama (Maha Oya) | 1.94 | 🟢 Normal | 0.000 |  |
| 2026-01-17 13:07:13 | Thawalama (Gin Ganga) | 1.23 | 🟢 Normal | -0.009 |  |
| 2026-01-17 13:07:00 | Moragaswewa (Deduru Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-01-17 13:06:32 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-01-17 13:06:19 | Peradeniya (Mahaweli Ganga) | 1.46 | 🟢 Normal | -0.138 |  |
| 2026-01-17 13:06:18 | Yaka Wewa (Ma Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-01-17 13:06:06 | Horowpothana (Yan Oya) | 1.53 | 🟢 Normal | 0.000 |  |
| 2026-01-17 13:05:15 | Pitabeddara (Nilwala Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-01-17 13:04:49 | Thanamalwila (Kirindi Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-01-17 13:04:23 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2026-01-17 13:03:35 | Padiyathalawa (Maduru Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-01-17 13:03:35 | Hanwella (Kelani Ganga) | 0.38 | 🟢 Normal | -0.020 |  |
| 2026-01-17 13:03:31 | Giriulla (Maha Oya) | 0.86 | 🟢 Normal | -0.010 |  |
| 2026-01-17 13:03:30 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.56 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-01-17 13:03:30 | Rathnapura (Kalu Ganga) | 0.54 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-17 13:03:13 | Norwood (Kelani Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-01-17 13:03:05 | Baddegama (Gin Ganga) | 0.74 | 🟢 Normal | -0.010 |  |
| 2026-01-17 13:02:58 | Kithulgala (Kelani Ganga) | 1.47 | 🟢 Normal | -0.031 |  |
| 2026-01-17 13:02:57 | Putupaula (Kalu Ganga) | 0.65 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2026-01-17 13:02:56 | Katharagama (Menik Ganga) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-01-17 13:02:54 | Kuda Oya (Kirindi Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-01-17 13:02:49 | Thanthirimale (Malwathu Oya) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-01-17 13:02:39 | Urawa (Nilwala Ganga) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-01-17 13:02:33 | Nakkala (Kumbukkan Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-01-17 13:02:24 | Nawalapitiya (Mahaweli Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-01-17 13:01:55 | Thalgahagoda (Nilwala Ganga) | 0.31 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-01-17 13:01:45 | Weraganthota (Mahaweli Ganga) | -1.84 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-01-17 13:01:43 | Galgamuwa (Mee Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-01-17 13:01:36 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-01-17 13:01:28 | Ellagawa (Kalu Ganga) | 4.00 | 🟢 Normal | -0.010 |  |
| 2026-01-17 13:01:23 | Manampitiya (Mahaweli Ganga) | 1.29 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-01-17 13:01:08 | Thaldena (Mahaweli Ganga) | 0.64 | 🟢 Normal | 0.139 | 🔺 Rising |
| 2026-01-17 13:01:07 | Magura (Kalu Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-01-17 13:00:36 | Siyambalanduwa (Heda Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-01-17 13:00:16 | Moraketiya (Walawe Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-01-17 12:45:50 | Horowpothana (Yan Oya) | 1.53 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-17 13:01:08 | Thaldena (Mahaweli Ganga) | 0.64 | 🟢 Normal | 0.139 | 🔺 Rising |
| 2026-01-17 13:02:57 | Putupaula (Kalu Ganga) | 0.65 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2026-01-17 13:04:23 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2026-01-17 13:01:45 | Weraganthota (Mahaweli Ganga) | -1.84 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-01-17 13:03:30 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.56 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-01-17 13:01:23 | Manampitiya (Mahaweli Ganga) | 1.29 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-01-17 13:01:55 | Thalgahagoda (Nilwala Ganga) | 0.31 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-01-17 13:03:30 | Rathnapura (Kalu Ganga) | 0.54 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-17 13:09:35 | Deraniyagala (Kelani Ganga) | 0.10 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-01-17 13:01:36 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-01-17 13:02:33 | Nakkala (Kumbukkan Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-01-17 13:07:00 | Moragaswewa (Deduru Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-01-17 13:02:24 | Nawalapitiya (Mahaweli Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-01-17 13:06:18 | Yaka Wewa (Ma Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-01-17 13:06:06 | Horowpothana (Yan Oya) | 1.53 | 🟢 Normal | 0.000 |  |
| 2026-01-17 13:01:43 | Galgamuwa (Mee Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-01-17 13:01:07 | Magura (Kalu Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-01-17 13:05:15 | Pitabeddara (Nilwala Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-01-17 13:03:13 | Norwood (Kelani Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-01-17 13:11:44 | Panadugama (Nilwala Ganga) | 2.19 | 🟢 Normal | 0.000 |  |
| 2026-01-17 13:03:35 | Padiyathalawa (Maduru Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-01-17 13:00:16 | Moraketiya (Walawe Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-01-17 13:00:36 | Siyambalanduwa (Heda Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-01-17 13:13:01 | Dunamale (Aththanagalu Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-01-17 13:02:56 | Katharagama (Menik Ganga) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-01-17 13:07:32 | Badalgama (Maha Oya) | 1.94 | 🟢 Normal | 0.000 |  |
| 2026-01-17 13:06:32 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-01-17 13:02:49 | Thanthirimale (Malwathu Oya) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-01-17 13:02:39 | Urawa (Nilwala Ganga) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-01-17 13:02:54 | Kuda Oya (Kirindi Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-01-17 13:04:49 | Thanamalwila (Kirindi Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-01-17 13:13:01 | Glencourse (Kelani Ganga) | 8.50 | 🟢 Normal | -0.009 |  |
| 2026-01-17 13:07:13 | Thawalama (Gin Ganga) | 1.23 | 🟢 Normal | -0.009 |  |
| 2026-01-17 13:03:31 | Giriulla (Maha Oya) | 0.86 | 🟢 Normal | -0.010 |  |
| 2026-01-17 13:01:28 | Ellagawa (Kalu Ganga) | 4.00 | 🟢 Normal | -0.010 |  |
| 2026-01-17 13:03:05 | Baddegama (Gin Ganga) | 0.74 | 🟢 Normal | -0.010 |  |
| 2026-01-17 13:03:35 | Hanwella (Kelani Ganga) | 0.38 | 🟢 Normal | -0.020 |  |
| 2026-01-17 13:02:58 | Kithulgala (Kelani Ganga) | 1.47 | 🟢 Normal | -0.031 |  |
| 2026-01-17 13:06:19 | Peradeniya (Mahaweli Ganga) | 1.46 | 🟢 Normal | -0.138 |  |

## River Water Level Charts by Station

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

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

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

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

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)