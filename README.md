# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--20_05:29:07-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **265,754 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Nawalapitiya — Alert; 🟡 Magura — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **32** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-20 05:29:07 | Urawa (Nilwala Ganga) | 0.49 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-09-20 05:19:37 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-09-20 05:19:24 | Rathnapura (Kalu Ganga) | 1.70 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-09-20 05:19:02 | Holombuwa (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-09-20 05:12:56 | Pitabeddara (Nilwala Ganga) | 0.78 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-09-20 05:12:36 | Glencourse (Kelani Ganga) | 10.36 | 🟢 Normal | 0.000 |  |
| 2026-09-20 05:12:30 | Siyambalanduwa (Heda Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-09-20 05:10:49 | Panadugama (Nilwala Ganga) | 2.98 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2026-09-20 05:09:06 | Norwood (Kelani Ganga) | 0.71 | 🟢 Normal | 0.076 | 🔺 Rising |
| 2026-09-20 05:09:03 | Baddegama (Gin Ganga) | 2.22 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-09-20 05:07:45 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-09-20 05:07:26 | Thawalama (Gin Ganga) | 2.35 | 🟢 Normal | 0.309 | 🔺 Rising |
| 2026-09-20 05:06:57 | Dunamale (Aththanagalu Oya) | 1.60 | 🟢 Normal | 0.067 | 🔺 Rising |
| 2026-09-20 05:06:45 | Wellawaya (Kirindi Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-09-20 05:06:16 | Nawalapitiya (Mahaweli Ganga) | 3.60 | 🟡 Alert | 1.986 | 🔺 Rising |
| 2026-09-20 05:05:48 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-09-20 05:05:37 | Deraniyagala (Kelani Ganga) | 2.63 | 🟢 Normal | 1.636 | 🔺 Rising |
| 2026-09-20 05:05:33 | Badalgama (Maha Oya) | 1.86 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-09-20 05:05:17 | Ellagawa (Kalu Ganga) | 5.57 | 🟢 Normal | 0.095 | 🔺 Rising |
| 2026-09-20 05:04:41 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-09-20 05:04:33 | Thaldena (Mahaweli Ganga) | 0.28 | 🟢 Normal | -0.020 |  |
| 2026-09-20 05:04:30 | Hanwella (Kelani Ganga) | 1.85 | 🟢 Normal | 0.087 | 🔺 Rising |
| 2026-09-20 05:04:27 | Moraketiya (Walawe Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-09-20 05:03:29 | Moragaswewa (Deduru Oya) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-09-20 05:03:15 | Horowpothana (Yan Oya) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-09-20 05:02:53 | Horowpothana (Yan Oya) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-09-20 05:02:36 | Nakkala (Kumbukkan Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-09-20 05:02:32 | Thanamalwila (Kirindi Oya) | 1.06 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-20 05:02:22 | Manampitiya (Mahaweli Ganga) | -0.20 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-20 05:02:08 | Giriulla (Maha Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-09-20 05:01:46 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-20 05:00:57 | Peradeniya (Mahaweli Ganga) | 1.86 | 🟢 Normal | -0.203 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-20 05:06:16 | Nawalapitiya (Mahaweli Ganga) | 3.60 | 🟡 Alert | 1.986 | 🔺 Rising |
| 2026-09-20 05:00:52 | Magura (Kalu Ganga) | 4.10 | 🟡 Alert | 0.050 | 🔺 Rising |
| 2026-09-20 05:05:37 | Deraniyagala (Kelani Ganga) | 2.63 | 🟢 Normal | 1.636 | 🔺 Rising |
| 2026-09-20 05:07:26 | Thawalama (Gin Ganga) | 2.35 | 🟢 Normal | 0.309 | 🔺 Rising |
| 2026-09-20 04:05:03 | Kithulgala (Kelani Ganga) | 2.05 | 🟢 Normal | 0.175 | 🔺 Rising |
| 2026-09-20 05:05:17 | Ellagawa (Kalu Ganga) | 5.57 | 🟢 Normal | 0.095 | 🔺 Rising |
| 2026-09-20 05:04:30 | Hanwella (Kelani Ganga) | 1.85 | 🟢 Normal | 0.087 | 🔺 Rising |
| 2026-09-20 05:10:49 | Panadugama (Nilwala Ganga) | 2.98 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2026-09-20 05:09:06 | Norwood (Kelani Ganga) | 0.71 | 🟢 Normal | 0.076 | 🔺 Rising |
| 2026-09-20 05:06:57 | Dunamale (Aththanagalu Oya) | 1.60 | 🟢 Normal | 0.067 | 🔺 Rising |
| 2026-09-20 05:19:24 | Rathnapura (Kalu Ganga) | 1.70 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-09-20 05:29:07 | Urawa (Nilwala Ganga) | 0.49 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-09-20 05:09:03 | Baddegama (Gin Ganga) | 2.22 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-09-20 05:12:56 | Pitabeddara (Nilwala Ganga) | 0.78 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-09-20 04:56:57 | Putupaula (Kalu Ganga) | 0.93 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-09-20 05:02:22 | Manampitiya (Mahaweli Ganga) | -0.20 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-20 04:02:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.45 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-20 05:02:32 | Thanamalwila (Kirindi Oya) | 1.06 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-20 05:05:33 | Badalgama (Maha Oya) | 1.86 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-09-20 05:06:45 | Wellawaya (Kirindi Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-09-20 05:02:36 | Nakkala (Kumbukkan Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-09-20 05:03:29 | Moragaswewa (Deduru Oya) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-09-20 05:01:46 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-20 05:02:08 | Giriulla (Maha Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-09-20 05:03:15 | Horowpothana (Yan Oya) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-09-19 18:01:55 | Galgamuwa (Mee Oya) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-09-20 05:04:41 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-09-20 05:07:45 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-09-20 05:12:36 | Glencourse (Kelani Ganga) | 10.36 | 🟢 Normal | 0.000 |  |
| 2026-09-20 05:04:27 | Moraketiya (Walawe Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-09-20 05:12:30 | Siyambalanduwa (Heda Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-09-20 05:05:48 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-09-20 05:19:02 | Holombuwa (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-09-19 18:01:39 | Thanthirimale (Malwathu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-09-20 05:19:37 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-09-20 04:01:18 | Kuda Oya (Kirindi Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-09-19 18:01:44 | Weraganthota (Mahaweli Ganga) | -2.95 | 🟢 Normal | -0.010 |  |
| 2026-09-20 05:04:33 | Thaldena (Mahaweli Ganga) | 0.28 | 🟢 Normal | -0.020 |  |
| 2026-09-20 05:00:57 | Peradeniya (Mahaweli Ganga) | 1.86 | 🟢 Normal | -0.203 |  |

## River Water Level Charts by Station

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)