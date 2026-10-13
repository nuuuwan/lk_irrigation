# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--13_17:17:40-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **286,919 measurements** from **39** stations.
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
| 2026-10-13 17:17:40 | Norwood (Kelani Ganga) | 1.18 | 🟢 Normal | -0.109 |  |
| 2026-10-13 17:16:17 | Urawa (Nilwala Ganga) | 1.20 | 🟢 Normal | 0.118 | 🔺 Rising |
| 2026-10-13 17:15:45 | Magura (Kalu Ganga) | 2.88 | 🟢 Normal | 0.564 | 🔺 Rising |
| 2026-10-13 17:10:38 | Peradeniya (Mahaweli Ganga) | 2.88 | 🟢 Normal | 0.203 | 🔺 Rising |
| 2026-10-13 17:09:30 | Dunamale (Aththanagalu Oya) | 2.26 | 🟢 Normal | -0.021 |  |
| 2026-10-13 17:09:16 | Ellagawa (Kalu Ganga) | 7.05 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-10-13 17:08:24 | Thalgahagoda (Nilwala Ganga) | 1.59 | 🟡 Alert | 0.018 | 🔺 Rising |
| 2026-10-13 17:08:06 | Panadugama (Nilwala Ganga) | 5.75 | 🟡 Alert | -0.046 |  |
| 2026-10-13 17:07:01 | Baddegama (Gin Ganga) | 2.61 | 🟢 Normal | -0.010 |  |
| 2026-10-13 17:06:11 | Yaka Wewa (Ma Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-10-13 17:06:07 | Thawalama (Gin Ganga) | 1.93 | 🟢 Normal | -0.022 |  |
| 2026-10-13 17:05:28 | Putupaula (Kalu Ganga) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-10-13 17:05:27 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-13 17:05:24 | Katharagama (Menik Ganga) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-10-13 17:04:36 | Badalgama (Maha Oya) | 2.82 | 🟢 Normal | -0.010 |  |
| 2026-10-13 17:04:34 | Hanwella (Kelani Ganga) | 3.23 | 🟢 Normal | -0.011 |  |
| 2026-10-13 17:04:31 | Nagalagam Street (Kelani Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-10-13 17:04:07 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.06 | 🟡 Alert | -0.021 |  |
| 2026-10-13 17:03:58 | Manampitiya (Mahaweli Ganga) | -0.29 | 🟢 Normal | 0.000 |  |
| 2026-10-13 17:03:41 | Glencourse (Kelani Ganga) | 10.95 | 🟢 Normal | -0.021 |  |
| 2026-10-13 17:03:32 | Rathnapura (Kalu Ganga) | 2.98 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-10-13 17:03:19 | Giriulla (Maha Oya) | 1.49 | 🟢 Normal | -0.020 |  |
| 2026-10-13 17:03:02 | Galgamuwa (Mee Oya) | 0.07 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-13 17:02:41 | Holombuwa (Kelani Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-10-13 17:02:40 | Deraniyagala (Kelani Ganga) | 0.70 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-10-13 17:02:34 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | -0.019 |  |
| 2026-10-13 17:02:23 | Pitabeddara (Nilwala Ganga) | 1.60 | 🟢 Normal | -0.080 |  |
| 2026-10-13 17:02:22 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | -0.010 |  |
| 2026-10-13 17:02:21 | Moraketiya (Walawe Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-10-13 17:02:12 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-10-13 17:02:12 | Thanamalwila (Kirindi Oya) | 0.77 | 🟢 Normal | -0.032 |  |
| 2026-10-13 17:01:44 | Kuda Oya (Kirindi Oya) | 1.17 | 🟢 Normal | -0.020 |  |
| 2026-10-13 17:01:35 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | -0.010 |  |
| 2026-10-13 17:01:27 | Nawalapitiya (Mahaweli Ganga) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-10-13 17:01:11 | Thanthirimale (Malwathu Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-10-13 17:00:49 | Moragaswewa (Deduru Oya) | 0.68 | 🟢 Normal | -0.010 |  |
| 2026-10-13 17:00:47 | Weraganthota (Mahaweli Ganga) | -3.34 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-13 17:00:07 | Horowpothana (Yan Oya) | 1.60 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-13 17:08:24 | Thalgahagoda (Nilwala Ganga) | 1.59 | 🟡 Alert | 0.018 | 🔺 Rising |
| 2026-10-13 17:04:07 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.06 | 🟡 Alert | -0.021 |  |
| 2026-10-13 17:08:06 | Panadugama (Nilwala Ganga) | 5.75 | 🟡 Alert | -0.046 |  |
| 2026-10-13 17:15:45 | Magura (Kalu Ganga) | 2.88 | 🟢 Normal | 0.564 | 🔺 Rising |
| 2026-10-13 17:10:38 | Peradeniya (Mahaweli Ganga) | 2.88 | 🟢 Normal | 0.203 | 🔺 Rising |
| 2026-10-13 17:16:17 | Urawa (Nilwala Ganga) | 1.20 | 🟢 Normal | 0.118 | 🔺 Rising |
| 2026-10-13 17:09:16 | Ellagawa (Kalu Ganga) | 7.05 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-10-13 17:02:40 | Deraniyagala (Kelani Ganga) | 0.70 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-10-13 17:03:32 | Rathnapura (Kalu Ganga) | 2.98 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-10-13 17:03:02 | Galgamuwa (Mee Oya) | 0.07 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-13 17:00:47 | Weraganthota (Mahaweli Ganga) | -3.34 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-13 17:05:27 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-13 17:01:27 | Nawalapitiya (Mahaweli Ganga) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-10-13 17:06:11 | Yaka Wewa (Ma Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-10-13 17:00:07 | Horowpothana (Yan Oya) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-10-13 17:02:12 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-10-13 17:04:31 | Nagalagam Street (Kelani Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-10-13 17:02:21 | Moraketiya (Walawe Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-10-13 17:05:24 | Katharagama (Menik Ganga) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-10-13 17:05:28 | Putupaula (Kalu Ganga) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-10-13 17:02:41 | Holombuwa (Kelani Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-10-13 17:03:58 | Manampitiya (Mahaweli Ganga) | -0.29 | 🟢 Normal | 0.000 |  |
| 2026-10-13 17:01:11 | Thanthirimale (Malwathu Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-10-13 17:07:01 | Baddegama (Gin Ganga) | 2.61 | 🟢 Normal | -0.010 |  |
| 2026-10-13 17:01:35 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | -0.010 |  |
| 2026-10-13 17:02:22 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | -0.010 |  |
| 2026-10-13 17:04:36 | Badalgama (Maha Oya) | 2.82 | 🟢 Normal | -0.010 |  |
| 2026-10-13 17:00:49 | Moragaswewa (Deduru Oya) | 0.68 | 🟢 Normal | -0.010 |  |
| 2026-10-13 17:04:34 | Hanwella (Kelani Ganga) | 3.23 | 🟢 Normal | -0.011 |  |
| 2026-10-13 17:02:34 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | -0.019 |  |
| 2026-10-13 17:01:44 | Kuda Oya (Kirindi Oya) | 1.17 | 🟢 Normal | -0.020 |  |
| 2026-10-13 17:03:19 | Giriulla (Maha Oya) | 1.49 | 🟢 Normal | -0.020 |  |
| 2026-10-13 17:03:41 | Glencourse (Kelani Ganga) | 10.95 | 🟢 Normal | -0.021 |  |
| 2026-10-13 17:09:30 | Dunamale (Aththanagalu Oya) | 2.26 | 🟢 Normal | -0.021 |  |
| 2026-10-13 17:06:07 | Thawalama (Gin Ganga) | 1.93 | 🟢 Normal | -0.022 |  |
| 2026-10-13 17:02:12 | Thanamalwila (Kirindi Oya) | 0.77 | 🟢 Normal | -0.032 |  |
| 2026-10-13 16:02:21 | Kithulgala (Kelani Ganga) | 1.71 | 🟢 Normal | -0.040 |  |
| 2026-10-13 17:02:23 | Pitabeddara (Nilwala Ganga) | 1.60 | 🟢 Normal | -0.080 |  |
| 2026-10-13 17:17:40 | Norwood (Kelani Ganga) | 1.18 | 🟢 Normal | -0.109 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)