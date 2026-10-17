# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--18_04:02:42-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **290,922 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood; 🟠 Panadugama — Minor Flood; 🟡 Kalawellawa (Millakanda) — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **17** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-18 04:02:42 | Thalgahagoda (Nilwala Ganga) | 2.03 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-18 04:02:26 | Badalgama (Maha Oya) | 2.95 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-10-18 04:02:26 | Magura (Kalu Ganga) | 2.42 | 🟢 Normal | -0.010 |  |
| 2026-10-18 04:02:16 | Ellagawa (Kalu Ganga) | 7.60 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-10-18 04:02:08 | Deraniyagala (Kelani Ganga) | 0.96 | 🟢 Normal | -0.031 |  |
| 2026-10-18 04:01:56 | Kuda Oya (Kirindi Oya) | 1.35 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-10-18 04:01:30 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-10-18 04:01:28 | Thanamalwila (Kirindi Oya) | 1.09 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-10-18 04:01:25 | Nakkala (Kumbukkan Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-10-18 04:01:21 | Moraketiya (Walawe Ganga) | 1.52 | 🟢 Normal | -0.052 |  |
| 2026-10-18 04:01:09 | Padiyathalawa (Maduru Oya) | 1.28 | 🟢 Normal | -0.021 |  |
| 2026-10-18 04:00:57 | Thaldena (Mahaweli Ganga) | 0.73 | 🟢 Normal | -0.096 |  |
| 2026-10-18 04:00:52 | Manampitiya (Mahaweli Ganga) | 0.64 | 🟢 Normal | -0.145 |  |
| 2026-10-18 03:22:38 | Moragaswewa (Deduru Oya) | 1.16 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-10-18 03:22:27 | Horowpothana (Yan Oya) | 2.94 | 🟢 Normal | 108.000 | 🔺 Rising |
| 2026-10-18 03:22:26 | Horowpothana (Yan Oya) | 2.91 | 🟢 Normal | 108.000 | 🔺 Rising |
| 2026-10-18 03:22:25 | Horowpothana (Yan Oya) | 2.88 | 🟢 Normal | 108.000 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-18 04:02:42 | Thalgahagoda (Nilwala Ganga) | 2.03 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-18 03:07:04 | Panadugama (Nilwala Ganga) | 6.21 | 🟠 Minor Flood | -0.011 |  |
| 2026-10-18 03:10:41 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.40 | 🟡 Alert | -1.029 |  |
| 2026-10-18 03:22:27 | Horowpothana (Yan Oya) | 2.94 | 🟢 Normal | 108.000 | 🔺 Rising |
| 2026-10-18 03:17:25 | Kithulgala (Kelani Ganga) | 2.18 | 🟢 Normal | 0.278 | 🔺 Rising |
| 2026-10-18 03:05:01 | Hanwella (Kelani Ganga) | 4.51 | 🟢 Normal | 0.111 | 🔺 Rising |
| 2026-10-18 03:02:26 | Nagalagam Street (Kelani Ganga) | 0.79 | 🟢 Normal | 0.094 | 🔺 Rising |
| 2026-10-18 04:01:56 | Kuda Oya (Kirindi Oya) | 1.35 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-10-18 04:01:28 | Thanamalwila (Kirindi Oya) | 1.09 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-10-18 04:02:16 | Ellagawa (Kalu Ganga) | 7.60 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-10-18 03:05:58 | Giriulla (Maha Oya) | 2.94 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-10-18 04:02:26 | Badalgama (Maha Oya) | 2.95 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-10-18 03:22:38 | Moragaswewa (Deduru Oya) | 1.16 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-10-17 18:02:22 | Weraganthota (Mahaweli Ganga) | -3.16 | 🟢 Normal | 0.000 |  |
| 2026-10-18 04:01:25 | Nakkala (Kumbukkan Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-10-18 03:02:24 | Nawalapitiya (Mahaweli Ganga) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-10-18 03:07:14 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-10-18 03:05:44 | Baddegama (Gin Ganga) | 3.10 | 🟢 Normal | 0.000 |  |
| 2026-10-18 04:01:30 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-10-18 03:03:45 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-10-17 21:21:56 | Galgamuwa (Mee Oya) | 1.54 | 🟢 Normal | -0.009 |  |
| 2026-10-18 03:04:52 | Putupaula (Kalu Ganga) | 2.03 | 🟢 Normal | -0.010 |  |
| 2026-10-18 04:02:26 | Magura (Kalu Ganga) | 2.42 | 🟢 Normal | -0.010 |  |
| 2026-10-18 04:01:09 | Padiyathalawa (Maduru Oya) | 1.28 | 🟢 Normal | -0.021 |  |
| 2026-10-18 04:02:08 | Deraniyagala (Kelani Ganga) | 0.96 | 🟢 Normal | -0.031 |  |
| 2026-10-18 03:12:15 | Wellawaya (Kirindi Oya) | 1.36 | 🟢 Normal | -0.033 |  |
| 2026-10-18 03:16:36 | Norwood (Kelani Ganga) | 1.35 | 🟢 Normal | -0.034 |  |
| 2026-10-18 03:01:30 | Thawalama (Gin Ganga) | 3.96 | 🟢 Normal | -0.038 |  |
| 2026-10-17 18:01:56 | Thanthirimale (Malwathu Oya) | 2.41 | 🟢 Normal | -0.040 |  |
| 2026-10-18 02:09:12 | Urawa (Nilwala Ganga) | 1.75 | 🟢 Normal | -0.040 |  |
| 2026-10-18 04:01:21 | Moraketiya (Walawe Ganga) | 1.52 | 🟢 Normal | -0.052 |  |
| 2026-10-18 03:06:05 | Dunamale (Aththanagalu Oya) | 2.60 | 🟢 Normal | -0.060 |  |
| 2026-10-18 03:01:54 | Pitabeddara (Nilwala Ganga) | 2.98 | 🟢 Normal | -0.072 |  |
| 2026-10-18 03:06:52 | Holombuwa (Kelani Ganga) | 1.44 | 🟢 Normal | -0.088 |  |
| 2026-10-18 04:00:57 | Thaldena (Mahaweli Ganga) | 0.73 | 🟢 Normal | -0.096 |  |
| 2026-10-18 04:00:52 | Manampitiya (Mahaweli Ganga) | 0.64 | 🟢 Normal | -0.145 |  |
| 2026-10-18 03:06:29 | Glencourse (Kelani Ganga) | 12.80 | 🟢 Normal | -0.216 |  |
| 2026-10-18 03:15:21 | Rathnapura (Kalu Ganga) | 4.99 | 🟢 Normal | -0.303 |  |
| 2026-10-18 03:02:21 | Peradeniya (Mahaweli Ganga) | 3.82 | 🟢 Normal | -0.339 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)