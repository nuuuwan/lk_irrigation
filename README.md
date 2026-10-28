# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--28_09:32:31-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **300,142 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Baddegama — Minor Flood; 🟠 Thalgahagoda — Minor Flood; 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟡 Putupaula — Alert; 🟡 Ellagawa — Alert…
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-28 09:32:31 | Rathnapura (Kalu Ganga) | 6.47 | 🟡 Alert | -0.063 |  |
| 2026-10-28 09:13:21 | Urawa (Nilwala Ganga) | 1.37 | 🟢 Normal | -0.046 |  |
| 2026-10-28 09:09:41 | Horowpothana (Yan Oya) | 3.20 | 🟢 Normal | -0.069 |  |
| 2026-10-28 09:09:23 | Nakkala (Kumbukkan Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-10-28 09:09:19 | Galgamuwa (Mee Oya) | 2.41 | 🟢 Normal | -0.020 |  |
| 2026-10-28 09:07:31 | Padiyathalawa (Maduru Oya) | 0.29 | 🟢 Normal | -0.009 |  |
| 2026-10-28 09:07:28 | Kithulgala (Kelani Ganga) | 2.27 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-10-28 09:07:26 | Magura (Kalu Ganga) | 4.27 | 🟡 Alert | -0.043 |  |
| 2026-10-28 09:07:07 | Norwood (Kelani Ganga) | 1.20 | 🟢 Normal | -0.009 |  |
| 2026-10-28 09:07:04 | Holombuwa (Kelani Ganga) | 1.21 | 🟢 Normal | -0.010 |  |
| 2026-10-28 09:06:20 | Hanwella (Kelani Ganga) | 4.54 | 🟢 Normal | -0.047 |  |
| 2026-10-28 09:06:17 | Deraniyagala (Kelani Ganga) | 1.13 | 🟢 Normal | -0.019 |  |
| 2026-10-28 09:06:15 | Glencourse (Kelani Ganga) | 11.73 | 🟢 Normal | -0.049 |  |
| 2026-10-28 09:06:13 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.77 | 🟠 Minor Flood | -0.010 |  |
| 2026-10-28 09:06:10 | Thawalama (Gin Ganga) | 2.67 | 🟢 Normal | -0.032 |  |
| 2026-10-28 09:05:36 | Panadugama (Nilwala Ganga) | 5.89 | 🟡 Alert | -0.020 |  |
| 2026-10-28 09:05:13 | Baddegama (Gin Ganga) | 4.24 | 🟠 Minor Flood | 0.010 | 🔺 Rising |
| 2026-10-28 09:04:35 | Pitabeddara (Nilwala Ganga) | 2.08 | 🟢 Normal | 0.000 |  |
| 2026-10-28 09:04:12 | Putupaula (Kalu Ganga) | 3.62 | 🟡 Alert | 0.010 | 🔺 Rising |
| 2026-10-28 09:04:09 | Siyambalanduwa (Heda Oya) | 0.53 | 🟢 Normal | -0.010 |  |
| 2026-10-28 09:03:43 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | -0.047 |  |
| 2026-10-28 09:03:39 | Peradeniya (Mahaweli Ganga) | 3.08 | 🟢 Normal | 0.000 |  |
| 2026-10-28 09:03:34 | Weraganthota (Mahaweli Ganga) | -3.14 | 🟢 Normal | -0.096 |  |
| 2026-10-28 09:03:24 | Thaldena (Mahaweli Ganga) | 0.37 | 🟢 Normal | -0.010 |  |
| 2026-10-28 09:03:23 | Manampitiya (Mahaweli Ganga) | 0.33 | 🟢 Normal | -0.020 |  |
| 2026-10-28 09:03:14 | Nakkala (Kumbukkan Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-10-28 09:03:13 | Moraketiya (Walawe Ganga) | 1.39 | 🟢 Normal | -0.010 |  |
| 2026-10-28 09:02:55 | Moragaswewa (Deduru Oya) | 3.06 | 🟢 Normal | -0.031 |  |
| 2026-10-28 09:02:50 | Ellagawa (Kalu Ganga) | 10.45 | 🟡 Alert | 0.000 |  |
| 2026-10-28 09:02:29 | Giriulla (Maha Oya) | 2.27 | 🟢 Normal | -0.050 |  |
| 2026-10-28 09:02:24 | Badalgama (Maha Oya) | 3.55 | 🟢 Normal | -0.050 |  |
| 2026-10-28 09:02:14 | Dunamale (Aththanagalu Oya) | 3.95 | 🟡 Alert | -0.073 |  |
| 2026-10-28 09:02:12 | Katharagama (Menik Ganga) | -0.20 | 🟢 Normal | 0.000 |  |
| 2026-10-28 09:02:09 | Thanthirimale (Malwathu Oya) | 2.35 | 🟢 Normal | -0.050 |  |
| 2026-10-28 09:02:05 | Wellawaya (Kirindi Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-10-28 09:02:01 | Thanamalwila (Kirindi Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-10-28 09:01:40 | Yaka Wewa (Ma Oya) | 0.61 | 🟢 Normal | -0.011 |  |
| 2026-10-28 09:01:22 | Nawalapitiya (Mahaweli Ganga) | 1.56 | 🟢 Normal | 0.000 |  |
| 2026-10-28 09:01:11 | Thalgahagoda (Nilwala Ganga) | 1.80 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-28 09:00:46 | Kuda Oya (Kirindi Oya) | 1.40 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-28 09:05:13 | Baddegama (Gin Ganga) | 4.24 | 🟠 Minor Flood | 0.010 | 🔺 Rising |
| 2026-10-28 09:01:11 | Thalgahagoda (Nilwala Ganga) | 1.80 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-28 09:06:13 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.77 | 🟠 Minor Flood | -0.010 |  |
| 2026-10-28 09:04:12 | Putupaula (Kalu Ganga) | 3.62 | 🟡 Alert | 0.010 | 🔺 Rising |
| 2026-10-28 09:02:50 | Ellagawa (Kalu Ganga) | 10.45 | 🟡 Alert | 0.000 |  |
| 2026-10-28 09:05:36 | Panadugama (Nilwala Ganga) | 5.89 | 🟡 Alert | -0.020 |  |
| 2026-10-28 09:07:26 | Magura (Kalu Ganga) | 4.27 | 🟡 Alert | -0.043 |  |
| 2026-10-28 09:32:31 | Rathnapura (Kalu Ganga) | 6.47 | 🟡 Alert | -0.063 |  |
| 2026-10-28 09:02:14 | Dunamale (Aththanagalu Oya) | 3.95 | 🟡 Alert | -0.073 |  |
| 2026-10-28 09:07:28 | Kithulgala (Kelani Ganga) | 2.27 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-10-28 09:02:05 | Wellawaya (Kirindi Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-10-28 09:09:23 | Nakkala (Kumbukkan Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-10-28 09:01:22 | Nawalapitiya (Mahaweli Ganga) | 1.56 | 🟢 Normal | 0.000 |  |
| 2026-10-28 09:04:35 | Pitabeddara (Nilwala Ganga) | 2.08 | 🟢 Normal | 0.000 |  |
| 2026-10-28 09:02:12 | Katharagama (Menik Ganga) | -0.20 | 🟢 Normal | 0.000 |  |
| 2026-10-28 09:03:39 | Peradeniya (Mahaweli Ganga) | 3.08 | 🟢 Normal | 0.000 |  |
| 2026-10-28 09:00:46 | Kuda Oya (Kirindi Oya) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-10-28 09:02:01 | Thanamalwila (Kirindi Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-10-28 09:07:31 | Padiyathalawa (Maduru Oya) | 0.29 | 🟢 Normal | -0.009 |  |
| 2026-10-28 09:07:07 | Norwood (Kelani Ganga) | 1.20 | 🟢 Normal | -0.009 |  |
| 2026-10-28 09:04:09 | Siyambalanduwa (Heda Oya) | 0.53 | 🟢 Normal | -0.010 |  |
| 2026-10-28 09:07:04 | Holombuwa (Kelani Ganga) | 1.21 | 🟢 Normal | -0.010 |  |
| 2026-10-28 09:03:13 | Moraketiya (Walawe Ganga) | 1.39 | 🟢 Normal | -0.010 |  |
| 2026-10-28 09:03:24 | Thaldena (Mahaweli Ganga) | 0.37 | 🟢 Normal | -0.010 |  |
| 2026-10-28 09:01:40 | Yaka Wewa (Ma Oya) | 0.61 | 🟢 Normal | -0.011 |  |
| 2026-10-28 09:06:17 | Deraniyagala (Kelani Ganga) | 1.13 | 🟢 Normal | -0.019 |  |
| 2026-10-28 09:03:23 | Manampitiya (Mahaweli Ganga) | 0.33 | 🟢 Normal | -0.020 |  |
| 2026-10-28 09:09:19 | Galgamuwa (Mee Oya) | 2.41 | 🟢 Normal | -0.020 |  |
| 2026-10-28 09:02:55 | Moragaswewa (Deduru Oya) | 3.06 | 🟢 Normal | -0.031 |  |
| 2026-10-28 09:06:10 | Thawalama (Gin Ganga) | 2.67 | 🟢 Normal | -0.032 |  |
| 2026-10-28 09:13:21 | Urawa (Nilwala Ganga) | 1.37 | 🟢 Normal | -0.046 |  |
| 2026-10-28 09:03:43 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | -0.047 |  |
| 2026-10-28 09:06:20 | Hanwella (Kelani Ganga) | 4.54 | 🟢 Normal | -0.047 |  |
| 2026-10-28 09:06:15 | Glencourse (Kelani Ganga) | 11.73 | 🟢 Normal | -0.049 |  |
| 2026-10-28 09:02:09 | Thanthirimale (Malwathu Oya) | 2.35 | 🟢 Normal | -0.050 |  |
| 2026-10-28 09:02:24 | Badalgama (Maha Oya) | 3.55 | 🟢 Normal | -0.050 |  |
| 2026-10-28 09:02:29 | Giriulla (Maha Oya) | 2.27 | 🟢 Normal | -0.050 |  |
| 2026-10-28 09:09:41 | Horowpothana (Yan Oya) | 3.20 | 🟢 Normal | -0.069 |  |
| 2026-10-28 09:03:34 | Weraganthota (Mahaweli Ganga) | -3.14 | 🟢 Normal | -0.096 |  |

## River Water Level Charts by Station

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)