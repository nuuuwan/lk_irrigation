# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--25_09:23:50-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **55,119 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-25 09:23:50 | Padiyathalawa (Maduru Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-01-25 09:16:47 | Panadugama (Nilwala Ganga) | 1.98 | 🟢 Normal | 0.000 |  |
| 2026-01-25 09:09:48 | Holombuwa (Kelani Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-01-25 09:08:47 | Horowpothana (Yan Oya) | 1.42 | 🟢 Normal | -0.009 |  |
| 2026-01-25 09:06:17 | Thanamalwila (Kirindi Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-01-25 09:06:09 | Magura (Kalu Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-01-25 09:04:59 | Urawa (Nilwala Ganga) | 0.06 | 🟢 Normal | -0.010 |  |
| 2026-01-25 09:04:46 | Thalgahagoda (Nilwala Ganga) | 0.43 | 🟢 Normal | -0.009 |  |
| 2026-01-25 09:03:59 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-01-25 09:03:55 | Galgamuwa (Mee Oya) | 0.15 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-25 09:03:48 | Hanwella (Kelani Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-01-25 09:03:39 | Rathnapura (Kalu Ganga) | 0.51 | 🟢 Normal | -0.010 |  |
| 2026-01-25 09:03:36 | Thawalama (Gin Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-01-25 09:03:31 | Thaldena (Mahaweli Ganga) | 0.47 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-25 09:03:27 | Siyambalanduwa (Heda Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-01-25 09:03:24 | Manampitiya (Mahaweli Ganga) | 0.95 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-01-25 09:03:15 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.39 | 🟢 Normal | -0.049 |  |
| 2026-01-25 09:03:10 | Giriulla (Maha Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-01-25 09:03:01 | Deraniyagala (Kelani Ganga) | 0.24 | 🟢 Normal | 0.114 | 🔺 Rising |
| 2026-01-25 09:02:59 | Baddegama (Gin Ganga) | 1.15 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-01-25 09:02:59 | Dunamale (Aththanagalu Oya) | 0.40 | 🟢 Normal | -0.010 |  |
| 2026-01-25 09:02:47 | Pitabeddara (Nilwala Ganga) | 0.28 | 🟢 Normal | -0.012 |  |
| 2026-01-25 09:02:39 | Glencourse (Kelani Ganga) | 8.48 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-25 09:02:18 | Putupaula (Kalu Ganga) | 0.54 | 🟢 Normal | -0.098 |  |
| 2026-01-25 09:02:12 | Katharagama (Menik Ganga) | -0.01 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-25 09:02:10 | Badalgama (Maha Oya) | 1.87 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-25 09:02:05 | Weraganthota (Mahaweli Ganga) | -1.92 | 🟢 Normal | -0.444 |  |
| 2026-01-25 09:01:54 | Yaka Wewa (Ma Oya) | 1.28 | 🟢 Normal | -0.043 |  |
| 2026-01-25 09:01:49 | Peradeniya (Mahaweli Ganga) | 1.30 | 🟢 Normal | 0.118 | 🔺 Rising |
| 2026-01-25 09:01:47 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | -0.062 |  |
| 2026-01-25 09:01:47 | Moragaswewa (Deduru Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-01-25 09:01:46 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-01-25 09:01:45 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-01-25 09:01:44 | Kithulgala (Kelani Ganga) | 1.60 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-01-25 09:01:27 | Wellawaya (Kirindi Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-01-25 09:01:23 | Nawalapitiya (Mahaweli Ganga) | 0.64 | 🟢 Normal | -0.010 |  |
| 2026-01-25 09:00:44 | Weraganthota (Mahaweli Ganga) | -1.91 | 🟢 Normal | -0.444 |  |
| 2026-01-25 09:00:40 | Thanthirimale (Malwathu Oya) | 1.51 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-01-25 09:00:34 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-01-25 09:00:21 | Nakkala (Kumbukkan Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-01-25 09:00:21 | Ellagawa (Kalu Ganga) | 3.80 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-25 09:01:49 | Peradeniya (Mahaweli Ganga) | 1.30 | 🟢 Normal | 0.118 | 🔺 Rising |
| 2026-01-25 09:03:01 | Deraniyagala (Kelani Ganga) | 0.24 | 🟢 Normal | 0.114 | 🔺 Rising |
| 2026-01-25 09:02:59 | Baddegama (Gin Ganga) | 1.15 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-01-25 09:01:44 | Kithulgala (Kelani Ganga) | 1.60 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-01-25 09:00:40 | Thanthirimale (Malwathu Oya) | 1.51 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-01-25 09:03:24 | Manampitiya (Mahaweli Ganga) | 0.95 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-01-25 09:03:31 | Thaldena (Mahaweli Ganga) | 0.47 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-25 09:03:55 | Galgamuwa (Mee Oya) | 0.15 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-25 09:02:39 | Glencourse (Kelani Ganga) | 8.48 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-25 09:02:12 | Katharagama (Menik Ganga) | -0.01 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-25 09:02:10 | Badalgama (Maha Oya) | 1.87 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-25 09:01:27 | Wellawaya (Kirindi Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-01-25 09:00:21 | Nakkala (Kumbukkan Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-01-25 09:01:47 | Moragaswewa (Deduru Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-01-25 09:03:10 | Giriulla (Maha Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-01-25 09:06:09 | Magura (Kalu Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-01-25 09:03:59 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-01-25 09:03:48 | Hanwella (Kelani Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-01-25 09:00:21 | Ellagawa (Kalu Ganga) | 3.80 | 🟢 Normal | 0.000 |  |
| 2026-01-25 09:16:47 | Panadugama (Nilwala Ganga) | 1.98 | 🟢 Normal | 0.000 |  |
| 2026-01-25 09:23:50 | Padiyathalawa (Maduru Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-01-25 09:01:45 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-01-25 09:03:27 | Siyambalanduwa (Heda Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-01-25 09:09:48 | Holombuwa (Kelani Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-01-25 09:03:36 | Thawalama (Gin Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-01-25 09:01:46 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-01-25 09:06:17 | Thanamalwila (Kirindi Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-01-25 09:08:47 | Horowpothana (Yan Oya) | 1.42 | 🟢 Normal | -0.009 |  |
| 2026-01-25 09:04:46 | Thalgahagoda (Nilwala Ganga) | 0.43 | 🟢 Normal | -0.009 |  |
| 2026-01-25 09:04:59 | Urawa (Nilwala Ganga) | 0.06 | 🟢 Normal | -0.010 |  |
| 2026-01-25 09:01:23 | Nawalapitiya (Mahaweli Ganga) | 0.64 | 🟢 Normal | -0.010 |  |
| 2026-01-25 09:03:39 | Rathnapura (Kalu Ganga) | 0.51 | 🟢 Normal | -0.010 |  |
| 2026-01-25 09:02:59 | Dunamale (Aththanagalu Oya) | 0.40 | 🟢 Normal | -0.010 |  |
| 2026-01-25 09:02:47 | Pitabeddara (Nilwala Ganga) | 0.28 | 🟢 Normal | -0.012 |  |
| 2026-01-25 09:01:54 | Yaka Wewa (Ma Oya) | 1.28 | 🟢 Normal | -0.043 |  |
| 2026-01-25 09:03:15 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.39 | 🟢 Normal | -0.049 |  |
| 2026-01-25 09:01:47 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | -0.062 |  |
| 2026-01-25 09:02:18 | Putupaula (Kalu Ganga) | 0.54 | 🟢 Normal | -0.098 |  |
| 2026-01-25 09:02:05 | Weraganthota (Mahaweli Ganga) | -1.92 | 🟢 Normal | -0.444 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)