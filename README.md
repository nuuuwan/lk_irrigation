# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--27_00:03:25-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **326,597 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Magura — Alert; 🟡 Dunamale — Alert; 🟡 Kalawellawa (Millakanda) — Alert; 🟡 Moraketiya — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **12** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-27 00:03:25 | Ellagawa (Kalu Ganga) | 6.60 | 🟢 Normal | 0.129 | 🔺 Rising |
| 2026-11-27 00:03:25 | Dunamale (Aththanagalu Oya) | 3.64 | 🟡 Alert | 0.030 | 🔺 Rising |
| 2026-11-27 00:03:24 | Kuda Oya (Kirindi Oya) | 3.53 | 🟢 Normal | -0.271 |  |
| 2026-11-27 00:03:19 | Baddegama (Gin Ganga) | 1.66 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-11-27 00:03:01 | Norwood (Kelani Ganga) | 1.20 | 🟢 Normal | -0.022 |  |
| 2026-11-27 00:02:54 | Yaka Wewa (Ma Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-11-27 00:02:48 | Manampitiya (Mahaweli Ganga) | 1.49 | 🟢 Normal | -0.050 |  |
| 2026-11-27 00:02:41 | Nakkala (Kumbukkan Oya) | 1.95 | 🟢 Normal | -0.156 |  |
| 2026-11-27 00:02:09 | Thaldena (Mahaweli Ganga) | 0.80 | 🟢 Normal | -0.053 |  |
| 2026-11-27 00:01:24 | Horowpothana (Yan Oya) | 2.39 | 🟢 Normal | 0.000 |  |
| 2026-11-27 00:00:35 | Padiyathalawa (Maduru Oya) | 1.51 | 🟢 Normal | -0.641 |  |
| 2026-11-27 00:00:06 | Thalgahagoda (Nilwala Ganga) | 0.73 | 🟢 Normal | -0.022 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-26 20:03:05 | Magura (Kalu Ganga) | 4.55 | 🟡 Alert | 0.271 | 🔺 Rising |
| 2026-11-27 00:03:25 | Dunamale (Aththanagalu Oya) | 3.64 | 🟡 Alert | 0.030 | 🔺 Rising |
| 2026-11-26 22:02:44 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.18 | 🟡 Alert | 0.023 | 🔺 Rising |
| 2026-11-26 23:07:32 | Moraketiya (Walawe Ganga) | 4.10 | 🟡 Alert | -0.160 |  |
| 2026-11-26 23:06:45 | Giriulla (Maha Oya) | 4.32 | 🟢 Normal | 0.222 | 🔺 Rising |
| 2026-11-26 23:03:11 | Panadugama (Nilwala Ganga) | 4.09 | 🟢 Normal | 0.211 | 🔺 Rising |
| 2026-11-26 23:05:14 | Peradeniya (Mahaweli Ganga) | 3.86 | 🟢 Normal | 0.201 | 🔺 Rising |
| 2026-11-26 23:05:59 | Glencourse (Kelani Ganga) | 11.60 | 🟢 Normal | 0.150 | 🔺 Rising |
| 2026-11-27 00:03:25 | Ellagawa (Kalu Ganga) | 6.60 | 🟢 Normal | 0.129 | 🔺 Rising |
| 2026-11-26 23:02:11 | Siyambalanduwa (Heda Oya) | 1.75 | 🟢 Normal | 0.101 | 🔺 Rising |
| 2026-11-26 23:02:43 | Katharagama (Menik Ganga) | 0.15 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-11-26 23:06:02 | Thawalama (Gin Ganga) | 2.88 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-11-27 00:03:19 | Baddegama (Gin Ganga) | 1.66 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-11-26 23:02:37 | Hanwella (Kelani Ganga) | 3.41 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-26 23:02:30 | Pitabeddara (Nilwala Ganga) | 2.22 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-11-26 18:00:24 | Weraganthota (Mahaweli Ganga) | -1.98 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-11-26 23:02:58 | Kithulgala (Kelani Ganga) | 1.85 | 🟢 Normal | 0.000 |  |
| 2026-11-27 00:02:54 | Yaka Wewa (Ma Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-11-27 00:01:24 | Horowpothana (Yan Oya) | 2.39 | 🟢 Normal | 0.000 |  |
| 2026-11-26 22:03:58 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-11-26 18:02:07 | Thanthirimale (Malwathu Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-11-26 23:04:13 | Urawa (Nilwala Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-11-26 23:06:56 | Nawalapitiya (Mahaweli Ganga) | 1.54 | 🟢 Normal | -0.010 |  |
| 2026-11-26 23:01:48 | Moragaswewa (Deduru Oya) | 4.65 | 🟢 Normal | -0.011 |  |
| 2026-11-26 23:02:30 | Wellawaya (Kirindi Oya) | 1.96 | 🟢 Normal | -0.020 |  |
| 2026-11-26 23:02:15 | Putupaula (Kalu Ganga) | 1.28 | 🟢 Normal | -0.020 |  |
| 2026-11-26 18:01:55 | Galgamuwa (Mee Oya) | 1.18 | 🟢 Normal | -0.021 |  |
| 2026-11-27 00:00:06 | Thalgahagoda (Nilwala Ganga) | 0.73 | 🟢 Normal | -0.022 |  |
| 2026-11-27 00:03:01 | Norwood (Kelani Ganga) | 1.20 | 🟢 Normal | -0.022 |  |
| 2026-11-26 23:05:26 | Badalgama (Maha Oya) | 3.68 | 🟢 Normal | -0.031 |  |
| 2026-11-27 00:02:48 | Manampitiya (Mahaweli Ganga) | 1.49 | 🟢 Normal | -0.050 |  |
| 2026-11-27 00:02:09 | Thaldena (Mahaweli Ganga) | 0.80 | 🟢 Normal | -0.053 |  |
| 2026-11-26 23:04:07 | Deraniyagala (Kelani Ganga) | 1.04 | 🟢 Normal | -0.066 |  |
| 2026-11-26 23:07:19 | Rathnapura (Kalu Ganga) | 3.49 | 🟢 Normal | -0.100 |  |
| 2026-11-26 23:05:58 | Thanamalwila (Kirindi Oya) | 3.41 | 🟢 Normal | -0.108 |  |
| 2026-11-27 00:02:41 | Nakkala (Kumbukkan Oya) | 1.95 | 🟢 Normal | -0.156 |  |
| 2026-11-27 00:03:24 | Kuda Oya (Kirindi Oya) | 3.53 | 🟢 Normal | -0.271 |  |
| 2026-11-26 23:08:38 | Holombuwa (Kelani Ganga) | 2.43 | 🟢 Normal | -0.313 |  |
| 2026-11-27 00:00:35 | Padiyathalawa (Maduru Oya) | 1.51 | 🟢 Normal | -0.641 |  |

## River Water Level Charts by Station

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)