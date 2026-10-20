# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--20_12:37:43-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **293,068 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Thalgahagoda — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-20 12:37:43 | Norwood (Kelani Ganga) | 1.07 | 🟢 Normal | -0.006 |  |
| 2026-10-20 12:14:45 | Glencourse (Kelani Ganga) | 10.89 | 🟢 Normal | 0.000 |  |
| 2026-10-20 12:10:58 | Moragaswewa (Deduru Oya) | 1.11 | 🟢 Normal | -0.009 |  |
| 2026-10-20 12:10:52 | Kithulgala (Kelani Ganga) | 2.04 | 🟢 Normal | -0.075 |  |
| 2026-10-20 12:08:27 | Moraketiya (Walawe Ganga) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-10-20 12:07:47 | Urawa (Nilwala Ganga) | 0.85 | 🟢 Normal | -0.011 |  |
| 2026-10-20 12:07:36 | Magura (Kalu Ganga) | 1.80 | 🟢 Normal | -0.009 |  |
| 2026-10-20 12:07:01 | Thalgahagoda (Nilwala Ganga) | 1.67 | 🟡 Alert | -0.009 |  |
| 2026-10-20 12:05:41 | Galgamuwa (Mee Oya) | 0.61 | 🟢 Normal | -0.010 |  |
| 2026-10-20 12:05:04 | Rathnapura (Kalu Ganga) | 2.23 | 🟢 Normal | -0.045 |  |
| 2026-10-20 12:05:03 | Thawalama (Gin Ganga) | 2.16 | 🟢 Normal | -0.010 |  |
| 2026-10-20 12:04:36 | Nakkala (Kumbukkan Oya) | 0.93 | 🟢 Normal | -0.047 |  |
| 2026-10-20 12:04:33 | Badalgama (Maha Oya) | 2.62 | 🟢 Normal | 0.000 |  |
| 2026-10-20 12:03:55 | Putupaula (Kalu Ganga) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-10-20 12:03:47 | Holombuwa (Kelani Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-10-20 12:03:44 | Horowpothana (Yan Oya) | 2.14 | 🟢 Normal | -0.020 |  |
| 2026-10-20 12:03:44 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.23 | 🟢 Normal | -0.063 |  |
| 2026-10-20 12:03:13 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-10-20 12:02:59 | Panadugama (Nilwala Ganga) | 4.57 | 🟢 Normal | -0.020 |  |
| 2026-10-20 12:02:59 | Baddegama (Gin Ganga) | 1.94 | 🟢 Normal | -0.021 |  |
| 2026-10-20 12:02:43 | Padiyathalawa (Maduru Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-10-20 12:02:42 | Giriulla (Maha Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-10-20 12:02:38 | Glencourse (Kelani Ganga) | 10.89 | 🟢 Normal | 0.000 |  |
| 2026-10-20 12:02:34 | Thanamalwila (Kirindi Oya) | 1.30 | 🟢 Normal | -0.720 |  |
| 2026-10-20 12:02:26 | Hanwella (Kelani Ganga) | 2.82 | 🟢 Normal | -0.041 |  |
| 2026-10-20 12:02:25 | Wellawaya (Kirindi Oya) | 1.31 | 🟢 Normal | -0.020 |  |
| 2026-10-20 12:02:14 | Deraniyagala (Kelani Ganga) | 0.96 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-10-20 12:01:52 | Manampitiya (Mahaweli Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-10-20 12:01:52 | Thaldena (Mahaweli Ganga) | 0.31 | 🟢 Normal | -0.010 |  |
| 2026-10-20 12:01:42 | Thanthirimale (Malwathu Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-10-20 12:01:37 | Dunamale (Aththanagalu Oya) | 1.92 | 🟢 Normal | -0.020 |  |
| 2026-10-20 12:01:36 | Pitabeddara (Nilwala Ganga) | 1.48 | 🟢 Normal | -0.010 |  |
| 2026-10-20 12:01:36 | Weraganthota (Mahaweli Ganga) | -2.52 | 🟢 Normal | -0.012 |  |
| 2026-10-20 12:01:36 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-10-20 12:01:29 | Ellagawa (Kalu Ganga) | 6.27 | 🟢 Normal | -0.051 |  |
| 2026-10-20 12:01:22 | Peradeniya (Mahaweli Ganga) | 2.79 | 🟢 Normal | 0.000 |  |
| 2026-10-20 12:01:05 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | -0.015 |  |
| 2026-10-20 12:01:00 | Nawalapitiya (Mahaweli Ganga) | 1.23 | 🟢 Normal | -0.010 |  |
| 2026-10-20 12:00:54 | Thanamalwila (Kirindi Oya) | 1.32 | 🟢 Normal | -0.720 |  |
| 2026-10-20 12:00:53 | Siyambalanduwa (Heda Oya) | 0.58 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-20 12:07:01 | Thalgahagoda (Nilwala Ganga) | 1.67 | 🟡 Alert | -0.009 |  |
| 2026-10-20 12:02:14 | Deraniyagala (Kelani Ganga) | 0.96 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-10-20 12:01:36 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-10-20 12:02:42 | Giriulla (Maha Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-10-20 12:02:43 | Padiyathalawa (Maduru Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-10-20 12:14:45 | Glencourse (Kelani Ganga) | 10.89 | 🟢 Normal | 0.000 |  |
| 2026-10-20 12:08:27 | Moraketiya (Walawe Ganga) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-10-20 12:03:13 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-10-20 12:03:55 | Putupaula (Kalu Ganga) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-10-20 12:04:33 | Badalgama (Maha Oya) | 2.62 | 🟢 Normal | 0.000 |  |
| 2026-10-20 12:03:47 | Holombuwa (Kelani Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-10-20 12:01:52 | Manampitiya (Mahaweli Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-10-20 12:01:42 | Thanthirimale (Malwathu Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-10-20 12:01:22 | Peradeniya (Mahaweli Ganga) | 2.79 | 🟢 Normal | 0.000 |  |
| 2026-10-20 11:05:02 | Kuda Oya (Kirindi Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-10-20 12:37:43 | Norwood (Kelani Ganga) | 1.07 | 🟢 Normal | -0.006 |  |
| 2026-10-20 12:10:58 | Moragaswewa (Deduru Oya) | 1.11 | 🟢 Normal | -0.009 |  |
| 2026-10-20 12:07:36 | Magura (Kalu Ganga) | 1.80 | 🟢 Normal | -0.009 |  |
| 2026-10-20 12:05:41 | Galgamuwa (Mee Oya) | 0.61 | 🟢 Normal | -0.010 |  |
| 2026-10-20 12:01:00 | Nawalapitiya (Mahaweli Ganga) | 1.23 | 🟢 Normal | -0.010 |  |
| 2026-10-20 12:01:52 | Thaldena (Mahaweli Ganga) | 0.31 | 🟢 Normal | -0.010 |  |
| 2026-10-20 12:01:36 | Pitabeddara (Nilwala Ganga) | 1.48 | 🟢 Normal | -0.010 |  |
| 2026-10-20 12:00:53 | Siyambalanduwa (Heda Oya) | 0.58 | 🟢 Normal | -0.010 |  |
| 2026-10-20 12:05:03 | Thawalama (Gin Ganga) | 2.16 | 🟢 Normal | -0.010 |  |
| 2026-10-20 12:07:47 | Urawa (Nilwala Ganga) | 0.85 | 🟢 Normal | -0.011 |  |
| 2026-10-20 12:01:36 | Weraganthota (Mahaweli Ganga) | -2.52 | 🟢 Normal | -0.012 |  |
| 2026-10-20 12:01:05 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | -0.015 |  |
| 2026-10-20 12:02:59 | Panadugama (Nilwala Ganga) | 4.57 | 🟢 Normal | -0.020 |  |
| 2026-10-20 12:03:44 | Horowpothana (Yan Oya) | 2.14 | 🟢 Normal | -0.020 |  |
| 2026-10-20 12:02:25 | Wellawaya (Kirindi Oya) | 1.31 | 🟢 Normal | -0.020 |  |
| 2026-10-20 12:01:37 | Dunamale (Aththanagalu Oya) | 1.92 | 🟢 Normal | -0.020 |  |
| 2026-10-20 12:02:59 | Baddegama (Gin Ganga) | 1.94 | 🟢 Normal | -0.021 |  |
| 2026-10-20 12:02:26 | Hanwella (Kelani Ganga) | 2.82 | 🟢 Normal | -0.041 |  |
| 2026-10-20 12:05:04 | Rathnapura (Kalu Ganga) | 2.23 | 🟢 Normal | -0.045 |  |
| 2026-10-20 12:04:36 | Nakkala (Kumbukkan Oya) | 0.93 | 🟢 Normal | -0.047 |  |
| 2026-10-20 12:01:29 | Ellagawa (Kalu Ganga) | 6.27 | 🟢 Normal | -0.051 |  |
| 2026-10-20 12:03:44 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.23 | 🟢 Normal | -0.063 |  |
| 2026-10-20 12:10:52 | Kithulgala (Kelani Ganga) | 2.04 | 🟢 Normal | -0.075 |  |
| 2026-10-20 12:02:34 | Thanamalwila (Kirindi Oya) | 1.30 | 🟢 Normal | -0.720 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)