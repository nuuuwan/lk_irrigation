# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--07_14:15:54-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **66,649 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-07 14:15:54 | Thawalama (Gin Ganga) | 1.19 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-02-07 14:10:12 | Urawa (Nilwala Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-02-07 14:10:09 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-02-07 14:09:38 | Panadugama (Nilwala Ganga) | 2.16 | 🟢 Normal | -0.009 |  |
| 2026-02-07 14:09:38 | Rathnapura (Kalu Ganga) | 0.91 | 🟢 Normal | -0.029 |  |
| 2026-02-07 14:09:00 | Baddegama (Gin Ganga) | 1.45 | 🟢 Normal | -0.057 |  |
| 2026-02-07 14:05:55 | Thanamalwila (Kirindi Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-02-07 14:05:38 | Peradeniya (Mahaweli Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-02-07 14:04:55 | Magura (Kalu Ganga) | 1.29 | 🟢 Normal | -0.020 |  |
| 2026-02-07 14:04:40 | Nawalapitiya (Mahaweli Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-02-07 14:04:40 | Glencourse (Kelani Ganga) | 8.57 | 🟢 Normal | -0.028 |  |
| 2026-02-07 14:04:31 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-07 14:04:30 | Holombuwa (Kelani Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-02-07 14:04:28 | Weraganthota (Mahaweli Ganga) | -2.01 | 🟢 Normal | -0.029 |  |
| 2026-02-07 14:04:14 | Yaka Wewa (Ma Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-02-07 14:04:14 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-02-07 14:03:43 | Pitabeddara (Nilwala Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-02-07 14:03:37 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.120 | 🔺 Rising |
| 2026-02-07 14:03:36 | Hanwella (Kelani Ganga) | 0.63 | 🟢 Normal | -0.010 |  |
| 2026-02-07 14:03:36 | Putupaula (Kalu Ganga) | 0.50 | 🟢 Normal | 0.152 | 🔺 Rising |
| 2026-02-07 14:03:22 | Galgamuwa (Mee Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-02-07 14:03:10 | Deraniyagala (Kelani Ganga) | 0.10 | 🟢 Normal | -0.010 |  |
| 2026-02-07 14:03:10 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.22 | 🟢 Normal | -0.052 |  |
| 2026-02-07 14:02:47 | Siyambalanduwa (Heda Oya) | 0.66 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-07 14:02:42 | Dunamale (Aththanagalu Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-02-07 14:02:23 | Manampitiya (Mahaweli Ganga) | 2.09 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-07 14:02:15 | Moraketiya (Walawe Ganga) | 0.85 | 🟢 Normal | -0.010 |  |
| 2026-02-07 14:02:14 | Kithulgala (Kelani Ganga) | 1.50 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-07 14:02:14 | Ellagawa (Kalu Ganga) | 4.30 | 🟢 Normal | -0.010 |  |
| 2026-02-07 14:02:13 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-02-07 14:01:51 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | -0.010 |  |
| 2026-02-07 14:01:44 | Nakkala (Kumbukkan Oya) | 1.07 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-07 14:01:34 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-02-07 14:01:27 | Horowpothana (Yan Oya) | 2.57 | 🟢 Normal | -0.030 |  |
| 2026-02-07 14:01:14 | Padiyathalawa (Maduru Oya) | 1.06 | 🟢 Normal | -0.042 |  |
| 2026-02-07 14:01:05 | Moragaswewa (Deduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-02-07 14:00:49 | Thanthirimale (Malwathu Oya) | 1.87 | 🟢 Normal | -0.011 |  |
| 2026-02-07 14:00:47 | Thaldena (Mahaweli Ganga) | 0.74 | 🟢 Normal | -0.011 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-07 14:03:36 | Putupaula (Kalu Ganga) | 0.50 | 🟢 Normal | 0.152 | 🔺 Rising |
| 2026-02-07 14:03:37 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.120 | 🔺 Rising |
| 2026-02-07 14:02:14 | Kithulgala (Kelani Ganga) | 1.50 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-07 14:02:23 | Manampitiya (Mahaweli Ganga) | 2.09 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-07 14:01:44 | Nakkala (Kumbukkan Oya) | 1.07 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-07 14:02:47 | Siyambalanduwa (Heda Oya) | 0.66 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-07 14:15:54 | Thawalama (Gin Ganga) | 1.19 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-02-07 14:01:34 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-02-07 14:01:05 | Moragaswewa (Deduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-02-07 14:04:40 | Nawalapitiya (Mahaweli Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-02-07 14:04:14 | Yaka Wewa (Ma Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-02-07 14:02:13 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-02-07 14:03:22 | Galgamuwa (Mee Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-02-07 14:03:43 | Pitabeddara (Nilwala Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-02-07 14:02:42 | Dunamale (Aththanagalu Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-02-07 14:10:09 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-02-07 14:04:31 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-07 14:04:30 | Holombuwa (Kelani Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-02-07 14:05:38 | Peradeniya (Mahaweli Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-02-07 14:10:12 | Urawa (Nilwala Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-02-07 14:04:14 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-02-07 14:05:55 | Thanamalwila (Kirindi Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-02-07 14:09:38 | Panadugama (Nilwala Ganga) | 2.16 | 🟢 Normal | -0.009 |  |
| 2026-02-07 14:01:51 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | -0.010 |  |
| 2026-02-07 14:03:36 | Hanwella (Kelani Ganga) | 0.63 | 🟢 Normal | -0.010 |  |
| 2026-02-07 14:02:15 | Moraketiya (Walawe Ganga) | 0.85 | 🟢 Normal | -0.010 |  |
| 2026-02-07 14:03:10 | Deraniyagala (Kelani Ganga) | 0.10 | 🟢 Normal | -0.010 |  |
| 2026-02-07 14:02:14 | Ellagawa (Kalu Ganga) | 4.30 | 🟢 Normal | -0.010 |  |
| 2026-02-07 14:00:49 | Thanthirimale (Malwathu Oya) | 1.87 | 🟢 Normal | -0.011 |  |
| 2026-02-07 14:00:47 | Thaldena (Mahaweli Ganga) | 0.74 | 🟢 Normal | -0.011 |  |
| 2026-02-07 14:04:55 | Magura (Kalu Ganga) | 1.29 | 🟢 Normal | -0.020 |  |
| 2026-02-07 13:11:30 | Thalgahagoda (Nilwala Ganga) | 0.24 | 🟢 Normal | -0.026 |  |
| 2026-02-07 14:04:40 | Glencourse (Kelani Ganga) | 8.57 | 🟢 Normal | -0.028 |  |
| 2026-02-07 14:09:38 | Rathnapura (Kalu Ganga) | 0.91 | 🟢 Normal | -0.029 |  |
| 2026-02-07 14:04:28 | Weraganthota (Mahaweli Ganga) | -2.01 | 🟢 Normal | -0.029 |  |
| 2026-02-07 14:01:27 | Horowpothana (Yan Oya) | 2.57 | 🟢 Normal | -0.030 |  |
| 2026-02-07 14:01:14 | Padiyathalawa (Maduru Oya) | 1.06 | 🟢 Normal | -0.042 |  |
| 2026-02-07 14:03:10 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.22 | 🟢 Normal | -0.052 |  |
| 2026-02-07 14:09:00 | Baddegama (Gin Ganga) | 1.45 | 🟢 Normal | -0.057 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)