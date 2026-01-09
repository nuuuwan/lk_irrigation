# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--09_23:22:08-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **41,289 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-09 23:22:08 | Giriulla (Maha Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-01-09 23:21:25 | Urawa (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-01-09 23:14:58 | Peradeniya (Mahaweli Ganga) | 2.68 | 🟢 Normal | 0.176 | 🔺 Rising |
| 2026-01-09 23:14:32 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.34 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-01-09 23:09:55 | Glencourse (Kelani Ganga) | 8.47 | 🟢 Normal | 0.000 |  |
| 2026-01-09 23:07:49 | Baddegama (Gin Ganga) | 0.92 | 🟢 Normal | -0.010 |  |
| 2026-01-09 23:06:22 | Pitabeddara (Nilwala Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-01-09 23:05:59 | Kuda Oya (Kirindi Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-01-09 23:05:53 | Magura (Kalu Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-01-09 23:05:03 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-01-09 23:04:36 | Thanamalwila (Kirindi Oya) | 1.05 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-09 23:04:29 | Deraniyagala (Kelani Ganga) | 0.27 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-01-09 23:04:19 | Dunamale (Aththanagalu Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-01-09 23:04:15 | Padiyathalawa (Maduru Oya) | 1.20 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-09 23:04:09 | Rathnapura (Kalu Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-01-09 23:04:00 | Norwood (Kelani Ganga) | 0.51 | 🟢 Normal | -0.010 |  |
| 2026-01-09 23:03:30 | Nakkala (Kumbukkan Oya) | 1.15 | 🟢 Normal | -0.010 |  |
| 2026-01-09 23:03:21 | Kithulgala (Kelani Ganga) | 1.52 | 🟢 Normal | -0.030 |  |
| 2026-01-09 23:03:09 | Hanwella (Kelani Ganga) | 0.43 | 🟢 Normal | -0.021 |  |
| 2026-01-09 23:02:37 | Katharagama (Menik Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-01-09 23:02:07 | Siyambalanduwa (Heda Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-01-09 23:02:06 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-09 23:02:02 | Yaka Wewa (Ma Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-01-09 23:02:02 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.095 |  |
| 2026-01-09 23:01:48 | Moragaswewa (Deduru Oya) | 1.16 | 🟢 Normal | -0.012 |  |
| 2026-01-09 23:01:42 | Horowpothana (Yan Oya) | 2.39 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-09 23:01:34 | Manampitiya (Mahaweli Ganga) | 2.15 | 🟢 Normal | -0.032 |  |
| 2026-01-09 23:01:27 | Ellagawa (Kalu Ganga) | 4.07 | 🟢 Normal | 0.000 |  |
| 2026-01-09 23:01:08 | Badalgama (Maha Oya) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-01-09 23:01:04 | Thaldena (Mahaweli Ganga) | 0.92 | 🟢 Normal | -0.021 |  |
| 2026-01-09 23:00:53 | Nawalapitiya (Mahaweli Ganga) | 0.74 | 🟢 Normal | -0.010 |  |
| 2026-01-09 23:00:44 | Thawalama (Gin Ganga) | 1.26 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-01-09 23:00:26 | Wellawaya (Kirindi Oya) | 1.41 | 🟢 Normal | 0.093 | 🔺 Rising |
| 2026-01-09 22:38:36 | Putupaula (Kalu Ganga) | 0.51 | 🟢 Normal | -0.069 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-09 23:14:58 | Peradeniya (Mahaweli Ganga) | 2.68 | 🟢 Normal | 0.176 | 🔺 Rising |
| 2026-01-09 23:00:26 | Wellawaya (Kirindi Oya) | 1.41 | 🟢 Normal | 0.093 | 🔺 Rising |
| 2026-01-09 23:04:29 | Deraniyagala (Kelani Ganga) | 0.27 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-01-09 23:00:44 | Thawalama (Gin Ganga) | 1.26 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-01-09 23:14:32 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.34 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-01-09 17:13:03 | Thanthirimale (Malwathu Oya) | 1.55 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-09 23:02:06 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-09 23:04:15 | Padiyathalawa (Maduru Oya) | 1.20 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-09 23:01:42 | Horowpothana (Yan Oya) | 2.39 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-09 23:04:36 | Thanamalwila (Kirindi Oya) | 1.05 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-09 23:02:02 | Yaka Wewa (Ma Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-01-09 23:22:08 | Giriulla (Maha Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-01-09 23:05:53 | Magura (Kalu Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-01-09 23:06:22 | Pitabeddara (Nilwala Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-01-09 23:01:27 | Ellagawa (Kalu Ganga) | 4.07 | 🟢 Normal | 0.000 |  |
| 2026-01-09 23:09:55 | Glencourse (Kelani Ganga) | 8.47 | 🟢 Normal | 0.000 |  |
| 2026-01-09 23:02:07 | Siyambalanduwa (Heda Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-01-09 23:04:19 | Dunamale (Aththanagalu Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-01-09 23:02:37 | Katharagama (Menik Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-01-09 23:01:08 | Badalgama (Maha Oya) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-01-09 23:05:03 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-01-09 23:04:09 | Rathnapura (Kalu Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-01-09 23:21:25 | Urawa (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-01-09 23:05:59 | Kuda Oya (Kirindi Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-01-09 23:03:30 | Nakkala (Kumbukkan Oya) | 1.15 | 🟢 Normal | -0.010 |  |
| 2026-01-09 23:07:49 | Baddegama (Gin Ganga) | 0.92 | 🟢 Normal | -0.010 |  |
| 2026-01-09 23:00:53 | Nawalapitiya (Mahaweli Ganga) | 0.74 | 🟢 Normal | -0.010 |  |
| 2026-01-09 23:04:00 | Norwood (Kelani Ganga) | 0.51 | 🟢 Normal | -0.010 |  |
| 2026-01-09 18:00:08 | Weraganthota (Mahaweli Ganga) | -1.21 | 🟢 Normal | -0.010 |  |
| 2026-01-09 18:08:00 | Galgamuwa (Mee Oya) | 0.29 | 🟢 Normal | -0.011 |  |
| 2026-01-09 22:03:10 | Panadugama (Nilwala Ganga) | 2.46 | 🟢 Normal | -0.011 |  |
| 2026-01-09 23:01:48 | Moragaswewa (Deduru Oya) | 1.16 | 🟢 Normal | -0.012 |  |
| 2026-01-09 23:01:04 | Thaldena (Mahaweli Ganga) | 0.92 | 🟢 Normal | -0.021 |  |
| 2026-01-09 23:03:09 | Hanwella (Kelani Ganga) | 0.43 | 🟢 Normal | -0.021 |  |
| 2026-01-09 23:03:21 | Kithulgala (Kelani Ganga) | 1.52 | 🟢 Normal | -0.030 |  |
| 2026-01-09 23:01:34 | Manampitiya (Mahaweli Ganga) | 2.15 | 🟢 Normal | -0.032 |  |
| 2026-01-09 22:05:06 | Thalgahagoda (Nilwala Ganga) | 0.47 | 🟢 Normal | -0.035 |  |
| 2026-01-09 22:38:36 | Putupaula (Kalu Ganga) | 0.51 | 🟢 Normal | -0.069 |  |
| 2026-01-09 23:02:02 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.095 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

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

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)