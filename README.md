# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--09_12:13:05-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **311,112 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Dunamale — Minor Flood; 🟡 Kalawellawa (Millakanda) — Alert; 🟡 Baddegama — Alert; 🟡 Thalgahagoda — Alert; 🟡 Panadugama — Alert; 🟡 Magura — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **42** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-09 12:13:05 | Urawa (Nilwala Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-11-09 12:10:17 | Holombuwa (Kelani Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-11-09 12:09:34 | Thalgahagoda (Nilwala Ganga) | 1.52 | 🟡 Alert | 0.000 |  |
| 2026-11-09 12:08:23 | Urawa (Nilwala Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-11-09 12:08:18 | Rathnapura (Kalu Ganga) | 2.93 | 🟢 Normal | -0.046 |  |
| 2026-11-09 12:07:57 | Baddegama (Gin Ganga) | 3.65 | 🟡 Alert | 0.000 |  |
| 2026-11-09 12:07:38 | Padiyathalawa (Maduru Oya) | 0.50 | 🟢 Normal | -0.020 |  |
| 2026-11-09 12:07:17 | Panadugama (Nilwala Ganga) | 5.65 | 🟡 Alert | -0.043 |  |
| 2026-11-09 12:07:11 | Magura (Kalu Ganga) | 4.92 | 🟡 Alert | -0.049 |  |
| 2026-11-09 12:07:07 | Glencourse (Kelani Ganga) | 11.32 | 🟢 Normal | -0.106 |  |
| 2026-11-09 12:06:46 | Nagalagam Street (Kelani Ganga) | 0.79 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-11-09 12:06:42 | Thanamalwila (Kirindi Oya) | 1.49 | 🟢 Normal | -0.018 |  |
| 2026-11-09 12:06:05 | Galgamuwa (Mee Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-11-09 12:05:15 | Norwood (Kelani Ganga) | 0.97 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-11-09 12:05:15 | Holombuwa (Kelani Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-11-09 12:05:07 | Pitabeddara (Nilwala Ganga) | 2.63 | 🟢 Normal | 0.000 |  |
| 2026-11-09 12:03:45 | Giriulla (Maha Oya) | 2.85 | 🟢 Normal | -0.078 |  |
| 2026-11-09 12:03:42 | Badalgama (Maha Oya) | 4.09 | 🟢 Normal | -0.081 |  |
| 2026-11-09 12:03:35 | Moraketiya (Walawe Ganga) | 1.77 | 🟢 Normal | -0.059 |  |
| 2026-11-09 12:03:33 | Kuda Oya (Kirindi Oya) | 1.68 | 🟢 Normal | -0.010 |  |
| 2026-11-09 12:03:07 | Peradeniya (Mahaweli Ganga) | 2.98 | 🟢 Normal | 0.000 |  |
| 2026-11-09 12:03:06 | Weraganthota (Mahaweli Ganga) | -2.40 | 🟢 Normal | -0.147 |  |
| 2026-11-09 12:03:06 | Thaldena (Mahaweli Ganga) | 0.64 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-11-09 12:02:50 | Nawalapitiya (Mahaweli Ganga) | 1.33 | 🟢 Normal | -0.020 |  |
| 2026-11-09 12:02:50 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.99 | 🟡 Alert | 0.010 | 🔺 Rising |
| 2026-11-09 12:02:48 | Hanwella (Kelani Ganga) | 4.37 | 🟢 Normal | -0.152 |  |
| 2026-11-09 12:02:45 | Thawalama (Gin Ganga) | 2.18 | 🟢 Normal | -0.022 |  |
| 2026-11-09 12:02:41 | Moragaswewa (Deduru Oya) | 2.71 | 🟢 Normal | -0.021 |  |
| 2026-11-09 12:02:39 | Kithulgala (Kelani Ganga) | 1.76 | 🟢 Normal | -0.020 |  |
| 2026-11-09 12:02:24 | Deraniyagala (Kelani Ganga) | 0.67 | 🟢 Normal | -0.010 |  |
| 2026-11-09 12:02:14 | Katharagama (Menik Ganga) | 0.00 | 🟢 Normal | -0.010 |  |
| 2026-11-09 12:02:11 | Putupaula (Kalu Ganga) | 2.38 | 🟢 Normal | -0.010 |  |
| 2026-11-09 12:02:05 | Ellagawa (Kalu Ganga) | 7.70 | 🟢 Normal | -0.082 |  |
| 2026-11-09 12:01:56 | Wellawaya (Kirindi Oya) | 1.31 | 🟢 Normal | -0.010 |  |
| 2026-11-09 12:01:54 | Yaka Wewa (Ma Oya) | 0.75 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-11-09 12:01:45 | Horowpothana (Yan Oya) | 2.71 | 🟢 Normal | 0.000 |  |
| 2026-11-09 12:01:31 | Siyambalanduwa (Heda Oya) | 0.55 | 🟢 Normal | -0.011 |  |
| 2026-11-09 12:01:11 | Manampitiya (Mahaweli Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-11-09 12:00:54 | Dunamale (Aththanagalu Oya) | 4.44 | 🟠 Minor Flood | 0.010 | 🔺 Rising |
| 2026-11-09 12:00:45 | Nakkala (Kumbukkan Oya) | 1.05 | 🟢 Normal | -0.010 |  |
| 2026-11-09 12:00:36 | Pitabeddara (Nilwala Ganga) | 2.63 | 🟢 Normal | 0.000 |  |
| 2026-11-09 12:00:33 | Thanthirimale (Malwathu Oya) | 1.89 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-09 12:00:54 | Dunamale (Aththanagalu Oya) | 4.44 | 🟠 Minor Flood | 0.010 | 🔺 Rising |
| 2026-11-09 12:02:50 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.99 | 🟡 Alert | 0.010 | 🔺 Rising |
| 2026-11-09 12:07:57 | Baddegama (Gin Ganga) | 3.65 | 🟡 Alert | 0.000 |  |
| 2026-11-09 12:09:34 | Thalgahagoda (Nilwala Ganga) | 1.52 | 🟡 Alert | 0.000 |  |
| 2026-11-09 12:07:17 | Panadugama (Nilwala Ganga) | 5.65 | 🟡 Alert | -0.043 |  |
| 2026-11-09 12:07:11 | Magura (Kalu Ganga) | 4.92 | 🟡 Alert | -0.049 |  |
| 2026-11-09 12:06:46 | Nagalagam Street (Kelani Ganga) | 0.79 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-11-09 12:01:54 | Yaka Wewa (Ma Oya) | 0.75 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-11-09 12:03:06 | Thaldena (Mahaweli Ganga) | 0.64 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-11-09 12:05:15 | Norwood (Kelani Ganga) | 0.97 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-11-09 12:01:45 | Horowpothana (Yan Oya) | 2.71 | 🟢 Normal | 0.000 |  |
| 2026-11-09 12:06:05 | Galgamuwa (Mee Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-11-09 12:05:07 | Pitabeddara (Nilwala Ganga) | 2.63 | 🟢 Normal | 0.000 |  |
| 2026-11-09 12:10:17 | Holombuwa (Kelani Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-11-09 12:01:11 | Manampitiya (Mahaweli Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-11-09 12:00:33 | Thanthirimale (Malwathu Oya) | 1.89 | 🟢 Normal | 0.000 |  |
| 2026-11-09 12:03:07 | Peradeniya (Mahaweli Ganga) | 2.98 | 🟢 Normal | 0.000 |  |
| 2026-11-09 12:13:05 | Urawa (Nilwala Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-11-09 12:01:56 | Wellawaya (Kirindi Oya) | 1.31 | 🟢 Normal | -0.010 |  |
| 2026-11-09 12:03:33 | Kuda Oya (Kirindi Oya) | 1.68 | 🟢 Normal | -0.010 |  |
| 2026-11-09 12:02:11 | Putupaula (Kalu Ganga) | 2.38 | 🟢 Normal | -0.010 |  |
| 2026-11-09 12:02:24 | Deraniyagala (Kelani Ganga) | 0.67 | 🟢 Normal | -0.010 |  |
| 2026-11-09 12:00:45 | Nakkala (Kumbukkan Oya) | 1.05 | 🟢 Normal | -0.010 |  |
| 2026-11-09 12:02:14 | Katharagama (Menik Ganga) | 0.00 | 🟢 Normal | -0.010 |  |
| 2026-11-09 12:01:31 | Siyambalanduwa (Heda Oya) | 0.55 | 🟢 Normal | -0.011 |  |
| 2026-11-09 12:06:42 | Thanamalwila (Kirindi Oya) | 1.49 | 🟢 Normal | -0.018 |  |
| 2026-11-09 12:07:38 | Padiyathalawa (Maduru Oya) | 0.50 | 🟢 Normal | -0.020 |  |
| 2026-11-09 12:02:50 | Nawalapitiya (Mahaweli Ganga) | 1.33 | 🟢 Normal | -0.020 |  |
| 2026-11-09 12:02:39 | Kithulgala (Kelani Ganga) | 1.76 | 🟢 Normal | -0.020 |  |
| 2026-11-09 12:02:41 | Moragaswewa (Deduru Oya) | 2.71 | 🟢 Normal | -0.021 |  |
| 2026-11-09 12:02:45 | Thawalama (Gin Ganga) | 2.18 | 🟢 Normal | -0.022 |  |
| 2026-11-09 12:08:18 | Rathnapura (Kalu Ganga) | 2.93 | 🟢 Normal | -0.046 |  |
| 2026-11-09 12:03:35 | Moraketiya (Walawe Ganga) | 1.77 | 🟢 Normal | -0.059 |  |
| 2026-11-09 12:03:45 | Giriulla (Maha Oya) | 2.85 | 🟢 Normal | -0.078 |  |
| 2026-11-09 12:03:42 | Badalgama (Maha Oya) | 4.09 | 🟢 Normal | -0.081 |  |
| 2026-11-09 12:02:05 | Ellagawa (Kalu Ganga) | 7.70 | 🟢 Normal | -0.082 |  |
| 2026-11-09 12:07:07 | Glencourse (Kelani Ganga) | 11.32 | 🟢 Normal | -0.106 |  |
| 2026-11-09 12:03:06 | Weraganthota (Mahaweli Ganga) | -2.40 | 🟢 Normal | -0.147 |  |
| 2026-11-09 12:02:48 | Hanwella (Kelani Ganga) | 4.37 | 🟢 Normal | -0.152 |  |

## River Water Level Charts by Station

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

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

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)