# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--26_04:03:47-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **298,109 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Magura — Alert; 🟡 Norwood — Alert; 🟡 Rathnapura — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **17** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-26 04:03:47 | Giriulla (Maha Oya) | 3.22 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-10-26 04:03:23 | Kithulgala (Kelani Ganga) | 2.32 | 🟢 Normal | 0.102 | 🔺 Rising |
| 2026-10-26 04:03:01 | Katharagama (Menik Ganga) | -0.19 | 🟢 Normal | 0.000 |  |
| 2026-10-26 04:02:46 | Yaka Wewa (Ma Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-10-26 04:02:43 | Manampitiya (Mahaweli Ganga) | 0.44 | 🟢 Normal | -0.062 |  |
| 2026-10-26 04:02:34 | Moragaswewa (Deduru Oya) | 2.96 | 🟢 Normal | 0.176 | 🔺 Rising |
| 2026-10-26 04:01:51 | Norwood (Kelani Ganga) | 1.54 | 🟡 Alert | 0.000 |  |
| 2026-10-26 04:01:48 | Kuda Oya (Kirindi Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-10-26 04:01:32 | Nakkala (Kumbukkan Oya) | 1.18 | 🟢 Normal | -0.052 |  |
| 2026-10-26 04:01:29 | Ellagawa (Kalu Ganga) | 8.07 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-10-26 04:01:15 | Thaldena (Mahaweli Ganga) | 0.45 | 🟢 Normal | -0.010 |  |
| 2026-10-26 04:01:08 | Moraketiya (Walawe Ganga) | 1.19 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-26 04:00:50 | Wellawaya (Kirindi Oya) | 1.13 | 🟢 Normal | -0.020 |  |
| 2026-10-26 04:00:42 | Magura (Kalu Ganga) | 4.08 | 🟡 Alert | 0.098 | 🔺 Rising |
| 2026-10-26 04:00:41 | Thalgahagoda (Nilwala Ganga) | 1.13 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-10-26 04:00:10 | Peradeniya (Mahaweli Ganga) | 3.66 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-10-26 03:23:33 | Peradeniya (Mahaweli Ganga) | 3.65 | 🟢 Normal | 0.016 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-26 04:00:42 | Magura (Kalu Ganga) | 4.08 | 🟡 Alert | 0.098 | 🔺 Rising |
| 2026-10-26 04:01:51 | Norwood (Kelani Ganga) | 1.54 | 🟡 Alert | 0.000 |  |
| 2026-10-26 03:05:53 | Rathnapura (Kalu Ganga) | 5.97 | 🟡 Alert | -0.082 |  |
| 2026-10-26 03:07:00 | Baddegama (Gin Ganga) | 2.52 | 🟢 Normal | 0.415 | 🔺 Rising |
| 2026-10-26 04:02:34 | Moragaswewa (Deduru Oya) | 2.96 | 🟢 Normal | 0.176 | 🔺 Rising |
| 2026-10-26 03:10:01 | Badalgama (Maha Oya) | 3.75 | 🟢 Normal | 0.129 | 🔺 Rising |
| 2026-10-26 03:09:38 | Hanwella (Kelani Ganga) | 3.94 | 🟢 Normal | 0.128 | 🔺 Rising |
| 2026-10-25 18:03:46 | Galgamuwa (Mee Oya) | 1.82 | 🟢 Normal | 0.121 | 🔺 Rising |
| 2026-10-26 04:03:23 | Kithulgala (Kelani Ganga) | 2.32 | 🟢 Normal | 0.102 | 🔺 Rising |
| 2026-10-26 03:03:22 | Glencourse (Kelani Ganga) | 12.47 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-10-26 04:03:47 | Giriulla (Maha Oya) | 3.22 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-10-26 03:02:23 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.65 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-10-26 04:01:29 | Ellagawa (Kalu Ganga) | 8.07 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-10-26 03:03:53 | Panadugama (Nilwala Ganga) | 4.74 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-10-26 04:00:41 | Thalgahagoda (Nilwala Ganga) | 1.13 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-10-26 03:14:13 | Nagalagam Street (Kelani Ganga) | 0.79 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-10-26 03:13:39 | Thawalama (Gin Ganga) | 3.27 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-10-26 04:00:10 | Peradeniya (Mahaweli Ganga) | 3.66 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-10-26 03:05:50 | Putupaula (Kalu Ganga) | 1.67 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-10-26 03:02:42 | Horowpothana (Yan Oya) | 2.33 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-26 04:01:08 | Moraketiya (Walawe Ganga) | 1.19 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-26 04:02:46 | Yaka Wewa (Ma Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-10-26 03:03:33 | Pitabeddara (Nilwala Ganga) | 1.90 | 🟢 Normal | 0.000 |  |
| 2026-10-26 03:04:31 | Siyambalanduwa (Heda Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-10-26 03:01:40 | Dunamale (Aththanagalu Oya) | 3.10 | 🟢 Normal | 0.000 |  |
| 2026-10-26 04:03:01 | Katharagama (Menik Ganga) | -0.19 | 🟢 Normal | 0.000 |  |
| 2026-10-25 18:02:16 | Thanthirimale (Malwathu Oya) | 1.54 | 🟢 Normal | 0.000 |  |
| 2026-10-26 04:01:48 | Kuda Oya (Kirindi Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-10-26 03:10:52 | Thanamalwila (Kirindi Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-10-26 03:06:52 | Padiyathalawa (Maduru Oya) | 0.25 | 🟢 Normal | -0.003 |  |
| 2026-10-26 04:01:15 | Thaldena (Mahaweli Ganga) | 0.45 | 🟢 Normal | -0.010 |  |
| 2026-10-26 04:00:50 | Wellawaya (Kirindi Oya) | 1.13 | 🟢 Normal | -0.020 |  |
| 2026-10-26 04:01:32 | Nakkala (Kumbukkan Oya) | 1.18 | 🟢 Normal | -0.052 |  |
| 2026-10-26 04:02:43 | Manampitiya (Mahaweli Ganga) | 0.44 | 🟢 Normal | -0.062 |  |
| 2026-10-25 18:03:32 | Weraganthota (Mahaweli Ganga) | -3.24 | 🟢 Normal | -0.069 |  |
| 2026-10-26 03:02:45 | Nawalapitiya (Mahaweli Ganga) | 1.91 | 🟢 Normal | -0.071 |  |
| 2026-10-26 03:05:37 | Deraniyagala (Kelani Ganga) | 1.47 | 🟢 Normal | -0.099 |  |
| 2026-10-26 03:09:11 | Holombuwa (Kelani Ganga) | 1.50 | 🟢 Normal | -0.152 |  |
| 2026-10-26 03:06:27 | Urawa (Nilwala Ganga) | 1.27 | 🟢 Normal | -7.579 |  |

## River Water Level Charts by Station

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)