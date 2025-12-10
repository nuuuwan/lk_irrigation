# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--10_09:13:09-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **14,011 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-10 09:13:09 | Horowpothana (Yan Oya) | 4.76 | 🟢 Normal | 0.142 | 🔺 Rising |
| 2025-12-10 09:12:56 | Nakkala (Kumbukkan Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2025-12-10 09:12:54 | Galgamuwa (Mee Oya) | 0.76 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2025-12-10 09:12:17 | Magura (Kalu Ganga) | 1.95 | 🟢 Normal | -0.037 |  |
| 2025-12-10 09:08:05 | Ellagawa (Kalu Ganga) | 5.18 | 🟢 Normal | -0.009 |  |
| 2025-12-10 09:07:40 | Padiyathalawa (Maduru Oya) | 1.20 | 🟢 Normal | -0.099 |  |
| 2025-12-10 09:07:05 | Holombuwa (Kelani Ganga) | 0.78 | 🟢 Normal | -0.010 |  |
| 2025-12-10 09:06:52 | Baddegama (Gin Ganga) | 1.83 | 🟢 Normal | -0.031 |  |
| 2025-12-10 09:06:51 | Norwood (Kelani Ganga) | 0.85 | 🟢 Normal | -0.010 |  |
| 2025-12-10 09:06:26 | Weraganthota (Mahaweli Ganga) | -1.39 | 🟢 Normal | -0.057 |  |
| 2025-12-10 09:05:32 | Thaldena (Mahaweli Ganga) | 0.74 | 🟢 Normal | -0.010 |  |
| 2025-12-10 09:05:29 | Urawa (Nilwala Ganga) | 0.72 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2025-12-10 09:05:23 | Panadugama (Nilwala Ganga) | 4.18 | 🟢 Normal | -0.087 |  |
| 2025-12-10 09:05:09 | Rathnapura (Kalu Ganga) | 1.61 | 🟢 Normal | -0.010 |  |
| 2025-12-10 09:04:30 | Thanthirimale (Malwathu Oya) | 3.45 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2025-12-10 09:04:23 | Katharagama (Menik Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2025-12-10 09:04:03 | Glencourse (Kelani Ganga) | 9.84 | 🟢 Normal | -0.010 |  |
| 2025-12-10 09:03:57 | Kithulgala (Kelani Ganga) | 1.58 | 🟢 Normal | -0.233 |  |
| 2025-12-10 09:03:48 | Dunamale (Aththanagalu Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2025-12-10 09:03:37 | Deraniyagala (Kelani Ganga) | 0.61 | 🟢 Normal | -0.020 |  |
| 2025-12-10 09:03:33 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.48 | 🟢 Normal | -0.061 |  |
| 2025-12-10 09:03:22 | Hanwella (Kelani Ganga) | 2.08 | 🟢 Normal | -0.020 |  |
| 2025-12-10 09:03:18 | Thawalama (Gin Ganga) | 1.68 | 🟢 Normal | -0.011 |  |
| 2025-12-10 09:03:12 | Kuda Oya (Kirindi Oya) | 1.51 | 🟢 Normal | -0.010 |  |
| 2025-12-10 09:02:49 | Thalgahagoda (Nilwala Ganga) | 1.01 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-10 09:02:42 | Putupaula (Kalu Ganga) | 0.81 | 🟢 Normal | -0.103 |  |
| 2025-12-10 09:02:38 | Pitabeddara (Nilwala Ganga) | 1.50 | 🟢 Normal | -0.206 |  |
| 2025-12-10 09:02:36 | Giriulla (Maha Oya) | 1.36 | 🟢 Normal | 0.000 |  |
| 2025-12-10 09:02:36 | Siyambalanduwa (Heda Oya) | 0.96 | 🟢 Normal | -0.010 |  |
| 2025-12-10 09:02:00 | Wellawaya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2025-12-10 09:01:51 | Badalgama (Maha Oya) | 2.60 | 🟢 Normal | 0.000 |  |
| 2025-12-10 09:01:48 | Moraketiya (Walawe Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2025-12-10 09:01:44 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.131 |  |
| 2025-12-10 09:01:36 | Thanamalwila (Kirindi Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2025-12-10 09:00:52 | Manampitiya (Mahaweli Ganga) | 2.65 | 🟢 Normal | 0.065 | 🔺 Rising |
| 2025-12-10 09:00:24 | Peradeniya (Mahaweli Ganga) | 2.63 | 🟢 Normal | -0.076 |  |
| 2025-12-10 09:00:15 | Yaka Wewa (Ma Oya) | 1.88 | 🟢 Normal | 0.231 | 🔺 Rising |
| 2025-12-10 09:00:11 | Nawalapitiya (Mahaweli Ganga) | 1.16 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-11-28 06:04:09⌛ | Moragaswewa (Deduru Oya) | 8.33 | 🔴 Major Flood | 0.051 | 🔺 Rising |
| 2025-12-10 09:00:15 | Yaka Wewa (Ma Oya) | 1.88 | 🟢 Normal | 0.231 | 🔺 Rising |
| 2025-12-10 09:13:09 | Horowpothana (Yan Oya) | 4.76 | 🟢 Normal | 0.142 | 🔺 Rising |
| 2025-12-10 09:00:52 | Manampitiya (Mahaweli Ganga) | 2.65 | 🟢 Normal | 0.065 | 🔺 Rising |
| 2025-12-10 09:04:30 | Thanthirimale (Malwathu Oya) | 3.45 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2025-12-10 09:05:29 | Urawa (Nilwala Ganga) | 0.72 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2025-12-10 09:02:49 | Thalgahagoda (Nilwala Ganga) | 1.01 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-10 09:12:54 | Galgamuwa (Mee Oya) | 0.76 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2025-12-10 09:02:00 | Wellawaya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2025-12-10 09:12:56 | Nakkala (Kumbukkan Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2025-12-10 09:00:11 | Nawalapitiya (Mahaweli Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2025-12-10 09:02:36 | Giriulla (Maha Oya) | 1.36 | 🟢 Normal | 0.000 |  |
| 2025-12-10 09:01:48 | Moraketiya (Walawe Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2025-12-10 09:03:48 | Dunamale (Aththanagalu Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2025-12-10 09:04:23 | Katharagama (Menik Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2025-12-10 09:01:51 | Badalgama (Maha Oya) | 2.60 | 🟢 Normal | 0.000 |  |
| 2025-12-10 09:01:36 | Thanamalwila (Kirindi Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2025-12-10 09:08:05 | Ellagawa (Kalu Ganga) | 5.18 | 🟢 Normal | -0.009 |  |
| 2025-12-10 09:05:32 | Thaldena (Mahaweli Ganga) | 0.74 | 🟢 Normal | -0.010 |  |
| 2025-12-10 09:05:09 | Rathnapura (Kalu Ganga) | 1.61 | 🟢 Normal | -0.010 |  |
| 2025-12-10 09:06:51 | Norwood (Kelani Ganga) | 0.85 | 🟢 Normal | -0.010 |  |
| 2025-12-10 09:02:36 | Siyambalanduwa (Heda Oya) | 0.96 | 🟢 Normal | -0.010 |  |
| 2025-12-10 09:03:12 | Kuda Oya (Kirindi Oya) | 1.51 | 🟢 Normal | -0.010 |  |
| 2025-12-10 09:07:05 | Holombuwa (Kelani Ganga) | 0.78 | 🟢 Normal | -0.010 |  |
| 2025-12-10 09:04:03 | Glencourse (Kelani Ganga) | 9.84 | 🟢 Normal | -0.010 |  |
| 2025-12-10 09:03:18 | Thawalama (Gin Ganga) | 1.68 | 🟢 Normal | -0.011 |  |
| 2025-12-10 09:03:37 | Deraniyagala (Kelani Ganga) | 0.61 | 🟢 Normal | -0.020 |  |
| 2025-12-10 09:03:22 | Hanwella (Kelani Ganga) | 2.08 | 🟢 Normal | -0.020 |  |
| 2025-12-10 09:06:52 | Baddegama (Gin Ganga) | 1.83 | 🟢 Normal | -0.031 |  |
| 2025-12-10 09:12:17 | Magura (Kalu Ganga) | 1.95 | 🟢 Normal | -0.037 |  |
| 2025-12-10 09:06:26 | Weraganthota (Mahaweli Ganga) | -1.39 | 🟢 Normal | -0.057 |  |
| 2025-12-10 09:03:33 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.48 | 🟢 Normal | -0.061 |  |
| 2025-12-10 09:00:24 | Peradeniya (Mahaweli Ganga) | 2.63 | 🟢 Normal | -0.076 |  |
| 2025-12-10 09:05:23 | Panadugama (Nilwala Ganga) | 4.18 | 🟢 Normal | -0.087 |  |
| 2025-12-10 09:07:40 | Padiyathalawa (Maduru Oya) | 1.20 | 🟢 Normal | -0.099 |  |
| 2025-12-10 09:02:42 | Putupaula (Kalu Ganga) | 0.81 | 🟢 Normal | -0.103 |  |
| 2025-12-10 09:01:44 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.131 |  |
| 2025-12-10 09:02:38 | Pitabeddara (Nilwala Ganga) | 1.50 | 🟢 Normal | -0.206 |  |
| 2025-12-10 09:03:57 | Kithulgala (Kelani Ganga) | 1.58 | 🟢 Normal | -0.233 |  |

## River Water Level Charts by Station

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)