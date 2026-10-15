# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--15_18:16:18-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **288,787 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Panadugama — Minor Flood; 🟠 Thalgahagoda — Minor Flood; 🟡 Pitabeddara — Alert; 🟡 Kalawellawa (Millakanda) — Alert; 🟡 Dunamale — Alert…
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-15 18:16:18 | Yaka Wewa (Ma Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-10-15 18:09:13 | Urawa (Nilwala Ganga) | 3.08 | 🟡 Alert | -0.128 |  |
| 2026-10-15 18:08:24 | Panadugama (Nilwala Ganga) | 6.04 | 🟠 Minor Flood | 0.177 | 🔺 Rising |
| 2026-10-15 18:07:42 | Katharagama (Menik Ganga) | 0.10 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-15 18:07:28 | Thalgahagoda (Nilwala Ganga) | 1.83 | 🟠 Minor Flood | 0.012 | 🔺 Rising |
| 2026-10-15 18:05:28 | Glencourse (Kelani Ganga) | 11.70 | 🟢 Normal | 0.000 |  |
| 2026-10-15 18:05:26 | Glencourse (Kelani Ganga) | 11.70 | 🟢 Normal | 0.000 |  |
| 2026-10-15 18:04:44 | Thanthirimale (Malwathu Oya) | 1.47 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-10-15 18:04:39 | Thawalama (Gin Ganga) | 3.90 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-15 18:04:35 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-10-15 18:04:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.89 | 🟡 Alert | -0.010 |  |
| 2026-10-15 18:04:04 | Wellawaya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-10-15 18:04:03 | Badalgama (Maha Oya) | 3.45 | 🟢 Normal | -0.021 |  |
| 2026-10-15 18:03:45 | Hanwella (Kelani Ganga) | 4.20 | 🟢 Normal | -0.030 |  |
| 2026-10-15 18:03:40 | Nagalagam Street (Kelani Ganga) | 0.85 | 🟢 Normal | -0.031 |  |
| 2026-10-15 18:03:12 | Giriulla (Maha Oya) | 2.28 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-15 18:03:02 | Moragaswewa (Deduru Oya) | 2.28 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-10-15 18:03:01 | Baddegama (Gin Ganga) | 2.61 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-10-15 18:02:54 | Dunamale (Aththanagalu Oya) | 3.77 | 🟡 Alert | -0.011 |  |
| 2026-10-15 18:02:52 | Deraniyagala (Kelani Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-10-15 18:02:49 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-10-15 18:02:42 | Moraketiya (Walawe Ganga) | 2.90 | 🟢 Normal | 1.020 | 🔺 Rising |
| 2026-10-15 18:02:36 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-15 18:02:29 | Norwood (Kelani Ganga) | 1.37 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-15 18:02:23 | Weraganthota (Mahaweli Ganga) | -3.25 | 🟢 Normal | 0.000 |  |
| 2026-10-15 18:02:22 | Peradeniya (Mahaweli Ganga) | 3.20 | 🟢 Normal | -0.021 |  |
| 2026-10-15 18:02:21 | Manampitiya (Mahaweli Ganga) | 0.26 | 🟢 Normal | -0.083 |  |
| 2026-10-15 18:02:16 | Pitabeddara (Nilwala Ganga) | 4.47 | 🟡 Alert | 0.263 | 🔺 Rising |
| 2026-10-15 18:02:16 | Magura (Kalu Ganga) | 3.52 | 🟢 Normal | 0.174 | 🔺 Rising |
| 2026-10-15 18:02:09 | Thanamalwila (Kirindi Oya) | 1.01 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-15 18:02:00 | Kithulgala (Kelani Ganga) | 2.00 | 🟢 Normal | 0.218 | 🔺 Rising |
| 2026-10-15 18:01:30 | Rathnapura (Kalu Ganga) | 3.00 | 🟢 Normal | -0.042 |  |
| 2026-10-15 18:01:26 | Holombuwa (Kelani Ganga) | 1.40 | 🟢 Normal | -0.022 |  |
| 2026-10-15 18:01:13 | Nawalapitiya (Mahaweli Ganga) | 1.26 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-10-15 18:01:13 | Ellagawa (Kalu Ganga) | 7.99 | 🟢 Normal | -0.022 |  |
| 2026-10-15 18:00:45 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-10-15 18:00:32 | Horowpothana (Yan Oya) | 1.85 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-15 18:00:21 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | -0.010 |  |
| 2026-10-15 18:00:16 | Putupaula (Kalu Ganga) | 2.46 | 🟢 Normal | 0.032 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-15 18:08:24 | Panadugama (Nilwala Ganga) | 6.04 | 🟠 Minor Flood | 0.177 | 🔺 Rising |
| 2026-10-15 18:07:28 | Thalgahagoda (Nilwala Ganga) | 1.83 | 🟠 Minor Flood | 0.012 | 🔺 Rising |
| 2026-10-15 18:02:16 | Pitabeddara (Nilwala Ganga) | 4.47 | 🟡 Alert | 0.263 | 🔺 Rising |
| 2026-10-15 18:04:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.89 | 🟡 Alert | -0.010 |  |
| 2026-10-15 18:02:54 | Dunamale (Aththanagalu Oya) | 3.77 | 🟡 Alert | -0.011 |  |
| 2026-10-15 18:09:13 | Urawa (Nilwala Ganga) | 3.08 | 🟡 Alert | -0.128 |  |
| 2026-10-15 18:02:42 | Moraketiya (Walawe Ganga) | 2.90 | 🟢 Normal | 1.020 | 🔺 Rising |
| 2026-10-15 18:02:00 | Kithulgala (Kelani Ganga) | 2.00 | 🟢 Normal | 0.218 | 🔺 Rising |
| 2026-10-15 18:02:16 | Magura (Kalu Ganga) | 3.52 | 🟢 Normal | 0.174 | 🔺 Rising |
| 2026-10-15 18:04:44 | Thanthirimale (Malwathu Oya) | 1.47 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-10-15 18:03:01 | Baddegama (Gin Ganga) | 2.61 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-10-15 17:05:37 | Galgamuwa (Mee Oya) | 0.56 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-10-15 18:00:16 | Putupaula (Kalu Ganga) | 2.46 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-10-15 18:01:13 | Nawalapitiya (Mahaweli Ganga) | 1.26 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-10-15 18:03:02 | Moragaswewa (Deduru Oya) | 2.28 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-10-15 18:02:09 | Thanamalwila (Kirindi Oya) | 1.01 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-15 18:04:39 | Thawalama (Gin Ganga) | 3.90 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-15 18:07:42 | Katharagama (Menik Ganga) | 0.10 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-15 18:03:12 | Giriulla (Maha Oya) | 2.28 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-15 18:00:32 | Horowpothana (Yan Oya) | 1.85 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-15 18:02:36 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-15 18:02:29 | Norwood (Kelani Ganga) | 1.37 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-15 18:02:23 | Weraganthota (Mahaweli Ganga) | -3.25 | 🟢 Normal | 0.000 |  |
| 2026-10-15 18:04:04 | Wellawaya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-10-15 18:16:18 | Yaka Wewa (Ma Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-10-15 18:02:52 | Deraniyagala (Kelani Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-10-15 18:04:35 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-10-15 18:05:28 | Glencourse (Kelani Ganga) | 11.70 | 🟢 Normal | 0.000 |  |
| 2026-10-15 18:02:49 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-10-15 18:00:45 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-10-15 18:00:21 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | -0.010 |  |
| 2026-10-15 18:04:03 | Badalgama (Maha Oya) | 3.45 | 🟢 Normal | -0.021 |  |
| 2026-10-15 18:02:22 | Peradeniya (Mahaweli Ganga) | 3.20 | 🟢 Normal | -0.021 |  |
| 2026-10-15 18:01:26 | Holombuwa (Kelani Ganga) | 1.40 | 🟢 Normal | -0.022 |  |
| 2026-10-15 18:01:13 | Ellagawa (Kalu Ganga) | 7.99 | 🟢 Normal | -0.022 |  |
| 2026-10-15 18:03:45 | Hanwella (Kelani Ganga) | 4.20 | 🟢 Normal | -0.030 |  |
| 2026-10-15 18:03:40 | Nagalagam Street (Kelani Ganga) | 0.85 | 🟢 Normal | -0.031 |  |
| 2026-10-15 18:01:30 | Rathnapura (Kalu Ganga) | 3.00 | 🟢 Normal | -0.042 |  |
| 2026-10-15 18:02:21 | Manampitiya (Mahaweli Ganga) | 0.26 | 🟢 Normal | -0.083 |  |

## River Water Level Charts by Station

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)