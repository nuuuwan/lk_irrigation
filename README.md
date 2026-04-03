# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--03_06:13:17-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **114,769 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-03 06:13:17 | Thanamalwila (Kirindi Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-03 06:12:04 | Moragaswewa (Deduru Oya) | -0.19 | 🟢 Normal | 0.000 |  |
| 2026-04-03 06:11:24 | Urawa (Nilwala Ganga) | 0.28 | 🟢 Normal | -0.048 |  |
| 2026-04-03 06:09:11 | Panadugama (Nilwala Ganga) | 1.85 | 🟢 Normal | 0.000 |  |
| 2026-04-03 06:08:57 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | -0.009 |  |
| 2026-04-03 06:08:21 | Dunamale (Aththanagalu Oya) | 0.40 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-04-03 06:08:05 | Rathnapura (Kalu Ganga) | 1.15 | 🟢 Normal | 0.111 | 🔺 Rising |
| 2026-04-03 06:07:36 | Pitabeddara (Nilwala Ganga) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-04-03 06:06:36 | Holombuwa (Kelani Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-04-03 06:05:11 | Badalgama (Maha Oya) | 1.66 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-03 06:04:31 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | -0.010 |  |
| 2026-04-03 06:04:23 | Horowpothana (Yan Oya) | 1.19 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-04-03 06:04:23 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-03 06:04:14 | Padiyathalawa (Maduru Oya) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-04-03 06:04:00 | Peradeniya (Mahaweli Ganga) | 1.23 | 🟢 Normal | -0.068 |  |
| 2026-04-03 06:03:30 | Giriulla (Maha Oya) | 0.79 | 🟢 Normal | 0.126 | 🔺 Rising |
| 2026-04-03 06:03:27 | Moraketiya (Walawe Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-04-03 06:02:59 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-03 06:02:58 | Moragaswewa (Deduru Oya) | -0.19 | 🟢 Normal | 0.000 |  |
| 2026-04-03 06:02:49 | Hanwella (Kelani Ganga) | 0.36 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-04-03 06:02:44 | Thawalama (Gin Ganga) | 1.25 | 🟢 Normal | -0.010 |  |
| 2026-04-03 06:02:41 | Siyambalanduwa (Heda Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-04-03 06:02:38 | Baddegama (Gin Ganga) | 1.19 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-03 06:02:15 | Deraniyagala (Kelani Ganga) | 0.06 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-04-03 06:02:08 | Wellawaya (Kirindi Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-04-03 06:01:50 | Thaldena (Mahaweli Ganga) | 0.27 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-03 06:01:48 | Glencourse (Kelani Ganga) | 8.84 | 🟢 Normal | -0.031 |  |
| 2026-04-03 06:01:36 | Ellagawa (Kalu Ganga) | 3.75 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-03 06:01:31 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | -0.163 |  |
| 2026-04-03 06:01:27 | Kuda Oya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-04-03 06:01:20 | Manampitiya (Mahaweli Ganga) | 0.66 | 🟢 Normal | -0.044 |  |
| 2026-04-03 06:01:20 | Kithulgala (Kelani Ganga) | 1.52 | 🟢 Normal | 0.000 |  |
| 2026-04-03 06:01:16 | Magura (Kalu Ganga) | 0.89 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-04-03 06:01:00 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-03 06:00:46 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.167 |  |
| 2026-04-03 06:00:20 | Weraganthota (Mahaweli Ganga) | -2.05 | 🟢 Normal | 0.083 | 🔺 Rising |
| 2026-04-03 06:00:13 | Nawalapitiya (Mahaweli Ganga) | 0.53 | 🟢 Normal | -0.020 |  |
| 2026-04-03 05:59:25 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.36 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-03 06:03:30 | Giriulla (Maha Oya) | 0.79 | 🟢 Normal | 0.126 | 🔺 Rising |
| 2026-04-03 06:08:05 | Rathnapura (Kalu Ganga) | 1.15 | 🟢 Normal | 0.111 | 🔺 Rising |
| 2026-04-03 06:00:20 | Weraganthota (Mahaweli Ganga) | -2.05 | 🟢 Normal | 0.083 | 🔺 Rising |
| 2026-04-03 06:04:23 | Horowpothana (Yan Oya) | 1.19 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-04-03 06:02:49 | Hanwella (Kelani Ganga) | 0.36 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-04-03 06:01:00 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-03 06:02:59 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-03 06:02:15 | Deraniyagala (Kelani Ganga) | 0.06 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-04-03 06:01:16 | Magura (Kalu Ganga) | 0.89 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-04-03 06:05:11 | Badalgama (Maha Oya) | 1.66 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-03 06:01:50 | Thaldena (Mahaweli Ganga) | 0.27 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-03 06:02:38 | Baddegama (Gin Ganga) | 1.19 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-03 06:01:36 | Ellagawa (Kalu Ganga) | 3.75 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-02 18:02:18 | Thanthirimale (Malwathu Oya) | 1.14 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-03 06:08:21 | Dunamale (Aththanagalu Oya) | 0.40 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-04-03 06:01:20 | Kithulgala (Kelani Ganga) | 1.52 | 🟢 Normal | 0.000 |  |
| 2026-04-03 06:02:08 | Wellawaya (Kirindi Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-04-03 06:04:23 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-03 06:12:04 | Moragaswewa (Deduru Oya) | -0.19 | 🟢 Normal | 0.000 |  |
| 2026-04-02 18:08:10 | Galgamuwa (Mee Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-04-03 06:07:36 | Pitabeddara (Nilwala Ganga) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-04-03 06:09:11 | Panadugama (Nilwala Ganga) | 1.85 | 🟢 Normal | 0.000 |  |
| 2026-04-03 06:04:14 | Padiyathalawa (Maduru Oya) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-04-03 06:03:27 | Moraketiya (Walawe Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-04-03 06:02:41 | Siyambalanduwa (Heda Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-04-03 06:06:36 | Holombuwa (Kelani Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-04-03 06:01:27 | Kuda Oya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-04-03 06:13:17 | Thanamalwila (Kirindi Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-03 05:59:25 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-04-03 06:08:57 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | -0.009 |  |
| 2026-04-03 06:02:44 | Thawalama (Gin Ganga) | 1.25 | 🟢 Normal | -0.010 |  |
| 2026-04-03 06:04:31 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | -0.010 |  |
| 2026-04-03 06:00:13 | Nawalapitiya (Mahaweli Ganga) | 0.53 | 🟢 Normal | -0.020 |  |
| 2026-04-03 06:01:48 | Glencourse (Kelani Ganga) | 8.84 | 🟢 Normal | -0.031 |  |
| 2026-04-03 06:01:20 | Manampitiya (Mahaweli Ganga) | 0.66 | 🟢 Normal | -0.044 |  |
| 2026-04-03 06:11:24 | Urawa (Nilwala Ganga) | 0.28 | 🟢 Normal | -0.048 |  |
| 2026-04-03 06:04:00 | Peradeniya (Mahaweli Ganga) | 1.23 | 🟢 Normal | -0.068 |  |
| 2026-04-03 06:01:31 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | -0.163 |  |
| 2026-04-03 06:00:46 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.167 |  |

## River Water Level Charts by Station

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)