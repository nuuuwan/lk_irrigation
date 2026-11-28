# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--28_09:03:00-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **327,811 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Kalawellawa (Millakanda) — Alert; 🟡 Moraketiya — Alert; 🟡 Dunamale — Alert; 🟡 Panadugama — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **20** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-28 09:03:00 | Thanthirimale (Malwathu Oya) | 1.42 | 🟢 Normal | -0.024 |  |
| 2026-11-28 09:02:42 | Ellagawa (Kalu Ganga) | 7.26 | 🟢 Normal | -0.060 |  |
| 2026-11-28 09:02:39 | Hanwella (Kelani Ganga) | 4.00 | 🟢 Normal | -0.082 |  |
| 2026-11-28 09:02:30 | Thawalama (Gin Ganga) | 2.35 | 🟢 Normal | -0.113 |  |
| 2026-11-28 09:02:29 | Nawalapitiya (Mahaweli Ganga) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-11-28 09:02:26 | Moragaswewa (Deduru Oya) | 2.30 | 🟢 Normal | -0.020 |  |
| 2026-11-28 09:02:17 | Thanamalwila (Kirindi Oya) | 2.20 | 🟢 Normal | -0.030 |  |
| 2026-11-28 09:02:11 | Dunamale (Aththanagalu Oya) | 3.99 | 🟡 Alert | 0.000 |  |
| 2026-11-28 09:02:10 | Giriulla (Maha Oya) | 2.93 | 🟢 Normal | -0.032 |  |
| 2026-11-28 09:02:06 | Peradeniya (Mahaweli Ganga) | 2.88 | 🟢 Normal | -0.022 |  |
| 2026-11-28 09:01:41 | Glencourse (Kelani Ganga) | 11.67 | 🟢 Normal | -0.162 |  |
| 2026-11-28 09:01:39 | Baddegama (Gin Ganga) | 2.05 | 🟢 Normal | -0.010 |  |
| 2026-11-28 09:01:11 | Nakkala (Kumbukkan Oya) | 1.02 | 🟢 Normal | -0.010 |  |
| 2026-11-28 09:00:43 | Thaldena (Mahaweli Ganga) | 0.70 | 🟢 Normal | -0.010 |  |
| 2026-11-28 09:00:34 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-11-28 09:00:25 | Thalgahagoda (Nilwala Ganga) | 1.21 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-11-28 09:00:20 | Kuda Oya (Kirindi Oya) | 2.51 | 🟢 Normal | -0.031 |  |
| 2026-11-28 09:00:11 | Siyambalanduwa (Heda Oya) | 0.89 | 🟢 Normal | -0.053 |  |
| 2026-11-28 08:32:01 | Urawa (Nilwala Ganga) | 1.13 | 🟢 Normal | -0.055 |  |
| 2026-11-28 08:22:58 | Horowpothana (Yan Oya) | 2.37 | 🟢 Normal | -0.007 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-28 08:03:32 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.20 | 🟡 Alert | 0.052 | 🔺 Rising |
| 2026-11-28 08:05:44 | Moraketiya (Walawe Ganga) | 3.20 | 🟡 Alert | 0.000 |  |
| 2026-11-28 09:02:11 | Dunamale (Aththanagalu Oya) | 3.99 | 🟡 Alert | 0.000 |  |
| 2026-11-28 08:19:28 | Panadugama (Nilwala Ganga) | 5.52 | 🟡 Alert | -0.029 |  |
| 2026-11-28 08:09:10 | Manampitiya (Mahaweli Ganga) | 1.90 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-11-28 08:04:45 | Putupaula (Kalu Ganga) | 1.76 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-11-28 07:00:16 | Weraganthota (Mahaweli Ganga) | -1.32 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-11-28 09:00:25 | Thalgahagoda (Nilwala Ganga) | 1.21 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-11-28 09:02:29 | Nawalapitiya (Mahaweli Ganga) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-11-28 09:00:34 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-11-28 08:05:20 | Norwood (Kelani Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-11-28 08:04:21 | Padiyathalawa (Maduru Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-11-28 08:22:58 | Horowpothana (Yan Oya) | 2.37 | 🟢 Normal | -0.007 |  |
| 2026-11-28 08:09:56 | Katharagama (Menik Ganga) | 0.14 | 🟢 Normal | -0.010 |  |
| 2026-11-28 09:01:11 | Nakkala (Kumbukkan Oya) | 1.02 | 🟢 Normal | -0.010 |  |
| 2026-11-28 09:00:43 | Thaldena (Mahaweli Ganga) | 0.70 | 🟢 Normal | -0.010 |  |
| 2026-11-28 09:01:39 | Baddegama (Gin Ganga) | 2.05 | 🟢 Normal | -0.010 |  |
| 2026-11-28 09:02:26 | Moragaswewa (Deduru Oya) | 2.30 | 🟢 Normal | -0.020 |  |
| 2026-11-28 08:02:18 | Deraniyagala (Kelani Ganga) | 0.81 | 🟢 Normal | -0.020 |  |
| 2026-11-28 09:02:06 | Peradeniya (Mahaweli Ganga) | 2.88 | 🟢 Normal | -0.022 |  |
| 2026-11-28 09:03:00 | Thanthirimale (Malwathu Oya) | 1.42 | 🟢 Normal | -0.024 |  |
| 2026-11-28 09:02:17 | Thanamalwila (Kirindi Oya) | 2.20 | 🟢 Normal | -0.030 |  |
| 2026-11-28 08:01:47 | Wellawaya (Kirindi Oya) | 1.55 | 🟢 Normal | -0.031 |  |
| 2026-11-28 09:00:20 | Kuda Oya (Kirindi Oya) | 2.51 | 🟢 Normal | -0.031 |  |
| 2026-11-28 09:02:10 | Giriulla (Maha Oya) | 2.93 | 🟢 Normal | -0.032 |  |
| 2026-11-28 09:00:11 | Siyambalanduwa (Heda Oya) | 0.89 | 🟢 Normal | -0.053 |  |
| 2026-11-28 08:32:01 | Urawa (Nilwala Ganga) | 1.13 | 🟢 Normal | -0.055 |  |
| 2026-11-28 09:02:42 | Ellagawa (Kalu Ganga) | 7.26 | 🟢 Normal | -0.060 |  |
| 2026-11-28 08:08:34 | Galgamuwa (Mee Oya) | 0.67 | 🟢 Normal | -0.062 |  |
| 2026-11-28 08:05:34 | Magura (Kalu Ganga) | 3.79 | 🟢 Normal | -0.067 |  |
| 2026-11-28 08:02:41 | Pitabeddara (Nilwala Ganga) | 2.45 | 🟢 Normal | -0.067 |  |
| 2026-11-28 08:11:38 | Badalgama (Maha Oya) | 4.12 | 🟢 Normal | -0.076 |  |
| 2026-11-28 09:02:39 | Hanwella (Kelani Ganga) | 4.00 | 🟢 Normal | -0.082 |  |
| 2026-11-28 08:03:57 | Rathnapura (Kalu Ganga) | 2.66 | 🟢 Normal | -0.093 |  |
| 2026-11-28 09:02:30 | Thawalama (Gin Ganga) | 2.35 | 🟢 Normal | -0.113 |  |
| 2026-11-28 08:06:57 | Holombuwa (Kelani Ganga) | 1.45 | 🟢 Normal | -0.124 |  |
| 2026-11-28 08:09:48 | Nagalagam Street (Kelani Ganga) | 0.59 | 🟢 Normal | -0.131 |  |
| 2026-11-28 09:01:41 | Glencourse (Kelani Ganga) | 11.67 | 🟢 Normal | -0.162 |  |
| 2026-11-28 08:03:12 | Kithulgala (Kelani Ganga) | 1.47 | 🟢 Normal | -0.488 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)