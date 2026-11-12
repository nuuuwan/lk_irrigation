# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--12_18:13:33-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **314,023 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Panadugama — Minor Flood; 🟠 Baddegama — Minor Flood; 🟠 Thalgahagoda — Minor Flood; 🟡 Dunamale — Alert; 🟡 Kalawellawa (Millakanda) — Alert…
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-12 18:13:33 | Padiyathalawa (Maduru Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-11-12 18:09:04 | Panadugama (Nilwala Ganga) | 6.16 | 🟠 Minor Flood | 0.115 | 🔺 Rising |
| 2026-11-12 18:08:45 | Holombuwa (Kelani Ganga) | 1.51 | 🟢 Normal | 0.000 |  |
| 2026-11-12 18:08:42 | Katharagama (Menik Ganga) | 0.50 | 🟢 Normal | -0.029 |  |
| 2026-11-12 18:08:38 | Baddegama (Gin Ganga) | 4.13 | 🟠 Minor Flood | 0.010 | 🔺 Rising |
| 2026-11-12 18:07:18 | Urawa (Nilwala Ganga) | 1.68 | 🟢 Normal | 0.146 | 🔺 Rising |
| 2026-11-12 18:06:48 | Galgamuwa (Mee Oya) | 0.72 | 🟢 Normal | -0.009 |  |
| 2026-11-12 18:05:59 | Pitabeddara (Nilwala Ganga) | 3.46 | 🟢 Normal | 0.244 | 🔺 Rising |
| 2026-11-12 18:05:33 | Thalgahagoda (Nilwala Ganga) | 1.82 | 🟠 Minor Flood | 0.000 |  |
| 2026-11-12 18:05:19 | Nagalagam Street (Kelani Ganga) | 0.82 | 🟢 Normal | -0.058 |  |
| 2026-11-12 18:05:04 | Badalgama (Maha Oya) | 3.94 | 🟢 Normal | -0.041 |  |
| 2026-11-12 18:04:25 | Thanamalwila (Kirindi Oya) | 2.52 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-12 18:03:58 | Norwood (Kelani Ganga) | 1.47 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-11-12 18:03:52 | Ellagawa (Kalu Ganga) | 8.29 | 🟢 Normal | -0.020 |  |
| 2026-11-12 18:03:51 | Hanwella (Kelani Ganga) | 4.86 | 🟢 Normal | -0.098 |  |
| 2026-11-12 18:03:43 | Moragaswewa (Deduru Oya) | 2.58 | 🟢 Normal | -0.289 |  |
| 2026-11-12 18:03:31 | Wellawaya (Kirindi Oya) | 2.22 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-11-12 18:03:31 | Dunamale (Aththanagalu Oya) | 4.06 | 🟡 Alert | 0.000 |  |
| 2026-11-12 18:03:30 | Glencourse (Kelani Ganga) | 12.10 | 🟢 Normal | -0.111 |  |
| 2026-11-12 18:03:19 | Kithulgala (Kelani Ganga) | 2.15 | 🟢 Normal | 0.000 |  |
| 2026-11-12 18:03:08 | Deraniyagala (Kelani Ganga) | 1.27 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-12 18:02:46 | Magura (Kalu Ganga) | 4.95 | 🟡 Alert | -0.046 |  |
| 2026-11-12 18:02:34 | Giriulla (Maha Oya) | 2.46 | 🟢 Normal | -0.039 |  |
| 2026-11-12 18:02:28 | Yaka Wewa (Ma Oya) | 0.73 | 🟢 Normal | -0.010 |  |
| 2026-11-12 18:02:19 | Manampitiya (Mahaweli Ganga) | 2.17 | 🟢 Normal | 0.000 |  |
| 2026-11-12 18:02:15 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.32 | 🟡 Alert | 0.000 |  |
| 2026-11-12 18:02:14 | Moraketiya (Walawe Ganga) | 3.65 | 🟡 Alert | -0.106 |  |
| 2026-11-12 18:01:57 | Thaldena (Mahaweli Ganga) | 2.67 | 🟢 Normal | -0.115 |  |
| 2026-11-12 18:01:57 | Rathnapura (Kalu Ganga) | 5.02 | 🟢 Normal | -0.032 |  |
| 2026-11-12 18:01:56 | Nawalapitiya (Mahaweli Ganga) | 1.63 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-12 18:01:47 | Kuda Oya (Kirindi Oya) | 3.00 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-11-12 18:01:32 | Peradeniya (Mahaweli Ganga) | 4.72 | 🟢 Normal | 0.096 | 🔺 Rising |
| 2026-11-12 18:01:24 | Thawalama (Gin Ganga) | 3.45 | 🟢 Normal | 0.151 | 🔺 Rising |
| 2026-11-12 18:01:04 | Thanthirimale (Malwathu Oya) | 2.02 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-12 18:00:56 | Nakkala (Kumbukkan Oya) | 1.45 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-12 18:00:44 | Siyambalanduwa (Heda Oya) | 1.15 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-11-12 18:00:35 | Weraganthota (Mahaweli Ganga) | -1.97 | 🟢 Normal | 0.130 | 🔺 Rising |
| 2026-11-12 18:00:12 | Horowpothana (Yan Oya) | 2.51 | 🟢 Normal | 0.000 |  |
| 2026-11-12 18:00:09 | Putupaula (Kalu Ganga) | 2.52 | 🟢 Normal | 0.000 |  |
| 2026-11-12 17:58:32 | Dunamale (Aththanagalu Oya) | 4.06 | 🟡 Alert | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-12 18:09:04 | Panadugama (Nilwala Ganga) | 6.16 | 🟠 Minor Flood | 0.115 | 🔺 Rising |
| 2026-11-12 18:08:38 | Baddegama (Gin Ganga) | 4.13 | 🟠 Minor Flood | 0.010 | 🔺 Rising |
| 2026-11-12 18:05:33 | Thalgahagoda (Nilwala Ganga) | 1.82 | 🟠 Minor Flood | 0.000 |  |
| 2026-11-12 18:03:31 | Dunamale (Aththanagalu Oya) | 4.06 | 🟡 Alert | 0.000 |  |
| 2026-11-12 18:02:15 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.32 | 🟡 Alert | 0.000 |  |
| 2026-11-12 18:02:46 | Magura (Kalu Ganga) | 4.95 | 🟡 Alert | -0.046 |  |
| 2026-11-12 18:02:14 | Moraketiya (Walawe Ganga) | 3.65 | 🟡 Alert | -0.106 |  |
| 2026-11-12 18:05:59 | Pitabeddara (Nilwala Ganga) | 3.46 | 🟢 Normal | 0.244 | 🔺 Rising |
| 2026-11-12 18:01:24 | Thawalama (Gin Ganga) | 3.45 | 🟢 Normal | 0.151 | 🔺 Rising |
| 2026-11-12 18:07:18 | Urawa (Nilwala Ganga) | 1.68 | 🟢 Normal | 0.146 | 🔺 Rising |
| 2026-11-12 18:00:35 | Weraganthota (Mahaweli Ganga) | -1.97 | 🟢 Normal | 0.130 | 🔺 Rising |
| 2026-11-12 18:01:32 | Peradeniya (Mahaweli Ganga) | 4.72 | 🟢 Normal | 0.096 | 🔺 Rising |
| 2026-11-12 18:03:31 | Wellawaya (Kirindi Oya) | 2.22 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-11-12 18:03:58 | Norwood (Kelani Ganga) | 1.47 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-11-12 18:01:47 | Kuda Oya (Kirindi Oya) | 3.00 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-11-12 18:00:44 | Siyambalanduwa (Heda Oya) | 1.15 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-11-12 18:04:25 | Thanamalwila (Kirindi Oya) | 2.52 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-12 18:03:08 | Deraniyagala (Kelani Ganga) | 1.27 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-12 18:01:04 | Thanthirimale (Malwathu Oya) | 2.02 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-12 18:01:56 | Nawalapitiya (Mahaweli Ganga) | 1.63 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-12 18:00:56 | Nakkala (Kumbukkan Oya) | 1.45 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-12 18:03:19 | Kithulgala (Kelani Ganga) | 2.15 | 🟢 Normal | 0.000 |  |
| 2026-11-12 18:00:12 | Horowpothana (Yan Oya) | 2.51 | 🟢 Normal | 0.000 |  |
| 2026-11-12 18:13:33 | Padiyathalawa (Maduru Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-11-12 18:00:09 | Putupaula (Kalu Ganga) | 2.52 | 🟢 Normal | 0.000 |  |
| 2026-11-12 18:08:45 | Holombuwa (Kelani Ganga) | 1.51 | 🟢 Normal | 0.000 |  |
| 2026-11-12 18:02:19 | Manampitiya (Mahaweli Ganga) | 2.17 | 🟢 Normal | 0.000 |  |
| 2026-11-12 18:06:48 | Galgamuwa (Mee Oya) | 0.72 | 🟢 Normal | -0.009 |  |
| 2026-11-12 18:02:28 | Yaka Wewa (Ma Oya) | 0.73 | 🟢 Normal | -0.010 |  |
| 2026-11-12 18:03:52 | Ellagawa (Kalu Ganga) | 8.29 | 🟢 Normal | -0.020 |  |
| 2026-11-12 18:08:42 | Katharagama (Menik Ganga) | 0.50 | 🟢 Normal | -0.029 |  |
| 2026-11-12 18:01:57 | Rathnapura (Kalu Ganga) | 5.02 | 🟢 Normal | -0.032 |  |
| 2026-11-12 18:02:34 | Giriulla (Maha Oya) | 2.46 | 🟢 Normal | -0.039 |  |
| 2026-11-12 18:05:04 | Badalgama (Maha Oya) | 3.94 | 🟢 Normal | -0.041 |  |
| 2026-11-12 18:05:19 | Nagalagam Street (Kelani Ganga) | 0.82 | 🟢 Normal | -0.058 |  |
| 2026-11-12 18:03:51 | Hanwella (Kelani Ganga) | 4.86 | 🟢 Normal | -0.098 |  |
| 2026-11-12 18:03:30 | Glencourse (Kelani Ganga) | 12.10 | 🟢 Normal | -0.111 |  |
| 2026-11-12 18:01:57 | Thaldena (Mahaweli Ganga) | 2.67 | 🟢 Normal | -0.115 |  |
| 2026-11-12 18:03:43 | Moragaswewa (Deduru Oya) | 2.58 | 🟢 Normal | -0.289 |  |

## River Water Level Charts by Station

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)