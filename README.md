# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--02_10:37:42-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **62,355 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-02 10:37:42 | Nakkala (Kumbukkan Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-02-02 10:29:39 | Thalgahagoda (Nilwala Ganga) | 0.33 | 🟢 Normal | -0.020 |  |
| 2026-02-02 10:19:54 | Rathnapura (Kalu Ganga) | 0.95 | 🟢 Normal | -0.026 |  |
| 2026-02-02 10:13:07 | Thawalama (Gin Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-02-02 10:12:10 | Galgamuwa (Mee Oya) | 0.36 | 🟢 Normal | -0.009 |  |
| 2026-02-02 10:09:47 | Urawa (Nilwala Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-02-02 10:09:45 | Ellagawa (Kalu Ganga) | 4.50 | 🟢 Normal | -0.035 |  |
| 2026-02-02 10:08:57 | Magura (Kalu Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-02-02 10:08:39 | Manampitiya (Mahaweli Ganga) | 1.50 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-02-02 10:08:36 | Peradeniya (Mahaweli Ganga) | 1.82 | 🟢 Normal | 0.197 | 🔺 Rising |
| 2026-02-02 10:06:50 | Giriulla (Maha Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-02-02 10:06:17 | Dunamale (Aththanagalu Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-02-02 10:06:13 | Holombuwa (Kelani Ganga) | 0.37 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-02 10:05:57 | Siyambalanduwa (Heda Oya) | 0.56 | 🟢 Normal | -0.010 |  |
| 2026-02-02 10:05:52 | Weraganthota (Mahaweli Ganga) | -1.96 | 🟢 Normal | 0.258 | 🔺 Rising |
| 2026-02-02 10:05:22 | Thanamalwila (Kirindi Oya) | 0.49 | 🟢 Normal | -0.010 |  |
| 2026-02-02 10:05:12 | Panadugama (Nilwala Ganga) | 2.24 | 🟢 Normal | -0.011 |  |
| 2026-02-02 10:05:11 | Badalgama (Maha Oya) | 1.91 | 🟢 Normal | 0.000 |  |
| 2026-02-02 10:04:47 | Baddegama (Gin Ganga) | 1.22 | 🟢 Normal | -0.043 |  |
| 2026-02-02 10:04:25 | Thaldena (Mahaweli Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-02-02 10:04:02 | Padiyathalawa (Maduru Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-02-02 10:03:34 | Hanwella (Kelani Ganga) | 0.39 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-02-02 10:03:30 | Yaka Wewa (Ma Oya) | 1.06 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-02-02 10:03:28 | Putupaula (Kalu Ganga) | 0.32 | 🟢 Normal | -0.020 |  |
| 2026-02-02 10:02:57 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-02-02 10:02:51 | Glencourse (Kelani Ganga) | 8.56 | 🟢 Normal | -0.010 |  |
| 2026-02-02 10:02:48 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-02-02 10:02:46 | Kithulgala (Kelani Ganga) | 1.67 | 🟢 Normal | 0.128 | 🔺 Rising |
| 2026-02-02 10:02:45 | Giriulla (Maha Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-02-02 10:02:38 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-02-02 10:02:38 | Deraniyagala (Kelani Ganga) | 0.15 | 🟢 Normal | -0.062 |  |
| 2026-02-02 10:02:33 | Katharagama (Menik Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-02-02 10:02:28 | Thawalama (Gin Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-02-02 10:02:16 | Nagalagam Street (Kelani Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-02-02 10:02:15 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.78 | 🟢 Normal | -0.070 |  |
| 2026-02-02 10:02:06 | Wellawaya (Kirindi Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-02-02 10:02:02 | Nawalapitiya (Mahaweli Ganga) | 0.70 | 🟢 Normal | -0.010 |  |
| 2026-02-02 10:01:54 | Moragaswewa (Deduru Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-02-02 10:01:24 | Pitabeddara (Nilwala Ganga) | 0.53 | 🟢 Normal | -0.040 |  |
| 2026-02-02 10:01:03 | Thanthirimale (Malwathu Oya) | 2.63 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-02-02 10:00:59 | Horowpothana (Yan Oya) | 1.81 | 🟢 Normal | 0.010 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-02 10:05:52 | Weraganthota (Mahaweli Ganga) | -1.96 | 🟢 Normal | 0.258 | 🔺 Rising |
| 2026-02-02 10:08:36 | Peradeniya (Mahaweli Ganga) | 1.82 | 🟢 Normal | 0.197 | 🔺 Rising |
| 2026-02-02 10:02:46 | Kithulgala (Kelani Ganga) | 1.67 | 🟢 Normal | 0.128 | 🔺 Rising |
| 2026-02-02 10:03:34 | Hanwella (Kelani Ganga) | 0.39 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-02-02 10:03:30 | Yaka Wewa (Ma Oya) | 1.06 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-02-02 10:01:03 | Thanthirimale (Malwathu Oya) | 2.63 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-02-02 10:08:39 | Manampitiya (Mahaweli Ganga) | 1.50 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-02-02 10:06:13 | Holombuwa (Kelani Ganga) | 0.37 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-02 10:00:59 | Horowpothana (Yan Oya) | 1.81 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-02 10:02:06 | Wellawaya (Kirindi Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-02-02 10:37:42 | Nakkala (Kumbukkan Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-02-02 10:01:54 | Moragaswewa (Deduru Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-02-02 10:06:50 | Giriulla (Maha Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-02-02 10:08:57 | Magura (Kalu Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-02-02 10:02:57 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-02-02 10:04:02 | Padiyathalawa (Maduru Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-02-02 10:02:16 | Nagalagam Street (Kelani Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-02-02 10:02:38 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-02-02 10:06:17 | Dunamale (Aththanagalu Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-02-02 10:04:25 | Thaldena (Mahaweli Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-02-02 10:02:33 | Katharagama (Menik Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-02-02 10:05:11 | Badalgama (Maha Oya) | 1.91 | 🟢 Normal | 0.000 |  |
| 2026-02-02 10:13:07 | Thawalama (Gin Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-02-02 10:09:47 | Urawa (Nilwala Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-02-02 10:02:48 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-02-02 10:12:10 | Galgamuwa (Mee Oya) | 0.36 | 🟢 Normal | -0.009 |  |
| 2026-02-02 10:05:22 | Thanamalwila (Kirindi Oya) | 0.49 | 🟢 Normal | -0.010 |  |
| 2026-02-02 10:05:57 | Siyambalanduwa (Heda Oya) | 0.56 | 🟢 Normal | -0.010 |  |
| 2026-02-02 10:02:02 | Nawalapitiya (Mahaweli Ganga) | 0.70 | 🟢 Normal | -0.010 |  |
| 2026-02-02 10:02:51 | Glencourse (Kelani Ganga) | 8.56 | 🟢 Normal | -0.010 |  |
| 2026-02-02 10:05:12 | Panadugama (Nilwala Ganga) | 2.24 | 🟢 Normal | -0.011 |  |
| 2026-02-02 10:03:28 | Putupaula (Kalu Ganga) | 0.32 | 🟢 Normal | -0.020 |  |
| 2026-02-02 10:29:39 | Thalgahagoda (Nilwala Ganga) | 0.33 | 🟢 Normal | -0.020 |  |
| 2026-02-02 10:19:54 | Rathnapura (Kalu Ganga) | 0.95 | 🟢 Normal | -0.026 |  |
| 2026-02-02 10:09:45 | Ellagawa (Kalu Ganga) | 4.50 | 🟢 Normal | -0.035 |  |
| 2026-02-02 10:01:24 | Pitabeddara (Nilwala Ganga) | 0.53 | 🟢 Normal | -0.040 |  |
| 2026-02-02 10:04:47 | Baddegama (Gin Ganga) | 1.22 | 🟢 Normal | -0.043 |  |
| 2026-02-02 10:02:38 | Deraniyagala (Kelani Ganga) | 0.15 | 🟢 Normal | -0.062 |  |
| 2026-02-02 10:02:15 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.78 | 🟢 Normal | -0.070 |  |

## River Water Level Charts by Station

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

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

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)