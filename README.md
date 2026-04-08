# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--09_05:13:53-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **120,099 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-09 05:13:53 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.51 | 🟢 Normal | 0.124 | 🔺 Rising |
| 2026-04-09 05:09:54 | Pitabeddara (Nilwala Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-04-09 05:09:52 | Pitabeddara (Nilwala Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-04-09 05:09:51 | Pitabeddara (Nilwala Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-04-09 05:09:50 | Pitabeddara (Nilwala Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-04-09 05:09:48 | Pitabeddara (Nilwala Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-04-09 05:07:32 | Hanwella (Kelani Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-04-09 05:06:05 | Thanamalwila (Kirindi Oya) | 0.33 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-04-09 05:05:47 | Nawalapitiya (Mahaweli Ganga) | 0.62 | 🟢 Normal | -0.028 |  |
| 2026-04-09 05:05:19 | Rathnapura (Kalu Ganga) | 0.84 | 🟢 Normal | -0.031 |  |
| 2026-04-09 05:04:40 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-04-09 05:04:35 | Dunamale (Aththanagalu Oya) | 0.46 | 🟢 Normal | -0.010 |  |
| 2026-04-09 05:04:34 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-04-09 05:04:34 | Deraniyagala (Kelani Ganga) | 0.26 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-04-09 05:04:32 | Norwood (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-04-09 05:03:33 | Badalgama (Maha Oya) | 1.89 | 🟢 Normal | 0.000 |  |
| 2026-04-09 05:03:25 | Giriulla (Maha Oya) | 0.86 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-04-09 05:03:10 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-04-09 05:02:50 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-09 05:02:43 | Padiyathalawa (Maduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-09 05:02:42 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-04-09 05:02:42 | Manampitiya (Mahaweli Ganga) | 0.43 | 🟢 Normal | -0.030 |  |
| 2026-04-09 05:02:38 | Glencourse (Kelani Ganga) | 8.89 | 🟢 Normal | 0.096 | 🔺 Rising |
| 2026-04-09 05:02:29 | Thaldena (Mahaweli Ganga) | 0.23 | 🟢 Normal | -0.010 |  |
| 2026-04-09 05:02:10 | Yaka Wewa (Ma Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-04-09 05:01:50 | Wellawaya (Kirindi Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-04-09 05:01:46 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-04-09 05:01:42 | Kithulgala (Kelani Ganga) | 1.10 | 🟢 Normal | -0.078 |  |
| 2026-04-09 05:01:38 | Peradeniya (Mahaweli Ganga) | 1.29 | 🟢 Normal | -0.061 |  |
| 2026-04-09 05:01:36 | Magura (Kalu Ganga) | 1.25 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2026-04-09 05:01:28 | Holombuwa (Kelani Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-04-09 05:01:09 | Kuda Oya (Kirindi Oya) | 1.15 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-09 05:01:01 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-04-09 05:00:55 | Thawalama (Gin Ganga) | 1.54 | 🟢 Normal | -0.035 |  |
| 2026-04-09 05:00:11 | Thalgahagoda (Nilwala Ganga) | 0.19 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-04-09 04:48:21 | Wellawaya (Kirindi Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-04-09 04:46:31 | Panadugama (Nilwala Ganga) | 1.76 | 🟢 Normal | 0.000 |  |
| 2026-04-09 04:45:25 | Thanamalwila (Kirindi Oya) | 0.32 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-04-09 04:34:03 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | 0.122 | 🔺 Rising |
| 2026-04-09 04:27:26 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-08 18:05:20 | Weraganthota (Mahaweli Ganga) | 3.20 | 🟢 Normal | 5.983 | 🔺 Rising |
| 2026-04-09 05:13:53 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.51 | 🟢 Normal | 0.124 | 🔺 Rising |
| 2026-04-09 04:34:03 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | 0.122 | 🔺 Rising |
| 2026-04-09 05:01:36 | Magura (Kalu Ganga) | 1.25 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2026-04-09 05:02:38 | Glencourse (Kelani Ganga) | 8.89 | 🟢 Normal | 0.096 | 🔺 Rising |
| 2026-04-09 05:03:25 | Giriulla (Maha Oya) | 0.86 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-04-09 05:06:05 | Thanamalwila (Kirindi Oya) | 0.33 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-04-09 05:00:11 | Thalgahagoda (Nilwala Ganga) | 0.19 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-04-09 05:04:34 | Deraniyagala (Kelani Ganga) | 0.26 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-04-09 01:04:03 | Urawa (Nilwala Ganga) | -0.05 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-09 05:01:09 | Kuda Oya (Kirindi Oya) | 1.15 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-09 05:01:50 | Wellawaya (Kirindi Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-04-09 05:02:50 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-09 05:01:01 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-04-09 05:02:10 | Yaka Wewa (Ma Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-04-09 05:02:42 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-04-08 18:02:48 | Galgamuwa (Mee Oya) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-04-09 05:09:54 | Pitabeddara (Nilwala Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-04-09 05:04:32 | Norwood (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-04-09 05:07:32 | Hanwella (Kelani Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-04-09 04:15:15 | Baddegama (Gin Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-04-09 04:46:31 | Panadugama (Nilwala Ganga) | 1.76 | 🟢 Normal | 0.000 |  |
| 2026-04-09 05:02:43 | Padiyathalawa (Maduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-09 05:04:40 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-04-09 05:04:34 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-04-09 05:01:46 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-04-09 05:03:10 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-04-09 05:03:33 | Badalgama (Maha Oya) | 1.89 | 🟢 Normal | 0.000 |  |
| 2026-04-09 05:01:28 | Holombuwa (Kelani Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-04-09 04:02:44 | Ellagawa (Kalu Ganga) | 3.87 | 🟢 Normal | -0.005 |  |
| 2026-04-08 18:02:20 | Thanthirimale (Malwathu Oya) | 1.40 | 🟢 Normal | -0.010 |  |
| 2026-04-09 05:02:29 | Thaldena (Mahaweli Ganga) | 0.23 | 🟢 Normal | -0.010 |  |
| 2026-04-09 05:04:35 | Dunamale (Aththanagalu Oya) | 0.46 | 🟢 Normal | -0.010 |  |
| 2026-04-09 05:05:47 | Nawalapitiya (Mahaweli Ganga) | 0.62 | 🟢 Normal | -0.028 |  |
| 2026-04-09 05:02:42 | Manampitiya (Mahaweli Ganga) | 0.43 | 🟢 Normal | -0.030 |  |
| 2026-04-09 05:05:19 | Rathnapura (Kalu Ganga) | 0.84 | 🟢 Normal | -0.031 |  |
| 2026-04-09 05:00:55 | Thawalama (Gin Ganga) | 1.54 | 🟢 Normal | -0.035 |  |
| 2026-04-09 05:01:38 | Peradeniya (Mahaweli Ganga) | 1.29 | 🟢 Normal | -0.061 |  |
| 2026-04-09 05:01:42 | Kithulgala (Kelani Ganga) | 1.10 | 🟢 Normal | -0.078 |  |

## River Water Level Charts by Station

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)