# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--27_09:03:57-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **326,921 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Kalawellawa (Millakanda) — Alert; 🟡 Dunamale — Alert; 🟡 Magura — Alert; 🟡 Moraketiya — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **20** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-27 09:03:57 | Katharagama (Menik Ganga) | 0.36 | 🟢 Normal | -0.020 |  |
| 2026-11-27 09:03:49 | Manampitiya (Mahaweli Ganga) | 2.13 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2026-11-27 09:03:33 | Thawalama (Gin Ganga) | 2.51 | 🟢 Normal | -0.127 |  |
| 2026-11-27 09:03:25 | Pitabeddara (Nilwala Ganga) | 1.51 | 🟢 Normal | -0.126 |  |
| 2026-11-27 09:03:21 | Thanthirimale (Malwathu Oya) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-11-27 09:03:18 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.32 | 🟡 Alert | 0.010 | 🔺 Rising |
| 2026-11-27 09:03:18 | Siyambalanduwa (Heda Oya) | 1.39 | 🟢 Normal | -0.088 |  |
| 2026-11-27 09:02:57 | Deraniyagala (Kelani Ganga) | 0.76 | 🟢 Normal | -0.010 |  |
| 2026-11-27 09:02:55 | Horowpothana (Yan Oya) | 2.39 | 🟢 Normal | 0.000 |  |
| 2026-11-27 09:02:55 | Putupaula (Kalu Ganga) | 1.55 | 🟢 Normal | -0.010 |  |
| 2026-11-27 09:02:22 | Moragaswewa (Deduru Oya) | 3.48 | 🟢 Normal | -0.021 |  |
| 2026-11-27 09:02:19 | Thanamalwila (Kirindi Oya) | 2.45 | 🟢 Normal | -0.040 |  |
| 2026-11-27 09:01:58 | Dunamale (Aththanagalu Oya) | 3.98 | 🟡 Alert | 0.000 |  |
| 2026-11-27 09:01:55 | Wellawaya (Kirindi Oya) | 1.63 | 🟢 Normal | -0.020 |  |
| 2026-11-27 09:01:20 | Ellagawa (Kalu Ganga) | 6.76 | 🟢 Normal | -0.021 |  |
| 2026-11-27 09:01:19 | Magura (Kalu Ganga) | 4.49 | 🟡 Alert | -0.089 |  |
| 2026-11-27 09:01:02 | Weraganthota (Mahaweli Ganga) | -1.79 | 🟢 Normal | -0.030 |  |
| 2026-11-27 09:01:01 | Nawalapitiya (Mahaweli Ganga) | 1.46 | 🟢 Normal | -0.010 |  |
| 2026-11-27 09:00:23 | Kuda Oya (Kirindi Oya) | 2.66 | 🟢 Normal | -0.052 |  |
| 2026-11-27 09:00:10 | Nakkala (Kumbukkan Oya) | 1.44 | 🟢 Normal | -0.060 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-27 09:03:18 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.32 | 🟡 Alert | 0.010 | 🔺 Rising |
| 2026-11-27 09:01:58 | Dunamale (Aththanagalu Oya) | 3.98 | 🟡 Alert | 0.000 |  |
| 2026-11-27 09:01:19 | Magura (Kalu Ganga) | 4.49 | 🟡 Alert | -0.089 |  |
| 2026-11-27 08:01:51 | Moraketiya (Walawe Ganga) | 3.80 | 🟡 Alert | -0.197 |  |
| 2026-11-27 09:03:49 | Manampitiya (Mahaweli Ganga) | 2.13 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2026-11-27 08:09:41 | Urawa (Nilwala Ganga) | 0.92 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-11-27 08:07:08 | Baddegama (Gin Ganga) | 2.06 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-11-27 08:20:47 | Thalgahagoda (Nilwala Ganga) | 0.92 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-11-27 08:15:39 | Yaka Wewa (Ma Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-11-27 09:02:55 | Horowpothana (Yan Oya) | 2.39 | 🟢 Normal | 0.000 |  |
| 2026-11-27 09:03:21 | Thanthirimale (Malwathu Oya) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-11-27 08:03:49 | Galgamuwa (Mee Oya) | 0.98 | 🟢 Normal | -0.010 |  |
| 2026-11-27 08:08:02 | Badalgama (Maha Oya) | 4.97 | 🟢 Normal | -0.010 |  |
| 2026-11-27 09:02:57 | Deraniyagala (Kelani Ganga) | 0.76 | 🟢 Normal | -0.010 |  |
| 2026-11-27 09:02:55 | Putupaula (Kalu Ganga) | 1.55 | 🟢 Normal | -0.010 |  |
| 2026-11-27 08:02:14 | Norwood (Kelani Ganga) | 1.09 | 🟢 Normal | -0.010 |  |
| 2026-11-27 09:01:01 | Nawalapitiya (Mahaweli Ganga) | 1.46 | 🟢 Normal | -0.010 |  |
| 2026-11-27 08:10:28 | Padiyathalawa (Maduru Oya) | 0.98 | 🟢 Normal | -0.018 |  |
| 2026-11-27 09:03:57 | Katharagama (Menik Ganga) | 0.36 | 🟢 Normal | -0.020 |  |
| 2026-11-27 09:01:55 | Wellawaya (Kirindi Oya) | 1.63 | 🟢 Normal | -0.020 |  |
| 2026-11-27 09:01:20 | Ellagawa (Kalu Ganga) | 6.76 | 🟢 Normal | -0.021 |  |
| 2026-11-27 08:07:39 | Thaldena (Mahaweli Ganga) | 0.68 | 🟢 Normal | -0.021 |  |
| 2026-11-27 09:02:22 | Moragaswewa (Deduru Oya) | 3.48 | 🟢 Normal | -0.021 |  |
| 2026-11-27 08:07:27 | Panadugama (Nilwala Ganga) | 4.38 | 🟢 Normal | -0.027 |  |
| 2026-11-27 09:01:02 | Weraganthota (Mahaweli Ganga) | -1.79 | 🟢 Normal | -0.030 |  |
| 2026-11-27 09:02:19 | Thanamalwila (Kirindi Oya) | 2.45 | 🟢 Normal | -0.040 |  |
| 2026-11-27 08:06:47 | Glencourse (Kelani Ganga) | 11.18 | 🟢 Normal | -0.048 |  |
| 2026-11-27 08:03:16 | Hanwella (Kelani Ganga) | 3.54 | 🟢 Normal | -0.052 |  |
| 2026-11-27 09:00:23 | Kuda Oya (Kirindi Oya) | 2.66 | 🟢 Normal | -0.052 |  |
| 2026-11-27 08:05:55 | Rathnapura (Kalu Ganga) | 2.95 | 🟢 Normal | -0.052 |  |
| 2026-11-27 09:00:10 | Nakkala (Kumbukkan Oya) | 1.44 | 🟢 Normal | -0.060 |  |
| 2026-11-27 08:07:14 | Holombuwa (Kelani Ganga) | 1.68 | 🟢 Normal | -0.079 |  |
| 2026-11-27 09:03:18 | Siyambalanduwa (Heda Oya) | 1.39 | 🟢 Normal | -0.088 |  |
| 2026-11-27 08:02:31 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.122 |  |
| 2026-11-27 08:09:20 | Giriulla (Maha Oya) | 4.13 | 🟢 Normal | -0.122 |  |
| 2026-11-27 09:03:25 | Pitabeddara (Nilwala Ganga) | 1.51 | 🟢 Normal | -0.126 |  |
| 2026-11-27 09:03:33 | Thawalama (Gin Ganga) | 2.51 | 🟢 Normal | -0.127 |  |
| 2026-11-27 08:07:04 | Peradeniya (Mahaweli Ganga) | 4.00 | 🟢 Normal | -0.191 |  |
| 2026-11-27 08:02:03 | Kithulgala (Kelani Ganga) | 1.62 | 🟢 Normal | -0.405 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)