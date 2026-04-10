# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--11_04:25:40-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **121,835 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-11 04:25:40 | Urawa (Nilwala Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-04-11 04:19:20 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-04-11 04:13:46 | Putupaula (Kalu Ganga) | 0.55 | 🟢 Normal | 0.114 | 🔺 Rising |
| 2026-04-11 04:12:01 | Holombuwa (Kelani Ganga) | 0.17 | 🟢 Normal | -0.005 |  |
| 2026-04-11 04:11:36 | Magura (Kalu Ganga) | 0.69 | 🟢 Normal | -0.018 |  |
| 2026-04-11 04:09:32 | Deraniyagala (Kelani Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-04-11 04:08:27 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-04-11 04:08:21 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-11 04:08:07 | Rathnapura (Kalu Ganga) | 0.68 | 🟢 Normal | 0.074 | 🔺 Rising |
| 2026-04-11 04:07:51 | Baddegama (Gin Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-04-11 04:06:54 | Horowpothana (Yan Oya) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-04-11 04:06:31 | Panadugama (Nilwala Ganga) | 2.23 | 🟢 Normal | -0.171 |  |
| 2026-04-11 04:05:44 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.50 | 🟢 Normal | 0.181 | 🔺 Rising |
| 2026-04-11 04:05:34 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | -0.009 |  |
| 2026-04-11 04:05:28 | Glencourse (Kelani Ganga) | 8.70 | 🟢 Normal | 0.088 | 🔺 Rising |
| 2026-04-11 04:04:08 | Hanwella (Kelani Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-04-11 04:03:39 | Nawalapitiya (Mahaweli Ganga) | 0.53 | 🟢 Normal | -0.013 |  |
| 2026-04-11 04:03:39 | Padiyathalawa (Maduru Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-04-11 04:03:38 | Thaldena (Mahaweli Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-04-11 04:03:28 | Badalgama (Maha Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-04-11 04:03:15 | Norwood (Kelani Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-04-11 04:03:07 | Pitabeddara (Nilwala Ganga) | 1.07 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-04-11 04:02:37 | Kithulgala (Kelani Ganga) | 1.15 | 🟢 Normal | -0.210 |  |
| 2026-04-11 04:02:34 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-04-11 04:02:23 | Manampitiya (Mahaweli Ganga) | 0.25 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-11 04:02:15 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-04-11 04:02:02 | Thawalama (Gin Ganga) | 1.48 | 🟢 Normal | 0.000 |  |
| 2026-04-11 04:01:38 | Giriulla (Maha Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-04-11 04:01:01 | Moraketiya (Walawe Ganga) | 1.06 | 🟢 Normal | -0.011 |  |
| 2026-04-11 04:00:58 | Wellawaya (Kirindi Oya) | 0.68 | 🟢 Normal | -0.011 |  |
| 2026-04-11 04:00:54 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-11 04:00:09 | Peradeniya (Mahaweli Ganga) | 1.29 | 🟢 Normal | -0.152 |  |
| 2026-04-11 03:59:30 | Panadugama (Nilwala Ganga) | 2.25 | 🟢 Normal | -0.171 |  |
| 2026-04-11 03:38:18 | Magura (Kalu Ganga) | 0.70 | 🟢 Normal | -0.018 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-10 18:06:03 | Weraganthota (Mahaweli Ganga) | -2.20 | 🟢 Normal | 0.886 | 🔺 Rising |
| 2026-04-11 04:05:44 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.50 | 🟢 Normal | 0.181 | 🔺 Rising |
| 2026-04-11 04:13:46 | Putupaula (Kalu Ganga) | 0.55 | 🟢 Normal | 0.114 | 🔺 Rising |
| 2026-04-11 04:05:28 | Glencourse (Kelani Ganga) | 8.70 | 🟢 Normal | 0.088 | 🔺 Rising |
| 2026-04-11 04:08:07 | Rathnapura (Kalu Ganga) | 0.68 | 🟢 Normal | 0.074 | 🔺 Rising |
| 2026-04-11 04:03:07 | Pitabeddara (Nilwala Ganga) | 1.07 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-04-11 04:02:23 | Manampitiya (Mahaweli Ganga) | 0.25 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-11 04:00:54 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-11 04:02:15 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-04-11 04:01:38 | Giriulla (Maha Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-04-11 04:06:54 | Horowpothana (Yan Oya) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-04-10 18:02:42 | Galgamuwa (Mee Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-04-11 04:03:15 | Norwood (Kelani Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-04-11 04:04:08 | Hanwella (Kelani Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-04-11 04:09:32 | Deraniyagala (Kelani Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-04-11 04:07:51 | Baddegama (Gin Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-04-11 04:03:39 | Padiyathalawa (Maduru Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-04-11 04:08:27 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-04-11 04:02:34 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-04-11 04:08:21 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-11 04:03:38 | Thaldena (Mahaweli Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-04-11 03:12:01 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-04-11 04:03:28 | Badalgama (Maha Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-04-11 04:02:02 | Thawalama (Gin Ganga) | 1.48 | 🟢 Normal | 0.000 |  |
| 2026-04-11 04:25:40 | Urawa (Nilwala Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-04-11 04:19:20 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-04-11 04:12:01 | Holombuwa (Kelani Ganga) | 0.17 | 🟢 Normal | -0.005 |  |
| 2026-04-11 04:05:34 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | -0.009 |  |
| 2026-04-11 03:09:57 | Thanamalwila (Kirindi Oya) | 0.38 | 🟢 Normal | -0.009 |  |
| 2026-04-11 03:04:11 | Ellagawa (Kalu Ganga) | 3.89 | 🟢 Normal | -0.010 |  |
| 2026-04-10 18:01:05 | Thanthirimale (Malwathu Oya) | 1.12 | 🟢 Normal | -0.010 |  |
| 2026-04-11 04:01:01 | Moraketiya (Walawe Ganga) | 1.06 | 🟢 Normal | -0.011 |  |
| 2026-04-11 04:00:58 | Wellawaya (Kirindi Oya) | 0.68 | 🟢 Normal | -0.011 |  |
| 2026-04-11 04:03:39 | Nawalapitiya (Mahaweli Ganga) | 0.53 | 🟢 Normal | -0.013 |  |
| 2026-04-11 04:11:36 | Magura (Kalu Ganga) | 0.69 | 🟢 Normal | -0.018 |  |
| 2026-04-11 03:01:04 | Thalgahagoda (Nilwala Ganga) | 0.26 | 🟢 Normal | -0.042 |  |
| 2026-04-11 04:00:09 | Peradeniya (Mahaweli Ganga) | 1.29 | 🟢 Normal | -0.152 |  |
| 2026-04-11 04:06:31 | Panadugama (Nilwala Ganga) | 2.23 | 🟢 Normal | -0.171 |  |
| 2026-04-11 04:02:37 | Kithulgala (Kelani Ganga) | 1.15 | 🟢 Normal | -0.210 |  |

## River Water Level Charts by Station

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

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

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

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

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)