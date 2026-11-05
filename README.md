# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--05_21:17:20-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **307,844 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **11** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-05 21:17:20 | Magura (Kalu Ganga) | 2.74 | 🟢 Normal | 126.000 | 🔺 Rising |
| 2026-11-05 21:17:18 | Magura (Kalu Ganga) | 2.67 | 🟢 Normal | 126.000 | 🔺 Rising |
| 2026-11-05 21:16:40 | Thawalama (Gin Ganga) | 2.09 | 🟢 Normal | -0.008 |  |
| 2026-11-05 21:14:12 | Thaldena (Mahaweli Ganga) | 0.38 | 🟢 Normal | -0.009 |  |
| 2026-11-05 21:13:53 | Ellagawa (Kalu Ganga) | 6.51 | 🟢 Normal | -0.057 |  |
| 2026-11-05 21:13:42 | Horowpothana (Yan Oya) | 2.20 | 🟢 Normal | 0.000 |  |
| 2026-11-05 21:10:40 | Baddegama (Gin Ganga) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-11-05 21:10:33 | Kithulgala (Kelani Ganga) | 1.84 | 🟢 Normal | -0.039 |  |
| 2026-11-05 21:09:47 | Thanamalwila (Kirindi Oya) | 1.93 | 🟢 Normal | -0.009 |  |
| 2026-11-05 21:09:46 | Kuda Oya (Kirindi Oya) | 2.16 | 🟢 Normal | 0.000 |  |
| 2026-11-05 21:08:16 | Padiyathalawa (Maduru Oya) | 0.37 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-05 21:17:20 | Magura (Kalu Ganga) | 2.74 | 🟢 Normal | 126.000 | 🔺 Rising |
| 2026-11-05 21:06:57 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.150 | 🔺 Rising |
| 2026-11-05 21:04:51 | Glencourse (Kelani Ganga) | 10.45 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-11-05 21:06:26 | Rathnapura (Kalu Ganga) | 2.73 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-11-05 21:03:19 | Giriulla (Maha Oya) | 2.10 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-11-05 21:04:10 | Dunamale (Aththanagalu Oya) | 2.49 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-05 21:04:08 | Nakkala (Kumbukkan Oya) | 0.80 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-05 21:02:16 | Wellawaya (Kirindi Oya) | 1.47 | 🟢 Normal | 0.000 |  |
| 2026-11-05 21:02:27 | Moragaswewa (Deduru Oya) | 3.26 | 🟢 Normal | 0.000 |  |
| 2026-11-05 21:02:16 | Nawalapitiya (Mahaweli Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-11-05 21:05:14 | Yaka Wewa (Ma Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-11-05 21:13:42 | Horowpothana (Yan Oya) | 2.20 | 🟢 Normal | 0.000 |  |
| 2026-11-05 18:03:39 | Galgamuwa (Mee Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-11-05 20:15:28 | Pitabeddara (Nilwala Ganga) | 1.44 | 🟢 Normal | 0.000 |  |
| 2026-11-05 21:05:19 | Hanwella (Kelani Ganga) | 2.30 | 🟢 Normal | 0.000 |  |
| 2026-11-05 21:04:52 | Deraniyagala (Kelani Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-11-05 21:10:40 | Baddegama (Gin Ganga) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-11-05 21:02:45 | Panadugama (Nilwala Ganga) | 4.26 | 🟢 Normal | 0.000 |  |
| 2026-11-05 21:08:16 | Padiyathalawa (Maduru Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-11-05 21:03:09 | Moraketiya (Walawe Ganga) | 1.76 | 🟢 Normal | 0.000 |  |
| 2026-11-05 21:03:57 | Katharagama (Menik Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-11-05 21:07:07 | Badalgama (Maha Oya) | 3.22 | 🟢 Normal | 0.000 |  |
| 2026-11-05 21:01:27 | Thalgahagoda (Nilwala Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-11-05 21:09:46 | Kuda Oya (Kirindi Oya) | 2.16 | 🟢 Normal | 0.000 |  |
| 2026-11-05 21:16:40 | Thawalama (Gin Ganga) | 2.09 | 🟢 Normal | -0.008 |  |
| 2026-11-05 21:14:12 | Thaldena (Mahaweli Ganga) | 0.38 | 🟢 Normal | -0.009 |  |
| 2026-11-05 21:09:47 | Thanamalwila (Kirindi Oya) | 1.93 | 🟢 Normal | -0.009 |  |
| 2026-11-05 21:01:26 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | -0.010 |  |
| 2026-11-05 21:07:11 | Urawa (Nilwala Ganga) | 1.03 | 🟢 Normal | -0.010 |  |
| 2026-11-05 21:06:28 | Putupaula (Kalu Ganga) | 1.32 | 🟢 Normal | -0.011 |  |
| 2026-11-05 18:01:46 | Thanthirimale (Malwathu Oya) | 1.84 | 🟢 Normal | -0.012 |  |
| 2026-11-05 21:04:41 | Norwood (Kelani Ganga) | 0.99 | 🟢 Normal | -0.019 |  |
| 2026-11-05 21:02:19 | Manampitiya (Mahaweli Ganga) | 0.91 | 🟢 Normal | -0.029 |  |
| 2026-11-05 21:04:22 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.80 | 🟢 Normal | -0.039 |  |
| 2026-11-05 21:10:33 | Kithulgala (Kelani Ganga) | 1.84 | 🟢 Normal | -0.039 |  |
| 2026-11-05 18:01:57 | Weraganthota (Mahaweli Ganga) | -3.00 | 🟢 Normal | -0.049 |  |
| 2026-11-05 21:13:53 | Ellagawa (Kalu Ganga) | 6.51 | 🟢 Normal | -0.057 |  |
| 2026-11-05 21:06:30 | Holombuwa (Kelani Ganga) | 1.18 | 🟢 Normal | -0.060 |  |
| 2026-11-05 21:02:47 | Peradeniya (Mahaweli Ganga) | 2.72 | 🟢 Normal | -39.130 |  |

## River Water Level Charts by Station

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)