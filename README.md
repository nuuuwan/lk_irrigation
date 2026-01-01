# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--02_02:15:00-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **34,199 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **30** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-02 02:15:00 | Panadugama (Nilwala Ganga) | 2.28 | 🟢 Normal | 0.000 |  |
| 2026-01-02 02:12:07 | Holombuwa (Kelani Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-01-02 02:11:48 | Holombuwa (Kelani Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-01-02 02:08:40 | Glencourse (Kelani Ganga) | 8.85 | 🟢 Normal | -0.032 |  |
| 2026-01-02 02:08:30 | Siyambalanduwa (Heda Oya) | 2.24 | 🟢 Normal | 0.212 | 🔺 Rising |
| 2026-01-02 02:07:13 | Baddegama (Gin Ganga) | 1.15 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-02 02:07:02 | Thanamalwila (Kirindi Oya) | 1.88 | 🟢 Normal | -0.057 |  |
| 2026-01-02 02:06:09 | Thawalama (Gin Ganga) | 1.20 | 🟢 Normal | -0.019 |  |
| 2026-01-02 02:05:51 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-01-02 02:05:29 | Hanwella (Kelani Ganga) | 0.67 | 🟢 Normal | -0.010 |  |
| 2026-01-02 02:04:49 | Nakkala (Kumbukkan Oya) | 1.76 | 🟢 Normal | 0.292 | 🔺 Rising |
| 2026-01-02 02:04:09 | Kithulgala (Kelani Ganga) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-01-02 02:04:07 | Magura (Kalu Ganga) | 0.92 | 🟢 Normal | -0.010 |  |
| 2026-01-02 02:03:43 | Rathnapura (Kalu Ganga) | 0.86 | 🟢 Normal | -0.011 |  |
| 2026-01-02 02:03:21 | Peradeniya (Mahaweli Ganga) | 2.55 | 🟢 Normal | -0.250 |  |
| 2026-01-02 02:03:18 | Norwood (Kelani Ganga) | 0.58 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-02 02:03:05 | Giriulla (Maha Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-01-02 02:02:54 | Yaka Wewa (Ma Oya) | 0.91 | 🟢 Normal | -0.020 |  |
| 2026-01-02 02:02:42 | Moragaswewa (Deduru Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-01-02 02:01:38 | Manampitiya (Mahaweli Ganga) | 1.64 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-02 02:01:35 | Ellagawa (Kalu Ganga) | 4.34 | 🟢 Normal | -0.010 |  |
| 2026-01-02 02:01:28 | Nawalapitiya (Mahaweli Ganga) | 0.89 | 🟢 Normal | -0.010 |  |
| 2026-01-02 02:01:21 | Dunamale (Aththanagalu Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-01-02 02:01:05 | Moraketiya (Walawe Ganga) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-01-02 02:00:57 | Badalgama (Maha Oya) | 2.17 | 🟢 Normal | 0.000 |  |
| 2026-01-02 02:00:51 | Thaldena (Mahaweli Ganga) | 1.21 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-02 02:00:43 | Kithulgala (Kelani Ganga) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-01-02 02:00:18 | Kuda Oya (Kirindi Oya) | 2.00 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-02 01:56:16 | Horowpothana (Yan Oya) | 3.80 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-01-02 01:32:45 | Thalgahagoda (Nilwala Ganga) | 0.18 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-02 00:05:40 | Padiyathalawa (Maduru Oya) | 4.25 | 🟡 Alert | -0.096 |  |
| 2026-01-02 02:04:49 | Nakkala (Kumbukkan Oya) | 1.76 | 🟢 Normal | 0.292 | 🔺 Rising |
| 2026-01-02 02:08:30 | Siyambalanduwa (Heda Oya) | 2.24 | 🟢 Normal | 0.212 | 🔺 Rising |
| 2026-01-02 00:04:07 | Putupaula (Kalu Ganga) | 0.71 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-01-02 02:00:18 | Kuda Oya (Kirindi Oya) | 2.00 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-02 02:01:38 | Manampitiya (Mahaweli Ganga) | 1.64 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-02 01:56:16 | Horowpothana (Yan Oya) | 3.80 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-01-02 02:07:13 | Baddegama (Gin Ganga) | 1.15 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-02 02:00:51 | Thaldena (Mahaweli Ganga) | 1.21 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-02 02:03:18 | Norwood (Kelani Ganga) | 0.58 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-02 02:04:09 | Kithulgala (Kelani Ganga) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-01-02 02:02:42 | Moragaswewa (Deduru Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-01-02 02:03:05 | Giriulla (Maha Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-01-01 17:09:46 | Galgamuwa (Mee Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-01-02 00:05:31 | Pitabeddara (Nilwala Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-01-02 02:15:00 | Panadugama (Nilwala Ganga) | 2.28 | 🟢 Normal | 0.000 |  |
| 2026-01-02 02:05:51 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-01-02 02:01:05 | Moraketiya (Walawe Ganga) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-01-02 02:01:21 | Dunamale (Aththanagalu Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-01-02 02:00:57 | Badalgama (Maha Oya) | 2.17 | 🟢 Normal | 0.000 |  |
| 2026-01-02 02:12:07 | Holombuwa (Kelani Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-01-02 01:00:46 | Urawa (Nilwala Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-01-02 01:32:45 | Thalgahagoda (Nilwala Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-01-02 02:05:29 | Hanwella (Kelani Ganga) | 0.67 | 🟢 Normal | -0.010 |  |
| 2026-01-02 02:01:28 | Nawalapitiya (Mahaweli Ganga) | 0.89 | 🟢 Normal | -0.010 |  |
| 2026-01-02 02:04:07 | Magura (Kalu Ganga) | 0.92 | 🟢 Normal | -0.010 |  |
| 2026-01-02 02:01:35 | Ellagawa (Kalu Ganga) | 4.34 | 🟢 Normal | -0.010 |  |
| 2026-01-02 02:03:43 | Rathnapura (Kalu Ganga) | 0.86 | 🟢 Normal | -0.011 |  |
| 2026-01-02 02:06:09 | Thawalama (Gin Ganga) | 1.20 | 🟢 Normal | -0.019 |  |
| 2026-01-02 02:02:54 | Yaka Wewa (Ma Oya) | 0.91 | 🟢 Normal | -0.020 |  |
| 2026-01-01 18:02:09 | Weraganthota (Mahaweli Ganga) | -1.82 | 🟢 Normal | -0.020 |  |
| 2026-01-01 20:14:45 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.46 | 🟢 Normal | -0.030 |  |
| 2026-01-02 02:08:40 | Glencourse (Kelani Ganga) | 8.85 | 🟢 Normal | -0.032 |  |
| 2026-01-02 00:11:06 | Wellawaya (Kirindi Oya) | 1.30 | 🟢 Normal | -0.038 |  |
| 2026-01-01 18:00:31 | Thanthirimale (Malwathu Oya) | 2.12 | 🟢 Normal | -0.040 |  |
| 2026-01-02 02:07:02 | Thanamalwila (Kirindi Oya) | 1.88 | 🟢 Normal | -0.057 |  |
| 2026-01-02 01:02:08 | Deraniyagala (Kelani Ganga) | 0.32 | 🟢 Normal | -0.062 |  |
| 2026-01-02 01:05:40 | Katharagama (Menik Ganga) | 1.13 | 🟢 Normal | -0.069 |  |
| 2026-01-02 02:03:21 | Peradeniya (Mahaweli Ganga) | 2.55 | 🟢 Normal | -0.250 |  |

## River Water Level Charts by Station

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)