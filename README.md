# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--07_22:02:12-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **309,653 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Dunamale — Alert; 🟡 Urawa — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **9** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-07 22:02:12 | Hanwella (Kelani Ganga) | 3.53 | 🟢 Normal | 0.000 |  |
| 2026-11-07 22:01:39 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-11-07 22:01:22 | Moragaswewa (Deduru Oya) | 1.33 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-07 22:01:19 | Horowpothana (Yan Oya) | 2.44 | 🟢 Normal | 0.000 |  |
| 2026-11-07 22:01:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.97 | 🟢 Normal | -0.011 |  |
| 2026-11-07 22:00:37 | Nakkala (Kumbukkan Oya) | 0.98 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-11-07 22:00:17 | Glencourse (Kelani Ganga) | 10.85 | 🟢 Normal | -0.053 |  |
| 2026-11-07 21:37:27 | Norwood (Kelani Ganga) | 1.09 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-11-07 21:18:43 | Panadugama (Nilwala Ganga) | 3.98 | 🟢 Normal | 0.188 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-07 21:02:48 | Dunamale (Aththanagalu Oya) | 3.68 | 🟡 Alert | 0.100 | 🔺 Rising |
| 2026-11-07 21:08:17 | Urawa (Nilwala Ganga) | 3.84 | 🟡 Alert | 0.029 | 🔺 Rising |
| 2026-11-07 21:01:07 | Moraketiya (Walawe Ganga) | 2.45 | 🟢 Normal | 0.500 | 🔺 Rising |
| 2026-11-07 21:06:36 | Giriulla (Maha Oya) | 2.78 | 🟢 Normal | 0.470 | 🔺 Rising |
| 2026-11-07 21:06:29 | Thawalama (Gin Ganga) | 2.57 | 🟢 Normal | 0.360 | 🔺 Rising |
| 2026-11-07 21:18:43 | Panadugama (Nilwala Ganga) | 3.98 | 🟢 Normal | 0.188 | 🔺 Rising |
| 2026-11-07 21:03:09 | Wellawaya (Kirindi Oya) | 3.29 | 🟢 Normal | 0.132 | 🔺 Rising |
| 2026-11-07 21:03:28 | Magura (Kalu Ganga) | 2.58 | 🟢 Normal | 0.103 | 🔺 Rising |
| 2026-11-07 21:11:46 | Rathnapura (Kalu Ganga) | 3.11 | 🟢 Normal | 0.101 | 🔺 Rising |
| 2026-11-07 21:03:47 | Baddegama (Gin Ganga) | 2.05 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2026-11-07 21:06:44 | Holombuwa (Kelani Ganga) | 1.34 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-11-07 20:04:53 | Deraniyagala (Kelani Ganga) | 0.74 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-11-07 21:37:27 | Norwood (Kelani Ganga) | 1.09 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-11-07 21:05:19 | Peradeniya (Mahaweli Ganga) | 3.90 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-07 22:00:37 | Nakkala (Kumbukkan Oya) | 0.98 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-11-07 21:05:32 | Kuda Oya (Kirindi Oya) | 1.66 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-07 21:06:31 | Pitabeddara (Nilwala Ganga) | 1.70 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-07 21:04:22 | Ellagawa (Kalu Ganga) | 6.18 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-07 22:01:22 | Moragaswewa (Deduru Oya) | 1.33 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-07 21:10:06 | Kithulgala (Kelani Ganga) | 1.84 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-07 21:06:07 | Nawalapitiya (Mahaweli Ganga) | 1.32 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-07 21:07:51 | Thanamalwila (Kirindi Oya) | 1.49 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-11-07 21:07:19 | Katharagama (Menik Ganga) | 0.13 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-11-07 22:01:39 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-11-07 22:01:19 | Horowpothana (Yan Oya) | 2.44 | 🟢 Normal | 0.000 |  |
| 2026-11-07 18:03:13 | Galgamuwa (Mee Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-11-07 22:02:12 | Hanwella (Kelani Ganga) | 3.53 | 🟢 Normal | 0.000 |  |
| 2026-11-07 21:06:26 | Padiyathalawa (Maduru Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-07 21:04:16 | Siyambalanduwa (Heda Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-11-07 21:03:16 | Badalgama (Maha Oya) | 3.50 | 🟢 Normal | 0.000 |  |
| 2026-11-07 18:01:10 | Thanthirimale (Malwathu Oya) | 1.52 | 🟢 Normal | -0.010 |  |
| 2026-11-07 22:01:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.97 | 🟢 Normal | -0.011 |  |
| 2026-11-07 18:00:15 | Weraganthota (Mahaweli Ganga) | -2.95 | 🟢 Normal | -0.021 |  |
| 2026-11-07 21:02:13 | Manampitiya (Mahaweli Ganga) | 1.24 | 🟢 Normal | -0.021 |  |
| 2026-11-07 21:02:40 | Putupaula (Kalu Ganga) | 1.41 | 🟢 Normal | -0.022 |  |
| 2026-11-07 21:01:57 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.031 |  |
| 2026-11-07 22:00:17 | Glencourse (Kelani Ganga) | 10.85 | 🟢 Normal | -0.053 |  |
| 2026-11-07 21:01:53 | Thaldena (Mahaweli Ganga) | 1.76 | 🟢 Normal | -0.153 |  |
| 2026-11-07 21:04:52 | Thalgahagoda (Nilwala Ganga) | 0.98 | 🟢 Normal | -0.175 |  |

## River Water Level Charts by Station

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)