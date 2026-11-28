# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--28_18:33:55-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **328,188 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Dunamale — Alert; 🟡 Kalawellawa (Millakanda) — Alert; 🟡 Moraketiya — Alert; 🟡 Panadugama — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **43** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-28 18:33:55 | Thalgahagoda (Nilwala Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-11-28 18:25:54 | Horowpothana (Yan Oya) | 2.33 | 🟢 Normal | -0.007 |  |
| 2026-11-28 18:12:14 | Urawa (Nilwala Ganga) | 1.08 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-11-28 18:11:18 | Holombuwa (Kelani Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-11-28 18:11:05 | Holombuwa (Kelani Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-11-28 18:09:19 | Padiyathalawa (Maduru Oya) | 0.56 | 🟢 Normal | -0.009 |  |
| 2026-11-28 18:08:54 | Dunamale (Aththanagalu Oya) | 3.90 | 🟡 Alert | 0.000 |  |
| 2026-11-28 18:08:53 | Dunamale (Aththanagalu Oya) | 3.90 | 🟡 Alert | 0.000 |  |
| 2026-11-28 18:08:51 | Dunamale (Aththanagalu Oya) | 3.95 | 🟡 Alert | 0.000 |  |
| 2026-11-28 18:08:22 | Glencourse (Kelani Ganga) | 10.76 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-11-28 18:07:54 | Badalgama (Maha Oya) | 3.61 | 🟢 Normal | -0.039 |  |
| 2026-11-28 18:05:45 | Hanwella (Kelani Ganga) | 3.10 | 🟢 Normal | -0.076 |  |
| 2026-11-28 18:04:25 | Moragaswewa (Deduru Oya) | 2.16 | 🟢 Normal | -0.009 |  |
| 2026-11-28 18:04:20 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | -0.032 |  |
| 2026-11-28 18:04:15 | Peradeniya (Mahaweli Ganga) | 2.60 | 🟢 Normal | -60.000 |  |
| 2026-11-28 18:04:15 | Kithulgala (Kelani Ganga) | 1.75 | 🟢 Normal | -0.067 |  |
| 2026-11-28 18:04:12 | Pitabeddara (Nilwala Ganga) | 1.62 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-11-28 18:04:12 | Peradeniya (Mahaweli Ganga) | 2.65 | 🟢 Normal | -60.000 |  |
| 2026-11-28 18:03:58 | Panadugama (Nilwala Ganga) | 5.02 | 🟡 Alert | -0.070 |  |
| 2026-11-28 18:03:55 | Thaldena (Mahaweli Ganga) | 0.69 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-11-28 18:03:53 | Rathnapura (Kalu Ganga) | 2.26 | 🟢 Normal | 0.094 | 🔺 Rising |
| 2026-11-28 18:03:35 | Thawalama (Gin Ganga) | 2.35 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-11-28 18:03:29 | Weraganthota (Mahaweli Ganga) | -1.52 | 🟢 Normal | -0.030 |  |
| 2026-11-28 18:03:28 | Katharagama (Menik Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-11-28 18:03:25 | Galgamuwa (Mee Oya) | 0.32 | 🟢 Normal | -0.029 |  |
| 2026-11-28 18:03:19 | Magura (Kalu Ganga) | 3.49 | 🟢 Normal | 0.335 | 🔺 Rising |
| 2026-11-28 18:02:49 | Moraketiya (Walawe Ganga) | 3.08 | 🟡 Alert | -0.020 |  |
| 2026-11-28 18:02:42 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-11-28 18:02:42 | Baddegama (Gin Ganga) | 2.05 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-28 18:02:34 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.09 | 🟡 Alert | -0.010 |  |
| 2026-11-28 18:02:30 | Deraniyagala (Kelani Ganga) | 0.70 | 🟢 Normal | -0.010 |  |
| 2026-11-28 18:02:24 | Ellagawa (Kalu Ganga) | 6.64 | 🟢 Normal | -0.041 |  |
| 2026-11-28 18:02:16 | Nawalapitiya (Mahaweli Ganga) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-11-28 18:02:13 | Thanamalwila (Kirindi Oya) | 1.95 | 🟢 Normal | -0.010 |  |
| 2026-11-28 18:01:54 | Norwood (Kelani Ganga) | 1.11 | 🟢 Normal | 0.129 | 🔺 Rising |
| 2026-11-28 18:01:47 | Nakkala (Kumbukkan Oya) | 0.98 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-11-28 18:01:41 | Thanthirimale (Malwathu Oya) | 1.45 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-28 18:01:27 | Giriulla (Maha Oya) | 2.34 | 🟢 Normal | -0.035 |  |
| 2026-11-28 18:01:10 | Kuda Oya (Kirindi Oya) | 2.20 | 🟢 Normal | -0.030 |  |
| 2026-11-28 18:00:39 | Putupaula (Kalu Ganga) | 1.66 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-11-28 18:00:33 | Siyambalanduwa (Heda Oya) | 0.79 | 🟢 Normal | -0.010 |  |
| 2026-11-28 18:00:24 | Wellawaya (Kirindi Oya) | 1.49 | 🟢 Normal | -0.011 |  |
| 2026-11-28 18:00:22 | Manampitiya (Mahaweli Ganga) | 1.78 | 🟢 Normal | -0.020 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-28 18:08:54 | Dunamale (Aththanagalu Oya) | 3.90 | 🟡 Alert | 0.000 |  |
| 2026-11-28 18:02:34 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.09 | 🟡 Alert | -0.010 |  |
| 2026-11-28 18:02:49 | Moraketiya (Walawe Ganga) | 3.08 | 🟡 Alert | -0.020 |  |
| 2026-11-28 18:03:58 | Panadugama (Nilwala Ganga) | 5.02 | 🟡 Alert | -0.070 |  |
| 2026-11-28 18:03:19 | Magura (Kalu Ganga) | 3.49 | 🟢 Normal | 0.335 | 🔺 Rising |
| 2026-11-28 18:01:54 | Norwood (Kelani Ganga) | 1.11 | 🟢 Normal | 0.129 | 🔺 Rising |
| 2026-11-28 18:03:53 | Rathnapura (Kalu Ganga) | 2.26 | 🟢 Normal | 0.094 | 🔺 Rising |
| 2026-11-28 18:12:14 | Urawa (Nilwala Ganga) | 1.08 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-11-28 18:04:12 | Pitabeddara (Nilwala Ganga) | 1.62 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-11-28 18:03:55 | Thaldena (Mahaweli Ganga) | 0.69 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-11-28 18:08:22 | Glencourse (Kelani Ganga) | 10.76 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-11-28 18:03:35 | Thawalama (Gin Ganga) | 2.35 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-11-28 18:00:39 | Putupaula (Kalu Ganga) | 1.66 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-11-28 18:01:47 | Nakkala (Kumbukkan Oya) | 0.98 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-11-28 18:02:42 | Baddegama (Gin Ganga) | 2.05 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-28 18:01:41 | Thanthirimale (Malwathu Oya) | 1.45 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-28 18:02:16 | Nawalapitiya (Mahaweli Ganga) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-11-28 18:02:42 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-11-28 18:03:28 | Katharagama (Menik Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-11-28 18:11:18 | Holombuwa (Kelani Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-11-28 18:33:55 | Thalgahagoda (Nilwala Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-11-28 18:25:54 | Horowpothana (Yan Oya) | 2.33 | 🟢 Normal | -0.007 |  |
| 2026-11-28 18:09:19 | Padiyathalawa (Maduru Oya) | 0.56 | 🟢 Normal | -0.009 |  |
| 2026-11-28 18:04:25 | Moragaswewa (Deduru Oya) | 2.16 | 🟢 Normal | -0.009 |  |
| 2026-11-28 18:02:13 | Thanamalwila (Kirindi Oya) | 1.95 | 🟢 Normal | -0.010 |  |
| 2026-11-28 18:00:33 | Siyambalanduwa (Heda Oya) | 0.79 | 🟢 Normal | -0.010 |  |
| 2026-11-28 18:02:30 | Deraniyagala (Kelani Ganga) | 0.70 | 🟢 Normal | -0.010 |  |
| 2026-11-28 18:00:24 | Wellawaya (Kirindi Oya) | 1.49 | 🟢 Normal | -0.011 |  |
| 2026-11-28 18:00:22 | Manampitiya (Mahaweli Ganga) | 1.78 | 🟢 Normal | -0.020 |  |
| 2026-11-28 18:03:25 | Galgamuwa (Mee Oya) | 0.32 | 🟢 Normal | -0.029 |  |
| 2026-11-28 18:03:29 | Weraganthota (Mahaweli Ganga) | -1.52 | 🟢 Normal | -0.030 |  |
| 2026-11-28 18:01:10 | Kuda Oya (Kirindi Oya) | 2.20 | 🟢 Normal | -0.030 |  |
| 2026-11-28 18:04:20 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | -0.032 |  |
| 2026-11-28 18:01:27 | Giriulla (Maha Oya) | 2.34 | 🟢 Normal | -0.035 |  |
| 2026-11-28 18:07:54 | Badalgama (Maha Oya) | 3.61 | 🟢 Normal | -0.039 |  |
| 2026-11-28 18:02:24 | Ellagawa (Kalu Ganga) | 6.64 | 🟢 Normal | -0.041 |  |
| 2026-11-28 18:04:15 | Kithulgala (Kelani Ganga) | 1.75 | 🟢 Normal | -0.067 |  |
| 2026-11-28 18:05:45 | Hanwella (Kelani Ganga) | 3.10 | 🟢 Normal | -0.076 |  |
| 2026-11-28 18:04:15 | Peradeniya (Mahaweli Ganga) | 2.60 | 🟢 Normal | -60.000 |  |

## River Water Level Charts by Station

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)