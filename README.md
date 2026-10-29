# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--29_17:37:59-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **301,362 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood; 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟡 Putupaula — Alert; 🟡 Baddegama — Alert; 🟡 Panadugama — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-29 17:37:59 | Urawa (Nilwala Ganga) | 1.28 | 🟢 Normal | 0.007 | 🔺 Rising |
| 2026-10-29 17:30:26 | Panadugama (Nilwala Ganga) | 5.71 | 🟡 Alert | -0.084 |  |
| 2026-10-29 17:18:40 | Norwood (Kelani Ganga) | 1.05 | 🟢 Normal | -36.000 |  |
| 2026-10-29 17:18:39 | Norwood (Kelani Ganga) | 1.06 | 🟢 Normal | -36.000 |  |
| 2026-10-29 17:08:56 | Panadugama (Nilwala Ganga) | 5.74 | 🟡 Alert | -0.084 |  |
| 2026-10-29 17:08:56 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.16 | 🟠 Minor Flood | -0.045 |  |
| 2026-10-29 17:07:41 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | -0.009 |  |
| 2026-10-29 17:07:32 | Baddegama (Gin Ganga) | 3.99 | 🟡 Alert | -0.019 |  |
| 2026-10-29 17:07:11 | Nagalagam Street (Kelani Ganga) | 0.66 | 🟢 Normal | -0.071 |  |
| 2026-10-29 17:05:59 | Galgamuwa (Mee Oya) | 1.89 | 🟢 Normal | -0.021 |  |
| 2026-10-29 17:05:57 | Badalgama (Maha Oya) | 3.12 | 🟢 Normal | -0.010 |  |
| 2026-10-29 17:05:38 | Thawalama (Gin Ganga) | 2.39 | 🟢 Normal | -0.021 |  |
| 2026-10-29 17:05:19 | Peradeniya (Mahaweli Ganga) | 2.90 | 🟢 Normal | 0.000 |  |
| 2026-10-29 17:05:06 | Horowpothana (Yan Oya) | 2.34 | 🟢 Normal | -0.020 |  |
| 2026-10-29 17:04:49 | Putupaula (Kalu Ganga) | 3.67 | 🟡 Alert | -0.010 |  |
| 2026-10-29 17:04:30 | Holombuwa (Kelani Ganga) | 0.96 | 🟢 Normal | -0.010 |  |
| 2026-10-29 17:03:20 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | -0.009 |  |
| 2026-10-29 17:03:18 | Hanwella (Kelani Ganga) | 3.39 | 🟢 Normal | -0.040 |  |
| 2026-10-29 17:03:15 | Manampitiya (Mahaweli Ganga) | 0.38 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2026-10-29 17:03:09 | Padiyathalawa (Maduru Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-10-29 17:03:08 | Pitabeddara (Nilwala Ganga) | 2.04 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-10-29 17:03:08 | Giriulla (Maha Oya) | 1.83 | 🟢 Normal | -0.010 |  |
| 2026-10-29 17:02:58 | Kithulgala (Kelani Ganga) | 2.10 | 🟢 Normal | -0.079 |  |
| 2026-10-29 17:02:51 | Rathnapura (Kalu Ganga) | 4.43 | 🟢 Normal | -0.051 |  |
| 2026-10-29 17:02:43 | Deraniyagala (Kelani Ganga) | 0.96 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-29 17:02:36 | Moraketiya (Walawe Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-10-29 17:02:29 | Yaka Wewa (Ma Oya) | 0.51 | 🟢 Normal | -0.011 |  |
| 2026-10-29 17:02:26 | Ellagawa (Kalu Ganga) | 9.80 | 🟢 Normal | -0.040 |  |
| 2026-10-29 17:02:23 | Thaldena (Mahaweli Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-10-29 17:02:23 | Moragaswewa (Deduru Oya) | 1.18 | 🟢 Normal | -0.019 |  |
| 2026-10-29 17:02:15 | Glencourse (Kelani Ganga) | 10.96 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-10-29 17:02:12 | Thanamalwila (Kirindi Oya) | 0.86 | 🟢 Normal | -0.020 |  |
| 2026-10-29 17:01:51 | Dunamale (Aththanagalu Oya) | 2.39 | 🟢 Normal | -0.044 |  |
| 2026-10-29 17:01:26 | Kuda Oya (Kirindi Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-10-29 17:01:07 | Thanthirimale (Malwathu Oya) | 1.50 | 🟢 Normal | -0.052 |  |
| 2026-10-29 17:01:00 | Wellawaya (Kirindi Oya) | 1.15 | 🟢 Normal | -0.030 |  |
| 2026-10-29 17:00:53 | Nawalapitiya (Mahaweli Ganga) | 1.39 | 🟢 Normal | -0.011 |  |
| 2026-10-29 17:00:36 | Thalgahagoda (Nilwala Ganga) | 1.87 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-29 17:00:33 | Nakkala (Kumbukkan Oya) | 0.73 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-29 17:00:21 | Weraganthota (Mahaweli Ganga) | -2.74 | 🟢 Normal | 0.258 | 🔺 Rising |
| 2026-10-29 17:00:12 | Magura (Kalu Ganga) | 3.26 | 🟢 Normal | -0.042 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-29 17:00:36 | Thalgahagoda (Nilwala Ganga) | 1.87 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-29 17:08:56 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.16 | 🟠 Minor Flood | -0.045 |  |
| 2026-10-29 17:04:49 | Putupaula (Kalu Ganga) | 3.67 | 🟡 Alert | -0.010 |  |
| 2026-10-29 17:07:32 | Baddegama (Gin Ganga) | 3.99 | 🟡 Alert | -0.019 |  |
| 2026-10-29 17:30:26 | Panadugama (Nilwala Ganga) | 5.71 | 🟡 Alert | -0.084 |  |
| 2026-10-29 17:00:21 | Weraganthota (Mahaweli Ganga) | -2.74 | 🟢 Normal | 0.258 | 🔺 Rising |
| 2026-10-29 17:03:15 | Manampitiya (Mahaweli Ganga) | 0.38 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2026-10-29 17:03:08 | Pitabeddara (Nilwala Ganga) | 2.04 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-10-29 17:02:15 | Glencourse (Kelani Ganga) | 10.96 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-10-29 17:00:33 | Nakkala (Kumbukkan Oya) | 0.73 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-29 17:02:43 | Deraniyagala (Kelani Ganga) | 0.96 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-29 17:37:59 | Urawa (Nilwala Ganga) | 1.28 | 🟢 Normal | 0.007 | 🔺 Rising |
| 2026-10-29 17:03:09 | Padiyathalawa (Maduru Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-10-29 17:02:36 | Moraketiya (Walawe Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-10-29 17:02:23 | Thaldena (Mahaweli Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-10-29 17:05:19 | Peradeniya (Mahaweli Ganga) | 2.90 | 🟢 Normal | 0.000 |  |
| 2026-10-29 17:01:26 | Kuda Oya (Kirindi Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-10-29 17:07:41 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | -0.009 |  |
| 2026-10-29 17:03:20 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | -0.009 |  |
| 2026-10-29 17:05:57 | Badalgama (Maha Oya) | 3.12 | 🟢 Normal | -0.010 |  |
| 2026-10-29 17:03:08 | Giriulla (Maha Oya) | 1.83 | 🟢 Normal | -0.010 |  |
| 2026-10-29 17:04:30 | Holombuwa (Kelani Ganga) | 0.96 | 🟢 Normal | -0.010 |  |
| 2026-10-29 17:00:53 | Nawalapitiya (Mahaweli Ganga) | 1.39 | 🟢 Normal | -0.011 |  |
| 2026-10-29 17:02:29 | Yaka Wewa (Ma Oya) | 0.51 | 🟢 Normal | -0.011 |  |
| 2026-10-29 17:02:23 | Moragaswewa (Deduru Oya) | 1.18 | 🟢 Normal | -0.019 |  |
| 2026-10-29 17:02:12 | Thanamalwila (Kirindi Oya) | 0.86 | 🟢 Normal | -0.020 |  |
| 2026-10-29 17:05:06 | Horowpothana (Yan Oya) | 2.34 | 🟢 Normal | -0.020 |  |
| 2026-10-29 17:05:38 | Thawalama (Gin Ganga) | 2.39 | 🟢 Normal | -0.021 |  |
| 2026-10-29 17:05:59 | Galgamuwa (Mee Oya) | 1.89 | 🟢 Normal | -0.021 |  |
| 2026-10-29 17:01:00 | Wellawaya (Kirindi Oya) | 1.15 | 🟢 Normal | -0.030 |  |
| 2026-10-29 17:03:18 | Hanwella (Kelani Ganga) | 3.39 | 🟢 Normal | -0.040 |  |
| 2026-10-29 17:02:26 | Ellagawa (Kalu Ganga) | 9.80 | 🟢 Normal | -0.040 |  |
| 2026-10-29 17:00:12 | Magura (Kalu Ganga) | 3.26 | 🟢 Normal | -0.042 |  |
| 2026-10-29 17:01:51 | Dunamale (Aththanagalu Oya) | 2.39 | 🟢 Normal | -0.044 |  |
| 2026-10-29 17:02:51 | Rathnapura (Kalu Ganga) | 4.43 | 🟢 Normal | -0.051 |  |
| 2026-10-29 17:01:07 | Thanthirimale (Malwathu Oya) | 1.50 | 🟢 Normal | -0.052 |  |
| 2026-10-29 17:07:11 | Nagalagam Street (Kelani Ganga) | 0.66 | 🟢 Normal | -0.071 |  |
| 2026-10-29 17:02:58 | Kithulgala (Kelani Ganga) | 2.10 | 🟢 Normal | -0.079 |  |
| 2026-10-29 17:18:40 | Norwood (Kelani Ganga) | 1.05 | 🟢 Normal | -36.000 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)