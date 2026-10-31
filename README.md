# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--31_22:03:00-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **303,322 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Thalgahagoda — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **11** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-31 22:03:00 | Putupaula (Kalu Ganga) | 1.62 | 🟢 Normal | -0.051 |  |
| 2026-10-31 22:02:59 | Ellagawa (Kalu Ganga) | 6.00 | 🟢 Normal | -0.050 |  |
| 2026-10-31 22:02:55 | Kuda Oya (Kirindi Oya) | 1.50 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-10-31 22:02:53 | Giriulla (Maha Oya) | 1.46 | 🟢 Normal | -0.021 |  |
| 2026-10-31 22:02:21 | Thawalama (Gin Ganga) | 2.05 | 🟢 Normal | -0.010 |  |
| 2026-10-31 22:02:18 | Dunamale (Aththanagalu Oya) | 1.85 | 🟢 Normal | -0.010 |  |
| 2026-10-31 22:01:35 | Siyambalanduwa (Heda Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-10-31 22:01:26 | Nakkala (Kumbukkan Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-10-31 22:01:08 | Nawalapitiya (Mahaweli Ganga) | 1.23 | 🟢 Normal | -0.010 |  |
| 2026-10-31 22:00:49 | Pitabeddara (Nilwala Ganga) | 1.42 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-31 22:00:40 | Wellawaya (Kirindi Oya) | 1.19 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-31 21:02:09 | Thalgahagoda (Nilwala Ganga) | 1.55 | 🟡 Alert | 0.000 |  |
| 2026-10-31 21:07:44 | Thanamalwila (Kirindi Oya) | 1.53 | 🟢 Normal | 0.163 | 🔺 Rising |
| 2026-10-31 21:02:11 | Kithulgala (Kelani Ganga) | 1.98 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-10-31 22:02:55 | Kuda Oya (Kirindi Oya) | 1.50 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-10-31 22:00:49 | Pitabeddara (Nilwala Ganga) | 1.42 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-31 21:03:55 | Moraketiya (Walawe Ganga) | 1.15 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-31 21:03:15 | Peradeniya (Mahaweli Ganga) | 2.74 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-31 21:04:31 | Manampitiya (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-31 22:00:40 | Wellawaya (Kirindi Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-10-31 22:01:26 | Nakkala (Kumbukkan Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-10-31 21:01:36 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-10-31 21:15:00 | Horowpothana (Yan Oya) | 2.28 | 🟢 Normal | 0.000 |  |
| 2026-10-31 21:03:34 | Norwood (Kelani Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-10-31 21:03:38 | Padiyathalawa (Maduru Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-10-31 22:01:35 | Siyambalanduwa (Heda Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-10-31 21:04:43 | Holombuwa (Kelani Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-10-31 21:16:46 | Rathnapura (Kalu Ganga) | 2.01 | 🟢 Normal | 0.000 |  |
| 2026-10-31 21:03:26 | Urawa (Nilwala Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-10-31 21:03:32 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | -0.010 |  |
| 2026-10-31 18:00:38 | Thanthirimale (Malwathu Oya) | 1.29 | 🟢 Normal | -0.010 |  |
| 2026-10-31 22:02:18 | Dunamale (Aththanagalu Oya) | 1.85 | 🟢 Normal | -0.010 |  |
| 2026-10-31 21:05:25 | Badalgama (Maha Oya) | 2.82 | 🟢 Normal | -0.010 |  |
| 2026-10-31 21:03:22 | Moragaswewa (Deduru Oya) | 1.03 | 🟢 Normal | -0.010 |  |
| 2026-10-31 22:01:08 | Nawalapitiya (Mahaweli Ganga) | 1.23 | 🟢 Normal | -0.010 |  |
| 2026-10-31 22:02:21 | Thawalama (Gin Ganga) | 2.05 | 🟢 Normal | -0.010 |  |
| 2026-10-31 18:01:51 | Galgamuwa (Mee Oya) | 1.09 | 🟢 Normal | -0.011 |  |
| 2026-10-31 18:04:44 | Weraganthota (Mahaweli Ganga) | -3.15 | 🟢 Normal | -0.020 |  |
| 2026-10-31 22:02:53 | Giriulla (Maha Oya) | 1.46 | 🟢 Normal | -0.021 |  |
| 2026-10-31 21:01:39 | Magura (Kalu Ganga) | 1.98 | 🟢 Normal | -0.025 |  |
| 2026-10-31 21:05:26 | Panadugama (Nilwala Ganga) | 4.45 | 🟢 Normal | -0.029 |  |
| 2026-10-31 21:05:01 | Baddegama (Gin Ganga) | 2.32 | 🟢 Normal | -0.033 |  |
| 2026-10-31 21:04:42 | Glencourse (Kelani Ganga) | 10.20 | 🟢 Normal | -0.039 |  |
| 2026-10-31 21:02:52 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.28 | 🟢 Normal | -0.042 |  |
| 2026-10-31 21:04:08 | Thaldena (Mahaweli Ganga) | 0.33 | 🟢 Normal | -0.047 |  |
| 2026-10-31 22:02:59 | Ellagawa (Kalu Ganga) | 6.00 | 🟢 Normal | -0.050 |  |
| 2026-10-31 22:03:00 | Putupaula (Kalu Ganga) | 1.62 | 🟢 Normal | -0.051 |  |
| 2026-10-31 21:05:08 | Hanwella (Kelani Ganga) | 2.37 | 🟢 Normal | -0.054 |  |
| 2026-10-31 21:02:26 | Deraniyagala (Kelani Ganga) | 0.70 | 🟢 Normal | -0.063 |  |
| 2026-10-31 21:03:27 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.063 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)