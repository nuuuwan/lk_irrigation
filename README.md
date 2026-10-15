# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--15_06:32:31-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **288,312 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood; 🟡 Dunamale — Alert; 🟡 Panadugama — Alert; 🟡 Kalawellawa (Millakanda) — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **42** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-15 06:32:31 | Galgamuwa (Mee Oya) | 0.25 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-15 06:28:41 | Thalgahagoda (Nilwala Ganga) | 1.75 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-15 06:26:09 | Glencourse (Kelani Ganga) | 13.38 | 🟢 Normal | 77.143 | 🔺 Rising |
| 2026-10-15 06:25:48 | Glencourse (Kelani Ganga) | 12.93 | 🟢 Normal | 77.143 | 🔺 Rising |
| 2026-10-15 06:25:45 | Glencourse (Kelani Ganga) | 13.12 | 🟢 Normal | 77.143 | 🔺 Rising |
| 2026-10-15 06:25:43 | Glencourse (Kelani Ganga) | 13.26 | 🟢 Normal | 77.143 | 🔺 Rising |
| 2026-10-15 06:20:10 | Panadugama (Nilwala Ganga) | 5.10 | 🟡 Alert | -0.032 |  |
| 2026-10-15 06:16:36 | Horowpothana (Yan Oya) | 1.78 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-10-15 06:13:45 | Kuda Oya (Kirindi Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-10-15 06:09:43 | Ellagawa (Kalu Ganga) | 8.10 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-10-15 06:08:28 | Norwood (Kelani Ganga) | 1.25 | 🟢 Normal | -0.018 |  |
| 2026-10-15 06:08:21 | Nagalagam Street (Kelani Ganga) | 0.98 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-10-15 06:07:34 | Moragaswewa (Deduru Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-10-15 06:07:11 | Holombuwa (Kelani Ganga) | 1.72 | 🟢 Normal | -0.254 |  |
| 2026-10-15 06:07:10 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-10-15 06:06:49 | Urawa (Nilwala Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-10-15 06:06:29 | Hanwella (Kelani Ganga) | 5.01 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-10-15 06:05:55 | Baddegama (Gin Ganga) | 2.46 | 🟢 Normal | -0.010 |  |
| 2026-10-15 06:05:43 | Deraniyagala (Kelani Ganga) | 0.90 | 🟢 Normal | -0.010 |  |
| 2026-10-15 06:05:24 | Rathnapura (Kalu Ganga) | 4.07 | 🟢 Normal | -0.155 |  |
| 2026-10-15 06:05:04 | Badalgama (Maha Oya) | 4.42 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-10-15 06:05:03 | Peradeniya (Mahaweli Ganga) | 3.12 | 🟢 Normal | -0.116 |  |
| 2026-10-15 06:04:31 | Dunamale (Aththanagalu Oya) | 3.90 | 🟡 Alert | 0.000 |  |
| 2026-10-15 06:03:52 | Thawalama (Gin Ganga) | 2.30 | 🟢 Normal | -0.135 |  |
| 2026-10-15 06:03:22 | Katharagama (Menik Ganga) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-10-15 06:03:21 | Yaka Wewa (Ma Oya) | 0.66 | 🟢 Normal | -0.010 |  |
| 2026-10-15 06:03:16 | Magura (Kalu Ganga) | 3.89 | 🟢 Normal | -0.116 |  |
| 2026-10-15 06:03:02 | Giriulla (Maha Oya) | 3.21 | 🟢 Normal | -0.451 |  |
| 2026-10-15 06:02:56 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-10-15 06:02:44 | Nawalapitiya (Mahaweli Ganga) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-10-15 06:02:34 | Weraganthota (Mahaweli Ganga) | -3.04 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-10-15 06:02:32 | Thaldena (Mahaweli Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-10-15 06:02:24 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.09 | 🟡 Alert | -0.159 |  |
| 2026-10-15 06:02:14 | Thanamalwila (Kirindi Oya) | 0.82 | 🟢 Normal | -0.020 |  |
| 2026-10-15 06:02:12 | Pitabeddara (Nilwala Ganga) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-10-15 06:01:44 | Manampitiya (Mahaweli Ganga) | 0.79 | 🟢 Normal | -0.010 |  |
| 2026-10-15 06:01:41 | Putupaula (Kalu Ganga) | 2.30 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-10-15 06:01:41 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | -0.021 |  |
| 2026-10-15 06:01:24 | Kithulgala (Kelani Ganga) | 2.05 | 🟢 Normal | -0.072 |  |
| 2026-10-15 06:01:21 | Moraketiya (Walawe Ganga) | 1.28 | 🟢 Normal | 0.123 | 🔺 Rising |
| 2026-10-15 06:00:08 | Wellawaya (Kirindi Oya) | 1.18 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-10-15 05:51:06 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.12 | 🟡 Alert | -0.159 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-15 06:28:41 | Thalgahagoda (Nilwala Ganga) | 1.75 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-15 06:04:31 | Dunamale (Aththanagalu Oya) | 3.90 | 🟡 Alert | 0.000 |  |
| 2026-10-15 06:20:10 | Panadugama (Nilwala Ganga) | 5.10 | 🟡 Alert | -0.032 |  |
| 2026-10-15 06:02:24 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.09 | 🟡 Alert | -0.159 |  |
| 2026-10-15 06:26:09 | Glencourse (Kelani Ganga) | 13.38 | 🟢 Normal | 77.143 | 🔺 Rising |
| 2026-10-15 06:01:21 | Moraketiya (Walawe Ganga) | 1.28 | 🟢 Normal | 0.123 | 🔺 Rising |
| 2026-10-15 06:00:08 | Wellawaya (Kirindi Oya) | 1.18 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-10-15 06:05:04 | Badalgama (Maha Oya) | 4.42 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-10-15 06:01:41 | Putupaula (Kalu Ganga) | 2.30 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-10-15 06:09:43 | Ellagawa (Kalu Ganga) | 8.10 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-10-15 06:08:21 | Nagalagam Street (Kelani Ganga) | 0.98 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-10-15 06:06:29 | Hanwella (Kelani Ganga) | 5.01 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-10-15 06:02:34 | Weraganthota (Mahaweli Ganga) | -3.04 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-10-15 06:32:31 | Galgamuwa (Mee Oya) | 0.25 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-15 06:16:36 | Horowpothana (Yan Oya) | 1.78 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-10-15 06:07:10 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-10-15 06:07:34 | Moragaswewa (Deduru Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-10-15 06:02:44 | Nawalapitiya (Mahaweli Ganga) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-10-15 06:02:12 | Pitabeddara (Nilwala Ganga) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-10-15 06:02:56 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-10-15 06:02:32 | Thaldena (Mahaweli Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-10-15 06:03:22 | Katharagama (Menik Ganga) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-10-14 18:02:47 | Thanthirimale (Malwathu Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-10-15 06:06:49 | Urawa (Nilwala Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-10-15 06:13:45 | Kuda Oya (Kirindi Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-10-15 06:05:43 | Deraniyagala (Kelani Ganga) | 0.90 | 🟢 Normal | -0.010 |  |
| 2026-10-15 06:05:55 | Baddegama (Gin Ganga) | 2.46 | 🟢 Normal | -0.010 |  |
| 2026-10-15 06:03:21 | Yaka Wewa (Ma Oya) | 0.66 | 🟢 Normal | -0.010 |  |
| 2026-10-15 06:01:44 | Manampitiya (Mahaweli Ganga) | 0.79 | 🟢 Normal | -0.010 |  |
| 2026-10-15 06:08:28 | Norwood (Kelani Ganga) | 1.25 | 🟢 Normal | -0.018 |  |
| 2026-10-15 06:02:14 | Thanamalwila (Kirindi Oya) | 0.82 | 🟢 Normal | -0.020 |  |
| 2026-10-15 06:01:41 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | -0.021 |  |
| 2026-10-15 06:01:24 | Kithulgala (Kelani Ganga) | 2.05 | 🟢 Normal | -0.072 |  |
| 2026-10-15 06:03:16 | Magura (Kalu Ganga) | 3.89 | 🟢 Normal | -0.116 |  |
| 2026-10-15 06:05:03 | Peradeniya (Mahaweli Ganga) | 3.12 | 🟢 Normal | -0.116 |  |
| 2026-10-15 06:03:52 | Thawalama (Gin Ganga) | 2.30 | 🟢 Normal | -0.135 |  |
| 2026-10-15 06:05:24 | Rathnapura (Kalu Ganga) | 4.07 | 🟢 Normal | -0.155 |  |
| 2026-10-15 06:07:11 | Holombuwa (Kelani Ganga) | 1.72 | 🟢 Normal | -0.254 |  |
| 2026-10-15 06:03:02 | Giriulla (Maha Oya) | 3.21 | 🟢 Normal | -0.451 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)