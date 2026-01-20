# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--20_08:07:39-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **50,569 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-20 08:07:39 | Padiyathalawa (Maduru Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-01-20 08:07:17 | Norwood (Kelani Ganga) | 0.44 | 🟢 Normal | -0.009 |  |
| 2026-01-20 08:06:54 | Baddegama (Gin Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-01-20 08:06:39 | Holombuwa (Kelani Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-01-20 08:06:35 | Badalgama (Maha Oya) | 1.89 | 🟢 Normal | 0.000 |  |
| 2026-01-20 08:06:34 | Thanthirimale (Malwathu Oya) | 1.51 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-20 08:06:22 | Kithulgala (Kelani Ganga) | 1.54 | 🟢 Normal | -0.009 |  |
| 2026-01-20 08:06:12 | Thalgahagoda (Nilwala Ganga) | 0.50 | 🟢 Normal | -0.173 |  |
| 2026-01-20 08:05:15 | Peradeniya (Mahaweli Ganga) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-01-20 08:05:12 | Katharagama (Menik Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-01-20 08:04:40 | Magura (Kalu Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-01-20 08:04:34 | Manampitiya (Mahaweli Ganga) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-01-20 08:04:09 | Manampitiya (Mahaweli Ganga) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-01-20 08:04:04 | Ellagawa (Kalu Ganga) | 3.92 | 🟢 Normal | 0.000 |  |
| 2026-01-20 08:03:54 | Putupaula (Kalu Ganga) | 0.46 | 🟢 Normal | -0.137 |  |
| 2026-01-20 08:03:26 | Hanwella (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-01-20 08:03:16 | Pitabeddara (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-01-20 08:02:59 | Thaldena (Mahaweli Ganga) | 0.55 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-01-20 08:02:56 | Nawalapitiya (Mahaweli Ganga) | 0.64 | 🟢 Normal | -0.010 |  |
| 2026-01-20 08:02:54 | Thawalama (Gin Ganga) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-01-20 08:02:39 | Kuda Oya (Kirindi Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-01-20 08:02:30 | Wellawaya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-20 08:02:21 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.54 | 🟢 Normal | -0.060 |  |
| 2026-01-20 08:02:07 | Deraniyagala (Kelani Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-01-20 08:01:40 | Glencourse (Kelani Ganga) | 8.52 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-20 08:01:10 | Giriulla (Maha Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-01-20 08:00:55 | Moragaswewa (Deduru Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-01-20 08:00:50 | Horowpothana (Yan Oya) | 1.48 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-20 08:00:25 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | -0.157 |  |
| 2026-01-20 08:00:10 | Siyambalanduwa (Heda Oya) | 0.68 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-20 08:00:05 | Nakkala (Kumbukkan Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-01-20 07:45:23 | Thalgahagoda (Nilwala Ganga) | 0.56 | 🟢 Normal | -0.173 |  |
| 2026-01-20 07:38:38 | Panadugama (Nilwala Ganga) | 2.09 | 🟢 Normal | 0.000 |  |
| 2026-01-20 07:20:36 | Moragaswewa (Deduru Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-01-20 07:12:04 | Pitabeddara (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-20 08:01:40 | Glencourse (Kelani Ganga) | 8.52 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-20 08:02:59 | Thaldena (Mahaweli Ganga) | 0.55 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-01-20 08:02:30 | Wellawaya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-20 08:06:34 | Thanthirimale (Malwathu Oya) | 1.51 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-20 08:00:50 | Horowpothana (Yan Oya) | 1.48 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-20 08:00:10 | Siyambalanduwa (Heda Oya) | 0.68 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-20 08:00:05 | Nakkala (Kumbukkan Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-01-20 08:00:55 | Moragaswewa (Deduru Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-01-20 07:02:00 | Yaka Wewa (Ma Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-01-20 08:01:10 | Giriulla (Maha Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-01-20 07:03:03 | Galgamuwa (Mee Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-01-20 08:04:40 | Magura (Kalu Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-01-20 08:03:16 | Pitabeddara (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-01-20 08:03:26 | Hanwella (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-01-20 08:02:07 | Deraniyagala (Kelani Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-01-20 08:04:04 | Ellagawa (Kalu Ganga) | 3.92 | 🟢 Normal | 0.000 |  |
| 2026-01-20 08:06:54 | Baddegama (Gin Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-01-20 07:38:38 | Panadugama (Nilwala Ganga) | 2.09 | 🟢 Normal | 0.000 |  |
| 2026-01-20 08:07:39 | Padiyathalawa (Maduru Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-01-20 07:01:17 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-01-20 07:03:47 | Dunamale (Aththanagalu Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-01-20 08:05:12 | Katharagama (Menik Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-01-20 08:06:35 | Badalgama (Maha Oya) | 1.89 | 🟢 Normal | 0.000 |  |
| 2026-01-20 08:06:39 | Holombuwa (Kelani Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-01-20 08:04:34 | Manampitiya (Mahaweli Ganga) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-01-20 07:03:50 | Rathnapura (Kalu Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-01-20 08:02:54 | Thawalama (Gin Ganga) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-01-20 08:05:15 | Peradeniya (Mahaweli Ganga) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-01-20 07:07:52 | Urawa (Nilwala Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-01-20 08:02:39 | Kuda Oya (Kirindi Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-01-20 07:04:02 | Thanamalwila (Kirindi Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-01-20 08:07:17 | Norwood (Kelani Ganga) | 0.44 | 🟢 Normal | -0.009 |  |
| 2026-01-20 08:06:22 | Kithulgala (Kelani Ganga) | 1.54 | 🟢 Normal | -0.009 |  |
| 2026-01-20 08:02:56 | Nawalapitiya (Mahaweli Ganga) | 0.64 | 🟢 Normal | -0.010 |  |
| 2026-01-20 07:00:44 | Weraganthota (Mahaweli Ganga) | -1.80 | 🟢 Normal | -0.011 |  |
| 2026-01-20 08:02:21 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.54 | 🟢 Normal | -0.060 |  |
| 2026-01-20 08:03:54 | Putupaula (Kalu Ganga) | 0.46 | 🟢 Normal | -0.137 |  |
| 2026-01-20 08:00:25 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | -0.157 |  |
| 2026-01-20 08:06:12 | Thalgahagoda (Nilwala Ganga) | 0.50 | 🟢 Normal | -0.173 |  |

## River Water Level Charts by Station

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

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

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

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

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)