# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--31_06:08:38-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **302,732 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood; 🟡 Kalawellawa (Millakanda) — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **43** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-31 06:08:38 | Peradeniya (Mahaweli Ganga) | 2.76 | 🟢 Normal | -0.019 |  |
| 2026-10-31 06:08:25 | Manampitiya (Mahaweli Ganga) | 0.44 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-10-31 06:08:16 | Kuda Oya (Kirindi Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-10-31 06:06:57 | Baddegama (Gin Ganga) | 2.79 | 🟢 Normal | -0.010 |  |
| 2026-10-31 06:06:46 | Norwood (Kelani Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-10-31 06:06:26 | Urawa (Nilwala Ganga) | 1.00 | 🟢 Normal | -0.010 |  |
| 2026-10-31 06:06:10 | Rathnapura (Kalu Ganga) | 2.40 | 🟢 Normal | -0.050 |  |
| 2026-10-31 06:06:06 | Deraniyagala (Kelani Ganga) | 0.80 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-10-31 06:05:48 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | -0.060 |  |
| 2026-10-31 06:05:46 | Padiyathalawa (Maduru Oya) | 1.00 | 🟢 Normal | -0.104 |  |
| 2026-10-31 06:05:17 | Holombuwa (Kelani Ganga) | 0.81 | 🟢 Normal | -0.010 |  |
| 2026-10-31 06:05:14 | Thanamalwila (Kirindi Oya) | 1.40 | 🟢 Normal | -0.152 |  |
| 2026-10-31 06:05:08 | Panadugama (Nilwala Ganga) | 4.92 | 🟢 Normal | -0.045 |  |
| 2026-10-31 06:04:54 | Thalgahagoda (Nilwala Ganga) | 1.70 | 🟠 Minor Flood | -0.028 |  |
| 2026-10-31 06:04:43 | Dunamale (Aththanagalu Oya) | 2.02 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-31 06:04:29 | Katharagama (Menik Ganga) | -0.20 | 🟢 Normal | 0.000 |  |
| 2026-10-31 06:04:12 | Ellagawa (Kalu Ganga) | 7.18 | 🟢 Normal | -0.050 |  |
| 2026-10-31 06:04:08 | Nawalapitiya (Mahaweli Ganga) | 1.29 | 🟢 Normal | -0.010 |  |
| 2026-10-31 06:03:45 | Putupaula (Kalu Ganga) | 2.72 | 🟢 Normal | -0.062 |  |
| 2026-10-31 06:03:32 | Giriulla (Maha Oya) | 1.86 | 🟢 Normal | -0.041 |  |
| 2026-10-31 06:03:20 | Glencourse (Kelani Ganga) | 10.65 | 🟢 Normal | 0.000 |  |
| 2026-10-31 06:02:58 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.61 | 🟡 Alert | -4.096 |  |
| 2026-10-31 06:02:45 | Siyambalanduwa (Heda Oya) | 0.65 | 🟢 Normal | -0.020 |  |
| 2026-10-31 06:02:43 | Katharagama (Menik Ganga) | -0.20 | 🟢 Normal | 0.000 |  |
| 2026-10-31 06:02:27 | Wellawaya (Kirindi Oya) | 1.42 | 🟢 Normal | -0.030 |  |
| 2026-10-31 06:02:10 | Badalgama (Maha Oya) | 3.08 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-10-31 06:02:05 | Kithulgala (Kelani Ganga) | 2.18 | 🟢 Normal | -0.219 |  |
| 2026-10-31 06:01:56 | Hanwella (Kelani Ganga) | 2.76 | 🟢 Normal | -0.021 |  |
| 2026-10-31 06:01:45 | Horowpothana (Yan Oya) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-10-31 06:01:44 | Moraketiya (Walawe Ganga) | 1.08 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-31 06:01:42 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-10-31 06:01:30 | Thaldena (Mahaweli Ganga) | 0.49 | 🟢 Normal | -0.011 |  |
| 2026-10-31 06:01:11 | Moragaswewa (Deduru Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-10-31 06:01:02 | Thawalama (Gin Ganga) | 2.08 | 🟢 Normal | -0.013 |  |
| 2026-10-31 06:00:37 | Nakkala (Kumbukkan Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-10-31 06:00:33 | Magura (Kalu Ganga) | 2.60 | 🟢 Normal | -0.070 |  |
| 2026-10-31 06:00:16 | Weraganthota (Mahaweli Ganga) | -2.83 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-31 06:00:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.80 | 🟡 Alert | -4.096 |  |
| 2026-10-31 05:59:53 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.90 | 🟡 Alert | -4.096 |  |
| 2026-10-31 05:47:56 | Nakkala (Kumbukkan Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-10-31 05:43:02 | Deraniyagala (Kelani Ganga) | 0.78 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-10-31 05:42:25 | Deraniyagala (Kelani Ganga) | 0.78 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-10-31 05:36:43 | Pitabeddara (Nilwala Ganga) | 1.53 | 🟢 Normal | -0.012 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-31 06:04:54 | Thalgahagoda (Nilwala Ganga) | 1.70 | 🟠 Minor Flood | -0.028 |  |
| 2026-10-31 06:02:58 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.61 | 🟡 Alert | -4.096 |  |
| 2026-10-31 06:06:06 | Deraniyagala (Kelani Ganga) | 0.80 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-10-31 06:02:10 | Badalgama (Maha Oya) | 3.08 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-10-31 06:08:25 | Manampitiya (Mahaweli Ganga) | 0.44 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-10-31 06:04:43 | Dunamale (Aththanagalu Oya) | 2.02 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-31 06:01:44 | Moraketiya (Walawe Ganga) | 1.08 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-31 06:00:16 | Weraganthota (Mahaweli Ganga) | -2.83 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-31 06:00:37 | Nakkala (Kumbukkan Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-10-31 06:01:11 | Moragaswewa (Deduru Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-10-31 06:01:42 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-10-31 06:01:45 | Horowpothana (Yan Oya) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-10-30 18:01:07 | Galgamuwa (Mee Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-10-31 06:06:46 | Norwood (Kelani Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-10-31 06:03:20 | Glencourse (Kelani Ganga) | 10.65 | 🟢 Normal | 0.000 |  |
| 2026-10-31 06:04:29 | Katharagama (Menik Ganga) | -0.20 | 🟢 Normal | 0.000 |  |
| 2026-10-31 06:08:16 | Kuda Oya (Kirindi Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-10-31 06:04:08 | Nawalapitiya (Mahaweli Ganga) | 1.29 | 🟢 Normal | -0.010 |  |
| 2026-10-31 06:06:57 | Baddegama (Gin Ganga) | 2.79 | 🟢 Normal | -0.010 |  |
| 2026-10-31 06:06:26 | Urawa (Nilwala Ganga) | 1.00 | 🟢 Normal | -0.010 |  |
| 2026-10-31 06:05:17 | Holombuwa (Kelani Ganga) | 0.81 | 🟢 Normal | -0.010 |  |
| 2026-10-31 06:01:30 | Thaldena (Mahaweli Ganga) | 0.49 | 🟢 Normal | -0.011 |  |
| 2026-10-31 05:36:43 | Pitabeddara (Nilwala Ganga) | 1.53 | 🟢 Normal | -0.012 |  |
| 2026-10-31 06:01:02 | Thawalama (Gin Ganga) | 2.08 | 🟢 Normal | -0.013 |  |
| 2026-10-31 06:08:38 | Peradeniya (Mahaweli Ganga) | 2.76 | 🟢 Normal | -0.019 |  |
| 2026-10-31 06:02:45 | Siyambalanduwa (Heda Oya) | 0.65 | 🟢 Normal | -0.020 |  |
| 2026-10-30 18:00:42 | Thanthirimale (Malwathu Oya) | 1.44 | 🟢 Normal | -0.021 |  |
| 2026-10-31 06:01:56 | Hanwella (Kelani Ganga) | 2.76 | 🟢 Normal | -0.021 |  |
| 2026-10-31 06:02:27 | Wellawaya (Kirindi Oya) | 1.42 | 🟢 Normal | -0.030 |  |
| 2026-10-31 06:03:32 | Giriulla (Maha Oya) | 1.86 | 🟢 Normal | -0.041 |  |
| 2026-10-31 06:05:08 | Panadugama (Nilwala Ganga) | 4.92 | 🟢 Normal | -0.045 |  |
| 2026-10-31 06:06:10 | Rathnapura (Kalu Ganga) | 2.40 | 🟢 Normal | -0.050 |  |
| 2026-10-31 06:04:12 | Ellagawa (Kalu Ganga) | 7.18 | 🟢 Normal | -0.050 |  |
| 2026-10-31 06:05:48 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | -0.060 |  |
| 2026-10-31 06:03:45 | Putupaula (Kalu Ganga) | 2.72 | 🟢 Normal | -0.062 |  |
| 2026-10-31 06:00:33 | Magura (Kalu Ganga) | 2.60 | 🟢 Normal | -0.070 |  |
| 2026-10-31 06:05:46 | Padiyathalawa (Maduru Oya) | 1.00 | 🟢 Normal | -0.104 |  |
| 2026-10-31 06:05:14 | Thanamalwila (Kirindi Oya) | 1.40 | 🟢 Normal | -0.152 |  |
| 2026-10-31 06:02:05 | Kithulgala (Kelani Ganga) | 2.18 | 🟢 Normal | -0.219 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)