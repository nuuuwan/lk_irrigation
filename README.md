# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--14_10:03:22-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **315,480 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood; 🟡 Baddegama — Alert; 🟡 Panadugama — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **18** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-14 10:03:22 | Galgamuwa (Mee Oya) | 0.29 | 🟢 Normal | -0.010 |  |
| 2026-11-14 10:03:12 | Padiyathalawa (Maduru Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-11-14 10:03:12 | Rathnapura (Kalu Ganga) | 2.40 | 🟢 Normal | -0.011 |  |
| 2026-11-14 10:02:59 | Hanwella (Kelani Ganga) | 2.91 | 🟢 Normal | -0.030 |  |
| 2026-11-14 10:02:58 | Kuda Oya (Kirindi Oya) | 1.97 | 🟢 Normal | -0.010 |  |
| 2026-11-14 10:02:50 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.88 | 🟢 Normal | -0.106 |  |
| 2026-11-14 10:02:25 | Badalgama (Maha Oya) | 3.00 | 🟢 Normal | -0.010 |  |
| 2026-11-14 10:02:15 | Ellagawa (Kalu Ganga) | 6.29 | 🟢 Normal | -0.074 |  |
| 2026-11-14 10:01:47 | Horowpothana (Yan Oya) | 2.30 | 🟢 Normal | -0.019 |  |
| 2026-11-14 10:01:47 | Manampitiya (Mahaweli Ganga) | 1.23 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-14 10:01:43 | Wellawaya (Kirindi Oya) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-11-14 10:01:42 | Thanamalwila (Kirindi Oya) | 1.83 | 🟢 Normal | -0.010 |  |
| 2026-11-14 10:01:35 | Thanthirimale (Malwathu Oya) | 1.66 | 🟢 Normal | 0.000 |  |
| 2026-11-14 10:01:28 | Nawalapitiya (Mahaweli Ganga) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-11-14 10:01:07 | Siyambalanduwa (Heda Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-11-14 10:01:02 | Moragaswewa (Deduru Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-11-14 10:00:50 | Nakkala (Kumbukkan Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-11-14 10:00:36 | Weraganthota (Mahaweli Ganga) | -1.83 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-14 09:23:13 | Thalgahagoda (Nilwala Ganga) | 1.90 | 🟠 Minor Flood | 0.000 |  |
| 2026-11-14 09:07:03 | Baddegama (Gin Ganga) | 3.65 | 🟡 Alert | -0.031 |  |
| 2026-11-14 09:02:42 | Panadugama (Nilwala Ganga) | 5.54 | 🟡 Alert | -0.041 |  |
| 2026-11-14 09:08:46 | Kithulgala (Kelani Ganga) | 2.20 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-11-14 10:01:47 | Manampitiya (Mahaweli Ganga) | 1.23 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-14 10:01:43 | Wellawaya (Kirindi Oya) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-11-14 10:00:50 | Nakkala (Kumbukkan Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-11-14 10:01:02 | Moragaswewa (Deduru Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-11-14 10:01:28 | Nawalapitiya (Mahaweli Ganga) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-11-14 09:01:09 | Giriulla (Maha Oya) | 1.66 | 🟢 Normal | 0.000 |  |
| 2026-11-14 10:03:12 | Padiyathalawa (Maduru Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-11-14 10:01:07 | Siyambalanduwa (Heda Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-11-14 09:06:15 | Katharagama (Menik Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-11-14 09:05:25 | Holombuwa (Kelani Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-11-14 10:01:35 | Thanthirimale (Malwathu Oya) | 1.66 | 🟢 Normal | 0.000 |  |
| 2026-11-14 09:02:01 | Peradeniya (Mahaweli Ganga) | 3.00 | 🟢 Normal | 0.000 |  |
| 2026-11-14 09:26:58 | Urawa (Nilwala Ganga) | 1.27 | 🟢 Normal | -0.009 |  |
| 2026-11-14 09:11:19 | Deraniyagala (Kelani Ganga) | 0.87 | 🟢 Normal | -0.009 |  |
| 2026-11-14 09:05:32 | Norwood (Kelani Ganga) | 1.12 | 🟢 Normal | -0.010 |  |
| 2026-11-14 10:01:42 | Thanamalwila (Kirindi Oya) | 1.83 | 🟢 Normal | -0.010 |  |
| 2026-11-14 10:00:36 | Weraganthota (Mahaweli Ganga) | -1.83 | 🟢 Normal | -0.010 |  |
| 2026-11-14 09:02:05 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | -0.010 |  |
| 2026-11-14 10:02:58 | Kuda Oya (Kirindi Oya) | 1.97 | 🟢 Normal | -0.010 |  |
| 2026-11-14 10:02:25 | Badalgama (Maha Oya) | 3.00 | 🟢 Normal | -0.010 |  |
| 2026-11-14 10:03:22 | Galgamuwa (Mee Oya) | 0.29 | 🟢 Normal | -0.010 |  |
| 2026-11-14 10:03:12 | Rathnapura (Kalu Ganga) | 2.40 | 🟢 Normal | -0.011 |  |
| 2026-11-14 09:08:03 | Magura (Kalu Ganga) | 2.37 | 🟢 Normal | -0.011 |  |
| 2026-11-14 09:01:45 | Pitabeddara (Nilwala Ganga) | 1.71 | 🟢 Normal | -0.011 |  |
| 2026-11-14 09:04:31 | Dunamale (Aththanagalu Oya) | 2.44 | 🟢 Normal | -0.019 |  |
| 2026-11-14 10:01:47 | Horowpothana (Yan Oya) | 2.30 | 🟢 Normal | -0.019 |  |
| 2026-11-14 09:06:36 | Thawalama (Gin Ganga) | 2.25 | 🟢 Normal | -0.020 |  |
| 2026-11-14 09:03:24 | Moraketiya (Walawe Ganga) | 1.88 | 🟢 Normal | -0.020 |  |
| 2026-11-14 09:05:37 | Glencourse (Kelani Ganga) | 10.89 | 🟢 Normal | -0.021 |  |
| 2026-11-14 10:02:59 | Hanwella (Kelani Ganga) | 2.91 | 🟢 Normal | -0.030 |  |
| 2026-11-14 09:05:49 | Thaldena (Mahaweli Ganga) | 0.78 | 🟢 Normal | -0.049 |  |
| 2026-11-14 09:02:30 | Putupaula (Kalu Ganga) | 1.75 | 🟢 Normal | -0.052 |  |
| 2026-11-14 10:02:15 | Ellagawa (Kalu Ganga) | 6.29 | 🟢 Normal | -0.074 |  |
| 2026-11-14 09:05:08 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.102 |  |
| 2026-11-14 10:02:50 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.88 | 🟢 Normal | -0.106 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)