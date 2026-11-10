# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--10_20:03:07-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **312,265 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood; 🟠 Baddegama — Minor Flood; 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟠 Dunamale — Minor Flood; 🟡 Peradeniya — Alert…
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **13** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-10 20:03:07 | Giriulla (Maha Oya) | 2.20 | 🟢 Normal | -0.010 |  |
| 2026-11-10 20:02:58 | Horowpothana (Yan Oya) | 2.69 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-11-10 20:02:57 | Peradeniya (Mahaweli Ganga) | 5.82 | 🟡 Alert | 0.683 | 🔺 Rising |
| 2026-11-10 20:02:54 | Hanwella (Kelani Ganga) | 4.42 | 🟢 Normal | -0.102 |  |
| 2026-11-10 20:02:52 | Panadugama (Nilwala Ganga) | 5.84 | 🟡 Alert | 0.088 | 🔺 Rising |
| 2026-11-10 20:02:40 | Nakkala (Kumbukkan Oya) | 1.65 | 🟢 Normal | -0.139 |  |
| 2026-11-10 20:02:34 | Manampitiya (Mahaweli Ganga) | 1.40 | 🟢 Normal | -0.069 |  |
| 2026-11-10 20:02:21 | Ellagawa (Kalu Ganga) | 8.60 | 🟢 Normal | -0.020 |  |
| 2026-11-10 20:02:00 | Kuda Oya (Kirindi Oya) | 1.93 | 🟢 Normal | -0.020 |  |
| 2026-11-10 20:01:45 | Yaka Wewa (Ma Oya) | 0.70 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-11-10 20:01:45 | Glencourse (Kelani Ganga) | 12.19 | 🟢 Normal | 0.231 | 🔺 Rising |
| 2026-11-10 20:00:38 | Thalgahagoda (Nilwala Ganga) | 1.72 | 🟠 Minor Flood | 0.023 | 🔺 Rising |
| 2026-11-10 20:00:14 | Wellawaya (Kirindi Oya) | 1.62 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-10 20:00:38 | Thalgahagoda (Nilwala Ganga) | 1.72 | 🟠 Minor Flood | 0.023 | 🔺 Rising |
| 2026-11-10 19:04:35 | Baddegama (Gin Ganga) | 4.26 | 🟠 Minor Flood | 0.000 |  |
| 2026-11-10 19:01:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.70 | 🟠 Minor Flood | 0.000 |  |
| 2026-11-10 19:04:16 | Dunamale (Aththanagalu Oya) | 4.52 | 🟠 Minor Flood | -0.019 |  |
| 2026-11-10 20:02:57 | Peradeniya (Mahaweli Ganga) | 5.82 | 🟡 Alert | 0.683 | 🔺 Rising |
| 2026-11-10 20:02:52 | Panadugama (Nilwala Ganga) | 5.84 | 🟡 Alert | 0.088 | 🔺 Rising |
| 2026-11-10 19:05:33 | Magura (Kalu Ganga) | 4.30 | 🟡 Alert | -0.078 |  |
| 2026-11-10 19:03:34 | Moraketiya (Walawe Ganga) | 3.00 | 🟡 Alert | -0.269 |  |
| 2026-11-10 19:13:13 | Norwood (Kelani Ganga) | 1.47 | 🟢 Normal | 1.065 | 🔺 Rising |
| 2026-11-10 19:06:34 | Rathnapura (Kalu Ganga) | 5.17 | 🟢 Normal | 0.786 | 🔺 Rising |
| 2026-11-10 19:06:30 | Holombuwa (Kelani Ganga) | 1.66 | 🟢 Normal | 0.542 | 🔺 Rising |
| 2026-11-10 19:01:27 | Pitabeddara (Nilwala Ganga) | 2.42 | 🟢 Normal | 0.376 | 🔺 Rising |
| 2026-11-10 19:05:23 | Thawalama (Gin Ganga) | 3.05 | 🟢 Normal | 0.253 | 🔺 Rising |
| 2026-11-10 20:01:45 | Glencourse (Kelani Ganga) | 12.19 | 🟢 Normal | 0.231 | 🔺 Rising |
| 2026-11-10 19:03:41 | Thaldena (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.216 | 🔺 Rising |
| 2026-11-10 19:02:54 | Nawalapitiya (Mahaweli Ganga) | 1.82 | 🟢 Normal | 0.101 | 🔺 Rising |
| 2026-11-10 18:00:51 | Weraganthota (Mahaweli Ganga) | -2.63 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2026-11-10 20:01:45 | Yaka Wewa (Ma Oya) | 0.70 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-11-10 19:06:20 | Thanamalwila (Kirindi Oya) | 2.05 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-11-10 19:11:23 | Urawa (Nilwala Ganga) | 1.35 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-11-10 19:16:24 | Padiyathalawa (Maduru Oya) | 0.46 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-11-10 20:02:58 | Horowpothana (Yan Oya) | 2.69 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-11-10 19:05:36 | Siyambalanduwa (Heda Oya) | 1.82 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-10 19:04:47 | Kithulgala (Kelani Ganga) | 2.20 | 🟢 Normal | 0.000 |  |
| 2026-11-10 20:00:14 | Wellawaya (Kirindi Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-11-10 19:09:12 | Putupaula (Kalu Ganga) | 2.62 | 🟢 Normal | 0.000 |  |
| 2026-11-10 18:04:35 | Thanthirimale (Malwathu Oya) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-11-10 18:10:04 | Galgamuwa (Mee Oya) | 0.76 | 🟢 Normal | -0.009 |  |
| 2026-11-10 19:04:53 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | -0.010 |  |
| 2026-11-10 20:03:07 | Giriulla (Maha Oya) | 2.20 | 🟢 Normal | -0.010 |  |
| 2026-11-10 20:02:00 | Kuda Oya (Kirindi Oya) | 1.93 | 🟢 Normal | -0.020 |  |
| 2026-11-10 20:02:21 | Ellagawa (Kalu Ganga) | 8.60 | 🟢 Normal | -0.020 |  |
| 2026-11-10 19:07:10 | Badalgama (Maha Oya) | 3.47 | 🟢 Normal | -0.021 |  |
| 2026-11-10 20:02:34 | Manampitiya (Mahaweli Ganga) | 1.40 | 🟢 Normal | -0.069 |  |
| 2026-11-10 20:02:54 | Hanwella (Kelani Ganga) | 4.42 | 🟢 Normal | -0.102 |  |
| 2026-11-10 19:14:54 | Moragaswewa (Deduru Oya) | 3.82 | 🟢 Normal | -0.103 |  |
| 2026-11-10 19:03:07 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.123 |  |
| 2026-11-10 20:02:40 | Nakkala (Kumbukkan Oya) | 1.65 | 🟢 Normal | -0.139 |  |
| 2026-11-10 19:02:03 | Deraniyagala (Kelani Ganga) | 2.43 | 🟢 Normal | -0.474 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)