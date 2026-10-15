# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--15_19:07:11-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **288,818 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Panadugama — Minor Flood; 🟠 Thalgahagoda — Minor Flood; 🟡 Pitabeddara — Alert; 🟡 Dunamale — Alert; 🟡 Kalawellawa (Millakanda) — Alert…
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **30** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-15 19:07:11 | Katharagama (Menik Ganga) | 0.14 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-10-15 19:05:40 | Putupaula (Kalu Ganga) | 2.46 | 🟢 Normal | 0.000 |  |
| 2026-10-15 19:05:37 | Badalgama (Maha Oya) | 3.42 | 🟢 Normal | -0.029 |  |
| 2026-10-15 19:05:22 | Manampitiya (Mahaweli Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-10-15 19:05:08 | Hanwella (Kelani Ganga) | 4.18 | 🟢 Normal | -0.020 |  |
| 2026-10-15 19:04:42 | Panadugama (Nilwala Ganga) | 6.20 | 🟠 Minor Flood | 0.171 | 🔺 Rising |
| 2026-10-15 19:04:39 | Ellagawa (Kalu Ganga) | 7.96 | 🟢 Normal | -0.028 |  |
| 2026-10-15 19:04:34 | Thaldena (Mahaweli Ganga) | 0.25 | 🟢 Normal | -0.048 |  |
| 2026-10-15 19:04:34 | Dunamale (Aththanagalu Oya) | 3.77 | 🟡 Alert | 0.000 |  |
| 2026-10-15 19:04:29 | Deraniyagala (Kelani Ganga) | 0.79 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-10-15 19:04:27 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.89 | 🟡 Alert | 0.000 |  |
| 2026-10-15 19:04:12 | Baddegama (Gin Ganga) | 2.68 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-10-15 19:04:02 | Kithulgala (Kelani Ganga) | 2.10 | 🟢 Normal | 0.097 | 🔺 Rising |
| 2026-10-15 19:03:54 | Wellawaya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-10-15 19:03:52 | Norwood (Kelani Ganga) | 1.41 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-10-15 19:03:37 | Moragaswewa (Deduru Oya) | 2.31 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-15 19:03:33 | Glencourse (Kelani Ganga) | 11.61 | 🟢 Normal | -0.093 |  |
| 2026-10-15 19:03:27 | Yaka Wewa (Ma Oya) | 0.66 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-10-15 19:03:27 | Holombuwa (Kelani Ganga) | 1.36 | 🟢 Normal | -0.039 |  |
| 2026-10-15 19:03:16 | Kuda Oya (Kirindi Oya) | 1.29 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-15 19:03:04 | Thanamalwila (Kirindi Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-10-15 19:02:38 | Peradeniya (Mahaweli Ganga) | 3.10 | 🟢 Normal | -0.100 |  |
| 2026-10-15 19:02:19 | Magura (Kalu Ganga) | 3.64 | 🟢 Normal | 0.120 | 🔺 Rising |
| 2026-10-15 19:02:15 | Nagalagam Street (Kelani Ganga) | 0.79 | 🟢 Normal | -0.062 |  |
| 2026-10-15 19:02:09 | Nakkala (Kumbukkan Oya) | 0.64 | 🟢 Normal | -0.010 |  |
| 2026-10-15 19:02:07 | Moraketiya (Walawe Ganga) | 2.25 | 🟢 Normal | -0.656 |  |
| 2026-10-15 19:01:42 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-10-15 19:01:36 | Nawalapitiya (Mahaweli Ganga) | 1.29 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-15 19:01:13 | Pitabeddara (Nilwala Ganga) | 4.58 | 🟡 Alert | 0.112 | 🔺 Rising |
| 2026-10-15 19:00:08 | Horowpothana (Yan Oya) | 1.86 | 🟢 Normal | 0.010 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-15 19:04:42 | Panadugama (Nilwala Ganga) | 6.20 | 🟠 Minor Flood | 0.171 | 🔺 Rising |
| 2026-10-15 18:07:28 | Thalgahagoda (Nilwala Ganga) | 1.83 | 🟠 Minor Flood | 0.012 | 🔺 Rising |
| 2026-10-15 19:01:13 | Pitabeddara (Nilwala Ganga) | 4.58 | 🟡 Alert | 0.112 | 🔺 Rising |
| 2026-10-15 19:04:34 | Dunamale (Aththanagalu Oya) | 3.77 | 🟡 Alert | 0.000 |  |
| 2026-10-15 19:04:27 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.89 | 🟡 Alert | 0.000 |  |
| 2026-10-15 18:09:13 | Urawa (Nilwala Ganga) | 3.08 | 🟡 Alert | -0.128 |  |
| 2026-10-15 19:02:19 | Magura (Kalu Ganga) | 3.64 | 🟢 Normal | 0.120 | 🔺 Rising |
| 2026-10-15 19:04:02 | Kithulgala (Kelani Ganga) | 2.10 | 🟢 Normal | 0.097 | 🔺 Rising |
| 2026-10-15 19:04:12 | Baddegama (Gin Ganga) | 2.68 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-10-15 18:04:44 | Thanthirimale (Malwathu Oya) | 1.47 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-10-15 19:07:11 | Katharagama (Menik Ganga) | 0.14 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-10-15 19:03:52 | Norwood (Kelani Ganga) | 1.41 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-10-15 19:01:36 | Nawalapitiya (Mahaweli Ganga) | 1.29 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-15 19:03:37 | Moragaswewa (Deduru Oya) | 2.31 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-15 19:04:29 | Deraniyagala (Kelani Ganga) | 0.79 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-10-15 19:03:27 | Yaka Wewa (Ma Oya) | 0.66 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-10-15 18:04:39 | Thawalama (Gin Ganga) | 3.90 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-15 18:18:48 | Galgamuwa (Mee Oya) | 0.58 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-10-15 18:03:12 | Giriulla (Maha Oya) | 2.28 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-15 19:00:08 | Horowpothana (Yan Oya) | 1.86 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-15 19:03:16 | Kuda Oya (Kirindi Oya) | 1.29 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-15 18:02:23 | Weraganthota (Mahaweli Ganga) | -3.25 | 🟢 Normal | 0.000 |  |
| 2026-10-15 19:03:54 | Wellawaya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-10-15 18:04:35 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-10-15 19:01:42 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-10-15 19:05:40 | Putupaula (Kalu Ganga) | 2.46 | 🟢 Normal | 0.000 |  |
| 2026-10-15 19:05:22 | Manampitiya (Mahaweli Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-10-15 19:03:04 | Thanamalwila (Kirindi Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-10-15 19:02:09 | Nakkala (Kumbukkan Oya) | 0.64 | 🟢 Normal | -0.010 |  |
| 2026-10-15 19:05:08 | Hanwella (Kelani Ganga) | 4.18 | 🟢 Normal | -0.020 |  |
| 2026-10-15 19:04:39 | Ellagawa (Kalu Ganga) | 7.96 | 🟢 Normal | -0.028 |  |
| 2026-10-15 19:05:37 | Badalgama (Maha Oya) | 3.42 | 🟢 Normal | -0.029 |  |
| 2026-10-15 19:03:27 | Holombuwa (Kelani Ganga) | 1.36 | 🟢 Normal | -0.039 |  |
| 2026-10-15 18:01:30 | Rathnapura (Kalu Ganga) | 3.00 | 🟢 Normal | -0.042 |  |
| 2026-10-15 19:04:34 | Thaldena (Mahaweli Ganga) | 0.25 | 🟢 Normal | -0.048 |  |
| 2026-10-15 19:02:15 | Nagalagam Street (Kelani Ganga) | 0.79 | 🟢 Normal | -0.062 |  |
| 2026-10-15 19:03:33 | Glencourse (Kelani Ganga) | 11.61 | 🟢 Normal | -0.093 |  |
| 2026-10-15 19:02:38 | Peradeniya (Mahaweli Ganga) | 3.10 | 🟢 Normal | -0.100 |  |
| 2026-10-15 19:02:07 | Moraketiya (Walawe Ganga) | 2.25 | 🟢 Normal | -0.656 |  |

## River Water Level Charts by Station

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)