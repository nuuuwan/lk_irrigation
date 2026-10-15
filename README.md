# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--15_07:12:32-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **288,349 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood; 🟡 Dunamale — Alert; 🟡 Kalawellawa (Millakanda) — Alert; 🟡 Panadugama — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-15 07:12:32 | Thaldena (Mahaweli Ganga) | 0.36 | 🟢 Normal | -0.009 |  |
| 2026-10-15 07:12:11 | Magura (Kalu Ganga) | 3.80 | 🟢 Normal | -0.078 |  |
| 2026-10-15 07:12:09 | Baddegama (Gin Ganga) | 2.45 | 🟢 Normal | -0.009 |  |
| 2026-10-15 07:11:34 | Rathnapura (Kalu Ganga) | 3.93 | 🟢 Normal | -0.127 |  |
| 2026-10-15 07:09:14 | Badalgama (Maha Oya) | 4.39 | 🟢 Normal | -0.028 |  |
| 2026-10-15 07:08:46 | Thawalama (Gin Ganga) | 2.25 | 🟢 Normal | -0.046 |  |
| 2026-10-15 07:08:00 | Urawa (Nilwala Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-10-15 07:07:42 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-10-15 07:07:17 | Yaka Wewa (Ma Oya) | 0.65 | 🟢 Normal | -0.009 |  |
| 2026-10-15 07:07:00 | Ellagawa (Kalu Ganga) | 8.10 | 🟢 Normal | 0.000 |  |
| 2026-10-15 07:06:49 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-10-15 07:06:49 | Kithulgala (Kelani Ganga) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-10-15 07:06:18 | Peradeniya (Mahaweli Ganga) | 3.00 | 🟢 Normal | -0.118 |  |
| 2026-10-15 07:06:15 | Dunamale (Aththanagalu Oya) | 3.91 | 🟡 Alert | 0.010 | 🔺 Rising |
| 2026-10-15 07:06:05 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-10-15 07:05:56 | Nagalagam Street (Kelani Ganga) | 0.88 | 🟢 Normal | -0.095 |  |
| 2026-10-15 07:04:47 | Putupaula (Kalu Ganga) | 2.34 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-10-15 07:04:43 | Moragaswewa (Deduru Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-10-15 07:03:49 | Hanwella (Kelani Ganga) | 4.99 | 🟢 Normal | -0.021 |  |
| 2026-10-15 07:03:38 | Panadugama (Nilwala Ganga) | 5.05 | 🟡 Alert | -0.069 |  |
| 2026-10-15 07:03:21 | Norwood (Kelani Ganga) | 1.13 | 🟢 Normal | -0.131 |  |
| 2026-10-15 07:03:14 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.03 | 🟡 Alert | -0.059 |  |
| 2026-10-15 07:02:57 | Giriulla (Maha Oya) | 2.99 | 🟢 Normal | -0.220 |  |
| 2026-10-15 07:02:44 | Manampitiya (Mahaweli Ganga) | 0.74 | 🟢 Normal | -0.049 |  |
| 2026-10-15 07:02:39 | Galgamuwa (Mee Oya) | 0.24 | 🟢 Normal | -0.020 |  |
| 2026-10-15 07:02:28 | Holombuwa (Kelani Ganga) | 1.61 | 🟢 Normal | -0.119 |  |
| 2026-10-15 07:02:21 | Deraniyagala (Kelani Ganga) | 0.85 | 🟢 Normal | -0.053 |  |
| 2026-10-15 07:02:17 | Thanthirimale (Malwathu Oya) | 1.07 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-10-15 07:02:13 | Thanamalwila (Kirindi Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-10-15 07:02:03 | Weraganthota (Mahaweli Ganga) | -3.11 | 🟢 Normal | -0.071 |  |
| 2026-10-15 07:01:32 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-10-15 07:01:16 | Nawalapitiya (Mahaweli Ganga) | 1.24 | 🟢 Normal | -0.010 |  |
| 2026-10-15 07:00:48 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-10-15 07:00:45 | Wellawaya (Kirindi Oya) | 1.13 | 🟢 Normal | -0.049 |  |
| 2026-10-15 07:00:29 | Kuda Oya (Kirindi Oya) | 1.24 | 🟢 Normal | -0.013 |  |
| 2026-10-15 07:00:15 | Horowpothana (Yan Oya) | 1.79 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-10-15 07:00:11 | Pitabeddara (Nilwala Ganga) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-10-15 06:32:31 | Galgamuwa (Mee Oya) | 0.25 | 🟢 Normal | -0.020 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-15 06:28:41 | Thalgahagoda (Nilwala Ganga) | 1.75 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-15 07:06:15 | Dunamale (Aththanagalu Oya) | 3.91 | 🟡 Alert | 0.010 | 🔺 Rising |
| 2026-10-15 07:03:14 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.03 | 🟡 Alert | -0.059 |  |
| 2026-10-15 07:03:38 | Panadugama (Nilwala Ganga) | 5.05 | 🟡 Alert | -0.069 |  |
| 2026-10-15 06:26:09 | Glencourse (Kelani Ganga) | 13.38 | 🟢 Normal | 77.143 | 🔺 Rising |
| 2026-10-15 06:01:21 | Moraketiya (Walawe Ganga) | 1.28 | 🟢 Normal | 0.123 | 🔺 Rising |
| 2026-10-15 07:04:47 | Putupaula (Kalu Ganga) | 2.34 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-10-15 07:00:15 | Horowpothana (Yan Oya) | 1.79 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-10-15 07:02:17 | Thanthirimale (Malwathu Oya) | 1.07 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-10-15 07:06:49 | Kithulgala (Kelani Ganga) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-10-15 07:00:48 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-10-15 07:04:43 | Moragaswewa (Deduru Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-10-15 07:00:11 | Pitabeddara (Nilwala Ganga) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-10-15 07:07:00 | Ellagawa (Kalu Ganga) | 8.10 | 🟢 Normal | 0.000 |  |
| 2026-10-15 07:07:42 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-10-15 07:01:32 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-10-15 07:06:49 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-10-15 07:08:00 | Urawa (Nilwala Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-10-15 07:02:13 | Thanamalwila (Kirindi Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-10-15 07:12:32 | Thaldena (Mahaweli Ganga) | 0.36 | 🟢 Normal | -0.009 |  |
| 2026-10-15 07:12:09 | Baddegama (Gin Ganga) | 2.45 | 🟢 Normal | -0.009 |  |
| 2026-10-15 07:07:17 | Yaka Wewa (Ma Oya) | 0.65 | 🟢 Normal | -0.009 |  |
| 2026-10-15 07:01:16 | Nawalapitiya (Mahaweli Ganga) | 1.24 | 🟢 Normal | -0.010 |  |
| 2026-10-15 07:00:29 | Kuda Oya (Kirindi Oya) | 1.24 | 🟢 Normal | -0.013 |  |
| 2026-10-15 07:02:39 | Galgamuwa (Mee Oya) | 0.24 | 🟢 Normal | -0.020 |  |
| 2026-10-15 07:03:49 | Hanwella (Kelani Ganga) | 4.99 | 🟢 Normal | -0.021 |  |
| 2026-10-15 07:09:14 | Badalgama (Maha Oya) | 4.39 | 🟢 Normal | -0.028 |  |
| 2026-10-15 07:08:46 | Thawalama (Gin Ganga) | 2.25 | 🟢 Normal | -0.046 |  |
| 2026-10-15 07:02:44 | Manampitiya (Mahaweli Ganga) | 0.74 | 🟢 Normal | -0.049 |  |
| 2026-10-15 07:00:45 | Wellawaya (Kirindi Oya) | 1.13 | 🟢 Normal | -0.049 |  |
| 2026-10-15 07:02:21 | Deraniyagala (Kelani Ganga) | 0.85 | 🟢 Normal | -0.053 |  |
| 2026-10-15 07:02:03 | Weraganthota (Mahaweli Ganga) | -3.11 | 🟢 Normal | -0.071 |  |
| 2026-10-15 07:12:11 | Magura (Kalu Ganga) | 3.80 | 🟢 Normal | -0.078 |  |
| 2026-10-15 07:05:56 | Nagalagam Street (Kelani Ganga) | 0.88 | 🟢 Normal | -0.095 |  |
| 2026-10-15 07:06:18 | Peradeniya (Mahaweli Ganga) | 3.00 | 🟢 Normal | -0.118 |  |
| 2026-10-15 07:02:28 | Holombuwa (Kelani Ganga) | 1.61 | 🟢 Normal | -0.119 |  |
| 2026-10-15 07:11:34 | Rathnapura (Kalu Ganga) | 3.93 | 🟢 Normal | -0.127 |  |
| 2026-10-15 07:03:21 | Norwood (Kelani Ganga) | 1.13 | 🟢 Normal | -0.131 |  |
| 2026-10-15 07:02:57 | Giriulla (Maha Oya) | 2.99 | 🟢 Normal | -0.220 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)