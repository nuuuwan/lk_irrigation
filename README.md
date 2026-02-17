# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--17_11:09:28-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **75,435 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **33** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-17 11:09:28 | Thawalama (Gin Ganga) | 1.01 | 🟢 Normal | -0.027 |  |
| 2026-02-17 11:08:35 | Magura (Kalu Ganga) | 0.87 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-02-17 11:08:19 | Galgamuwa (Mee Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-17 11:07:41 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | 0.127 | 🔺 Rising |
| 2026-02-17 11:07:23 | Holombuwa (Kelani Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-02-17 11:06:09 | Baddegama (Gin Ganga) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-02-17 11:06:06 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-17 11:04:53 | Putupaula (Kalu Ganga) | 0.35 | 🟢 Normal | 0.098 | 🔺 Rising |
| 2026-02-17 11:04:50 | Kithulgala (Kelani Ganga) | 1.73 | 🟢 Normal | 0.429 | 🔺 Rising |
| 2026-02-17 11:04:35 | Glencourse (Kelani Ganga) | 8.37 | 🟢 Normal | 0.000 |  |
| 2026-02-17 11:04:34 | Deraniyagala (Kelani Ganga) | 0.15 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-02-17 11:04:14 | Hanwella (Kelani Ganga) | 0.35 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-17 11:04:14 | Dunamale (Aththanagalu Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-02-17 11:04:08 | Ellagawa (Kalu Ganga) | 3.92 | 🟢 Normal | -0.010 |  |
| 2026-02-17 11:03:43 | Siyambalanduwa (Heda Oya) | 0.53 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-02-17 11:03:12 | Norwood (Kelani Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-02-17 11:02:56 | Rathnapura (Kalu Ganga) | 0.57 | 🟢 Normal | -0.010 |  |
| 2026-02-17 11:02:31 | Kuda Oya (Kirindi Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-02-17 11:02:14 | Thanamalwila (Kirindi Oya) | 0.72 | 🟢 Normal | -0.010 |  |
| 2026-02-17 11:02:06 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.57 | 🟢 Normal | -0.030 |  |
| 2026-02-17 11:01:49 | Yaka Wewa (Ma Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-02-17 11:01:48 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-17 11:01:44 | Thalgahagoda (Nilwala Ganga) | 0.20 | 🟢 Normal | -0.050 |  |
| 2026-02-17 11:01:37 | Weraganthota (Mahaweli Ganga) | -2.38 | 🟢 Normal | 0.290 | 🔺 Rising |
| 2026-02-17 11:01:31 | Giriulla (Maha Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-02-17 11:01:15 | Wellawaya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-02-17 11:01:14 | Manampitiya (Mahaweli Ganga) | 0.86 | 🟢 Normal | -0.030 |  |
| 2026-02-17 11:01:08 | Thaldena (Mahaweli Ganga) | 0.47 | 🟢 Normal | -0.010 |  |
| 2026-02-17 11:00:48 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-02-17 11:00:42 | Moragaswewa (Deduru Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-02-17 11:00:23 | Nakkala (Kumbukkan Oya) | 0.86 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-02-17 11:00:14 | Nawalapitiya (Mahaweli Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-02-17 11:00:13 | Padiyathalawa (Maduru Oya) | 0.90 | 🟢 Normal | 0.036 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-17 11:04:50 | Kithulgala (Kelani Ganga) | 1.73 | 🟢 Normal | 0.429 | 🔺 Rising |
| 2026-02-17 11:01:37 | Weraganthota (Mahaweli Ganga) | -2.38 | 🟢 Normal | 0.290 | 🔺 Rising |
| 2026-02-17 11:07:41 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | 0.127 | 🔺 Rising |
| 2026-02-17 11:04:53 | Putupaula (Kalu Ganga) | 0.35 | 🟢 Normal | 0.098 | 🔺 Rising |
| 2026-02-17 10:07:32 | Peradeniya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-02-17 11:04:34 | Deraniyagala (Kelani Ganga) | 0.15 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-02-17 11:03:43 | Siyambalanduwa (Heda Oya) | 0.53 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-02-17 11:00:13 | Padiyathalawa (Maduru Oya) | 0.90 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-02-17 11:00:23 | Nakkala (Kumbukkan Oya) | 0.86 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-02-17 11:08:35 | Magura (Kalu Ganga) | 0.87 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-02-17 11:04:14 | Hanwella (Kelani Ganga) | 0.35 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-17 11:01:15 | Wellawaya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-02-17 11:00:42 | Moragaswewa (Deduru Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-02-17 11:00:14 | Nawalapitiya (Mahaweli Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-02-17 11:01:49 | Yaka Wewa (Ma Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-02-17 11:01:31 | Giriulla (Maha Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-02-17 11:08:19 | Galgamuwa (Mee Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-17 10:08:22 | Pitabeddara (Nilwala Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-02-17 11:03:12 | Norwood (Kelani Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-02-17 11:06:09 | Baddegama (Gin Ganga) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-02-17 11:04:35 | Glencourse (Kelani Ganga) | 8.37 | 🟢 Normal | 0.000 |  |
| 2026-02-17 11:00:48 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-02-17 11:04:14 | Dunamale (Aththanagalu Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-02-17 11:01:48 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-17 11:06:06 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-17 11:07:23 | Holombuwa (Kelani Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-02-17 10:03:27 | Thanthirimale (Malwathu Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-02-17 10:03:55 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-02-17 11:02:31 | Kuda Oya (Kirindi Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-02-17 10:07:02 | Panadugama (Nilwala Ganga) | 1.99 | 🟢 Normal | -0.009 |  |
| 2026-02-17 11:04:08 | Ellagawa (Kalu Ganga) | 3.92 | 🟢 Normal | -0.010 |  |
| 2026-02-17 11:02:14 | Thanamalwila (Kirindi Oya) | 0.72 | 🟢 Normal | -0.010 |  |
| 2026-02-17 11:02:56 | Rathnapura (Kalu Ganga) | 0.57 | 🟢 Normal | -0.010 |  |
| 2026-02-17 11:01:08 | Thaldena (Mahaweli Ganga) | 0.47 | 🟢 Normal | -0.010 |  |
| 2026-02-17 10:00:58 | Horowpothana (Yan Oya) | 1.47 | 🟢 Normal | -0.016 |  |
| 2026-02-17 11:09:28 | Thawalama (Gin Ganga) | 1.01 | 🟢 Normal | -0.027 |  |
| 2026-02-17 11:01:14 | Manampitiya (Mahaweli Ganga) | 0.86 | 🟢 Normal | -0.030 |  |
| 2026-02-17 11:02:06 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.57 | 🟢 Normal | -0.030 |  |
| 2026-02-17 11:01:44 | Thalgahagoda (Nilwala Ganga) | 0.20 | 🟢 Normal | -0.050 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

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

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)