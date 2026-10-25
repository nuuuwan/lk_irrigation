# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--25_23:03:46-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **297,936 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Rathnapura — Alert; 🟡 Norwood — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **16** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-25 23:03:46 | Norwood (Kelani Ganga) | 1.64 | 🟡 Alert | 0.077 | 🔺 Rising |
| 2026-10-25 23:03:36 | Deraniyagala (Kelani Ganga) | 1.87 | 🟢 Normal | 0.235 | 🔺 Rising |
| 2026-10-25 23:02:51 | Moraketiya (Walawe Ganga) | 1.19 | 🟢 Normal | -0.010 |  |
| 2026-10-25 23:02:48 | Thalgahagoda (Nilwala Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-10-25 23:02:24 | Hanwella (Kelani Ganga) | 3.35 | 🟢 Normal | 0.140 | 🔺 Rising |
| 2026-10-25 23:02:21 | Nakkala (Kumbukkan Oya) | 1.62 | 🟢 Normal | -0.089 |  |
| 2026-10-25 23:01:47 | Yaka Wewa (Ma Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-10-25 23:01:45 | Moragaswewa (Deduru Oya) | 1.43 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-10-25 23:01:40 | Manampitiya (Mahaweli Ganga) | 0.45 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-10-25 23:01:32 | Peradeniya (Mahaweli Ganga) | 3.65 | 🟢 Normal | -0.054 |  |
| 2026-10-25 23:01:29 | Padiyathalawa (Maduru Oya) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-10-25 23:01:25 | Kuda Oya (Kirindi Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-10-25 23:01:09 | Ellagawa (Kalu Ganga) | 7.71 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-10-25 23:00:53 | Magura (Kalu Ganga) | 3.32 | 🟢 Normal | 0.116 | 🔺 Rising |
| 2026-10-25 23:00:48 | Wellawaya (Kirindi Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-10-25 23:00:15 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | 0.080 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-25 22:07:29 | Rathnapura (Kalu Ganga) | 5.59 | 🟡 Alert | 0.508 | 🔺 Rising |
| 2026-10-25 23:03:46 | Norwood (Kelani Ganga) | 1.64 | 🟡 Alert | 0.077 | 🔺 Rising |
| 2026-10-25 23:03:36 | Deraniyagala (Kelani Ganga) | 1.87 | 🟢 Normal | 0.235 | 🔺 Rising |
| 2026-10-25 22:07:06 | Giriulla (Maha Oya) | 2.40 | 🟢 Normal | 0.218 | 🔺 Rising |
| 2026-10-25 23:02:24 | Hanwella (Kelani Ganga) | 3.35 | 🟢 Normal | 0.140 | 🔺 Rising |
| 2026-10-25 22:05:20 | Glencourse (Kelani Ganga) | 11.81 | 🟢 Normal | 0.137 | 🔺 Rising |
| 2026-10-25 22:02:28 | Dunamale (Aththanagalu Oya) | 2.82 | 🟢 Normal | 0.122 | 🔺 Rising |
| 2026-10-25 18:03:46 | Galgamuwa (Mee Oya) | 1.82 | 🟢 Normal | 0.121 | 🔺 Rising |
| 2026-10-25 23:00:53 | Magura (Kalu Ganga) | 3.32 | 🟢 Normal | 0.116 | 🔺 Rising |
| 2026-10-25 22:06:17 | Badalgama (Maha Oya) | 3.09 | 🟢 Normal | 0.094 | 🔺 Rising |
| 2026-10-25 23:00:15 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-10-25 22:04:38 | Pitabeddara (Nilwala Ganga) | 1.80 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-10-25 23:01:45 | Moragaswewa (Deduru Oya) | 1.43 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-10-25 22:04:05 | Urawa (Nilwala Ganga) | 1.31 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-10-25 22:03:43 | Kithulgala (Kelani Ganga) | 2.41 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-10-25 23:01:09 | Ellagawa (Kalu Ganga) | 7.71 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-10-25 22:02:44 | Horowpothana (Yan Oya) | 2.15 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-10-25 22:06:45 | Baddegama (Gin Ganga) | 2.28 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-10-25 23:01:40 | Manampitiya (Mahaweli Ganga) | 0.45 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-10-25 22:08:26 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.55 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-10-25 22:07:26 | Putupaula (Kalu Ganga) | 1.57 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-25 22:05:25 | Panadugama (Nilwala Ganga) | 4.60 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-25 22:04:57 | Thanamalwila (Kirindi Oya) | 0.86 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-25 23:00:48 | Wellawaya (Kirindi Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-10-25 23:01:47 | Yaka Wewa (Ma Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-10-25 23:01:29 | Padiyathalawa (Maduru Oya) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-10-25 22:02:44 | Katharagama (Menik Ganga) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-10-25 18:02:16 | Thanthirimale (Malwathu Oya) | 1.54 | 🟢 Normal | 0.000 |  |
| 2026-10-25 23:02:48 | Thalgahagoda (Nilwala Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-10-25 23:01:25 | Kuda Oya (Kirindi Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-10-25 22:06:40 | Siyambalanduwa (Heda Oya) | 0.55 | 🟢 Normal | -0.010 |  |
| 2026-10-25 23:02:51 | Moraketiya (Walawe Ganga) | 1.19 | 🟢 Normal | -0.010 |  |
| 2026-10-25 22:05:44 | Nawalapitiya (Mahaweli Ganga) | 2.16 | 🟢 Normal | -0.020 |  |
| 2026-10-25 22:03:53 | Thawalama (Gin Ganga) | 3.15 | 🟢 Normal | -0.039 |  |
| 2026-10-25 23:01:32 | Peradeniya (Mahaweli Ganga) | 3.65 | 🟢 Normal | -0.054 |  |
| 2026-10-25 22:04:25 | Thaldena (Mahaweli Ganga) | 0.61 | 🟢 Normal | -0.063 |  |
| 2026-10-25 18:03:32 | Weraganthota (Mahaweli Ganga) | -3.24 | 🟢 Normal | -0.069 |  |
| 2026-10-25 23:02:21 | Nakkala (Kumbukkan Oya) | 1.62 | 🟢 Normal | -0.089 |  |
| 2026-10-25 22:08:40 | Holombuwa (Kelani Ganga) | 2.32 | 🟢 Normal | -0.178 |  |

## River Water Level Charts by Station

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)