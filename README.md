# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--08_09:15:10-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **227,714 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-08 09:15:10 | Panadugama (Nilwala Ganga) | 2.82 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-08-08 09:09:32 | Galgamuwa (Mee Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-08-08 09:09:15 | Badalgama (Maha Oya) | 2.15 | 🟢 Normal | -0.010 |  |
| 2026-08-08 09:09:08 | Thawalama (Gin Ganga) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-08-08 09:07:23 | Holombuwa (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-08-08 09:07:14 | Rathnapura (Kalu Ganga) | 1.58 | 🟢 Normal | -0.038 |  |
| 2026-08-08 09:06:45 | Thalgahagoda (Nilwala Ganga) | 0.36 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-08-08 09:06:06 | Magura (Kalu Ganga) | 1.44 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-08-08 09:05:34 | Baddegama (Gin Ganga) | 1.78 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-08-08 09:04:51 | Peradeniya (Mahaweli Ganga) | 3.74 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-08-08 09:04:49 | Glencourse (Kelani Ganga) | 10.80 | 🟢 Normal | -0.030 |  |
| 2026-08-08 09:04:46 | Pitabeddara (Nilwala Ganga) | 0.67 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-08-08 09:04:46 | Kithulgala (Kelani Ganga) | 2.35 | 🟢 Normal | -0.065 |  |
| 2026-08-08 09:04:23 | Urawa (Nilwala Ganga) | 0.14 | 🟢 Normal | -0.012 |  |
| 2026-08-08 09:03:59 | Thanamalwila (Kirindi Oya) | 0.59 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-08 09:03:50 | Norwood (Kelani Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-08-08 09:03:44 | Putupaula (Kalu Ganga) | 0.65 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-08-08 09:03:22 | Nakkala (Kumbukkan Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-08-08 09:03:13 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-08-08 09:03:05 | Hanwella (Kelani Ganga) | 2.37 | 🟢 Normal | -0.010 |  |
| 2026-08-08 09:03:03 | Giriulla (Maha Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-08-08 09:02:33 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.68 | 🟢 Normal | 0.000 |  |
| 2026-08-08 09:02:13 | Deraniyagala (Kelani Ganga) | 1.01 | 🟢 Normal | -0.011 |  |
| 2026-08-08 09:02:11 | Katharagama (Menik Ganga) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-08-08 09:02:11 | Siyambalanduwa (Heda Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-08-08 09:02:00 | Thaldena (Mahaweli Ganga) | 0.11 | 🟢 Normal | -0.010 |  |
| 2026-08-08 09:01:58 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-08 09:01:47 | Wellawaya (Kirindi Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-08-08 09:01:36 | Horowpothana (Yan Oya) | 1.71 | 🟢 Normal | 0.000 |  |
| 2026-08-08 09:01:29 | Nawalapitiya (Mahaweli Ganga) | 2.02 | 🟢 Normal | -0.022 |  |
| 2026-08-08 09:01:29 | Kuda Oya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-08-08 09:01:28 | Moragaswewa (Deduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-08 09:01:25 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-08-08 09:01:20 | Ellagawa (Kalu Ganga) | 5.28 | 🟢 Normal | -0.040 |  |
| 2026-08-08 09:01:15 | Moraketiya (Walawe Ganga) | 0.76 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-08 09:01:12 | Weraganthota (Mahaweli Ganga) | -3.46 | 🟢 Normal | -0.010 |  |
| 2026-08-08 09:01:03 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-08-08 09:00:47 | Thanthirimale (Malwathu Oya) | 0.68 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-08 09:15:10 | Panadugama (Nilwala Ganga) | 2.82 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-08-08 09:05:34 | Baddegama (Gin Ganga) | 1.78 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-08-08 09:03:13 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-08-08 09:06:45 | Thalgahagoda (Nilwala Ganga) | 0.36 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-08-08 09:06:06 | Magura (Kalu Ganga) | 1.44 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-08-08 09:03:44 | Putupaula (Kalu Ganga) | 0.65 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-08-08 09:04:51 | Peradeniya (Mahaweli Ganga) | 3.74 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-08-08 09:04:46 | Pitabeddara (Nilwala Ganga) | 0.67 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-08-08 09:01:15 | Moraketiya (Walawe Ganga) | 0.76 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-08 09:03:59 | Thanamalwila (Kirindi Oya) | 0.59 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-08 09:01:47 | Wellawaya (Kirindi Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-08-08 09:03:22 | Nakkala (Kumbukkan Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-08-08 09:01:28 | Moragaswewa (Deduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-08 09:01:25 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-08-08 09:03:03 | Giriulla (Maha Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-08-08 09:01:36 | Horowpothana (Yan Oya) | 1.71 | 🟢 Normal | 0.000 |  |
| 2026-08-08 09:09:32 | Galgamuwa (Mee Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-08-08 09:03:50 | Norwood (Kelani Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-08-08 09:01:58 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-08 09:02:11 | Siyambalanduwa (Heda Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-08-08 09:02:11 | Katharagama (Menik Ganga) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-08-08 09:07:23 | Holombuwa (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-08-08 09:01:03 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-08-08 09:09:08 | Thawalama (Gin Ganga) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-08-08 09:01:29 | Kuda Oya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-08-08 09:02:33 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.68 | 🟢 Normal | 0.000 |  |
| 2026-08-08 09:09:15 | Badalgama (Maha Oya) | 2.15 | 🟢 Normal | -0.010 |  |
| 2026-08-08 08:04:24 | Dunamale (Aththanagalu Oya) | 0.55 | 🟢 Normal | -0.010 |  |
| 2026-08-08 09:01:12 | Weraganthota (Mahaweli Ganga) | -3.46 | 🟢 Normal | -0.010 |  |
| 2026-08-08 09:02:00 | Thaldena (Mahaweli Ganga) | 0.11 | 🟢 Normal | -0.010 |  |
| 2026-08-08 09:03:05 | Hanwella (Kelani Ganga) | 2.37 | 🟢 Normal | -0.010 |  |
| 2026-08-08 09:00:47 | Thanthirimale (Malwathu Oya) | 0.68 | 🟢 Normal | -0.010 |  |
| 2026-08-08 09:02:13 | Deraniyagala (Kelani Ganga) | 1.01 | 🟢 Normal | -0.011 |  |
| 2026-08-08 09:04:23 | Urawa (Nilwala Ganga) | 0.14 | 🟢 Normal | -0.012 |  |
| 2026-08-08 09:01:29 | Nawalapitiya (Mahaweli Ganga) | 2.02 | 🟢 Normal | -0.022 |  |
| 2026-08-08 09:04:49 | Glencourse (Kelani Ganga) | 10.80 | 🟢 Normal | -0.030 |  |
| 2026-08-08 09:07:14 | Rathnapura (Kalu Ganga) | 1.58 | 🟢 Normal | -0.038 |  |
| 2026-08-08 09:01:20 | Ellagawa (Kalu Ganga) | 5.28 | 🟢 Normal | -0.040 |  |
| 2026-08-08 09:04:46 | Kithulgala (Kelani Ganga) | 2.35 | 🟢 Normal | -0.065 |  |

## River Water Level Charts by Station

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

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

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)