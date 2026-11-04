# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--05_05:03:16-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **307,196 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Kalawellawa (Millakanda) — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **16** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-05 05:03:16 | Dunamale (Aththanagalu Oya) | 3.07 | 🟢 Normal | -0.020 |  |
| 2026-11-05 05:02:42 | Norwood (Kelani Ganga) | 1.01 | 🟢 Normal | -0.010 |  |
| 2026-11-05 05:02:39 | Horowpothana (Yan Oya) | 2.41 | 🟢 Normal | 0.000 |  |
| 2026-11-05 05:02:29 | Giriulla (Maha Oya) | 2.68 | 🟢 Normal | -0.101 |  |
| 2026-11-05 05:01:14 | Kuda Oya (Kirindi Oya) | 2.90 | 🟢 Normal | -0.200 |  |
| 2026-11-05 05:01:08 | Padiyathalawa (Maduru Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-11-05 05:00:55 | Manampitiya (Mahaweli Ganga) | 0.90 | 🟢 Normal | -0.030 |  |
| 2026-11-05 05:00:38 | Moraketiya (Walawe Ganga) | 2.12 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-11-05 05:00:13 | Wellawaya (Kirindi Oya) | 1.65 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-11-05 05:00:08 | Thalgahagoda (Nilwala Ganga) | 1.22 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-11-05 04:59:31 | Padiyathalawa (Maduru Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-11-05 04:39:06 | Thanamalwila (Kirindi Oya) | 2.52 | 🟢 Normal | -0.257 |  |
| 2026-11-05 04:36:22 | Horowpothana (Yan Oya) | 2.41 | 🟢 Normal | 0.000 |  |
| 2026-11-05 04:34:33 | Nawalapitiya (Mahaweli Ganga) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-11-05 04:28:58 | Moragaswewa (Deduru Oya) | 3.85 | 🟢 Normal | -0.048 |  |
| 2026-11-05 04:27:36 | Hanwella (Kelani Ganga) | 2.87 | 🟢 Normal | 0.030 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-05 04:01:24 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.17 | 🟡 Alert | -0.010 |  |
| 2026-11-05 04:06:40 | Rathnapura (Kalu Ganga) | 2.76 | 🟢 Normal | 0.875 | 🔺 Rising |
| 2026-11-05 04:06:10 | Badalgama (Maha Oya) | 3.78 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2026-11-05 04:05:56 | Panadugama (Nilwala Ganga) | 4.27 | 🟢 Normal | 0.067 | 🔺 Rising |
| 2026-11-05 05:00:13 | Wellawaya (Kirindi Oya) | 1.65 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-11-05 04:09:09 | Urawa (Nilwala Ganga) | 2.31 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-11-05 04:09:52 | Thawalama (Gin Ganga) | 2.32 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-11-05 01:07:28 | Pitabeddara (Nilwala Ganga) | 1.82 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-05 04:27:36 | Hanwella (Kelani Ganga) | 2.87 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-05 04:04:32 | Deraniyagala (Kelani Ganga) | 0.85 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-11-05 05:00:38 | Moraketiya (Walawe Ganga) | 2.12 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-11-05 05:00:08 | Thalgahagoda (Nilwala Ganga) | 1.22 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-11-05 03:31:15 | Putupaula (Kalu Ganga) | 1.45 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-11-05 02:06:12 | Magura (Kalu Ganga) | 2.67 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-05 04:01:45 | Nakkala (Kumbukkan Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-11-05 04:34:33 | Nawalapitiya (Mahaweli Ganga) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-11-05 04:17:14 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-05 05:02:39 | Horowpothana (Yan Oya) | 2.41 | 🟢 Normal | 0.000 |  |
| 2026-11-05 05:01:08 | Padiyathalawa (Maduru Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-11-05 04:05:52 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-11-04 18:00:12 | Thanthirimale (Malwathu Oya) | 1.48 | 🟢 Normal | 0.000 |  |
| 2026-11-05 04:01:59 | Peradeniya (Mahaweli Ganga) | 2.98 | 🟢 Normal | 0.000 |  |
| 2026-11-05 04:08:57 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | -0.009 |  |
| 2026-11-05 04:08:51 | Baddegama (Gin Ganga) | 2.09 | 🟢 Normal | -0.010 |  |
| 2026-11-05 05:02:42 | Norwood (Kelani Ganga) | 1.01 | 🟢 Normal | -0.010 |  |
| 2026-11-05 04:03:15 | Thaldena (Mahaweli Ganga) | 0.42 | 🟢 Normal | -0.020 |  |
| 2026-11-05 05:03:16 | Dunamale (Aththanagalu Oya) | 3.07 | 🟢 Normal | -0.020 |  |
| 2026-11-05 04:00:11 | Glencourse (Kelani Ganga) | 11.12 | 🟢 Normal | -0.020 |  |
| 2026-11-05 04:07:42 | Kithulgala (Kelani Ganga) | 2.05 | 🟢 Normal | -0.021 |  |
| 2026-11-04 18:02:29 | Galgamuwa (Mee Oya) | 0.85 | 🟢 Normal | -0.030 |  |
| 2026-11-05 05:00:55 | Manampitiya (Mahaweli Ganga) | 0.90 | 🟢 Normal | -0.030 |  |
| 2026-11-04 18:03:43 | Weraganthota (Mahaweli Ganga) | -3.06 | 🟢 Normal | -0.038 |  |
| 2026-11-05 04:28:58 | Moragaswewa (Deduru Oya) | 3.85 | 🟢 Normal | -0.048 |  |
| 2026-11-05 04:05:02 | Holombuwa (Kelani Ganga) | 1.12 | 🟢 Normal | -0.049 |  |
| 2026-11-05 04:03:13 | Ellagawa (Kalu Ganga) | 6.19 | 🟢 Normal | -0.063 |  |
| 2026-11-05 04:08:26 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.069 |  |
| 2026-11-05 05:02:29 | Giriulla (Maha Oya) | 2.68 | 🟢 Normal | -0.101 |  |
| 2026-11-05 05:01:14 | Kuda Oya (Kirindi Oya) | 2.90 | 🟢 Normal | -0.200 |  |
| 2026-11-05 04:39:06 | Thanamalwila (Kirindi Oya) | 2.52 | 🟢 Normal | -0.257 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)