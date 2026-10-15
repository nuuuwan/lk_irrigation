# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--15_10:08:33-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **288,466 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood; 🟡 Dunamale — Alert; 🟡 Kalawellawa (Millakanda) — Alert; 🟡 Panadugama — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-15 10:08:33 | Holombuwa (Kelani Ganga) | 1.61 | 🟢 Normal | -0.083 |  |
| 2026-10-15 10:08:19 | Putupaula (Kalu Ganga) | 2.30 | 🟢 Normal | -0.019 |  |
| 2026-10-15 10:07:53 | Horowpothana (Yan Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-10-15 10:07:34 | Pitabeddara (Nilwala Ganga) | 1.57 | 🟢 Normal | -0.009 |  |
| 2026-10-15 10:07:04 | Baddegama (Gin Ganga) | 2.38 | 🟢 Normal | -0.032 |  |
| 2026-10-15 10:06:37 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-10-15 10:06:36 | Giriulla (Maha Oya) | 2.55 | 🟢 Normal | -0.131 |  |
| 2026-10-15 10:06:08 | Glencourse (Kelani Ganga) | 12.14 | 🟢 Normal | -0.168 |  |
| 2026-10-15 10:05:54 | Thaldena (Mahaweli Ganga) | 0.28 | 🟢 Normal | -0.048 |  |
| 2026-10-15 10:05:38 | Badalgama (Maha Oya) | 4.01 | 🟢 Normal | -0.143 |  |
| 2026-10-15 10:05:26 | Thawalama (Gin Ganga) | 2.19 | 🟢 Normal | -0.010 |  |
| 2026-10-15 10:04:23 | Moraketiya (Walawe Ganga) | 1.27 | 🟢 Normal | -0.030 |  |
| 2026-10-15 10:04:20 | Dunamale (Aththanagalu Oya) | 3.92 | 🟡 Alert | -0.011 |  |
| 2026-10-15 10:04:18 | Deraniyagala (Kelani Ganga) | 0.79 | 🟢 Normal | -0.020 |  |
| 2026-10-15 10:04:15 | Galgamuwa (Mee Oya) | 0.47 | 🟢 Normal | 0.240 | 🔺 Rising |
| 2026-10-15 10:04:08 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | -0.030 |  |
| 2026-10-15 10:03:36 | Rathnapura (Kalu Ganga) | 3.60 | 🟢 Normal | -0.153 |  |
| 2026-10-15 10:03:28 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-15 10:03:05 | Hanwella (Kelani Ganga) | 4.79 | 🟢 Normal | -0.090 |  |
| 2026-10-15 10:02:51 | Norwood (Kelani Ganga) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-10-15 10:02:39 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.98 | 🟡 Alert | -0.020 |  |
| 2026-10-15 10:02:32 | Kuda Oya (Kirindi Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-10-15 10:02:19 | Thanamalwila (Kirindi Oya) | 0.86 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-15 10:02:08 | Ellagawa (Kalu Ganga) | 8.11 | 🟢 Normal | 0.000 |  |
| 2026-10-15 10:02:06 | Nawalapitiya (Mahaweli Ganga) | 1.22 | 🟢 Normal | -0.010 |  |
| 2026-10-15 10:01:38 | Kithulgala (Kelani Ganga) | 2.11 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-15 10:01:37 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-10-15 10:01:35 | Thanthirimale (Malwathu Oya) | 1.11 | 🟢 Normal | 36.000 | 🔺 Rising |
| 2026-10-15 10:01:34 | Thanthirimale (Malwathu Oya) | 1.10 | 🟢 Normal | 36.000 | 🔺 Rising |
| 2026-10-15 10:01:31 | Kuda Oya (Kirindi Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-10-15 10:01:18 | Peradeniya (Mahaweli Ganga) | 2.82 | 🟢 Normal | -0.231 |  |
| 2026-10-15 10:01:03 | Kuda Oya (Kirindi Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-10-15 10:01:00 | Moragaswewa (Deduru Oya) | 0.94 | 🟢 Normal | 0.251 | 🔺 Rising |
| 2026-10-15 10:00:57 | Weraganthota (Mahaweli Ganga) | -3.24 | 🟢 Normal | -0.040 |  |
| 2026-10-15 10:00:46 | Manampitiya (Mahaweli Ganga) | 0.53 | 🟢 Normal | -0.071 |  |
| 2026-10-15 10:00:45 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-10-15 10:00:13 | Wellawaya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-10-15 09:49:04 | Moragaswewa (Deduru Oya) | 0.89 | 🟢 Normal | 0.251 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-15 09:10:03 | Thalgahagoda (Nilwala Ganga) | 1.80 | 🟠 Minor Flood | 0.044 | 🔺 Rising |
| 2026-10-15 10:04:20 | Dunamale (Aththanagalu Oya) | 3.92 | 🟡 Alert | -0.011 |  |
| 2026-10-15 10:02:39 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.98 | 🟡 Alert | -0.020 |  |
| 2026-10-15 09:03:55 | Panadugama (Nilwala Ganga) | 5.01 | 🟡 Alert | -0.021 |  |
| 2026-10-15 10:01:35 | Thanthirimale (Malwathu Oya) | 1.11 | 🟢 Normal | 36.000 | 🔺 Rising |
| 2026-10-15 10:01:00 | Moragaswewa (Deduru Oya) | 0.94 | 🟢 Normal | 0.251 | 🔺 Rising |
| 2026-10-15 10:04:15 | Galgamuwa (Mee Oya) | 0.47 | 🟢 Normal | 0.240 | 🔺 Rising |
| 2026-10-15 09:14:34 | Urawa (Nilwala Ganga) | 0.98 | 🟢 Normal | 0.093 | 🔺 Rising |
| 2026-10-15 10:03:28 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-15 10:02:19 | Thanamalwila (Kirindi Oya) | 0.86 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-15 10:01:38 | Kithulgala (Kelani Ganga) | 2.11 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-15 10:00:13 | Wellawaya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-10-15 10:00:45 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-10-15 10:07:53 | Horowpothana (Yan Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-10-15 10:02:51 | Norwood (Kelani Ganga) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-10-15 10:02:08 | Ellagawa (Kalu Ganga) | 8.11 | 🟢 Normal | 0.000 |  |
| 2026-10-15 10:01:37 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-10-15 10:06:37 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-10-15 10:02:32 | Kuda Oya (Kirindi Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-10-15 10:07:34 | Pitabeddara (Nilwala Ganga) | 1.57 | 🟢 Normal | -0.009 |  |
| 2026-10-15 10:05:26 | Thawalama (Gin Ganga) | 2.19 | 🟢 Normal | -0.010 |  |
| 2026-10-15 10:02:06 | Nawalapitiya (Mahaweli Ganga) | 1.22 | 🟢 Normal | -0.010 |  |
| 2026-10-15 09:01:34 | Yaka Wewa (Ma Oya) | 0.63 | 🟢 Normal | -0.011 |  |
| 2026-10-15 10:08:19 | Putupaula (Kalu Ganga) | 2.30 | 🟢 Normal | -0.019 |  |
| 2026-10-15 10:04:18 | Deraniyagala (Kelani Ganga) | 0.79 | 🟢 Normal | -0.020 |  |
| 2026-10-15 10:04:23 | Moraketiya (Walawe Ganga) | 1.27 | 🟢 Normal | -0.030 |  |
| 2026-10-15 10:04:08 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | -0.030 |  |
| 2026-10-15 10:07:04 | Baddegama (Gin Ganga) | 2.38 | 🟢 Normal | -0.032 |  |
| 2026-10-15 09:04:54 | Magura (Kalu Ganga) | 3.73 | 🟢 Normal | -0.035 |  |
| 2026-10-15 10:00:57 | Weraganthota (Mahaweli Ganga) | -3.24 | 🟢 Normal | -0.040 |  |
| 2026-10-15 10:05:54 | Thaldena (Mahaweli Ganga) | 0.28 | 🟢 Normal | -0.048 |  |
| 2026-10-15 10:00:46 | Manampitiya (Mahaweli Ganga) | 0.53 | 🟢 Normal | -0.071 |  |
| 2026-10-15 10:08:33 | Holombuwa (Kelani Ganga) | 1.61 | 🟢 Normal | -0.083 |  |
| 2026-10-15 10:03:05 | Hanwella (Kelani Ganga) | 4.79 | 🟢 Normal | -0.090 |  |
| 2026-10-15 10:06:36 | Giriulla (Maha Oya) | 2.55 | 🟢 Normal | -0.131 |  |
| 2026-10-15 10:05:38 | Badalgama (Maha Oya) | 4.01 | 🟢 Normal | -0.143 |  |
| 2026-10-15 10:03:36 | Rathnapura (Kalu Ganga) | 3.60 | 🟢 Normal | -0.153 |  |
| 2026-10-15 10:06:08 | Glencourse (Kelani Ganga) | 12.14 | 🟢 Normal | -0.168 |  |
| 2026-10-15 10:01:18 | Peradeniya (Mahaweli Ganga) | 2.82 | 🟢 Normal | -0.231 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)