# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--13_12:16:58-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **286,724 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Thalgahagoda — Alert; 🟡 Kalawellawa (Millakanda) — Alert; 🟡 Panadugama — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-13 12:16:58 | Urawa (Nilwala Ganga) | 1.18 | 🟢 Normal | -0.052 |  |
| 2026-10-13 12:09:10 | Dunamale (Aththanagalu Oya) | 2.40 | 🟢 Normal | -0.043 |  |
| 2026-10-13 12:08:54 | Ellagawa (Kalu Ganga) | 7.15 | 🟢 Normal | 0.000 |  |
| 2026-10-13 12:08:53 | Rathnapura (Kalu Ganga) | 3.03 | 🟢 Normal | -0.099 |  |
| 2026-10-13 12:06:33 | Thawalama (Gin Ganga) | 2.29 | 🟢 Normal | -0.057 |  |
| 2026-10-13 12:06:30 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.085 | 🔺 Rising |
| 2026-10-13 12:06:28 | Manampitiya (Mahaweli Ganga) | -0.29 | 🟢 Normal | -0.009 |  |
| 2026-10-13 12:06:24 | Panadugama (Nilwala Ganga) | 5.98 | 🟡 Alert | -0.050 |  |
| 2026-10-13 12:06:23 | Magura (Kalu Ganga) | 2.39 | 🟢 Normal | -0.121 |  |
| 2026-10-13 12:06:18 | Kuda Oya (Kirindi Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-10-13 12:06:16 | Moragaswewa (Deduru Oya) | 0.73 | 🟢 Normal | -0.019 |  |
| 2026-10-13 12:06:10 | Badalgama (Maha Oya) | 2.87 | 🟢 Normal | 0.000 |  |
| 2026-10-13 12:05:55 | Norwood (Kelani Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-10-13 12:05:26 | Putupaula (Kalu Ganga) | 1.75 | 🟢 Normal | -0.010 |  |
| 2026-10-13 12:04:40 | Norwood (Kelani Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-10-13 12:04:27 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.16 | 🟡 Alert | -0.030 |  |
| 2026-10-13 12:04:21 | Thalgahagoda (Nilwala Ganga) | 1.54 | 🟡 Alert | 0.019 | 🔺 Rising |
| 2026-10-13 12:04:12 | Pitabeddara (Nilwala Ganga) | 1.93 | 🟢 Normal | -0.161 |  |
| 2026-10-13 12:03:45 | Baddegama (Gin Ganga) | 2.65 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-13 12:03:44 | Glencourse (Kelani Ganga) | 11.00 | 🟢 Normal | 0.000 |  |
| 2026-10-13 12:03:31 | Giriulla (Maha Oya) | 1.58 | 🟢 Normal | -0.030 |  |
| 2026-10-13 12:03:18 | Deraniyagala (Kelani Ganga) | 0.66 | 🟢 Normal | -0.022 |  |
| 2026-10-13 12:03:07 | Kithulgala (Kelani Ganga) | 1.90 | 🟢 Normal | -0.029 |  |
| 2026-10-13 12:02:58 | Nakkala (Kumbukkan Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-10-13 12:02:48 | Peradeniya (Mahaweli Ganga) | 2.30 | 🟢 Normal | -0.234 |  |
| 2026-10-13 12:02:46 | Hanwella (Kelani Ganga) | 3.39 | 🟢 Normal | -0.060 |  |
| 2026-10-13 12:02:42 | Katharagama (Menik Ganga) | -0.20 | 🟢 Normal | 0.000 |  |
| 2026-10-13 12:02:40 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-10-13 12:02:08 | Thanamalwila (Kirindi Oya) | 0.79 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-10-13 12:01:52 | Nawalapitiya (Mahaweli Ganga) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-10-13 12:01:33 | Yaka Wewa (Ma Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-10-13 12:01:17 | Kuda Oya (Kirindi Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-10-13 12:01:15 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-13 12:01:14 | Wellawaya (Kirindi Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-10-13 12:00:58 | Thaldena (Mahaweli Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-10-13 12:00:42 | Moraketiya (Walawe Ganga) | 1.18 | 🟢 Normal | -0.021 |  |
| 2026-10-13 12:00:37 | Thanthirimale (Malwathu Oya) | 0.99 | 🟢 Normal | -0.020 |  |
| 2026-10-13 12:00:10 | Weraganthota (Mahaweli Ganga) | -3.30 | 🟢 Normal | -0.030 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-13 12:04:21 | Thalgahagoda (Nilwala Ganga) | 1.54 | 🟡 Alert | 0.019 | 🔺 Rising |
| 2026-10-13 12:04:27 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.16 | 🟡 Alert | -0.030 |  |
| 2026-10-13 12:06:24 | Panadugama (Nilwala Ganga) | 5.98 | 🟡 Alert | -0.050 |  |
| 2026-10-13 12:06:30 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.085 | 🔺 Rising |
| 2026-10-13 12:02:08 | Thanamalwila (Kirindi Oya) | 0.79 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-10-13 12:01:15 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-13 12:03:45 | Baddegama (Gin Ganga) | 2.65 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-13 12:01:14 | Wellawaya (Kirindi Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-10-13 12:02:58 | Nakkala (Kumbukkan Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-10-13 12:01:52 | Nawalapitiya (Mahaweli Ganga) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-10-13 12:01:33 | Yaka Wewa (Ma Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-10-13 11:00:55 | Horowpothana (Yan Oya) | 1.61 | 🟢 Normal | 0.000 |  |
| 2026-10-13 11:03:15 | Galgamuwa (Mee Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-10-13 12:05:55 | Norwood (Kelani Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-10-13 12:08:54 | Ellagawa (Kalu Ganga) | 7.15 | 🟢 Normal | 0.000 |  |
| 2026-10-13 12:03:44 | Glencourse (Kelani Ganga) | 11.00 | 🟢 Normal | 0.000 |  |
| 2026-10-13 12:02:40 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-10-13 12:00:58 | Thaldena (Mahaweli Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-10-13 12:02:42 | Katharagama (Menik Ganga) | -0.20 | 🟢 Normal | 0.000 |  |
| 2026-10-13 12:06:10 | Badalgama (Maha Oya) | 2.87 | 🟢 Normal | 0.000 |  |
| 2026-10-13 11:06:14 | Holombuwa (Kelani Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-10-13 12:06:18 | Kuda Oya (Kirindi Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-10-13 12:06:28 | Manampitiya (Mahaweli Ganga) | -0.29 | 🟢 Normal | -0.009 |  |
| 2026-10-13 12:05:26 | Putupaula (Kalu Ganga) | 1.75 | 🟢 Normal | -0.010 |  |
| 2026-10-13 12:06:16 | Moragaswewa (Deduru Oya) | 0.73 | 🟢 Normal | -0.019 |  |
| 2026-10-13 12:00:37 | Thanthirimale (Malwathu Oya) | 0.99 | 🟢 Normal | -0.020 |  |
| 2026-10-13 12:00:42 | Moraketiya (Walawe Ganga) | 1.18 | 🟢 Normal | -0.021 |  |
| 2026-10-13 12:03:18 | Deraniyagala (Kelani Ganga) | 0.66 | 🟢 Normal | -0.022 |  |
| 2026-10-13 12:03:07 | Kithulgala (Kelani Ganga) | 1.90 | 🟢 Normal | -0.029 |  |
| 2026-10-13 12:03:31 | Giriulla (Maha Oya) | 1.58 | 🟢 Normal | -0.030 |  |
| 2026-10-13 12:00:10 | Weraganthota (Mahaweli Ganga) | -3.30 | 🟢 Normal | -0.030 |  |
| 2026-10-13 12:09:10 | Dunamale (Aththanagalu Oya) | 2.40 | 🟢 Normal | -0.043 |  |
| 2026-10-13 12:16:58 | Urawa (Nilwala Ganga) | 1.18 | 🟢 Normal | -0.052 |  |
| 2026-10-13 12:06:33 | Thawalama (Gin Ganga) | 2.29 | 🟢 Normal | -0.057 |  |
| 2026-10-13 12:02:46 | Hanwella (Kelani Ganga) | 3.39 | 🟢 Normal | -0.060 |  |
| 2026-10-13 12:08:53 | Rathnapura (Kalu Ganga) | 3.03 | 🟢 Normal | -0.099 |  |
| 2026-10-13 12:06:23 | Magura (Kalu Ganga) | 2.39 | 🟢 Normal | -0.121 |  |
| 2026-10-13 12:04:12 | Pitabeddara (Nilwala Ganga) | 1.93 | 🟢 Normal | -0.161 |  |
| 2026-10-13 12:02:48 | Peradeniya (Mahaweli Ganga) | 2.30 | 🟢 Normal | -0.234 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)