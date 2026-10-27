# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--27_17:07:49-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **299,554 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟠 Baddegama — Minor Flood; 🟠 Panadugama — Minor Flood; 🟠 Dunamale — Minor Flood…
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-27 17:07:49 | Holombuwa (Kelani Ganga) | 1.44 | 🟢 Normal | -0.057 |  |
| 2026-10-27 17:07:00 | Baddegama (Gin Ganga) | 4.12 | 🟠 Minor Flood | 0.012 | 🔺 Rising |
| 2026-10-27 17:06:58 | Glencourse (Kelani Ganga) | 12.39 | 🟢 Normal | -0.121 |  |
| 2026-10-27 17:06:26 | Norwood (Kelani Ganga) | 1.34 | 🟢 Normal | -0.010 |  |
| 2026-10-27 17:06:21 | Pitabeddara (Nilwala Ganga) | 2.27 | 🟢 Normal | -0.049 |  |
| 2026-10-27 17:06:18 | Galgamuwa (Mee Oya) | 4.04 | 🟢 Normal | 0.000 |  |
| 2026-10-27 17:05:41 | Urawa (Nilwala Ganga) | 1.36 | 🟢 Normal | -0.019 |  |
| 2026-10-27 17:05:40 | Kuda Oya (Kirindi Oya) | 1.54 | 🟢 Normal | -0.025 |  |
| 2026-10-27 17:05:01 | Badalgama (Maha Oya) | 4.35 | 🟢 Normal | -0.061 |  |
| 2026-10-27 17:04:08 | Nagalagam Street (Kelani Ganga) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-10-27 17:03:43 | Padiyathalawa (Maduru Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-10-27 17:03:38 | Putupaula (Kalu Ganga) | 3.40 | 🟡 Alert | 0.020 | 🔺 Rising |
| 2026-10-27 17:02:57 | Panadugama (Nilwala Ganga) | 6.20 | 🟠 Minor Flood | -0.031 |  |
| 2026-10-27 17:02:56 | Ellagawa (Kalu Ganga) | 10.11 | 🟡 Alert | 0.030 | 🔺 Rising |
| 2026-10-27 17:02:46 | Deraniyagala (Kelani Ganga) | 1.24 | 🟢 Normal | -0.020 |  |
| 2026-10-27 17:02:38 | Hanwella (Kelani Ganga) | 5.50 | 🟢 Normal | -0.133 |  |
| 2026-10-27 17:02:37 | Wellawaya (Kirindi Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-10-27 17:02:32 | Moragaswewa (Deduru Oya) | 4.80 | 🟡 Alert | -0.083 |  |
| 2026-10-27 17:02:30 | Nawalapitiya (Mahaweli Ganga) | 1.69 | 🟢 Normal | -0.010 |  |
| 2026-10-27 17:02:30 | Rathnapura (Kalu Ganga) | 7.90 | 🟠 Minor Flood | -0.125 |  |
| 2026-10-27 17:02:23 | Thalgahagoda (Nilwala Ganga) | 1.61 | 🟡 Alert | -0.021 |  |
| 2026-10-27 17:02:11 | Manampitiya (Mahaweli Ganga) | 0.75 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-10-27 17:02:11 | Yaka Wewa (Ma Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-10-27 17:02:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.63 | 🟠 Minor Flood | 0.031 | 🔺 Rising |
| 2026-10-27 17:02:07 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | -0.010 |  |
| 2026-10-27 17:02:05 | Dunamale (Aththanagalu Oya) | 4.79 | 🟠 Minor Flood | -0.041 |  |
| 2026-10-27 17:02:04 | Weraganthota (Mahaweli Ganga) | -3.06 | 🟢 Normal | -0.080 |  |
| 2026-10-27 17:01:56 | Thanthirimale (Malwathu Oya) | 2.85 | 🟢 Normal | -0.160 |  |
| 2026-10-27 17:01:40 | Peradeniya (Mahaweli Ganga) | 3.30 | 🟢 Normal | -0.043 |  |
| 2026-10-27 17:01:40 | Thawalama (Gin Ganga) | 2.99 | 🟢 Normal | -0.043 |  |
| 2026-10-27 17:01:28 | Kithulgala (Kelani Ganga) | 2.34 | 🟢 Normal | 0.083 | 🔺 Rising |
| 2026-10-27 17:01:19 | Thanamalwila (Kirindi Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-10-27 17:01:07 | Horowpothana (Yan Oya) | 3.39 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-27 17:01:07 | Giriulla (Maha Oya) | 3.22 | 🟢 Normal | -0.094 |  |
| 2026-10-27 17:00:58 | Thaldena (Mahaweli Ganga) | 0.47 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-10-27 17:00:56 | Moraketiya (Walawe Ganga) | 1.45 | 🟢 Normal | -0.053 |  |
| 2026-10-27 17:00:40 | Magura (Kalu Ganga) | 4.88 | 🟡 Alert | -0.051 |  |
| 2026-10-27 17:00:10 | Siyambalanduwa (Heda Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-10-27 17:00:09 | Nakkala (Kumbukkan Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-10-27 16:59:53 | Siyambalanduwa (Heda Oya) | 0.54 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-27 17:02:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.63 | 🟠 Minor Flood | 0.031 | 🔺 Rising |
| 2026-10-27 17:07:00 | Baddegama (Gin Ganga) | 4.12 | 🟠 Minor Flood | 0.012 | 🔺 Rising |
| 2026-10-27 17:02:57 | Panadugama (Nilwala Ganga) | 6.20 | 🟠 Minor Flood | -0.031 |  |
| 2026-10-27 17:02:05 | Dunamale (Aththanagalu Oya) | 4.79 | 🟠 Minor Flood | -0.041 |  |
| 2026-10-27 17:02:30 | Rathnapura (Kalu Ganga) | 7.90 | 🟠 Minor Flood | -0.125 |  |
| 2026-10-27 17:02:56 | Ellagawa (Kalu Ganga) | 10.11 | 🟡 Alert | 0.030 | 🔺 Rising |
| 2026-10-27 17:03:38 | Putupaula (Kalu Ganga) | 3.40 | 🟡 Alert | 0.020 | 🔺 Rising |
| 2026-10-27 17:02:23 | Thalgahagoda (Nilwala Ganga) | 1.61 | 🟡 Alert | -0.021 |  |
| 2026-10-27 17:00:40 | Magura (Kalu Ganga) | 4.88 | 🟡 Alert | -0.051 |  |
| 2026-10-27 17:02:32 | Moragaswewa (Deduru Oya) | 4.80 | 🟡 Alert | -0.083 |  |
| 2026-10-27 17:01:28 | Kithulgala (Kelani Ganga) | 2.34 | 🟢 Normal | 0.083 | 🔺 Rising |
| 2026-10-27 17:00:58 | Thaldena (Mahaweli Ganga) | 0.47 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-10-27 17:02:11 | Manampitiya (Mahaweli Ganga) | 0.75 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-10-27 17:01:07 | Horowpothana (Yan Oya) | 3.39 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-27 17:02:37 | Wellawaya (Kirindi Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-10-27 17:00:09 | Nakkala (Kumbukkan Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-10-27 17:02:11 | Yaka Wewa (Ma Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-10-27 17:06:18 | Galgamuwa (Mee Oya) | 4.04 | 🟢 Normal | 0.000 |  |
| 2026-10-27 17:03:43 | Padiyathalawa (Maduru Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-10-27 17:04:08 | Nagalagam Street (Kelani Ganga) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-10-27 17:00:10 | Siyambalanduwa (Heda Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-10-27 17:01:19 | Thanamalwila (Kirindi Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-10-27 17:06:26 | Norwood (Kelani Ganga) | 1.34 | 🟢 Normal | -0.010 |  |
| 2026-10-27 17:02:07 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | -0.010 |  |
| 2026-10-27 17:02:30 | Nawalapitiya (Mahaweli Ganga) | 1.69 | 🟢 Normal | -0.010 |  |
| 2026-10-27 17:05:41 | Urawa (Nilwala Ganga) | 1.36 | 🟢 Normal | -0.019 |  |
| 2026-10-27 17:02:46 | Deraniyagala (Kelani Ganga) | 1.24 | 🟢 Normal | -0.020 |  |
| 2026-10-27 17:05:40 | Kuda Oya (Kirindi Oya) | 1.54 | 🟢 Normal | -0.025 |  |
| 2026-10-27 17:01:40 | Peradeniya (Mahaweli Ganga) | 3.30 | 🟢 Normal | -0.043 |  |
| 2026-10-27 17:01:40 | Thawalama (Gin Ganga) | 2.99 | 🟢 Normal | -0.043 |  |
| 2026-10-27 17:06:21 | Pitabeddara (Nilwala Ganga) | 2.27 | 🟢 Normal | -0.049 |  |
| 2026-10-27 17:00:56 | Moraketiya (Walawe Ganga) | 1.45 | 🟢 Normal | -0.053 |  |
| 2026-10-27 17:07:49 | Holombuwa (Kelani Ganga) | 1.44 | 🟢 Normal | -0.057 |  |
| 2026-10-27 17:05:01 | Badalgama (Maha Oya) | 4.35 | 🟢 Normal | -0.061 |  |
| 2026-10-27 17:02:04 | Weraganthota (Mahaweli Ganga) | -3.06 | 🟢 Normal | -0.080 |  |
| 2026-10-27 17:01:07 | Giriulla (Maha Oya) | 3.22 | 🟢 Normal | -0.094 |  |
| 2026-10-27 17:06:58 | Glencourse (Kelani Ganga) | 12.39 | 🟢 Normal | -0.121 |  |
| 2026-10-27 17:02:38 | Hanwella (Kelani Ganga) | 5.50 | 🟢 Normal | -0.133 |  |
| 2026-10-27 17:01:56 | Thanthirimale (Malwathu Oya) | 2.85 | 🟢 Normal | -0.160 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)