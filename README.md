# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--16_01:28:16-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **316,968 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Thalgahagoda — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **28** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-16 01:28:16 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-11-16 01:10:27 | Moraketiya (Walawe Ganga) | 1.78 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-16 01:09:21 | Thawalama (Gin Ganga) | 2.02 | 🟢 Normal | -0.009 |  |
| 2026-11-16 01:07:20 | Norwood (Kelani Ganga) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-11-16 01:06:08 | Wellawaya (Kirindi Oya) | 1.36 | 🟢 Normal | -0.010 |  |
| 2026-11-16 01:05:48 | Padiyathalawa (Maduru Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-11-16 01:05:48 | Glencourse (Kelani Ganga) | 10.48 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-11-16 01:05:27 | Baddegama (Gin Ganga) | 1.36 | 🟢 Normal | -1.014 |  |
| 2026-11-16 01:04:10 | Holombuwa (Kelani Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-11-16 01:03:54 | Kuda Oya (Kirindi Oya) | 1.66 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-16 01:03:53 | Giriulla (Maha Oya) | 1.44 | 🟢 Normal | -0.010 |  |
| 2026-11-16 01:03:42 | Hanwella (Kelani Ganga) | 2.28 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-16 01:03:22 | Badalgama (Maha Oya) | 2.75 | 🟢 Normal | -0.010 |  |
| 2026-11-16 01:03:22 | Thanamalwila (Kirindi Oya) | 1.49 | 🟢 Normal | -0.010 |  |
| 2026-11-16 01:03:20 | Katharagama (Menik Ganga) | -0.03 | 🟢 Normal | -0.011 |  |
| 2026-11-16 01:03:09 | Nakkala (Kumbukkan Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-11-16 01:03:08 | Kithulgala (Kelani Ganga) | 2.09 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-11-16 01:02:33 | Deraniyagala (Kelani Ganga) | 0.72 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-11-16 01:02:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.18 | 🟢 Normal | -0.024 |  |
| 2026-11-16 01:02:14 | Manampitiya (Mahaweli Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-11-16 01:01:55 | Siyambalanduwa (Heda Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-11-16 01:01:46 | Peradeniya (Mahaweli Ganga) | 2.95 | 🟢 Normal | 0.000 |  |
| 2026-11-16 01:01:29 | Moragaswewa (Deduru Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-11-16 01:01:29 | Dunamale (Aththanagalu Oya) | 1.82 | 🟢 Normal | -0.021 |  |
| 2026-11-16 01:01:22 | Thaldena (Mahaweli Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-11-16 01:01:08 | Ellagawa (Kalu Ganga) | 5.44 | 🟢 Normal | -0.010 |  |
| 2026-11-16 01:00:34 | Nawalapitiya (Mahaweli Ganga) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-11-16 01:00:08 | Thalgahagoda (Nilwala Ganga) | 1.65 | 🟡 Alert | -0.011 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-16 01:00:08 | Thalgahagoda (Nilwala Ganga) | 1.65 | 🟡 Alert | -0.011 |  |
| 2026-11-16 01:28:16 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-11-16 01:03:08 | Kithulgala (Kelani Ganga) | 2.09 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-11-16 01:05:48 | Glencourse (Kelani Ganga) | 10.48 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-11-16 01:02:33 | Deraniyagala (Kelani Ganga) | 0.72 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-11-16 01:03:42 | Hanwella (Kelani Ganga) | 2.28 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-16 01:10:27 | Moraketiya (Walawe Ganga) | 1.78 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-16 01:03:54 | Kuda Oya (Kirindi Oya) | 1.66 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-16 01:03:09 | Nakkala (Kumbukkan Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-11-16 01:01:29 | Moragaswewa (Deduru Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-11-16 01:00:34 | Nawalapitiya (Mahaweli Ganga) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-11-16 00:03:10 | Yaka Wewa (Ma Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-11-15 22:01:59 | Horowpothana (Yan Oya) | 2.07 | 🟢 Normal | 0.000 |  |
| 2026-11-16 00:03:32 | Magura (Kalu Ganga) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-11-16 00:11:45 | Pitabeddara (Nilwala Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-11-16 01:07:20 | Norwood (Kelani Ganga) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-11-16 00:11:34 | Panadugama (Nilwala Ganga) | 4.64 | 🟢 Normal | 0.000 |  |
| 2026-11-16 01:05:48 | Padiyathalawa (Maduru Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-11-16 01:01:55 | Siyambalanduwa (Heda Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-11-16 01:01:22 | Thaldena (Mahaweli Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-11-16 01:04:10 | Holombuwa (Kelani Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-11-16 01:02:14 | Manampitiya (Mahaweli Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-11-15 18:00:37 | Thanthirimale (Malwathu Oya) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-11-16 01:01:46 | Peradeniya (Mahaweli Ganga) | 2.95 | 🟢 Normal | 0.000 |  |
| 2026-11-16 00:11:33 | Urawa (Nilwala Ganga) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-11-16 01:09:21 | Thawalama (Gin Ganga) | 2.02 | 🟢 Normal | -0.009 |  |
| 2026-11-16 01:06:08 | Wellawaya (Kirindi Oya) | 1.36 | 🟢 Normal | -0.010 |  |
| 2026-11-16 01:03:22 | Badalgama (Maha Oya) | 2.75 | 🟢 Normal | -0.010 |  |
| 2026-11-16 01:03:53 | Giriulla (Maha Oya) | 1.44 | 🟢 Normal | -0.010 |  |
| 2026-11-16 01:01:08 | Ellagawa (Kalu Ganga) | 5.44 | 🟢 Normal | -0.010 |  |
| 2026-11-16 01:03:22 | Thanamalwila (Kirindi Oya) | 1.49 | 🟢 Normal | -0.010 |  |
| 2026-11-16 01:03:20 | Katharagama (Menik Ganga) | -0.03 | 🟢 Normal | -0.011 |  |
| 2026-11-15 18:01:22 | Galgamuwa (Mee Oya) | 0.29 | 🟢 Normal | -0.011 |  |
| 2026-11-15 23:51:55 | Putupaula (Kalu Ganga) | 0.80 | 🟢 Normal | -0.013 |  |
| 2026-11-16 01:01:29 | Dunamale (Aththanagalu Oya) | 1.82 | 🟢 Normal | -0.021 |  |
| 2026-11-16 01:02:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.18 | 🟢 Normal | -0.024 |  |
| 2026-11-16 00:11:05 | Rathnapura (Kalu Ganga) | 1.85 | 🟢 Normal | -0.025 |  |
| 2026-11-15 18:01:59 | Weraganthota (Mahaweli Ganga) | -1.94 | 🟢 Normal | -0.181 |  |
| 2026-11-16 01:05:27 | Baddegama (Gin Ganga) | 1.36 | 🟢 Normal | -1.014 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)