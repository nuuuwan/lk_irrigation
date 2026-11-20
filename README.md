# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--20_17:21:18-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **321,118 measurements** from **39** stations.
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
| 2026-11-20 17:21:18 | Thalgahagoda (Nilwala Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-11-20 17:14:57 | Urawa (Nilwala Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-11-20 17:13:21 | Panadugama (Nilwala Ganga) | 3.30 | 🟢 Normal | 0.000 |  |
| 2026-11-20 17:09:59 | Baddegama (Gin Ganga) | 1.12 | 🟢 Normal | -0.018 |  |
| 2026-11-20 17:09:23 | Peradeniya (Mahaweli Ganga) | 2.50 | 🟢 Normal | 0.000 |  |
| 2026-11-20 17:08:38 | Glencourse (Kelani Ganga) | 9.36 | 🟢 Normal | -0.071 |  |
| 2026-11-20 17:07:32 | Thanthirimale (Malwathu Oya) | 1.26 | 🟢 Normal | -0.009 |  |
| 2026-11-20 17:07:03 | Thawalama (Gin Ganga) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-11-20 17:06:58 | Moraketiya (Walawe Ganga) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-11-20 17:06:51 | Holombuwa (Kelani Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-11-20 17:06:29 | Kithulgala (Kelani Ganga) | 1.81 | 🟢 Normal | 0.104 | 🔺 Rising |
| 2026-11-20 17:06:29 | Putupaula (Kalu Ganga) | 0.51 | 🟢 Normal | -0.048 |  |
| 2026-11-20 17:06:23 | Rathnapura (Kalu Ganga) | 1.34 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-11-20 17:05:26 | Wellawaya (Kirindi Oya) | 1.12 | 🟢 Normal | -0.018 |  |
| 2026-11-20 17:04:39 | Badalgama (Maha Oya) | 2.36 | 🟢 Normal | -0.010 |  |
| 2026-11-20 17:04:19 | Dunamale (Aththanagalu Oya) | 1.28 | 🟢 Normal | -0.022 |  |
| 2026-11-20 17:04:02 | Hanwella (Kelani Ganga) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-11-20 17:03:54 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.19 | 🟢 Normal | -0.039 |  |
| 2026-11-20 17:03:50 | Ellagawa (Kalu Ganga) | 4.70 | 🟢 Normal | -0.010 |  |
| 2026-11-20 17:03:31 | Katharagama (Menik Ganga) | 0.03 | 🟢 Normal | -0.013 |  |
| 2026-11-20 17:03:24 | Deraniyagala (Kelani Ganga) | 0.56 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-11-20 17:03:06 | Hanwella (Kelani Ganga) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-11-20 17:03:03 | Nawalapitiya (Mahaweli Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-11-20 17:02:59 | Pitabeddara (Nilwala Ganga) | 1.02 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-11-20 17:02:55 | Manampitiya (Mahaweli Ganga) | 1.07 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-20 17:02:51 | Horowpothana (Yan Oya) | 1.88 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-11-20 17:02:19 | Thanamalwila (Kirindi Oya) | 1.11 | 🟢 Normal | -0.019 |  |
| 2026-11-20 17:01:53 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-20 17:01:36 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-11-20 17:01:24 | Norwood (Kelani Ganga) | 0.85 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-20 17:01:21 | Nakkala (Kumbukkan Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-11-20 17:01:20 | Thaldena (Mahaweli Ganga) | 0.45 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-20 17:01:12 | Giriulla (Maha Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-11-20 17:01:11 | Siyambalanduwa (Heda Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-11-20 17:00:55 | Magura (Kalu Ganga) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-11-20 17:00:55 | Moragaswewa (Deduru Oya) | 0.37 | 🟢 Normal | -0.010 |  |
| 2026-11-20 17:00:51 | Kuda Oya (Kirindi Oya) | 1.47 | 🟢 Normal | -0.030 |  |
| 2026-11-20 17:00:28 | Weraganthota (Mahaweli Ganga) | -2.15 | 🟢 Normal | -0.020 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-20 17:06:29 | Kithulgala (Kelani Ganga) | 1.81 | 🟢 Normal | 0.104 | 🔺 Rising |
| 2026-11-20 17:06:23 | Rathnapura (Kalu Ganga) | 1.34 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-11-20 17:01:20 | Thaldena (Mahaweli Ganga) | 0.45 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-20 17:03:24 | Deraniyagala (Kelani Ganga) | 0.56 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-11-20 17:02:51 | Horowpothana (Yan Oya) | 1.88 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-11-20 17:02:59 | Pitabeddara (Nilwala Ganga) | 1.02 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-11-20 17:02:55 | Manampitiya (Mahaweli Ganga) | 1.07 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-20 17:01:24 | Norwood (Kelani Ganga) | 0.85 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-20 17:01:21 | Nakkala (Kumbukkan Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-11-20 17:03:03 | Nawalapitiya (Mahaweli Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-11-20 17:01:53 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-20 17:01:12 | Giriulla (Maha Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-11-20 16:10:18 | Galgamuwa (Mee Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-11-20 17:00:55 | Magura (Kalu Ganga) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-11-20 17:04:02 | Hanwella (Kelani Ganga) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-11-20 17:13:21 | Panadugama (Nilwala Ganga) | 3.30 | 🟢 Normal | 0.000 |  |
| 2026-11-19 14:01:52⌛ | Padiyathalawa (Maduru Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-11-20 17:01:36 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-11-20 17:06:58 | Moraketiya (Walawe Ganga) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-11-20 17:01:11 | Siyambalanduwa (Heda Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-11-20 17:06:51 | Holombuwa (Kelani Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-11-20 17:07:03 | Thawalama (Gin Ganga) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-11-20 17:09:23 | Peradeniya (Mahaweli Ganga) | 2.50 | 🟢 Normal | 0.000 |  |
| 2026-11-20 17:14:57 | Urawa (Nilwala Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-11-20 17:21:18 | Thalgahagoda (Nilwala Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-11-20 17:07:32 | Thanthirimale (Malwathu Oya) | 1.26 | 🟢 Normal | -0.009 |  |
| 2026-11-20 17:03:50 | Ellagawa (Kalu Ganga) | 4.70 | 🟢 Normal | -0.010 |  |
| 2026-11-20 17:04:39 | Badalgama (Maha Oya) | 2.36 | 🟢 Normal | -0.010 |  |
| 2026-11-20 17:00:55 | Moragaswewa (Deduru Oya) | 0.37 | 🟢 Normal | -0.010 |  |
| 2026-11-20 17:03:31 | Katharagama (Menik Ganga) | 0.03 | 🟢 Normal | -0.013 |  |
| 2026-11-20 17:05:26 | Wellawaya (Kirindi Oya) | 1.12 | 🟢 Normal | -0.018 |  |
| 2026-11-20 17:09:59 | Baddegama (Gin Ganga) | 1.12 | 🟢 Normal | -0.018 |  |
| 2026-11-20 17:02:19 | Thanamalwila (Kirindi Oya) | 1.11 | 🟢 Normal | -0.019 |  |
| 2026-11-20 17:00:28 | Weraganthota (Mahaweli Ganga) | -2.15 | 🟢 Normal | -0.020 |  |
| 2026-11-20 17:04:19 | Dunamale (Aththanagalu Oya) | 1.28 | 🟢 Normal | -0.022 |  |
| 2026-11-20 17:00:51 | Kuda Oya (Kirindi Oya) | 1.47 | 🟢 Normal | -0.030 |  |
| 2026-11-20 17:03:54 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.19 | 🟢 Normal | -0.039 |  |
| 2026-11-20 17:06:29 | Putupaula (Kalu Ganga) | 0.51 | 🟢 Normal | -0.048 |  |
| 2026-11-20 17:08:38 | Glencourse (Kelani Ganga) | 9.36 | 🟢 Normal | -0.071 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

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

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)