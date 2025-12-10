# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--10_08:24:14-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **13,972 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-10 08:24:14 | Magura (Kalu Ganga) | 1.98 | 🟢 Normal | -0.120 |  |
| 2025-12-10 08:14:45 | Manampitiya (Mahaweli Ganga) | 2.60 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2025-12-10 08:09:42 | Baddegama (Gin Ganga) | 1.86 | 🟢 Normal | -0.009 |  |
| 2025-12-10 08:09:10 | Holombuwa (Kelani Ganga) | 0.79 | 🟢 Normal | -0.010 |  |
| 2025-12-10 08:08:38 | Thawalama (Gin Ganga) | 1.69 | 🟢 Normal | -0.046 |  |
| 2025-12-10 08:08:14 | Yaka Wewa (Ma Oya) | 1.68 | 🟢 Normal | 0.228 | 🔺 Rising |
| 2025-12-10 08:07:15 | Padiyathalawa (Maduru Oya) | 1.30 | 🟢 Normal | -0.047 |  |
| 2025-12-10 08:06:58 | Nakkala (Kumbukkan Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2025-12-10 08:06:23 | Thalgahagoda (Nilwala Ganga) | 1.00 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2025-12-10 08:06:14 | Glencourse (Kelani Ganga) | 9.85 | 🟢 Normal | -0.039 |  |
| 2025-12-10 08:06:13 | Katharagama (Menik Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2025-12-10 08:05:46 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | -0.121 |  |
| 2025-12-10 08:05:31 | Thanthirimale (Malwathu Oya) | 3.40 | 🟢 Normal | 0.086 | 🔺 Rising |
| 2025-12-10 08:05:22 | Norwood (Kelani Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2025-12-10 08:05:16 | Peradeniya (Mahaweli Ganga) | 2.70 | 🟢 Normal | -0.037 |  |
| 2025-12-10 08:04:25 | Urawa (Nilwala Ganga) | 0.68 | 🟢 Normal | 0.065 | 🔺 Rising |
| 2025-12-10 08:04:23 | Putupaula (Kalu Ganga) | 0.91 | 🟢 Normal | -0.057 |  |
| 2025-12-10 08:04:22 | Hanwella (Kelani Ganga) | 2.10 | 🟢 Normal | -0.030 |  |
| 2025-12-10 08:04:16 | Galgamuwa (Mee Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2025-12-10 08:04:14 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.54 | 🟢 Normal | -0.059 |  |
| 2025-12-10 08:03:35 | Weraganthota (Mahaweli Ganga) | -1.33 | 🟢 Normal | -0.163 |  |
| 2025-12-10 08:03:35 | Wellawaya (Kirindi Oya) | 1.08 | 🟢 Normal | -0.010 |  |
| 2025-12-10 08:03:24 | Panadugama (Nilwala Ganga) | 4.27 | 🟢 Normal | -0.107 |  |
| 2025-12-10 08:03:20 | Thaldena (Mahaweli Ganga) | 0.75 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-10 08:03:14 | Rathnapura (Kalu Ganga) | 1.62 | 🟢 Normal | -0.011 |  |
| 2025-12-10 08:03:11 | Deraniyagala (Kelani Ganga) | 0.63 | 🟢 Normal | -0.040 |  |
| 2025-12-10 08:03:02 | Thanamalwila (Kirindi Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2025-12-10 08:03:00 | Kuda Oya (Kirindi Oya) | 1.52 | 🟢 Normal | 0.000 |  |
| 2025-12-10 08:02:54 | Nawalapitiya (Mahaweli Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2025-12-10 08:02:43 | Ellagawa (Kalu Ganga) | 5.19 | 🟢 Normal | -0.010 |  |
| 2025-12-10 08:02:11 | Dunamale (Aththanagalu Oya) | 1.30 | 🟢 Normal | -0.021 |  |
| 2025-12-10 08:02:10 | Kithulgala (Kelani Ganga) | 1.82 | 🟢 Normal | -0.010 |  |
| 2025-12-10 08:02:06 | Badalgama (Maha Oya) | 2.60 | 🟢 Normal | 0.000 |  |
| 2025-12-10 08:01:49 | Siyambalanduwa (Heda Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-10 08:01:36 | Pitabeddara (Nilwala Ganga) | 1.71 | 🟢 Normal | -0.246 |  |
| 2025-12-10 08:01:19 | Moraketiya (Walawe Ganga) | 1.01 | 🟢 Normal | -0.010 |  |
| 2025-12-10 08:01:15 | Horowpothana (Yan Oya) | 4.59 | 🟢 Normal | 0.109 | 🔺 Rising |
| 2025-12-10 08:01:13 | Giriulla (Maha Oya) | 1.36 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-11-28 06:04:09⌛ | Moragaswewa (Deduru Oya) | 8.33 | 🔴 Major Flood | 0.051 | 🔺 Rising |
| 2025-12-10 08:08:14 | Yaka Wewa (Ma Oya) | 1.68 | 🟢 Normal | 0.228 | 🔺 Rising |
| 2025-12-10 08:01:15 | Horowpothana (Yan Oya) | 4.59 | 🟢 Normal | 0.109 | 🔺 Rising |
| 2025-12-10 08:05:31 | Thanthirimale (Malwathu Oya) | 3.40 | 🟢 Normal | 0.086 | 🔺 Rising |
| 2025-12-10 08:14:45 | Manampitiya (Mahaweli Ganga) | 2.60 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2025-12-10 08:04:25 | Urawa (Nilwala Ganga) | 0.68 | 🟢 Normal | 0.065 | 🔺 Rising |
| 2025-12-10 08:06:23 | Thalgahagoda (Nilwala Ganga) | 1.00 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2025-12-10 08:03:20 | Thaldena (Mahaweli Ganga) | 0.75 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-10 08:06:58 | Nakkala (Kumbukkan Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2025-12-10 08:02:54 | Nawalapitiya (Mahaweli Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2025-12-10 08:01:13 | Giriulla (Maha Oya) | 1.36 | 🟢 Normal | 0.000 |  |
| 2025-12-10 08:04:16 | Galgamuwa (Mee Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2025-12-10 08:05:22 | Norwood (Kelani Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2025-12-10 08:01:49 | Siyambalanduwa (Heda Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-10 08:06:13 | Katharagama (Menik Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2025-12-10 08:02:06 | Badalgama (Maha Oya) | 2.60 | 🟢 Normal | 0.000 |  |
| 2025-12-10 08:03:00 | Kuda Oya (Kirindi Oya) | 1.52 | 🟢 Normal | 0.000 |  |
| 2025-12-10 08:03:02 | Thanamalwila (Kirindi Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2025-12-10 08:09:42 | Baddegama (Gin Ganga) | 1.86 | 🟢 Normal | -0.009 |  |
| 2025-12-10 08:09:10 | Holombuwa (Kelani Ganga) | 0.79 | 🟢 Normal | -0.010 |  |
| 2025-12-10 08:03:35 | Wellawaya (Kirindi Oya) | 1.08 | 🟢 Normal | -0.010 |  |
| 2025-12-10 08:02:10 | Kithulgala (Kelani Ganga) | 1.82 | 🟢 Normal | -0.010 |  |
| 2025-12-10 08:02:43 | Ellagawa (Kalu Ganga) | 5.19 | 🟢 Normal | -0.010 |  |
| 2025-12-10 08:01:19 | Moraketiya (Walawe Ganga) | 1.01 | 🟢 Normal | -0.010 |  |
| 2025-12-10 08:03:14 | Rathnapura (Kalu Ganga) | 1.62 | 🟢 Normal | -0.011 |  |
| 2025-12-10 08:02:11 | Dunamale (Aththanagalu Oya) | 1.30 | 🟢 Normal | -0.021 |  |
| 2025-12-10 08:04:22 | Hanwella (Kelani Ganga) | 2.10 | 🟢 Normal | -0.030 |  |
| 2025-12-10 08:05:16 | Peradeniya (Mahaweli Ganga) | 2.70 | 🟢 Normal | -0.037 |  |
| 2025-12-10 08:06:14 | Glencourse (Kelani Ganga) | 9.85 | 🟢 Normal | -0.039 |  |
| 2025-12-10 08:03:11 | Deraniyagala (Kelani Ganga) | 0.63 | 🟢 Normal | -0.040 |  |
| 2025-12-10 08:08:38 | Thawalama (Gin Ganga) | 1.69 | 🟢 Normal | -0.046 |  |
| 2025-12-10 08:07:15 | Padiyathalawa (Maduru Oya) | 1.30 | 🟢 Normal | -0.047 |  |
| 2025-12-10 08:04:23 | Putupaula (Kalu Ganga) | 0.91 | 🟢 Normal | -0.057 |  |
| 2025-12-10 08:04:14 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.54 | 🟢 Normal | -0.059 |  |
| 2025-12-10 08:03:24 | Panadugama (Nilwala Ganga) | 4.27 | 🟢 Normal | -0.107 |  |
| 2025-12-10 08:24:14 | Magura (Kalu Ganga) | 1.98 | 🟢 Normal | -0.120 |  |
| 2025-12-10 08:05:46 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | -0.121 |  |
| 2025-12-10 08:03:35 | Weraganthota (Mahaweli Ganga) | -1.33 | 🟢 Normal | -0.163 |  |
| 2025-12-10 08:01:36 | Pitabeddara (Nilwala Ganga) | 1.71 | 🟢 Normal | -0.246 |  |

## River Water Level Charts by Station

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)