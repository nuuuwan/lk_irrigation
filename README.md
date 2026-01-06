# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--06_23:08:01-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **38,581 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **30** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-06 23:08:01 | Putupaula (Kalu Ganga) | 0.49 | 🟢 Normal | -0.065 |  |
| 2026-01-06 23:07:13 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | -0.019 |  |
| 2026-01-06 23:07:07 | Badalgama (Maha Oya) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-01-06 23:06:40 | Siyambalanduwa (Heda Oya) | 2.51 | 🟢 Normal | -0.112 |  |
| 2026-01-06 23:06:02 | Magura (Kalu Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-01-06 23:06:01 | Nawalapitiya (Mahaweli Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-01-06 23:05:45 | Baddegama (Gin Ganga) | 1.41 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-01-06 23:04:56 | Norwood (Kelani Ganga) | 0.60 | 🟢 Normal | -0.010 |  |
| 2026-01-06 23:04:38 | Manampitiya (Mahaweli Ganga) | 3.71 | 🟡 Alert | -0.038 |  |
| 2026-01-06 23:04:12 | Rathnapura (Kalu Ganga) | 0.87 | 🟢 Normal | -0.010 |  |
| 2026-01-06 23:03:53 | Thanamalwila (Kirindi Oya) | 1.34 | 🟢 Normal | -0.010 |  |
| 2026-01-06 23:03:37 | Padiyathalawa (Maduru Oya) | 1.57 | 🟢 Normal | -0.029 |  |
| 2026-01-06 23:03:25 | Urawa (Nilwala Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-01-06 23:03:23 | Katharagama (Menik Ganga) | 0.50 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-01-06 23:03:15 | Giriulla (Maha Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-01-06 23:03:05 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-01-06 23:02:51 | Wellawaya (Kirindi Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-01-06 23:02:48 | Deraniyagala (Kelani Ganga) | 0.19 | 🟢 Normal | -0.030 |  |
| 2026-01-06 23:02:45 | Hanwella (Kelani Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-01-06 23:02:26 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-01-06 23:02:21 | Moragaswewa (Deduru Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-01-06 23:01:55 | Peradeniya (Mahaweli Ganga) | 2.74 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-01-06 23:01:36 | Yaka Wewa (Ma Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-01-06 23:01:15 | Kuda Oya (Kirindi Oya) | 1.39 | 🟢 Normal | 0.000 |  |
| 2026-01-06 23:00:50 | Thaldena (Mahaweli Ganga) | 0.98 | 🟢 Normal | -0.074 |  |
| 2026-01-06 23:00:25 | Nakkala (Kumbukkan Oya) | 1.66 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-01-06 22:40:49 | Glencourse (Kelani Ganga) | 8.68 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-01-06 22:26:10 | Pitabeddara (Nilwala Ganga) | 0.75 | 🟢 Normal | -0.008 |  |
| 2026-01-06 22:18:45 | Urawa (Nilwala Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-01-06 22:16:25 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-06 23:04:38 | Manampitiya (Mahaweli Ganga) | 3.71 | 🟡 Alert | -0.038 |  |
| 2026-01-06 23:01:55 | Peradeniya (Mahaweli Ganga) | 2.74 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-01-06 22:01:21 | Horowpothana (Yan Oya) | 2.79 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-01-06 22:06:38 | Thawalama (Gin Ganga) | 1.45 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-01-06 23:00:25 | Nakkala (Kumbukkan Oya) | 1.66 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-01-06 23:05:45 | Baddegama (Gin Ganga) | 1.41 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-01-06 18:00:39 | Thanthirimale (Malwathu Oya) | 1.73 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-06 22:40:49 | Glencourse (Kelani Ganga) | 8.68 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-01-06 23:03:23 | Katharagama (Menik Ganga) | 0.50 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-01-06 18:02:01 | Weraganthota (Mahaweli Ganga) | -0.56 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-06 23:02:51 | Wellawaya (Kirindi Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-01-06 23:02:21 | Moragaswewa (Deduru Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-01-06 23:06:01 | Nawalapitiya (Mahaweli Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-01-06 23:01:36 | Yaka Wewa (Ma Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-01-06 23:03:15 | Giriulla (Maha Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-01-06 18:03:13 | Galgamuwa (Mee Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-01-06 23:06:02 | Magura (Kalu Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-01-06 23:02:45 | Hanwella (Kelani Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-01-06 22:08:00 | Panadugama (Nilwala Ganga) | 2.66 | 🟢 Normal | 0.000 |  |
| 2026-01-06 23:03:05 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-01-06 22:04:54 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-01-06 22:02:45 | Dunamale (Aththanagalu Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-01-06 23:07:07 | Badalgama (Maha Oya) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-01-06 23:02:26 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-01-06 23:03:25 | Urawa (Nilwala Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-01-06 23:01:15 | Kuda Oya (Kirindi Oya) | 1.39 | 🟢 Normal | 0.000 |  |
| 2026-01-06 22:26:10 | Pitabeddara (Nilwala Ganga) | 0.75 | 🟢 Normal | -0.008 |  |
| 2026-01-06 23:04:56 | Norwood (Kelani Ganga) | 0.60 | 🟢 Normal | -0.010 |  |
| 2026-01-06 22:04:11 | Ellagawa (Kalu Ganga) | 4.38 | 🟢 Normal | -0.010 |  |
| 2026-01-06 22:08:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.68 | 🟢 Normal | -0.010 |  |
| 2026-01-06 23:03:53 | Thanamalwila (Kirindi Oya) | 1.34 | 🟢 Normal | -0.010 |  |
| 2026-01-06 23:04:12 | Rathnapura (Kalu Ganga) | 0.87 | 🟢 Normal | -0.010 |  |
| 2026-01-06 23:07:13 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | -0.019 |  |
| 2026-01-06 23:03:37 | Padiyathalawa (Maduru Oya) | 1.57 | 🟢 Normal | -0.029 |  |
| 2026-01-06 23:02:48 | Deraniyagala (Kelani Ganga) | 0.19 | 🟢 Normal | -0.030 |  |
| 2026-01-06 23:08:01 | Putupaula (Kalu Ganga) | 0.49 | 🟢 Normal | -0.065 |  |
| 2026-01-06 23:00:50 | Thaldena (Mahaweli Ganga) | 0.98 | 🟢 Normal | -0.074 |  |
| 2026-01-06 22:04:59 | Kithulgala (Kelani Ganga) | 1.60 | 🟢 Normal | -0.086 |  |
| 2026-01-06 23:06:40 | Siyambalanduwa (Heda Oya) | 2.51 | 🟢 Normal | -0.112 |  |

## River Water Level Charts by Station

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

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

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

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

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)