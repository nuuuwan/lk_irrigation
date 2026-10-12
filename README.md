# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--12_07:23:37-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **285,641 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Kalawellawa (Millakanda) — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-12 07:23:37 | Panadugama (Nilwala Ganga) | 4.90 | 🟢 Normal | -0.032 |  |
| 2026-10-12 07:21:29 | Kithulgala (Kelani Ganga) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-10-12 07:13:06 | Baddegama (Gin Ganga) | 2.66 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-12 07:12:24 | Magura (Kalu Ganga) | 2.97 | 🟢 Normal | -0.026 |  |
| 2026-10-12 07:12:02 | Thanthirimale (Malwathu Oya) | 1.10 | 🟢 Normal | -0.002 |  |
| 2026-10-12 07:10:41 | Putupaula (Kalu Ganga) | 1.80 | 🟢 Normal | 0.512 | 🔺 Rising |
| 2026-10-12 07:10:00 | Badalgama (Maha Oya) | 3.78 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-10-12 07:09:47 | Deraniyagala (Kelani Ganga) | 0.78 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-10-12 07:09:40 | Glencourse (Kelani Ganga) | 11.50 | 🟢 Normal | -0.099 |  |
| 2026-10-12 07:09:31 | Peradeniya (Mahaweli Ganga) | 2.80 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-10-12 07:08:42 | Thawalama (Gin Ganga) | 2.72 | 🟢 Normal | -0.160 |  |
| 2026-10-12 07:08:10 | Thaldena (Mahaweli Ganga) | 0.49 | 🟢 Normal | -0.009 |  |
| 2026-10-12 07:06:04 | Pitabeddara (Nilwala Ganga) | 1.67 | 🟢 Normal | -0.029 |  |
| 2026-10-12 07:05:25 | Hanwella (Kelani Ganga) | 3.82 | 🟢 Normal | -0.052 |  |
| 2026-10-12 07:05:09 | Urawa (Nilwala Ganga) | 1.31 | 🟢 Normal | -0.031 |  |
| 2026-10-12 07:05:06 | Dunamale (Aththanagalu Oya) | 2.87 | 🟢 Normal | -0.010 |  |
| 2026-10-12 07:04:50 | Giriulla (Maha Oya) | 2.55 | 🟢 Normal | -0.097 |  |
| 2026-10-12 07:04:22 | Holombuwa (Kelani Ganga) | 1.10 | 🟢 Normal | -0.042 |  |
| 2026-10-12 07:03:23 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | -0.049 |  |
| 2026-10-12 07:03:22 | Rathnapura (Kalu Ganga) | 3.48 | 🟢 Normal | -0.139 |  |
| 2026-10-12 07:03:13 | Galgamuwa (Mee Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-10-12 07:03:02 | Wellawaya (Kirindi Oya) | 1.17 | 🟢 Normal | -0.010 |  |
| 2026-10-12 07:02:59 | Ellagawa (Kalu Ganga) | 7.26 | 🟢 Normal | -0.010 |  |
| 2026-10-12 07:02:39 | Kuda Oya (Kirindi Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-10-12 07:02:39 | Siyambalanduwa (Heda Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-10-12 07:02:33 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.10 | 🟡 Alert | 0.063 | 🔺 Rising |
| 2026-10-12 07:02:32 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.207 |  |
| 2026-10-12 07:02:08 | Nakkala (Kumbukkan Oya) | 0.90 | 🟢 Normal | -0.020 |  |
| 2026-10-12 07:01:50 | Moraketiya (Walawe Ganga) | 1.15 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-12 07:01:40 | Moragaswewa (Deduru Oya) | 1.10 | 🟢 Normal | -0.073 |  |
| 2026-10-12 07:01:28 | Thanamalwila (Kirindi Oya) | 1.21 | 🟢 Normal | -0.041 |  |
| 2026-10-12 07:01:19 | Norwood (Kelani Ganga) | 1.01 | 🟢 Normal | -0.011 |  |
| 2026-10-12 07:01:15 | Nawalapitiya (Mahaweli Ganga) | 1.22 | 🟢 Normal | -0.010 |  |
| 2026-10-12 07:01:13 | Weraganthota (Mahaweli Ganga) | -3.27 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-10-12 07:01:07 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-10-12 07:00:56 | Horowpothana (Yan Oya) | 1.61 | 🟢 Normal | 0.000 |  |
| 2026-10-12 07:00:56 | Manampitiya (Mahaweli Ganga) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-10-12 07:00:29 | Thalgahagoda (Nilwala Ganga) | 1.09 | 🟢 Normal | 0.047 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-12 07:02:33 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.10 | 🟡 Alert | 0.063 | 🔺 Rising |
| 2026-10-12 07:10:41 | Putupaula (Kalu Ganga) | 1.80 | 🟢 Normal | 0.512 | 🔺 Rising |
| 2026-10-12 07:00:29 | Thalgahagoda (Nilwala Ganga) | 1.09 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-10-12 07:09:47 | Deraniyagala (Kelani Ganga) | 0.78 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-10-12 07:01:13 | Weraganthota (Mahaweli Ganga) | -3.27 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-10-12 07:13:06 | Baddegama (Gin Ganga) | 2.66 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-12 07:01:50 | Moraketiya (Walawe Ganga) | 1.15 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-12 07:10:00 | Badalgama (Maha Oya) | 3.78 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-10-12 07:09:31 | Peradeniya (Mahaweli Ganga) | 2.80 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-10-12 07:21:29 | Kithulgala (Kelani Ganga) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-10-12 06:09:56 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-10-12 07:00:56 | Horowpothana (Yan Oya) | 1.61 | 🟢 Normal | 0.000 |  |
| 2026-10-12 07:03:13 | Galgamuwa (Mee Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-10-12 07:01:07 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-10-12 07:02:39 | Siyambalanduwa (Heda Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-10-12 07:00:56 | Manampitiya (Mahaweli Ganga) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-10-12 07:02:39 | Kuda Oya (Kirindi Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-10-12 07:12:02 | Thanthirimale (Malwathu Oya) | 1.10 | 🟢 Normal | -0.002 |  |
| 2026-10-12 07:08:10 | Thaldena (Mahaweli Ganga) | 0.49 | 🟢 Normal | -0.009 |  |
| 2026-10-12 07:05:06 | Dunamale (Aththanagalu Oya) | 2.87 | 🟢 Normal | -0.010 |  |
| 2026-10-12 07:02:59 | Ellagawa (Kalu Ganga) | 7.26 | 🟢 Normal | -0.010 |  |
| 2026-10-12 07:03:02 | Wellawaya (Kirindi Oya) | 1.17 | 🟢 Normal | -0.010 |  |
| 2026-10-12 07:01:15 | Nawalapitiya (Mahaweli Ganga) | 1.22 | 🟢 Normal | -0.010 |  |
| 2026-10-12 07:01:19 | Norwood (Kelani Ganga) | 1.01 | 🟢 Normal | -0.011 |  |
| 2026-10-12 07:02:08 | Nakkala (Kumbukkan Oya) | 0.90 | 🟢 Normal | -0.020 |  |
| 2026-10-12 07:12:24 | Magura (Kalu Ganga) | 2.97 | 🟢 Normal | -0.026 |  |
| 2026-10-12 07:06:04 | Pitabeddara (Nilwala Ganga) | 1.67 | 🟢 Normal | -0.029 |  |
| 2026-10-12 07:05:09 | Urawa (Nilwala Ganga) | 1.31 | 🟢 Normal | -0.031 |  |
| 2026-10-12 07:23:37 | Panadugama (Nilwala Ganga) | 4.90 | 🟢 Normal | -0.032 |  |
| 2026-10-12 07:01:28 | Thanamalwila (Kirindi Oya) | 1.21 | 🟢 Normal | -0.041 |  |
| 2026-10-12 07:04:22 | Holombuwa (Kelani Ganga) | 1.10 | 🟢 Normal | -0.042 |  |
| 2026-10-12 07:03:23 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | -0.049 |  |
| 2026-10-12 07:05:25 | Hanwella (Kelani Ganga) | 3.82 | 🟢 Normal | -0.052 |  |
| 2026-10-12 07:01:40 | Moragaswewa (Deduru Oya) | 1.10 | 🟢 Normal | -0.073 |  |
| 2026-10-12 07:04:50 | Giriulla (Maha Oya) | 2.55 | 🟢 Normal | -0.097 |  |
| 2026-10-12 07:09:40 | Glencourse (Kelani Ganga) | 11.50 | 🟢 Normal | -0.099 |  |
| 2026-10-12 07:03:22 | Rathnapura (Kalu Ganga) | 3.48 | 🟢 Normal | -0.139 |  |
| 2026-10-12 07:08:42 | Thawalama (Gin Ganga) | 2.72 | 🟢 Normal | -0.160 |  |
| 2026-10-12 07:02:32 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.207 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)