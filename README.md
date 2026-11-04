# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--04_18:04:00-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **306,831 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Kalawellawa (Millakanda) — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **31** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-04 18:04:00 | Holombuwa (Kelani Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-11-04 18:03:58 | Deraniyagala (Kelani Ganga) | 1.14 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2026-11-04 18:03:48 | Norwood (Kelani Ganga) | 1.14 | 🟢 Normal | -0.078 |  |
| 2026-11-04 18:03:46 | Padiyathalawa (Maduru Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-11-04 18:03:43 | Weraganthota (Mahaweli Ganga) | -3.06 | 🟢 Normal | -0.038 |  |
| 2026-11-04 18:03:39 | Thanamalwila (Kirindi Oya) | 1.49 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-11-04 18:03:18 | Pitabeddara (Nilwala Ganga) | 1.73 | 🟢 Normal | -0.022 |  |
| 2026-11-04 18:03:12 | Magura (Kalu Ganga) | 2.48 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-11-04 18:03:11 | Nawalapitiya (Mahaweli Ganga) | 1.38 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-04 18:03:10 | Hanwella (Kelani Ganga) | 2.43 | 🟢 Normal | -0.073 |  |
| 2026-11-04 18:03:09 | Thawalama (Gin Ganga) | 2.20 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-11-04 18:03:06 | Moraketiya (Walawe Ganga) | 2.12 | 🟢 Normal | 0.000 |  |
| 2026-11-04 18:02:52 | Nakkala (Kumbukkan Oya) | 0.83 | 🟢 Normal | -0.010 |  |
| 2026-11-04 18:02:49 | Siyambalanduwa (Heda Oya) | 0.52 | 🟢 Normal | -0.010 |  |
| 2026-11-04 18:02:43 | Baddegama (Gin Ganga) | 2.31 | 🟢 Normal | -0.031 |  |
| 2026-11-04 18:02:40 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.08 | 🟡 Alert | 0.030 | 🔺 Rising |
| 2026-11-04 18:02:32 | Glencourse (Kelani Ganga) | 10.26 | 🟢 Normal | -0.054 |  |
| 2026-11-04 18:02:29 | Galgamuwa (Mee Oya) | 0.85 | 🟢 Normal | -0.030 |  |
| 2026-11-04 18:02:16 | Badalgama (Maha Oya) | 3.55 | 🟢 Normal | -0.064 |  |
| 2026-11-04 18:02:08 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-04 18:01:55 | Peradeniya (Mahaweli Ganga) | 3.05 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2026-11-04 18:01:39 | Giriulla (Maha Oya) | 2.35 | 🟢 Normal | -0.071 |  |
| 2026-11-04 18:01:27 | Thaldena (Mahaweli Ganga) | 0.40 | 🟢 Normal | -0.082 |  |
| 2026-11-04 18:01:12 | Kuda Oya (Kirindi Oya) | 1.55 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-04 18:00:57 | Rathnapura (Kalu Ganga) | 2.57 | 🟢 Normal | -0.061 |  |
| 2026-11-04 18:00:38 | Putupaula (Kalu Ganga) | 1.40 | 🟢 Normal | -0.021 |  |
| 2026-11-04 18:00:33 | Horowpothana (Yan Oya) | 2.45 | 🟢 Normal | -0.021 |  |
| 2026-11-04 18:00:31 | Manampitiya (Mahaweli Ganga) | 1.17 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-04 18:00:25 | Thalgahagoda (Nilwala Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-11-04 18:00:24 | Wellawaya (Kirindi Oya) | 1.59 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-04 18:00:12 | Thanthirimale (Malwathu Oya) | 1.48 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-04 18:02:40 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.08 | 🟡 Alert | 0.030 | 🔺 Rising |
| 2026-11-04 17:06:26 | Urawa (Nilwala Ganga) | 1.30 | 🟢 Normal | 0.191 | 🔺 Rising |
| 2026-11-04 18:03:58 | Deraniyagala (Kelani Ganga) | 1.14 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2026-11-04 18:01:55 | Peradeniya (Mahaweli Ganga) | 3.05 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2026-11-04 17:08:30 | Kithulgala (Kelani Ganga) | 1.93 | 🟢 Normal | 0.067 | 🔺 Rising |
| 2026-11-04 18:03:12 | Magura (Kalu Ganga) | 2.48 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-11-04 18:03:09 | Thawalama (Gin Ganga) | 2.20 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-11-04 18:03:39 | Thanamalwila (Kirindi Oya) | 1.49 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-11-04 18:00:31 | Manampitiya (Mahaweli Ganga) | 1.17 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-04 18:00:24 | Wellawaya (Kirindi Oya) | 1.59 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-04 17:03:08 | Ellagawa (Kalu Ganga) | 6.72 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-04 18:01:12 | Kuda Oya (Kirindi Oya) | 1.55 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-04 18:03:11 | Nawalapitiya (Mahaweli Ganga) | 1.38 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-04 18:02:08 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-04 18:03:46 | Padiyathalawa (Maduru Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-11-04 17:05:43 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-11-04 18:03:06 | Moraketiya (Walawe Ganga) | 2.12 | 🟢 Normal | 0.000 |  |
| 2026-11-04 17:08:02 | Katharagama (Menik Ganga) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-11-04 18:04:00 | Holombuwa (Kelani Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-11-04 18:00:12 | Thanthirimale (Malwathu Oya) | 1.48 | 🟢 Normal | 0.000 |  |
| 2026-11-04 18:00:25 | Thalgahagoda (Nilwala Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-11-04 18:02:49 | Siyambalanduwa (Heda Oya) | 0.52 | 🟢 Normal | -0.010 |  |
| 2026-11-04 18:02:52 | Nakkala (Kumbukkan Oya) | 0.83 | 🟢 Normal | -0.010 |  |
| 2026-11-04 18:00:33 | Horowpothana (Yan Oya) | 2.45 | 🟢 Normal | -0.021 |  |
| 2026-11-04 17:06:27 | Panadugama (Nilwala Ganga) | 4.25 | 🟢 Normal | -0.021 |  |
| 2026-11-04 18:00:38 | Putupaula (Kalu Ganga) | 1.40 | 🟢 Normal | -0.021 |  |
| 2026-11-04 18:03:18 | Pitabeddara (Nilwala Ganga) | 1.73 | 🟢 Normal | -0.022 |  |
| 2026-11-04 17:02:36 | Moragaswewa (Deduru Oya) | 4.32 | 🟢 Normal | -0.022 |  |
| 2026-11-04 18:02:29 | Galgamuwa (Mee Oya) | 0.85 | 🟢 Normal | -0.030 |  |
| 2026-11-04 18:02:43 | Baddegama (Gin Ganga) | 2.31 | 🟢 Normal | -0.031 |  |
| 2026-11-04 18:03:43 | Weraganthota (Mahaweli Ganga) | -3.06 | 🟢 Normal | -0.038 |  |
| 2026-11-04 18:02:32 | Glencourse (Kelani Ganga) | 10.26 | 🟢 Normal | -0.054 |  |
| 2026-11-04 18:00:57 | Rathnapura (Kalu Ganga) | 2.57 | 🟢 Normal | -0.061 |  |
| 2026-11-04 17:10:32 | Dunamale (Aththanagalu Oya) | 2.20 | 🟢 Normal | -0.062 |  |
| 2026-11-04 18:02:16 | Badalgama (Maha Oya) | 3.55 | 🟢 Normal | -0.064 |  |
| 2026-11-04 18:01:39 | Giriulla (Maha Oya) | 2.35 | 🟢 Normal | -0.071 |  |
| 2026-11-04 18:03:10 | Hanwella (Kelani Ganga) | 2.43 | 🟢 Normal | -0.073 |  |
| 2026-11-04 18:03:48 | Norwood (Kelani Ganga) | 1.14 | 🟢 Normal | -0.078 |  |
| 2026-11-04 18:01:27 | Thaldena (Mahaweli Ganga) | 0.40 | 🟢 Normal | -0.082 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)