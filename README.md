# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--20_10:12:04-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **50,655 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-20 10:12:04 | Giriulla (Maha Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-01-20 10:12:04 | Yaka Wewa (Ma Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-01-20 10:11:52 | Thawalama (Gin Ganga) | 1.02 | 🟢 Normal | -0.009 |  |
| 2026-01-20 10:10:49 | Manampitiya (Mahaweli Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-01-20 10:08:07 | Nagalagam Street (Kelani Ganga) | 0.17 | 🟢 Normal | -0.030 |  |
| 2026-01-20 10:07:09 | Peradeniya (Mahaweli Ganga) | 1.83 | 🟢 Normal | 0.308 | 🔺 Rising |
| 2026-01-20 10:06:21 | Badalgama (Maha Oya) | 1.90 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-20 10:06:09 | Magura (Kalu Ganga) | 0.73 | 🟢 Normal | -0.009 |  |
| 2026-01-20 10:06:06 | Thanthirimale (Malwathu Oya) | 1.51 | 🟢 Normal | 0.000 |  |
| 2026-01-20 10:05:31 | Kithulgala (Kelani Ganga) | 1.32 | 🟢 Normal | -0.245 |  |
| 2026-01-20 10:05:28 | Panadugama (Nilwala Ganga) | 2.08 | 🟢 Normal | -0.012 |  |
| 2026-01-20 10:05:22 | Padiyathalawa (Maduru Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-01-20 10:05:21 | Urawa (Nilwala Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-01-20 10:05:04 | Holombuwa (Kelani Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-01-20 10:04:54 | Rathnapura (Kalu Ganga) | 0.55 | 🟢 Normal | -0.010 |  |
| 2026-01-20 10:04:20 | Galgamuwa (Mee Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-01-20 10:04:17 | Katharagama (Menik Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-01-20 10:04:06 | Hanwella (Kelani Ganga) | 0.39 | 🟢 Normal | -0.020 |  |
| 2026-01-20 10:03:54 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-20 10:03:50 | Glencourse (Kelani Ganga) | 8.40 | 🟢 Normal | -0.071 |  |
| 2026-01-20 10:03:49 | Kuda Oya (Kirindi Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-01-20 10:03:41 | Wellawaya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-01-20 10:03:18 | Putupaula (Kalu Ganga) | 0.27 | 🟢 Normal | -0.079 |  |
| 2026-01-20 10:03:10 | Thaldena (Mahaweli Ganga) | 0.56 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-20 10:02:45 | Baddegama (Gin Ganga) | 1.19 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-01-20 10:02:43 | Deraniyagala (Kelani Ganga) | 0.11 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-20 10:02:40 | Dunamale (Aththanagalu Oya) | 0.57 | 🟢 Normal | -0.010 |  |
| 2026-01-20 10:02:38 | Norwood (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-01-20 10:02:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.43 | 🟢 Normal | -0.050 |  |
| 2026-01-20 10:02:15 | Ellagawa (Kalu Ganga) | 3.91 | 🟢 Normal | -0.011 |  |
| 2026-01-20 10:01:37 | Thanamalwila (Kirindi Oya) | 0.71 | 🟢 Normal | -0.020 |  |
| 2026-01-20 10:01:37 | Siyambalanduwa (Heda Oya) | 0.69 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-20 10:01:23 | Weraganthota (Mahaweli Ganga) | -1.84 | 🟢 Normal | -0.030 |  |
| 2026-01-20 10:01:15 | Moragaswewa (Deduru Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-01-20 10:01:14 | Nawalapitiya (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-20 10:01:09 | Pitabeddara (Nilwala Ganga) | 0.34 | 🟢 Normal | -0.010 |  |
| 2026-01-20 10:00:45 | Thalgahagoda (Nilwala Ganga) | 0.39 | 🟢 Normal | -0.065 |  |
| 2026-01-20 10:00:27 | Nakkala (Kumbukkan Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-01-20 10:00:25 | Horowpothana (Yan Oya) | 1.48 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-20 10:07:09 | Peradeniya (Mahaweli Ganga) | 1.83 | 🟢 Normal | 0.308 | 🔺 Rising |
| 2026-01-20 10:01:14 | Nawalapitiya (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-20 10:02:45 | Baddegama (Gin Ganga) | 1.19 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-01-20 10:02:43 | Deraniyagala (Kelani Ganga) | 0.11 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-20 10:01:37 | Siyambalanduwa (Heda Oya) | 0.69 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-20 10:06:21 | Badalgama (Maha Oya) | 1.90 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-20 10:03:54 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-20 10:03:10 | Thaldena (Mahaweli Ganga) | 0.56 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-20 10:03:41 | Wellawaya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-01-20 10:00:27 | Nakkala (Kumbukkan Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-01-20 10:01:15 | Moragaswewa (Deduru Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-01-20 10:12:04 | Yaka Wewa (Ma Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-01-20 10:12:04 | Giriulla (Maha Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-01-20 10:00:25 | Horowpothana (Yan Oya) | 1.48 | 🟢 Normal | 0.000 |  |
| 2026-01-20 10:04:20 | Galgamuwa (Mee Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-01-20 10:02:38 | Norwood (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-01-20 10:05:22 | Padiyathalawa (Maduru Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-01-20 10:04:17 | Katharagama (Menik Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-01-20 10:05:04 | Holombuwa (Kelani Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-01-20 10:10:49 | Manampitiya (Mahaweli Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-01-20 10:06:06 | Thanthirimale (Malwathu Oya) | 1.51 | 🟢 Normal | 0.000 |  |
| 2026-01-20 10:05:21 | Urawa (Nilwala Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-01-20 10:03:49 | Kuda Oya (Kirindi Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-01-20 10:11:52 | Thawalama (Gin Ganga) | 1.02 | 🟢 Normal | -0.009 |  |
| 2026-01-20 10:06:09 | Magura (Kalu Ganga) | 0.73 | 🟢 Normal | -0.009 |  |
| 2026-01-20 10:04:54 | Rathnapura (Kalu Ganga) | 0.55 | 🟢 Normal | -0.010 |  |
| 2026-01-20 10:01:09 | Pitabeddara (Nilwala Ganga) | 0.34 | 🟢 Normal | -0.010 |  |
| 2026-01-20 10:02:40 | Dunamale (Aththanagalu Oya) | 0.57 | 🟢 Normal | -0.010 |  |
| 2026-01-20 10:02:15 | Ellagawa (Kalu Ganga) | 3.91 | 🟢 Normal | -0.011 |  |
| 2026-01-20 10:05:28 | Panadugama (Nilwala Ganga) | 2.08 | 🟢 Normal | -0.012 |  |
| 2026-01-20 10:01:37 | Thanamalwila (Kirindi Oya) | 0.71 | 🟢 Normal | -0.020 |  |
| 2026-01-20 10:04:06 | Hanwella (Kelani Ganga) | 0.39 | 🟢 Normal | -0.020 |  |
| 2026-01-20 10:01:23 | Weraganthota (Mahaweli Ganga) | -1.84 | 🟢 Normal | -0.030 |  |
| 2026-01-20 10:08:07 | Nagalagam Street (Kelani Ganga) | 0.17 | 🟢 Normal | -0.030 |  |
| 2026-01-20 10:02:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.43 | 🟢 Normal | -0.050 |  |
| 2026-01-20 10:00:45 | Thalgahagoda (Nilwala Ganga) | 0.39 | 🟢 Normal | -0.065 |  |
| 2026-01-20 10:03:50 | Glencourse (Kelani Ganga) | 8.40 | 🟢 Normal | -0.071 |  |
| 2026-01-20 10:03:18 | Putupaula (Kalu Ganga) | 0.27 | 🟢 Normal | -0.079 |  |
| 2026-01-20 10:05:31 | Kithulgala (Kelani Ganga) | 1.32 | 🟢 Normal | -0.245 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)