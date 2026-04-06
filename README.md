# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--06_11:16:06-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **117,666 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-06 11:16:06 | Weraganthota (Mahaweli Ganga) | -1.90 | 🟢 Normal | -0.008 |  |
| 2026-04-06 11:14:40 | Galgamuwa (Mee Oya) | 0.10 | 🟢 Normal | -0.009 |  |
| 2026-04-06 11:13:07 | Horowpothana (Yan Oya) | 1.45 | 🟢 Normal | -0.008 |  |
| 2026-04-06 11:10:00 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-06 11:09:46 | Magura (Kalu Ganga) | 0.70 | 🟢 Normal | -0.009 |  |
| 2026-04-06 11:09:39 | Holombuwa (Kelani Ganga) | 0.24 | 🟢 Normal | -0.009 |  |
| 2026-04-06 11:09:30 | Panadugama (Nilwala Ganga) | 1.96 | 🟢 Normal | -0.009 |  |
| 2026-04-06 11:09:24 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | 0.226 | 🔺 Rising |
| 2026-04-06 11:08:53 | Urawa (Nilwala Ganga) | -0.03 | 🟢 Normal | -0.010 |  |
| 2026-04-06 11:08:47 | Thalgahagoda (Nilwala Ganga) | 0.26 | 🟢 Normal | -0.084 |  |
| 2026-04-06 11:05:54 | Glencourse (Kelani Ganga) | 8.36 | 🟢 Normal | -0.089 |  |
| 2026-04-06 11:05:37 | Peradeniya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-04-06 11:05:18 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-04-06 11:05:03 | Rathnapura (Kalu Ganga) | 0.71 | 🟢 Normal | -0.010 |  |
| 2026-04-06 11:04:44 | Baddegama (Gin Ganga) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-04-06 11:04:36 | Badalgama (Maha Oya) | 1.84 | 🟢 Normal | -0.010 |  |
| 2026-04-06 11:04:10 | Nagalagam Street (Kelani Ganga) | 0.18 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-04-06 11:04:05 | Pitabeddara (Nilwala Ganga) | 0.19 | 🟢 Normal | -0.039 |  |
| 2026-04-06 11:03:59 | Kuda Oya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-04-06 11:03:50 | Thawalama (Gin Ganga) | 1.07 | 🟢 Normal | -0.010 |  |
| 2026-04-06 11:03:38 | Siyambalanduwa (Heda Oya) | 0.52 | 🟢 Normal | -0.010 |  |
| 2026-04-06 11:03:34 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-04-06 11:03:25 | Hanwella (Kelani Ganga) | 0.40 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-06 11:03:01 | Giriulla (Maha Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-04-06 11:02:59 | Putupaula (Kalu Ganga) | 0.33 | 🟢 Normal | 0.132 | 🔺 Rising |
| 2026-04-06 11:02:52 | Thanamalwila (Kirindi Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-04-06 11:02:42 | Deraniyagala (Kelani Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-04-06 11:02:37 | Katharagama (Menik Ganga) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-04-06 11:02:23 | Wellawaya (Kirindi Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-06 11:02:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-04-06 11:02:02 | Padiyathalawa (Maduru Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-04-06 11:01:43 | Nawalapitiya (Mahaweli Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-04-06 11:01:39 | Thaldena (Mahaweli Ganga) | 0.25 | 🟢 Normal | -0.010 |  |
| 2026-04-06 11:01:30 | Thanthirimale (Malwathu Oya) | 1.84 | 🟢 Normal | -0.030 |  |
| 2026-04-06 11:01:09 | Ellagawa (Kalu Ganga) | 3.98 | 🟢 Normal | -0.020 |  |
| 2026-04-06 11:00:41 | Manampitiya (Mahaweli Ganga) | 0.30 | 🟢 Normal | -0.051 |  |
| 2026-04-06 11:00:34 | Moragaswewa (Deduru Oya) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-04-06 11:00:12 | Nakkala (Kumbukkan Oya) | 0.67 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-06 11:09:24 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | 0.226 | 🔺 Rising |
| 2026-04-06 11:02:59 | Putupaula (Kalu Ganga) | 0.33 | 🟢 Normal | 0.132 | 🔺 Rising |
| 2026-04-06 11:04:10 | Nagalagam Street (Kelani Ganga) | 0.18 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-04-06 11:03:25 | Hanwella (Kelani Ganga) | 0.40 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-06 11:02:23 | Wellawaya (Kirindi Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-06 11:00:12 | Nakkala (Kumbukkan Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-04-06 11:00:34 | Moragaswewa (Deduru Oya) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-04-06 11:01:43 | Nawalapitiya (Mahaweli Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-04-06 10:02:07 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-04-06 11:03:01 | Giriulla (Maha Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-04-06 11:05:18 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-04-06 11:02:42 | Deraniyagala (Kelani Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-04-06 11:04:44 | Baddegama (Gin Ganga) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-04-06 11:02:02 | Padiyathalawa (Maduru Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-04-06 11:03:34 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-04-06 11:10:00 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-06 11:02:37 | Katharagama (Menik Ganga) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-04-06 11:05:37 | Peradeniya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-04-06 11:03:59 | Kuda Oya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-04-06 11:02:52 | Thanamalwila (Kirindi Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-04-06 11:02:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-04-06 11:16:06 | Weraganthota (Mahaweli Ganga) | -1.90 | 🟢 Normal | -0.008 |  |
| 2026-04-06 11:13:07 | Horowpothana (Yan Oya) | 1.45 | 🟢 Normal | -0.008 |  |
| 2026-04-06 11:14:40 | Galgamuwa (Mee Oya) | 0.10 | 🟢 Normal | -0.009 |  |
| 2026-04-06 11:09:39 | Holombuwa (Kelani Ganga) | 0.24 | 🟢 Normal | -0.009 |  |
| 2026-04-06 11:09:46 | Magura (Kalu Ganga) | 0.70 | 🟢 Normal | -0.009 |  |
| 2026-04-06 11:09:30 | Panadugama (Nilwala Ganga) | 1.96 | 🟢 Normal | -0.009 |  |
| 2026-04-06 11:03:38 | Siyambalanduwa (Heda Oya) | 0.52 | 🟢 Normal | -0.010 |  |
| 2026-04-06 11:05:03 | Rathnapura (Kalu Ganga) | 0.71 | 🟢 Normal | -0.010 |  |
| 2026-04-06 11:08:53 | Urawa (Nilwala Ganga) | -0.03 | 🟢 Normal | -0.010 |  |
| 2026-04-06 11:03:50 | Thawalama (Gin Ganga) | 1.07 | 🟢 Normal | -0.010 |  |
| 2026-04-06 11:01:39 | Thaldena (Mahaweli Ganga) | 0.25 | 🟢 Normal | -0.010 |  |
| 2026-04-06 11:04:36 | Badalgama (Maha Oya) | 1.84 | 🟢 Normal | -0.010 |  |
| 2026-04-06 11:01:09 | Ellagawa (Kalu Ganga) | 3.98 | 🟢 Normal | -0.020 |  |
| 2026-04-06 11:01:30 | Thanthirimale (Malwathu Oya) | 1.84 | 🟢 Normal | -0.030 |  |
| 2026-04-06 11:04:05 | Pitabeddara (Nilwala Ganga) | 0.19 | 🟢 Normal | -0.039 |  |
| 2026-04-06 11:00:41 | Manampitiya (Mahaweli Ganga) | 0.30 | 🟢 Normal | -0.051 |  |
| 2026-04-06 11:08:47 | Thalgahagoda (Nilwala Ganga) | 0.26 | 🟢 Normal | -0.084 |  |
| 2026-04-06 11:05:54 | Glencourse (Kelani Ganga) | 8.36 | 🟢 Normal | -0.089 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)