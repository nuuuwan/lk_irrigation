# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--13_12:05:11-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **71,911 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-13 12:05:11 | Katharagama (Menik Ganga) | -0.05 | 🟢 Normal | -0.010 |  |
| 2026-02-13 12:04:56 | Moragaswewa (Deduru Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-02-13 12:04:38 | Rathnapura (Kalu Ganga) | 1.23 | 🟢 Normal | -0.071 |  |
| 2026-02-13 12:04:31 | Ellagawa (Kalu Ganga) | 4.42 | 🟢 Normal | 0.116 | 🔺 Rising |
| 2026-02-13 12:04:27 | Holombuwa (Kelani Ganga) | 0.31 | 🟢 Normal | -0.010 |  |
| 2026-02-13 12:04:21 | Magura (Kalu Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-02-13 12:04:11 | Pitabeddara (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-02-13 12:04:11 | Badalgama (Maha Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-02-13 12:04:05 | Putupaula (Kalu Ganga) | 0.50 | 🟢 Normal | 0.114 | 🔺 Rising |
| 2026-02-13 12:04:01 | Giriulla (Maha Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-02-13 12:03:44 | Baddegama (Gin Ganga) | 1.42 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-02-13 12:03:42 | Thawalama (Gin Ganga) | 1.37 | 🟢 Normal | -0.021 |  |
| 2026-02-13 12:03:24 | Thaldena (Mahaweli Ganga) | 0.53 | 🟢 Normal | -0.029 |  |
| 2026-02-13 12:03:17 | Hanwella (Kelani Ganga) | 0.42 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-13 12:02:59 | Norwood (Kelani Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-02-13 12:02:50 | Padiyathalawa (Maduru Oya) | 1.30 | 🟢 Normal | -0.010 |  |
| 2026-02-13 12:02:50 | Kuda Oya (Kirindi Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-02-13 12:02:40 | Nawalapitiya (Mahaweli Ganga) | 0.77 | 🟢 Normal | -0.020 |  |
| 2026-02-13 12:02:37 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.80 | 🟢 Normal | -0.081 |  |
| 2026-02-13 12:02:33 | Glencourse (Kelani Ganga) | 8.41 | 🟢 Normal | -0.042 |  |
| 2026-02-13 12:02:16 | Deraniyagala (Kelani Ganga) | 0.23 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-13 12:02:08 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-02-13 12:02:04 | Horowpothana (Yan Oya) | 1.33 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-13 12:02:03 | Dunamale (Aththanagalu Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-02-13 12:02:01 | Dunamale (Aththanagalu Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-02-13 12:02:00 | Peradeniya (Mahaweli Ganga) | 1.48 | 🟢 Normal | -0.069 |  |
| 2026-02-13 12:01:25 | Kithulgala (Kelani Ganga) | 1.46 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-13 12:01:12 | Wellawaya (Kirindi Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-02-13 12:00:58 | Moraketiya (Walawe Ganga) | 1.01 | 🟢 Normal | -0.042 |  |
| 2026-02-13 12:00:50 | Weraganthota (Mahaweli Ganga) | -2.00 | 🟢 Normal | -0.204 |  |
| 2026-02-13 12:00:32 | Thanthirimale (Malwathu Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-02-13 12:00:28 | Nakkala (Kumbukkan Oya) | 0.93 | 🟢 Normal | -0.030 |  |
| 2026-02-13 12:00:11 | Manampitiya (Mahaweli Ganga) | 0.87 | 🟢 Normal | 0.095 | 🔺 Rising |
| 2026-02-13 11:17:30 | Panadugama (Nilwala Ganga) | 2.11 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-02-13 11:15:48 | Urawa (Nilwala Ganga) | 0.25 | 🟢 Normal | -0.010 |  |
| 2026-02-13 11:15:03 | Magura (Kalu Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-02-13 11:09:57 | Thalgahagoda (Nilwala Ganga) | 0.34 | 🟢 Normal | -0.009 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-13 12:04:31 | Ellagawa (Kalu Ganga) | 4.42 | 🟢 Normal | 0.116 | 🔺 Rising |
| 2026-02-13 12:04:05 | Putupaula (Kalu Ganga) | 0.50 | 🟢 Normal | 0.114 | 🔺 Rising |
| 2026-02-13 12:00:11 | Manampitiya (Mahaweli Ganga) | 0.87 | 🟢 Normal | 0.095 | 🔺 Rising |
| 2026-02-13 12:03:44 | Baddegama (Gin Ganga) | 1.42 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-02-13 12:02:16 | Deraniyagala (Kelani Ganga) | 0.23 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-13 11:17:30 | Panadugama (Nilwala Ganga) | 2.11 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-02-13 12:01:25 | Kithulgala (Kelani Ganga) | 1.46 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-13 12:03:17 | Hanwella (Kelani Ganga) | 0.42 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-13 12:02:04 | Horowpothana (Yan Oya) | 1.33 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-13 12:01:12 | Wellawaya (Kirindi Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-02-13 12:04:56 | Moragaswewa (Deduru Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-02-13 12:04:01 | Giriulla (Maha Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-02-13 12:04:21 | Magura (Kalu Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-02-13 12:04:11 | Pitabeddara (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-02-13 12:02:59 | Norwood (Kelani Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-02-13 12:02:08 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-02-13 11:02:16 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-02-13 12:02:03 | Dunamale (Aththanagalu Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-02-13 12:04:11 | Badalgama (Maha Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-02-13 12:00:32 | Thanthirimale (Malwathu Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-02-13 12:02:50 | Kuda Oya (Kirindi Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-02-13 11:02:04 | Thanamalwila (Kirindi Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-02-13 11:02:15 | Yaka Wewa (Ma Oya) | 0.74 | 🟢 Normal | -0.005 |  |
| 2026-02-13 11:09:57 | Thalgahagoda (Nilwala Ganga) | 0.34 | 🟢 Normal | -0.009 |  |
| 2026-02-13 12:05:11 | Katharagama (Menik Ganga) | -0.05 | 🟢 Normal | -0.010 |  |
| 2026-02-13 11:15:48 | Urawa (Nilwala Ganga) | 0.25 | 🟢 Normal | -0.010 |  |
| 2026-02-13 12:04:27 | Holombuwa (Kelani Ganga) | 0.31 | 🟢 Normal | -0.010 |  |
| 2026-02-13 12:02:50 | Padiyathalawa (Maduru Oya) | 1.30 | 🟢 Normal | -0.010 |  |
| 2026-02-13 11:08:30 | Galgamuwa (Mee Oya) | 0.10 | 🟢 Normal | -0.011 |  |
| 2026-02-13 12:02:40 | Nawalapitiya (Mahaweli Ganga) | 0.77 | 🟢 Normal | -0.020 |  |
| 2026-02-13 12:03:42 | Thawalama (Gin Ganga) | 1.37 | 🟢 Normal | -0.021 |  |
| 2026-02-13 12:03:24 | Thaldena (Mahaweli Ganga) | 0.53 | 🟢 Normal | -0.029 |  |
| 2026-02-13 12:00:28 | Nakkala (Kumbukkan Oya) | 0.93 | 🟢 Normal | -0.030 |  |
| 2026-02-13 12:00:58 | Moraketiya (Walawe Ganga) | 1.01 | 🟢 Normal | -0.042 |  |
| 2026-02-13 12:02:33 | Glencourse (Kelani Ganga) | 8.41 | 🟢 Normal | -0.042 |  |
| 2026-02-13 12:02:00 | Peradeniya (Mahaweli Ganga) | 1.48 | 🟢 Normal | -0.069 |  |
| 2026-02-13 12:04:38 | Rathnapura (Kalu Ganga) | 1.23 | 🟢 Normal | -0.071 |  |
| 2026-02-13 12:02:37 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.80 | 🟢 Normal | -0.081 |  |
| 2026-02-13 12:00:50 | Weraganthota (Mahaweli Ganga) | -2.00 | 🟢 Normal | -0.204 |  |

## River Water Level Charts by Station

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

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

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)