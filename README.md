# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--16_06:17:32-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **289,216 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Panadugama — Minor Flood; 🟠 Thalgahagoda — Minor Flood; 🟡 Kalawellawa (Millakanda) — Alert; 🟡 Dunamale — Alert; 🟡 Pitabeddara — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-16 06:17:32 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-10-16 06:11:52 | Panadugama (Nilwala Ganga) | 6.69 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-16 06:10:24 | Ellagawa (Kalu Ganga) | 7.55 | 🟢 Normal | -0.028 |  |
| 2026-10-16 06:07:47 | Hanwella (Kelani Ganga) | 3.76 | 🟢 Normal | -0.010 |  |
| 2026-10-16 06:07:26 | Holombuwa (Kelani Ganga) | 1.17 | 🟢 Normal | -0.032 |  |
| 2026-10-16 06:07:17 | Peradeniya (Mahaweli Ganga) | 2.60 | 🟢 Normal | -0.225 |  |
| 2026-10-16 06:06:26 | Glencourse (Kelani Ganga) | 11.35 | 🟢 Normal | -0.020 |  |
| 2026-10-16 06:06:25 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.92 | 🟡 Alert | 0.080 | 🔺 Rising |
| 2026-10-16 06:06:12 | Baddegama (Gin Ganga) | 3.07 | 🟢 Normal | -0.012 |  |
| 2026-10-16 06:05:39 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-10-16 06:05:21 | Dunamale (Aththanagalu Oya) | 3.70 | 🟡 Alert | -0.033 |  |
| 2026-10-16 06:04:50 | Thalgahagoda (Nilwala Ganga) | 1.92 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-16 06:04:46 | Nagalagam Street (Kelani Ganga) | 0.91 | 🟢 Normal | -0.105 |  |
| 2026-10-16 06:04:16 | Horowpothana (Yan Oya) | 1.91 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-16 06:03:57 | Yaka Wewa (Ma Oya) | 0.63 | 🟢 Normal | -0.011 |  |
| 2026-10-16 06:03:44 | Moragaswewa (Deduru Oya) | 2.62 | 🟢 Normal | -0.205 |  |
| 2026-10-16 06:03:37 | Badalgama (Maha Oya) | 3.38 | 🟢 Normal | -0.020 |  |
| 2026-10-16 06:03:33 | Urawa (Nilwala Ganga) | 2.00 | 🟢 Normal | -0.054 |  |
| 2026-10-16 06:03:26 | Thawalama (Gin Ganga) | 3.96 | 🟢 Normal | -0.021 |  |
| 2026-10-16 06:03:13 | Kithulgala (Kelani Ganga) | 2.08 | 🟢 Normal | -0.049 |  |
| 2026-10-16 06:03:12 | Giriulla (Maha Oya) | 2.07 | 🟢 Normal | -0.040 |  |
| 2026-10-16 06:03:11 | Katharagama (Menik Ganga) | 0.08 | 🟢 Normal | -0.025 |  |
| 2026-10-16 06:03:03 | Thanamalwila (Kirindi Oya) | 0.98 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-10-16 06:02:53 | Nawalapitiya (Mahaweli Ganga) | 1.25 | 🟢 Normal | -0.020 |  |
| 2026-10-16 06:02:46 | Norwood (Kelani Ganga) | 1.20 | 🟢 Normal | -0.052 |  |
| 2026-10-16 06:02:39 | Weraganthota (Mahaweli Ganga) | -3.03 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-10-16 06:02:39 | Manampitiya (Mahaweli Ganga) | 0.23 | 🟢 Normal | -0.020 |  |
| 2026-10-16 06:02:38 | Pitabeddara (Nilwala Ganga) | 4.15 | 🟡 Alert | -0.162 |  |
| 2026-10-16 06:02:27 | Magura (Kalu Ganga) | 3.82 | 🟢 Normal | -0.053 |  |
| 2026-10-16 06:02:19 | Deraniyagala (Kelani Ganga) | 0.83 | 🟢 Normal | -0.020 |  |
| 2026-10-16 06:01:54 | Thaldena (Mahaweli Ganga) | 0.28 | 🟢 Normal | -0.011 |  |
| 2026-10-16 06:01:44 | Moraketiya (Walawe Ganga) | 2.20 | 🟢 Normal | -0.117 |  |
| 2026-10-16 06:01:43 | Wellawaya (Kirindi Oya) | 1.12 | 🟢 Normal | -0.043 |  |
| 2026-10-16 06:01:31 | Kuda Oya (Kirindi Oya) | 1.35 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-10-16 06:01:31 | Putupaula (Kalu Ganga) | 2.50 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-10-16 06:01:13 | Rathnapura (Kalu Ganga) | 3.65 | 🟢 Normal | -0.010 |  |
| 2026-10-16 06:00:55 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-16 06:11:52 | Panadugama (Nilwala Ganga) | 6.69 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-16 06:04:50 | Thalgahagoda (Nilwala Ganga) | 1.92 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-16 06:06:25 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.92 | 🟡 Alert | 0.080 | 🔺 Rising |
| 2026-10-16 06:05:21 | Dunamale (Aththanagalu Oya) | 3.70 | 🟡 Alert | -0.033 |  |
| 2026-10-16 06:02:38 | Pitabeddara (Nilwala Ganga) | 4.15 | 🟡 Alert | -0.162 |  |
| 2026-10-15 18:04:44 | Thanthirimale (Malwathu Oya) | 1.47 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-10-16 06:03:03 | Thanamalwila (Kirindi Oya) | 0.98 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-10-16 06:01:31 | Putupaula (Kalu Ganga) | 2.50 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-10-16 06:01:31 | Kuda Oya (Kirindi Oya) | 1.35 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-10-16 06:02:39 | Weraganthota (Mahaweli Ganga) | -3.03 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-10-15 18:18:48 | Galgamuwa (Mee Oya) | 0.58 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-10-16 06:04:16 | Horowpothana (Yan Oya) | 1.91 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-16 06:17:32 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-10-16 06:05:39 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-10-16 06:00:55 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-10-16 06:07:47 | Hanwella (Kelani Ganga) | 3.76 | 🟢 Normal | -0.010 |  |
| 2026-10-16 06:01:13 | Rathnapura (Kalu Ganga) | 3.65 | 🟢 Normal | -0.010 |  |
| 2026-10-16 06:03:57 | Yaka Wewa (Ma Oya) | 0.63 | 🟢 Normal | -0.011 |  |
| 2026-10-16 06:01:54 | Thaldena (Mahaweli Ganga) | 0.28 | 🟢 Normal | -0.011 |  |
| 2026-10-16 06:06:12 | Baddegama (Gin Ganga) | 3.07 | 🟢 Normal | -0.012 |  |
| 2026-10-16 06:06:26 | Glencourse (Kelani Ganga) | 11.35 | 🟢 Normal | -0.020 |  |
| 2026-10-16 06:02:53 | Nawalapitiya (Mahaweli Ganga) | 1.25 | 🟢 Normal | -0.020 |  |
| 2026-10-16 06:02:39 | Manampitiya (Mahaweli Ganga) | 0.23 | 🟢 Normal | -0.020 |  |
| 2026-10-16 06:02:19 | Deraniyagala (Kelani Ganga) | 0.83 | 🟢 Normal | -0.020 |  |
| 2026-10-16 06:03:37 | Badalgama (Maha Oya) | 3.38 | 🟢 Normal | -0.020 |  |
| 2026-10-16 06:03:26 | Thawalama (Gin Ganga) | 3.96 | 🟢 Normal | -0.021 |  |
| 2026-10-16 06:03:11 | Katharagama (Menik Ganga) | 0.08 | 🟢 Normal | -0.025 |  |
| 2026-10-16 06:10:24 | Ellagawa (Kalu Ganga) | 7.55 | 🟢 Normal | -0.028 |  |
| 2026-10-16 06:07:26 | Holombuwa (Kelani Ganga) | 1.17 | 🟢 Normal | -0.032 |  |
| 2026-10-16 06:03:12 | Giriulla (Maha Oya) | 2.07 | 🟢 Normal | -0.040 |  |
| 2026-10-16 06:01:43 | Wellawaya (Kirindi Oya) | 1.12 | 🟢 Normal | -0.043 |  |
| 2026-10-16 06:03:13 | Kithulgala (Kelani Ganga) | 2.08 | 🟢 Normal | -0.049 |  |
| 2026-10-16 06:02:46 | Norwood (Kelani Ganga) | 1.20 | 🟢 Normal | -0.052 |  |
| 2026-10-16 06:02:27 | Magura (Kalu Ganga) | 3.82 | 🟢 Normal | -0.053 |  |
| 2026-10-16 06:03:33 | Urawa (Nilwala Ganga) | 2.00 | 🟢 Normal | -0.054 |  |
| 2026-10-16 06:04:46 | Nagalagam Street (Kelani Ganga) | 0.91 | 🟢 Normal | -0.105 |  |
| 2026-10-16 06:01:44 | Moraketiya (Walawe Ganga) | 2.20 | 🟢 Normal | -0.117 |  |
| 2026-10-16 06:03:44 | Moragaswewa (Deduru Oya) | 2.62 | 🟢 Normal | -0.205 |  |
| 2026-10-16 06:07:17 | Peradeniya (Mahaweli Ganga) | 2.60 | 🟢 Normal | -0.225 |  |

## River Water Level Charts by Station

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)