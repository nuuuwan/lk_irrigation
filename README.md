# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--16_19:12:52-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **47,400 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-16 19:12:52 | Panadugama (Nilwala Ganga) | 2.23 | 🟢 Normal | 0.000 |  |
| 2026-01-16 19:11:47 | Badalgama (Maha Oya) | 1.96 | 🟢 Normal | -0.009 |  |
| 2026-01-16 19:10:00 | Urawa (Nilwala Ganga) | 0.15 | 🟢 Normal | -0.009 |  |
| 2026-01-16 19:09:48 | Moragaswewa (Deduru Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-01-16 19:09:32 | Rathnapura (Kalu Ganga) | 0.60 | 🟢 Normal | -0.010 |  |
| 2026-01-16 19:08:53 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-01-16 19:07:06 | Thawalama (Gin Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-01-16 19:06:54 | Kithulgala (Kelani Ganga) | 1.68 | 🟢 Normal | 0.077 | 🔺 Rising |
| 2026-01-16 19:06:34 | Putupaula (Kalu Ganga) | 0.63 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-01-16 19:06:15 | Thanamalwila (Kirindi Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-01-16 19:06:09 | Deraniyagala (Kelani Ganga) | 0.12 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-01-16 19:05:31 | Glencourse (Kelani Ganga) | 8.53 | 🟢 Normal | -0.041 |  |
| 2026-01-16 19:05:14 | Moraketiya (Walawe Ganga) | 0.86 | 🟢 Normal | -0.010 |  |
| 2026-01-16 19:04:19 | Peradeniya (Mahaweli Ganga) | 1.35 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-01-16 19:03:38 | Nawalapitiya (Mahaweli Ganga) | 0.68 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-01-16 19:03:29 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-01-16 19:03:09 | Baddegama (Gin Ganga) | 0.91 | 🟢 Normal | -0.030 |  |
| 2026-01-16 19:02:57 | Hanwella (Kelani Ganga) | 0.45 | 🟢 Normal | -0.010 |  |
| 2026-01-16 19:02:51 | Norwood (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-01-16 19:02:32 | Dunamale (Aththanagalu Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-01-16 19:02:24 | Katharagama (Menik Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-01-16 19:02:19 | Siyambalanduwa (Heda Oya) | 0.75 | 🟢 Normal | -0.010 |  |
| 2026-01-16 19:02:10 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-01-16 19:01:59 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | -0.010 |  |
| 2026-01-16 19:01:50 | Yaka Wewa (Ma Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-01-16 19:01:45 | Moragaswewa (Deduru Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-01-16 19:01:28 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-01-16 19:01:26 | Giriulla (Maha Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-01-16 19:01:12 | Pitabeddara (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-01-16 19:01:10 | Manampitiya (Mahaweli Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-01-16 19:01:08 | Ellagawa (Kalu Ganga) | 4.07 | 🟢 Normal | 0.000 |  |
| 2026-01-16 19:01:07 | Magura (Kalu Ganga) | 1.10 | 🟢 Normal | -0.039 |  |
| 2026-01-16 19:00:28 | Nakkala (Kumbukkan Oya) | 0.99 | 🟢 Normal | -0.010 |  |
| 2026-01-16 18:56:44 | Manampitiya (Mahaweli Ganga) | 1.18 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-16 19:06:54 | Kithulgala (Kelani Ganga) | 1.68 | 🟢 Normal | 0.077 | 🔺 Rising |
| 2026-01-16 19:04:19 | Peradeniya (Mahaweli Ganga) | 1.35 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-01-16 18:00:22 | Weraganthota (Mahaweli Ganga) | -1.98 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-01-16 19:03:38 | Nawalapitiya (Mahaweli Ganga) | 0.68 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-01-16 19:06:34 | Putupaula (Kalu Ganga) | 0.63 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-01-16 19:06:09 | Deraniyagala (Kelani Ganga) | 0.12 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-01-16 19:02:10 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-01-16 19:09:48 | Moragaswewa (Deduru Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-01-16 19:01:50 | Yaka Wewa (Ma Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-01-16 19:01:26 | Giriulla (Maha Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-01-16 18:06:10 | Galgamuwa (Mee Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-01-16 19:01:12 | Pitabeddara (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-01-16 19:02:51 | Norwood (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-01-16 19:01:08 | Ellagawa (Kalu Ganga) | 4.07 | 🟢 Normal | 0.000 |  |
| 2026-01-16 19:12:52 | Panadugama (Nilwala Ganga) | 2.23 | 🟢 Normal | 0.000 |  |
| 2026-01-16 18:04:24 | Padiyathalawa (Maduru Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-01-16 19:01:28 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-01-16 19:02:32 | Dunamale (Aththanagalu Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-01-16 19:02:24 | Katharagama (Menik Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-01-16 19:03:29 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-01-16 19:01:10 | Manampitiya (Mahaweli Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-01-16 19:07:06 | Thawalama (Gin Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-01-16 19:08:53 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-01-16 19:06:15 | Thanamalwila (Kirindi Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-01-16 19:10:00 | Urawa (Nilwala Ganga) | 0.15 | 🟢 Normal | -0.009 |  |
| 2026-01-16 19:11:47 | Badalgama (Maha Oya) | 1.96 | 🟢 Normal | -0.009 |  |
| 2026-01-16 19:09:32 | Rathnapura (Kalu Ganga) | 0.60 | 🟢 Normal | -0.010 |  |
| 2026-01-16 19:05:14 | Moraketiya (Walawe Ganga) | 0.86 | 🟢 Normal | -0.010 |  |
| 2026-01-16 19:01:59 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | -0.010 |  |
| 2026-01-16 19:02:57 | Hanwella (Kelani Ganga) | 0.45 | 🟢 Normal | -0.010 |  |
| 2026-01-16 19:00:28 | Nakkala (Kumbukkan Oya) | 0.99 | 🟢 Normal | -0.010 |  |
| 2026-01-16 19:02:19 | Siyambalanduwa (Heda Oya) | 0.75 | 🟢 Normal | -0.010 |  |
| 2026-01-16 18:00:06 | Thaldena (Mahaweli Ganga) | 0.61 | 🟢 Normal | -0.010 |  |
| 2026-01-16 18:01:44 | Thanthirimale (Malwathu Oya) | 1.60 | 🟢 Normal | -0.020 |  |
| 2026-01-16 19:03:09 | Baddegama (Gin Ganga) | 0.91 | 🟢 Normal | -0.030 |  |
| 2026-01-16 19:01:07 | Magura (Kalu Ganga) | 1.10 | 🟢 Normal | -0.039 |  |
| 2026-01-16 19:05:31 | Glencourse (Kelani Ganga) | 8.53 | 🟢 Normal | -0.041 |  |
| 2026-01-16 18:02:18 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.80 | 🟢 Normal | -0.051 |  |
| 2026-01-16 18:03:22 | Horowpothana (Yan Oya) | 1.94 | 🟢 Normal | -0.146 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)