# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--28_12:11:43-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **273,244 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Thalgahagoda — Alert; 🟡 Baddegama — Alert; 🟡 Kalawellawa (Millakanda) — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-28 12:11:43 | Baddegama (Gin Ganga) | 3.97 | 🟡 Alert | -0.062 |  |
| 2026-09-28 12:08:40 | Thalgahagoda (Nilwala Ganga) | 1.62 | 🟡 Alert | -0.022 |  |
| 2026-09-28 12:08:08 | Holombuwa (Kelani Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-09-28 12:07:40 | Panadugama (Nilwala Ganga) | 4.56 | 🟢 Normal | 0.000 |  |
| 2026-09-28 12:07:16 | Thanamalwila (Kirindi Oya) | 1.12 | 🟢 Normal | -36.000 |  |
| 2026-09-28 12:07:15 | Thanamalwila (Kirindi Oya) | 1.13 | 🟢 Normal | -36.000 |  |
| 2026-09-28 12:07:11 | Rathnapura (Kalu Ganga) | 2.18 | 🟢 Normal | -0.028 |  |
| 2026-09-28 12:06:35 | Deraniyagala (Kelani Ganga) | 1.08 | 🟢 Normal | -0.056 |  |
| 2026-09-28 12:06:06 | Hanwella (Kelani Ganga) | 3.27 | 🟢 Normal | -0.029 |  |
| 2026-09-28 12:05:41 | Glencourse (Kelani Ganga) | 11.27 | 🟢 Normal | -0.010 |  |
| 2026-09-28 12:05:30 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.096 | 🔺 Rising |
| 2026-09-28 12:05:26 | Katharagama (Menik Ganga) | -0.28 | 🟢 Normal | 0.000 |  |
| 2026-09-28 12:05:13 | Horowpothana (Yan Oya) | 1.63 | 🟢 Normal | 0.000 |  |
| 2026-09-28 12:04:33 | Ellagawa (Kalu Ganga) | 6.32 | 🟢 Normal | -0.078 |  |
| 2026-09-28 12:04:28 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.00 | 🟡 Alert | -0.100 |  |
| 2026-09-28 12:04:21 | Moraketiya (Walawe Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-09-28 12:04:07 | Thawalama (Gin Ganga) | 2.23 | 🟢 Normal | -0.021 |  |
| 2026-09-28 12:04:06 | Panadugama (Nilwala Ganga) | 4.56 | 🟢 Normal | 0.000 |  |
| 2026-09-28 12:04:00 | Wellawaya (Kirindi Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-09-28 12:03:42 | Norwood (Kelani Ganga) | 0.87 | 🟢 Normal | -0.010 |  |
| 2026-09-28 12:03:39 | Giriulla (Maha Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-09-28 12:03:30 | Katharagama (Menik Ganga) | -0.28 | 🟢 Normal | 0.000 |  |
| 2026-09-28 12:03:29 | Urawa (Nilwala Ganga) | 0.62 | 🟢 Normal | -0.011 |  |
| 2026-09-28 12:03:11 | Magura (Kalu Ganga) | 2.20 | 🟢 Normal | -0.023 |  |
| 2026-09-28 12:03:09 | Kuda Oya (Kirindi Oya) | 0.90 | 🟢 Normal | -18.000 |  |
| 2026-09-28 12:03:07 | Kuda Oya (Kirindi Oya) | 0.91 | 🟢 Normal | -18.000 |  |
| 2026-09-28 12:03:04 | Thaldena (Mahaweli Ganga) | 0.08 | 🟢 Normal | -0.049 |  |
| 2026-09-28 12:03:04 | Dunamale (Aththanagalu Oya) | 1.93 | 🟢 Normal | -0.010 |  |
| 2026-09-28 12:02:52 | Pitabeddara (Nilwala Ganga) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-09-28 12:02:43 | Badalgama (Maha Oya) | 2.35 | 🟢 Normal | -0.010 |  |
| 2026-09-28 12:02:36 | Kithulgala (Kelani Ganga) | 2.18 | 🟢 Normal | -0.147 |  |
| 2026-09-28 12:02:32 | Manampitiya (Mahaweli Ganga) | -0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-28 12:02:26 | Nawalapitiya (Mahaweli Ganga) | 1.74 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-28 12:02:22 | Nakkala (Kumbukkan Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-09-28 12:02:18 | Siyambalanduwa (Heda Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-09-28 12:02:14 | Putupaula (Kalu Ganga) | 1.91 | 🟢 Normal | -0.053 |  |
| 2026-09-28 12:02:08 | Galgamuwa (Mee Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-09-28 12:01:50 | Weraganthota (Mahaweli Ganga) | -3.36 | 🟢 Normal | -0.020 |  |
| 2026-09-28 12:01:49 | Thanthirimale (Malwathu Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-09-28 12:01:10 | Peradeniya (Mahaweli Ganga) | 2.39 | 🟢 Normal | -0.332 |  |
| 2026-09-28 12:00:39 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-28 12:08:40 | Thalgahagoda (Nilwala Ganga) | 1.62 | 🟡 Alert | -0.022 |  |
| 2026-09-28 12:11:43 | Baddegama (Gin Ganga) | 3.97 | 🟡 Alert | -0.062 |  |
| 2026-09-28 12:04:28 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.00 | 🟡 Alert | -0.100 |  |
| 2026-09-28 12:05:30 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.096 | 🔺 Rising |
| 2026-09-28 12:02:26 | Nawalapitiya (Mahaweli Ganga) | 1.74 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-28 12:04:00 | Wellawaya (Kirindi Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-09-28 12:02:22 | Nakkala (Kumbukkan Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-09-28 11:03:52 | Moragaswewa (Deduru Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-09-28 12:00:39 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-28 12:03:39 | Giriulla (Maha Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-09-28 12:05:13 | Horowpothana (Yan Oya) | 1.63 | 🟢 Normal | 0.000 |  |
| 2026-09-28 12:02:08 | Galgamuwa (Mee Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-09-28 12:02:52 | Pitabeddara (Nilwala Ganga) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-09-28 12:07:40 | Panadugama (Nilwala Ganga) | 4.56 | 🟢 Normal | 0.000 |  |
| 2026-09-28 11:00:21 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-09-28 12:04:21 | Moraketiya (Walawe Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-09-28 12:02:18 | Siyambalanduwa (Heda Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-09-28 12:05:26 | Katharagama (Menik Ganga) | -0.28 | 🟢 Normal | 0.000 |  |
| 2026-09-28 12:08:08 | Holombuwa (Kelani Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-09-28 12:02:32 | Manampitiya (Mahaweli Ganga) | -0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-28 12:01:49 | Thanthirimale (Malwathu Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-09-28 12:03:42 | Norwood (Kelani Ganga) | 0.87 | 🟢 Normal | -0.010 |  |
| 2026-09-28 12:03:04 | Dunamale (Aththanagalu Oya) | 1.93 | 🟢 Normal | -0.010 |  |
| 2026-09-28 12:05:41 | Glencourse (Kelani Ganga) | 11.27 | 🟢 Normal | -0.010 |  |
| 2026-09-28 12:02:43 | Badalgama (Maha Oya) | 2.35 | 🟢 Normal | -0.010 |  |
| 2026-09-28 12:03:29 | Urawa (Nilwala Ganga) | 0.62 | 🟢 Normal | -0.011 |  |
| 2026-09-28 12:01:50 | Weraganthota (Mahaweli Ganga) | -3.36 | 🟢 Normal | -0.020 |  |
| 2026-09-28 12:04:07 | Thawalama (Gin Ganga) | 2.23 | 🟢 Normal | -0.021 |  |
| 2026-09-28 12:03:11 | Magura (Kalu Ganga) | 2.20 | 🟢 Normal | -0.023 |  |
| 2026-09-28 12:07:11 | Rathnapura (Kalu Ganga) | 2.18 | 🟢 Normal | -0.028 |  |
| 2026-09-28 12:06:06 | Hanwella (Kelani Ganga) | 3.27 | 🟢 Normal | -0.029 |  |
| 2026-09-28 12:03:04 | Thaldena (Mahaweli Ganga) | 0.08 | 🟢 Normal | -0.049 |  |
| 2026-09-28 12:02:14 | Putupaula (Kalu Ganga) | 1.91 | 🟢 Normal | -0.053 |  |
| 2026-09-28 12:06:35 | Deraniyagala (Kelani Ganga) | 1.08 | 🟢 Normal | -0.056 |  |
| 2026-09-28 12:04:33 | Ellagawa (Kalu Ganga) | 6.32 | 🟢 Normal | -0.078 |  |
| 2026-09-28 12:02:36 | Kithulgala (Kelani Ganga) | 2.18 | 🟢 Normal | -0.147 |  |
| 2026-09-28 12:01:10 | Peradeniya (Mahaweli Ganga) | 2.39 | 🟢 Normal | -0.332 |  |
| 2026-09-28 12:03:09 | Kuda Oya (Kirindi Oya) | 0.90 | 🟢 Normal | -18.000 |  |
| 2026-09-28 12:07:16 | Thanamalwila (Kirindi Oya) | 1.12 | 🟢 Normal | -36.000 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)