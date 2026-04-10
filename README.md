# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--11_02:15:10-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **121,764 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **31** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-11 02:15:10 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2026-04-11 02:14:47 | Rathnapura (Kalu Ganga) | 0.60 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-04-11 02:11:40 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.15 | 🟢 Normal | -0.007 |  |
| 2026-04-11 02:08:51 | Hanwella (Kelani Ganga) | 0.29 | 🟢 Normal | -0.009 |  |
| 2026-04-11 02:08:49 | Moraketiya (Walawe Ganga) | 1.10 | 🟢 Normal | -0.018 |  |
| 2026-04-11 02:08:00 | Putupaula (Kalu Ganga) | 0.36 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-04-11 02:07:44 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-11 02:07:05 | Deraniyagala (Kelani Ganga) | 0.10 | 🟢 Normal | -0.021 |  |
| 2026-04-11 02:06:54 | Holombuwa (Kelani Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-04-11 02:06:31 | Thanamalwila (Kirindi Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-04-11 02:05:39 | Thaldena (Mahaweli Ganga) | 0.23 | 🟢 Normal | -18.000 |  |
| 2026-04-11 02:05:37 | Thaldena (Mahaweli Ganga) | 0.24 | 🟢 Normal | -18.000 |  |
| 2026-04-11 02:05:31 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-04-11 02:05:00 | Urawa (Nilwala Ganga) | 0.06 | 🟢 Normal | -0.024 |  |
| 2026-04-11 02:03:26 | Kithulgala (Kelani Ganga) | 1.52 | 🟢 Normal | 0.000 |  |
| 2026-04-11 02:03:21 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | -0.050 |  |
| 2026-04-11 02:02:51 | Norwood (Kelani Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-04-11 02:02:51 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-04-11 02:02:41 | Padiyathalawa (Maduru Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-04-11 02:02:09 | Badalgama (Maha Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-04-11 02:02:08 | Horowpothana (Yan Oya) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-04-11 02:02:05 | Nawalapitiya (Mahaweli Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-11 02:01:50 | Ellagawa (Kalu Ganga) | 3.90 | 🟢 Normal | 0.000 |  |
| 2026-04-11 02:01:36 | Wellawaya (Kirindi Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-04-11 02:01:29 | Nawalapitiya (Mahaweli Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-11 02:01:27 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-04-11 02:01:14 | Glencourse (Kelani Ganga) | 8.55 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-04-11 02:01:11 | Giriulla (Maha Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-04-11 02:00:24 | Manampitiya (Mahaweli Ganga) | 0.21 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-04-11 02:00:09 | Peradeniya (Mahaweli Ganga) | 1.65 | 🟢 Normal | -0.131 |  |
| 2026-04-11 01:43:02 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-10 18:06:03 | Weraganthota (Mahaweli Ganga) | -2.20 | 🟢 Normal | 0.886 | 🔺 Rising |
| 2026-04-11 02:15:10 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2026-04-11 01:21:11 | Pitabeddara (Nilwala Ganga) | 0.93 | 🟢 Normal | 0.077 | 🔺 Rising |
| 2026-04-11 02:14:47 | Rathnapura (Kalu Ganga) | 0.60 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-04-11 02:01:14 | Glencourse (Kelani Ganga) | 8.55 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-04-11 01:15:25 | Panadugama (Nilwala Ganga) | 2.20 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-04-11 02:00:24 | Manampitiya (Mahaweli Ganga) | 0.21 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-04-11 02:08:00 | Putupaula (Kalu Ganga) | 0.36 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-04-11 02:03:26 | Kithulgala (Kelani Ganga) | 1.52 | 🟢 Normal | 0.000 |  |
| 2026-04-11 02:01:36 | Wellawaya (Kirindi Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-04-11 02:07:44 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-11 02:01:27 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-04-11 02:02:05 | Nawalapitiya (Mahaweli Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-11 00:01:42 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-04-11 02:01:11 | Giriulla (Maha Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-04-11 02:02:08 | Horowpothana (Yan Oya) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-04-10 18:02:42 | Galgamuwa (Mee Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-04-11 02:02:51 | Norwood (Kelani Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-04-11 02:01:50 | Ellagawa (Kalu Ganga) | 3.90 | 🟢 Normal | 0.000 |  |
| 2026-04-11 00:03:29 | Baddegama (Gin Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-04-11 02:02:41 | Padiyathalawa (Maduru Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-04-11 02:02:51 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-04-11 01:05:38 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-11 01:28:03 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-04-11 02:02:09 | Badalgama (Maha Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-04-11 02:06:54 | Holombuwa (Kelani Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-04-11 02:05:31 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-04-11 02:06:31 | Thanamalwila (Kirindi Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-04-11 02:11:40 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.15 | 🟢 Normal | -0.007 |  |
| 2026-04-11 02:08:51 | Hanwella (Kelani Ganga) | 0.29 | 🟢 Normal | -0.009 |  |
| 2026-04-11 00:09:22 | Magura (Kalu Ganga) | 0.73 | 🟢 Normal | -0.010 |  |
| 2026-04-11 01:04:24 | Thawalama (Gin Ganga) | 1.50 | 🟢 Normal | -0.010 |  |
| 2026-04-10 18:01:05 | Thanthirimale (Malwathu Oya) | 1.12 | 🟢 Normal | -0.010 |  |
| 2026-04-11 02:08:49 | Moraketiya (Walawe Ganga) | 1.10 | 🟢 Normal | -0.018 |  |
| 2026-04-11 02:07:05 | Deraniyagala (Kelani Ganga) | 0.10 | 🟢 Normal | -0.021 |  |
| 2026-04-11 02:05:00 | Urawa (Nilwala Ganga) | 0.06 | 🟢 Normal | -0.024 |  |
| 2026-04-11 02:03:21 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | -0.050 |  |
| 2026-04-11 02:00:09 | Peradeniya (Mahaweli Ganga) | 1.65 | 🟢 Normal | -0.131 |  |
| 2026-04-11 02:05:39 | Thaldena (Mahaweli Ganga) | 0.23 | 🟢 Normal | -18.000 |  |

## River Water Level Charts by Station

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

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

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)