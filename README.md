# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--31_01:03:50-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **302,539 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood; 🟡 Panadugama — Alert; 🟡 Putupaula — Alert; 🟡 Kalawellawa (Millakanda) — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **18** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-31 01:03:50 | Giriulla (Maha Oya) | 1.90 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-10-31 01:03:50 | Wellawaya (Kirindi Oya) | 1.48 | 🟢 Normal | -0.030 |  |
| 2026-10-31 01:03:43 | Deraniyagala (Kelani Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-10-31 01:03:33 | Baddegama (Gin Ganga) | 2.93 | 🟢 Normal | -0.050 |  |
| 2026-10-31 01:03:04 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-10-31 01:02:46 | Peradeniya (Mahaweli Ganga) | 2.92 | 🟢 Normal | -0.148 |  |
| 2026-10-31 01:02:40 | Kuda Oya (Kirindi Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-10-31 01:02:32 | Katharagama (Menik Ganga) | -0.20 | 🟢 Normal | 0.000 |  |
| 2026-10-31 01:02:16 | Kithulgala (Kelani Ganga) | 2.10 | 🟢 Normal | -0.073 |  |
| 2026-10-31 01:02:10 | Thanamalwila (Kirindi Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-10-31 01:02:01 | Manampitiya (Mahaweli Ganga) | 0.60 | 🟢 Normal | -0.084 |  |
| 2026-10-31 01:01:43 | Moragaswewa (Deduru Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-10-31 01:01:33 | Horowpothana (Yan Oya) | 2.00 | 🟢 Normal | -0.013 |  |
| 2026-10-31 01:01:17 | Rathnapura (Kalu Ganga) | 2.54 | 🟢 Normal | 0.000 |  |
| 2026-10-31 01:01:14 | Nakkala (Kumbukkan Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-10-31 01:00:56 | Rathnapura (Kalu Ganga) | 2.54 | 🟢 Normal | 0.000 |  |
| 2026-10-31 01:00:42 | Thalgahagoda (Nilwala Ganga) | 1.76 | 🟠 Minor Flood | -0.013 |  |
| 2026-10-31 01:00:06 | Siyambalanduwa (Heda Oya) | 0.61 | 🟢 Normal | -0.020 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-31 01:00:42 | Thalgahagoda (Nilwala Ganga) | 1.76 | 🟠 Minor Flood | -0.013 |  |
| 2026-10-31 00:15:01 | Panadugama (Nilwala Ganga) | 5.05 | 🟡 Alert | -0.017 |  |
| 2026-10-31 00:05:27 | Putupaula (Kalu Ganga) | 3.06 | 🟡 Alert | -0.040 |  |
| 2026-10-31 00:01:57 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.06 | 🟡 Alert | -0.052 |  |
| 2026-10-31 00:12:29 | Magura (Kalu Ganga) | 2.48 | 🟢 Normal | 0.094 | 🔺 Rising |
| 2026-10-31 01:03:50 | Giriulla (Maha Oya) | 1.90 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-10-31 00:09:32 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-10-31 00:03:10 | Badalgama (Maha Oya) | 2.85 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-10-31 01:01:14 | Nakkala (Kumbukkan Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-10-31 01:01:43 | Moragaswewa (Deduru Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-10-31 01:03:04 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-10-30 18:01:07 | Galgamuwa (Mee Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-10-31 01:03:43 | Deraniyagala (Kelani Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-10-31 00:16:40 | Glencourse (Kelani Ganga) | 10.75 | 🟢 Normal | 0.000 |  |
| 2026-10-31 00:02:22 | Dunamale (Aththanagalu Oya) | 2.10 | 🟢 Normal | 0.000 |  |
| 2026-10-31 01:02:32 | Katharagama (Menik Ganga) | -0.20 | 🟢 Normal | 0.000 |  |
| 2026-10-31 00:13:51 | Holombuwa (Kelani Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-10-31 01:01:17 | Rathnapura (Kalu Ganga) | 2.54 | 🟢 Normal | 0.000 |  |
| 2026-10-30 23:05:29 | Urawa (Nilwala Ganga) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-10-31 01:02:40 | Kuda Oya (Kirindi Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-10-31 01:02:10 | Thanamalwila (Kirindi Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-10-31 00:06:05 | Moraketiya (Walawe Ganga) | 1.09 | 🟢 Normal | -0.006 |  |
| 2026-10-31 00:06:06 | Hanwella (Kelani Ganga) | 2.83 | 🟢 Normal | -0.009 |  |
| 2026-10-31 00:04:59 | Norwood (Kelani Ganga) | 0.98 | 🟢 Normal | -0.010 |  |
| 2026-10-31 00:01:16 | Pitabeddara (Nilwala Ganga) | 1.57 | 🟢 Normal | -0.010 |  |
| 2026-10-31 00:01:32 | Nawalapitiya (Mahaweli Ganga) | 1.30 | 🟢 Normal | -0.010 |  |
| 2026-10-31 01:01:33 | Horowpothana (Yan Oya) | 2.00 | 🟢 Normal | -0.013 |  |
| 2026-10-31 01:00:06 | Siyambalanduwa (Heda Oya) | 0.61 | 🟢 Normal | -0.020 |  |
| 2026-10-30 18:00:09 | Weraganthota (Mahaweli Ganga) | -3.06 | 🟢 Normal | -0.021 |  |
| 2026-10-31 00:01:07 | Thawalama (Gin Ganga) | 2.16 | 🟢 Normal | -0.021 |  |
| 2026-10-30 18:00:42 | Thanthirimale (Malwathu Oya) | 1.44 | 🟢 Normal | -0.021 |  |
| 2026-10-31 01:03:50 | Wellawaya (Kirindi Oya) | 1.48 | 🟢 Normal | -0.030 |  |
| 2026-10-31 00:04:18 | Padiyathalawa (Maduru Oya) | 1.38 | 🟢 Normal | -0.049 |  |
| 2026-10-31 01:03:33 | Baddegama (Gin Ganga) | 2.93 | 🟢 Normal | -0.050 |  |
| 2026-10-31 00:01:47 | Thaldena (Mahaweli Ganga) | 0.70 | 🟢 Normal | -0.051 |  |
| 2026-10-31 01:02:16 | Kithulgala (Kelani Ganga) | 2.10 | 🟢 Normal | -0.073 |  |
| 2026-10-31 01:02:01 | Manampitiya (Mahaweli Ganga) | 0.60 | 🟢 Normal | -0.084 |  |
| 2026-10-31 00:10:44 | Ellagawa (Kalu Ganga) | 7.80 | 🟢 Normal | -0.090 |  |
| 2026-10-31 01:02:46 | Peradeniya (Mahaweli Ganga) | 2.92 | 🟢 Normal | -0.148 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)