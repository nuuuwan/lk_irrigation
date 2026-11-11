# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--11_12:07:49-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **312,873 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood; 🟠 Baddegama — Minor Flood; 🟡 Panadugama — Alert; 🟡 Dunamale — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **32** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-11 12:07:49 | Thawalama (Gin Ganga) | 2.35 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-11-11 12:06:41 | Moragaswewa (Deduru Oya) | 2.88 | 🟢 Normal | 0.205 | 🔺 Rising |
| 2026-11-11 12:06:21 | Galgamuwa (Mee Oya) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-11-11 12:06:17 | Thalgahagoda (Nilwala Ganga) | 1.79 | 🟠 Minor Flood | 0.000 |  |
| 2026-11-11 12:05:39 | Badalgama (Maha Oya) | 3.85 | 🟢 Normal | -0.143 |  |
| 2026-11-11 12:05:31 | Magura (Kalu Ganga) | 3.02 | 🟢 Normal | -0.095 |  |
| 2026-11-11 12:05:31 | Baddegama (Gin Ganga) | 4.22 | 🟠 Minor Flood | -0.011 |  |
| 2026-11-11 12:05:07 | Rathnapura (Kalu Ganga) | 4.23 | 🟢 Normal | -0.132 |  |
| 2026-11-11 12:04:33 | Putupaula (Kalu Ganga) | 2.64 | 🟢 Normal | 0.000 |  |
| 2026-11-11 12:04:28 | Thanamalwila (Kirindi Oya) | 1.77 | 🟢 Normal | 0.000 |  |
| 2026-11-11 12:04:10 | Kithulgala (Kelani Ganga) | 2.00 | 🟢 Normal | -0.098 |  |
| 2026-11-11 12:03:45 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.60 | 🟢 Normal | -1.971 |  |
| 2026-11-11 12:03:35 | Weraganthota (Mahaweli Ganga) | -2.30 | 🟢 Normal | -0.135 |  |
| 2026-11-11 12:03:22 | Hanwella (Kelani Ganga) | 4.36 | 🟢 Normal | -0.115 |  |
| 2026-11-11 12:03:21 | Katharagama (Menik Ganga) | 0.12 | 🟢 Normal | -0.010 |  |
| 2026-11-11 12:03:17 | Dunamale (Aththanagalu Oya) | 4.02 | 🟡 Alert | -0.088 |  |
| 2026-11-11 12:03:06 | Horowpothana (Yan Oya) | 2.45 | 🟢 Normal | -0.028 |  |
| 2026-11-11 12:02:45 | Nawalapitiya (Mahaweli Ganga) | 1.51 | 🟢 Normal | 0.000 |  |
| 2026-11-11 12:02:42 | Peradeniya (Mahaweli Ganga) | 3.84 | 🟢 Normal | -0.044 |  |
| 2026-11-11 12:02:40 | Pitabeddara (Nilwala Ganga) | 1.70 | 🟢 Normal | -0.048 |  |
| 2026-11-11 12:02:39 | Siyambalanduwa (Heda Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-11-11 12:02:34 | Panadugama (Nilwala Ganga) | 5.62 | 🟡 Alert | -0.050 |  |
| 2026-11-11 12:02:26 | Holombuwa (Kelani Ganga) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-11-11 12:02:25 | Thaldena (Mahaweli Ganga) | 0.67 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-11 12:02:11 | Moraketiya (Walawe Ganga) | 2.16 | 🟢 Normal | 0.000 |  |
| 2026-11-11 12:02:02 | Deraniyagala (Kelani Ganga) | 1.05 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-11 12:01:35 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.093 | 🔺 Rising |
| 2026-11-11 12:01:27 | Thanthirimale (Malwathu Oya) | 2.01 | 🟢 Normal | -0.020 |  |
| 2026-11-11 12:01:19 | Giriulla (Maha Oya) | 2.37 | 🟢 Normal | -0.081 |  |
| 2026-11-11 12:00:56 | Nakkala (Kumbukkan Oya) | 1.12 | 🟢 Normal | -0.020 |  |
| 2026-11-11 12:00:50 | Manampitiya (Mahaweli Ganga) | 1.30 | 🟢 Normal | 0.075 | 🔺 Rising |
| 2026-11-11 12:00:26 | Wellawaya (Kirindi Oya) | 1.50 | 🟢 Normal | -0.011 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-11 12:06:17 | Thalgahagoda (Nilwala Ganga) | 1.79 | 🟠 Minor Flood | 0.000 |  |
| 2026-11-11 12:05:31 | Baddegama (Gin Ganga) | 4.22 | 🟠 Minor Flood | -0.011 |  |
| 2026-11-11 12:02:34 | Panadugama (Nilwala Ganga) | 5.62 | 🟡 Alert | -0.050 |  |
| 2026-11-11 12:03:17 | Dunamale (Aththanagalu Oya) | 4.02 | 🟡 Alert | -0.088 |  |
| 2026-11-11 11:02:46 | Kuda Oya (Kirindi Oya) | 1.89 | 🟢 Normal | 1.078 | 🔺 Rising |
| 2026-11-11 12:06:41 | Moragaswewa (Deduru Oya) | 2.88 | 🟢 Normal | 0.205 | 🔺 Rising |
| 2026-11-11 12:01:35 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.093 | 🔺 Rising |
| 2026-11-11 12:00:50 | Manampitiya (Mahaweli Ganga) | 1.30 | 🟢 Normal | 0.075 | 🔺 Rising |
| 2026-11-11 12:07:49 | Thawalama (Gin Ganga) | 2.35 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-11-11 12:02:02 | Deraniyagala (Kelani Ganga) | 1.05 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-11 12:02:25 | Thaldena (Mahaweli Ganga) | 0.67 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-11 11:17:16 | Padiyathalawa (Maduru Oya) | 0.60 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-11-11 12:02:45 | Nawalapitiya (Mahaweli Ganga) | 1.51 | 🟢 Normal | 0.000 |  |
| 2026-11-11 12:06:21 | Galgamuwa (Mee Oya) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-11-11 12:02:11 | Moraketiya (Walawe Ganga) | 2.16 | 🟢 Normal | 0.000 |  |
| 2026-11-11 12:02:39 | Siyambalanduwa (Heda Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-11-11 12:04:33 | Putupaula (Kalu Ganga) | 2.64 | 🟢 Normal | 0.000 |  |
| 2026-11-11 12:02:26 | Holombuwa (Kelani Ganga) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-11-11 11:05:38 | Urawa (Nilwala Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-11-11 12:04:28 | Thanamalwila (Kirindi Oya) | 1.77 | 🟢 Normal | 0.000 |  |
| 2026-11-11 10:14:57 | Yaka Wewa (Ma Oya) | 0.57 | 🟢 Normal | -0.008 |  |
| 2026-11-11 11:02:54 | Norwood (Kelani Ganga) | 1.12 | 🟢 Normal | -0.010 |  |
| 2026-11-11 12:03:21 | Katharagama (Menik Ganga) | 0.12 | 🟢 Normal | -0.010 |  |
| 2026-11-11 12:00:26 | Wellawaya (Kirindi Oya) | 1.50 | 🟢 Normal | -0.011 |  |
| 2026-11-11 12:00:56 | Nakkala (Kumbukkan Oya) | 1.12 | 🟢 Normal | -0.020 |  |
| 2026-11-11 12:01:27 | Thanthirimale (Malwathu Oya) | 2.01 | 🟢 Normal | -0.020 |  |
| 2026-11-11 12:03:06 | Horowpothana (Yan Oya) | 2.45 | 🟢 Normal | -0.028 |  |
| 2026-11-11 11:02:09 | Ellagawa (Kalu Ganga) | 8.49 | 🟢 Normal | -0.036 |  |
| 2026-11-11 12:02:42 | Peradeniya (Mahaweli Ganga) | 3.84 | 🟢 Normal | -0.044 |  |
| 2026-11-11 12:02:40 | Pitabeddara (Nilwala Ganga) | 1.70 | 🟢 Normal | -0.048 |  |
| 2026-11-11 12:01:19 | Giriulla (Maha Oya) | 2.37 | 🟢 Normal | -0.081 |  |
| 2026-11-11 12:05:31 | Magura (Kalu Ganga) | 3.02 | 🟢 Normal | -0.095 |  |
| 2026-11-11 12:04:10 | Kithulgala (Kelani Ganga) | 2.00 | 🟢 Normal | -0.098 |  |
| 2026-11-11 11:05:14 | Glencourse (Kelani Ganga) | 11.87 | 🟢 Normal | -0.101 |  |
| 2026-11-11 12:03:22 | Hanwella (Kelani Ganga) | 4.36 | 🟢 Normal | -0.115 |  |
| 2026-11-11 12:05:07 | Rathnapura (Kalu Ganga) | 4.23 | 🟢 Normal | -0.132 |  |
| 2026-11-11 12:03:35 | Weraganthota (Mahaweli Ganga) | -2.30 | 🟢 Normal | -0.135 |  |
| 2026-11-11 12:05:39 | Badalgama (Maha Oya) | 3.85 | 🟢 Normal | -0.143 |  |
| 2026-11-11 12:03:45 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.60 | 🟢 Normal | -1.971 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)