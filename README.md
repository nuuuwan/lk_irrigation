# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--27_03:03:06-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **326,683 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Dunamale — Alert; 🟡 Kalawellawa (Millakanda) — Alert; 🟡 Moraketiya — Alert; 🟡 Magura — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **7** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-27 03:03:06 | Nakkala (Kumbukkan Oya) | 1.48 | 🟢 Normal | -0.167 |  |
| 2026-11-27 03:02:20 | Manampitiya (Mahaweli Ganga) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-11-27 03:01:57 | Dunamale (Aththanagalu Oya) | 3.80 | 🟡 Alert | 0.188 | 🔺 Rising |
| 2026-11-27 03:01:47 | Giriulla (Maha Oya) | 4.54 | 🟢 Normal | -0.030 |  |
| 2026-11-27 03:01:23 | Moraketiya (Walawe Ganga) | 4.00 | 🟡 Alert | 0.000 |  |
| 2026-11-27 03:00:55 | Wellawaya (Kirindi Oya) | 1.75 | 🟢 Normal | -0.069 |  |
| 2026-11-27 02:49:13 | Dunamale (Aththanagalu Oya) | 3.76 | 🟡 Alert | 0.188 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-27 03:01:57 | Dunamale (Aththanagalu Oya) | 3.80 | 🟡 Alert | 0.188 | 🔺 Rising |
| 2026-11-27 02:01:59 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.20 | 🟡 Alert | 0.011 | 🔺 Rising |
| 2026-11-27 03:01:23 | Moraketiya (Walawe Ganga) | 4.00 | 🟡 Alert | 0.000 |  |
| 2026-11-27 01:05:59 | Magura (Kalu Ganga) | 5.00 | 🟡 Alert | -0.062 |  |
| 2026-11-27 02:09:53 | Badalgama (Maha Oya) | 4.64 | 🟢 Normal | 0.206 | 🔺 Rising |
| 2026-11-27 02:04:35 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | 0.155 | 🔺 Rising |
| 2026-11-27 02:07:45 | Katharagama (Menik Ganga) | 0.67 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2026-11-26 23:06:02 | Thawalama (Gin Ganga) | 2.88 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-11-27 00:05:59 | Panadugama (Nilwala Ganga) | 4.18 | 🟢 Normal | 0.086 | 🔺 Rising |
| 2026-11-27 01:01:39 | Ellagawa (Kalu Ganga) | 6.68 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2026-11-27 02:04:07 | Putupaula (Kalu Ganga) | 1.33 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-11-27 02:11:24 | Thaldena (Mahaweli Ganga) | 0.78 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-11-27 02:08:22 | Baddegama (Gin Ganga) | 1.73 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-11-27 02:05:11 | Nawalapitiya (Mahaweli Ganga) | 1.70 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-27 02:03:19 | Hanwella (Kelani Ganga) | 3.52 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-27 02:00:57 | Peradeniya (Mahaweli Ganga) | 3.78 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-11-27 01:04:51 | Thalgahagoda (Nilwala Ganga) | 0.75 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-11-26 18:00:24 | Weraganthota (Mahaweli Ganga) | -1.98 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-11-27 02:03:22 | Norwood (Kelani Ganga) | 1.23 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-11-27 02:05:49 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-11-27 00:02:54 | Yaka Wewa (Ma Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-11-27 01:05:35 | Horowpothana (Yan Oya) | 2.39 | 🟢 Normal | 0.000 |  |
| 2026-11-27 02:02:26 | Glencourse (Kelani Ganga) | 11.76 | 🟢 Normal | 0.000 |  |
| 2026-11-27 03:02:20 | Manampitiya (Mahaweli Ganga) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-11-26 18:02:07 | Thanthirimale (Malwathu Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-11-27 02:04:57 | Urawa (Nilwala Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-11-27 02:06:39 | Pitabeddara (Nilwala Ganga) | 2.20 | 🟢 Normal | -0.010 |  |
| 2026-11-26 18:01:55 | Galgamuwa (Mee Oya) | 1.18 | 🟢 Normal | -0.021 |  |
| 2026-11-27 02:06:42 | Siyambalanduwa (Heda Oya) | 2.52 | 🟢 Normal | -0.028 |  |
| 2026-11-27 02:03:57 | Moragaswewa (Deduru Oya) | 4.57 | 🟢 Normal | -0.029 |  |
| 2026-11-27 03:01:47 | Giriulla (Maha Oya) | 4.54 | 🟢 Normal | -0.030 |  |
| 2026-11-27 02:03:01 | Rathnapura (Kalu Ganga) | 3.24 | 🟢 Normal | -0.052 |  |
| 2026-11-27 02:12:57 | Deraniyagala (Kelani Ganga) | 0.81 | 🟢 Normal | -0.054 |  |
| 2026-11-27 01:00:20 | Padiyathalawa (Maduru Oya) | 1.45 | 🟢 Normal | -0.060 |  |
| 2026-11-27 03:00:55 | Wellawaya (Kirindi Oya) | 1.75 | 🟢 Normal | -0.069 |  |
| 2026-11-27 02:04:45 | Thanamalwila (Kirindi Oya) | 2.91 | 🟢 Normal | -0.112 |  |
| 2026-11-27 03:03:06 | Nakkala (Kumbukkan Oya) | 1.48 | 🟢 Normal | -0.167 |  |
| 2026-11-27 02:14:37 | Holombuwa (Kelani Ganga) | 1.66 | 🟢 Normal | -0.242 |  |
| 2026-11-27 02:07:00 | Kuda Oya (Kirindi Oya) | 2.97 | 🟢 Normal | -0.335 |  |

## River Water Level Charts by Station

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)