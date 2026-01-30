# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--30_14:11:30-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **59,786 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-30 14:11:30 | Ellagawa (Kalu Ganga) | 3.79 | 🟢 Normal | -0.011 |  |
| 2026-01-30 14:10:16 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-01-30 14:09:28 | Holombuwa (Kelani Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-01-30 14:09:16 | Thanamalwila (Kirindi Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-01-30 14:08:39 | Thaldena (Mahaweli Ganga) | 0.65 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-01-30 14:06:44 | Peradeniya (Mahaweli Ganga) | 1.35 | 🟢 Normal | -0.079 |  |
| 2026-01-30 14:06:31 | Putupaula (Kalu Ganga) | 0.56 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-01-30 14:06:00 | Badalgama (Maha Oya) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-01-30 14:06:00 | Padiyathalawa (Maduru Oya) | 0.54 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-30 14:05:42 | Dunamale (Aththanagalu Oya) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-01-30 14:04:52 | Thawalama (Gin Ganga) | 0.87 | 🟢 Normal | -0.019 |  |
| 2026-01-30 14:04:38 | Moraketiya (Walawe Ganga) | 0.85 | 🟢 Normal | -0.012 |  |
| 2026-01-30 14:04:14 | Giriulla (Maha Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-01-30 14:04:00 | Magura (Kalu Ganga) | 0.61 | 🟢 Normal | -0.010 |  |
| 2026-01-30 14:03:52 | Hanwella (Kelani Ganga) | 0.33 | 🟢 Normal | -0.010 |  |
| 2026-01-30 14:03:46 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-30 14:03:17 | Panadugama (Nilwala Ganga) | 1.91 | 🟢 Normal | 0.000 |  |
| 2026-01-30 14:03:00 | Deraniyagala (Kelani Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-01-30 14:02:55 | Yaka Wewa (Ma Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-01-30 14:02:42 | Nakkala (Kumbukkan Oya) | 0.87 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-30 14:02:34 | Nawalapitiya (Mahaweli Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-01-30 14:02:28 | Baddegama (Gin Ganga) | 1.05 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-30 14:02:21 | Katharagama (Menik Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-01-30 14:02:21 | Galgamuwa (Mee Oya) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-01-30 14:02:17 | Wellawaya (Kirindi Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-01-30 14:02:15 | Siyambalanduwa (Heda Oya) | 0.62 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-30 14:02:07 | Kithulgala (Kelani Ganga) | 1.48 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-01-30 14:02:05 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.22 | 🟢 Normal | -0.030 |  |
| 2026-01-30 14:02:03 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-01-30 14:01:39 | Pitabeddara (Nilwala Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-01-30 14:01:26 | Glencourse (Kelani Ganga) | 8.44 | 🟢 Normal | -0.011 |  |
| 2026-01-30 14:01:24 | Horowpothana (Yan Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-01-30 14:00:54 | Manampitiya (Mahaweli Ganga) | 0.94 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-30 14:00:54 | Moragaswewa (Deduru Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-01-30 14:00:38 | Weraganthota (Mahaweli Ganga) | -1.90 | 🟢 Normal | 0.121 | 🔺 Rising |
| 2026-01-30 14:00:21 | Thanthirimale (Malwathu Oya) | 1.43 | 🟢 Normal | -0.010 |  |
| 2026-01-30 13:38:30 | Panadugama (Nilwala Ganga) | 1.91 | 🟢 Normal | 0.000 |  |
| 2026-01-30 13:19:10 | Thalgahagoda (Nilwala Ganga) | 0.31 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-01-30 13:17:56 | Rathnapura (Kalu Ganga) | 0.42 | 🟢 Normal | -0.009 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-30 14:00:38 | Weraganthota (Mahaweli Ganga) | -1.90 | 🟢 Normal | 0.121 | 🔺 Rising |
| 2026-01-30 14:02:07 | Kithulgala (Kelani Ganga) | 1.48 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-01-30 14:08:39 | Thaldena (Mahaweli Ganga) | 0.65 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-01-30 14:06:31 | Putupaula (Kalu Ganga) | 0.56 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-01-30 13:19:10 | Thalgahagoda (Nilwala Ganga) | 0.31 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-01-30 14:02:28 | Baddegama (Gin Ganga) | 1.05 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-30 14:02:15 | Siyambalanduwa (Heda Oya) | 0.62 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-30 14:00:54 | Manampitiya (Mahaweli Ganga) | 0.94 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-30 14:02:42 | Nakkala (Kumbukkan Oya) | 0.87 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-30 14:03:46 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-30 14:06:00 | Padiyathalawa (Maduru Oya) | 0.54 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-30 14:02:17 | Wellawaya (Kirindi Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-01-30 14:00:54 | Moragaswewa (Deduru Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-01-30 14:02:34 | Nawalapitiya (Mahaweli Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-01-30 14:02:55 | Yaka Wewa (Ma Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-01-30 14:04:14 | Giriulla (Maha Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-01-30 14:01:24 | Horowpothana (Yan Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-01-30 14:02:21 | Galgamuwa (Mee Oya) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-01-30 14:01:39 | Pitabeddara (Nilwala Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-01-30 14:03:00 | Deraniyagala (Kelani Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-01-30 14:03:17 | Panadugama (Nilwala Ganga) | 1.91 | 🟢 Normal | 0.000 |  |
| 2026-01-30 14:02:03 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-01-30 14:05:42 | Dunamale (Aththanagalu Oya) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-01-30 14:02:21 | Katharagama (Menik Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-01-30 14:06:00 | Badalgama (Maha Oya) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-01-30 14:09:28 | Holombuwa (Kelani Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-01-30 14:10:16 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-01-30 13:09:46 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-01-30 14:09:16 | Thanamalwila (Kirindi Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-01-30 13:17:56 | Rathnapura (Kalu Ganga) | 0.42 | 🟢 Normal | -0.009 |  |
| 2026-01-30 14:04:00 | Magura (Kalu Ganga) | 0.61 | 🟢 Normal | -0.010 |  |
| 2026-01-30 14:03:52 | Hanwella (Kelani Ganga) | 0.33 | 🟢 Normal | -0.010 |  |
| 2026-01-30 14:00:21 | Thanthirimale (Malwathu Oya) | 1.43 | 🟢 Normal | -0.010 |  |
| 2026-01-30 14:01:26 | Glencourse (Kelani Ganga) | 8.44 | 🟢 Normal | -0.011 |  |
| 2026-01-30 14:11:30 | Ellagawa (Kalu Ganga) | 3.79 | 🟢 Normal | -0.011 |  |
| 2026-01-30 14:04:38 | Moraketiya (Walawe Ganga) | 0.85 | 🟢 Normal | -0.012 |  |
| 2026-01-30 14:04:52 | Thawalama (Gin Ganga) | 0.87 | 🟢 Normal | -0.019 |  |
| 2026-01-30 14:02:05 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.22 | 🟢 Normal | -0.030 |  |
| 2026-01-30 14:06:44 | Peradeniya (Mahaweli Ganga) | 1.35 | 🟢 Normal | -0.079 |  |

## River Water Level Charts by Station

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

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

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)