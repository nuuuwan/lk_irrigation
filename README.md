# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--10_14:16:03-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **121,333 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-10 14:16:03 | Panadugama (Nilwala Ganga) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-04-10 14:13:46 | Moragaswewa (Deduru Oya) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-04-10 14:13:39 | Magura (Kalu Ganga) | 0.68 | 🟢 Normal | -0.011 |  |
| 2026-04-10 14:12:18 | Pitabeddara (Nilwala Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-04-10 14:10:45 | Thawalama (Gin Ganga) | 1.10 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-04-10 14:10:31 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-10 14:09:53 | Thalgahagoda (Nilwala Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-04-10 14:09:36 | Baddegama (Gin Ganga) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-04-10 14:08:37 | Peradeniya (Mahaweli Ganga) | 1.00 | 🟢 Normal | -0.018 |  |
| 2026-04-10 14:05:48 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-04-10 14:05:41 | Holombuwa (Kelani Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-04-10 14:05:34 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-04-10 14:05:26 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | -0.009 |  |
| 2026-04-10 14:05:25 | Deraniyagala (Kelani Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-04-10 14:05:07 | Rathnapura (Kalu Ganga) | 0.53 | 🟢 Normal | -0.049 |  |
| 2026-04-10 14:04:52 | Badalgama (Maha Oya) | 1.81 | 🟢 Normal | 0.000 |  |
| 2026-04-10 14:04:45 | Kuda Oya (Kirindi Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-04-10 14:04:10 | Urawa (Nilwala Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-04-10 14:04:01 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-10 14:03:59 | Glencourse (Kelani Ganga) | 8.41 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-04-10 14:03:55 | Horowpothana (Yan Oya) | 1.43 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-04-10 14:03:53 | Thaldena (Mahaweli Ganga) | 0.22 | 🟢 Normal | -0.010 |  |
| 2026-04-10 14:03:15 | Hanwella (Kelani Ganga) | 0.32 | 🟢 Normal | -0.030 |  |
| 2026-04-10 14:03:07 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-04-10 14:03:07 | Norwood (Kelani Ganga) | 0.37 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-10 14:02:30 | Kithulgala (Kelani Ganga) | 1.41 | 🟢 Normal | 0.000 |  |
| 2026-04-10 14:02:22 | Padiyathalawa (Maduru Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-04-10 14:02:13 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.26 | 🟢 Normal | -0.020 |  |
| 2026-04-10 14:02:13 | Putupaula (Kalu Ganga) | 0.36 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-04-10 14:01:48 | Ellagawa (Kalu Ganga) | 3.98 | 🟢 Normal | -0.010 |  |
| 2026-04-10 14:01:47 | Nakkala (Kumbukkan Oya) | 0.69 | 🟢 Normal | -0.010 |  |
| 2026-04-10 14:01:42 | Giriulla (Maha Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-04-10 14:01:12 | Thanamalwila (Kirindi Oya) | 0.25 | 🟢 Normal | -0.010 |  |
| 2026-04-10 14:00:56 | Wellawaya (Kirindi Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-04-10 14:00:55 | Manampitiya (Mahaweli Ganga) | 0.11 | 🟢 Normal | -0.024 |  |
| 2026-04-10 14:00:42 | Thanthirimale (Malwathu Oya) | 1.14 | 🟢 Normal | -0.010 |  |
| 2026-04-10 14:00:09 | Weraganthota (Mahaweli Ganga) | -2.86 | 🟢 Normal | 0.000 |  |
| 2026-04-10 13:59:19 | Weraganthota (Mahaweli Ganga) | -2.86 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-10 14:10:45 | Thawalama (Gin Ganga) | 1.10 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-04-10 14:02:13 | Putupaula (Kalu Ganga) | 0.36 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-04-10 14:03:59 | Glencourse (Kelani Ganga) | 8.41 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-04-10 14:03:55 | Horowpothana (Yan Oya) | 1.43 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-04-10 14:03:07 | Norwood (Kelani Ganga) | 0.37 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-10 13:01:05 | Nawalapitiya (Mahaweli Ganga) | 0.49 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-10 14:05:48 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-04-10 14:02:30 | Kithulgala (Kelani Ganga) | 1.41 | 🟢 Normal | 0.000 |  |
| 2026-04-10 14:00:09 | Weraganthota (Mahaweli Ganga) | -2.86 | 🟢 Normal | 0.000 |  |
| 2026-04-10 14:00:56 | Wellawaya (Kirindi Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-04-10 14:13:46 | Moragaswewa (Deduru Oya) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-04-10 14:04:01 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-10 14:01:42 | Giriulla (Maha Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-04-10 13:17:39 | Galgamuwa (Mee Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-04-10 14:12:18 | Pitabeddara (Nilwala Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-04-10 14:05:25 | Deraniyagala (Kelani Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-04-10 14:09:36 | Baddegama (Gin Ganga) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-04-10 14:16:03 | Panadugama (Nilwala Ganga) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-04-10 14:02:22 | Padiyathalawa (Maduru Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-04-10 14:05:34 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-04-10 14:10:31 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-10 14:03:07 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-04-10 14:04:52 | Badalgama (Maha Oya) | 1.81 | 🟢 Normal | 0.000 |  |
| 2026-04-10 14:05:41 | Holombuwa (Kelani Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-04-10 14:04:10 | Urawa (Nilwala Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-04-10 14:09:53 | Thalgahagoda (Nilwala Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-04-10 14:04:45 | Kuda Oya (Kirindi Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-04-10 14:05:26 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | -0.009 |  |
| 2026-04-10 14:01:47 | Nakkala (Kumbukkan Oya) | 0.69 | 🟢 Normal | -0.010 |  |
| 2026-04-10 14:01:48 | Ellagawa (Kalu Ganga) | 3.98 | 🟢 Normal | -0.010 |  |
| 2026-04-10 14:01:12 | Thanamalwila (Kirindi Oya) | 0.25 | 🟢 Normal | -0.010 |  |
| 2026-04-10 14:00:42 | Thanthirimale (Malwathu Oya) | 1.14 | 🟢 Normal | -0.010 |  |
| 2026-04-10 14:03:53 | Thaldena (Mahaweli Ganga) | 0.22 | 🟢 Normal | -0.010 |  |
| 2026-04-10 14:13:39 | Magura (Kalu Ganga) | 0.68 | 🟢 Normal | -0.011 |  |
| 2026-04-10 14:08:37 | Peradeniya (Mahaweli Ganga) | 1.00 | 🟢 Normal | -0.018 |  |
| 2026-04-10 14:02:13 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.26 | 🟢 Normal | -0.020 |  |
| 2026-04-10 14:00:55 | Manampitiya (Mahaweli Ganga) | 0.11 | 🟢 Normal | -0.024 |  |
| 2026-04-10 14:03:15 | Hanwella (Kelani Ganga) | 0.32 | 🟢 Normal | -0.030 |  |
| 2026-04-10 14:05:07 | Rathnapura (Kalu Ganga) | 0.53 | 🟢 Normal | -0.049 |  |

## River Water Level Charts by Station

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

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

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

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

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)