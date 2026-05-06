# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--07_01:21:16-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **144,860 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **29** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-07 01:21:16 | Wellawaya (Kirindi Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-05-07 01:12:29 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-05-07 01:10:47 | Thanamalwila (Kirindi Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-05-07 01:10:46 | Kithulgala (Kelani Ganga) | 1.59 | 🟢 Normal | -0.121 |  |
| 2026-05-07 01:09:37 | Thaldena (Mahaweli Ganga) | 0.32 | 🟢 Normal | -0.018 |  |
| 2026-05-07 01:07:03 | Thawalama (Gin Ganga) | 1.80 | 🟢 Normal | 0.151 | 🔺 Rising |
| 2026-05-07 01:05:44 | Giriulla (Maha Oya) | 0.90 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-07 01:05:29 | Dunamale (Aththanagalu Oya) | 0.66 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-05-07 01:04:41 | Panadugama (Nilwala Ganga) | 1.97 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-05-07 01:04:09 | Rathnapura (Kalu Ganga) | 0.96 | 🟢 Normal | 0.676 | 🔺 Rising |
| 2026-05-07 01:03:46 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-05-07 01:03:33 | Norwood (Kelani Ganga) | 0.71 | 🟢 Normal | -0.010 |  |
| 2026-05-07 01:03:21 | Deraniyagala (Kelani Ganga) | 0.88 | 🟢 Normal | 0.292 | 🔺 Rising |
| 2026-05-07 01:02:47 | Thalgahagoda (Nilwala Ganga) | 0.23 | 🟢 Normal | -0.214 |  |
| 2026-05-07 01:02:34 | Glencourse (Kelani Ganga) | 9.20 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-05-07 01:02:23 | Hanwella (Kelani Ganga) | 0.46 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-05-07 01:02:06 | Badalgama (Maha Oya) | 1.89 | 🟢 Normal | 0.000 |  |
| 2026-05-07 01:02:00 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-05-07 01:01:57 | Padiyathalawa (Maduru Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-05-07 01:01:52 | Holombuwa (Kelani Ganga) | 1.87 | 🟢 Normal | -0.175 |  |
| 2026-05-07 01:01:34 | Moragaswewa (Deduru Oya) | 0.36 | 🟢 Normal | 0.005 | 🔺 Rising |
| 2026-05-07 01:01:31 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-07 01:01:29 | Ellagawa (Kalu Ganga) | 4.13 | 🟢 Normal | -0.010 |  |
| 2026-05-07 01:01:23 | Manampitiya (Mahaweli Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-05-07 01:01:19 | Horowpothana (Yan Oya) | 2.42 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-05-07 01:01:14 | Kuda Oya (Kirindi Oya) | 1.39 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-07 01:00:30 | Nawalapitiya (Mahaweli Ganga) | 0.83 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-07 00:57:11 | Thalgahagoda (Nilwala Ganga) | 0.25 | 🟢 Normal | -0.214 |  |
| 2026-05-07 00:54:23 | Rathnapura (Kalu Ganga) | 0.85 | 🟢 Normal | 0.676 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-07 00:08:04 | Magura (Kalu Ganga) | 1.11 | 🟢 Normal | 2.769 | 🔺 Rising |
| 2026-05-07 01:04:09 | Rathnapura (Kalu Ganga) | 0.96 | 🟢 Normal | 0.676 | 🔺 Rising |
| 2026-05-07 01:03:21 | Deraniyagala (Kelani Ganga) | 0.88 | 🟢 Normal | 0.292 | 🔺 Rising |
| 2026-05-06 22:14:28 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.88 | 🟢 Normal | 0.242 | 🔺 Rising |
| 2026-05-07 01:07:03 | Thawalama (Gin Ganga) | 1.80 | 🟢 Normal | 0.151 | 🔺 Rising |
| 2026-05-07 00:03:58 | Peradeniya (Mahaweli Ganga) | 1.96 | 🟢 Normal | 0.144 | 🔺 Rising |
| 2026-05-07 01:05:29 | Dunamale (Aththanagalu Oya) | 0.66 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-05-07 01:03:46 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-05-07 01:01:19 | Horowpothana (Yan Oya) | 2.42 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-05-07 01:02:34 | Glencourse (Kelani Ganga) | 9.20 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-05-07 00:07:08 | Baddegama (Gin Ganga) | 1.04 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-05-07 01:00:30 | Nawalapitiya (Mahaweli Ganga) | 0.83 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-07 01:04:41 | Panadugama (Nilwala Ganga) | 1.97 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-05-07 01:05:44 | Giriulla (Maha Oya) | 0.90 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-07 01:02:23 | Hanwella (Kelani Ganga) | 0.46 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-05-07 01:01:31 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-07 01:01:14 | Kuda Oya (Kirindi Oya) | 1.39 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-06 22:05:10 | Pitabeddara (Nilwala Ganga) | 0.22 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-06 18:05:19 | Galgamuwa (Mee Oya) | 0.10 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-07 01:01:34 | Moragaswewa (Deduru Oya) | 0.36 | 🟢 Normal | 0.005 | 🔺 Rising |
| 2026-05-07 01:21:16 | Wellawaya (Kirindi Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-05-07 00:01:13 | Nakkala (Kumbukkan Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-05-07 01:12:29 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-05-07 01:01:57 | Padiyathalawa (Maduru Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-05-07 01:02:00 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-05-07 00:03:04 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-05-07 01:02:06 | Badalgama (Maha Oya) | 1.89 | 🟢 Normal | 0.000 |  |
| 2026-05-07 01:01:23 | Manampitiya (Mahaweli Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-05-06 23:06:16 | Urawa (Nilwala Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-05-07 01:10:47 | Thanamalwila (Kirindi Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-05-06 18:02:21 | Weraganthota (Mahaweli Ganga) | -3.22 | 🟢 Normal | -0.010 |  |
| 2026-05-06 18:01:28 | Thanthirimale (Malwathu Oya) | 1.50 | 🟢 Normal | -0.010 |  |
| 2026-05-07 01:03:33 | Norwood (Kelani Ganga) | 0.71 | 🟢 Normal | -0.010 |  |
| 2026-05-07 01:01:29 | Ellagawa (Kalu Ganga) | 4.13 | 🟢 Normal | -0.010 |  |
| 2026-05-07 01:09:37 | Thaldena (Mahaweli Ganga) | 0.32 | 🟢 Normal | -0.018 |  |
| 2026-05-06 23:02:43 | Putupaula (Kalu Ganga) | 0.32 | 🟢 Normal | -0.103 |  |
| 2026-05-07 01:10:46 | Kithulgala (Kelani Ganga) | 1.59 | 🟢 Normal | -0.121 |  |
| 2026-05-07 01:01:52 | Holombuwa (Kelani Ganga) | 1.87 | 🟢 Normal | -0.175 |  |
| 2026-05-07 01:02:47 | Thalgahagoda (Nilwala Ganga) | 0.23 | 🟢 Normal | -0.214 |  |

## River Water Level Charts by Station

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)