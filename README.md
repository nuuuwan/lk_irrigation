# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--18_06:13:10-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **76,140 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-18 06:13:10 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-02-18 06:11:42 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.128 |  |
| 2026-02-18 06:10:09 | Rathnapura (Kalu Ganga) | 0.53 | 🟢 Normal | 0.212 | 🔺 Rising |
| 2026-02-18 06:09:10 | Baddegama (Gin Ganga) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-02-18 06:09:06 | Manampitiya (Mahaweli Ganga) | 1.30 | 🟢 Normal | 0.104 | 🔺 Rising |
| 2026-02-18 06:08:55 | Peradeniya (Mahaweli Ganga) | 1.17 | 🟢 Normal | -0.121 |  |
| 2026-02-18 06:08:38 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-02-18 06:08:37 | Magura (Kalu Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-02-18 06:07:14 | Panadugama (Nilwala Ganga) | 1.95 | 🟢 Normal | -0.010 |  |
| 2026-02-18 06:06:55 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | -0.010 |  |
| 2026-02-18 06:05:20 | Horowpothana (Yan Oya) | 1.38 | 🟢 Normal | -0.010 |  |
| 2026-02-18 06:05:11 | Deraniyagala (Kelani Ganga) | 0.14 | 🟢 Normal | 3.892 | 🔺 Rising |
| 2026-02-18 06:04:52 | Pitabeddara (Nilwala Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-02-18 06:04:44 | Weraganthota (Mahaweli Ganga) | -2.30 | 🟢 Normal | 0.007 | 🔺 Rising |
| 2026-02-18 06:04:34 | Deraniyagala (Kelani Ganga) | 0.10 | 🟢 Normal | 3.892 | 🔺 Rising |
| 2026-02-18 06:04:30 | Thanamalwila (Kirindi Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-02-18 06:04:07 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-02-18 06:04:03 | Moraketiya (Walawe Ganga) | 0.89 | 🟢 Normal | -0.011 |  |
| 2026-02-18 06:03:13 | Ellagawa (Kalu Ganga) | 3.85 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-18 06:03:08 | Giriulla (Maha Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-02-18 06:03:08 | Nakkala (Kumbukkan Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-02-18 06:03:06 | Moragaswewa (Deduru Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-02-18 06:02:53 | Thaldena (Mahaweli Ganga) | 0.54 | 🟢 Normal | -0.010 |  |
| 2026-02-18 06:02:47 | Glencourse (Kelani Ganga) | 8.60 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-02-18 06:02:25 | Hanwella (Kelani Ganga) | 0.31 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-18 06:02:25 | Dunamale (Aththanagalu Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-02-18 06:02:00 | Thawalama (Gin Ganga) | 1.00 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-18 06:01:46 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-02-18 06:01:39 | Nawalapitiya (Mahaweli Ganga) | 0.62 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-18 06:01:37 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | 0.210 | 🔺 Rising |
| 2026-02-18 06:01:32 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.70 | 🟢 Normal | -0.040 |  |
| 2026-02-18 06:01:30 | Yaka Wewa (Ma Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-02-18 06:01:30 | Putupaula (Kalu Ganga) | 0.69 | 🟢 Normal | -0.073 |  |
| 2026-02-18 06:01:25 | Badalgama (Maha Oya) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-02-18 06:01:23 | Siyambalanduwa (Heda Oya) | 0.59 | 🟢 Normal | -0.020 |  |
| 2026-02-18 06:01:15 | Kuda Oya (Kirindi Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-02-18 05:28:46 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | -0.128 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-18 06:05:11 | Deraniyagala (Kelani Ganga) | 0.14 | 🟢 Normal | 3.892 | 🔺 Rising |
| 2026-02-18 06:10:09 | Rathnapura (Kalu Ganga) | 0.53 | 🟢 Normal | 0.212 | 🔺 Rising |
| 2026-02-18 06:01:37 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | 0.210 | 🔺 Rising |
| 2026-02-18 06:09:06 | Manampitiya (Mahaweli Ganga) | 1.30 | 🟢 Normal | 0.104 | 🔺 Rising |
| 2026-02-18 06:02:47 | Glencourse (Kelani Ganga) | 8.60 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-02-18 06:04:07 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-02-18 06:01:39 | Nawalapitiya (Mahaweli Ganga) | 0.62 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-18 06:02:00 | Thawalama (Gin Ganga) | 1.00 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-18 06:02:25 | Hanwella (Kelani Ganga) | 0.31 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-18 06:03:13 | Ellagawa (Kalu Ganga) | 3.85 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-18 06:04:44 | Weraganthota (Mahaweli Ganga) | -2.30 | 🟢 Normal | 0.007 | 🔺 Rising |
| 2026-02-18 06:03:08 | Nakkala (Kumbukkan Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-02-18 06:03:06 | Moragaswewa (Deduru Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-02-18 06:01:30 | Yaka Wewa (Ma Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-02-18 06:03:08 | Giriulla (Maha Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-02-17 18:04:27 | Galgamuwa (Mee Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-02-18 06:08:37 | Magura (Kalu Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-02-18 06:04:52 | Pitabeddara (Nilwala Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-02-18 06:01:46 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-02-18 06:09:10 | Baddegama (Gin Ganga) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-02-18 06:02:25 | Dunamale (Aththanagalu Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-02-18 06:01:25 | Badalgama (Maha Oya) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-02-18 05:05:04 | Holombuwa (Kelani Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-02-17 18:02:27 | Thanthirimale (Malwathu Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-02-18 06:08:38 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-02-18 06:13:10 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-02-18 06:01:15 | Kuda Oya (Kirindi Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-02-18 06:04:30 | Thanamalwila (Kirindi Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-02-18 06:07:14 | Panadugama (Nilwala Ganga) | 1.95 | 🟢 Normal | -0.010 |  |
| 2026-02-18 06:05:20 | Horowpothana (Yan Oya) | 1.38 | 🟢 Normal | -0.010 |  |
| 2026-02-18 06:06:55 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | -0.010 |  |
| 2026-02-18 06:02:53 | Thaldena (Mahaweli Ganga) | 0.54 | 🟢 Normal | -0.010 |  |
| 2026-02-18 05:01:10 | Padiyathalawa (Maduru Oya) | 1.05 | 🟢 Normal | -0.010 |  |
| 2026-02-18 06:04:03 | Moraketiya (Walawe Ganga) | 0.89 | 🟢 Normal | -0.011 |  |
| 2026-02-18 06:01:23 | Siyambalanduwa (Heda Oya) | 0.59 | 🟢 Normal | -0.020 |  |
| 2026-02-18 06:01:32 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.70 | 🟢 Normal | -0.040 |  |
| 2026-02-18 06:01:30 | Putupaula (Kalu Ganga) | 0.69 | 🟢 Normal | -0.073 |  |
| 2026-02-18 06:08:55 | Peradeniya (Mahaweli Ganga) | 1.17 | 🟢 Normal | -0.121 |  |
| 2026-02-18 06:11:42 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.128 |  |

## River Water Level Charts by Station

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

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

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)