# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--02_13:29:39-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **62,474 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-02 13:29:39 | Thalgahagoda (Nilwala Ganga) | 0.14 | 🟢 Normal | -4.000 |  |
| 2026-02-02 13:27:51 | Thalgahagoda (Nilwala Ganga) | 0.26 | 🟢 Normal | -4.000 |  |
| 2026-02-02 13:23:03 | Thanthirimale (Malwathu Oya) | 2.53 | 🟢 Normal | -0.030 |  |
| 2026-02-02 13:16:23 | Thanamalwila (Kirindi Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-02-02 13:09:54 | Magura (Kalu Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-02-02 13:08:42 | Badalgama (Maha Oya) | 1.90 | 🟢 Normal | 0.000 |  |
| 2026-02-02 13:07:46 | Thawalama (Gin Ganga) | 1.04 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-02 13:07:11 | Katharagama (Menik Ganga) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-02-02 13:05:48 | Baddegama (Gin Ganga) | 1.08 | 🟢 Normal | -0.042 |  |
| 2026-02-02 13:05:27 | Panadugama (Nilwala Ganga) | 2.22 | 🟢 Normal | -0.011 |  |
| 2026-02-02 13:05:22 | Ellagawa (Kalu Ganga) | 4.40 | 🟢 Normal | -0.019 |  |
| 2026-02-02 13:04:54 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-02-02 13:04:34 | Peradeniya (Mahaweli Ganga) | 1.45 | 🟢 Normal | -0.145 |  |
| 2026-02-02 13:04:05 | Hanwella (Kelani Ganga) | 0.44 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-02 13:03:55 | Deraniyagala (Kelani Ganga) | 0.09 | 🟢 Normal | -0.010 |  |
| 2026-02-02 13:03:50 | Putupaula (Kalu Ganga) | 0.50 | 🟢 Normal | 0.101 | 🔺 Rising |
| 2026-02-02 13:03:49 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-02-02 13:03:29 | Pitabeddara (Nilwala Ganga) | 0.42 | 🟢 Normal | -0.032 |  |
| 2026-02-02 13:03:29 | Giriulla (Maha Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-02-02 13:03:27 | Holombuwa (Kelani Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-02-02 13:03:26 | Padiyathalawa (Maduru Oya) | 0.66 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-02-02 13:03:24 | Galgamuwa (Mee Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-02-02 13:03:03 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-02-02 13:02:58 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-02-02 13:02:44 | Thaldena (Mahaweli Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-02-02 13:02:34 | Dunamale (Aththanagalu Oya) | 0.75 | 🟢 Normal | -0.011 |  |
| 2026-02-02 13:02:30 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.72 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-02 13:02:19 | Horowpothana (Yan Oya) | 1.80 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-02 13:02:13 | Moragaswewa (Deduru Oya) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-02-02 13:02:10 | Siyambalanduwa (Heda Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-02-02 13:02:08 | Yaka Wewa (Ma Oya) | 1.08 | 🟢 Normal | -0.020 |  |
| 2026-02-02 13:02:02 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.123 | 🔺 Rising |
| 2026-02-02 13:01:54 | Kithulgala (Kelani Ganga) | 1.46 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-02 13:01:51 | Wellawaya (Kirindi Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-02-02 13:01:35 | Nawalapitiya (Mahaweli Ganga) | 0.69 | 🟢 Normal | -0.010 |  |
| 2026-02-02 13:01:20 | Weraganthota (Mahaweli Ganga) | -2.24 | 🟢 Normal | -0.124 |  |
| 2026-02-02 13:01:15 | Glencourse (Kelani Ganga) | 8.50 | 🟢 Normal | -0.010 |  |
| 2026-02-02 13:00:39 | Manampitiya (Mahaweli Ganga) | 1.51 | 🟢 Normal | -0.021 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-02 13:02:02 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.123 | 🔺 Rising |
| 2026-02-02 13:03:50 | Putupaula (Kalu Ganga) | 0.50 | 🟢 Normal | 0.101 | 🔺 Rising |
| 2026-02-02 13:02:30 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.72 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-02 13:03:26 | Padiyathalawa (Maduru Oya) | 0.66 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-02-02 13:02:19 | Horowpothana (Yan Oya) | 1.80 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-02 13:01:54 | Kithulgala (Kelani Ganga) | 1.46 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-02 13:04:05 | Hanwella (Kelani Ganga) | 0.44 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-02 13:07:46 | Thawalama (Gin Ganga) | 1.04 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-02 13:01:51 | Wellawaya (Kirindi Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-02-02 13:00:06 | Nakkala (Kumbukkan Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-02-02 13:02:13 | Moragaswewa (Deduru Oya) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-02-02 13:03:29 | Giriulla (Maha Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-02-02 13:03:24 | Galgamuwa (Mee Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-02-02 13:09:54 | Magura (Kalu Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-02-02 13:03:49 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-02-02 13:04:54 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-02-02 13:02:10 | Siyambalanduwa (Heda Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-02-02 13:02:44 | Thaldena (Mahaweli Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-02-02 13:07:11 | Katharagama (Menik Ganga) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-02-02 13:08:42 | Badalgama (Maha Oya) | 1.90 | 🟢 Normal | 0.000 |  |
| 2026-02-02 13:03:27 | Holombuwa (Kelani Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-02-02 12:02:29 | Urawa (Nilwala Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-02-02 13:02:58 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-02-02 13:16:23 | Thanamalwila (Kirindi Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-02-02 13:01:15 | Glencourse (Kelani Ganga) | 8.50 | 🟢 Normal | -0.010 |  |
| 2026-02-02 13:01:35 | Nawalapitiya (Mahaweli Ganga) | 0.69 | 🟢 Normal | -0.010 |  |
| 2026-02-02 13:03:55 | Deraniyagala (Kelani Ganga) | 0.09 | 🟢 Normal | -0.010 |  |
| 2026-02-02 13:05:27 | Panadugama (Nilwala Ganga) | 2.22 | 🟢 Normal | -0.011 |  |
| 2026-02-02 13:02:34 | Dunamale (Aththanagalu Oya) | 0.75 | 🟢 Normal | -0.011 |  |
| 2026-02-02 13:05:22 | Ellagawa (Kalu Ganga) | 4.40 | 🟢 Normal | -0.019 |  |
| 2026-02-02 13:02:08 | Yaka Wewa (Ma Oya) | 1.08 | 🟢 Normal | -0.020 |  |
| 2026-02-02 13:00:39 | Manampitiya (Mahaweli Ganga) | 1.51 | 🟢 Normal | -0.021 |  |
| 2026-02-02 13:23:03 | Thanthirimale (Malwathu Oya) | 2.53 | 🟢 Normal | -0.030 |  |
| 2026-02-02 13:03:29 | Pitabeddara (Nilwala Ganga) | 0.42 | 🟢 Normal | -0.032 |  |
| 2026-02-02 13:05:48 | Baddegama (Gin Ganga) | 1.08 | 🟢 Normal | -0.042 |  |
| 2026-02-02 12:09:30 | Rathnapura (Kalu Ganga) | 0.89 | 🟢 Normal | -0.045 |  |
| 2026-02-02 13:01:20 | Weraganthota (Mahaweli Ganga) | -2.24 | 🟢 Normal | -0.124 |  |
| 2026-02-02 13:04:34 | Peradeniya (Mahaweli Ganga) | 1.45 | 🟢 Normal | -0.145 |  |
| 2026-02-02 13:29:39 | Thalgahagoda (Nilwala Ganga) | 0.14 | 🟢 Normal | -4.000 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

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

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)